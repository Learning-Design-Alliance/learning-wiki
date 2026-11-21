---
type: claim
title: Model grading performance does not exhibit a clear correlation with student proficiency levels on MathEDU
description: Model grading performance does not exhibit a clear correlation with student proficiency levels on MathEDU
id: mathedu-performance-uncorrelated-with-student-proficiency
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
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

# Model grading performance does not exhibit a clear correlation with student proficiency levels on MathEDU

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across six students, model performance on correctness classification, error identification, and feedback generation did not clearly correlate with student proficiency; the highest-performing student yielded the lowest error-identification performance. [→ Wei-Ling Hsu 2026](#wei-ling-hsu-2026)

## Evidence

### Wei-Ling Hsu 2026

Wei-Ling Hsu, Yu-Chien Tang, An-Zi Yen. (2026). MathEDU: Feedback Generation on Problem-Solving Processes for Mathematical Learning Support. Originally published 2025. [doi:10.18653/v1/2026.eacl-long.132](https://doi.org/10.18653/v1/2026.eacl-long.132)

`q2 · i?` · `design · r2`

Per-student analysis (Tables 6-8) of Llama3 8B and the end-to-end fine-tuned model across six student annotators categorized into three proficiency levels. The article reports "the lowest model performance in error identification" for the highest-performing student. No effect size is printed.

> "Model performance does not exhibit a clear cor-relation with student proficiency levels. S2, de-spite being the highest-performing student, yields the lowest model performance in error identifica-tion."

## Discussion


## Related Claims
- [End-to-end fine-tuning improves error identification, and o1-mini surpasses it in exact match but performs worse on the Hausdorff distance metric](mathedu-error-identification-end-to-end-and-o1-mini.md) — related
- [LoRA fine-tuning a small LLM significantly improves answer correctness classification over prompted baselines, with the single-task model with rationale significantly outperforming Llama3 70B without rationale](mathedu-finetuning-improves-correctness-classification.md) — related
- [Generated feedback across models shows a considerable gap from teacher-written feedback: fine-tuned models score near zero on LLM rating, and human experts rate all model feedback below the ideal score of 3](mathedu-feedback-generation-gap-from-teachers.md) — related
- [Accurate LLM solution diagnosis does not reliably produce pedagogically actionable feedback, with lowest rubric scores on error identification and actionability](accurate-diagnosis-not-actionable-feedback.md) — related
