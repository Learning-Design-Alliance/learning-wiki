---
type: claim
title: "AKT's learned Rasch difficulty parameters order questions within a concept and match intuitive difficulty levels"
description: "AKT's learned Rasch difficulty parameters order questions within a concept and match intuitive difficulty levels"
id: akt-learned-difficulty-parameters-match-intuition
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: weak
sources:
  - id: aritra-ghosh-2020
    title: Aritra Ghosh 2020
    q: 1
    i: "?"
    kind: design
    rigour: 2
  - id: aritra-ghosh-2020-2
    title: Aritra Ghosh 2020 (2)
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# AKT's learned Rasch difficulty parameters order questions within a concept and match intuitive difficulty levels

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q1`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` Learned question embeddings on the same concept form a curve ordered by difficulty, with easy questions at one end and hard questions at the other. [→ Aritra Ghosh 2020](#aritra-ghosh-2020)
`q1 i?` Learned difficulty parameters for sample questions match the authors' understanding of their difficulty, e.g., values of -0.0515, 0.0088, and 0.0548 for easy, average, and hard probability questions. [→ Aritra Ghosh 2020 (2)](#aritra-ghosh-2020-2)

## Evidence

### Aritra Ghosh 2020

Aritra Ghosh, Neil Heffernan, and Andrew S. Lan. 2020. Context-Aware Attentive Knowledge Tracing. In Proceedings of the 26th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '20). https://doi.org/10.1145/3394486.3403282

`q1 · i?` · `design · r2`

t-SNE visualization of learned Rasch question embeddings with empirical difficulties (portions of correct responses across learners) on ASSISTments2009; questions on the same concept "form a curve and are ordered by their difficulty levels."

> "We see that questions on the same concept form a curve and are ordered by their difficulty levels: for the majority of concepts, questions on one end of the line segment are easy while questions on the other end are hard."

### Aritra Ghosh 2020 (2)

Aritra Ghosh, Neil Heffernan, and Andrew S. Lan. 2020. Context-Aware Attentive Knowledge Tracing. In Proceedings of the 26th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '20). https://doi.org/10.1145/3394486.3403282

`q1 · i?` · `design · r2`

Case study listing sample questions on three concepts with their learned difficulty parameters; for Probability of a Single Event the values are −0.0515, 0.0088, and 0.0548, and the authors state these "match our understanding about the difficulty levels of these questions."

> "Using the "Probability of a Single Event" concept as an example, the learned difficulty parameter values (µq) are −0.0515 for the easy one, 0.0088 for the average one, and 0.0548 for the hard one. These learned difficulty levels match our understanding about the difficulty levels of these questions."

## Discussion


## Related Claims
- [AKT's learned attention weights are interpretable, operating at multiple time scales and focusing on past practices of the same concept](akt-attention-weights-interpretable-same-concept-focus.md) — related
- [Rasch analysis shows DialogPR item difficulty spans −2.00 to 1.06, with recall, discussion-before-reading, and completion prompts least endorsed and responding, discussion-after, and wh-/open-ended questions most endorsed](dialogpr-rasch-item-difficulty-ordering.md) — related
- [LLM difficulty labels track structural question features: stem length, option length, and digits in stems rise monotonically across Easy, Medium, and Hard labels](llm-difficulty-labels-track-structural-item-features.md) — related
- [Within the FCI-metric, questions 1 and 6 are the easiest and 25 and 26 the hardest, while questions 5, 13 and 18 discriminate best and question 29's item characteristic curve is almost flat](fci-item-difficulty-and-discrimination-extremes.md) — related
