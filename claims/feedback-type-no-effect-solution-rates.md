---
type: claim
title: Feedback type did not affect whether students solved assignments; solution rates were very similar across all conditions
description: Feedback type did not affect whether students solved assignments; solution rates were very similar across all conditions
id: feedback-type-no-effect-solution-rates
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: tsvetomila-mihaylova-2026
    resource: "https://doi.org/10.48550/arxiv.2605.16933"
    title: "Tsvetomila Mihaylova, Evanfiya Logacheva, Arto Hellas, Jing Fan, Francisco Castro, Bita Akram, Narges Norouzi, Peter Brusilovsky, Juho Leinonen. (2026). The Effects of Structured LLM-Generated Feedback on Programming Assignment Performance. https://arxiv.org/abs/2605.16933 [doi:10.48550/arxiv.2605.16933](https://doi.org/10.48550/arxiv.2605.16933)"
    author: Tsvetomila Mihaylova, Evanfiya Logacheva, Arto Hellas, Jing Fan, Francisco Castro, Bita Akram, Narges Norouzi, Peter Brusilovsky, Juho Leinonen
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Feedback type did not affect whether students solved assignments; solution rates were very similar across all conditions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Solution rates were very similar across all feedback types and the compiler-errors-only condition, so feedback type did not affect whether students solved the assignment. [→ Tsvetomila Mihaylova 2026](#tsvetomila-mihaylova-2026)

## Evidence

### Tsvetomila Mihaylova 2026

Tsvetomila Mihaylova, Evanfiya Logacheva, Arto Hellas, Jing Fan, Francisco Castro, Bita Akram, Narges Norouzi, Peter Brusilovsky, Juho Leinonen. (2026). The Effects of Structured LLM-Generated Feedback on Programming Assignment Performance. https://arxiv.org/abs/2605.16933 [doi:10.48550/arxiv.2605.16933](https://doi.org/10.48550/arxiv.2605.16933)

`q2 · i?` · `causal · r2`

Descriptive comparison of solved percentages per feedback type (Table 8): No Feedback 98.1%, General 98.7%, Single-Issue 98.5%, Diagnostic 99.2%. The article reports these as descriptive rates with no significance test.

> "Very similar solution rate was observed for all the feedback types, as well as the case where only compiler errors were shown, therefore the different feedback types did not affect whether the students solve the assignment."

## Discussion

## Related Claims

- [Feedback improves learning by a medium amount on average, but its effect varies widely with the information it carries, and more than a third of feedback interventions reduce performance](feedback-improves-learning.md) — the general claim this finding bears on, with the studies behind it
- [All three LLM-generated feedback types are associated with faster time to solution than a compiler-errors-only baseline, with Single-Issue Feedback showing the largest reduction](llm-feedback-faster-time-to-solution.md) — related
- MAB assignment yields higher average rewards (student outcomes) than uniform random assignment during experiments — related
- [Attempt-reduction patterns differed across course parts: Diagnostic and General Feedback were associated with fewer attempts for New Content, Single-Issue for Old Content](attempt-reduction-varies-by-course-part.md) — related
- [Feedback effects on time to solution did not differ significantly between novice and advanced students, though predicted trends suggest feedback was more beneficial for advanced students](no-significant-feedback-expertise-interaction.md) — related
- [Advanced students showed reduced attempts with all hint types, while novices did not clearly benefit and made slightly more submissions with Single-Issue Feedback](advanced-students-attempt-reduction-novices-not.md) — related
- [All three LLM feedback types credibly reduced attempts to success relative to the baseline, with the largest reduction for Diagnostic Feedback](llm-feedback-fewer-attempts.md) — related
- [Feedback effectiveness varied by content recency: guidance-heavy feedback performed less consistently on newer material released after the model's knowledge cutoff](content-recency-moderates-feedback-effectiveness.md) — related
