---
type: claim
title: Prompt refinement significantly improves GPT-3.5 agreement with human rater 1 but not, statistically, with rater 2
description: Prompt refinement significantly improves GPT-3.5 agreement with human rater 1 but not, statistically, with rater 2
id: scaffolded-cot-significance-by-rater
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: mixed
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: zhongzhou-chen-and-tong-wan-2024
    resource: "https://doi.org/10.1119/perc.2024.pr.chen"
    title: "Zhongzhou Chen and Tong Wan. (2024). Achieving Human Level Partial Credit Grading of Written Responses to Physics Conceptual Question using GPT-3.5 with Only Prompt Engineering. [doi:10.1119/perc.2024.pr.chen](https://doi.org/10.1119/perc.2024.pr.chen)"
    author: Zhongzhou Chen and Tong Wan
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: zhongzhou-chen-and-tong-wan-2024-2
    resource: "https://doi.org/10.1119/perc.2024.pr.chen"
    title: "Zhongzhou Chen and Tong Wan. (2024). Achieving Human Level Partial Credit Grading of Written Responses to Physics Conceptual Question using GPT-3.5 with Only Prompt Engineering. [doi:10.1119/perc.2024.pr.chen](https://doi.org/10.1119/perc.2024.pr.chen)"
    author: Zhongzhou Chen and Tong Wan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Prompt refinement significantly improves GPT-3.5 agreement with human rater 1 but not, statistically, with rater 2

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Cochran's Q test (p = 0.004) and Friedman's test (p = 0.031) show agreement with human rater 1 improves significantly across prompt versions. [→ Zhongzhou Chen and Tong Wan 2024](#zhongzhou-chen-and-tong-wan-2024)
`q2 i?` Against human rater 2 the improvement is not statistically significant (Cochran's Q p = 0.050, near threshold; Friedman's p = 0.062), though QWK still improves from moderate to substantial. [→ Zhongzhou Chen and Tong Wan 2024 (2)](#zhongzhou-chen-and-tong-wan-2024-2)

## Evidence

### Zhongzhou Chen and Tong Wan 2024

Zhongzhou Chen and Tong Wan. (2024). Achieving Human Level Partial Credit Grading of Written Responses to Physics Conceptual Question using GPT-3.5 with Only Prompt Engineering. [doi:10.1119/perc.2024.pr.chen](https://doi.org/10.1119/perc.2024.pr.chen)

`q2 · i?` · `causal · r1`

Cochran's Q test on percent agreement and Friedman's test on SMD distributions across the 40 graded responses for the three prompt versions against human rater 1, both reaching significance as printed.

> "Statistical tests also confirmed that the agreement (or disagreement) with human rater 1 was improved by refining the prompt (p = 0.004 for Cochran's Q and p = 0.031 for Friedman's)"

### Zhongzhou Chen and Tong Wan 2024 (2)

Zhongzhou Chen and Tong Wan. (2024). Achieving Human Level Partial Credit Grading of Written Responses to Physics Conceptual Question using GPT-3.5 with Only Prompt Engineering. [doi:10.1119/perc.2024.pr.chen](https://doi.org/10.1119/perc.2024.pr.chen)

`q2 · i?` · `design · r2`

The same tests against human rater 2 do not reach significance as printed; the article notes the QWK nonetheless shows scaffolded COT improving agreement with rater 2 from moderate to substantial.

> "When compared with human rater 2, the result from the Cochran's Q test (p = 0.050) is very close to the significance threshold, while the result from Friedman's test (p = 0.062) shows that the improvement is not significant"

## Discussion


## Related Claims
- [Scaffolded COT prompting brings GPT-3.5 grading agreement with human raters to 70%-80%, comparable to agreement between two human raters](scaffolded-cot-human-level-agreement-gpt35-grading.md) — related
- [GPT-4 achieved almost perfect inter-rater reliability with faculty after three iterations of rubric engineering on three of four medical school OEQ questions](gpt4-almost-perfect-irr-after-rubric-engineering.md) — a narrower finding that bears on this claim
- [The human-refined framework improved human agreement substantially but produced only modest gains for ICL-based LLM annotation](human-refined-framework-gains-humans-not-llms.md) — related
- [In-context learning did not consistently improve LLM annotation reliability over zero-shot prompting for engagement coding](icl-no-better-than-zero-shot-engagement-coding.md) — related
