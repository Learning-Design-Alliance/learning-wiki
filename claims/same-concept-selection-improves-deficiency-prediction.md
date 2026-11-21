---
type: claim
title: "Selecting historical responses by same-concept filtering improves concept-level deficiency prediction, with DeepSeek-R1 achieving the highest Macro-F1 of 17.40% under Same-Concept Selection"
description: "Selecting historical responses by same-concept filtering improves concept-level deficiency prediction, with DeepSeek-R1 achieving the highest Macro-F1 of 17.40% under Same-Concept Selection"
id: same-concept-selection-improves-deficiency-prediction
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

# Selecting historical responses by same-concept filtering improves concept-level deficiency prediction, with DeepSeek-R1 achieving the highest Macro-F1 of 17.40% under Same-Concept Selection

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Restricting LLM input to responses involving the same concepts as the target question yields substantial gains in concept-level deficiency prediction over using all responses, with DeepSeek-R1 reaching Macro-F1 17.40% and correctness 71.02%. [→ Yu-Chen Kang 2026](#yu-chen-kang-2026)

## Evidence

### Yu-Chen Kang 2026

Yu-Chen Kang, Yu-Chien Tang, An-Zi Yen. (2026). ConceptKT: A Benchmark for Concept-Level Deficiency Prediction in Knowledge Tracing. [doi:10.63317/34ncpc8ovxbz](https://doi.org/10.63317/34ncpc8ovxbz)

`q2 · i?` · `design · r2`

Benchmark experiment on ConceptKT comparing four LLMs/LRMs under three response-selection strategies, with accuracy for correctness and Macro-F1 for multi-label deficiency prediction (Table 5). The article reports DeepSeek-R1 "achieves the high- est Macro-F1 score (17.40%)" with correctness "(71.02%)" under Same-Concept Selection.

> "DeepSeek-R1 achieves the high- est Macro-F1 score (17.40%) for concept-level de- ficiency prediction among all models in this setting, along with strong performance on answer correct- ness prediction (71.02%)."

## Discussion


## Related Claims
- [Feeding the entire response history without filtering sharply degrades concept-level deficiency prediction (Macro-F1 of only 5.43% for Llama-4 and 2.16% for o3-mini)](all-responses-degrades-deficiency-prediction.md) — possibly the same claim (merge candidate)
- [Conceptual Semantic Selection significantly improves o3-mini's concept-level deficiency prediction from 2.16% to 12.77% Macro-F1 (t-test, p < 0.01)](conceptual-semantic-selection-o3-mini-gain.md) — related
- [Supplementing sparse same-concept histories with different-concept responses reduces Llama-4's correctness accuracy and deficiency identification](different-concept-augmentation-hurts-prediction.md) — related
- [OKT predicts answer correctness strongly but performs poorly in predicting concept-level deficiencies](okt-strong-correctness-poor-deficiency.md) — related
