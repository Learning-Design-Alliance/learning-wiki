---
type: claim
title: Edu-QuRaters recover held-out GPT-4.1-mini pairwise educational preferences from single-text scores, with mean accuracy rising from 0.895 (Sheared-LLaMA-1.3B) to 0.917 (Gemma-3-4B-PT)
description: Edu-QuRaters recover held-out GPT-4.1-mini pairwise educational preferences from single-text scores, with mean accuracy rising from 0.895 (Sheared-LLaMA-1.3B) to 0.917 (Gemma-3-4B-PT)
id: edu-quraters-distill-pairwise-educational-preferences
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
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

# Edu-QuRaters recover held-out GPT-4.1-mini pairwise educational preferences from single-text scores, with mean accuracy rising from 0.895 (Sheared-LLaMA-1.3B) to 0.917 (Gemma-3-4B-PT)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across two base models and six criteria, trained Edu-QuRaters recover held-out pairwise preferences with both base models exceeding 0.86 accuracy on every criterion, and Gemma-3-4B-PT improving accuracy uniformly across every criterion. [→ Garrod 2026](#garrod-2026)

## Evidence

### Garrod 2026

Garrod, O. G. B., Ince, R. A. A., Liu, M., Huti, M., Boos, M., Waldock, A., Andrews, D., Alonso-Kropil, R., & Atherton, P. (2026). Edu-QuRating: Multi-Dimensional Educational Data Curation with Distilled Pairwise Judgements. arXiv. https://arxiv.org/abs/2609.09425

`q2 · i?` · `design · r2`

Numerical evaluation on 50,000 held-out GPT-4.1-mini pairs per criterion, where each Edu-QuRater scores texts independently and the sign of the score difference determines the implied winner. The article reports "Mean accuracy rises from 0.895 for Sheared-LLaMA-1.3B to 0.917 for Gemma-3-4B-PT."

> "Across the two base models and six criteria, Edu-QuRaters recover the held-out pairwise preferences with high accuracy (Figure 2). Both base models exceed 0.86 accuracy on every criterion. Mean accuracy rises from 0.895 for Sheared-LLaMA-1.3B to 0.917 for Gemma-3-4B-PT."

## Discussion


## Related Claims
- [Core-Ed Edu-QuRater scores vary sensibly with education-level metadata on out-of-sample materials (marginal Pearson correlations 0.62 and 0.64; six-dimension cross-validated R2 of 0.449)](core-ed-scores-track-education-level-metadata.md) — related
- [In held-out pairwise judge evaluation, combining Edu-QuRater and answer-structure GRPO rewards yields the highest pedagogical-quality win rate (81.08%) while retaining instruction-following above parity (68.24%) against the Qwen3-4B base model](edu-qurater-grpo-rewards-improve-responses.md) — related
- [Distillation validation loss decreases sharply from 20k to 200k pairwise examples and plateaus beyond 200k for the Sheared-LLaMA-1.3B base model](edu-qurating-200k-pairwise-examples-practical-scale.md) — related
- [The pairwise-distillation procedure transfers to foundational-literacy scoring, with Gemma-3-4B-PT validation losses of 0.128 (student-facing) and 0.175 (teacher-facing)](foundational-literacy-edu-quraters-distill-successfully.md) — related
- [Edu-QuRater rewards alone raise pedagogical-quality win rate (77.70%) but fall below parity on instruction following (40.54%), consistent with over-optimizing a proxy reward](edu-qurater-rewards-alone-below-parity-instruction-following.md) — related
- [In matched single-run 1B pre-training comparisons, all Edu-QuRating-based mixtures reach higher observed aggregate accuracy at 30k steps than the FineWeb-Edu baseline, with gains concentrated in specific tasks](edu-qurating-filtered-pretraining-higher-endpoints.md) — related
