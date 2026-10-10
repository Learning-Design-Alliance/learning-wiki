---
type: claim
title: The pairwise-distillation procedure transfers to foundational-literacy scoring, with Gemma-3-4B-PT validation losses of 0.128 (student-facing) and 0.175 (teacher-facing)
description: The pairwise-distillation procedure transfers to foundational-literacy scoring, with Gemma-3-4B-PT validation losses of 0.128 (student-facing) and 0.175 (teacher-facing)
id: foundational-literacy-edu-quraters-distill-successfully
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: garrod-2026
    resource: "https://arxiv.org/abs/2609.09425"
    title: "Garrod, O. G. B., Ince, R. A. A., Liu, M., Huti, M., Boos, M., Waldock, A., Andrews, D., Alonso-Kropil, R., & Atherton, P. (2026). Edu-QuRating: Multi-Dimensional Educational Data Curation with Distilled Pairwise Judgements. arXiv. https://arxiv.org/abs/2609.09425"
    author: "Garrod, O. G. B., Ince, R. A. A., Liu, M., Huti, M., Boos, M., Waldock, A., Andrews, D., Alonso-Kropil, R., & Atherton, P."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The pairwise-distillation procedure transfers to foundational-literacy scoring, with Gemma-3-4B-PT validation losses of 0.128 (student-facing) and 0.175 (teacher-facing)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Two literacy-facing Edu-QuRater families trained with the same pipeline reached low validation losses, and a qualitative sanity check on external materials showed structured variation by education level and material type. [→ Garrod 2026](#garrod-2026)

## Evidence

### Garrod 2026

Garrod, O. G. B., Ince, R. A. A., Liu, M., Huti, M., Boos, M., Waldock, A., Andrews, D., Alonso-Kropil, R., & Atherton, P. (2026). Edu-QuRating: Multi-Dimensional Educational Data Curation with Distilled Pairwise Judgements. arXiv. https://arxiv.org/abs/2609.09425

`q2 · i?` · `design · r2`

Application of the same pairwise-distillation pipeline to foundational-literacy rubric families (FL-Student and FL-Teacher), reporting the printed validation losses. A qualitative sanity check on external materials suggested the retargeted scorers are "not merely reproducing a single generic educational-quality signal."

> "The pipeline worked very similarly here. Gemma-3-4B-PT reached validation losses of 0.128 for student-facing literacy scoring and 0.175 for teacher-facing literacy scoring."

## Discussion


## Related Claims
- [Core-Ed Edu-QuRater scores vary sensibly with education-level metadata on out-of-sample materials (marginal Pearson correlations 0.62 and 0.64; six-dimension cross-validated R2 of 0.449)](core-ed-scores-track-education-level-metadata.md) — related
- [Edu-QuRaters recover held-out GPT-4.1-mini pairwise educational preferences from single-text scores, with mean accuracy rising from 0.895 (Sheared-LLaMA-1.3B) to 0.917 (Gemma-3-4B-PT)](edu-quraters-distill-pairwise-educational-preferences.md) — related
- [Distillation validation loss decreases sharply from 20k to 200k pairwise examples and plateaus beyond 200k for the Sheared-LLaMA-1.3B base model](edu-qurating-200k-pairwise-examples-practical-scale.md) — related
- [In matched single-run 1B pre-training comparisons, all Edu-QuRating-based mixtures reach higher observed aggregate accuracy at 30k steps than the FineWeb-Edu baseline, with gains concentrated in specific tasks](edu-qurating-filtered-pretraining-higher-endpoints.md) — related
