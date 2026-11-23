---
type: claim
title: The relationship between question difficulty and response latency is absent for Gemini Flash and weakly positive for GPT-5 Instant
description: The relationship between question difficulty and response latency is absent for Gemini Flash and weakly positive for GPT-5 Instant
id: difficulty-latency-correlation-model-specific
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
evidence_strength: weak
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

# The relationship between question difficulty and response latency is absent for Gemini Flash and weakly positive for GPT-5 Instant

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` A Spearman rank correlation found no statistically significant difficulty-latency association for Gemini Flash (P=.19) but a weak, statistically significant positive correlation for GPT-5 Instant (P=.004). [→ Kirchberger Michael Constantin MD; Mavragani Amaryllis 2026](#kirchberger-michael-constantin-md-mavragani-amaryllis-2026)

## Evidence

### Kirchberger Michael Constantin MD; Mavragani Amaryllis 2026

Kirchberger Michael Constantin MD; Mavragani Amaryllis. (2026). A 2-Tiered Rescue Protocol to Mitigate Difficulty-Based Failures of ChatGPT (GPT-5) and Gemini on the German M2 Medical Examination: Evaluation Study. JMIR Formative Research. https://doi.org/10.2196/86999

`q3 · i?` · `design · r2`

Spearman rank correlation between the AMBOSS difficulty rating and T1 response latency across the 316 examination items; no correlation coefficient is printed, so only the significance tests are reported. The article states GPT-5 Instant tended to take slightly longer on harder questions.

> "A Spearman rank correlation test found no statistically significant association for Gemini Flash (P=.19). For GPT-5 Instant, a weak but statistically significant positive correlation was detected (P=.004)"

## Discussion


## Related Claims
- [LLM accuracy on the German M2 falls sharply with human-rated question difficulty, and the inverse relationship persists after rescue](accuracy-inversely-related-to-question-difficulty.md) — related
- [GPT-5 Instant takes significantly longer on items it answers incorrectly while Gemini 2.5 Flash shows no such hesitation](gpt5-instant-hesitation-on-incorrect-answers.md) — related
- [Gemini 2.5 Flash responds significantly faster than GPT-5 Instant on the German M2 examination](gemini-flash-faster-latency-than-gpt5-instant.md) — related
- [Gemini 2.5 Flash and GPT-5 Instant achieve identical 91.5% baseline accuracy on the German M2 examination but share only 16 of their 27 errors](t1-identical-accuracy-divergent-errors-m2.md) — related
- [The 2-tiered rescue protocol corrects roughly one-third to one-half of T1 errors, raising final accuracy to 94.3% (Gemini) and 95.6% (GPT-5) with no significant system difference](two-tier-rescue-raises-final-accuracy.md) — related
- [Problem difficulty affects latency only in State 1, indicating a qualitative processing difference between states](difficulty-effect-only-state-one.md) — related
