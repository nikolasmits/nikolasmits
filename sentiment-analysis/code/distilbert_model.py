import time
import random
import numpy as np
import torch
from torch.utils.data import DataLoader, Dataset
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification


class TextDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_len=128):
        self.encodings = tokenizer(
            texts,
            truncation=True,
            padding=True,
            max_length=max_len
        )
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        item = {}
        for key in self.encodings:
            item[key] = torch.tensor(self.encodings[key][idx], dtype=torch.long)
        item["labels"] = torch.tensor(self.labels[idx], dtype=torch.long)
        return item


def train_distilbert(
    train_texts,
    train_labels,
    val_texts,
    val_labels,
    seed=42,
    batch_size=8,
    lr=2e-5,
    num_epochs=3,
    max_len=128
):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    start_time = time.time()

    print("\n[Model 4 — DistilBERT (fine-tuned)]")
    print("  Loading tokenizer and model...")

    tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-base-uncased")

    train_dataset = TextDataset(train_texts, train_labels, tokenizer, max_len=max_len)
    val_dataset = TextDataset(val_texts, val_labels, tokenizer, max_len=max_len)

    generator = torch.Generator()
    generator.manual_seed(seed)

    train_loader = DataLoader(
        train_dataset,
        batch_size=batch_size,
        shuffle=True,
        generator=generator
    )

    val_loader = DataLoader(
        val_dataset,
        batch_size=batch_size,
        shuffle=False
    )

    model = DistilBertForSequenceClassification.from_pretrained(
        "distilbert-base-uncased",
        num_labels=2
    )

    model.to(device)

    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    best_val_acc = 0.0
    best_state = None
    patience = 2
    patience_counter = 0

    print("  Fine-tuning full model...")
    for epoch in range(num_epochs):
        model.train()
        total_loss = 0.0

        for batch in train_loader:
            batch = {k: v.to(device) for k, v in batch.items()}

            outputs = model(**batch)
            loss = outputs.loss

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        model.eval()
        correct = 0
        total = 0

        with torch.no_grad():
            for batch in val_loader:
                batch = {k: v.to(device) for k, v in batch.items()}

                outputs = model(**batch)
                preds = torch.argmax(outputs.logits, dim=1)

                correct += (preds == batch["labels"]).sum().item()
                total += batch["labels"].size(0)

        avg_loss = total_loss / len(train_loader)
        val_acc = correct / total

        print(f"  Epoch {epoch+1:02d} | Loss: {avg_loss:.4f} | Val Acc: {val_acc:.4f}")

        if val_acc > best_val_acc:
            best_val_acc = val_acc
            best_state = {k: v.detach().cpu().clone() for k, v in model.state_dict().items()}
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

    return model, tokenizer, train_time


def predict_distilbert(model, tokenizer, texts, max_len=128):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    dataset = TextDataset(texts, [0] * len(texts), tokenizer, max_len=max_len)
    loader = DataLoader(dataset, batch_size=32, shuffle=False)

    model.eval()
    model.to(device)

    preds_all = []
    probs_all = []

    with torch.no_grad():
        for batch in loader:
            batch = {k: v.to(device) for k, v in batch.items()}

            outputs = model(**batch)
            probs = torch.softmax(outputs.logits, dim=1)
            preds = torch.argmax(outputs.logits, dim=1)

            preds_all.extend(preds.cpu().numpy())
            probs_all.extend(probs[:, 1].cpu().numpy())

    return np.array(preds_all), np.array(probs_all)
