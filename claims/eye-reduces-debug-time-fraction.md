---
type: claim
title: Using Eye for debugging data-structure programs reduces the fraction of debug time spent on a problem, with a marginal p-value of 0.0578
description: Using Eye for debugging data-structure programs reduces the fraction of debug time spent on a problem, with a marginal p-value of 0.0578
id: eye-reduces-debug-time-fraction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2021
sources:
  - id: aman-bansal-2021
    resource: "https://doi.org/10.1145/3408877.3439684"
    title: "Aman Bansal, Preey Shah, and Sahil Shah. (2021). Eye: Program Visualizer for CS2. arXiv preprint. [doi:10.1145/3408877.3439684](https://doi.org/10.1145/3408877.3439684)"
    author: Aman Bansal, Preey Shah, and Sahil Shah
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Using Eye for debugging data-structure programs reduces the fraction of debug time spent on a problem, with a marginal p-value of 0.0578

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Counterbalanced debugging experiment found a lower average fraction of total debug time for problems debugged with Eye, with p = 0.0578. [→ Aman Bansal 2021](#aman-bansal-2021)

## Evidence

### Aman Bansal 2021

Aman Bansal, Preey Shah, and Sahil Shah. (2021). Eye: Program Visualizer for CS2. arXiv preprint. [doi:10.1145/3408877.3439684](https://doi.org/10.1145/3408877.3439684)

`q2 · i?` · `causal · r1`

Counterbalanced online experiment with 20 senior CS undergraduates: half debugged Prob1 with Eye and Prob2 without, the other half the reverse. The article reports the p-value for the percentage-of-debug-time measure as 0.0578 and states "These results show that Eye improves debug time."

> "We consider these percentages to be random variables and test against the null hypothesis that the variables have the same mean for the two groups. We had to eliminate the four subjects who did not have alternating tool usage for the two problems."

## Discussion


## Related Claims
- [Proactive multimodal feedback significantly reduces debugging time on task compared to control](propact-feedback-reduces-debugging-time.md) — related
- [LLM-rewritten Python error messages improved subjective evaluations but did not reliably improve objective debugging performance](llm-error-rewrites-subjective-not-objective-gains.md) — related
- [Subjects estimated that debugging with Eye reduces frustration by 61.43% on average](eye-survey-frustration-reduction.md) — related
