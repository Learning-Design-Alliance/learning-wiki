---
type: claim
title: Gemini 2.5 Flash responds significantly faster than GPT-5 Instant on the German M2 examination
description: Gemini 2.5 Flash responds significantly faster than GPT-5 Instant on the German M2 examination
id: gemini-flash-faster-latency-than-gpt5-instant
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
---

# Gemini 2.5 Flash responds significantly faster than GPT-5 Instant on the German M2 examination

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` Gemini 2.5 Flash (mean 1.57, SD 1.06 s) was significantly faster than GPT-5 Instant (mean 2.07, SD 1.89 s; Wilcoxon signed-rank P<.001). [→ Kirchberger Michael Constantin MD; Mavragani Amaryllis 2026](#kirchberger-michael-constantin-md-mavragani-amaryllis-2026)

## Evidence

### Kirchberger Michael Constantin MD; Mavragani Amaryllis 2026

Kirchberger Michael Constantin MD; Mavragani Amaryllis. (2026). A 2-Tiered Rescue Protocol to Mitigate Difficulty-Based Failures of ChatGPT (GPT-5) and Gemini on the German M2 Medical Examination: Evaluation Study. JMIR Formative Research. https://doi.org/10.2196/86999

`q3 · i?` · `design · r2`

Paired latency comparison across the same 316 examination items; latency data were nonnormally distributed (Shapiro-Wilk P<.001 for both), so the Wilcoxon signed-rank test confirmed the difference (P<.001). The discussion reports Gemini Flash was 24.1% faster.

> "The Gemini 2.5 Flash model (mean 1.57, SD 1.06 s) was significantly faster than the GPT-5 Instant model (mean 2.07, SD 1.89 s)."

## Discussion


## Related Claims
- [The relationship between question difficulty and response latency is absent for Gemini Flash and weakly positive for GPT-5 Instant](difficulty-latency-correlation-model-specific.md) — related
- [GPT-5 Instant takes significantly longer on items it answers incorrectly while Gemini 2.5 Flash shows no such hesitation](gpt5-instant-hesitation-on-incorrect-answers.md) — related
- [Gemini 2.5 Flash and GPT-5 Instant achieve identical 91.5% baseline accuracy on the German M2 examination but share only 16 of their 27 errors](t1-identical-accuracy-divergent-errors-m2.md) — related
- [The 2-tiered rescue protocol corrects roughly one-third to one-half of T1 errors, raising final accuracy to 94.3% (Gemini) and 95.6% (GPT-5) with no significant system difference](two-tier-rescue-raises-final-accuracy.md) — related
