---
type: claim
title: DKVMN consistently outperforms BKT, DKT and a MANN baseline in knowledge-tracing prediction AUC across four datasets
description: DKVMN consistently outperforms BKT, DKT and a MANN baseline in knowledge-tracing prediction AUC across four datasets
id: dkvmn-outperforms-dkt-mann-bkt-auc
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

# DKVMN consistently outperforms BKT, DKT and a MANN baseline in knowledge-tracing prediction AUC across four datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2017 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2020**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the Statics2011 dataset, DKVMN achieves a test AUC of 82.8%, exceeding DKT (80.2%), MANN (77.6%), BKT (73%) and BKT+ (75%). [→ Zhang et al. 2017](#zhang-et-al-2017)
`q2 i?` On Synthetic-5, ASSISTments2009 and ASSISTments2015, DKVMN's test AUC (82.7%, 81.6%, 72.7%) is higher than MANN, DKT and BKT on each dataset. [→ Zhang et al. 2017](#zhang-et-al-2017)

## Evidence

### Zhang et al. 2017

Jiani Zhang, Xingjian Shi, Irwin King, Dit-Yan Yeung. (2017). Dynamic Key-Value Memory Networks for Knowledge Tracing. WWW 2017, Perth, Australia. https://doi.org/10.1145/3038912.3052580

`q2 · i?` · `design · r2`

Comparative evaluation on four KT datasets (one synthetic, three real-world) reporting test AUC in Table 1; on Statics2011 DKVMN reaches 82.8% versus 80.2% for the authors' DKT implementation, 77.6% for MANN, and 73%/75% for BKT/BKT+. The article reports DKVMN "outperforming all previous models".

> "With regard to Statics2011, which has the maximum number of exercise tags and the minimum number of answers, classical BKT gains the AUC of 73% and BKT cooperating with forgetting, skill discovery, and latent abilities obtains an AUC of 75%"

## Discussion


## Related Claims
- [DKVMN reaches higher prediction accuracy than DKT with substantially fewer parameters, especially at low state dimensions](dkvmn-better-accuracy-fewer-parameters.md) — related
- [SBRKT achieves the highest AUC on several knowledge tracing benchmarks and ranks second on the others, despite sparse discrete representations](sbrkt-auc-vs-baselines.md) — related
- [Under one standardised evaluation, most deep knowledge-tracing models published after the original DKT do not beat it, and a common KC-level evaluation shortcut inflates reported accuracy](newer-deep-kt-models-rarely-beat-dkt-standard-protocol.md) — related
- [AKT outperforms existing knowledge tracing methods on benchmark datasets in predicting future learner responses](akt-outperforms-kt-baselines-auc-benchmarks.md) — related
