---
type: claim
title: LLMs show statistically significant grading bias for Essay/Writing tasks across all writing-style perturbation types, with large effect sizes
description: LLMs show statistically significant grading bias for Essay/Writing tasks across all writing-style perturbation types, with large effect sizes
id: llm-essay-grading-style-bias
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
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

# LLMs show statistically significant grading bias for Essay/Writing tasks across all writing-style perturbation types, with large effect sizes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2` · `i3` large
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i3` All six Essay/Writing conditions across both models reached statistical significance with effect sizes exceeding d = 0.8, up to d = 4.25. [→ Rudra Jadhav 2026](#rudra-jadhav-2026)

## Evidence

### Rudra Jadhav 2026

Rudra Jadhav, Janhavi Danve, and Sonalika Shaw. (2026). Implicit Grading Bias in Large Language Models: How Writing Style Affects Automated Assessment Across Math, Programming, and Essay Tasks. Preprint. [doi:10.48550/arXiv.2603.18765](https://doi.org/10.48550/arXiv.2603.18765)

`q2 · i3` · `causal · r2`

Controlled perturbation experiment: 180 responses (3x3x20 design) graded by LLaMA 3.3 70B and Qwen 2.5 72B with paired t-tests per condition. The article reports "All six Essay/Writing conditions across both models achieved statistical significance" with the largest effect d = 4.25 (LLaMA, informal).

> "All six Essay/Writing conditions across both models achieved statistical significance (p <0.05), with effect sizes uniformly exceeding conventional thresholds for "large" effects (d >0.8)."

## Discussion


## Related Claims
- [LLaMA and Qwen converge on the same bias hierarchy despite different training pipelines, suggesting a systemic property of large-scale language modeling](cross-model-convergence-bias-hierarchy.md) — a broader claim this one bears on
- [Informal language receives the heaviest grading penalty among perturbation types, with deductions up to 1.90 points on a 10-point scale](informal-language-heaviest-grading-penalty.md) — a narrower finding that bears on this claim
- [LLM grading bias follows a subjectivity gradient: near-zero bias for Programming and Math, severe bias for Essay/Writing, consistent across both models](llm-grading-subjectivity-gradient.md) — a broader claim this one bears on
- [Explicit prompt-level anti-bias instructions fail to prevent style-based grading bias in LLMs](prompt-instructions-fail-to-debias-llm-grading.md) — related
