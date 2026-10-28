---
type: claim
title: LLMs' generation probabilities for multiple-choice distractors correlate moderately with how often students choose them
description: Across 3,202 four-option MCQs with real student response distributions, LLaMA and Qwen models (0.5B–72B) assigned distractor probabilities that correlated with student selection at Pearson r = 0.28–0.37, and when wrong chose students' most common wrong answer about 51–59% of the time.
id: llm-distractor-likelihood-moderately-tracks-student-choices
status: review
generated:
  by: claude/unspecified
  at: 2026-10-21
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: liu-2025
    resource: "https://doi.org/10.1007/978-3-031-98459-4_26"
    title: "Liu, N., Sonkar, S., & Baraniuk, R. (2025). Do LLMs make mistakes like students? Exploring natural alignments between language models and human error patterns. In *Artificial Intelligence in Education (AIED 2025)*, Lecture Notes in Computer Science (pp. 364–377). Springer. [doi:10.1007/978-3-031-98459-4_26](https://doi.org/10.1007/978-3-031-98459-4_26)"
    author: "Liu, N., Sonkar, S., & Baraniuk, R."
    q: 2
    i: "?"
    n: 3,202 MCQs from three assessment platforms, six subjects
    kind: associational
    rigour: 2
---

# LLMs' generation probabilities for multiple-choice distractors correlate moderately with how often students choose them

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2` · n=3,202 MCQs from three assessment platforms, six subjects
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

An LLM's preference among wrong answers carries some, but far from all, of the information in real students' error distribution.

## Subclaims

`q2 i?` The probabilities LLMs assign to the distractors of a question correlate moderately with the proportion of students choosing each (Pearson r = 0.28–0.37), with larger models slightly more aligned. [→ Liu 2025](#liu-2025)

`q2 i?` When a model answers incorrectly it picks the distractor students most commonly choose about 51% of the time at 0.5B parameters and up to 59% for larger models. [→ Liu 2025](#liu-2025)

## Evidence

### Liu 2025

Liu, N., Sonkar, S., & Baraniuk, R. (2025). Do LLMs make mistakes like students? Exploring natural alignments between language models and human error patterns. In *Artificial Intelligence in Education (AIED 2025)*, Lecture Notes in Computer Science (pp. 364–377). Springer. [doi:10.1007/978-3-031-98459-4_26](https://doi.org/10.1007/978-3-031-98459-4_26)

`q2 · correlational analysis of model likelihoods against student response data` · `i? · correlations printed (r = 0.28–0.37), not converted` · `n=3,202 MCQs from three assessment platforms, six subjects` · `associational · r2`

Questions were drawn from three assessment platforms across mathematics, biology, physics, social science, reading comprehension and humanities, kept only if at least 50 students answered and the error rate exceeded 5%, and limited to four options. Two model families (LLaMA and Qwen, 0.5B to 72B parameters) were compared with the student distributions on two measures: correlation between generation likelihood and student selection, and whether a model's wrong answer is the students' most common wrong answer. Figures read from the arXiv preprint of the paper (arXiv:2502.15140, February 2025); the AIED version was not read.

## Discussion

The authors read the moderate correlation as evidence that LLMs approach problems differently from students, and suggest LLM distractors could complement rather than replace human ones. The result is consistent with the finding that LLM-generated distractors are judged valid more often than plausible ([Feng et al. 2024](llm-math-distractors-more-valid-than-plausible.md)). Because student errors are themselves unstable and population-specific ([Payne & Squibb 1990](algebra-mal-rules-are-unstable-skewed-and-school-specific.md)), an aggregate distribution of choices is a moving target for any model.

## Related Claims
- [LLM-generated distractors for math multiple-choice questions are judged mathematically valid more often than plausible to students, and rarely reproduce the full set of human-written distractors](llm-math-distractors-more-valid-than-plausible.md) — related
- [LLMs predict common distractors above chance but fall 15 percentage points below chance at predicting which errors students rarely select](llm-distractor-prediction-asymmetry.md) — related
- [Distractor similarity to the correct answer increases MCQ complexity](distractor-similarity-increases-complexity.md) — related
