---
type: claim
title: MSE loss performed at least as well as cross-entropy loss for pseudo-regression scoring of constructed response items
description: MSE loss performed at least as well as cross-entropy loss for pseudo-regression scoring of constructed response items
id: mse-loss-at-least-as-effective-as-cross-entropy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: morris-2025
    resource: "https://doi.org/10.1007/s40593-024-00418-w"
    title: "Morris, W., Holmes, L., Choi, J. S., & Crossley, S. (2025). Automated Scoring of Constructed Response Items in Math Assessment Using Large Language Models. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00418-w"
    author: "Morris, W., Holmes, L., Choi, J. S., & Crossley, S."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# MSE loss performed at least as well as cross-entropy loss for pseudo-regression scoring of constructed response items

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Mean-squared error loss was at least as effective as cross-entropy loss for almost all items when finetuning DeBERTa-v3-large for math response scoring. [→ Morris 2025](#morris-2025)

## Evidence

### Morris 2025

Morris, W., Holmes, L., Choi, J. S., & Crossley, S. (2025). Automated Scoring of Constructed Response Items in Math Assessment Using Large Language Models. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00418-w

`q2 · i?` · `causal · r2`

The article compared MSE and CE loss functions using fivefold cross-validated DeBERTa-v3-large models. The article reports that "mean-squared error (MSE) loss was at least as effective as cross-entropy (CE) loss for almost all items as reported in Table 6 below."

> "We found that mean-squared error (MSE) loss was at least as effective as cross-entropy (CE) loss for almost all items as reported in Table 6 below."

## Discussion


## Related Claims
- [Fine-tuning LLMs and MLMs with cross-entropy loss using soft targets outperforms standard discretization and regression-head approaches on vocabulary difficulty prediction](soft-target-finetuning-beats-standard-loss-vocabulary-difficulty.md) — related
