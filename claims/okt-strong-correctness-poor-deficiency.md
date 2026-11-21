---
type: claim
title: OKT predicts answer correctness strongly but performs poorly in predicting concept-level deficiencies
description: OKT predicts answer correctness strongly but performs poorly in predicting concept-level deficiencies
id: okt-strong-correctness-poor-deficiency
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: yu-chen-kang-2026
    resource: "https://doi.org/10.63317/34ncpc8ovxbz"
    title: "Yu-Chen Kang, Yu-Chien Tang, An-Zi Yen. (2026). ConceptKT: A Benchmark for Concept-Level Deficiency Prediction in Knowledge Tracing. [doi:10.63317/34ncpc8ovxbz](https://doi.org/10.63317/34ncpc8ovxbz)"
    author: Yu-Chen Kang, Yu-Chien Tang, An-Zi Yen
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# OKT predicts answer correctness strongly but performs poorly in predicting concept-level deficiencies

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Among trained baselines, only OKT can predict concept deficiencies, and it does so poorly despite strong correctness accuracy (69.25%). [→ Yu-Chen Kang 2026](#yu-chen-kang-2026)

## Evidence

### Yu-Chen Kang 2026

Yu-Chen Kang, Yu-Chien Tang, An-Zi Yen. (2026). ConceptKT: A Benchmark for Concept-Level Deficiency Prediction in Knowledge Tracing. [doi:10.63317/34ncpc8ovxbz](https://doi.org/10.63317/34ncpc8ovxbz)

`q2 · i?` · `design · r2`

Baseline comparison in the benchmark experiment (Table 5): DKT, DKVMN, GKT, SAKT and OKT were trained as baselines, among which only OKT can predict concept deficiencies. The article reports OKT "demonstrates strong accuracy in predicting answer correctness" (69.25% in Table 5) while stating it performs poorly in predicting concept-level deficiencies, with Macro-F1 of only 1.87% in Table 5.

> "OKT demonstrates strong accuracy in predicting answer correctness."

## Discussion


## Related Claims
- [Feeding the entire response history without filtering sharply degrades concept-level deficiency prediction (Macro-F1 of only 5.43% for Llama-4 and 2.16% for o3-mini)](all-responses-degrades-deficiency-prediction.md) — related
- [Selecting historical responses by same-concept filtering improves concept-level deficiency prediction, with DeepSeek-R1 achieving the highest Macro-F1 of 17.40% under Same-Concept Selection](same-concept-selection-improves-deficiency-prediction.md) — related
- [Supplementing sparse same-concept histories with different-concept responses reduces Llama-4's correctness accuracy and deficiency identification](different-concept-augmentation-hurts-prediction.md) — related
