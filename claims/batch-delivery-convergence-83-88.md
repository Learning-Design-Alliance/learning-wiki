---
type: claim
title: "Batch delivery of ten questions converges LLM accuracy to 83%–88% with no statistically significant inter-model differences"
description: "Batch delivery of ten questions converges LLM accuracy to 83%–88% with no statistically significant inter-model differences"
id: batch-delivery-convergence-83-88
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

# Batch delivery of ten questions converges LLM accuracy to 83%–88% with no statistically significant inter-model differences

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Under batch delivery in sets of ten, accuracy ranged from 83% to 88% and ANOVA showed no significant differences across models. [→ Vinson 2026](#vinson-2026)

## Evidence

### Vinson 2026

Vinson, J., Caronia, C., & Savargaonkar, R. (2026). Input structure–driven instability and convergence in large language model clinical reasoning: a formative study using pediatric residency–level MCQs. Scientific Reports. https://doi.org/10.1038/s41598-026-48326-4

`q2 · i?` · `causal · r1`

Cross-sectional comparative evaluation of six LLMs on 77 validated pediatric MCQs, batch-of-ten condition. The article reports convergence to 83%–88% and a non-significant ANOVA (F(5,456) = 0.294, ρ = 0.916). No effect size printed, so impact is coded i? (no magnitude reported; not a null effect).

> "When questions were administered in smaller batches, accuracy markedly improved and converged across models, ranging from 83% to 88%. Copilot achieved the highest accuracy (88%), followed closely by ChatGPT, DeepSeek, and Perplexity (86–87%). Gemini and OpenEvidence performed at 83%. ANOVA demonstrated no significant differences (F(5,456) = 0.294, ρ = 0.916)"

## Discussion


## Related Claims
- [Sequential delivery in batches of ten substantially reduces performance dispersion and instability across evaluated LLMs compared with simultaneous delivery](batch-delivery-reduces-instability.md) — a broader claim this one bears on
- [LLM clinical reasoning performance is highly sensitive to input structure, with prompt structure a critical determinant of reliable behavior independent of model architecture](input-structure-determines-llm-reliability.md) — a broader claim this one bears on
- [LLM accuracy on pediatric residency-level MCQs varies widely (38%–90%) across models when all questions are delivered simultaneously](all-at-once-llm-accuracy-38-90.md) — related
- [Ten large language models achieved mean accuracies of 72–85% on the complete 300-item European Board of Hand Surgery written examination, with seven of ten reaching or exceeding an illustrative 75% pass threshold.](llm-ebhs-exam-accuracy-range-72-85-percent.md) — related
- [Expert physician review excluded 23 of 100 LLM-generated MCQs, yielding a validated set of 77 questions](physician-validation-77-mcqs.md) — related
