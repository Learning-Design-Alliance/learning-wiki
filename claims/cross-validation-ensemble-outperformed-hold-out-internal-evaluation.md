---
type: claim
title: Cross-validated ensemble models performed better on the test set than hold-out models on internal evaluation, suggesting cross-validation leverages data more effectively
description: Cross-validated ensemble models performed better on the test set than hold-out models on internal evaluation, suggesting cross-validation leverages data more effectively
id: cross-validation-ensemble-outperformed-hold-out-internal-evaluation
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

# Cross-validated ensemble models performed better on the test set than hold-out models on internal evaluation, suggesting cross-validation leverages data more effectively

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Models achieved higher QWK on the NAEP test set (mean 0.945) than on internal out-of-fold evaluation (mean 0.899), which the authors attribute to the ensemble leveraging the full dataset through cross-validation. [→ Morris 2025](#morris-2025)

## Evidence

### Morris 2025

Morris, W., Holmes, L., Choi, J. S., & Crossley, S. (2025). Automated Scoring of Constructed Response Items in Math Assessment Using Large Language Models. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00418-w

`q2 · i?` · `design · r2`

The article reports that "Our models were more accurate in the test set (mean QWK = 0.945) than in the training dataset (mean QWK = 0.899)." The authors attribute this to the ensemble of five cross-validated models leveraging the full dataset, while individual internal evaluation models each used only 80% of training data.

> "Our models were more accurate in the test set (mean QWK = 0.945) than in the training dataset (mean QWK = 0.899)."

## Discussion


## Related Claims
- [Finetuned DeBERTa-v3-large models achieved human-like agreement on nine of ten NAEP math constructed response items in the held-out test set](deberta-human-like-agreement-nine-of-ten-naep-math-items.md) — related
- [A Soft-Voting Ensemble achieves the best behavioral-dataset attrition prediction (CV F1 = 0.737, test recall = 0.769)](soft-voting-ensemble-behavioral-attrition-f1.md) — related
