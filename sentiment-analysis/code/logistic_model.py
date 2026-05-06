"""
logistic_model.py
-----------------
Model 1: Logistic Regression with TF-IDF features.

PyTorch-style implementation with an explicit training loop.

Lecture connection (Log-linear Models lecture):
  - TF-IDF = feature extraction (text -> sparse vector)
  - Logistic Regression = log-linear model
  - BCEWithLogitsLoss = binary cross-entropy, equivalent to
    maximising the log-likelihood of the labels
  - L2 regularisation (weight_decay) prevents overfitting

What this model does:
  1. TF-IDF vectoriser converts each review into a vector of
     10,000 numbers (one per vocabulary word/bigram)
  2. A single linear layer + sigmoid learns which words predict
     positive vs negative sentiment
  3. Threshold at 0.5 to get a hard 0/1 prediction
"""

import time
import random
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

import torch
import torch.nn as nn
import torch.optim as optim


class LogisticRegressionTorch(nn.Module):
    """
    Binary logistic regression as a single linear layer.

    Input:  TF-IDF vector  [batch_size, input_dim]
    Output: single logit   [batch_size]

    We output one logit per example because BCEWithLogitsLoss
    applies sigmoid internally — more numerically stable than
    applying sigmoid ourselves then using BCELoss.
    """

    def __init__(self, input_dim):
        super().__init__()
        self.linear = nn.Linear(input_dim, 1)

    def forward(self, x):
        # nn.Linear gives [batch_size, 1]
        # .squeeze(1) removes trailing dim -> [batch_size]
        return self.linear(x).squeeze(1)


def train_logistic(
    train_texts,
    train_labels,
    val_texts,
    val_labels,
    max_features=10000,
    C=1.0,
    seed=42,
):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)

    print("\n[Model 1 — Logistic Regression (PyTorch)]")
    print("  Fitting TF-IDF vectoriser on training data only...")

    # ------------------------------------------------------------------
    # Step 1: TF-IDF vectorisation
    # fit_transform on training data only — learns the vocabulary here.
    # transform on val/test — applies same vocabulary (no data leakage).
    # ngram_range=(1,2): unigrams + bigrams so "not good" is one feature.
    # sublinear_tf=True: log(1+tf) dampens very frequent words.
    # ------------------------------------------------------------------
    vectorizer = TfidfVectorizer(
        max_features=max_features,
        ngram_range=(1, 2),
        sublinear_tf=True
    )

    X_train_sparse = vectorizer.fit_transform(train_texts)
    X_val_sparse   = vectorizer.transform(val_texts)

    print(f"  Vocabulary size : {len(vectorizer.vocabulary_)}")
    print(f"  Training matrix : {X_train_sparse.shape[0]} x {X_train_sparse.shape[1]}")

    # .toarray() converts scipy sparse -> dense numpy array
    # For 4000 x 10000 float32 this is ~160MB, which is fine
    X_train = torch.tensor(X_train_sparse.toarray(), dtype=torch.float32)
    X_val   = torch.tensor(X_val_sparse.toarray(),   dtype=torch.float32)

    # BCEWithLogitsLoss requires float32 targets
    y_train = torch.tensor(train_labels, dtype=torch.float32)
    y_val   = torch.tensor(val_labels,   dtype=torch.float32)

    # ------------------------------------------------------------------
    # Step 2: Model, loss, optimiser
    # ------------------------------------------------------------------
    model     = LogisticRegressionTorch(X_train.shape[1])
    criterion = nn.BCEWithLogitsLoss()

    # Correct L2 regularisation strength from sklearn's C parameter:
    # sklearn defines C = 1 / (2 * n_samples * lambda)
    # so lambda = 1 / (2 * n_samples * C)
    # With n_samples=4000, C=1.0 -> weight_decay ~ 0.000125
    n_samples    = X_train.shape[0]
    weight_decay = 1.0 / (2.0 * n_samples * C)

    # LBFGS is the same second-order optimiser sklearn uses internally.
    # It converges much faster than Adam/SGD for convex log-linear problems.
    # requires a closure function (see training loop below).
    optimizer = optim.LBFGS(
        model.parameters(),
        lr=1.0,
        max_iter=20,
        line_search_fn="strong_wolfe"
    )

    best_val_acc     = 0.0
    best_state       = None
    patience         = 5
    patience_counter = 0
    n_epochs         = 20

    print("  Training logistic regression...")
    start_time = time.time()

    for epoch in range(n_epochs):
        model.train()

        # LBFGS needs a closure: a function that recomputes the loss
        # and calls .backward() each time the optimiser requests it.
        # This is different from Adam/SGD which just call .step() directly.
        def closure():
            optimizer.zero_grad()
            logits = model(X_train)
            loss   = criterion(logits, y_train)
            # Add L2 penalty manually (equivalent to weight_decay in Adam)
            l2 = sum(torch.sum(p ** 2) for p in model.parameters())
            loss = loss + weight_decay * l2
            loss.backward()
            return loss

        train_loss = optimizer.step(closure)

        model.eval()
        with torch.no_grad():
            val_logits = model(X_val)
            val_probs  = torch.sigmoid(val_logits)
            val_preds  = (val_probs >= 0.5).long()
            val_acc    = (val_preds == y_val.long()).float().mean().item()

        print(f"  Epoch {epoch+1:02d} | Loss: {train_loss.item():.4f} | Val Acc: {val_acc:.4f}")

        if val_acc > best_val_acc:
            best_val_acc     = val_acc
            best_state       = {k: v.detach().clone() for k, v in model.state_dict().items()}
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

    return vectorizer, model, train_time


def predict_logistic(vectorizer, model, texts):
    """
    Returns (preds, probs):
      preds : numpy array of 0/1 hard predictions
      probs : numpy array of positive-class probabilities (needed for ROC-AUC)
    """
    X_sparse = vectorizer.transform(texts)
    X        = torch.tensor(X_sparse.toarray(), dtype=torch.float32)

    model.eval()
    with torch.no_grad():
        logits = model(X)
        probs  = torch.sigmoid(logits)
        preds  = (probs >= 0.5).long()

    return preds.cpu().numpy(), probs.cpu().numpy()
