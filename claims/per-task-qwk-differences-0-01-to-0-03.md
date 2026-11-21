---
type: claim
title: Per-task QWK differences between the adapter framework and fully fine-tuned models range from 0.01 to 0.03, with negligible differences on binary-label tasks
description: Per-task QWK differences between the adapter framework and fully fine-tuned models range from 0.01 to 0.03, with negligible differences on binary-label tasks
id: per-task-qwk-differences-0-01-to-0-03
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: latif-2024
    resource: "https://doi.org/10.48550/arXiv.2412.21065"
    title: "Latif, E., Zhou, Y., Fang, L., & Zhai, X. (2024). Efficient Multi-Task Inferencing with a Shared Backbone and Lightweight Task-Specific Adapters for Automatic Scoring. [doi:10.48550/arXiv.2412.21065](https://doi.org/10.48550/arXiv.2412.21065)"
    author: "Latif, E., Zhou, Y., Fang, L., & Zhai, X."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Per-task QWK differences between the adapter framework and fully fine-tuned models range from 0.01 to 0.03, with negligible differences on binary-label tasks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For individual tasks the QWK difference between the proposed framework and fully fine-tuned baselines ranges between 0.01 and 0.03, and tasks with fewer labels such as binary classification show negligible differences. [→ Latif 2024](#latif-2024)

## Evidence

### Latif 2024

Latif, E., Zhou, Y., Fang, L., & Zhai, X. (2024). Efficient Multi-Task Inferencing with a Shared Backbone and Lightweight Task-Specific Adapters for Automatic Scoring. [doi:10.48550/arXiv.2412.21065](https://doi.org/10.48550/arXiv.2412.21065)

`q2 · i?` · `design · r2`

Results section analysis of per-task QWK on selected items (e.g., S131Q02, S268Q02, S269Q01) from the 27-task evaluation; the text states "the difference in QWK ranges between 0.01 and 0.03" and notes binary tasks S268Q02 and S269Q01 show negligible differences.

> "For individual tasks, the difference in QWK ranges between 0.01 and 0.03, demonstrating that the proposed framework delivers comparable performance."

## Discussion


## Related Claims
- [A shared-backbone framework with task-specific LoRA adapters achieves average QWK of 0.848 across 27 scoring tasks versus 0.888 for fully fine-tuned models](shared-backbone-lora-qwk-0-848-vs-0-888.md) — related
