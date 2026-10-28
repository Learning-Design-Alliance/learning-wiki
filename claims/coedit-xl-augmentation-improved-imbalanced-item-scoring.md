---
type: claim
title: Data augmentation with Coedit-XL paraphrasing and targeted filtering improved model performance on imbalanced items
description: Data augmentation with Coedit-XL paraphrasing and targeted filtering improved model performance on imbalanced items
id: coedit-xl-augmentation-improved-imbalanced-item-scoring
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: morris-2025
    resource: "https://doi.org/10.1007/s40593-024-00418-w"
    title: "Morris, W., Holmes, L., Choi, J. S., & Crossley, S. (2025). Automated Scoring of Constructed Response Items in Math Assessment Using Large Language Models. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00418-w"
    author: "Morris, W., Holmes, L., Choi, J. S., & Crossley, S."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Data augmentation with Coedit-XL paraphrasing and targeted filtering improved model performance on imbalanced items

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Data augmentation using Coedit-XL paraphrasing and targeted filtering of over-represented classes improved scoring model performance on items with imbalanced score distributions. [→ Morris 2025](#morris-2025)

## Evidence

### Morris 2025

Morris, W., Holmes, L., Choi, J. S., & Crossley, S. (2025). Automated Scoring of Constructed Response Items in Math Assessment Using Large Language Models. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00418-w

`q2 · i?` · `design · r2`

The article reports that for items with imbalanced score distributions, "Data augmentation and filters helped balance out the data and improved the model performance to some extent." Augmentation used Grammarly's Coedit-XL model to paraphrase high-scoring responses, with injected spelling errors and lowercasing to mimic authentic student writing.

> "Data augmentation and filters helped balance out the data and improved the model performance to some extent."

## Discussion


## Related Claims
- [Class balance and score distribution matter more than overall sample size for training accurate scoring models](class-balance-more-important-than-sample-size.md) — related
- [Data augmentation was critical for ordinal discriminability, with QWK dropping to near-zero without it in the Focus dimension and gains up to +0.346 in severely imbalanced dimensions](augmentation-critical-ordinal-qwk-gains.md) — a narrower finding that bears on this claim
- [In the Overview dimension, augmentation produced a marginal QWK decrease (ΔQWK = −0.006) despite improving macro-F1, the only dimension with this trade-off](overview-augmentation-qwk-tradeoff.md) — a narrower finding that bears on this claim
- [SGD classifiers on document-term matrices outperformed explicit linguistic-feature filters for removing low-scoring responses](sgd-classifier-filtering-outperformed-linguistic-features.md) — a narrower finding that bears on this claim
