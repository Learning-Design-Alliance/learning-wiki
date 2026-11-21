---
type: claim
title: "Supplementing sparse same-concept histories with different-concept responses reduces Llama-4's correctness accuracy and deficiency identification"
description: "Supplementing sparse same-concept histories with different-concept responses reduces Llama-4's correctness accuracy and deficiency identification"
id: different-concept-augmentation-hurts-prediction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
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

# Supplementing sparse same-concept histories with different-concept responses reduces Llama-4's correctness accuracy and deficiency identification

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Llama-4 performs better using only same-concept responses without augmentation, even when fewer than 30 responses are available; random or similarity-based augmentation lowers both metrics. [→ Yu-Chen Kang 2026](#yu-chen-kang-2026)

## Evidence

### Yu-Chen Kang 2026

Yu-Chen Kang, Yu-Chien Tang, An-Zi Yen. (2026). ConceptKT: A Benchmark for Concept-Level Deficiency Prediction in Knowledge Tracing. [doi:10.63317/34ncpc8ovxbz](https://doi.org/10.63317/34ncpc8ovxbz)

`q2 · i?` · `design · r2`

Supplementary experiment (Table 6) restricted to 106 target questions with fewer than 30 same-concept responses, comparing no augmentation, random augmentation, and similarity-based augmentation for Llama-4. No-augmentation scored 68.87% correctness and 9.15% Macro-F1 versus 66.98%/5.08% and 66.04%/7.66%.

> "Llama-4 performs better when using only same-concept responses (i.e., no augmentation), even if the total number of responses is less than 30."

## Discussion


## Related Claims
- [Feeding the entire response history without filtering sharply degrades concept-level deficiency prediction (Macro-F1 of only 5.43% for Llama-4 and 2.16% for o3-mini)](all-responses-degrades-deficiency-prediction.md) — related
- [Selecting historical responses by same-concept filtering improves concept-level deficiency prediction, with DeepSeek-R1 achieving the highest Macro-F1 of 17.40% under Same-Concept Selection](same-concept-selection-improves-deficiency-prediction.md) — related
- [OKT predicts answer correctness strongly but performs poorly in predicting concept-level deficiencies](okt-strong-correctness-poor-deficiency.md) — related
