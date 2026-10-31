---
type: claim
title: Few-shot LLM approaches outperform standalone supervised ML approaches, yet hand-crafted rules remain relevant
description: Few-shot LLM approaches outperform standalone supervised ML approaches, yet hand-crafted rules remain relevant
id: few-shot-llm-outperforms-ml-hcr-relevant
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-10-28
recheck_by: 2029
sources:
  - id: lehesvuori-2026
    resource: "https://doi.org/10.1007/s11423-025-10545-3"
    title: "Lehesvuori, S., Urrutia, F., Heilala, V., Araya, R., & Hämäläinen, R. (2026). Discovering technology-aided possibilities for automatic analysis of science teacher questions. Education Tech Research Dev. https://doi.org/10.1007/s11423-025-10545-3"
    author: "Lehesvuori, S., Urrutia, F., Heilala, V., Araya, R., & Hämäläinen, R."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Few-shot LLM approaches outperform standalone supervised ML approaches, yet hand-crafted rules remain relevant

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-28 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the whole dataset, GPT-3.5-turbo five-shot CoT outperformed standalone ML models, while hand-crafted rules and BoW+HCR combinations remained competitive. [→ Lehesvuori 2026](#lehesvuori-2026)

## Evidence

### Lehesvuori 2026

Lehesvuori, S., Urrutia, F., Heilala, V., Araya, R., & Hämäläinen, R. (2026). Discovering technology-aided possibilities for automatic analysis of science teacher questions. Education Tech Research Dev. https://doi.org/10.1007/s11423-025-10545-3

`q2 · i?` · `design · r2`

Whole-dataset comparison (Table 3): GPT-3.5-turbo 5-shot CoT reached F1 0.4302 and BA 0.8428, above standalone BoW and BERT models, while "HCR models are relevant in both sole and combination models (especially BoW + HCR)" with F1 0.431.

> "The results show that while GPT-3.5-turbo performs well, also HCR models are relevant in both sole and combination models (especially BoW + HCR)."

## Discussion


## Related Claims
- [Few-shot chain-of-thought prompting outperforms zero-shot prompting for detecting teacher questions](few-shot-cot-outperforms-zero-shot-question-detection.md) — related
- [In-context examples improve LLM Bloom classification: three-shot and ten-shot prompting score at or above zero-shot on every dataset tested, and above it in most comparisons](in-context-examples-improve-bloom-classification.md) — related
- [GPT-4 outperforms GPT-3.5-turbo in a single-lesson question-detection test](gpt4-outperforms-gpt35-single-lesson.md) — related
- [LLMs show robust zero- and few-shot Bloom classification of OOD AI-assisted questions compared with ML and BERT models](llms-robust-ood-bloom-classification.md) — a narrower finding that bears on this claim
- [In zero-shot evaluation, GPT-4's multi-label classification results were similar to what might be expected of fine-tuned classifiers, with SetFit and GPT-3.5 showing contrasting precision/recall patterns](gpt4-zero-shot-comparable-finetuned-classifiers.md) — related
- [Zero-shot LLMs perform only marginally above random in five-class competency classification but exceed 70% accuracy on binary classification](zero-shot-llm-granularity-competency-classification.md) — related
- [Supervised ML/DL Bloom question classifiers trained on one dataset drop substantially in weighted F1 when tested on unseen datasets](supervised-bloom-classifiers-degrade-cross-dataset.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
