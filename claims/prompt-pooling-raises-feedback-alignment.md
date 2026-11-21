---
type: claim
title: Prompt pooling raises both lexical and semantic alignment of LLM feedback with TA-written gold-standard feedback across models
description: Prompt pooling raises both lexical and semantic alignment of LLM feedback with TA-written gold-standard feedback across models
id: prompt-pooling-raises-feedback-alignment
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

# Prompt pooling raises both lexical and semantic alignment of LLM feedback with TA-written gold-standard feedback across models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Adding prompt pooling to the Autograder+ pipeline improved BERTScore F1, precision, and SBERT cosine similarity across tested models, with falcon3-10B (Base) reaching the best lexical match (F1 = 0.7658, Precision = 0.7706). [→ Vikrant Sahu 2025](#vikrant-sahu-2025)

## Evidence

### Vikrant Sahu 2025

Vikrant Sahu, Dr. Gagan Raj Gupta, Raghav Borikar, and Nitin Mane. 2025. Autograder+: A Multi-Faceted AI Framework for Rich Pedagogical Feedback in Programming Education. CODS '25. [doi:10.1145/3799830.3799878](https://doi.org/10.1145/3799830.3799878)

`q2 · i?` · `design · r2`

Evaluation of enhanced configurations on 600 IITBh PC25 submissions against TA-written gold-standard feedback, reported in Table 5. The article reports that "prompt pooling, which raises both lexical (BERT F1/Precision) and semantic (SBERT cosine) scores across models"; no effect size is printed, so impact is coded i? (no magnitude reported; not a null effect).

> "The most consistent improvements come from prompt pooling, which raises both lexical (BERT F1/Precision) and semantic (SBERT cosine) scores across models, withfalcon3-10B (Base)achieving the best lexical match (F1 = 0.7658, Precision = 0.7706)"

## Discussion


## Related Claims
- [Among baseline LLMs integrated without fine-tuning or prompt pooling, falcon3:10b and llama3.2:3b achieved the highest BERTScore F1](baseline-llm-feedback-comparison.md) — related
