---
type: claim
title: "Generated feedback across models shows a considerable gap from teacher-written feedback: fine-tuned models score near zero on LLM rating, and human experts rate all model feedback below the ideal score of 3"
description: "Generated feedback across models shows a considerable gap from teacher-written feedback: fine-tuned models score near zero on LLM rating, and human experts rate all model feedback below the ideal score of 3"
id: mathedu-feedback-generation-gap-from-teachers
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
  - id: wei-ling-hsu-2026-2
    resource: "https://doi.org/10.18653/v1/2026.eacl-long.132"
    title: "Wei-Ling Hsu, Yu-Chien Tang, An-Zi Yen. (2026). MathEDU: Feedback Generation on Problem-Solving Processes for Mathematical Learning Support. Originally published 2025. [doi:10.18653/v1/2026.eacl-long.132](https://doi.org/10.18653/v1/2026.eacl-long.132)"
    author: Wei-Ling Hsu, Yu-Chien Tang, An-Zi Yen
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Generated feedback across models shows a considerable gap from teacher-written feedback: fine-tuned models score near zero on LLM rating, and human experts rate all model feedback below the ideal score of 3

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Larger models such as Llama3 70B and GPT-3.5 do not outperform Llama3 8B on feedback generation, indicating generating teacher-like feedback remains challenging even for high-capacity models. [→ Wei-Ling Hsu 2026](#wei-ling-hsu-2026)
`q2 i?` In human expert evaluation, responses from language models remain below the ideal score of 3, with models struggling especially with Calculation Errors. [→ Wei-Ling Hsu 2026 (2)](#wei-ling-hsu-2026-2)

## Evidence

### Wei-Ling Hsu 2026

Wei-Ling Hsu, Yu-Chien Tang, An-Zi Yen. (2026). MathEDU: Feedback Generation on Problem-Solving Processes for Mathematical Learning Support. Originally published 2025. [doi:10.18653/v1/2026.eacl-long.132](https://doi.org/10.18653/v1/2026.eacl-long.132)

`q2 · i?` · `design · r2`

Feedback generation evaluated with ROUGE-L, BERTScore, and GPT-4 LLM Rating (0-5) against ground-truth teacher suggestions. Fine-tuned single-task and multi-task models scored near zero (e.g., multi-task LLM rating 0.08); the article states larger models "do not outperform Llama3 8B". No effect size is printed.

> "Larger models such as Llama3 70B and GPT-3.5 do not outperform Llama3 8B as expected, suggesting that generating teacher-like feedback remains a challenging task even for high-capacity models."

### Wei-Ling Hsu 2026 (2)

Wei-Ling Hsu, Yu-Chien Tang, An-Zi Yen. (2026). MathEDU: Feedback Generation on Problem-Solving Processes for Mathematical Learning Support. Originally published 2025. [doi:10.18653/v1/2026.eacl-long.132](https://doi.org/10.18653/v1/2026.eacl-long.132)

`q2 · i?` · `design · r2`

Human evaluation by three mathematics experts on a 0-3 helpfulness scale (Krippendorff's Alpha 0.7628) of feedback from Llama3 70B, GPT-3.5, o1-mini, and the end-to-end model. Ratings "remain below the ideal score of 3"; models struggled with Calculation Errors. No effect size is printed.

> "The responses from language models remain be-low the ideal score of 3. All models excelled at handling "Lack of Necessary Mathematical Concept" errors, since these cases only require gen-erating the correct solution and explanation."

## Discussion


## Related Claims
- [The proposed framework outperforms fine-tuned BERT, Instructor-LM, GPT-4, and RAPT on TeacherEval-2023 across consistency, credibility, calibration, and fairness metrics](llm-teacher-assessment-outperforms-baselines-teachereval.md) — related
- [Supervised fine-tuning on misconception-faithful demonstrations sharply improves SFS (up to +0.555 on Malrule for Qwen3-4B)](sft-improves-selective-update-behavior.md) — related
- [Supervised fine-tuning does not outperform zero-shot prompting on rubric score for math feedback generation, and ROUGE-L and BERTScore are unreliable estimates of feedback quality.](sft-ineffective-reference-metrics-unreliable.md) — related
- [LLM student simulators exhibit near-zero Selective Flip Score, flipping at similarly high rates under targeted, misaligned, and generic feedback](llm-simulators-near-zero-sfs-indiscriminate-flipping.md) — related
- [Model grading performance does not exhibit a clear correlation with student proficiency levels on MathEDU](mathedu-performance-uncorrelated-with-student-proficiency.md) — related
