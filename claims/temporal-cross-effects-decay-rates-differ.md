---
type: claim
title: Different cross-skill effects in knowledge tracing decay at different rates over time, which a global decay function cannot capture
description: Different cross-skill effects in knowledge tracing decay at different rates over time, which a global decay function cannot capture
id: temporal-cross-effects-decay-rates-differ
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-26
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: wang-et-al-2021
    resource: "https://doi.org/10.1145/3437963.3441802"
    title: "Chenyang Wang, Weizhi Ma, Min Zhang, Chuancheng Lv, Fengyuan Wan, Huijie Lin, Taoran Tang, Yiqun Liu, Shaoping Ma. (2021). Temporal Cross-Effects in Knowledge Tracing. Proceedings of the Fourteenth ACM International Conference on Web Search and Data Mining (WSDM '21). https://doi.org/10.1145/3437963.3441802"
    author: Chenyang Wang, Weizhi Ma, Min Zhang, Chuancheng Lv, Fengyuan Wan, Huijie Lin, Taoran Tang, Yiqun Liu, Shaoping Ma
    q: 3
    i: "?"
    kind: associational
    rigour: 2
---

# Different cross-skill effects in knowledge tracing decay at different rates over time, which a global decay function cannot capture

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q3`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q3 i?` The temporal evolution of CMI for different skill pairs shows obviously different decay rates, named temporal cross-effects. [→ Wang et al. 2021](#wang-et-al-2021)

## Evidence

### Wang et al. 2021

Chenyang Wang, Weizhi Ma, Min Zhang, Chuancheng Lv, Fengyuan Wan, Huijie Lin, Taoran Tang, Yiqun Liu, Shaoping Ma. (2021). Temporal Cross-Effects in Knowledge Tracing. Proceedings of the Fourteenth ACM International Conference on Web Search and Data Mining (WSDM '21). https://doi.org/10.1145/3437963.3441802

`q3 · i?` · `associational · r2`

Empirical study grouping interaction pairs by log time interval in ASSISTments 12-13 (Figure 3). Globally the evolution decays due to forgetting, but the authors show "the decay rates differ from each other obviously" across skill pairs, e.g. pair 8-7 decays quickly while 8-2 decays slower.

> "However, it is noteworthy that for different skill pairs, the decay rates differ from each other obviously, which we call temporal cross-effects. For example, when the pre- and post-interaction is 8 and 7 respectively, the CMI in the short term is large because they are highly related, but it decays quickly with time."

## Discussion


## Related Claims
- [Ablations show both adaptive decay rates (temporal cross-effects) and matrix factorization reparameterization contribute to HawkesKT's performance](hawkeskt-ablation-cross-and-cf.md) — a narrower finding that bears on this claim
- [Cross-skill effects exist in knowledge tracing: mastery of a target skill depends on previous interactions with other, related skills, not only the same skill](cross-skill-effects-in-knowledge-tracing.md) — a broader claim this one bears on
- [HawkesKT outperforms state-of-the-art knowledge tracing baselines on three benchmark datasets in AUC](hawkeskt-outperforms-kt-baselines.md) — related
