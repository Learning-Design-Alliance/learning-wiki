---
type: claim
title: End-to-end fine-tuning improves error identification, and o1-mini surpasses it in exact match but performs worse on the Hausdorff distance metric
description: End-to-end fine-tuning improves error identification, and o1-mini surpasses it in exact match but performs worse on the Hausdorff distance metric
id: mathedu-error-identification-end-to-end-and-o1-mini
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

# End-to-end fine-tuning improves error identification, and o1-mini surpasses it in exact match but performs worse on the Hausdorff distance metric

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The end-to-end fine-tuned model outperformed Llama3 8B without rationale and showed noticeable improvements with rationale for locating erroneous equations. [→ Wei-Ling Hsu 2026](#wei-ling-hsu-2026)
`q2 i?` o1-mini surpassed the end-to-end model in error identification exact match but performed worse in the distance metric, misidentifying formulas in unfinished-problem cases. [→ Wei-Ling Hsu 2026 (2)](#wei-ling-hsu-2026-2)

## Evidence

### Wei-Ling Hsu 2026

Wei-Ling Hsu, Yu-Chien Tang, An-Zi Yen. (2026). MathEDU: Feedback Generation on Problem-Solving Processes for Mathematical Learning Support. Originally published 2025. [doi:10.18653/v1/2026.eacl-long.132](https://doi.org/10.18653/v1/2026.eacl-long.132)

`q2 · i?` · `design · r2`

Error identification evaluated by exact match and Hausdorff distance between model-detected and manually annotated error spans. The end-to-end model with rationale reached 40.12% EM versus Llama3 8B's 11.73%; the article reports "noticeable improvements with rationale". No effect size is printed.

> "In contrast, the end-to-end model outper-formed Llama3 8B without rationale and showed noticeable improvements with rationale. This result indicates that fine-tuning with this approach helps the model better understand and utilize rationale for error identification."

### Wei-Ling Hsu 2026 (2)

Wei-Ling Hsu, Yu-Chien Tang, An-Zi Yen. (2026). MathEDU: Feedback Generation on Problem-Solving Processes for Mathematical Learning Support. Originally published 2025. [doi:10.18653/v1/2026.eacl-long.132](https://doi.org/10.18653/v1/2026.eacl-long.132)

`q2 · i?` · `design · r2`

Comparison of o1-mini against the fine-tuned end-to-end model on error identification metrics. o1-mini achieved 41.98% EM but a 56.30 distance; the article explains it "performed worse in terms of the distance metric" because it misidentified formulas in unfinished problems. No effect size is printed.

> "o1-mini demonstrated stronger mathematical rea-soning and understanding abilities, surpassing the end-to-end model. However, it performed worse in terms of the distance metric."

## Discussion


## Related Claims
- [LoRA fine-tuning a small LLM significantly improves answer correctness classification over prompted baselines, with the single-task model with rationale significantly outperforming Llama3 70B without rationale](mathedu-finetuning-improves-correctness-classification.md) — related
- [In one essay-feedback system, fine-tuned models produced no usable deep-level feedback output, so only directly prompted LLMs were evaluated; the authors suggest prompting may be more effective than supervised fine-tuning for this task](sft-less-effective-than-prompting-for-feedback-generation.md) — related
- [Model grading performance does not exhibit a clear correlation with student proficiency levels on MathEDU](mathedu-performance-uncorrelated-with-student-proficiency.md) — related
