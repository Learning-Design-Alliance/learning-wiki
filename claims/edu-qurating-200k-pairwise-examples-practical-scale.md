---
type: claim
title: Distillation validation loss decreases sharply from 20k to 200k pairwise examples and plateaus beyond 200k for the Sheared-LLaMA-1.3B base model
description: Distillation validation loss decreases sharply from 20k to 200k pairwise examples and plateaus beyond 200k for the Sheared-LLaMA-1.3B base model
id: edu-qurating-200k-pairwise-examples-practical-scale
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

# Distillation validation loss decreases sharply from 20k to 200k pairwise examples and plateaus beyond 200k for the Sheared-LLaMA-1.3B base model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Best validation loss falls from 0.307 at 20k to 0.245 at 200k pairwise examples, while 300k and 400k examples yield almost no additional gain (0.245 and 0.244). [→ Garrod 2026](#garrod-2026)

## Evidence

### Garrod 2026

Garrod, O. G. B., Ince, R. A. A., Liu, M., Huti, M., Boos, M., Waldock, A., Andrews, D., Alonso-Kropil, R., & Atherton, P. (2026). Edu-QuRating: Multi-Dimensional Educational Data Curation with Distilled Pairwise Judgements. arXiv. https://arxiv.org/abs/2609.09425

`q2 · i?` · `design · r2`

Scaling experiment holding the Sheared-LLaMA-1.3B base model constant and varying the number of GPT-4.1-mini pairwise examples, measured by best validation loss on held-out pairwise probabilities. The article reports losses "falling from 0.307 at 20k to 0.264 at 100k and 0.245 at 200k."

> "Validation loss decreases sharply from 20k to 200k examples, falling from 0.307 at 20k to 0.264 at 100k and 0.245 at 200k (Figure 3). Increasing to 300k or 400k examples yields almost no additional gain, with best losses of 0.245 and 0.244."

## Discussion


## Related Claims
- [Core-Ed Edu-QuRater scores vary sensibly with education-level metadata on out-of-sample materials (marginal Pearson correlations 0.62 and 0.64; six-dimension cross-validated R2 of 0.449)](core-ed-scores-track-education-level-metadata.md) — related
- [Edu-QuRaters recover held-out GPT-4.1-mini pairwise educational preferences from single-text scores, with mean accuracy rising from 0.895 (Sheared-LLaMA-1.3B) to 0.917 (Gemma-3-4B-PT)](edu-quraters-distill-pairwise-educational-preferences.md) — related
- [The pairwise-distillation procedure transfers to foundational-literacy scoring, with Gemma-3-4B-PT validation losses of 0.128 (student-facing) and 0.175 (teacher-facing)](foundational-literacy-edu-quraters-distill-successfully.md) — related
