---
type: claim
title: "Feeding the entire response history without filtering sharply degrades concept-level deficiency prediction (Macro-F1 of only 5.43% for Llama-4 and 2.16% for o3-mini)"
description: "Feeding the entire response history without filtering sharply degrades concept-level deficiency prediction (Macro-F1 of only 5.43% for Llama-4 and 2.16% for o3-mini)"
id: all-responses-degrades-deficiency-prediction
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
    kind: causal
    rigour: 1
---

# Feeding the entire response history without filtering sharply degrades concept-level deficiency prediction (Macro-F1 of only 5.43% for Llama-4 and 2.16% for o3-mini)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Using all responses without filtering leads to a significant drop in concept-level deficiency prediction performance compared with concept-aware selection. [→ Yu-Chen Kang 2026](#yu-chen-kang-2026)

## Evidence

### Yu-Chen Kang 2026

Yu-Chen Kang, Yu-Chien Tang, An-Zi Yen. (2026). ConceptKT: A Benchmark for Concept-Level Deficiency Prediction in Knowledge Tracing. [doi:10.63317/34ncpc8ovxbz](https://doi.org/10.63317/34ncpc8ovxbz)

`q2 · i?` · `causal · r1`

Benchmark experiment (Table 5) under the All Responses strategy: the article reports that "Llama-4 and o3-mini achieve Macro-F1 scores of only 5.43% and 2.16%, respectively" for concept-level deficiency prediction, far below their same-concept results.

> "For example, Llama-4 and o3-mini achieve Macro-F1 scores of only 5.43% and 2.16%, respectively."

## Discussion


## Related Claims
- [Conceptual Semantic Selection significantly improves o3-mini's concept-level deficiency prediction from 2.16% to 12.77% Macro-F1 (t-test, p < 0.01)](conceptual-semantic-selection-o3-mini-gain.md) — possibly the same claim (merge candidate)
- [Selecting historical responses by same-concept filtering improves concept-level deficiency prediction, with DeepSeek-R1 achieving the highest Macro-F1 of 17.40% under Same-Concept Selection](same-concept-selection-improves-deficiency-prediction.md) — possibly the same claim (merge candidate)
- [OKT predicts answer correctness strongly but performs poorly in predicting concept-level deficiencies](okt-strong-correctness-poor-deficiency.md) — related
- [Supplementing sparse same-concept histories with different-concept responses reduces Llama-4's correctness accuracy and deficiency identification](different-concept-augmentation-hurts-prediction.md) — related
