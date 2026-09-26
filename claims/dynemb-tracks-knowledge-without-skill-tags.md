---
type: claim
title: Replacing concept/skill tags with question identifiers significantly degrades DKT and DKVMN performance, while DynEmb tracks knowledge using pretrained question embeddings instead of tags
description: Replacing concept/skill tags with question identifiers significantly degrades DKT and DKVMN performance, while DynEmb tracks knowledge using pretrained question embeddings instead of tags
id: dynemb-tracks-knowledge-without-skill-tags
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
evidence_strength: moderate
sources:
  - id: liangbei-xu-and-mark-a-davenport-2020
    resource: "https://educationaldatamining.org"
    title: "Liangbei Xu and Mark A. Davenport. (2020). Dynamic Knowledge Embedding and Tracing. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020). https://educationaldatamining.org"
    author: Liangbei Xu and Mark A. Davenport
    q: 2
    i: 2
---

# Replacing concept/skill tags with question identifiers significantly degrades DKT and DKVMN performance, while DynEmb tracks knowledge using pretrained question embeddings instead of tags

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment · `i2` medium

## Subclaims
`q2 i?` DKT and DKVMN suffer significant performance degradation when frequently repeating skill tags are replaced with question identifiers, whereas DynEmb avoids manual tagging by using a matrix-factorization question embedding. [→ Liangbei Xu and Mark A. Davenport 2020](#liangbei-xu-and-mark-a-davenport-2020)

## Evidence

### Liangbei Xu and Mark A. Davenport 2020

Liangbei Xu and Mark A. Davenport. (2020). Dynamic Knowledge Embedding and Tracing. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020). https://educationaldatamining.org

`q2 · i2`

The authors' experimental observation reported in the model-training section: substituting question identifiers for skill tags in DKT and DKVMN caused "signiﬁcant performance degradation" and heavy computational cost, while DynEmb's pretrained question embedding exploits question difficulty information and scales well when tags are unavailable.

> "in our experi- ments we have observed that if we replace the (frequently repeating) concept/skill tags in DKT and DKVMN with the (much less frequently repeating) question identiﬁers, then both DKT and DKVMN will have signiﬁcant performance degradation and require intensive computational resources to train."

## Discussion


## Related Claims
- [The survey reports, citing Pu and Becker, that removing students' repeated interactions on the same exercises reduced AKT's performance to close to that of DKVMN.](attentive-knowledge-tracing-benefits-from-repeated-interactions.md) — related
- [Embedding pretraining outperforms end-to-end training in DynEmb, avoiding the overfitting that end-to-end training exhibits](embedding-pretraining-beats-end-to-end-training-dynemb.md) — related
- [DynEmb outperforms BMF and DKT baselines in future response prediction across five tutoring datasets, with AUC improvement up to 5.43% in the New User setting](dynemb-outperforms-dkt-and-bmf-baselines.md) — related
- [The learned question embedding aligns with manually labeled skill categories, showing clear clustering of questions by skill in a multidimensional scaling visualization](dynemb-question-embedding-clusters-by-skill.md) — related
- [DynEmb's response-prediction AUC is stable over a wide range of question-embedding dimensionalities](dynemb-performance-stable-across-embedding-dimensionality.md) — related
- [Learned question embeddings capture question difficulty rather than clustering exercises by concept](question-embeddings-capture-difficulty-not-concepts.md) — related
