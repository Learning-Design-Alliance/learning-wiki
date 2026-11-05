---
type: claim
title: "Substantial within-model output instability was identified, most notably GPT-5.2 in female urology (SD ±22.8%) and anatomy (SD ±14.2%)"
description: "Substantial within-model output instability was identified, most notably GPT-5.2 in female urology (SD ±22.8%) and anatomy (SD ±14.2%)"
id: llm-output-instability-female-urology-anatomy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: kafagi-abdul-rhaman-atassi-nazih-kafagi-abdul-hadi-2026
    resource: "https://doi.org/10.1136/bmjopen-2025-108775"
    title: "Kafagi Abdul Rhaman; Atassi Nazih; Kafagi Abdul-Hadi. (2026). Performance of large language models (GPT-5.2, Gemini 3 Pro, Claude Sonnet 4.6 and Grok 4.1) on the Fellowship of The Royal College of Surgeons Urology Part A examination. BMJ Open. https://doi.org/10.1136/bmjopen-2025-108775"
    author: Kafagi Abdul Rhaman; Atassi Nazih; Kafagi Abdul-Hadi
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Substantial within-model output instability was identified, most notably GPT-5.2 in female urology (SD ±22.8%) and anatomy (SD ±14.2%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Within-model score variability across repeated runs was large in several domains, with GPT-5.2 showing SD ±22.8% in female urology and ±14.2% in anatomy, while some model–topic pairs achieved SD of zero. [→ Kafagi Abdul Rhaman; Atassi Nazih; Kafagi Abdul-Hadi 2026](#kafagi-abdul-rhaman-atassi-nazih-kafagi-abdul-hadi-2026)

## Evidence

### Kafagi Abdul Rhaman; Atassi Nazih; Kafagi Abdul-Hadi 2026

Kafagi Abdul Rhaman; Atassi Nazih; Kafagi Abdul-Hadi. (2026). Performance of large language models (GPT-5.2, Gemini 3 Pro, Claude Sonnet 4.6 and Grok 4.1) on the Fellowship of The Royal College of Surgeons Urology Part A examination. BMJ Open. https://doi.org/10.1136/bmjopen-2025-108775

`q2 · i?` · `design · r2`

Consistency secondary outcome from five independent runs per model, quantified by SD and 95% CIs via a sequential Monte Carlo sampling procedure. The discussion notes SD of zero in some domains, indicating "fully deterministic and reproducible performance in those areas".

> "Substantial within-model output instability was identified across several domains, most notably GPT-5.2 in female urology (SD±22.8%) and anatomy (SD±14.2%)."

## Discussion


## Related Claims
- [Smaller local LLMs show a minor position bias toward option ordering and partially guessing-like error variation, but accuracy remains relatively stable across permutations and repeated sampling runs](minor-position-bias-and-partial-guessing-in-small-llms.md) — related
- [Inter-run reliability of LLM performance on the EBHS examination was consistently high, with an overall mean Cohen's κ of 0.821 and no model falling below moderate agreement.](llm-ebhs-inter-run-reliability-high-kappa-0821.md) — reports the opposite
- [Self-Consistency is the most reproducible strategy across repeated runs yet shows weaker agreement with teacher mean scores (ICC (2,1) = 0.537)](sc-repeatable-but-weaker-agreement.md) — related
- [Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested](within-judge-stability-llm-rubric.md) — related
- [Item-by-implementation instability is substantial: a model can be reliable on some items and unreliable on others, varying across studies and training regimes](item-implementation-instability-scoring.md) — related
