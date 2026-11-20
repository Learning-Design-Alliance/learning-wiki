---
type: claim
title: "On GPT-4, the prompt-based method reaches 88.3% accuracy versus 71.0% for the base model and 77.2% for chain-of-thought prompting"
description: "On GPT-4, the prompt-based method reaches 88.3% accuracy versus 71.0% for the base model and 77.2% for chain-of-thought prompting"
id: gpt4-prompt-method-88-3-accuracy
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
    kind: design
    rigour: 2
---

# On GPT-4, the prompt-based method reaches 88.3% accuracy versus 71.0% for the base model and 77.2% for chain-of-thought prompting

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the GPT-4 model, the proposed method achieved an ACC of 88.3%, higher than the base model's 71.0% and the CoT method's 77.2%. [→ Kaito Tanaka 2024](#kaito-tanaka-2024)

## Evidence

### Kaito Tanaka 2024

Kaito Tanaka, Benjamin Tan, Brian Wong. (2024). Leveraging Language Models for Emotion and Behavior Analysis in Education. [doi:10.48550/arXiv.2408.06874](https://doi.org/10.48550/arXiv.2408.06874)

`q2 · i?` · `design · r2`

Detailed results analysis in Section 4.4.1 reporting accuracy scores from the model comparison experiments. The article states "our method reaches an ACC of 88.3%" on GPT-4, attributing the improvement to tailored prompts that decompose the task into sub-tasks.

> "For instance, on the GPT-4 model, our method reaches an ACC of 88.3%, compared to 71.0% for the base model and 77.2% for the CoT method."

## Discussion


## Related Claims
- [Tailored prompt engineering consistently outperforms base models and chain-of-thought prompting across four LLMs for educational emotion and behavior analysis](prompt-engineering-outperforms-baselines-llm-emotion-analysis.md) — a broader claim this one bears on
- [Chain-of-thought prompting increases recall at the expense of precision for GPT-4 but lowers GPT-3.5 performance](cot-recall-precision-tradeoff-socratic.md) — related
