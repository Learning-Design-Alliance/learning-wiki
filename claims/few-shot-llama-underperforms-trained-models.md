---
type: claim
title: Few-shot LLaMA significantly underperforms even the traditional bag of words approach for skill classification
description: Few-shot LLaMA significantly underperforms even the traditional bag of words approach for skill classification
id: few-shot-llama-underperforms-trained-models
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: rebeckah-k-fussell-2025
    resource: "https://doi.org/10.1103/physrevphyseducres.21.010128"
    title: "Rebeckah K. Fussell, Megan Flynn, Anil Damle, Michael F.J. Fox, and N. G. Holmes. (2025). Comparing Large Language Models for supervised analysis of students’ lab notes. [doi:10.1103/physrevphyseducres.21.010128](https://doi.org/10.1103/physrevphyseducres.21.010128)"
    author: Rebeckah K. Fussell, Megan Flynn, Anil Damle, Michael F.J. Fox, and N. G. Holmes
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Few-shot LLaMA significantly underperforms even the traditional bag of words approach for skill classification

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The few-shot LLaMA model, with no fine-tuning, had balanced accuracy comparable to BERT and bag of words but much lower accuracy than any trained model for the QC code. [→ Rebeckah K. Fussell 2025](#rebeckah-k-fussell-2025)

## Evidence

### Rebeckah K. Fussell 2025

Rebeckah K. Fussell, Megan Flynn, Anil Damle, Michael F.J. Fox, and N. G. Holmes. (2025). Comparing Large Language Models for supervised analysis of students’ lab notes. [doi:10.1103/physrevphyseducres.21.010128](https://doi.org/10.1103/physrevphyseducres.21.010128)

`q2 · i?` · `design · r2`

Results section comparison for the QC code across five model types; the few-shot LLaMA used only four labeled examples and no fine-tuning. The article attributes under-performance partly to generalized training not supporting the coding scheme's specificity.

> "Overall, the few-shot model significantly underperformed even the traditional bag of words approach. The few-shot LLaMA model resulted in a balanced accuracy score comparable to that of BERT and bag of words and an accuracy score much lower than any of the trained models."

## Discussion


## Related Claims
- [Fine-tuned LLaMA models outperform bag of words and BERT across performance metrics for the QC code](llama-outperforms-bow-bert-qc-code.md) — related
- [In zero-shot evaluation, GPT-4's multi-label classification results were similar to what might be expected of fine-tuned classifiers, with SetFit and GPT-3.5 showing contrasting precision/recall patterns](gpt4-zero-shot-comparable-finetuned-classifiers.md) — related
- [LLMs show robust zero- and few-shot Bloom classification of OOD AI-assisted questions compared with ML and BERT models](llms-robust-ood-bloom-classification.md) — related
- [Zero-shot LLMs perform only marginally above random in five-class competency classification but exceed 70% accuracy on binary classification](zero-shot-llm-granularity-competency-classification.md) — related
- [Mid-range degradation is conditioned on task-specific adaptation: it is most severe for few-shot LLMs with few examples, decreases with more task-specific data, and is mildest for the fine-tuned encoder](task-specific-adaptation-conditions-mid-range-degradation.md) — a broader claim this one bears on
- [Adding a prompt to fine-tuned LLaMA yields performance similar to unprompted fine-tuned LLaMA](prompted-llama-similar-to-unprompted.md) — related
- [Source-free domain adaptation methods that succeed in computer vision underperform direct application of pre-trained models for retention prediction](sfda-underperforms-in-retention-prediction.md) — related
