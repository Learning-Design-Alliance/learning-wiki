---
type: claim
title: LLaMA and Qwen converge on the same bias hierarchy despite different training pipelines, suggesting a systemic property of large-scale language modeling
description: LLaMA and Qwen converge on the same bias hierarchy despite different training pipelines, suggesting a systemic property of large-scale language modeling
id: cross-model-convergence-bias-hierarchy
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
    i: "?"
    kind: causal
    rigour: 2
---

# LLaMA and Qwen converge on the same bias hierarchy despite different training pipelines, suggesting a systemic property of large-scale language modeling

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Both models exhibited the same bias hierarchy — Essay > Math > Programming by subject and Informal > Non-native Phrasing > Grammar by perturbation type — despite divergent training data and origins. [→ Rudra Jadhav 2026](#rudra-jadhav-2026)

## Evidence

### Rudra Jadhav 2026

Rudra Jadhav, Janhavi Danve, and Sonalika Shaw. (2026). Implicit Grading Bias in Large Language Models: How Writing Style Affects Automated Assessment Across Math, Programming, and Essay Tasks. Preprint. [doi:10.48550/arXiv.2603.18765](https://doi.org/10.48550/arXiv.2603.18765)

`q2 · i?` · `causal · r2`

Cross-model comparison across the 18 conditions shows pattern convergence despite different training pipelines (Meta vs. Alibaba). The article states this convergence "suggests a systemic property of large-scale language modeling rather than an artifact of any single pipeline", while bias magnitudes diverged (LLaMA higher).

> "Both LLaMA 3.3 70B and Qwen 2.5 72B exhibited the same overall bias hierarchy: Essay > Math > Program- ming by subject, and Informal > Non-native Phrasing > Grammar by perturbation type."

## Discussion


## Related Claims
- [Informal language receives the heaviest grading penalty among perturbation types, with deductions up to 1.90 points on a 10-point scale](informal-language-heaviest-grading-penalty.md) — a narrower finding that bears on this claim
- [LLMs show statistically significant grading bias for Essay/Writing tasks across all writing-style perturbation types, with large effect sizes](llm-essay-grading-style-bias.md) — a narrower finding that bears on this claim
- [LLM grading bias follows a subjectivity gradient: near-zero bias for Programming and Math, severe bias for Essay/Writing, consistent across both models](llm-grading-subjectivity-gradient.md) — a narrower finding that bears on this claim
