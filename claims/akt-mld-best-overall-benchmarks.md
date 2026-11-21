---
type: claim
title: AKT-MLd achieves the best overall performance across benchmarks, with gains most pronounced on high-KC datasets
description: AKT-MLd achieves the best overall performance across benchmarks, with gains most pronounced on high-KC datasets
id: akt-mld-best-overall-benchmarks
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: yahya-badran-and-christine-preisach-2026
    resource: "https://doi.org/10.1007/s42979-026-05344-3"
    title: "Yahya Badran and Christine Preisach. (2026). Enhancing Knowledge Tracing through Leakage-Free and Recency-Aware Embeddings. Originally published 2025. [doi:10.1007/s42979-026-05344-3](https://doi.org/10.1007/s42979-026-05344-3)"
    author: Yahya Badran and Christine Preisach
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# AKT-MLd achieves the best overall performance across benchmarks, with gains most pronounced on high-KC datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On Duolingo2018, DKT-MLd gained noticeable improvement, outperforming the original attention-based models without recency encoding, which the authors hypothesise stems from stronger forgetting influence in language learning. [→ Yahya Badran and Christine Preisach 2026](#yahya-badran-and-christine-preisach-2026)

## Evidence

### Yahya Badran and Christine Preisach 2026

Yahya Badran and Christine Preisach. (2026). Enhancing Knowledge Tracing through Leakage-Free and Recency-Aware Embeddings. Originally published 2025. [doi:10.1007/s42979-026-05344-3](https://doi.org/10.1007/s42979-026-05344-3)

`q2 · i?` · `design · r2`

RNN-based variant result on Duolingo2018 (Table 4). The article reports DKT-MLd "outperform- ing the original attention based models without recency-encoding" and offers the forgetting hypothesis as an interpretation, not a tested result.

> "DKT-MLd gained noticeable improvement on the Duolingo2018 dataset, outperform- ing the original attention based models without recency-encoding. We hypothesise that this improvement stems from the stronger influence of forgetting in the context of language learning"

## Discussion


## Related Claims
- [Under one standardised evaluation, most deep knowledge-tracing models published after the original DKT do not beat it, and a common KC-level evaluation shortcut inflates reported accuracy](newer-deep-kt-models-rarely-beat-dkt-standard-protocol.md) — related
- [AKT outperforms existing knowledge tracing methods on benchmark datasets in predicting future learner responses](akt-outperforms-kt-baselines-auc-benchmarks.md) — related
- [The MASK label method outperforms alternative leakage-mitigation strategies across most KT benchmark datasets](mask-label-outperforms-mitigation-alternatives.md) — related
- [KC-sequence expansion causes label leakage that degrades KT model performance, shown by sharp drops on a correlated-KC dataset](kt-label-leakage-degrades-correlated-kc-performance.md) — related
