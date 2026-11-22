---
type: claim
title: "Gemini 2.5 Flash and GPT-5 Instant achieve identical 91.5% baseline accuracy on the German M2 examination but share only 16 of their 27 errors"
description: "Gemini 2.5 Flash and GPT-5 Instant achieve identical 91.5% baseline accuracy on the German M2 examination but share only 16 of their 27 errors"
id: t1-identical-accuracy-divergent-errors-m2
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: kirchberger-michael-constantin-md-mavragani-amaryllis-2026
    resource: "https://doi.org/10.2196/86999"
    title: "Kirchberger Michael Constantin MD; Mavragani Amaryllis. (2026). A 2-Tiered Rescue Protocol to Mitigate Difficulty-Based Failures of ChatGPT (GPT-5) and Gemini on the German M2 Medical Examination: Evaluation Study. JMIR Formative Research. https://doi.org/10.2196/86999"
    author: Kirchberger Michael Constantin MD; Mavragani Amaryllis
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# Gemini 2.5 Flash and GPT-5 Instant achieve identical 91.5% baseline accuracy on the German M2 examination but share only 16 of their 27 errors

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Both T1 models correctly answered 289 of 316 items (91.5%), with no statistically significant difference in error rates (McNemar P=.999), yet only 16 incorrect items overlapped. [→ Kirchberger Michael Constantin MD; Mavragani Amaryllis 2026](#kirchberger-michael-constantin-md-mavragani-amaryllis-2026)

## Evidence

### Kirchberger Michael Constantin MD; Mavragani Amaryllis 2026

Kirchberger Michael Constantin MD; Mavragani Amaryllis. (2026). A 2-Tiered Rescue Protocol to Mitigate Difficulty-Based Failures of ChatGPT (GPT-5) and Gemini on the German M2 Medical Examination: Evaluation Study. JMIR Formative Research. https://doi.org/10.2196/86999

`q3 · i?` · `design · r2`

Cross-sectional evaluation of all 316 items of the fall 2024 German M2 examination, including image-based questions, using zero-shot copy-paste prompting with strict exact-match scoring. Both T1 models scored "289 (91.5%) questions"; discordant errors were split 11 vs 11 (McNemar P=.999).

> "Gemini 2.5 Flash and GPT-5 Instant both correctly answered 289 (91.5%) questions, achieving an accuracy of 91.5% (95% CI 87.85%-94.06%) and committing 27 (8.5%) errors each."

## Discussion


## Related Claims
- [GPT-5 Instant takes significantly longer on items it answers incorrectly while Gemini 2.5 Flash shows no such hesitation](gpt5-instant-hesitation-on-incorrect-answers.md) — related
- [Gemini 2.5 Flash responds significantly faster than GPT-5 Instant on the German M2 examination](gemini-flash-faster-latency-than-gpt5-instant.md) — related
- [LLM accuracy on the German M2 falls sharply with human-rated question difficulty, and the inverse relationship persists after rescue](accuracy-inversely-related-to-question-difficulty.md) — related
- [The relationship between question difficulty and response latency is absent for Gemini Flash and weakly positive for GPT-5 Instant](difficulty-latency-correlation-model-specific.md) — related
- [The 2-tiered rescue protocol corrects roughly one-third to one-half of T1 errors, raising final accuracy to 94.3% (Gemini) and 95.6% (GPT-5) with no significant system difference](two-tier-rescue-raises-final-accuracy.md) — related
