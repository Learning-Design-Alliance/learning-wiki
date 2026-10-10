---
type: claim
title: Core-Ed dimensions capture part of the FineWeb-Edu scalar signal while remaining not individually redundant with it (six-dimension cross-validated R2 of 0.228)
description: Core-Ed dimensions capture part of the FineWeb-Edu scalar signal while remaining not individually redundant with it (six-dimension cross-validated R2 of 0.228)
id: core-ed-dimensions-decompose-fineweb-edu-signal
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

# Core-Ed dimensions capture part of the FineWeb-Edu scalar signal while remaining not individually redundant with it (six-dimension cross-validated R2 of 0.228)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Marginal Pearson correlations between Core-Ed document-level scores and the FineWeb-Edu score range from 0.042 to 0.326, and a linear model combining all six dimensions achieves a cross-validated R2 of 0.228 versus 0.106 for the strongest single dimension. [→ Garrod 2026](#garrod-2026)

## Evidence

### Garrod 2026

Garrod, O. G. B., Ince, R. A. A., Liu, M., Huti, M., Boos, M., Waldock, A., Andrews, D., Alonso-Kropil, R., & Atherton, P. (2026). Edu-QuRating: Multi-Dimensional Educational Data Curation with Distilled Pairwise Judgements. arXiv. https://arxiv.org/abs/2609.09425

`q2 · i?` · `design · r2`

Comparison of document-level Core-Ed scores with the FineWeb-Edu score across FineWeb-Edu-Fortified. The article reports correlations "ranging from 0.042 for lesson engagement to 0.326 forSecondary-level Suitability" and a combined-model cross-validated R2 of 0.228 versus 0.106 for the strongest single-dimension model.

> "Marginal Pearson correlations are modest, ranging from 0.042 for lesson engagement to 0.326 forSecondary-level Suitability; no individual dimension therefore closely reproduces the FineWeb-Edu score. A linear model combining all six dimensions achieves a cross-validated R2 of 0.228"

## Discussion


## Related Claims
- [Core-Ed Edu-QuRater scores vary sensibly with education-level metadata on out-of-sample materials (marginal Pearson correlations 0.62 and 0.64; six-dimension cross-validated R2 of 0.449)](core-ed-scores-track-education-level-metadata.md) — related
- [Cross-validation-selected hyperparameters generalized to the test set only for Situation and Clarity, with the other four dimensions showing CV–test misalignment](cv-test-misalignment-small-imbalanced-data.md) — related
