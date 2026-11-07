---
type: claim
title: "LLM accuracy on pediatric residency-level MCQs varies widely (38%–90%) across models when all questions are delivered simultaneously"
description: "LLM accuracy on pediatric residency-level MCQs varies widely (38%–90%) across models when all questions are delivered simultaneously"
id: all-at-once-llm-accuracy-38-90
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: vinson-2026
    resource: "https://doi.org/10.1038/s41598-026-48326-4"
    title: "Vinson, J., Caronia, C., & Savargaonkar, R. (2026). Input structure–driven instability and convergence in large language model clinical reasoning: a formative study using pediatric residency–level MCQs. Scientific Reports. https://doi.org/10.1038/s41598-026-48326-4"
    author: "Vinson, J., Caronia, C., & Savargaonkar, R."
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# LLM accuracy on pediatric residency-level MCQs varies widely (38%–90%) across models when all questions are delivered simultaneously

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person
> **Design limits** · Vinson 2026: groups were assigned but students were analysed as independent (read from the study by two models, 2026-11-04)

## Subclaims
`q2 i?` In the all-at-once condition, model accuracy ranged from 38% (Gemini) to 90% (Perplexity), with significant inter-model differences. [→ Vinson 2026](#vinson-2026)

## Evidence

### Vinson 2026

Vinson, J., Caronia, C., & Savargaonkar, R. (2026). Input structure–driven instability and convergence in large language model clinical reasoning: a formative study using pediatric residency–level MCQs. Scientific Reports. https://doi.org/10.1038/s41598-026-48326-4

`q2 · i?` · `causal · r1`

Cross-sectional comparative evaluation of six publicly available LLMs on 77 validated pediatric MCQs, all-at-once condition. The article reports accuracy from 38% (Gemini) to 90% (Perplexity) and a significant ANOVA (F(4,380) = 23.441, ρ < 0.001). No effect size printed, so impact is coded i? (no magnitude reported; not a null effect).

> "Accuracy ranged from 38% (Gemini) to 90% (Perplexity). DeepSeek demonstrated high performance (87%), while ChatGPT (GPT-4 Turbo) achieved moderate accuracy (62%). Copilot (GPT-4 Bing implementation) scored 44%. ANOVA demonstrated significant differences across models (F(4,380) = 23.441, ρ < 0.001)"

## Discussion


## Related Claims
- [Gemini 2.5 Pro achieved the highest accuracy (92.44%) on pediatric dentistry DUS questions, significantly outperforming most other LLMs](gemini-2-5-pro-highest-accuracy-pediatric-dus.md) — related
- [ChatGPT-5.1, DeepSeek-R1, and Gemini 2.5 Flash show high, statistically comparable accuracy on Turkish Pharmacy Specialty Examination questions](llms-high-comparable-accuracy-eus.md) — related
- [Batch delivery of ten questions converges LLM accuracy to 83%–88% with no statistically significant inter-model differences](batch-delivery-convergence-83-88.md) — related
- [Expert physician review excluded 23 of 100 LLM-generated MCQs, yielding a validated set of 77 questions](physician-validation-77-mcqs.md) — related
- [LLM performance was weakest in paediatric urology and testicular cancer and strongest in research methodology and andrology](llm-subspecialty-weaknesses-paediatric-urology-testicular-cancer.md) — related
- [Prior studies report widely varying ChatGPT diagnostic accuracy in dentistry (11% to 99%), likely due to differences in question types and content](prior-chatgpt-dental-accuracy-studies-vary-11-to-99-percent.md) — related
