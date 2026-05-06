# Deep Learning for NLP: Sentiment Classification Under Data and Compute Constraints

## Overview
This project evaluated four sentiment-classification models of increasing architectural complexity on **binary sentiment classification of IMDb movie reviews** under constrained experimental conditions. The models compared were:

- **TF-IDF + Logistic Regression**
- **Word2Vec + Mean Pooling + MLP**
- **LSTM trained from scratch**
- **fine-tuned DistilBERT**

The aim was not simply to identify the most accurate model, but to test whether increased architectural complexity delivers proportional gains when **training data is limited to 4,000 examples** and computation is restricted to a **CPU-only environment**.

All four models were evaluated on:
- **accuracy**
- **F1 score**
- **AUC**
- and **training time**

to compare both predictive performance and computational cost.

## Project Context
This project was completed for **Deep Learning for Natural Language Processes** and focused on **binary sentiment classification** using the **IMDb movie review dataset**.

The study was designed as a controlled progression through four generations of NLP methodology:

1. **statistical feature engineering** with TF-IDF and logistic regression
2. **dense word embeddings** with Word2Vec and an MLP classifier
3. **sequential modelling** with an LSTM
4. **pre-trained contextual representations** with DistilBERT

This made it possible to compare representational assumptions under the same data and hardware constraints, rather than treating model choice as independent of resource availability. :contentReference[oaicite:2]{index=2}

## My Contribution
This appears to be an individual report, and the uploaded paper presents the work as a full end-to-end comparative NLP experiment. My contribution included:

- designing the experimental comparison across four model classes
- implementing and training each sentiment-classification model
- enforcing a shared constrained setting of **4,000 training samples** and **CPU-only training**
- evaluating all models using consistent metrics
- analysing performance in terms of both **predictive quality** and **computational efficiency**
- and interpreting why simpler models could outperform more complex neural architectures under realistic constraints. :contentReference[oaicite:3]{index=3}

## Research Question
The central research question of the project was:

**Does greater model complexity reliably improve sentiment-classification performance when both data and compute are limited?**

That question is valuable because many comparisons between NLP models are dominated by scale effects. In this project, model choice was studied under deliberately constrained conditions, which makes the results more relevant to practical deployment settings where:
- labelled data is limited
- GPU access may not be available
- and training efficiency matters. :contentReference[oaicite:4]{index=4}

## Dataset and Experimental Setup
All models were trained and evaluated on the **IMDb movie review dataset**, a standard benchmark for binary sentiment classification containing **50,000 balanced reviews** overall. Because the project specifically examined performance under constrained conditions, training was limited to:

- **4,000 training examples**
- **500 validation examples**
- **500 test examples**

A fixed random seed of **42** was used for reproducibility across data splitting, initialisation, and batching. Reviews were preprocessed by:
- removing HTML tags
- lowercasing text
- and stripping leading/trailing whitespace. :contentReference[oaicite:5]{index=5}

This setup is a strong point of the project because it makes the comparison systematic and reproducible rather than anecdotal.

## Model 1: TF-IDF with Logistic Regression

### Objective
The first model used a **TF-IDF representation** with **logistic regression** as a strong statistical NLP baseline. Each review was converted into a sparse vector of up to **10,000 features**, including both **unigrams and bigrams**. :contentReference[oaicite:6]{index=6}

### Technical Work
The TF-IDF weighting scheme was used to reward terms that are frequent within a document but relatively rare across the corpus, helping isolate locally informative sentiment vocabulary. The inclusion of **bigrams** allowed the model to capture phrases such as **“not good”**, partially addressing negation despite the absence of sequence modelling. The classifier used:
- **L2 regularisation**
- and the **LBFGS optimiser**, which is especially well suited to convex optimisation problems such as regularised logistic regression. :contentReference[oaicite:7]{index=7}

### Key Results
This model achieved the best results of all four approaches:
- **Accuracy:** 0.8640
- **F1:** 0.8528
- **AUC:** 0.9457
- **Training time:** 1.17 s :contentReference[oaicite:8]{index=8}

The report argues convincingly that this strong performance reflects a good match between the task and the model: movie-review sentiment is often driven by highly diagnostic lexical cues, which TF-IDF captures very effectively. The confusion matrix on page 10 shows:
- **235 true negatives**
- **197 true positives**
- **24 false positives**
- **44 false negatives**, indicating a strong and relatively balanced classifier. :contentReference[oaicite:9]{index=9}

## Model 2: Word2Vec + Mean Pooling + MLP

### Objective
The second model replaced sparse bag-of-words features with **dense Word2Vec embeddings**, followed by **mean pooling** and a **two-layer MLP classifier**. This was intended to test whether learned semantic representations improved performance over TF-IDF. :contentReference[oaicite:10]{index=10}

### Technical Work
Word embeddings of dimension **50** were trained from scratch on the task corpus using the **skip-gram objective** with a context window of five. To obtain a fixed-length document representation, all token embeddings in a review were averaged, and the resulting vector was passed into an MLP with:
- a hidden layer of size **128**
- **ReLU** activation
- and a two-class output layer. :contentReference[oaicite:11]{index=11}

### Key Results
The Word2Vec + MLP model achieved:
- **Accuracy:** 0.7460
- **F1:** 0.7233
- **AUC:** 0.8269
- **Training time:** 32.22 s :contentReference[oaicite:12]{index=12}

The report identifies two main limitations:
1. the Word2Vec embeddings were trained on only **4,000 reviews**, which is far too little data for reliable semantic geometry
2. **mean pooling discards word order completely**, so the model cannot distinguish phrases like *“not good”* from *“good”* once the embeddings are averaged. :contentReference[oaicite:13]{index=13}

The confusion matrix on page 10 shows:
- **207 true negatives**
- **166 true positives**
- **52 false positives**
- **75 false negatives**, suggesting the model more often missed positive sentiment than it misclassified negative reviews. :contentReference[oaicite:14]{index=14}

## Model 3: LSTM Trained from Scratch

### Objective
The third model used an **LSTM** to explicitly model text as an ordered sequence, addressing the word-order blindness of both TF-IDF and mean-pooled Word2Vec. :contentReference[oaicite:15]{index=15}

### Technical Work
Reviews were tokenised into a vocabulary of up to **20,000 tokens**, truncated or padded to **200 tokens**, and then passed through:
- an embedding layer of size **100**
- an **LSTM** with hidden size **128**
- and a linear classifier on the final hidden state. :contentReference[oaicite:16]{index=16}

The report explains the LSTM clearly in terms of:
- the **forget gate**
- **input gate**
- **output gate**
- and **cell state**

showing how it was intended to preserve and update context over time. This is one of the strongest technical sections because it connects the recurrent architecture directly to the modelling goal of capturing compositional phenomena such as negation and qualification. :contentReference[oaicite:17]{index=17}

### Key Results
The LSTM achieved the weakest predictive performance:
- **Accuracy:** 0.7000
- **F1:** 0.7012
- **AUC:** 0.7693
- **Training time:** 123.25 s :contentReference[oaicite:18]{index=18}

The report gives a strong explanation for this result: the model had to learn
- word embeddings
- sequence representations
- and gating dynamics

all from the same limited **4,000 examples**, with random initialisation and no pre-training. That made the optimisation problem much harder than for the other models. The confusion matrix on page 11 shows:
- **174 true negatives**
- **176 true positives**
- **85 false positives**
- **65 false negatives**, indicating weaker class separation and a slight bias toward positive predictions. :contentReference[oaicite:19]{index=19}

## Model 4: Fine-Tuned DistilBERT

### Objective
The final model used **DistilBERT**, a distilled transformer encoder derived from BERT, to test the effect of **pre-trained contextual representations** on the same sentiment-classification task. :contentReference[oaicite:20]{index=20}

### Technical Work
The model used:
- **WordPiece tokenisation**
- truncation to **128 subword tokens**
- a prepended **[CLS] token**
- and a linear classification head on top of the final **[CLS] hidden state**. :contentReference[oaicite:21]{index=21}

The report explains the self-attention mechanism in technical terms, showing how DistilBERT differs fundamentally from the other models by allowing every token to attend directly to every other token. It also correctly notes that DistilBERT’s advantage cannot be attributed to transformer architecture alone, since it also benefits from massive-scale pre-training on **BookCorpus** and **English Wikipedia**. :contentReference[oaicite:22]{index=22}

### Key Results
DistilBERT achieved:
- **Accuracy:** 0.8320
- **F1:** 0.8257
- **AUC:** 0.9307
- **Training time:** 3234.43 s :contentReference[oaicite:23]{index=23}

This made it the **second-best** model overall on predictive performance, but at an enormous computational cost. The report notes that training time was more than **2,700 times greater** than for logistic regression, while performance was still lower on every reported metric. The confusion matrix on page 11 shows:
- **217 true negatives**
- **199 true positives**
- **42 false positives**
- **42 false negatives**, which is the most symmetric error distribution among the four models. :contentReference[oaicite:24]{index=24}

## Comparative Results
The core comparison is summarised clearly in the report:

| Model | Accuracy | F1 | AUC | Training Time (s) |
|---|---:|---:|---:|---:|
| Logistic Regression | 0.8640 | 0.8528 | 0.9457 | 1.17 |
| Word2Vec + MLP | 0.7460 | 0.7233 | 0.8269 | 32.22 |
| LSTM | 0.7000 | 0.7012 | 0.7693 | 123.25 |
| DistilBERT | 0.8320 | 0.8257 | 0.9307 | 3234.43 | :contentReference[oaicite:25]{index=25}

One of the strongest conclusions of the project is that **greater complexity did not reliably improve performance** under these constraints. The best model was also the simplest.

## Why This Project Matters
What makes this project strong is not only the range of models, but the quality of the analysis. It demonstrates that:
- a more sophisticated architecture is not always better
- task structure matters
- data scale matters
- compute budget matters
- and strong simple baselines should be evaluated seriously before adopting more complex deep-learning systems.

For sentiment classification on IMDb reviews under low-data, CPU-only conditions, the project shows that the task is sufficiently **lexically driven** for a well-designed TF-IDF + Logistic Regression pipeline to outperform more expressive neural models. :contentReference[oaicite:26]{index=26}

## Engineering and Technical Skills Demonstrated
This project demonstrates skills in:
- **NLP model comparison under controlled constraints**
- **TF-IDF feature engineering**
- **logistic regression for text classification**
- **Word2Vec training and document embedding**
- **MLP design for classification**
- **LSTM sequence modelling**
- **transformer fine-tuning with DistilBERT**
- **experimental design and reproducibility**
- **evaluation using accuracy, F1, AUC, and training time**
- **confusion-matrix analysis**
- **critical interpretation of model complexity vs performance trade-offs**

## Repository Contents
- `README.md` – project summary
- `report/` – final NLP report
- `code/` – training and evaluation scripts for all four models
- `figures/` – pipeline diagram, performance plots, and confusion matrices
