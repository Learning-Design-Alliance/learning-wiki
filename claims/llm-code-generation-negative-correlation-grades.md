---
type: claim
title: LLM use for code generation is significantly negatively correlated with student final grades
description: LLM use for code generation is significantly negatively correlated with student final grades
id: llm-code-generation-negative-correlation-grades
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: jošt-2024
    resource: "https://doi.org/10.3390/app14104115"
    title: "Jošt, G.; Taneski, V.; Karakatič, S. (2024). The Impact of Large Language Models on Programming Education and Student Learning Outcomes. Appl. Sci. 14, 4115. https://doi.org/10.3390/app14104115"
    author: Jošt, G.; Taneski, V.; Karakatič, S.
    q: 3
    i: "?"
    kind: causal
    rigour: 1
---

# LLM use for code generation is significantly negatively correlated with student final grades

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q3`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` Use of LLMs for generating code correlates negatively with final grades (Spearman's rho = -0.305, p = 0.045). [→ Jošt 2024](#jost-2024)

## Evidence

### Jošt 2024

Jošt, G.; Taneski, V.; Karakatič, S. (2024). The Impact of Large Language Models on Programming Education and Student Learning Outcomes. Appl. Sci. 14, 4115. https://doi.org/10.3390/app14104115

`q3 · i?` · `causal · r1`

One-sided Spearman correlation with bootstrap confidence intervals from the same thirty-two-participant experiment; the confidence interval (−0.595, −0.058) excludes zero. The article prints "Spearman's rho = −0.305, p = 0.045".

> "the analysis revealed a significant inverse relationship between the use of LLMs for generating code and final grades (Spearman's rho = −0.305, p = 0.045)"

## Discussion


## Related Claims

- [Higher average LLM use across all tasks is significantly negatively correlated with final grades in undergraduate programming education](average-llm-use-negative-correlation-final-grades.md) — a broader claim this one bears on
- [LLM use for debugging is significantly negatively correlated with student final grades](llm-debugging-negative-correlation-grades.md) — related
- [LLM use for seeking additional explanations does not significantly impact final grades](llm-explanations-no-significant-grade-impact.md) — related
- [A downward trend in final grades is observed with increased average LLM use across all task types](downward-grade-trend-increased-average-llm-use.md)
