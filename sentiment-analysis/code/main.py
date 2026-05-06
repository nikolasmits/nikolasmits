"""
main.py
-------
Single entry point for the ELEC0141 DLNLP assignment.

Runs the full pipeline:
  1. Load IMDb data
  2. Train all four models
  3. Evaluate each on the held-out test set
  4. Print a comparison table
  5. Save confusion matrix plots to /plots

To run:
    python main.py
"""

import random
import numpy as np
import torch

SEED = 42
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)

from data.data_loader import load_imdb
from models.logistic_model import train_logistic, predict_logistic
from models.word2vec_mlp_model import train_word2vec_mlp, predict_word2vec_mlp
from models.lstm_model import train_lstm, predict_lstm
from models.distilbert_model import train_distilbert, predict_distilbert
from evaluation.evaluator import evaluate


def main():
    print("=" * 80)
    print("  ELEC0141 — Sentiment Classification Pipeline")
    print("=" * 80)

    train_texts, train_labels, val_texts, val_labels, test_texts, test_labels = load_imdb(
        train_size=4000,
        val_size=500,
        test_size=500,
        seed=SEED
    )

    results = []

    # ------------------------------------------------------------
    # Model 1 — Logistic Regression
    # ------------------------------------------------------------
    vectorizer, log_model, log_time = train_logistic(
        train_texts,
        train_labels,
        val_texts,
        val_labels,
        max_features=10000,
        C=1.0,
        seed=SEED
    )

    log_preds, log_probs = predict_logistic(
        vectorizer,
        log_model,
        test_texts
    )

    log_acc, log_f1, log_auc = evaluate(
        y_true=test_labels,
        y_pred=log_preds,
        y_score=log_probs,
        model_name="Logistic Regression",
        plots_dir="plots"
    )

    results.append({
        "model": "Logistic Regression",
        "acc": log_acc,
        "f1": log_f1,
        "auc": log_auc,
        "time": log_time
    })

    # ------------------------------------------------------------
    # Model 2 — Word2Vec + MLP
    # ------------------------------------------------------------
    w2v_model, w2v_embeddings, w2v_time = train_word2vec_mlp(
        train_texts,
        train_labels,
        val_texts,
        val_labels,
        seed=SEED
    )

    w2v_preds, w2v_probs = predict_word2vec_mlp(
        w2v_model,
        w2v_embeddings,
        test_texts
    )

    w2v_acc, w2v_f1, w2v_auc = evaluate(
        y_true=test_labels,
        y_pred=w2v_preds,
        y_score=w2v_probs,
        model_name="Word2Vec MLP",
        plots_dir="plots"
    )

    results.append({
        "model": "Word2Vec MLP",
        "acc": w2v_acc,
        "f1": w2v_f1,
        "auc": w2v_auc,
        "time": w2v_time
    })

    # ------------------------------------------------------------
    # Model 3 — LSTM
    # ------------------------------------------------------------
    lstm_model, lstm_vocab, lstm_max_len, lstm_time = train_lstm(
        train_texts,
        train_labels,
        val_texts,
        val_labels,
        seed=SEED,
        max_vocab_size=20000,
        min_freq=2,
        max_len=200,
        embed_dim=100,
        hidden_dim=128,
        batch_size=32,
        lr=1e-3,
        num_epochs=10
    )

    lstm_preds, lstm_probs = predict_lstm(
        lstm_model,
        lstm_vocab,
        lstm_max_len,
        test_texts
    )

    lstm_acc, lstm_f1, lstm_auc = evaluate(
        y_true=test_labels,
        y_pred=lstm_preds,
        y_score=lstm_probs,
        model_name="LSTM",
        plots_dir="plots"
    )

    results.append({
        "model": "LSTM",
        "acc": lstm_acc,
        "f1": lstm_f1,
        "auc": lstm_auc,
        "time": lstm_time
    })

    # ------------------------------------------------------------
    # Model 4 — DistilBERT
    # ------------------------------------------------------------
    bert_model, bert_tokenizer, bert_time = train_distilbert(
        train_texts,
        train_labels,
        val_texts,
        val_labels,
        seed=SEED,
        batch_size=8,
        lr=2e-5,
        num_epochs=3,
        max_len=128
    )

    bert_preds, bert_probs = predict_distilbert(
        bert_model,
        bert_tokenizer,
        test_texts,
        max_len=128
    )

    bert_acc, bert_f1, bert_auc = evaluate(
        y_true=test_labels,
        y_pred=bert_preds,
        y_score=bert_probs,
        model_name="DistilBERT",
        plots_dir="plots"
    )

    results.append({
        "model": "DistilBERT",
        "acc": bert_acc,
        "f1": bert_f1,
        "auc": bert_auc,
        "time": bert_time
    })

    # ------------------------------------------------------------
    # Results summary
    # ------------------------------------------------------------
    print("\n" + "=" * 80)
    print("  RESULTS SUMMARY")
    print("=" * 80)
    print(f"  {'Model':<28} {'Accuracy':>10}  {'F1':>8}  {'AUC':>8}  {'Time':>10}")
    print("  " + "-" * 74)

    for row in results:
        auc_value = row["auc"] if row["auc"] is not None else float("nan")
        print(
            f"  {row['model']:<28} "
            f"{row['acc']:>10.4f}  "
            f"{row['f1']:>8.4f}  "
            f"{auc_value:>8.4f}  "
            f"{row['time']:>8.2f}s"
        )

    print("=" * 80)
    print("  All plots saved to /plots directory.")
    print()


if __name__ == "__main__":
    main()
