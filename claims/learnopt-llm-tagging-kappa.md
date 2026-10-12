---
type: claim
title: "Inter-model agreement on LLM skill tagging is moderate (Cohen's kappa 0.51), with strong agreement on S5 and disagreement concentrated in the S2/S3/S4 boundary"
description: "Inter-model agreement on LLM skill tagging is moderate (Cohen's kappa 0.51), with strong agreement on S5 and disagreement concentrated in the S2/S3/S4 boundary"
id: learnopt-llm-tagging-kappa
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: joy-bose-2025
    resource: "https://github.com/learnopt/learnopt"
    title: "Joy Bose, Om Thomas. (2025). LearnOpt: Recovering the Latent Cognitive Structure of Standardized Examinations via Knowledge Graphs and Constrained Optimization. https://github.com/learnopt/learnopt"
    author: Joy Bose, Om Thomas
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Inter-model agreement on LLM skill tagging is moderate (Cohen's kappa 0.51), with strong agreement on S5 and disagreement concentrated in the S2/S3/S4 boundary

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Two independently-prompted LLMs tagging the same 74 questions agree at kappa 0.51 (raw agreement 67.6%), with S5 agreement strong (80%) and disagreements concentrated in S2-vs-S3 and S4-vs-S3. [→ Joy Bose 2025](#joy-bose-2025)

## Evidence

### Joy Bose 2025

Joy Bose, Om Thomas. (2025). LearnOpt: Recovering the Latent Cognitive Structure of Standardized Examinations via Knowledge Graphs and Constrained Optimization. https://github.com/learnopt/learnopt

`q2 · i?` · `design · r2`

Reliability check computing Cohen's kappa between qwen2.5:7b and llama-3.1-8b-instant on 74 doubly-tagged questions at temperature 0 (Table 1: kappa 0.510, raw agreement 67.6%). The article reports S5 agreement at 80% and calls this an inter-model check, not a human gold standard.

> "A kappa of 0.51 falls in the "moderate" range (Landis & Koch, 1977). The confusion matrix shows this is not uniform noise but a structured pattern:"

## Discussion


## Related Claims
- [Systems Thinking Practices is the hardest CT construct to code reliably for both human raters and the LLM, requiring more explicitly operationalized rubrics](stp-low-reliability-complex-construct.md) — related
- [An LLM-based AI Evaluator agrees with expert human raters on collaboration transcripts at a level similar to inter-expert agreement](llm-evaluator-agreement-matches-expert-raters.md) — related
- [An independent human second coder reached moderate agreement (kappa = 0.395) with the AI-assisted primary coding on the five-category outcome](second-coder-moderate-agreement-kappa-0395.md) — related
- [Boundary compliance (S3) drives nearly all inter-model safety divergence, with a 53-point gap between the safest and least safe models](boundary-compliance-drives-safety-divergence-academiclaw.md) — related
