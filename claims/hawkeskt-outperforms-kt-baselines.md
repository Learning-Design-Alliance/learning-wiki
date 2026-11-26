---
type: claim
title: HawkesKT outperforms state-of-the-art knowledge tracing baselines on three benchmark datasets in AUC
description: HawkesKT outperforms state-of-the-art knowledge tracing baselines on three benchmark datasets in AUC
id: hawkeskt-outperforms-kt-baselines
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

# HawkesKT outperforms state-of-the-art knowledge tracing baselines on three benchmark datasets in AUC

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q3`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q3 i?` HawkesKT achieves the best AUC on ASSISTments 09-10, ASSISTments 12-13, and slepemapy.cz, significantly outperforming most baselines. [→ Wang et al. 2021](#wang-et-al-2021)
`q3 i?` On the geography dataset slepemapy.cz the improvement over DKT-Forgetting is not significant, because temporal cross-effects between skills are less helpful there. [→ Wang et al. 2021 (2)](#wang-et-al-2021-2)

## Evidence

### Wang et al. 2021

Chenyang Wang, Weizhi Ma, Min Zhang, Chuancheng Lv, Fengyuan Wan, Huijie Lin, Taoran Tang, Yiqun Liu, Shaoping Ma. (2021). Temporal Cross-Effects in Knowledge Tracing. Proceedings of the Fourteenth ACM International Conference on Web Search and Data Mining (WSDM '21). https://doi.org/10.1145/3437963.3441802

`q3 · i?` · `design · r2`

Comparative experiment with 5-fold cross validation on three datasets (Table 3): HawkesKT AUC 0.7629, 0.7676, 0.7500 versus baselines including DKT-Forgetting (0.7540, 0.7462, 0.7498) and AKT-R (0.7474, 0.7555, 0.7454). The article reports "HawkesKT performs consistently better than all the baselines".

> "Second, HawkesKT performs consistently better than all the baselines. Compared with DKT-Forgetting, HawkesKT naturally takes continuous time-varying effects into consideration and does not only rely on interactions with the same skill or adjacent one."

### Wang et al. 2021 (2)

Chenyang Wang, Weizhi Ma, Min Zhang, Chuancheng Lv, Fengyuan Wan, Huijie Lin, Taoran Tang, Yiqun Liu, Shaoping Ma. (2021). Temporal Cross-Effects in Knowledge Tracing. Proceedings of the Fourteenth ACM International Conference on Web Search and Data Mining (WSDM '21). https://doi.org/10.1145/3437963.3441802

`q3 · i?` · `design · r2`

Same comparative experiment, geography dataset result. The authors attribute the smaller, non-significant gain to simple skill relationships in geography, where the major temporal dynamic is self-forgetting.

> "While on the geography dataset (slepemapy.cz), the improvement is not that large (the difference compared to DKT-Forgetting is not significant). It is reasonable because the temporal cross-effects between skills are indeed more helpful in mathematics."

## Discussion


## Related Claims
- [AKT outperforms existing knowledge tracing methods on benchmark datasets in predicting future learner responses](akt-outperforms-kt-baselines-auc-benchmarks.md) — related
- [Under one standardised evaluation, most deep knowledge-tracing models published after the original DKT do not beat it, and a common KC-level evaluation shortcut inflates reported accuracy](newer-deep-kt-models-rarely-beat-dkt-standard-protocol.md) — related
- [HawkesKT trains faster with fewer parameters than state-of-the-art baselines, making it applicable to large-scale educational settings](hawkeskt-training-efficiency-advantage.md) — related
- [A prerequisite score derived from HawkesKT's mutual excitation parameters automatically discovers skill prerequisite relationships consistent with expert annotations](prerequisite-score-skill-relation-discovery.md) — related
- [Different cross-skill effects in knowledge tracing decay at different rates over time, which a global decay function cannot capture](temporal-cross-effects-decay-rates-differ.md) — related
- [Cross-skill effects exist in knowledge tracing: mastery of a target skill depends on previous interactions with other, related skills, not only the same skill](cross-skill-effects-in-knowledge-tracing.md) — related
- [Ablations show both adaptive decay rates (temporal cross-effects) and matrix factorization reparameterization contribute to HawkesKT's performance](hawkeskt-ablation-cross-and-cf.md) — related
- [TSDR improves the AUC of six state-of-the-art KT backbones across nine real-world benchmark datasets](tsdr-improves-kt-backbone-auc-benchmarks.md) — related
