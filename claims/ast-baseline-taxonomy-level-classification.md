---
type: claim
title: An AST-only structural classifier substantially exceeds random baseline accuracy in predicting CogTax levels, with L1–L3 mutually confused and L4 perfectly precise
description: An AST-only structural classifier substantially exceeds random baseline accuracy in predicting CogTax levels, with L1–L3 mutually confused and L4 perfectly precise
id: ast-baseline-taxonomy-level-classification
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: alonso-carracedo-2026
    resource: "https://arxiv.org/abs/2607.00140"
    title: "Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., & Otero-Cerdeira, L. (2026). CogTax: A Four-Level Cognitive Taxonomy for Command-Line Computing Education. arXiv. https://arxiv.org/abs/2607.00140"
    author: "Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., & Otero-Cerdeira, L."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# An AST-only structural classifier substantially exceeds random baseline accuracy in predicting CogTax levels, with L1–L3 mutually confused and L4 perfectly precise

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` A LinearSVC trained on AST structural features achieves 0.6632±0.0421 cross-validation accuracy and 0.6689±0.0444 macro-F1 on the 585-command dataset, well above the 0.25 random baseline, with Levels 1–3 mutually confused and L4 achieving perfect precision. [→ Alonso-Carracedo 2026](#alonso-carracedo-2026)

## Evidence

### Alonso-Carracedo 2026

Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., & Otero-Cerdeira, L. (2026). CogTax: A Four-Level Cognitive Taxonomy for Command-Line Computing Education. arXiv. https://arxiv.org/abs/2607.00140

`q2 · i?` · `design · r2`

Cross-validation evaluation of a LinearSVC on AST features over the complete 585-command dataset, reported in the results section. The article reports "0.6632±0.0421cross-validation accuracy" and 0.6689±0.0444 macro-F1, versus a 0.25 random baseline; the confusion matrix shows L4 with perfect precision and L3 with the lowest recall (0.44).

> "The AST-only baseline achieves0.6632±0.0421cross-validation accuracy and0.6689± 0.0444macro-F1 on the complete 585-command dataset. This performance substantially exceeds both the random baseline (0.25 for balanced four-class classification)"

## Discussion


## Related Claims
- [A combined AST-plus-embedding classifier achieves 89% accuracy assigning CogTax levels to 585 expert-annotated Linux/bash commands, outperforming either representation alone](combined-ast-embedding-classifier-89-accuracy.md) — related
- [All three trained classifiers outperformed the zero-rule baseline (28.4% accuracy) for classifying cognitive engagement in discussion posts](classifiers-beat-zero-rule-baseline-engagement.md) — related
- [Taxonomy level is defined as the maximum of cognitive complexity and operational impact, ensuring monotone coverage of both dimensions](cogtax-max-rule-monotone-coverage.md) — related
