---
type: claim
title: Taxonomy level is defined as the maximum of cognitive complexity and operational impact, ensuring monotone coverage of both dimensions
description: Taxonomy level is defined as the maximum of cognitive complexity and operational impact, ensuring monotone coverage of both dimensions
id: cogtax-max-rule-monotone-coverage
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: alonso-carracedo-2026
    resource: "https://arxiv.org/abs/2607.00140"
    title: "Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., & Otero-Cerdeira, L. (2026). CogTax: A Four-Level Cognitive Taxonomy for Command-Line Computing Education. arXiv. https://arxiv.org/abs/2607.00140"
    author: "Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., & Otero-Cerdeira, L."
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Taxonomy level is defined as the maximum of cognitive complexity and operational impact, ensuring monotone coverage of both dimensions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`

## Subclaims
`q1 i?` CogTax defines a command's level as L = max(C, O), so a command at level L requires at least level-L understanding or produces at least level-L effects, but not necessarily both. [→ Alonso-Carracedo 2026](#alonso-carracedo-2026)

## Evidence

### Alonso-Carracedo 2026

Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., & Otero-Cerdeira, L. (2026). CogTax: A Four-Level Cognitive Taxonomy for Command-Line Computing Education. arXiv. https://arxiv.org/abs/2607.00140

`q1 · i?` · `design · r2`

Definitional statement of the taxonomy's combination rule in the methodology section. The article presents the maximum rule as ensuring "monotonecoverage" so that conceptual mastery alone is insufficient if operational awareness is absent, and conversely. No empirical test of the rule itself is reported in the available text.

> "The taxonomy level of a given command is defined by Equation (1). This formula ensures monotonecoverage: acommandat levelLrequiresat leastlevel-Lunderstanding orproduces"

## Discussion


## Related Claims
- [An AST-only structural classifier substantially exceeds random baseline accuracy in predicting CogTax levels, with L1–L3 mutually confused and L4 perfectly precise](ast-baseline-taxonomy-level-classification.md) — related
- [A combined AST-plus-embedding classifier achieves 89% accuracy assigning CogTax levels to 585 expert-annotated Linux/bash commands, outperforming either representation alone](combined-ast-embedding-classifier-89-accuracy.md) — related
