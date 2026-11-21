---
type: claim
title: "Smaller LLMs more often used undefined symbols, missed equations, and hallucinated equations; a 14B parameter model (Phi4) achieved only about 70% accuracy on the task"
description: "Smaller LLMs more often used undefined symbols, missed equations, and hallucinated equations; a 14B parameter model (Phi4) achieved only about 70% accuracy on the task"
id: small-llms-undefined-symbols-phi4-70-percent
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
  - id: lachlan-mcginness-and-peter-baumgartner-2025-2
    resource: "https://doi.org/10.1103/v8f8-s11v"
    title: "Lachlan McGinness and Peter Baumgartner. (2025). Can Large Language Models Correctly Interpret Equations with Errors?. [doi:10.1103/v8f8-s11v](https://doi.org/10.1103/v8f8-s11v)"
    author: Lachlan McGinness and Peter Baumgartner
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Smaller LLMs more often used undefined symbols, missed equations, and hallucinated equations; a 14B parameter model (Phi4) achieved only about 70% accuracy on the task

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly
> **Design limits** · Lachlan McGinness and Peter Baumgartner 2025: the intervention came bundled with another change · Lachlan McGinness and Peter Baumgartner 2025 (2): no comparison group (read from the study by two models, 2026-11-21)

## Subclaims
`q2 i?` Smaller models were more likely than larger ones to use undefined symbols, miss an equation, and hallucinate equations. [→ Lachlan McGinness and Peter Baumgartner 2025](#lachlan-mcginness-and-peter-baumgartner-2025)
`q2 i?` Phi4, a 14B parameter model, completed the equation-extraction task at approximately 70% accuracy. [→ Lachlan McGinness and Peter Baumgartner 2025 (2)](#lachlan-mcginness-and-peter-baumgartner-2025-2)

## Evidence

### Lachlan McGinness and Peter Baumgartner 2025

Lachlan McGinness and Peter Baumgartner. (2025). Can Large Language Models Correctly Interpret Equations with Errors?. [doi:10.1103/v8f8-s11v](https://doi.org/10.1103/v8f8-s11v)

`q2 · i?` · `causal · r2`

Automated counting of error frequencies for models of 7, 14 and 70 billion parameters (Table II) shows most error types increase as model size decreases, with added equations the exception, remaining roughly constant across 7-70B parameters. The paper states "Smaller models were more likely to use undefined symbols".

> "Smaller models were more likely to use undefined symbols, miss an equation and hallucinate equations."

### Lachlan McGinness and Peter Baumgartner 2025 (2)

Lachlan McGinness and Peter Baumgartner. (2025). Can Large Language Models Correctly Interpret Equations with Errors?. [doi:10.1103/v8f8-s11v](https://doi.org/10.1103/v8f8-s11v)

`q2 · i?` · `causal · r2`

In the systematic experiments over the 200 typed Olympiad responses, the 14B Phi4 model reached approximately 70% accuracy on equation extraction. The paper reports that "a 14B parameter model (Phi4) was able to achieve this task with approximately 70% accuracy".

> "We found that a 14B parameter model (Phi4) was able to achieve this task with approximately 70% accuracy."

## Discussion


## Related Claims
- [Student references to a nonexistent attachment increased the chance that LLMs of all sizes hallucinated equations, the most common error type for large models](fictitious-attachment-references-trigger-llm-hallucinated-equations.md) — related
- [LLM accuracy on physics equation extraction increases with model size but plateaus at approximately 85% around 70B parameters for thinking models](llm-accuracy-plateaus-70b-physics-equation-extraction.md) — related
- [Scaling Qwen2.5 from 3B to 32B parameters improved both metrics and reduced the consistency gap by approximately 50%](model-scaling-reduces-consistency-gap.md) — related
- [In the fine-tuning experiments, increasing base model size up to 32B parameters improved performance, and larger LLMs consistently outperformed smaller MLMs](model-size-and-llm-vs-mlm-performance-vocabulary-difficulty.md) — related
- [GPT-4o and GPT-5.2 achieve higher accuracy and more fully correct answers on university IVDA multiple-choice questions than the smaller Mistral-7B and DeepSeek-R1 models](gpt-models-outperform-smaller-llms-on-ivda-mcqs.md) — related
