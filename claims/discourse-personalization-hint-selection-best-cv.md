---
type: claim
title: "The discourse personalization hint-selection model achieves the highest cross-validated accuracy (86.71%) and F1 (84.81%), significantly above all other models"
description: "The discourse personalization hint-selection model achieves the highest cross-validated accuracy (86.71%) and F1 (84.81%), significantly above all other models"
id: discourse-personalization-hint-selection-best-cv
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2022
sources:
  - id: kochmar-2022
    resource: "https://doi.org/10.1007/s40593-021-00267-x"
    title: "Kochmar, E., Vu, D. D., Belfer, R., Gupta, V., Serban, I. V., & Pineau, J. (2022). Automated Data-Driven Generation of Personalized Pedagogical Interventions in Intelligent Tutoring Systems. International Journal of Artificial Intelligence in Education, 32, 323–349. https://doi.org/10.1007/s40593-021-00267-x"
    author: "Kochmar, E., Vu, D. D., Belfer, R., Gupta, V., Serban, I. V., & Pineau, J."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The discourse personalization hint-selection model achieves the highest cross-validated accuracy (86.71%) and F1 (84.81%), significantly above all other models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` A Random Forest hint-selection model using linguistic, performance-based, and dialogue-history features outperforms random, baseline (linguistic-only), and shallow personalization models on 50-fold cross-validation, with statistically significant improvement at a 95% confidence level. [→ Kochmar 2022](#kochmar-2022)

## Evidence

### Kochmar 2022

Kochmar, E., Vu, D. D., Belfer, R., Gupta, V., Serban, I. V., & Pineau, J. (2022). Automated Data-Driven Generation of Personalized Pedagogical Interventions in Intelligent Tutoring Systems. International Journal of Artificial Intelligence in Education, 32, 323–349. https://doi.org/10.1007/s40593-021-00267-x

`q2 · i?` · `design · r2`

Cross-validation study (k = 50 folds) of Random Forest hint-selection models trained on 450 recorded student–system interactions. The discourse model reached "86.71% ± 3.34% accuracy and 84.81% ± 3.97% F1 score"; the RANDOM model achieved 53.64% ± 3.99% accuracy.

> "The best performing model overall uses DISCOURSE PERSONALIZATION and achieves 86.71% ± 3.34% accuracy and 84.81% ± 3.97% F1 score, which are statistically significant improvements at a 95% confidence level over all other models."

## Discussion


## Related Claims
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — a broader claim this one bears on
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — related
