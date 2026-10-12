---
type: research-method
id: varia-four-property-formalisation-of-the-aiaa-integrity-via-variation-hypothesis
title: VARIA four-property formalisation of the AIAA integrity-via-variation hypothesis
description: VARIA formalises the claim that an LLM can generate assessment variant sets that are simultaneously surface-distinct, construct-equivalent, rubric-applicable and difficulty-matched.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
---

# VARIA four-property formalisation of the AIAA integrity-via-variation hypothesis

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
VARIA formalises the claim that an LLM can generate assessment variant sets that are simultaneously surface-distinct, construct-equivalent, rubric-applicable and difficulty-matched. It "defines a blueprint as a triple of competency, analytic rubric, and canonical solution" and operationalises four properties P1-P4 with metrics (TF-IDF cosine and 4-gram overlap for diversity, an LLM judge for construct equivalence, Flesch reading-ease dispersion for difficulty parity) combined into a joint integrity score J. The framework makes the AIAA claim falsifiable: a generator fails if no prompting setting satisfies all four constraints jointly.

## Accounts
<!-- How each source describes or uses the method -->
- **VARIA four-property formalisation of the AIAA integrity-via-variation hypothesis**: VARIA formalises the claim that an LLM can generate assessment variant sets that are simultaneously surface-distinct, construct-equivalent, rubric-applicable and difficulty-matched. It "defines a blueprint as a triple of competency, analytic rubric, and canonical solution" and operationalises four properties P1-P4 with metrics (TF-IDF cosine and 4-gram overlap for diversity, an LLM judge for construct equivalence, Flesch reading-ease dispersion for difficulty parity) combined into a joint integrity score J. The framework makes the AIAA claim falsifiable: a generator fails if no prompting setting satisfies all four constraints jointly. (Ernesto Lee (2026))

### Claims
- [Frontier LLM prompting strategies cluster at joint integrity scores of 0.81-0.88 while non-frontier references collapse to 0.50-0.55, a 25-31 point capability-tier gap](../claims/varia-frontier-nonfrontier-tier-gap.md) [+M]
- [Under illustrative property thresholds, no prompting strategy passes all measured AIAA properties in every model-blueprint cell; few-shot anchoring passes only 2 of 9 cells](../claims/threshold-gating-no-strategy-fully-passes.md) [+M]

## Related Research Methods
-

## Key Sources
- Ernesto Lee. (2026). VARIA: Benchmarking Frontier LLMs on Construct-Equivalent Assessment Variant Generation. https://openrouter.ai
