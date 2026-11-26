---
type: claim
title: HawkesKT trains faster with fewer parameters than state-of-the-art baselines, making it applicable to large-scale educational settings
description: HawkesKT trains faster with fewer parameters than state-of-the-art baselines, making it applicable to large-scale educational settings
id: hawkeskt-training-efficiency-advantage
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

# HawkesKT trains faster with fewer parameters than state-of-the-art baselines, making it applicable to large-scale educational settings

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q3`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q3 i?` HawkesKT's training time per epoch is much less than other state-of-the-art methods, even faster than DKT, while achieving the best performance. [→ Wang et al. 2021](#wang-et-al-2021)

## Evidence

### Wang et al. 2021

Chenyang Wang, Weizhi Ma, Min Zhang, Chuancheng Lv, Fengyuan Wan, Huijie Lin, Taoran Tang, Yiqun Liu, Shaoping Ma. (2021). Temporal Cross-Effects in Knowledge Tracing. Proceedings of the Fourteenth ACM International Conference on Web Search and Data Mining (WSDM '21). https://doi.org/10.1145/3437963.3441802

`q3 · i?` · `associational · r2`

Efficiency comparison under identical settings (batch size, embedding size, single 1080Ti GPU; Table 4): HawkesKT 0.5s/epoch and 74.8k parameters on ASSISTments 09-10 versus DKT 0.8s/57.4k, KTM 7.5s/1760.7k, AKT-R 2.3s/160.7k; 15.2s/564.6k on slepemapy.cz.

> "We can observe that the training time of HawkesKT is much less than other state-of-the-art methods, even faster than DKT. KTM is especially slow and needs abundant parameters if there are a lot of questions in the dataset."

## Discussion


## Related Claims
- [HawkesKT outperforms state-of-the-art knowledge tracing baselines on three benchmark datasets in AUC](hawkeskt-outperforms-kt-baselines.md) — related
- [Under one standardised evaluation, most deep knowledge-tracing models published after the original DKT do not beat it, and a common KC-level evaluation shortcut inflates reported accuracy](newer-deep-kt-models-rarely-beat-dkt-standard-protocol.md) — related
- [A prerequisite score derived from HawkesKT's mutual excitation parameters automatically discovers skill prerequisite relationships consistent with expert annotations](prerequisite-score-skill-relation-discovery.md) — related
- [DKVMN reaches higher prediction accuracy than DKT with substantially fewer parameters, especially at low state dimensions](dkvmn-better-accuracy-fewer-parameters.md) — related
