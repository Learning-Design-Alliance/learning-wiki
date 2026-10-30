---
type: claim
title: "F1@K decreased as K increased for all methods"
description: "F1@K decreased as K increased for all methods"
id: f1-decreases-with-k
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: olatinwo-2025
    resource: "https://doi.org/10.1007/s40593-024-00441-x"
    title: "Olatinwo, S. O., & Demmans Epp, C. (2025). Predicting Tags for Learner Questions on Stack Overflow. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00441-x"
    author: "Olatinwo, S. O., & Demmans Epp, C."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# F1@K decreased as K increased for all methods

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` F1@K scores declined as K increased from 1 to 5 for every method evaluated, a pattern the authors attribute to the difficulty of predicting all tags correctly as the number of predicted tags grows. [→ Olatinwo 2025](#olatinwo-2025)

## Evidence

### Olatinwo 2025

Olatinwo, S. O., & Demmans Epp, C. (2025). Predicting Tags for Learner Questions on Stack Overflow. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00441-x

`q2 · i?` · `design · r2`

Cross-validation results across all six models show F1@K declining with K. The article calls this "a common phenomenon observed in multi-label tasks" and attributes it to the growing difficulty of predicting all tags correctly.

> "It is worth noting that the F1@K score decreased as K increased for all methods. This is a common phenomenon observed in multi-label tasks (Xu et al., 2021; Zhou et al., 2019; He et al., 2022), where it can be challenging for a model to predict all tags correctly as the number of predicted tags increases, leading to a decrease in the F1@K score."

## Discussion


## Related Claims
- [BERT-CBA outperformed baseline tag recommendation methods on Precision@K, Recall@K, and F1@K under cross-validation](bert-cba-outperforms-baselines-cross-validation.md) — related
