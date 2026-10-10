---
type: claim
title: "A combined AST-plus-embedding classifier achieves 89% accuracy assigning CogTax levels to 585 expert-annotated Linux/bash commands, outperforming either representation alone"
description: "A combined AST-plus-embedding classifier achieves 89% accuracy assigning CogTax levels to 585 expert-annotated Linux/bash commands, outperforming either representation alone"
id: combined-ast-embedding-classifier-89-accuracy
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

# A combined AST-plus-embedding classifier achieves 89% accuracy assigning CogTax levels to 585 expert-annotated Linux/bash commands, outperforming either representation alone

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` A classifier combining syntactic AST representations with semantic embeddings achieves 89% accuracy on 585 expert-annotated Linux/bash commands, outperforming either representation alone and demonstrating cross-language extensibility. [→ Alonso-Carracedo 2026](#alonso-carracedo-2026)

## Evidence

### Alonso-Carracedo 2026

Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., & Otero-Cerdeira, L. (2026). CogTax: A Four-Level Cognitive Taxonomy for Command-Line Computing Education. arXiv. https://arxiv.org/abs/2607.00140

`q2 · i?` · `design · r2`

Evaluation of the combined classification approach on the 585-command expert-annotated Linux/bash dataset, reported in the article's abstract as achieving "89% accuracy, outperforming either representation alone". The detailed results section was not available in the supplied text.

> "this combined approach achieves 89% accuracy, outperforming either representation alone, and demonstrates cross-language extensibility through structural equivalences across command languages."

## Discussion


## Related Claims
- [An AST-only structural classifier substantially exceeds random baseline accuracy in predicting CogTax levels, with L1–L3 mutually confused and L4 perfectly precise](ast-baseline-taxonomy-level-classification.md) — related
- [Taxonomy level is defined as the maximum of cognitive complexity and operational impact, ensuring monotone coverage of both dimensions](cogtax-max-rule-monotone-coverage.md) — related
