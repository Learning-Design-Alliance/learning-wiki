---
type: claim
title: "BERT outperforms other models once trained on about 20 to 30% of the training data, with all performance curves flattening as training size increases"
description: "BERT outperforms other models once trained on about 20 to 30% of the training data, with all performance curves flattening as training size increases"
id: bert-outperforms-at-20-30-percent-training-data
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: wulff-2023
    resource: "https://doi.org/10.1007/s40593-022-00290-6"
    title: "Wulff, P., Mientus, L., Nowak, A., & Borowski, A. (2023). Utilizing a Pretrained Language Model (BERT) to Classify Preservice Physics Teachers' Written Reflections. International Journal of Artificial Intelligence in Education, 33, 439–466. https://doi.org/10.1007/s40593-022-00290-6"
    author: "Wulff, P., Mientus, L., Nowak, A., & Borowski, A."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# BERT outperforms other models once trained on about 20 to 30% of the training data, with all performance curves flattening as training size increases

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` BERT with non-random word-order performs lower than FFNN and LSTM for smaller training data sizes but outperforms all other models at about 20 to 30% of the training data. [→ Wulff 2023](#wulff-2023)

## Evidence

### Wulff 2023

Wulff, P., Mientus, L., Nowak, A., & Borowski, A. (2023). Utilizing a Pretrained Language Model (BERT) to Classify Preservice Physics Teachers' Written Reflections. International Journal of Artificial Intelligence in Education, 33, 439–466. https://doi.org/10.1007/s40593-022-00290-6

`q2 · i?` · `design · r2`

Sensitivity analysis varied training data proportions from 0.05 to 1.00 with single random draws, assessing performance on the test dataset using the most performant RQ1 models. Results shown in Fig. 2 indicate BERT "outperforms all other models at about 20 to 30%" of training data.

> "Figure 2 indicates that BERT with non-random word-order performs lower for smaller training data sizes compared to FFNN and LSTM, but outperforms all other models at about 20 to 30% of the size of the entire training data."

## Discussion


## Related Claims
- [Fine-tuned BERT outperforms FFNN and LSTM deep learning architectures for classifying segments of written reflections, with weighted F1 average of .82](bert-outperforms-ffnn-lstm-reflective-writing-classification.md) — related
