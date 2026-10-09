---
type: claim
title: "Random-forest models trained on a prior semester showed significantly lower AUC when tested on a new semester's data without retraining"
description: "Random-forest models trained on a prior semester showed significantly lower AUC when tested on a new semester's data without retraining"
id: cross-semester-auc-decline-without-retraining
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: wei-dai-2025
    resource: "https://doi.org/10.18608/jla.2025.8735"
    title: "Wei Dai, Jionghao Lin, Flora Ji-Yoon Jin, Yi-Shan Tsai, Namrata Srivastava, Pierre Le Bodic, Dragan Gašević, and Guanliang Chen. (2025). Learning Analytics for Early Identification of At-Risk Students and Feedback Intervention. Journal of Learning Analytics, 12(3), 102–125. https://doi.org/10.18608/jla.2025.8735"
    author: Wei Dai, Jionghao Lin, Flora Ji-Yoon Jin, Yi-Shan Tsai, Namrata Srivastava, Pierre Le Bodic, Dragan Gašević, and Guanliang Chen
    q: 2
    i: 3
    kind: causal
    rigour: 1
  - id: wei-dai-2025-2
    resource: "https://doi.org/10.18608/jla.2025.8735"
    title: "Wei Dai, Jionghao Lin, Flora Ji-Yoon Jin, Yi-Shan Tsai, Namrata Srivastava, Pierre Le Bodic, Dragan Gašević, and Guanliang Chen. (2025). Learning Analytics for Early Identification of At-Risk Students and Feedback Intervention. Journal of Learning Analytics, 12(3), 102–125. https://doi.org/10.18608/jla.2025.8735"
    author: Wei Dai, Jionghao Lin, Flora Ji-Yoon Jin, Yi-Shan Tsai, Namrata Srivastava, Pierre Le Bodic, Dragan Gašević, and Guanliang Chen
    q: 2
    i: 3
    kind: design
    rigour: 2
---

# Random-forest models trained on a prior semester showed significantly lower AUC when tested on a new semester's data without retraining

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2` · `i3` large

## Subclaims
`q2 i3` Model 2 (0–4), trained on the source semester and tested on the target semester, achieved significantly lower AUC (0.72) than Model 1 (0–4) (0.98) and Model 3 (0–4) (0.96), with ANOVA F = 826.63 and eta squared 0.99. [→ Wei Dai 2025](#wei-dai-2025)
`q2 i3` The same pattern held for week 0–7 models: Model 2 (0–7) AUC 0.78 versus 0.98 (Model 1) and 0.96 (Model 3), F = 820.53, eta squared 0.99. [→ Wei Dai 2025 (2)](#wei-dai-2025-2)

## Evidence

### Wei Dai 2025

Wei Dai, Jionghao Lin, Flora Ji-Yoon Jin, Yi-Shan Tsai, Namrata Srivastava, Pierre Le Bodic, Dragan Gašević, and Guanliang Chen. (2025). Learning Analytics for Early Identification of At-Risk Students and Feedback Intervention. Journal of Learning Analytics, 12(3), 102–125. https://doi.org/10.18608/jla.2025.8735

`q2 · i3` · `causal · r1`

Post-hoc five-fold cross-validated evaluation of week 0–4 random-forest models (Table 3): "AUC score0.98 0.72 0.96" for Model 1 (source–source), Model 2 (source–target), and Model 3 (target–target); ANOVA F = 826.63, p = 1.40e-13, η² = 0.99.

> "AUC score0.98 0.72 0.96 826.63 1.40e-13 0.99"

### Wei Dai 2025 (2)

Wei Dai, Jionghao Lin, Flora Ji-Yoon Jin, Yi-Shan Tsai, Namrata Srivastava, Pierre Le Bodic, Dragan Gašević, and Guanliang Chen. (2025). Learning Analytics for Early Identification of At-Risk Students and Feedback Intervention. Journal of Learning Analytics, 12(3), 102–125. https://doi.org/10.18608/jla.2025.8735

`q2 · i3` · `design · r2`

Parallel week 0–7 evaluation (Table 4): "AUC score0.98 0.78 0.96" for Model 1 (0–7), Model 2 (0–7), and Model 3 (0–7); ANOVA F = 820.53, p = 1.46e-13, η² = 0.99.

> "AUC score0.98 0.78 0.96 820.53 1.46e-13 0.99"

## Discussion


## Related Claims
- [Predictive models trained on one semester's offering of a course identified at-risk students in the subsequent semester with high prediction accuracy](cross-semester-at-risk-prediction-high-accuracy.md) — reports the opposite
