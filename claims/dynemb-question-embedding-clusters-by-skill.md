---
type: claim
title: The learned question embedding aligns with manually labeled skill categories, showing clear clustering of questions by skill in a multidimensional scaling visualization
description: The learned question embedding aligns with manually labeled skill categories, showing clear clustering of questions by skill in a multidimensional scaling visualization
id: dynemb-question-embedding-clusters-by-skill
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
evidence_strength: weak
sources:
  - id: liangbei-xu-and-mark-a-davenport-2020
    resource: "https://educationaldatamining.org"
    title: "Liangbei Xu and Mark A. Davenport. (2020). Dynamic Knowledge Embedding and Tracing. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020). https://educationaldatamining.org"
    author: Liangbei Xu and Mark A. Davenport
    q: 1
    i: 1
---

# The learned question embedding aligns with manually labeled skill categories, showing clear clustering of questions by skill in a multidimensional scaling visualization

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q1` argument or single case · `i1` small

## Subclaims
`q1 i?` Although the matrix-factorization latent space is not explicitly aligned with the skill-tag space, the proposed initialization and sparsity promotion align the question embedding space with the skill embedding space, and a visualization of 200 questions shows clear clustering by associated skill. [→ Liangbei Xu and Mark A. Davenport 2020](#liangbei-xu-and-mark-a-davenport-2020)

## Evidence

### Liangbei Xu and Mark A. Davenport 2020

Liangbei Xu and Mark A. Davenport. (2020). Dynamic Knowledge Embedding and Tracing. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020). https://educationaldatamining.org

`q1 · i1`

Experiment 4 visualized the embedding of a random selection of 200 questions via multidimensional scaling (Figure 5); the authors report clear clustering with respect to associated skills, which they say adds semantic meaning and improves model interpretability.

> "Figure 5 shows clear clus- tering of question embedding with respect to the associated skills (indicated by skill identiﬁers)."

## Discussion


## Related Claims
- [Learned question embeddings capture question difficulty rather than clustering exercises by concept](question-embeddings-capture-difficulty-not-concepts.md) — reports the opposite
- [Replacing concept/skill tags with question identifiers significantly degrades DKT and DKVMN performance, while DynEmb tracks knowledge using pretrained question embeddings instead of tags](dynemb-tracks-knowledge-without-skill-tags.md) — related
- [Embedding pretraining outperforms end-to-end training in DynEmb, avoiding the overfitting that end-to-end training exhibits](embedding-pretraining-beats-end-to-end-training-dynemb.md) — related
