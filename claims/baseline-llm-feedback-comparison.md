---
type: claim
title: "Among baseline LLMs integrated without fine-tuning or prompt pooling, falcon3:10b and llama3.2:3b achieved the highest BERTScore F1"
description: "Among baseline LLMs integrated without fine-tuning or prompt pooling, falcon3:10b and llama3.2:3b achieved the highest BERTScore F1"
id: baseline-llm-feedback-comparison
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
sources:
  - id: vikrant-sahu-2025
    resource: "https://doi.org/10.1145/3799830.3799878"
    title: Vikrant Sahu 2025
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Among baseline LLMs integrated without fine-tuning or prompt pooling, falcon3:10b and llama3.2:3b achieved the highest BERTScore F1

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In the baseline evaluation, falcon3:10b (0.7435) and llama3.2:3b (0.7235) achieved the highest BERTScore F1 values, while qwen3:8b and phi4-reasoning lagged in precision and recall. [→ Vikrant Sahu 2025](#vikrant-sahu-2025)

## Evidence

### Vikrant Sahu 2025

Vikrant Sahu, Dr. Gagan Raj Gupta, Raghav Borikar, and Nitin Mane. 2025. Autograder+: A Multi-Faceted AI Framework for Rich Pedagogical Feedback in Programming Education. CODS '25. [doi:10.1145/3799830.3799878](https://doi.org/10.1145/3799830.3799878)

`q2 · i?` · `design · r2`

Baseline evaluation of five LLMs integrated directly into the pipeline without fine-tuning or prompt pooling, on the 600-submission evaluation set (Table 3). The article reports "falcon3:10b[49] (0.7435) andllama3.2:3b[36] (0.7235) achieve the highest BERTScore F1 values"; no effect size is printed, so impact is coded i? (no magnitude reported; not a null effect).

> "Among the tested models,falcon3:10b[49] (0.7435) andllama3.2:3b[36] (0.7235) achieve the highest BERTScore F1 values, indicating stronger semantic alignment with human feedback"

## Discussion


## Related Claims
- [Domain fine-tuning did not outperform strong base LLMs for feedback generation and mostly slightly reduced performance](fine-tuning-no-gain-over-base-models.md) — related
- [Prompt pooling raises both lexical and semantic alignment of LLM feedback with TA-written gold-standard feedback across models](prompt-pooling-raises-feedback-alignment.md) — related
