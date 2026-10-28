---
type: claim
title: Reducing BERT to a single encoder layer (BERT (1)) decreases classification performance by .05 points in weighted F1 average compared to the full 12-layer model
description: Reducing BERT to a single encoder layer (BERT (1)) decreases classification performance by .05 points in weighted F1 average compared to the full 12-layer model
id: bert-encoder-layer-count-affects-classification-performance
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
---

# Reducing BERT to a single encoder layer (BERT (1)) decreases classification performance by .05 points in weighted F1 average compared to the full 12-layer model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` BERT (1), with 11 of BERT's 12 encoder layers deleted, performed .05 points lower than full BERT in weighted F1 average on validation data. [→ Wulff 2023](#wulff-2023)

## Evidence

### Wulff 2023

Wulff, P., Mientus, L., Nowak, A., & Borowski, A. (2023). Utilizing a Pretrained Language Model (BERT) to Classify Preservice Physics Teachers' Written Reflections. International Journal of Artificial Intelligence in Education, 33, 439–466. https://doi.org/10.1007/s40593-022-00290-6

`q2 · i?` · `design · r2`

A reduced BERT model with only one encoder layer was fitted to assess the importance of architecture depth. "BERT (1) performed .05 points lower compared to BERT in weighted F1 average" on the validation dataset.

> "Furthermore, BERT (1) performed .05 points lower compared to BERT in weighted F1 average."

## Discussion


## Related Claims
- [Fine-tuned BERT outperforms FFNN and LSTM deep learning architectures for classifying segments of written reflections, with weighted F1 average of .82](bert-outperforms-ffnn-lstm-reflective-writing-classification.md) — related
- [For transformer models, oversampling and backtranslation augmentation improve performance while freezing the encoder substantially decreases it](transformer-ablation-oversampling-freezing.md) — related
- [Hungarian transformer models achieve slightly lower overall score (about 68%) but better minority-class sensitivity than shallow models](transformers-better-minority-class-sensitivity.md) — related
- [T-tests show no significant shallow-vs-transformer difference in accuracy, weighted F1 or macro-F1, but a significant ROC-AUC advantage for the shallow model](ttest-roc-auc-advantage-shallow.md) — related
