---
type: claim
title: MGPO discovers significantly more resource-rational planning strategies than baseline methods in partially observable environments
description: MGPO discovers significantly more resource-rational planning strategies than baseline methods in partially observable environments
id: mgpo-outperforms-baselines-partially-observable
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
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

# MGPO discovers significantly more resource-rational planning strategies than baseline methods in partially observable environments

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r3` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q1 i?` In simulation benchmarks across four partially observable environments, MGPO achieved higher resource-rationality scores than the meta-greedy policy and all PO-UCT configurations. [→ Heindrich 2025](#heindrich-2025)

## Evidence

### Heindrich 2025

Heindrich, L., Consul, S., & Lieder, F. (2025). An Intelligent Tutor for Planning in Large Partially Observable Environments. International Journal of Artificial Intelligence in Education, 35, 3095–3127. https://doi.org/10.1007/s40593-025-00493-7

`q1 · i?` · `causal · r3`

Simulation benchmark comparing MGPO against meta-greedy and PO-UCT baselines across four environments of 37–91 nodes, evaluated on 5000 random instances per condition. A three-way ANOVA (F(5, 239952) = 32682.5, p < .001) confirmed algorithm differences, with "MGPO performs signiﬁcantly better" on post-hoc tests.

> "A Tukey-HSD post-hoc comparison showed that MGPO performs signiﬁcantly better than the meta-greedy policy ( p = .001), the PO-UCT algorithm with 5000 steps ( p = .008), and all PO-UCT algorithm conﬁgurations with less than 5000 steps (all p <. 001)."

## Discussion


## Related Claims
- [MGPO selects planning computations in approximately 0.03 seconds, over 100 times faster than baseline methods](mgpo-computational-efficiency.md) — related
- [A preregistered experiment with 330 participants demonstrated the intelligent tutor is highly effective at improving planning in partially observable environments](tutor-improves-human-planning-partially-observable.md) — related
