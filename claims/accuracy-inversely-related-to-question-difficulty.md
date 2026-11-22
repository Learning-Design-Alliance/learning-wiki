---
type: claim
title: LLM accuracy on the German M2 falls sharply with human-rated question difficulty, and the inverse relationship persists after rescue
description: LLM accuracy on the German M2 falls sharply with human-rated question difficulty, and the inverse relationship persists after rescue
id: accuracy-inversely-related-to-question-difficulty
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
evidence_strength: strong
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: kirchberger-michael-constantin-md-mavragani-amaryllis-2026
    resource: "https://doi.org/10.2196/86999"
    title: "Kirchberger Michael Constantin MD; Mavragani Amaryllis. (2026). A 2-Tiered Rescue Protocol to Mitigate Difficulty-Based Failures of ChatGPT (GPT-5) and Gemini on the German M2 Medical Examination: Evaluation Study. JMIR Formative Research. https://doi.org/10.2196/86999"
    author: Kirchberger Michael Constantin MD; Mavragani Amaryllis
    q: 3
    i: 2
    kind: associational
    rigour: 2
  - id: kirchberger-michael-constantin-md-mavragani-amaryllis-2026-2
    resource: "https://doi.org/10.2196/86999"
    title: "Kirchberger Michael Constantin MD; Mavragani Amaryllis. (2026). A 2-Tiered Rescue Protocol to Mitigate Difficulty-Based Failures of ChatGPT (GPT-5) and Gemini on the German M2 Medical Examination: Evaluation Study. JMIR Formative Research. https://doi.org/10.2196/86999"
    author: Kirchberger Michael Constantin MD; Mavragani Amaryllis
    q: 3
    i: 1
    kind: associational
    rigour: 2
---

# LLM accuracy on the German M2 falls sharply with human-rated question difficulty, and the inverse relationship persists after rescue

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q3` · `i1`–`i2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i2` For every 1-point increase on the 5-point difficulty scale, the odds of a correct T1 response decreased by 42.1% for Gemini Flash (OR 0.579, 95% CI 0.425-0.788; P<.001) and 47.7% for GPT-5 Instant (OR 0.523, 95% CI 0.379-0.720; P<.001). [→ Kirchberger Michael Constantin MD; Mavragani Amaryllis 2026](#kirchberger-michael-constantin-md-mavragani-amaryllis-2026)
`q3 i1` The negative association persisted after rescue: final-response odds decreased significantly for the Gemini system (OR 0.633, 95% CI 0.442-0.909; P=.01) and the GPT-5 system (OR 0.550, 95% CI 0.360-0.840; P=.006). [→ Kirchberger Michael Constantin MD; Mavragani Amaryllis 2026 (2)](#kirchberger-michael-constantin-md-mavragani-amaryllis-2026-2)

## Evidence

### Kirchberger Michael Constantin MD; Mavragani Amaryllis 2026

Kirchberger Michael Constantin MD; Mavragani Amaryllis. (2026). A 2-Tiered Rescue Protocol to Mitigate Difficulty-Based Failures of ChatGPT (GPT-5) and Gemini on the German M2 Medical Examination: Evaluation Study. JMIR Formative Research. https://doi.org/10.2196/86999

`q3 · i2` · `associational · r2`

Logistic regression of T1 correctness on the AMBOSS 1-5 Hammer difficulty rating across 316 items. Descriptively, T1 accuracy fell from 98.9% at difficulty 1 to 81.3% (Gemini Flash) and 78.1% (GPT-5 Instant) at difficulty 5, with printed odds ratios of OR 0.579 and OR 0.523.

> "For every 1-point increase on the 5-point difficulty scale, the odds of a correct T1 response decreased by 42.1% for Gemini Flash (odds ratio [OR] 0.579, 95% CI 0.425-0.788; P<.001) and by 47.7% for GPT-5 Instant (OR 0.523, 95% CI 0.379-0.720; P<.001)."

### Kirchberger Michael Constantin MD; Mavragani Amaryllis 2026 (2)

Kirchberger Michael Constantin MD; Mavragani Amaryllis. (2026). A 2-Tiered Rescue Protocol to Mitigate Difficulty-Based Failures of ChatGPT (GPT-5) and Gemini on the German M2 Medical Examination: Evaluation Study. JMIR Formative Research. https://doi.org/10.2196/86999

`q3 · i1` · `associational · r2`

Post-rescue logistic regression on the same 316-item dataset showing the difficulty-accuracy relationship persisted after the T2 rescue step, with printed effect sizes OR 0.633 (Gemini system) and OR 0.550 (GPT-5 system).

> "The odds of a correct final (after rescue) response still decreased significantly for both the Gemini system (OR 0.633, 95% CI 0.442-0.909; P=.01) and the GPT-5 system (OR 0.550, 95% CI 0.360-0.840; P=.006)."

## Discussion


## Related Claims
- [The relationship between question difficulty and response latency is absent for Gemini Flash and weakly positive for GPT-5 Instant](difficulty-latency-correlation-model-specific.md) — related
- [Gemini 2.5 Flash and GPT-5 Instant achieve identical 91.5% baseline accuracy on the German M2 examination but share only 16 of their 27 errors](t1-identical-accuracy-divergent-errors-m2.md) — related
- [The 2-tiered rescue protocol corrects roughly one-third to one-half of T1 errors, raising final accuracy to 94.3% (Gemini) and 95.6% (GPT-5) with no significant system difference](two-tier-rescue-raises-final-accuracy.md) — related
