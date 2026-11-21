---
type: claim
title: SBRKT achieves the highest AUC on several knowledge tracing benchmarks and ranks second on the others, despite sparse discrete representations
description: SBRKT achieves the highest AUC on several knowledge tracing benchmarks and ranks second on the others, despite sparse discrete representations
id: sbrkt-auc-vs-baselines
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: yahya-badran-and-christine-preisach-2026
    resource: "https://doi.org/10.1007/978-3-032-39106-3_8"
    title: "Yahya Badran and Christine Preisach. (2026). Representation Learning of Auxiliary Concepts for Improved Student Modeling and Exercise Recommendation. Originally published 2025. [doi:10.1007/978-3-032-39106-3_8](https://doi.org/10.1007/978-3-032-39106-3_8)"
    author: Yahya Badran and Christine Preisach
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# SBRKT achieves the highest AUC on several knowledge tracing benchmarks and ranks second on the others, despite sparse discrete representations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On four benchmark datasets, SBRKT achieves the highest AUC on several datasets and ranks second on the others compared with BKT, DKT, DKVMN, deepIRT and QIKT baselines. [→ Yahya Badran and Christine Preisach 2026](#yahya-badran-and-christine-preisach-2026)

## Evidence

### Yahya Badran and Christine Preisach 2026

Yahya Badran and Christine Preisach. (2026). Representation Learning of Auxiliary Concepts for Improved Student Modeling and Exercise Recommendation. Originally published 2025. [doi:10.1007/978-3-032-39106-3_8](https://doi.org/10.1007/978-3-032-39106-3_8)

`q2 · i?` · `design · r2`

Benchmark comparison on four public knowledge tracing datasets (ASSISTments2009, ASSISTments2017, Algebra2005, riiid2020) using AUC with an 80/10/10 split; Table 2 shows SBRKT best on ASSISTments2009 and riiid2020 and second elsewhere. The article reports it "achieves the highest performance on several datasets".

> "The results show that our model achieves the highest performance on several datasets and ranks second on the others."

## Discussion


## Related Claims
- [Augmenting DKT with auxiliary KCs improves AUC on all datasets except Algebra2005, where it performs slightly worse than original DKT](dkt-aux-mixed-gains.md) — related
- [The quantization layer is important to SBRKT: removing it (dense variant) underperforms significantly, and auxiliary KCs from quantized variants transfer better](quantization-layer-ablation.md) — related
- [Under one standardised evaluation, most deep knowledge-tracing models published after the original DKT do not beat it, and a common KC-level evaluation shortcut inflates reported accuracy](newer-deep-kt-models-rarely-beat-dkt-standard-protocol.md) — related
