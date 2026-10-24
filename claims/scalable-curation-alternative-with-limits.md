---
type: claim
title: The framework offers a scalable alternative to manual curation, but the small dataset and label dependence limit current conclusions
description: The framework offers a scalable alternative to manual curation, but the small dataset and label dependence limit current conclusions
id: scalable-curation-alternative-with-limits
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: muntasir-hoq-2026
    resource: "https://doi.org/10.48550/arxiv.2607.05409"
    title: "Muntasir Hoq, Griffin Pitts, Zhangqi Duan, Arun Balajiee Lekshmi Narayanan, Mohammad Hassany, Andrew Lan, Peter Brusilovsky and Bita Akram. (2026). Automated Recommendation of Programming Learning Content Using Pattern-based Knowledge Components. CSEDM'26: 10th Educational Data Mining in Computer Science Education Workshop. https://arxiv.org/abs/2607.05409 [doi:10.48550/arxiv.2607.05409](https://doi.org/10.48550/arxiv.2607.05409)"
    author: Muntasir Hoq, Griffin Pitts, Zhangqi Duan, Arun Balajiee Lekshmi Narayanan, Mohammad Hassany, Andrew Lan, Peter Brusilovsky and Bita Akram
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# The framework offers a scalable alternative to manual curation, but the small dataset and label dependence limit current conclusions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q1 i?` The authors argue the pipeline can generalize to new materials with limited expert effort, while acknowledging the dataset is small (123 programs) and the pipeline uses topic labels for training. [→ Muntasir Hoq 2026](#muntasir-hoq-2026)

## Evidence

### Muntasir Hoq 2026

Muntasir Hoq, Griffin Pitts, Zhangqi Duan, Arun Balajiee Lekshmi Narayanan, Mohammad Hassany, Andrew Lan, Peter Brusilovsky and Bita Akram. (2026). Automated Recommendation of Programming Learning Content Using Pattern-based Knowledge Components. CSEDM'26: 10th Educational Data Mining in Computer Science Education Workshop. https://arxiv.org/abs/2607.05409 [doi:10.48550/arxiv.2607.05409](https://doi.org/10.48550/arxiv.2607.05409)

`q1 · i?` · `design · r2`

Authors' stated limitation in the Limitations and Future Work section. They call for expanding the dataset across course offerings, textbooks, and activity types, and for future classroom studies measuring problem-solving performance, time-to-solution, and transfer.

> "First, the dataset is small (123 programs), which may constrain both pattern-based KC discovery and evaluation sensitivity."

## Discussion


## Related Claims
- [The framework's validation is limited: structure and parameterisation were tested only on a small dataset and only for predictive accuracy](causal-assessment-framework-validation-limitations.md) — related
- [A model trained only on the 300-conversation BEA dataset plateaus at 74.84% average macro F1 due to limited data size and diversity](small-labeled-data-plateaus-evaluator.md) — related
