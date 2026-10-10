---
type: claim
title: "In held-out pairwise judge evaluation, combining Edu-QuRater and answer-structure GRPO rewards yields the highest pedagogical-quality win rate (81.08%) while retaining instruction-following above parity (68.24%) against the Qwen3-4B base model"
description: "In held-out pairwise judge evaluation, combining Edu-QuRater and answer-structure GRPO rewards yields the highest pedagogical-quality win rate (81.08%) while retaining instruction-following above parity (68.24%) again..."
id: edu-qurater-grpo-rewards-improve-responses
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
    kind: causal
    rigour: 1
---

# In held-out pairwise judge evaluation, combining Edu-QuRater and answer-structure GRPO rewards yields the highest pedagogical-quality win rate (81.08%) while retaining instruction-following above parity (68.24%) against the Qwen3-4B base model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` The combined Edu-QuRating plus answer-structure reward configuration produces a pedagogical-quality win rate of 81.08% and an instruction-following win rate of 68.24%, both above parity with the Qwen3-4B base model. [→ Garrod 2026](#garrod-2026)

## Evidence

### Garrod 2026

Garrod, O. G. B., Ince, R. A. A., Liu, M., Huti, M., Boos, M., Waldock, A., Andrews, D., Alonso-Kropil, R., & Atherton, P. (2026). Edu-QuRating: Multi-Dimensional Educational Data Curation with Distilled Pairwise Judgements. arXiv. https://arxiv.org/abs/2609.09425

`q2 · i?` · `causal · r1`

GRPO fine-tuning of Qwen3-4B on 1008 foundational-literacy teacher-task examples, evaluated on 73 held-out examples via pairwise judge comparison (gemini-3-flash-preview) against the base model, aggregated over both order configurations. The article reports the combined-reward win rates of 81.08% and 68.24%.

> "Combining the Edu-QuRating and answer-structure rewards produces the highest observed pedagogical-quality win rate (81.08%) while retaining an instruction-following win rate above parity with the base model (68.24%)."

## Discussion


## Related Claims
- [Edu-QuRater rewards alone raise pedagogical-quality win rate (77.70%) but fall below parity on instruction following (40.54%), consistent with over-optimizing a proxy reward](edu-qurater-rewards-alone-below-parity-instruction-following.md) — related
- [Edu-QuRaters recover held-out GPT-4.1-mini pairwise educational preferences from single-text scores, with mean accuracy rising from 0.895 (Sheared-LLaMA-1.3B) to 0.917 (Gemma-3-4B-PT)](edu-quraters-distill-pairwise-educational-preferences.md) — related
- [Core-Ed Edu-QuRater scores vary sensibly with education-level metadata on out-of-sample materials (marginal Pearson correlations 0.62 and 0.64; six-dimension cross-validated R2 of 0.449)](core-ed-scores-track-education-level-metadata.md) — related
