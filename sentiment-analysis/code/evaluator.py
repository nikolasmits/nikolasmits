"""
evaluator.py
------------
Shared evaluation utilities used by all four models.

Metrics computed:
  - Accuracy   : fraction of correct predictions
  - F1 Score   : harmonic mean of precision and recall (binary)
  - ROC-AUC    : area under the ROC curve (requires probabilities)

Also saves a confusion matrix plot to disk for each model.

Using the same evaluator for all four models ensures the comparison
is fair — all models are measured with identical code.
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')   # non-interactive backend — saves to file, no display
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    roc_auc_score
)


def evaluate(y_true, y_pred, model_name, plots_dir="plots", y_score=None):
    """
    Compute and print accuracy, F1, and optionally ROC-AUC.
    Save confusion matrix plot to disk.

    Parameters
    ----------
    y_true      : list or array of true labels (0 or 1)
    y_pred      : list or array of hard predicted labels (0 or 1)
    model_name  : string — used in print output and plot filename
    plots_dir   : folder where plot is saved (default "plots")
    y_score     : optional array of positive-class probabilities
                  if provided, ROC-AUC is computed
                  if None, ROC-AUC is skipped

    Returns
    -------
    accuracy : float
    f1       : float
    auc      : float or None
    """

    # ------------------------------------------------------------------
    # Compute metrics
    # ------------------------------------------------------------------

    # accuracy_score: fraction of y_pred that matches y_true
    accuracy = accuracy_score(y_true, y_pred)

    # f1_score: harmonic mean of precision and recall
    # average='binary' is correct for our 2-class (0/1) problem
    f1 = f1_score(y_true, y_pred, average='binary')

    # ROC-AUC requires probabilities, not just hard labels
    # It measures the quality of the probability estimates
    # by checking how well the model ranks positives above negatives
    auc = None
    if y_score is not None:
        auc = roc_auc_score(y_true, y_score)

    # ------------------------------------------------------------------
    # Print results
    # ------------------------------------------------------------------
    print(f"\n  [{model_name}] Results:")
    print(f"    Accuracy : {accuracy:.4f}  ({accuracy * 100:.2f}%)")
    print(f"    F1 Score : {f1:.4f}")
    if auc is not None:
        print(f"    ROC-AUC  : {auc:.4f}")

    # ------------------------------------------------------------------
    # Save confusion matrix plot
    # ------------------------------------------------------------------
    os.makedirs(plots_dir, exist_ok=True)

    # confusion_matrix produces a 2x2 table:
    #              Predicted NEG  Predicted POS
    # Actual NEG  [  TN         ,  FP          ]
    # Actual POS  [  FN         ,  TP          ]
    cm      = confusion_matrix(y_true, y_pred)
    display = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=["Negative", "Positive"]
    )

    fig, ax = plt.subplots(figsize=(5, 4))
    display.plot(ax=ax, colorbar=False)
    ax.set_title(f"Confusion Matrix — {model_name}")
    plt.tight_layout()

    # Build a safe filename from the model name
    safe_name = model_name.lower().replace(' ', '_')
    filename  = os.path.join(plots_dir, f"confusion_{safe_name}.png")

    plt.savefig(filename)
    plt.close()   # close figure to free memory between models
    print(f"    Confusion matrix saved -> {filename}")

    return accuracy, f1, auc
