---
type: claim
title: LLM marking agrees with human markers on only about half of graded Physics answers, and assigns higher, less variable normalized scores than humans
description: LLM marking agrees with human markers on only about half of graded Physics answers, and assigns higher, less variable normalized scores than humans
id: llm-marking-concordance-with-humans-about-half
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: will-yeadon-2024
    resource: "https://doi.org/10.1088/1361-6552/ad1fa2"
    title: "Will Yeadon, Tom Hardy. (2024). The Impact of AI in Physics Education: A Comprehensive Review from GCSE to University Levels. Originally published 2023. [doi:10.1088/1361-6552/ad1fa2](https://doi.org/10.1088/1361-6552/ad1fa2)"
    author: Will Yeadon, Tom Hardy
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: will-yeadon-2024-2
    resource: "https://doi.org/10.1088/1361-6552/ad1fa2"
    title: "Will Yeadon, Tom Hardy. (2024). The Impact of AI in Physics Education: A Comprehensive Review from GCSE to University Levels. Originally published 2023. [doi:10.1088/1361-6552/ad1fa2](https://doi.org/10.1088/1361-6552/ad1fa2)"
    author: Will Yeadon, Tom Hardy
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM marking agrees with human markers on only about half of graded Physics answers, and assigns higher, less variable normalized scores than humans

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Concordance between LLM-assigned and human-assigned scores was 49.82% (Zero-shot), 51.96% (In Context Learning), and 50.54% (Confirmatory Check). [→ Will Yeadon 2024](#will-yeadon-2024)
`q2 i?` Human markers' average normalized score was 0.515 (SD 0.448) while the LLM's was 0.952 (SD 0.167), and human-human correlation across methods (0.913) exceeded human-LLM correlations (0.102-0.257). [→ Will Yeadon 2024 (2)](#will-yeadon-2024-2)

## Evidence

### Will Yeadon 2024

Will Yeadon, Tom Hardy. (2024). The Impact of AI in Physics Education: A Comprehensive Review from GCSE to University Levels. Originally published 2023. [doi:10.1088/1361-6552/ad1fa2](https://doi.org/10.1088/1361-6552/ad1fa2)

`q2 · i?` · `design · r2`

Automated grading evaluation in which the LLM marked its own 3486 answers to 1162 questions with solution and guidance supplied; only 2209 instances were successfully graded. The article reports concordance rates of "49.82%, 51.96%, and 50.54%".

> "Human and LLM evaluation showed a concordance in scores for Zero- shot, In Context Learning, and Confirmatory Checking with rates of 49.82%, 51.96%, and 50.54%, respectively."

### Will Yeadon 2024 (2)

Will Yeadon, Tom Hardy. (2024). The Impact of AI in Physics Education: A Comprehensive Review from GCSE to University Levels. Originally published 2023. [doi:10.1088/1361-6552/ad1fa2](https://doi.org/10.1088/1361-6552/ad1fa2)

`q2 · i?` · `design · r2`

Score distribution comparison across the 2209 graded instances in the AI marking evaluation. The article prints the human mean of 0.515 versus the LLM mean of 0.952 and the correlation matrix in Table 3.

> "human markers assigned an average normalized score of 0.515, with a standard deviation of 0.448. The LLM’s average normalized score was a lot higher at 0.952 but had a lower standard deviation of 0.167."

## Discussion


## Related Claims
- [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](llm-grading-mixed-against-human-raters.md) — a broader claim this one bears on
- [Kappa agreement with human experts shows a system is neither much worse nor much better than experts, but not that experts are a desirable comparison basis](kappa-expert-agreement-limits.md) — related
- [Human Graders of Open-Ended Work Agree With Each Other Less Than Treating One Grade as Ground Truth Implies](human-graders-agree-less-than-single-grade-ground-truth-implies.md) — related
- [LLM-based scoring of Spanish argumentative writing achieves 60–80% per-item accuracy, slightly below human inter-rater agreement](llm-scoring-spanish-writing-60-80-accuracy-below-human-agreement.md) — related
- [AI-generated short-form physics essays marked by five independent markers averaged 71 ± 2%, in strong agreement with the module average of 71 ± 5%](ai-essays-first-class-physics-essay-marks.md) — related
