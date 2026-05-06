import random
import time
import re

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from gensim.models import Word2Vec


PAD_TOKEN = "<PAD>"
UNK_TOKEN = "<UNK>"


def tokenize(texts):
    tokenized = []
    for text in texts:
        words = re.findall(r"\b\w+\b", text.lower())
        tokenized.append(words)
    return tokenized


def train_word2vec(tokenized_texts, vector_size=100, window=5, min_count=1, seed=42):
    print("  Training Word2Vec on training data...")

    model = Word2Vec(
        sentences=tokenized_texts,
        vector_size=vector_size,
        window=window,
        min_count=min_count,
        workers=1,
        sg=1,
        seed=seed
    )

    print(f"  Word2Vec vocabulary size: {len(model.wv)}")
    return model


def build_embedding_matrix(word_vectors):
    vector_size = word_vectors.vector_size
    vocab_size = len(word_vectors)

    embedding_matrix = np.zeros((vocab_size + 2, vector_size), dtype=np.float32)

    for i in range(vocab_size):
        embedding_matrix[i] = word_vectors.vectors[i]

    pad_idx = vocab_size
    unk_idx = vocab_size + 1

    embedding_matrix[pad_idx] = np.zeros(vector_size, dtype=np.float32)
    embedding_matrix[unk_idx] = word_vectors.vectors.mean(axis=0).astype(np.float32)

    print(f"  PAD index: {pad_idx}")
    print(f"  UNK index: {unk_idx}")

    return embedding_matrix, pad_idx, unk_idx


def encode(tokens, word_vectors, unk_idx):
    encoded = []

    for token in tokens:
        if token in word_vectors:
            encoded.append(word_vectors.get_index(token))
        else:
            encoded.append(unk_idx)

    if len(encoded) == 0:
        encoded.append(unk_idx)

    return encoded


def pad_sequences(sequences, pad_idx):
    max_len = 0
    for seq in sequences:
        if len(seq) > max_len:
            max_len = len(seq)

    padded = []
    for seq in sequences:
        new_seq = seq + [pad_idx] * (max_len - len(seq))
        padded.append(new_seq)

    return torch.tensor(padded, dtype=torch.long)


class EmbeddingMLP(nn.Module):
    def __init__(self, embedding_matrix, pad_idx, hidden_dim=128):
        super().__init__()

        self.pad_idx = pad_idx

        self.embedding = nn.Embedding.from_pretrained(
            torch.tensor(embedding_matrix, dtype=torch.float32),
            freeze=True,
            padding_idx=pad_idx
        )

        embedding_dim = embedding_matrix.shape[1]

        self.fc1 = nn.Linear(embedding_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, 2)

    def forward(self, x):
        embedded = self.embedding(x)

        mask = (x != self.pad_idx).unsqueeze(-1).float()
        embedded = embedded * mask

        lengths = mask.sum(dim=1).clamp(min=1.0)
        pooled = embedded.sum(dim=1) / lengths

        hidden = self.relu(self.fc1(pooled))
        logits = self.fc2(hidden)

        return logits


def train_word2vec_mlp(train_texts, train_labels, val_texts, val_labels, seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    start_time = time.time()

    print("\n[Model 2 — Word2Vec + Mean Pooling + MLP]")
    print("  Tokenising text...")

    tokenized_train = tokenize(train_texts)
    tokenized_val = tokenize(val_texts)

    w2v_embeddings = train_word2vec(
        tokenized_train,
        vector_size=100,
        window=5,
        min_count=1,
        seed=seed
    )

    word_vectors = w2v_embeddings.wv
    embedding_matrix, pad_idx, unk_idx = build_embedding_matrix(word_vectors)

    print("  Encoding reviews...")
    X_train_encoded = []
    for tokens in tokenized_train:
        X_train_encoded.append(encode(tokens, word_vectors, unk_idx))

    X_val_encoded = []
    for tokens in tokenized_val:
        X_val_encoded.append(encode(tokens, word_vectors, unk_idx))

    X_train = pad_sequences(X_train_encoded, pad_idx)
    X_val = pad_sequences(X_val_encoded, pad_idx)

    y_train = torch.tensor(train_labels, dtype=torch.long)
    y_val = torch.tensor(val_labels, dtype=torch.long)

    print(f"  Train tensor shape: {X_train.shape}")
    print(f"  Val tensor shape  : {X_val.shape}")

    train_dataset = TensorDataset(X_train, y_train)
    val_dataset = TensorDataset(X_val, y_val)

    generator = torch.Generator()
    generator.manual_seed(seed)

    train_loader = DataLoader(
        train_dataset,
        batch_size=64,
        shuffle=True,
        generator=generator
    )

    val_loader = DataLoader(
        val_dataset,
        batch_size=64,
        shuffle=False
    )

    w2v_model = EmbeddingMLP(
        embedding_matrix=embedding_matrix,
        pad_idx=pad_idx,
        hidden_dim=128
    ).to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(w2v_model.parameters(), lr=1e-3)

    best_val_acc = 0.0
    best_state = None
    patience = 3
    patience_counter = 0

    print("  Training MLP classifier...")
    for epoch in range(15):
        w2v_model.train()
        train_loss_total = 0.0

        for batch_x, batch_y in train_loader:
            batch_x = batch_x.to(device)
            batch_y = batch_y.to(device)

            optimizer.zero_grad()
            outputs = w2v_model(batch_x)
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()

            train_loss_total += loss.item()

        w2v_model.eval()
        correct = 0
        total = 0

        with torch.no_grad():
            for batch_x, batch_y in val_loader:
                batch_x = batch_x.to(device)
                batch_y = batch_y.to(device)

                val_outputs = w2v_model(batch_x)
                val_preds = torch.argmax(val_outputs, dim=1)

                correct += (val_preds == batch_y).sum().item()
                total += batch_y.size(0)

        avg_loss = train_loss_total / len(train_loader)
        val_acc = correct / total

        print(f"  Epoch {epoch+1:02d} | Loss: {avg_loss:.4f} | Val Acc: {val_acc:.4f}")

        if val_acc > best_val_acc:
            best_val_acc = val_acc
            best_state = {k: v.detach().cpu().clone() for k, v in w2v_model.state_dict().items()}
            patience_counter = 0
        else:
            patience_counter += 1
            if patience_counter >= patience:
                print("  Early stopping triggered.")
                break

    if best_state is not None:
        w2v_model.load_state_dict(best_state)

    train_time = time.time() - start_time
    print(f"  Training complete in {train_time:.2f}s | Best val acc: {best_val_acc:.4f}")

    return w2v_model, w2v_embeddings, train_time


def predict_word2vec_mlp(w2v_model, w2v_embeddings, texts):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    word_vectors = w2v_embeddings.wv
    embedding_matrix, pad_idx, unk_idx = build_embedding_matrix(word_vectors)

    tokenized = tokenize(texts)

    X_encoded = []
    for tokens in tokenized:
        X_encoded.append(encode(tokens, word_vectors, unk_idx))

    X = pad_sequences(X_encoded, pad_idx)

    dataset = TensorDataset(X)
    loader = DataLoader(dataset, batch_size=128, shuffle=False)

    w2v_model.eval()
    w2v_model.to(device)

    preds_all = []
    probs_all = []

    with torch.no_grad():
        for (batch_x,) in loader:
            batch_x = batch_x.to(device)

            outputs = w2v_model(batch_x)
            probs = torch.softmax(outputs, dim=1)
            preds = torch.argmax(outputs, dim=1)

            preds_all.extend(preds.cpu().numpy())
            probs_all.extend(probs[:, 1].cpu().numpy())

    return np.array(preds_all), np.array(probs_all)
