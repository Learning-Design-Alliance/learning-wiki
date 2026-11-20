---
type: claim
title: Tailored prompt engineering consistently outperforms base models and chain-of-thought prompting across four LLMs for educational emotion and behavior analysis
description: Tailored prompt engineering consistently outperforms base models and chain-of-thought prompting across four LLMs for educational emotion and behavior analysis
id: prompt-engineering-outperforms-baselines-llm-emotion-analysis
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: kaito-tanaka-2024
    resource: "https://doi.org/10.48550/arXiv.2408.06874"
    title: "Kaito Tanaka, Benjamin Tan, Brian Wong. (2024). Leveraging Language Models for Emotion and Behavior Analysis in Education. [doi:10.48550/arXiv.2408.06874](https://doi.org/10.48550/arXiv.2408.06874)"
    author: Kaito Tanaka, Benjamin Tan, Brian Wong
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Tailored prompt engineering consistently outperforms base models and chain-of-thought prompting across four LLMs for educational emotion and behavior analysis

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across Qwen, ChatGPT, Claude2, and GPT-4, the proposed prompt-based method achieved higher accuracy and contextual scores than both the base model and the CoT method. [→ Kaito Tanaka 2024](#kaito-tanaka-2024)

## Evidence

### Kaito Tanaka 2024

Kaito Tanaka, Benjamin Tan, Brian Wong. (2024). Leveraging Language Models for Emotion and Behavior Analysis in Education. [doi:10.48550/arXiv.2408.06874](https://doi.org/10.48550/arXiv.2408.06874)

`q2 · i?` · `causal · r1`

Experimental comparison reported in Section 4.2 and Table 1, evaluating the prompt-based method against a base model and chain-of-thought prompting on four LLMs using accuracy and a GPT-4 based contextual scoring metric. The article reports the method "consistently outperformed the base model and the CoT method across all four LLMs".

> "Our proposed method consistently outperformed the base model and the CoT method across all four LLMs. The results demonstrate that prompt engineering significantly enhances the models' ability to accurately infer students' emotional and engagement states."

## Discussion


## Related Claims
- [On GPT-4, the prompt-based method reaches 88.3% accuracy versus 71.0% for the base model and 77.2% for chain-of-thought prompting](gpt4-prompt-method-88-3-accuracy.md) — a narrower finding that bears on this claim
- [The prompt-based method achieves contextual relevance scores of 0.89 to 0.92 across the four LLMs on the GPT-4 based scoring metric](llm-contextual-scores-089-092.md) — a narrower finding that bears on this claim
- [GPT-4's chain-of-thought reasoning, captured via structured output, was consistently reliable and appeared to provide logical, context-grounded justification usable for prompt tuning and end-user insight](gpt4-cot-reasoning-reliable-transparent.md) — related
- [The prompt-based method correctly identified subtle mixed-emotion and nuanced-feedback cues that the base model and CoT method missed](prompt-method-captures-subtle-emotion-cues.md) — a narrower finding that bears on this claim
