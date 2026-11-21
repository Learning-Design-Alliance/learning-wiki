---
type: claim
title: "LLM grading bias follows a subjectivity gradient: near-zero bias for Programming and Math, severe bias for Essay/Writing, consistent across both models"
description: "LLM grading bias follows a subjectivity gradient: near-zero bias for Programming and Math, severe bias for Essay/Writing, consistent across both models"
id: llm-grading-subjectivity-gradient
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
    i: "?"
    kind: causal
    rigour: 2
---

# LLM grading bias follows a subjectivity gradient: near-zero bias for Programming and Math, severe bias for Essay/Writing, consistent across both models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Bias magnitude increases sharply as the evaluation task becomes more subjective, with Programming showing virtually no bias (delta approximately 0.00) and Essay/Writing showing severe bias. [→ Rudra Jadhav 2026](#rudra-jadhav-2026)

## Evidence

### Rudra Jadhav 2026

Rudra Jadhav, Janhavi Danve, and Sonalika Shaw. (2026). Implicit Grading Bias in Large Language Models: How Writing Style Affects Automated Assessment Across Math, Programming, and Essay Tasks. Preprint. [doi:10.48550/arXiv.2603.18765](https://doi.org/10.48550/arXiv.2603.18765)

`q2 · i?` · `causal · r2`

Cross-subject analysis (Fig. 3) of the 18-condition experiment shows the "subjectivity gradient": Programming near-zero, Math slight, Essay severe. The article states the gradient "was consistent across both models". Only one non-Essay condition reached significance: Qwen Math non-native (d = 0.59, p = 0.017).

> "Programming tasks, with objectively verifiable outputs, show virtually no bias ( ∆≈0.00 across most conditions). Mathematics shows slight bias, primarily for informal language."

## Discussion


## Related Claims
- [LLaMA and Qwen converge on the same bias hierarchy despite different training pipelines, suggesting a systemic property of large-scale language modeling](cross-model-convergence-bias-hierarchy.md) — a broader claim this one bears on
- [LLMs show statistically significant grading bias for Essay/Writing tasks across all writing-style perturbation types, with large effect sizes](llm-essay-grading-style-bias.md) — a narrower finding that bears on this claim
- [Both LLMs correlate only weakly with human ground-truth scores overall, with agreement strongest for Programming and near-zero for Mathematics](weak-human-llm-grading-agreement.md) — related
