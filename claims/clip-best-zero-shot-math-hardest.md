---
type: claim
title: CLIP-RN50x64 is the best zero-shot model on STEM, outperforming GPT-3.5-Turbo by 5.9 percentage points, but math improves only marginally
description: CLIP-RN50x64 is the best zero-shot model on STEM, outperforming GPT-3.5-Turbo by 5.9 percentage points, but math improves only marginally
id: clip-best-zero-shot-math-hardest
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: jianhao-shen-2024
    resource: "https://doi.org/10.48550/arXiv.2402.17205"
    title: "Jianhao Shen, Ye Yuan, Srbuhi Mirzoyan, Ming Zhang, Chenguang Wang. (2024). MEASURING VISION-LANGUAGE STEM SKILLS OF NEURAL MODELS. Published as a conference paper at ICLR 2024. [doi:10.48550/arXiv.2402.17205](https://doi.org/10.48550/arXiv.2402.17205)"
    author: Jianhao Shen, Ye Yuan, Srbuhi Mirzoyan, Ming Zhang, Chenguang Wang
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# CLIP-RN50x64 is the best zero-shot model on STEM, outperforming GPT-3.5-Turbo by 5.9 percentage points, but math improves only marginally

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q3 i?` CLIP-RN50x64 achieves 18.0 percentage points over random guesses and outperforms GPT-3.5-Turbo by 5.9 points, while math shows only marginal improvement across all foundation models. [→ Jianhao Shen 2024](#jianhao-shen-2024)

## Evidence

### Jianhao Shen 2024

Jianhao Shen, Ye Yuan, Srbuhi Mirzoyan, Ming Zhang, Chenguang Wang. (2024). MEASURING VISION-LANGUAGE STEM SKILLS OF NEURAL MODELS. Published as a conference paper at ICLR 2024. [doi:10.48550/arXiv.2402.17205](https://doi.org/10.48550/arXiv.2402.17205)

`q3 · i?` · `design · r2`

Zero-shot evaluation of vision-language models on the STEM test sets (Table 2). CLIP-RN50x64 averages 54.9 versus GPT-3.5-Turbo's 49.0, while Virtex, 12-in-1, and ViLBERT perform near random guesses. The authors state math is the most challenging subject for current neural models.

> "CLIP-RN50x64 achieves the best result on STEM. It achieves 18.0% points improvements over random guesses. Notably, CLIP-RN50x64 outperforms GPT-3.5-Turbo by 5.9% points."

## Discussion


## Related Claims
- [Zero-shot LLMs perform only marginally above random in five-class competency classification but exceed 70% accuracy on binary classification](zero-shot-llm-granularity-competency-classification.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
- [Finetuning CLIP substantially boosts performance (+30 points on science and math) yet remains far below average elementary students](clip-finetuning-boost-still-below-students.md) — related
- Zero-shot CLIP accuracy improves with model size but saturates, indicating scaling alone is insufficient — related
