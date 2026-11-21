---
type: claim
title: "On Google's Natural Questions long-answer test, Prompt-CoTBase attains a higher F1 score than GPT-4o and BERT"
description: "On Google's Natural Questions long-answer test, Prompt-CoTBase attains a higher F1 score than GPT-4o and BERT"
id: prompt-cotbase-higher-f1-natural-questions
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: wenqi-guan-and-yang-fang-2025
    resource: "https://doi.org/10.4108/eai.21-11-2024.2354589"
    title: "Wenqi Guan and Yang Fang. (2025). Optimizing Web-Based AI Query Retrieval with GPT Integration in LangChain: A CoT-Enhanced Prompt Engineering Approach. Originally published 2024. [doi:10.4108/eai.21-11-2024.2354589](https://doi.org/10.4108/eai.21-11-2024.2354589)"
    author: Wenqi Guan and Yang Fang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# On Google's Natural Questions long-answer test, Prompt-CoTBase attains a higher F1 score than GPT-4o and BERT

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` On Google's Natural Questions long-answer evaluation, Prompt-CoTBase reached an F1 score of 0.63, higher than GPT-4o's 0.48 and BERT's 0.51, with precision 67.12% and recall 60.03%. [→ Wenqi Guan and Yang Fang 2025](#wenqi-guan-and-yang-fang-2025)

## Evidence

### Wenqi Guan and Yang Fang 2025

Wenqi Guan and Yang Fang. (2025). Optimizing Web-Based AI Query Retrieval with GPT Integration in LangChain: A CoT-Enhanced Prompt Engineering Approach. Originally published 2024. [doi:10.4108/eai.21-11-2024.2354589](https://doi.org/10.4108/eai.21-11-2024.2354589)

`q2 · i?` · `design · r2`

Second benchmark experiment on Google's Natural Questions dataset (over 300,000 questions answered from Wikipedia), reported in Table 2. The authors state the enhanced model is "rather more comparable to human performance" particularly in recall and overall answer accuracy.

> "the F1 score of Prompt-CoTBase reaches 0.63, which is significantly higher than GPT-4o's 0.48 and BERT's 0.51, indicating our model's enhanced ability to provide accurate and relevant long answers."

## Discussion


## Related Claims
- [A LangChain-based Prompt-CoT model achieves higher accuracy than GPT-4o and BERT on the Paul Graham Essay question-answering benchmark](prompt-cotbase-outperforms-gpt4o-paul-graham-qa.md) — related
- [Few-shot chain-of-thought prompting outperforms zero-shot prompting for detecting teacher questions](few-shot-cot-outperforms-zero-shot-question-detection.md) — related
