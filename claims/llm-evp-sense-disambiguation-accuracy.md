---
type: claim
title: LLMs can identify the intended EVP meaning of polysemous words in context, with accuracy decreasing as the number of candidate meanings increases
description: LLMs can identify the intended EVP meaning of polysemous words in context, with accuracy decreasing as the number of candidate meanings increases
id: llm-evp-sense-disambiguation-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: stefano-bannò-2025
    resource: "https://doi.org/10.18653/v1/2025.bea-1.45"
    title: "Stefano Bannò, Kate M. Knill, Mark J. F. Gales. (2025). Exploiting the English Vocabulary Profile for L2 word-level vocabulary assessment with LLMs. arXiv. [doi:10.18653/v1/2025.bea-1.45](https://doi.org/10.18653/v1/2025.bea-1.45)"
    author: Stefano Bannò, Kate M. Knill, Mark J. F. Gales
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLMs can identify the intended EVP meaning of polysemous words in context, with accuracy decreasing as the number of candidate meanings increases

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In the semantic understanding proof-of-concept on EVP learner example sentences, GPT-4o achieves the best average accuracy (84.4%) and all models except Llama 3.1 8B perform strongly, with accuracy falling as options rise from 3 to 6. [→ Stefano Bannò 2025](#stefano-banno-2025)

## Evidence

### Stefano Bannò 2025

Stefano Bannò, Kate M. Knill, Mark J. F. Gales. (2025). Exploiting the English Vocabulary Profile for L2 word-level vocabulary assessment with LLMs. arXiv. [doi:10.18653/v1/2025.bea-1.45](https://doi.org/10.18653/v1/2025.bea-1.45)

`q2 · i?` · `design · r2`

Proof-of-concept experiment (Table 1) in which five LLMs select the contextually appropriate EVP meaning for words with 3–6 candidate senses, averaging softmax probabilities over option permutations. GPT-4o averages 84.4% accuracy, dropping from 89.0% at 3 options to 79.5% at 6 options; the article reports "Accuracy decreases as the number of options" grows.

> "All models show a remarkable performance for this task with the exception of Llama 3.1 8B. As expected, Accuracy decreases as the number of options available for a given word increases."

## Discussion


## Related Claims
- [Word-level analysis of high-frequency polysemous words suggests a strong degree of consistency in the CEFR classifications provided by the EVP](evp-consistency-work-like-accuracy.md) — related
- [GPT-4o and GPT-5.2 achieve higher accuracy and more fully correct answers on university IVDA multiple-choice questions than the smaller Mistral-7B and DeepSeek-R1 models](gpt-models-outperform-smaller-llms-on-ivda-mcqs.md) — related
- [The OpenAI gpt-4o reference model outperformed all quantised models on human-rated coherence, fluency, relevance and cultural appropriateness, serving as an upper benchmark](gpt-4o-reference-outperformed-quantised-models-human-ratings.md) — related
