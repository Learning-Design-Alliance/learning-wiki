---
type: claim
title: Informal language receives the heaviest grading penalty among perturbation types, with deductions up to 1.90 points on a 10-point scale
description: Informal language receives the heaviest grading penalty among perturbation types, with deductions up to 1.90 points on a 10-point scale
id: informal-language-heaviest-grading-penalty
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: rudra-jadhav-2026
    resource: "https://doi.org/10.48550/arXiv.2603.18765"
    title: "Rudra Jadhav, Janhavi Danve, and Sonalika Shaw. (2026). Implicit Grading Bias in Large Language Models: How Writing Style Affects Automated Assessment Across Math, Programming, and Essay Tasks. Preprint. [doi:10.48550/arXiv.2603.18765](https://doi.org/10.48550/arXiv.2603.18765)"
    author: Rudra Jadhav, Janhavi Danve, and Sonalika Shaw
    q: 2
    i: 3
    kind: causal
    rigour: 2
---

# Informal language receives the heaviest grading penalty among perturbation types, with deductions up to 1.90 points on a 10-point scale

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2` · `i3` large
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i3` Informal language was penalized more than grammar errors or non-native phrasing, with LLaMA deducting 1.90 points and Qwen 1.20 points on average in Essay tasks. [→ Rudra Jadhav 2026](#rudra-jadhav-2026)

## Evidence

### Rudra Jadhav 2026

Rudra Jadhav, Janhavi Danve, and Sonalika Shaw. (2026). Implicit Grading Bias in Large Language Models: How Writing Style Affects Automated Assessment Across Math, Programming, and Essay Tasks. Preprint. [doi:10.48550/arXiv.2603.18765](https://doi.org/10.48550/arXiv.2603.18765)

`q2 · i3` · `causal · r2`

Across the 18-condition perturbation experiment, the informal-language perturbation produced the largest score deltas; the article reports LLaMA deducting "an average of1.90 pointsand Qwen deducting1.20 pointson a 10-point scale". The largest single effect was LLaMA essay informal, d = 4.25.

> "Informal language received the heaviest penalty, with LLaMA deducting an average of1.90 pointsand Qwen deducting1.20 pointson a 10-point scale — penalties comparable to the difference between a B+ and C+ letter grade."

## Discussion


## Related Claims
- [LLaMA and Qwen converge on the same bias hierarchy despite different training pipelines, suggesting a systemic property of large-scale language modeling](cross-model-convergence-bias-hierarchy.md) — a broader claim this one bears on
- [LLMs show statistically significant grading bias for Essay/Writing tasks across all writing-style perturbation types, with large effect sizes](llm-essay-grading-style-bias.md) — a broader claim this one bears on
- [LLMs overrate short underdeveloped essays and over-penalize minor language errors in well-developed essays](llm-overrate-short-essays-overpenalize-errors.md) — related
- [LLMs in educational applications hallucinate in 15–25% of responses and can amplify bias against non-native language inputs](llm-hallucination-rate-education.md) — related
