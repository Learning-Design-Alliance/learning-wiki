---
type: claim
title: LLMs outperform a PoS-based baseline and a random baseline on word-level CEFR prediction of L2 learner writing, with the largest gains on ambiguous words
description: LLMs outperform a PoS-based baseline and a random baseline on word-level CEFR prediction of L2 learner writing, with the largest gains on ambiguous words
id: llms-beat-pos-baseline-word-level-cefr
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
source_checked: 2026-11-21
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

# LLMs outperform a PoS-based baseline and a random baseline on word-level CEFR prediction of L2 learner writing, with the largest gains on ambiguous words

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · checked against its sources 2026-11-21 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the OneStopEnglish word-level CEFR prediction task, LLMs (GPT-4o, Llama 3.1 70B, Qwen 2.5 32B) achieve higher overall accuracy than a PoS-based model and a random baseline, with Qwen 2.5 32B best at 87.0% overall and 80.5% on ambiguous words versus 80.7% and 66.7% for the PoS-based model. [→ Stefano Bannò 2025](#stefano-banno-2025)

## Evidence

### Stefano Bannò 2025

Stefano Bannò, Kate M. Knill, Mark J. F. Gales. (2025). Exploiting the English Vocabulary Profile for L2 word-level vocabulary assessment with LLMs. arXiv. [doi:10.18653/v1/2025.bea-1.45](https://doi.org/10.18653/v1/2025.bea-1.45)

`q2 · i?` · `design · r2`

Evaluation of word-level CEFR prediction on 293 annotated sentence triplets from OneStopEnglish (Table 2). Qwen 2.5 32B reaches 87.0% overall and 80.5% on ambiguous words, versus 80.7% and 66.7% for the PoS-based model and 61.6% overall for the random baseline; the authors note the "best performance on both ambiguous and overall cases" is by the LLMs.

> "However, the best performance on both ambiguous and overall cases is achieved – in increasing order – by GPT-4o, Llama 3.1 70B, and Qwen 2.5 32B."

## Discussion


## Related Claims
- [Word-level analysis of high-frequency polysemous words suggests a strong degree of consistency in the CEFR classifications provided by the EVP](evp-consistency-work-like-accuracy.md) — related
- [Word-level CEFR distributions predicted with an LLM differentiate essay-level proficiency bands better than PoS-based predictions and yield stronger holistic-score correlations on EFCAMDAT](llm-word-features-essay-proficiency-efcamdat.md) — related
- [Zero-shot LLMs perform only marginally above random in five-class competency classification but exceed 70% accuracy on binary classification](zero-shot-llm-granularity-competency-classification.md) — related
