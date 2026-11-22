---
type: claim
title: "The 2-tiered rescue protocol corrects roughly one-third to one-half of T1 errors, raising final accuracy to 94.3% (Gemini) and 95.6% (GPT-5) with no significant system difference"
description: "The 2-tiered rescue protocol corrects roughly one-third to one-half of T1 errors, raising final accuracy to 94.3% (Gemini) and 95.6% (GPT-5) with no significant system difference"
id: two-tier-rescue-raises-final-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: kirchberger-michael-constantin-md-mavragani-amaryllis-2026
    resource: "https://doi.org/10.2196/86999"
    title: "Kirchberger Michael Constantin MD; Mavragani Amaryllis. (2026). A 2-Tiered Rescue Protocol to Mitigate Difficulty-Based Failures of ChatGPT (GPT-5) and Gemini on the German M2 Medical Examination: Evaluation Study. JMIR Formative Research. https://doi.org/10.2196/86999"
    author: Kirchberger Michael Constantin MD; Mavragani Amaryllis
    q: 3
    i: "?"
    kind: design
    rigour: 2
  - id: kirchberger-michael-constantin-md-mavragani-amaryllis-2026-2
    resource: "https://doi.org/10.2196/86999"
    title: "Kirchberger Michael Constantin MD; Mavragani Amaryllis. (2026). A 2-Tiered Rescue Protocol to Mitigate Difficulty-Based Failures of ChatGPT (GPT-5) and Gemini on the German M2 Medical Examination: Evaluation Study. JMIR Formative Research. https://doi.org/10.2196/86999"
    author: Kirchberger Michael Constantin MD; Mavragani Amaryllis
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# The 2-tiered rescue protocol corrects roughly one-third to one-half of T1 errors, raising final accuracy to 94.3% (Gemini) and 95.6% (GPT-5) with no significant system difference

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` Gemini 2.5 Pro rescued 9/27 (33.3%) and GPT-5 Thinking 13/27 (48.2%) of T1 errors (Fisher exact P=.41); final system accuracies were 94.3% and 95.6% (McNemar P=.48). [→ Kirchberger Michael Constantin MD; Mavragani Amaryllis 2026](#kirchberger-michael-constantin-md-mavragani-amaryllis-2026)
`q3 i?` GPT-5 Thinking's descriptively higher rescue rate was driven by success on high-difficulty items, rescuing 63.6% of level 4 or 5 errors versus 30% for Gemini Pro 2.5. [→ Kirchberger Michael Constantin MD; Mavragani Amaryllis 2026 (2)](#kirchberger-michael-constantin-md-mavragani-amaryllis-2026-2)

## Evidence

### Kirchberger Michael Constantin MD; Mavragani Amaryllis 2026

Kirchberger Michael Constantin MD; Mavragani Amaryllis. (2026). A 2-Tiered Rescue Protocol to Mitigate Difficulty-Based Failures of ChatGPT (GPT-5) and Gemini on the German M2 Medical Examination: Evaluation Study. JMIR Formative Research. https://doi.org/10.2196/86999

`q3 · i?` · `design · r2`

Rescue-efficacy analysis of the 27 T1 errors per system in the cross-sectional M2 evaluation. GPT-5 Thinking corrected 13/27 (48.2%; 95% CI 30.74%-66.01%); the between-model difference was not statistically significant (Fisher exact P=.41).

> "The T2 rescue model, Gemini 2.5 Pro, successfully corrected 9 (33.3%) of its T1 errors, achieving a rescue rate of 33.3% (95% CI 18.64%-52.18%)."

### Kirchberger Michael Constantin MD; Mavragani Amaryllis 2026 (2)

Kirchberger Michael Constantin MD; Mavragani Amaryllis. (2026). A 2-Tiered Rescue Protocol to Mitigate Difficulty-Based Failures of ChatGPT (GPT-5) and Gemini on the German M2 Medical Examination: Evaluation Study. JMIR Formative Research. https://doi.org/10.2196/86999

`q3 · i?` · `design · r2`

Authors' descriptive interpretation in the discussion of rescue performance on difficulty level 4-5 errors; the overall rescue-rate difference was not statistically significant (P=.41), so this is presented as descriptive, not a tested contrast.

> "the GPT-5 Thinking system’s superior rate was descriptively driven by its success on these high-difficulty items (rescuing 63.6% of level 4 or 5 errors, vs 30% for Gemini Pro 2.5)"

## Discussion


## Related Claims
- [Gemini 2.5 Flash and GPT-5 Instant achieve identical 91.5% baseline accuracy on the German M2 examination but share only 16 of their 27 errors](t1-identical-accuracy-divergent-errors-m2.md) — related
- [LLM accuracy on the German M2 falls sharply with human-rated question difficulty, and the inverse relationship persists after rescue](accuracy-inversely-related-to-question-difficulty.md) — related
- [GPT-5 Instant takes significantly longer on items it answers incorrectly while Gemini 2.5 Flash shows no such hesitation](gpt5-instant-hesitation-on-incorrect-answers.md) — related
- [The relationship between question difficulty and response latency is absent for Gemini Flash and weakly positive for GPT-5 Instant](difficulty-latency-correlation-model-specific.md) — related
- [Gemini 2.5 Flash responds significantly faster than GPT-5 Instant on the German M2 examination](gemini-flash-faster-latency-than-gpt5-instant.md) — related
