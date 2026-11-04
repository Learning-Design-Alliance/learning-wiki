---
type: research-method
id: sequential-batches-of-ten-for-llm-multiple-choice-evaluation
title: Sequential batches of ten for LLM multiple-choice evaluation
description: "This principle recommends administering multiple questions to LLMs sequentially in batches of ten rather than all at once, because the study found batch delivery converged accuracy to 83%–88% with no significant inter-model differences, while simultaneous delivery produced wide dispersion (38%–90%)."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-04
---

# Sequential batches of ten for LLM multiple-choice evaluation

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
This principle recommends administering multiple questions to LLMs sequentially in batches of ten rather than all at once, because the study found batch delivery converged accuracy to 83%–88% with no significant inter-model differences, while simultaneous delivery produced wide dispersion (38%–90%). The batch size of ten was "selected pragmatically to approximate typical USMLE exam pacing (approximately one question per minute) while remaining within context window limits." The article states this "substantially improves LLM response reproducibility and reduces cross-model variability."

## Accounts
<!-- How each source describes or uses the method -->
- **Deliver MCQs to LLMs in structured batches of ten to improve reproducibility and reduce cross-model variability**: This principle recommends administering multiple questions to LLMs sequentially in batches of ten rather than all at once, because the study found batch delivery converged accuracy to 83%–88% with no significant inter-model differences, while simultaneous delivery produced wide dispersion (38%–90%). The batch size of ten was "selected pragmatically to approximate typical USMLE exam pacing (approximately one question per minute) while remaining within context window limits." The article states this "substantially improves LLM response reproducibility and reduces cross-model variability." (Vinson et al. (2026))

### Claims
- [Batch delivery of ten questions converges LLM accuracy to 83%–88% with no statistically significant inter-model differences](../claims/batch-delivery-convergence-83-88.md) [+M]
- [Sequential delivery in batches of ten substantially reduces performance dispersion and instability across evaluated LLMs compared with simultaneous delivery](../claims/batch-delivery-reduces-instability.md) [+M]

## Related Research Methods
-

## Key Sources
- Vinson, J., Caronia, C., & Savargaonkar, R. (2026). Input structure–driven instability and convergence in large language model clinical reasoning: a formative study using pediatric residency–level MCQs. Scientific Reports. https://doi.org/10.1038/s41598-026-48326-4
