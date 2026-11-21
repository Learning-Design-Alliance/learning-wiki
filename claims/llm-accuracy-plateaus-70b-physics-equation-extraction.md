---
type: claim
title: "LLM accuracy on physics equation extraction increases with model size but plateaus at approximately 85% around 70B parameters for thinking models"
description: "LLM accuracy on physics equation extraction increases with model size but plateaus at approximately 85% around 70B parameters for thinking models"
id: llm-accuracy-plateaus-70b-physics-equation-extraction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: lachlan-mcginness-and-peter-baumgartner-2025
    resource: "https://doi.org/10.1103/v8f8-s11v"
    title: "Lachlan McGinness and Peter Baumgartner. (2025). Can Large Language Models Correctly Interpret Equations with Errors?. [doi:10.1103/v8f8-s11v](https://doi.org/10.1103/v8f8-s11v)"
    author: Lachlan McGinness and Peter Baumgartner
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# LLM accuracy on physics equation extraction increases with model size but plateaus at approximately 85% around 70B parameters for thinking models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Accuracy increases with model size, with a plateau of roughly 85% at approximately 70B parameters for thinking models. [→ Lachlan McGinness and Peter Baumgartner 2025](#lachlan-mcginness-and-peter-baumgartner-2025)

## Evidence

### Lachlan McGinness and Peter Baumgartner 2025

Lachlan McGinness and Peter Baumgartner. (2025). Can Large Language Models Correctly Interpret Equations with Errors?. [doi:10.1103/v8f8-s11v](https://doi.org/10.1103/v8f8-s11v)

`q2 · i?` · `causal · r2`

Systematic experiments with twelve open-source models from 1B to 671B parameters using four prompting techniques on the Olympiad equation-extraction task; results are plotted with sigmoid trend functions in Figure 2. The paper states there is "a plateau of approximately 85% accuracy" at about 70B parameters.

> "Accuracy of LLMs increases with model size, but there is a plateau of approximately 85% accuracy which occurs at approximately 70B parameters for thinking models."

## Discussion


## Related Claims
- [Smaller LLMs more often used undefined symbols, missed equations, and hallucinated equations; a 14B parameter model (Phi4) achieved only about 70% accuracy on the task](small-llms-undefined-symbols-phi4-70-percent.md) — related
- [Under identical LoRA hyperparameters and training data, the 27B Gemma model outperforms the 70B LLaMA model on every computed essay-scoring metric](model-scale-not-predictor-lora-scoring.md) — related
- [LLM grading performance generally correlates with parameter count, and 4-bit quantization has negligible effect on grading performance](llm-grading-performance-scales-with-parameters.md) — a broader claim this one bears on
