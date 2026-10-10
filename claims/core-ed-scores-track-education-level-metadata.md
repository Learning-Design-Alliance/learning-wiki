---
type: claim
title: Core-Ed Edu-QuRater scores vary sensibly with education-level metadata on out-of-sample materials (marginal Pearson correlations 0.62 and 0.64; six-dimension cross-validated R2 of 0.449)
description: Core-Ed Edu-QuRater scores vary sensibly with education-level metadata on out-of-sample materials (marginal Pearson correlations 0.62 and 0.64; six-dimension cross-validated R2 of 0.449)
id: core-ed-scores-track-education-level-metadata
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
    i: 3
    kind: associational
    rigour: 2
---

# Core-Ed Edu-QuRater scores vary sensibly with education-level metadata on out-of-sample materials (marginal Pearson correlations 0.62 and 0.64; six-dimension cross-validated R2 of 0.449)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2` · `i3` large

## Subclaims
`q2 i3` On ~15,800 external educational materials, Overall Education Level and Primary-level Suitability scores correlate with education-level metadata at r = 0.62 and r = 0.64, and a linear model combining all six dimensions achieves a cross-validated R2 of 0.449. [→ Garrod 2026](#garrod-2026)

## Evidence

### Garrod 2026

Garrod, O. G. B., Ince, R. A. A., Liu, M., Huti, M., Boos, M., Waldock, A., Andrews, D., Alonso-Kropil, R., & Atherton, P. (2026). Edu-QuRating: Multi-Dimensional Educational Data Curation with Distilled Pairwise Judgements. arXiv. https://arxiv.org/abs/2609.09425

`q2 · i3` · `associational · r2`

Correlational analysis of Edu-QuRater scores on ~15,800 out-of-sample educational materials with reliable metadata annotations, separate from the distillation corpus. The article reports marginal Pearson correlations of r = 0.62 and r = 0.64 for the two strongest dimensions, and a cross-validated R2 of 0.449 for the combined six-dimension model.

> "Marginal Pearson correlations between education level metadata and Core-Ed dimensions are highest for these two dimensions (0.62 and 0.64 respectively). A linear model of education level metadata which combines all six dimensions achieved a cross-validatedR2 of 0.449"

## Discussion


## Related Claims
- [Core-Ed dimensions capture part of the FineWeb-Edu scalar signal while remaining not individually redundant with it (six-dimension cross-validated R2 of 0.228)](core-ed-dimensions-decompose-fineweb-edu-signal.md) — related
- [The pairwise-distillation procedure transfers to foundational-literacy scoring, with Gemma-3-4B-PT validation losses of 0.128 (student-facing) and 0.175 (teacher-facing)](foundational-literacy-edu-quraters-distill-successfully.md) — related
- [Edu-QuRaters recover held-out GPT-4.1-mini pairwise educational preferences from single-text scores, with mean accuracy rising from 0.895 (Sheared-LLaMA-1.3B) to 0.917 (Gemma-3-4B-PT)](edu-quraters-distill-pairwise-educational-preferences.md) — related
- [Cross-validation-selected hyperparameters generalized to the test set only for Situation and Clarity, with the other four dimensions showing CV–test misalignment](cv-test-misalignment-small-imbalanced-data.md) — related
- [Distillation validation loss decreases sharply from 20k to 200k pairwise examples and plateaus beyond 200k for the Sheared-LLaMA-1.3B base model](edu-qurating-200k-pairwise-examples-practical-scale.md) — related
- [In matched single-run 1B pre-training comparisons, all Edu-QuRating-based mixtures reach higher observed aggregate accuracy at 30k steps than the FineWeb-Edu baseline, with gains concentrated in specific tasks](edu-qurating-filtered-pretraining-higher-endpoints.md) — related
- [In held-out pairwise judge evaluation, combining Edu-QuRater and answer-structure GRPO rewards yields the highest pedagogical-quality win rate (81.08%) while retaining instruction-following above parity (68.24%) against the Qwen3-4B base model](edu-qurater-grpo-rewards-improve-responses.md) — related
