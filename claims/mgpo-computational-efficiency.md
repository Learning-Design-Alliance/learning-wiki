---
type: claim
title: MGPO selects planning computations in approximately 0.03 seconds, over 100 times faster than baseline methods
description: MGPO selects planning computations in approximately 0.03 seconds, over 100 times faster than baseline methods
id: mgpo-computational-efficiency
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: heindrich-2025
    resource: "https://doi.org/10.1007/s40593-025-00493-7"
    title: "Heindrich, L., Consul, S., & Lieder, F. (2025). An Intelligent Tutor for Planning in Large Partially Observable Environments. International Journal of Artificial Intelligence in Education, 35, 3095–3127. https://doi.org/10.1007/s40593-025-00493-7"
    author: "Heindrich, L., Consul, S., & Lieder, F."
    q: 1
    i: "?"
    kind: causal
    rigour: 3
---

# MGPO selects planning computations in approximately 0.03 seconds, over 100 times faster than baseline methods

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r3` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` MGPO's computational efficiency enables online VOC computation, a prerequisite for real-time feedback in an intelligent tutor. [→ Heindrich 2025](#heindrich-2025)

## Evidence

### Heindrich 2025

Heindrich, L., Consul, S., & Lieder, F. (2025). An Intelligent Tutor for Planning in Large Partially Observable Environments. International Journal of Artificial Intelligence in Education, 35, 3095–3127. https://doi.org/10.1007/s40593-025-00493-7

`q1 · i?` · `causal · r3`

Timing data from the simulation evaluation section. The article reports "MGPO took 0 .03 seconds" per computation selection, while other baselines required over 100 times the computational budget (meta-greedy 4.89s, PO-UCT 5000 steps 14.19s).

> "On average, MGPO took 0 .03 seconds to select the next computation. The only baseline method with a comparable runtime is PO-UCT with 10 steps (0 .02 seconds)."

## Discussion


## Related Claims
- [MGPO discovers significantly more resource-rational planning strategies than baseline methods in partially observable environments](mgpo-outperforms-baselines-partially-observable.md) — related
- [A preregistered experiment with 330 participants demonstrated the intelligent tutor is highly effective at improving planning in partially observable environments](tutor-improves-human-planning-partially-observable.md) — related
