---
type: claim
title: "Prompt quality was significantly correlated with the effectiveness of CodeTutor's responses"
description: "Prompt quality was significantly correlated with the effectiveness of CodeTutor's responses"
id: prompt-quality-correlates-response-effectiveness
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
sources:
  - id: wenhan-lyu-2024
    title: Wenhan Lyu 2024
    q: 3
    i: "?"
    kind: associational
    rigour: 1
---

# Prompt quality was significantly correlated with the effectiveness of CodeTutor's responses

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q3`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` A chi-square test found prompt quality and response effectiveness were not independent (χ² = 144.84, p < 0.001); clearer, more detailed prompts were associated with more effective responses. [→ Wenhan Lyu 2024](#wenhan-lyu-2024)

## Evidence

### Wenhan Lyu 2024

Wenhan Lyu, Yimeng Wang, Tingting (Rachel) Chung, Yifan Sun, and Yixuan Zhang. 2024. Evaluating the Effectiveness of LLMs in Introductory Computer Science Education: A Semester-Long Field Study. In Proceedings of the Eleventh ACM Conference on Learning @ Scale (L@S '24). https://doi.org/10.1145/3657604.3662036

`q3 · i?` · `associational · r1`

Chi-square test on a corpus of 1,190 prompts (37% good quality, 63% poor), with poor prompts typed as incomplete information, lack of clear goals, over-reliance, and poor structural organization. The association is correlational.

> "Our results showed a significant correlation (𝜒 2 = 144.84, 𝑝 < 0.001). In other words, clearer and more detailed prompts are associated with responses that are more likely to be effective."

## Discussion


## Related Claims
- [Only the well-specified text-only prompt produced a correct quantitative result from o4-mini, while underspecified prompts led to numerical errors and misleading final results](prompt-specificity-shapes-lrm-physics-solution-correctness.md) — related
- [Prompt specificity changes AI tutor pedagogy: a no-direct-answer guardrail alone produces uniform questioning, while a detailed guided protocol produces varied, impasse-sensitive responses](prompt-specificity-shapes-tutor-pedagogy.md) — related
