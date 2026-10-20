---
type: claim
title: "StructRAG achieves 89.3% question-level accuracy and 93.0% edge-level F1 on 1,650 STEM diagram questions, outperforming OCR+CV, GPT-4 graph-only, direct-image GPT-4o, and ablated variants"
description: "StructRAG achieves 89.3% question-level accuracy and 93.0% edge-level F1 on 1,650 STEM diagram questions, outperforming OCR+CV, GPT-4 graph-only, direct-image GPT-4o, and ablated variants"
id: structrag-outperforms-baselines-stem-diagrams
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: sun-y-2026
    resource: "https://doi.org/10.1186/s40561-026-00459-9"
    title: "Sun Y., Liao Y. & Ma X. (2026). Advancing diagram-based reasoning in AI tutoring systems: a structural approach for STEM education. Smart Learning Environments. https://doi.org/10.1186/s40561-026-00459-9"
    author: "Sun Y., Liao Y. & Ma X."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: sun-y-2026-2
    resource: "https://doi.org/10.1186/s40561-026-00459-9"
    title: "Sun Y., Liao Y. & Ma X. (2026). Advancing diagram-based reasoning in AI tutoring systems: a structural approach for STEM education. Smart Learning Environments. https://doi.org/10.1186/s40561-026-00459-9"
    author: "Sun Y., Liao Y. & Ma X."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# StructRAG achieves 89.3% question-level accuracy and 93.0% edge-level F1 on 1,650 STEM diagram questions, outperforming OCR+CV, GPT-4 graph-only, direct-image GPT-4o, and ablated variants

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` StructRAG reached a macro-average question-level accuracy of 89.3% and a micro-averaged edge-level F1 of 93.0%, outperforming the OCR+CV, GPT-4 graph-only, direct-image GPT-4o, and ablated baselines. [→ Sun Y. 2026](#sun-y-2026)
`q2 i?` The improvements over baselines were statistically significant at p < 0.01 under paired bootstrap tests with Holm–Bonferroni correction. [→ Sun Y. 2026 (2)](#sun-y-2026-2)

## Evidence

### Sun Y. 2026

Sun Y., Liao Y. & Ma X. (2026). Advancing diagram-based reasoning in AI tutoring systems: a structural approach for STEM education. Smart Learning Environments. https://doi.org/10.1186/s40561-026-00459-9

`q2 · i?` · `design · r2`

Quantitative evaluation of the StructRAG framework against three baselines and ablated variants on the same 1,650-question dataset, reported as "a macro-average question-level accuracy of 89.3%" and "a micro-averaged edge-level F1 score of 93.0%". No effect size is printed, so impact is null.

> "We evaluate StructRAG on a dataset of 1,650 STEM-related questions. The results show a macro-average question-level accuracy of 89.3% and a micro-averaged edge-level F1 score of 93.0%, outperforming OCR+CV, GPT-4 graph-only, direct-image GPT-4o, and ablated StructRAG variants."

### Sun Y. 2026 (2)

Sun Y., Liao Y. & Ma X. (2026). Advancing diagram-based reasoning in AI tutoring systems: a structural approach for STEM education. Smart Learning Environments. https://doi.org/10.1186/s40561-026-00459-9

`q2 · i?` · `design · r2`

Significance testing of the performance differences over the compared baselines: paired bootstrap tests with Holm–Bonferroni correction, reported as "statistically signiﬁcant at p < 0.01". Only a p-value is printed, with no effect size, so impact is null.

> "Paired bootstrap tests with Holm–Bonferroni correction indicate that these improvements are statistically signiﬁcant at p < 0.01."

## Discussion


## Related Claims
- [Current AI tutoring systems misinterpret complex STEM engineering diagrams, omitting edges, misclassifying component connections, and flattening hierarchical topologies](ai-systems-misinterpret-stem-diagrams.md) — reports the opposite
- [Multimodal input consistently improves accuracy but not F1, model size correlates moderately with performance, and reasoning models show mixed results](multimodality-size-reasoning-mixed-effects.md) — related
