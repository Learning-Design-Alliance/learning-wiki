---
type: claim
title: "A prerequisite score derived from HawkesKT's mutual excitation parameters automatically discovers skill prerequisite relationships consistent with expert annotations"
description: "A prerequisite score derived from HawkesKT's mutual excitation parameters automatically discovers skill prerequisite relationships consistent with expert annotations"
id: prerequisite-score-skill-relation-discovery
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
    kind: design
    rigour: 2
  - id: wang-et-al-2021-2
    resource: "https://doi.org/10.1145/3437963.3441802"
    title: "Chenyang Wang, Weizhi Ma, Min Zhang, Chuancheng Lv, Fengyuan Wan, Huijie Lin, Taoran Tang, Yiqun Liu, Shaoping Ma. (2021). Temporal Cross-Effects in Knowledge Tracing. Proceedings of the Fourteenth ACM International Conference on Web Search and Data Mining (WSDM '21). https://doi.org/10.1145/3437963.3441802"
    author: Chenyang Wang, Weizhi Ma, Min Zhang, Chuancheng Lv, Fengyuan Wan, Huijie Lin, Taoran Tang, Yiqun Liu, Shaoping Ma
    q: 3
    i: "?"
    kind: associational
    rigour: 2
---

# A prerequisite score derived from HawkesKT's mutual excitation parameters automatically discovers skill prerequisite relationships consistent with expert annotations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q3`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Ranked lists of prerequisite skills generated from the prerequisite score achieve an averaged NDCG of 0.8267 against averaged expert annotations of helpfulness between skill pairs. [→ Wang et al. 2021](#wang-et-al-2021)
`q3 i?` A case study of learned parameters recovers meaningful relations, e.g. Multiplication Fractions as a strong prerequisite of Division Fractions. [→ Wang et al. 2021 (2)](#wang-et-al-2021-2)

## Evidence

### Wang et al. 2021

Chenyang Wang, Weizhi Ma, Min Zhang, Chuancheng Lv, Fengyuan Wan, Huijie Lin, Taoran Tang, Yiqun Liu, Shaoping Ma. (2021). Temporal Cross-Effects in Knowledge Tracing. Proceedings of the Fourteenth ACM International Conference on Web Search and Data Mining (WSDM '21). https://doi.org/10.1145/3437963.3441802

`q3 · i?` · `design · r2`

Annotation experiment on top-20 frequency skills in ASSISTments 12-13: three experts annotated binary helpfulness between each skill pair, with kappa coefficient 0.52. The ranked prerequisite-score lists reached averaged NDCG 0.8267 against the averaged annotations.

> "Then a ranked list for each skill is generated based on the proposed prerequisite score. This ranked list is evaluated according to the annotated relevance, whose averaged NDCG is 0.8267. This shows our model can indeed automatically find relationships between skills consistent with human perceptions."

### Wang et al. 2021 (2)

Chenyang Wang, Weizhi Ma, Min Zhang, Chuancheng Lv, Fengyuan Wan, Huijie Lin, Taoran Tang, Yiqun Liu, Shaoping Ma. (2021). Temporal Cross-Effects in Knowledge Tracing. Proceedings of the Fourteenth ACM International Conference on Web Search and Data Mining (WSDM '21). https://doi.org/10.1145/3437963.3441802

`q3 · i?` · `associational · r2`

Qualitative case study visualizing relations among top-10 frequency skills learned on ASSISTments 12-13 (Figure 5). The authors report the model "indeed finds some meaningful relations", including Addition and Subtraction Fractions having some impact on Division Fractions.

> "For example, Order of Operations All (6 in red) relies on skills about addition/subtraction (2) and multiplication/division (7, 8). The prerequisite scores for multiplication/division skills are higher because they are more essential when determining the order of operations."

## Discussion


## Related Claims
- [Ablations show both adaptive decay rates (temporal cross-effects) and matrix factorization reparameterization contribute to HawkesKT's performance](hawkeskt-ablation-cross-and-cf.md) — related
- [HawkesKT outperforms state-of-the-art knowledge tracing baselines on three benchmark datasets in AUC](hawkeskt-outperforms-kt-baselines.md) — related
- [The framework generalizes under automatically generated Q-matrices without requiring expert annotation](automatic-qmatrix-extraction-generalization.md) — related
- [HawkesKT trains faster with fewer parameters than state-of-the-art baselines, making it applicable to large-scale educational settings](hawkeskt-training-efficiency-advantage.md) — related
- [DKVMN's correlation weights automatically discover underlying concepts of exercises without expert annotation](dkvmn-automatic-concept-discovery.md) — related
- [Latent concepts discovered by GRATE are meaningful and go beyond the labeled topics in the data](grate-latent-concepts-beyond-topics.md) — related
