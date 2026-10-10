---
type: claim
title: In matched single-run 1B pre-training comparisons, all Edu-QuRating-based mixtures reach higher observed aggregate accuracy at 30k steps than the FineWeb-Edu baseline, with gains concentrated in specific tasks
description: In matched single-run 1B pre-training comparisons, all Edu-QuRating-based mixtures reach higher observed aggregate accuracy at 30k steps than the FineWeb-Edu baseline, with gains concentrated in specific tasks
id: edu-qurating-filtered-pretraining-higher-endpoints
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
  - id: garrod-2026-2
    resource: "https://arxiv.org/abs/2609.09425"
    title: "Garrod, O. G. B., Ince, R. A. A., Liu, M., Huti, M., Boos, M., Waldock, A., Andrews, D., Alonso-Kropil, R., & Atherton, P. (2026). Edu-QuRating: Multi-Dimensional Educational Data Curation with Distilled Pairwise Judgements. arXiv. https://arxiv.org/abs/2609.09425"
    author: "Garrod, O. G. B., Ince, R. A. A., Liu, M., Huti, M., Boos, M., Waldock, A., Andrews, D., Alonso-Kropil, R., & Atherton, P."
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# In matched single-run 1B pre-training comparisons, all Edu-QuRating-based mixtures reach higher observed aggregate accuracy at 30k steps than the FineWeb-Edu baseline, with gains concentrated in specific tasks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`

## Subclaims
`q2 i?` At 30k steps the FineWeb-Edu baseline reaches 0.3806 mean accuracy across nine tasks, versus 0.3903 for the 50-50-50 Edu-QuRating run, 0.3962 for stricter pedagogy, and 0.3961 for Edu-QuRating + DCLM. [→ Garrod 2026](#garrod-2026)
`q2 i?` Task-level gains are concentrated: ARC-CF and HellaSwag improve by roughly three to five accuracy points, while MMLU-family improvements are close to zero and CommonsenseQA is mixed. [→ Garrod 2026 (2)](#garrod-2026-2)

## Evidence

### Garrod 2026

Garrod, O. G. B., Ince, R. A. A., Liu, M., Huti, M., Boos, M., Waldock, A., Andrews, D., Alonso-Kropil, R., & Atherton, P. (2026). Edu-QuRating: Multi-Dimensional Educational Data Curation with Distilled Pairwise Judgements. arXiv. https://arxiv.org/abs/2609.09425

`q2 · i?` · `causal · r1`

Matched single-run pre-training comparison following the Smol Training Playbook 1B ablation configuration (45B tokens, 10% FineMath-3Plus and 20% Stack-Edu-Python fixed), varying only the 70% web-text slice. The article reports the baseline at "0.3806 mean accuracy across the nine tasks" and higher Edu-QuRating endpoints.

> "The baseline reaches 0.3806 mean accuracy across the nine tasks. The regenerated 50-50-50 Edu-QuRating run reaches 0.3903, a gain of 0.0097 over the baseline. The stricter-pedagogy run reaches 0.3962, and the Edu-QuRating + DCLM mixture reaches 0.3961."

### Garrod 2026 (2)

Garrod, O. G. B., Ince, R. A. A., Liu, M., Huti, M., Boos, M., Waldock, A., Andrews, D., Alonso-Kropil, R., & Atherton, P. (2026). Edu-QuRating: Multi-Dimensional Educational Data Curation with Distilled Pairwise Judgements. arXiv. https://arxiv.org/abs/2609.09425

`q2 · i?` · `causal · r1`

Task-level endpoint analysis of the same matched pre-training comparison, shown in Figure 6(C). The article reports that "ARC-CF and HellaSwag show the clearest improvements" while MMLU-family improvements are close to zero and CommonsenseQA is mixed.

> "ARC-CF and HellaSwag show the clearest improvements, with gains of roughly three to five accuracy points depending on the Edu-QuRating mixture. OpenBookQA, BoolQ, and WinoGrande also improve for all Edu-QuRating conditions, though by smaller margins."

## Discussion


## Related Claims
- [Core-Ed Edu-QuRater scores vary sensibly with education-level metadata on out-of-sample materials (marginal Pearson correlations 0.62 and 0.64; six-dimension cross-validated R2 of 0.449)](core-ed-scores-track-education-level-metadata.md) — related
- [Edu-QuRaters recover held-out GPT-4.1-mini pairwise educational preferences from single-text scores, with mean accuracy rising from 0.895 (Sheared-LLaMA-1.3B) to 0.917 (Gemma-3-4B-PT)](edu-quraters-distill-pairwise-educational-preferences.md) — related
- [The pairwise-distillation procedure transfers to foundational-literacy scoring, with Gemma-3-4B-PT validation losses of 0.128 (student-facing) and 0.175 (teacher-facing)](foundational-literacy-edu-quraters-distill-successfully.md) — related
