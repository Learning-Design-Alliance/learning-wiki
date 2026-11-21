---
type: claim
title: "Conceptual Semantic Selection significantly improves o3-mini's concept-level deficiency prediction from 2.16% to 12.77% Macro-F1 (t-test, p < 0.01)"
description: "Conceptual Semantic Selection significantly improves o3-mini's concept-level deficiency prediction from 2.16% to 12.77% Macro-F1 (t-test, p < 0.01)"
id: conceptual-semantic-selection-o3-mini-gain
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

# Conceptual Semantic Selection significantly improves o3-mini's concept-level deficiency prediction from 2.16% to 12.77% Macro-F1 (t-test, p < 0.01)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Prioritizing prior responses that are both conceptually and semantically relevant to the target question significantly improves deficiency prediction for the reasoning model o3-mini. [→ Yu-Chen Kang 2026](#yu-chen-kang-2026)

## Evidence

### Yu-Chen Kang 2026

Yu-Chen Kang, Yu-Chien Tang, An-Zi Yen. (2026). ConceptKT: A Benchmark for Concept-Level Deficiency Prediction in Knowledge Tracing. [doi:10.63317/34ncpc8ovxbz](https://doi.org/10.63317/34ncpc8ovxbz)

`q2 · i?` · `causal · r1`

Benchmark experiment (Table 5) applying Conceptual Semantic Selection, which ranks same-concept candidates by BERTScore similarity to the target question. The article reports o3-mini "rising from 2.16% to 12.77%" with a "statistically signifi- cantdifference( t-test, p <0.01)".

> "Using this strategy, o3-mini exhibits a remarkable improve- ment in concept-level deficiency prediction, rising from 2.16% to 12.77%, with a statistically signifi- cantdifference( t-test, p <0.01)."

## Discussion


## Related Claims
- [Feeding the entire response history without filtering sharply degrades concept-level deficiency prediction (Macro-F1 of only 5.43% for Llama-4 and 2.16% for o3-mini)](all-responses-degrades-deficiency-prediction.md) — possibly the same claim (merge candidate)
- [Selecting historical responses by same-concept filtering improves concept-level deficiency prediction, with DeepSeek-R1 achieving the highest Macro-F1 of 17.40% under Same-Concept Selection](same-concept-selection-improves-deficiency-prediction.md) — related
