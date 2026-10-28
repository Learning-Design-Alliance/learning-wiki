---
type: claim
title: BERT-FYBIO, which uses post text plus annotated reading context, significantly outperforms a Bi-LSTM baseline for emoji prediction
description: BERT-FYBIO, which uses post text plus annotated reading context, significantly outperforms a Bi-LSTM baseline for emoji prediction
id: bert-fybio-outperforms-bilstm
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: blobstein-2025
    resource: "https://doi.org/10.1007/s40593-024-00401-5"
    title: "Blobstein, A., Facciotti, M. T., Igo, M., Karger, D., Ravi, P., Sripathi, K., & Gal, K. (2025). #let's-discuss: Analyzing Students' Use of Emoji when Interacting with Course Readings. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-024-00401-5"
    author: "Blobstein, A., Facciotti, M. T., Igo, M., Karger, D., Ravi, P., Sripathi, K., & Gal, K."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# BERT-FYBIO, which uses post text plus annotated reading context, significantly outperforms a Bi-LSTM baseline for emoji prediction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The BERT model outperformed the Bi-LSTM model in precision, recall, and weighted F-1 scores by a significant margin (McNemar's test). [→ Blobstein 2025](#blobstein-2025)

## Evidence

### Blobstein 2025

Blobstein, A., Facciotti, M. T., Igo, M., Karger, D., Ravi, P., Sripathi, K., & Gal, K. (2025). #let's-discuss: Analyzing Students' Use of Emoji when Interacting with Course Readings. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-024-00401-5

`q2 · i?` · `design · r2`

Model comparison (Table 5) of BERT-FYBIO against a five-layer Bi-LSTM architecture with word2vec pre-training, evaluated with 8-fold cross-validation on the FYBIO dataset using precision, recall, and weighted F-1. The article states "the BERT model outper- forms the Bi-LSTM model in all three metrics by a signiﬁcant margin" with the printed McNemar's test p-value. No standardized effect size is printed.

> "We can see that the BERT model outper- forms the Bi-LSTM model in all three metrics by a signiﬁcant margin (McNemar’s test, p < 1.16 · e−35)."

## Discussion


## Related Claims
- [Fine-tuned BERT outperforms FFNN and LSTM deep learning architectures for classifying segments of written reflections, with weighted F1 average of .82](bert-outperforms-ffnn-lstm-reflective-writing-classification.md) — a broader claim this one bears on
- [BERT was the best unimodal text classifier for Key Stage classification with an F1 score of 0.75](bert-best-unimodal-f1-075.md) — related
- [Most student posts in the emoji-annotated biology course contained at least one emoji, with #question and #i-think used most often](emoji-posts-majority-self-report.md) — related
