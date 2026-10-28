---
type: claim
title: Fine-tuned BERT outperforms FFNN and LSTM deep learning architectures for classifying segments of written reflections, with weighted F1 average of .82
description: Fine-tuned BERT outperforms FFNN and LSTM deep learning architectures for classifying segments of written reflections, with weighted F1 average of .82
id: bert-outperforms-ffnn-lstm-reflective-writing-classification
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2023
sources:
  - id: wulff-2023
    resource: "https://doi.org/10.1007/s40593-022-00290-6"
    title: "Wulff, P., Mientus, L., Nowak, A., & Borowski, A. (2023). Utilizing a Pretrained Language Model (BERT) to Classify Preservice Physics Teachers' Written Reflections. International Journal of Artificial Intelligence in Education, 33, 439–466. https://doi.org/10.1007/s40593-022-00290-6"
    author: "Wulff, P., Mientus, L., Nowak, A., & Borowski, A."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: wulff-2023-2
    resource: "https://doi.org/10.1007/s40593-022-00290-6"
    title: "Wulff, P., Mientus, L., Nowak, A., & Borowski, A. (2023). Utilizing a Pretrained Language Model (BERT) to Classify Preservice Physics Teachers' Written Reflections. International Journal of Artificial Intelligence in Education, 33, 439–466. https://doi.org/10.1007/s40593-022-00290-6"
    author: "Wulff, P., Mientus, L., Nowak, A., & Borowski, A."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: wulff-2023-3
    resource: "https://doi.org/10.1007/s40593-022-00290-6"
    title: "Wulff, P., Mientus, L., Nowak, A., & Borowski, A. (2023). Utilizing a Pretrained Language Model (BERT) to Classify Preservice Physics Teachers' Written Reflections. International Journal of Artificial Intelligence in Education, 33, 439–466. https://doi.org/10.1007/s40593-022-00290-6"
    author: "Wulff, P., Mientus, L., Nowak, A., & Borowski, A."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fine-tuned BERT outperforms FFNN and LSTM deep learning architectures for classifying segments of written reflections, with weighted F1 average of .82

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` BERT achieved the highest classification performance (weighted F1 .82) compared to FFNN (.62/.64) and LSTM (.72) models on validation data. [→ Wulff 2023](#wulff-2023)
`q2 i?` BERT maintained its advantage under iterated k-fold cross-validation (weighted F1 .81), suggesting better generalizability than FFNN models. [→ Wulff 2023 (2)](#wulff-2023-2)
`q2 i?` On held-out test data, BERT achieved a weighted F1 average of .81 and Cohen's kappa of .74. [→ Wulff 2023 (3)](#wulff-2023-3)

## Evidence

### Wulff 2023

Wulff, P., Mientus, L., Nowak, A., & Borowski, A. (2023). Utilizing a Pretrained Language Model (BERT) to Classify Preservice Physics Teachers' Written Reflections. International Journal of Artificial Intelligence in Education, 33, 439–466. https://doi.org/10.1007/s40593-022-00290-6

`q2 · i?` · `design · r2`

Grid-search-optimized models were evaluated on validation data from 270 reflections by 92 preservice physics teachers. BERT reached a "weighted F1 average of .82" while FFNNs reached .62/.64 and LSTMs .72.

> "Overall, BERT was the most performant model to classify segments in the written reflections according to the reflection-supporting model, with a weighted F1 average of .82. The Cohen's kappa values for the classification performance were: FFNN: 0.48, FFNN*: 0.48, LSTM: 0.56, LSTM*: 0.58, BERT (1): 0.66, BERT: 0.75."

### Wulff 2023 (2)

Wulff, P., Mientus, L., Nowak, A., & Borowski, A. (2023). Utilizing a Pretrained Language Model (BERT) to Classify Preservice Physics Teachers' Written Reflections. International Journal of Artificial Intelligence in Education, 33, 439–466. https://doi.org/10.1007/s40593-022-00290-6

`q2 · i?` · `design · r2`

Iterated k-fold cross-validation (ten splits, iterated ten times) confirmed BERT's advantage with smaller standard deviations than FFNN models; the authors note hold-out results are "likely inflated".

> "The weighted F1 averages (standard deviations) for iterated k-fold cross-validation were as follows: FFNN: 0.60 (0.07), FFNN*: 0.57 (0.17), LSTM: 0.71 (0.02), LSTM*: 0.71 (0.02), BERT (1): 0.76 (0.02), BERT: 0.81 (0.02)."

### Wulff 2023 (3)

Wulff, P., Mientus, L., Nowak, A., & Borowski, A. (2023). Utilizing a Pretrained Language Model (BERT) to Classify Preservice Physics Teachers' Written Reflections. International Journal of Artificial Intelligence in Education, 33, 439–466. https://doi.org/10.1007/s40593-022-00290-6

`q2 · i?` · `design · r2`

The full fine-tuned BERT model was fit to held-out test data (20% of the dataset), achieving "a weighted F1 average of .81" and Cohen's kappa of .74.

> "When fit to the test data, BERT reached a weighted F1 average of .81. The Cohen's kappa value was .74."

## Discussion


## Related Claims
- [BERT-CBA outperformed BERT-FFNN by 6–15% on Precision@K, with t(5) = 6.56, p = .001, d = 4.64](bert-cba-beats-bert-ffnn.md) — related
- [BERT-CBA outperformed BERT-LSTM by 4–9% and BERT-GRU by 2–10% on F1@K](bert-cba-beats-lstm-gru.md) — related
- [BERT-CBA outperformed baseline tag recommendation methods on Precision@K, Recall@K, and F1@K under cross-validation](bert-cba-outperforms-baselines-cross-validation.md) — related
- [Reducing BERT to a single encoder layer (BERT (1)) decreases classification performance by .05 points in weighted F1 average compared to the full 12-layer model](bert-encoder-layer-count-affects-classification-performance.md) — related
- [BERT outperforms other models once trained on about 20 to 30% of the training data, with all performance curves flattening as training size increases](bert-outperforms-at-20-30-percent-training-data.md) — related
- [BERT was the best unimodal text classifier for Key Stage classification with an F1 score of 0.75](bert-best-unimodal-f1-075.md) — related
- [NLP models in LA studies typically reach moderate agreement (mean Cohen's kappa 0.54) and mean accuracy 0.79, with deep learning models outperforming others in most studies from 2021 onward](nlp-la-performance-kappa-accuracy-benchmarks.md) — a broader claim this one bears on
- [A fine-tuned BERT model achieves almost perfect agreement with human coders when classifying student self-affirmation essays, matching human-human reliability](fine-tuned-bert-matches-human-coders-self-affirmation-essays.md) — related
