---
type: claim
title: "Ablations show both adaptive decay rates (temporal cross-effects) and matrix factorization reparameterization contribute to HawkesKT's performance"
description: "Ablations show both adaptive decay rates (temporal cross-effects) and matrix factorization reparameterization contribute to HawkesKT's performance"
id: hawkeskt-ablation-cross-and-cf
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
    kind: design
    rigour: 2
---

# Ablations show both adaptive decay rates (temporal cross-effects) and matrix factorization reparameterization contribute to HawkesKT's performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q3`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Removing adaptive decay rates (the \Cross variant with a global decay parameter) leads to consistently worse results on all datasets, showing a global decay rate is not sufficient. [→ Wang et al. 2021](#wang-et-al-2021)
`q3 i?` Removing matrix factorization (the \CF variant) causes a moderate performance loss, showing collaborative-filtering reparameterization helps generalization. [→ Wang et al. 2021 (2)](#wang-et-al-2021-2)

## Evidence

### Wang et al. 2021

Chenyang Wang, Weizhi Ma, Min Zhang, Chuancheng Lv, Fengyuan Wan, Huijie Lin, Taoran Tang, Yiqun Liu, Shaoping Ma. (2021). Temporal Cross-Effects in Knowledge Tracing. Proceedings of the Fourteenth ACM International Conference on Web Search and Data Mining (WSDM '21). https://doi.org/10.1145/3437963.3441802

`q3 · i?` · `design · r2`

Ablation study (Figure 4) comparing HawkesKT with variants lacking temporal information, adaptive decay, or matrix factorization, alongside DKT-Forgetting and AKT-R. The \Cross variant "leads to consistently worse results on all the datasets".

> "Second, it is important to model fine-grained temporal evolution with different decay rates to capture temporal cross-effects in KT. Although the performance loss of \Cross is not the largest, it is noteworthy that \Cross leads to consistently worse results on all the datasets."

### Wang et al. 2021 (2)

Chenyang Wang, Weizhi Ma, Min Zhang, Chuancheng Lv, Fengyuan Wan, Huijie Lin, Taoran Tang, Yiqun Liu, Shaoping Ma. (2021). Temporal Cross-Effects in Knowledge Tracing. Proceedings of the Fourteenth ACM International Conference on Web Search and Data Mining (WSDM '21). https://doi.org/10.1145/3437963.3441802

`q3 · i?` · `design · r2`

Same ablation study: the \CF variant without matrix factorization suffers a moderate loss on all datasets, which the authors say shows the effectiveness of combining point process and collaborative filtering.

> "Third, reparameterization with matrix factorization brings stable performance gain. Matrix factorization helps to take advantage of collaborative filtering, which enables the learned patterns to propagate through embeddings and generalize under different circumstances."

## Discussion


## Related Claims
- [A prerequisite score derived from HawkesKT's mutual excitation parameters automatically discovers skill prerequisite relationships consistent with expert annotations](prerequisite-score-skill-relation-discovery.md) — related
- [Different cross-skill effects in knowledge tracing decay at different rates over time, which a global decay function cannot capture](temporal-cross-effects-decay-rates-differ.md) — a broader claim this one bears on
- [HawkesKT outperforms state-of-the-art knowledge tracing baselines on three benchmark datasets in AUC](hawkeskt-outperforms-kt-baselines.md) — related
