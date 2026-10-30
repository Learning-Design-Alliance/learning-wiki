---
type: claim
title: Training NQG models on multiple datasets with different answer types improved performance over single-dataset training
description: Training NQG models on multiple datasets with different answer types improved performance over single-dataset training
id: multi-dataset-training-improves-nqg-answer-types
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: said-al-faraby-2024
    resource: "https://doi.org/10.1007/s40593-023-00374-x"
    title: "Said Al Faraby, Adiwijaya Adiwijaya, Ade Romadhony. (2024). Review on Neural Question Generation for Education Purposes. Int J Artif Intell Educ 34:1008–1045. https://doi.org/10.1007/s40593-023-00374-x"
    author: Said Al Faraby, Adiwijaya Adiwijaya, Ade Romadhony
    q: 2
    i: "?"
    kind: review
    rigour: 2
---

# Training NQG models on multiple datasets with different answer types improved performance over single-dataset training

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Murakhovs'ka et al. (2021) showed models trained on diverse datasets containing different answer types performed better than models trained on a single dataset. [→ Said Al Faraby 2024](#said-al-faraby-2024)

## Evidence

### Said Al Faraby 2024

Said Al Faraby, Adiwijaya Adiwijaya, Ade Romadhony. (2024). Review on Neural Question Generation for Education Purposes. Int J Artif Intell Educ 34:1008–1045. https://doi.org/10.1007/s40593-023-00374-x

`q2 · i?` · `review · r2`

The review attributes this finding to Murakhovs'ka et al. (2021): training on various datasets "each containing different types of answers" improved performance versus single-dataset training. Related work by Yuan et al. (2022) adapted models to different answer types via lifelong learning.

> "Murakhovs’ka et al. (2021) demonstrated that mod- els trained on various datasets, each containing different types of answers, yielded improved performance compared to models trained on a single dataset."

## Discussion


## Related Claims
- [Multi-paragraph educational contexts require key content identification for useful NQG](key-content-identification-long-educational-contexts.md) — related
- [A model trained only on the 300-conversation BEA dataset plateaus at 74.84% average macro F1 due to limited data size and diversity](small-labeled-data-plateaus-evaluator.md) — related
- [Multi-task learning on a large multi-topic dataset outperforms separate topic-specific essay scoring models](mtl-multi-topic-beats-topic-specific-scoring.md) — a narrower finding that bears on this claim
