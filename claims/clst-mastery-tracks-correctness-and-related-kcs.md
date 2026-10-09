---
type: claim
title: "CLST's predicted mastery levels track response correctness and move similarly for related knowledge components"
description: "CLST's predicted mastery levels track response correctness and move similarly for related knowledge components"
id: clst-mastery-tracks-correctness-and-related-kcs
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: weak
sources:
  - id: heeseok-jung-2025
    resource: "https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2"
    title: "Heeseok Jung, Yohaan Yoon, Jaesang Yoo, Yeonju Jang. (2025). CLST: Cold-Start Mitigation in Knowledge Tracing by Aligning a Generative Language Model as a Students' Knowledge Tracer. Journal of Educational Data Mining, Volume 17, No 2. https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2"
    author: Heeseok Jung, Yohaan Yoon, Jaesang Yoo, Yeonju Jang
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# CLST's predicted mastery levels track response correctness and move similarly for related knowledge components

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`

## Subclaims
`q1 i?` Visual learning-trajectory analysis showed mastery for a KC rises after correct answers and falls after incorrect ones, and related KC pairs (e.g., scatter plot and stem-and-leaf plot) exhibited mutually similar trends. [→ Heeseok Jung 2025](#heeseok-jung-2025)

## Evidence

### Heeseok Jung 2025

Heeseok Jung, Yohaan Yoon, Jaesang Yoo, Yeonju Jang. (2025). CLST: Cold-Start Mitigation in Knowledge Tracing by Aligning a Generative Language Model as a Students' Knowledge Tracer. Journal of Educational Data Mining, Volume 17, No 2. https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2

`q1 · i?` · `design · r2`

Qualitative visual analysis (Figures 6-9) of heat maps and line graphs of predicted mastery per KC for randomly selected students from science, social studies, and Assist09 mathematics, using CLST fine-tuned with 64 students. The article found mastery "increases or decreases, respectively" with correctness, and related KCs showed similar trends.

> "when a student correctly or incorrectly answers a question about a specific KC, the mastery level of the corresponding KC increases or decreases, respectively."

## Discussion


## Related Claims
- [Quantitative inter-skill influence analysis shows conceptually similar skills exert the strongest mutual influence in CLST predictions](clst-inter-skill-influence-conceptual-similarity.md) — related
- [BKTransformer's generated parameters evolve intuitively with student response sequences, supporting interpretability of mastery and correctness predictions](bkt-parameter-evolution-interpretability.md) — related
- [MS-BKT mastery estimates fluctuate less than classic BKT and avoid over-high estimates after long incorrect runs, in fictitious-student comparisons](ms-bkt-estimates-fluctuate-less-than-bkt.md) — related
- [Under standard BKT with non-degenerate parameters, the mastery probability stays above the learn rate even after unboundedly many incorrect responses](bkt-mastery-floor-above-learn-rate.md) — related
