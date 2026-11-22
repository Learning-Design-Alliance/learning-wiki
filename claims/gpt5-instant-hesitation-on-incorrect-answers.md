---
type: claim
title: GPT-5 Instant takes significantly longer on items it answers incorrectly while Gemini 2.5 Flash shows no such hesitation
description: GPT-5 Instant takes significantly longer on items it answers incorrectly while Gemini 2.5 Flash shows no such hesitation
id: gpt5-instant-hesitation-on-incorrect-answers
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
    kind: associational
    rigour: 2
---

# GPT-5 Instant takes significantly longer on items it answers incorrectly while Gemini 2.5 Flash shows no such hesitation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` GPT-5 Instant expended significantly more time on incorrect answers than correct ones (P=.002), whereas Gemini 2.5 Flash's latency for incorrect answers was indistinguishable from correct answers (P=.81). [→ Kirchberger Michael Constantin MD; Mavragani Amaryllis 2026](#kirchberger-michael-constantin-md-mavragani-amaryllis-2026)

## Evidence

### Kirchberger Michael Constantin MD; Mavragani Amaryllis 2026

Kirchberger Michael Constantin MD; Mavragani Amaryllis. (2026). A 2-Tiered Rescue Protocol to Mitigate Difficulty-Based Failures of ChatGPT (GPT-5) and Gemini on the German M2 Medical Examination: Evaluation Study. JMIR Formative Research. https://doi.org/10.2196/86999

`q3 · i?` · `associational · r2`

Within-model latency comparison of correct versus incorrect responses using the Mann-Whitney U test. GPT-5 Instant medians were 2.00 s (incorrect) versus 1.00 s (correct); Gemini Flash showed no difference (P=.81), which the authors describe as a rapid, confidently wrong retrieval error.

> "GPT-5 Instant expended significantly more time (median 2.00 s, IQR 1.00-3.00 s) on the 27 items it answered incorrectly than the 289 items it answered correctly (median 1.00 s; IQR 1.00-2.00 s, P=.002)."

## Discussion


## Related Claims
- [The relationship between question difficulty and response latency is absent for Gemini Flash and weakly positive for GPT-5 Instant](difficulty-latency-correlation-model-specific.md) — related
- [Gemini 2.5 Flash responds significantly faster than GPT-5 Instant on the German M2 examination](gemini-flash-faster-latency-than-gpt5-instant.md) — related
- [Gemini 2.5 Flash and GPT-5 Instant achieve identical 91.5% baseline accuracy on the German M2 examination but share only 16 of their 27 errors](t1-identical-accuracy-divergent-errors-m2.md) — related
- [The 2-tiered rescue protocol corrects roughly one-third to one-half of T1 errors, raising final accuracy to 94.3% (Gemini) and 95.6% (GPT-5) with no significant system difference](two-tier-rescue-raises-final-accuracy.md) — related
- [Reasoning models performed best for case generation but were unsuitable for real-time patient simulation due to long response latency](reasoning-models-latency-unsuitable-simulator.md) — related
