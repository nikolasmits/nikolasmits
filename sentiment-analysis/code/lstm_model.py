"""
lstm_model.py
-------------
Model 3: LSTM sequence classifier.

Lab style reference (elec0141_lab_1.py section 2 — SequenceClassifierLSTM):
  - WordClassifierLSTM class name matches the lab
  - Same five constructor arguments as the lab LSTM
  - nn.Embedding -> nn.LSTM -> nn.Linear pipeline
  - batch_first=True
  - Uses hidden_state (not LSTM output) for sequence classification
    as specified in lab section 3.2

Lecture connection (RNN/LSTM lecture):
  - LSTM gates (forget, input, output) allow selective memory
  - Hidden state h_t accumulates context from the full sequence
  - Using h_n (final hidden state) for classification means the
    model's decision is based on having read the entire review

What this model does:
  1. Build vocabulary from training data only
  2. Encode each review as a sequence of integer token indices
  3. Pad/truncate to max_len for batching
  4. Embedding layer maps indices to dense vectors
  5. LSTM reads the sequence and produces a hidden state
  6. Final hidden state -> Linear -> 2 class logits
"""

import random
import time
import re
from collections import Counter

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset


PAD_TOKEN = "<PAD>"
UNK_TOKEN = "<UNK>"


def simple_tokenize(text):
    """
    Tokenise by extracting word characters only.
    re.findall(r"\b\w+\b", text) gives cleaner tokens than split()
    because it strips punctuation attached to words (e.g. "good." -> "good").
    This matches the LSTM lab style more closely.
    """
    return re.findall(r"\b\w+\b", text.lower())


def build_vocab(texts, max_vocab_size=20000, min_freq=2):
    """
    Build a word -> integer index vocabulary from training text only.

    PAD = index 0  (must be 0 to work with padding_idx=0 in nn.Embedding)
    UNK = index 1  (all words not seen during training map here)
    Real words start at index 2.

    min_freq=2: words appearing only once are likely noise or typos.
    """
    counter = Counter()
    for text in texts:
        counter.update(simple_tokenize(text))

    vocab = {PAD_TOKEN: 0, UNK_TOKEN: 1}

    for word, freq in counter.most_common():
        if freq < min_freq:
            continue
        if len(vocab) >= max_vocab_size:
            break
        vocab[word] = len(vocab)

    return vocab


def encode_text(text, vocab, max_len):
    """
    Convert one review to a fixed-length list of token indices.

    - Truncate to max_len tokens
    - Map unknown tokens to UNK index (1)
    - Pad shorter sequences to max_len with PAD index (0)
    - Also return the true length (before padding) for accurate
      extraction of the last real hidden state
    """
    tokens = simple_tokenize(text)
    ids    = [vocab.get(tok, vocab[UNK_TOKEN]) for tok in tokens[:max_len]]
    length = len(ids)

    if len(ids) < max_len:
        ids += [vocab[PAD_TOKEN]] * (max_len - len(ids))

    # Ensure length is at least 1 to avoid indexing errors
    if length == 0:
        length = 1

    return ids, length


def encode_texts(texts, vocab, max_len):
    """
    Encode a list of reviews into:
      encoded_texts : numpy array [n_reviews, max_len]
      lengths       : numpy array [n_reviews] — true length before padding
    """
    encoded_list = []
    lengths      = []

    for text in texts:
        ids, length = encode_text(text, vocab, max_len)
        encoded_list.append(ids)
        lengths.append(length)

    return (np.array(encoded_list, dtype=np.int64),
            np.array(lengths,      dtype=np.int64))


class WordClassifierLSTM(nn.Module):
    """
    LSTM sequence classifier — named WordClassifierLSTM to match the lab.

    Architecture:
        nn.Embedding -> nn.LSTM -> nn.Linear

    Constructor arguments match the lab's SequenceClassifierLSTM exactly:
        num_hidden_layers, hidden_dim, output_dim, num_embeddings, embedding_dim

    Forward pass:
        We use the LSTM hidden state h_n at the final real token position,
        NOT x[:,-1,:] (which would always be a PAD position for short reviews).
        We index the LSTM output at lengths-1 to get the last real token's state.
        This is more accurate and directly follows the lab guidance that
        "the correct way is to use the hidden_state value" for sequence classification.
    """

    def __init__(self, num_hidden_layers, hidden_dim, output_dim,
                 num_embeddings, embedding_dim):
        super().__init__()

        # padding_idx=0: PAD embeddings are kept as zero vectors
        # and gradients through them are not computed
        self.embedding = nn.Embedding(
            num_embeddings, embedding_dim, padding_idx=0
        )

        self.lstm = nn.LSTM(
            input_size=embedding_dim,
            hidden_size=hidden_dim,
            num_layers=num_hidden_layers,
            batch_first=True
        )

        self.dense = nn.Linear(hidden_dim, output_dim)

    def forward(self, x, lengths):
        """
        x       : LongTensor [batch_size, seq_len] — token indices
        lengths : LongTensor [batch_size] — true sequence length per review

        Returns: logits [batch_size, output_dim]
        """
        # [batch_size, seq_len] -> [batch_size, seq_len, embedding_dim]
        x = self.embedding(x)

        # LSTM processes the full padded sequence
        # output: [batch_size, seq_len, hidden_dim]
        # _     : (h_n, c_n) — final hidden and cell states (unused here)
        x, _ = self.lstm(x)

        # Extract the hidden state at the last REAL token position
        # x[i, lengths[i]-1, :] = hidden state just after reading token lengths[i]
        # This avoids using a PAD position's hidden state for classification
        batch_size   = x.size(0)
        last_outputs = x[torch.arange(batch_size), lengths - 1, :]

        # Linear classifier: [batch_size, hidden_dim] -> [batch_size, output_dim]
        logits = self.dense(last_outputs)
        return logits


def train_lstm(
    train_texts,
    train_labels,
    val_texts,
    val_labels,
    seed=42,
    max_vocab_size=20000,
    min_freq=2,
    max_len=200,
    embed_dim=100,
    hidden_dim=128,
    batch_size=32,
    lr=1e-3,
    num_epochs=10
):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)

    device     = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    start_time = time.time()

    print("\n[Model 3 — LSTM]")
    print("  Building vocabulary from training data...")

    vocab = build_vocab(train_texts, max_vocab_size=max_vocab_size,
                        min_freq=min_freq)
    print(f"  Vocabulary size: {len(vocab)}")

    print("  Encoding text as integer sequences...")
    X_train, train_lengths = encode_texts(train_texts, vocab, max_len)
    X_val,   val_lengths   = encode_texts(val_texts,   vocab, max_len)

    y_train = np.array(train_labels, dtype=np.int64)
    y_val   = np.array(val_labels,   dtype=np.int64)

    # Include lengths in the dataset so forward() can extract
    # the hidden state at the correct (non-PAD) position
    train_dataset = TensorDataset(
        torch.tensor(X_train,        dtype=torch.long),
        torch.tensor(train_lengths,  dtype=torch.long),
        torch.tensor(y_train,        dtype=torch.long)
    )
    val_dataset = TensorDataset(
        torch.tensor(X_val,          dtype=torch.long),
        torch.tensor(val_lengths,    dtype=torch.long),
        torch.tensor(y_val,          dtype=torch.long)
    )

    generator = torch.Generator()
    generator.manual_seed(seed)

    train_loader = DataLoader(train_dataset, batch_size=batch_size,
                              shuffle=True, generator=generator)
    val_loader   = DataLoader(val_dataset,   batch_size=batch_size,
                              shuffle=False)

    model = WordClassifierLSTM(
        num_hidden_layers=1,
        hidden_dim=hidden_dim,
        output_dim=2,
        num_embeddings=len(vocab),
        embedding_dim=embed_dim
    ).to(device)

    # CrossEntropyLoss: takes raw logits [batch, 2] and integer labels [batch]
    # Internally applies softmax — we do NOT apply softmax in forward()
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    best_val_acc     = 0.0
    best_state       = None
    patience         = 3
    patience_counter = 0

    print("  Training LSTM...")
    for epoch in range(num_epochs):

        model.train()
        train_loss_total = 0.0

        for batch_x, batch_lengths, batch_y in train_loader:
            batch_x       = batch_x.to(device)
            batch_lengths = batch_lengths.to(device)
            batch_y       = batch_y.to(device)

            optimizer.zero_grad()
            logits = model(batch_x, batch_lengths)
            loss   = criterion(logits, batch_y)
            loss.backward()
            optimizer.step()

            train_loss_total += loss.item()

        model.eval()
        correct = 0
        total   = 0

        with torch.no_grad():
            for batch_x, batch_lengths, batch_y in val_loader:
                batch_x       = batch_x.to(device)
                batch_lengths = batch_lengths.to(device)
                batch_y       = batch_y.to(device)

                logits = model(batch_x, batch_lengths)
                preds  = torch.argmax(logits, dim=1)
                correct += (preds == batch_y).sum().item()
                total   += batch_y.size(0)

        avg_loss = train_loss_total / len(train_loader)
        val_acc  = correct / total

        print(f"  Epoch {epoch+1:02d} | Loss: {avg_loss:.4f} | Val Acc: {val_acc:.4f}")

        if val_acc > best_val_acc:
            best_val_acc     = val_acc
            best_state       = {k: v.detach().cpu().clone()
                                for k, v in model.state_dict().items()}
            patience_counter = 0
        else:
            patience_counter += 1
            if patience_counter >= patience:
                print("  Early stopping triggered.")
                break

    if best_state is not None:
        model.load_state_dict(best_state)

    train_time = time.time() - start_time
    print(f"  Training complete in {train_time:.2f}s | Best val acc: {best_val_acc:.4f}")

    return model, vocab, max_len, train_time


def predict_lstm(model, vocab, max_len, texts):
    """
    Returns (preds, probs):
      preds : numpy array of 0/1 hard predictions
      probs : numpy array of positive-class probabilities (for ROC-AUC)
    """
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    X, lengths = encode_texts(texts, vocab, max_len)

    dataset = TensorDataset(
        torch.tensor(X,       dtype=torch.long),
        torch.tensor(lengths, dtype=torch.long)
    )
    loader = DataLoader(dataset, batch_size=128, shuffle=False)

    model.eval()
    model.to(device)

    preds_all = []
    probs_all = []

    with torch.no_grad():
        for batch_x, batch_lengths in loader:
            batch_x       = batch_x.to(device)
            batch_lengths = batch_lengths.to(device)

            logits = model(batch_x, batch_lengths)
            probs  = torch.softmax(logits, dim=1)
            preds  = torch.argmax(logits, dim=1)

            preds_all.extend(preds.cpu().numpy())
            probs_all.extend(probs[:, 1].cpu().numpy())

    return np.array(preds_all), np.array(probs_all)
