---
type: claim
title: "Cross-skill effects exist in knowledge tracing: mastery of a target skill depends on previous interactions with other, related skills, not only the same skill"
description: "Cross-skill effects exist in knowledge tracing: mastery of a target skill depends on previous interactions with other, related skills, not only the same skill"
id: cross-skill-effects-in-knowledge-tracing
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

# Cross-skill effects exist in knowledge tracing: mastery of a target skill depends on previous interactions with other, related skills, not only the same skill

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q3`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Conditional mutual information analyses of real-world interaction data show non-zero dependency between different skill pairs, with high dependencies within related skill groups. [→ Wang et al. 2021](#wang-et-al-2021)

## Evidence

### Wang et al. 2021

Chenyang Wang, Weizhi Ma, Min Zhang, Chuancheng Lv, Fengyuan Wan, Huijie Lin, Taoran Tang, Yiqun Liu, Shaoping Ma. (2021). Temporal Cross-Effects in Knowledge Tracing. Proceedings of the Fourteenth ACM International Conference on Web Search and Data Mining (WSDM '21). https://doi.org/10.1145/3437963.3441802

`q3 · i?` · `associational · r2`

Empirical CMI analysis of the ASSISTments 12-13 dataset (2.7M interactions, 265 skills), demonstrating cross-effects between skills. The authors report "dependencies are high within the skill group {0, 1, 2} and {7, 8, 9}", consistent with perceived skill relatedness.

> "However, there exist obvious cross-effects between different skills, such as the condition when the pre- and post-interaction is 9 and 4, respectively. And the dependencies are high within the skill group {0, 1, 2} and {7, 8, 9}"

## Discussion


## Related Claims
- [CSG-KT significantly outperforms classical, graph-based and SOTA knowledge tracing baselines across four real-world datasets](csg-kt-outperforms-kt-baselines.md) — related
- [GRATE outperforms state-of-the-art knowledge tracing baselines in student performance prediction on three real-world datasets](grate-outperforms-kt-baselines-performance-prediction.md) — related
- [The survey reports, citing Pavlik et al., that no single knowledge tracing model was always the best, and that a better model must consider multiple student features and the learning context.](no-single-knowledge-tracing-model-is-always-best.md) — related
- [Which knowledge-tracing model predicts learner performance best depends on the data, with logistic regression leading on smaller datasets and very long learner histories and deep knowledge tracing on large or sequential ones](knowledge-tracing-model-choice-depends-on-dataset.md) — related
- [Different cross-skill effects in knowledge tracing decay at different rates over time, which a global decay function cannot capture](temporal-cross-effects-decay-rates-differ.md) — a narrower finding that bears on this claim
- [HawkesKT outperforms state-of-the-art knowledge tracing baselines on three benchmark datasets in AUC](hawkeskt-outperforms-kt-baselines.md) — related
