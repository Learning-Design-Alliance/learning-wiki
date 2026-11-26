---
type: claim
title: DKVMN reaches higher prediction accuracy than DKT with substantially fewer parameters, especially at low state dimensions
description: DKVMN reaches higher prediction accuracy than DKT with substantially fewer parameters, especially at low state dimensions
id: dkvmn-better-accuracy-fewer-parameters
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-26
evidence_strength: moderate
newest_evidence: 2017
recheck_by: 2020
sources:
  - id: zhang-et-al-2017
    resource: "https://doi.org/10.1145/3038912.3052580"
    title: "Jiani Zhang, Xingjian Shi, Irwin King, Dit-Yan Yeung. (2017). Dynamic Key-Value Memory Networks for Knowledge Tracing. WWW 2017, Perth, Australia. https://doi.org/10.1145/3038912.3052580"
    author: Jiani Zhang, Xingjian Shi, Irwin King, Dit-Yan Yeung
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# DKVMN reaches higher prediction accuracy than DKT with substantially fewer parameters, especially at low state dimensions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2017 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2020**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On Statics2011, DKVMN achieves 82.84% test AUC with 50 state dimensions and 197 thousand parameters, while DKT peaks at 80.20% with 200 dimensions and 1 million parameters. [→ Zhang et al. 2017](#zhang-et-al-2017)

## Evidence

### Zhang et al. 2017

Jiani Zhang, Xingjian Shi, Irwin King, Dit-Yan Yeung. (2017). Dynamic Key-Value Memory Networks for Knowledge Tracing. WWW 2017, Perth, Australia. https://doi.org/10.1145/3038912.3052580

`q2 · i?` · `design · r2`

Hyperparameter traversal comparing DKVMN and DKT across state dimensions 10–200 and memory sizes on four datasets (Table 2). The numerical comparison shows DKVMN with low state dimensions achieving better test AUC than DKT with high state dimensions, at a fraction of the parameters.

> "on the Statics2011 dataset, DKT reaches the maximum test AUC of 80.20% when the dimension of states equals 200 using 1 million parameters. Meanwhile, DKVMN can achieve the test AUC of 82.84% only with 50 state dimensions using 197 thousand parameters"

## Discussion


## Related Claims
- [DKVMN consistently outperforms BKT, DKT and a MANN baseline in knowledge-tracing prediction AUC across four datasets](dkvmn-outperforms-dkt-mann-bkt-auc.md) — related
- [Under one standardised evaluation, most deep knowledge-tracing models published after the original DKT do not beat it, and a common KC-level evaluation shortcut inflates reported accuracy](newer-deep-kt-models-rarely-beat-dkt-standard-protocol.md) — reports the opposite
- [AKT outperforms existing knowledge tracing methods on benchmark datasets in predicting future learner responses](akt-outperforms-kt-baselines-auc-benchmarks.md) — related
- [SBRKT achieves the highest AUC on several knowledge tracing benchmarks and ranks second on the others, despite sparse discrete representations](sbrkt-auc-vs-baselines.md) — related
- [HawkesKT trains faster with fewer parameters than state-of-the-art baselines, making it applicable to large-scale educational settings](hawkeskt-training-efficiency-advantage.md) — related
