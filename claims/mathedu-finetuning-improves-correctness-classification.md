---
type: claim
title: LoRA fine-tuning a small LLM significantly improves answer correctness classification over prompted baselines, with the single-task model with rationale significantly outperforming Llama3 70B without rationale
description: LoRA fine-tuning a small LLM significantly improves answer correctness classification over prompted baselines, with the single-task model with rationale significantly outperforming Llama3 70B without rationale
id: mathedu-finetuning-improves-correctness-classification
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: wei-ling-hsu-2026
    resource: "https://doi.org/10.18653/v1/2026.eacl-long.132"
    title: "Wei-Ling Hsu, Yu-Chien Tang, An-Zi Yen. (2026). MathEDU: Feedback Generation on Problem-Solving Processes for Mathematical Learning Support. Originally published 2025. [doi:10.18653/v1/2026.eacl-long.132](https://doi.org/10.18653/v1/2026.eacl-long.132)"
    author: Wei-Ling Hsu, Yu-Chien Tang, An-Zi Yen
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LoRA fine-tuning a small LLM significantly improves answer correctness classification over prompted baselines, with the single-task model with rationale significantly outperforming Llama3 70B without rationale

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Fine-tuned Llama3 8B models achieve higher F-score in determining correctness than the non-fine-tuned Llama3 8B, and the single-task model with rationale significantly outperformed the Llama3 70B baseline (p < 0.001). [→ Wei-Ling Hsu 2026](#wei-ling-hsu-2026)

## Evidence

### Wei-Ling Hsu 2026

Wei-Ling Hsu, Yu-Chien Tang, An-Zi Yen. (2026). MathEDU: Feedback Generation on Problem-Solving Processes for Mathematical Learning Support. Originally published 2025. [doi:10.18653/v1/2026.eacl-long.132](https://doi.org/10.18653/v1/2026.eacl-long.132)

`q2 · i?` · `design · r2`

Evaluation on the MathEDU test set (603 examples) of LoRA fine-tuned Llama3 8B against prompted baselines, using F-score for correctness classification. The single-task model with rationale reached 95.07% F-score and "significantly outperformed the baseline, with p <0.001"; no effect size is printed.

> "We further conducted McNemar's test to assess the significance of differences between our fine-tuned models and the baseline Llama3 70B without rationale. The single-task model with rationale significantly outperformed the baseline, with p <0.001."

## Discussion


## Related Claims
- [End-to-end fine-tuning improves error identification, and o1-mini surpasses it in exact match but performs worse on the Hausdorff distance metric](mathedu-error-identification-end-to-end-and-o1-mini.md) — related
- [Under identical LoRA hyperparameters and training data, the 27B Gemma model outperforms the 70B LLaMA model on every computed essay-scoring metric](model-scale-not-predictor-lora-scoring.md) — related
- [Fine-tuned 8B LLMs generate K-2 stories with difficulty-related metric scores statistically significantly different from (mostly better than) zero-shot GPT-4o and Llama 3.3 70B](finetuned-8b-llms-beat-zero-shot-large-models-on-difficulty-metrics.md) — related
- [In one essay-feedback system, fine-tuned models produced no usable deep-level feedback output, so only directly prompted LLMs were evaluated; the authors suggest prompting may be more effective than supervised fine-tuning for this task](sft-less-effective-than-prompting-for-feedback-generation.md) — related
- [Model grading performance does not exhibit a clear correlation with student proficiency levels on MathEDU](mathedu-performance-uncorrelated-with-student-proficiency.md) — related
