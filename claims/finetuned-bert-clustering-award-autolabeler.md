---
type: claim
title: Clustering fine-tuned BERT embeddings of award descriptions yields an accurate automatic award labeler, with Agglomerative Clustering using Ward linkage performing best (Rand Index 0.990)
description: Clustering fine-tuned BERT embeddings of award descriptions yields an accurate automatic award labeler, with Agglomerative Clustering using Ward linkage performing best (Rand Index 0.990)
id: finetuned-bert-clustering-award-autolabeler
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: xinzhe-zheng-2025
    resource: "https://doi.org/10.48550/arXiv.2509.00863"
    title: "Xinzhe Zheng, Zhen-Qun Yang, Jiannong Cao, and Jiabei Cheng. (2025). Predicting Multi-Type Talented Students in Secondary School Using Semi-Supervised Machine Learning. arXiv. [doi:10.48550/arXiv.2509.00863](https://doi.org/10.48550/arXiv.2509.00863)"
    author: Xinzhe Zheng, Zhen-Qun Yang, Jiannong Cao, and Jiabei Cheng
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: xinzhe-zheng-2025-2
    resource: "https://doi.org/10.48550/arXiv.2509.00863"
    title: "Xinzhe Zheng, Zhen-Qun Yang, Jiannong Cao, and Jiabei Cheng. (2025). Predicting Multi-Type Talented Students in Secondary School Using Semi-Supervised Machine Learning. arXiv. [doi:10.48550/arXiv.2509.00863](https://doi.org/10.48550/arXiv.2509.00863)"
    author: Xinzhe Zheng, Zhen-Qun Yang, Jiannong Cao, and Jiabei Cheng
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Clustering fine-tuned BERT embeddings of award descriptions yields an accurate automatic award labeler, with Agglomerative Clustering using Ward linkage performing best (Rand Index 0.990)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On fine-tuned BERT embeddings, all twelve clustering algorithms score Rand Index above 0.900, and Agglomerative Clustering with Ward linkage performs best. [→ Xinzhe Zheng 2025](#xinzhe-zheng-2025)
`q2 i?` The authors conclude the clustering-plus-fine-tuned-BERT pipeline is a valid and accurate auto labeler for awards data of Hong Kong secondary school students. [→ Xinzhe Zheng 2025 (2)](#xinzhe-zheng-2025-2)

## Evidence

### Xinzhe Zheng 2025

Xinzhe Zheng, Zhen-Qun Yang, Jiannong Cao, and Jiabei Cheng. (2025). Predicting Multi-Type Talented Students in Secondary School Using Semi-Supervised Machine Learning. arXiv. [doi:10.48550/arXiv.2509.00863](https://doi.org/10.48550/arXiv.2509.00863)

`q2 · i?` · `design · r2`

Numerical clustering evaluation shown in Fig. 2b and Table I, grouping award descriptions into seven clusters using embeddings from BERT fine-tuned on awards data from 1,041 students. The article reports Rand Index above 0.900 for all algorithms and Ward linkage best at 0.990 in Table I.

> "All have a Rand Index above 0.900, and most of them reached a Rand Index of 0.970 and a mutual information score of 0.970. While Agglomerative Clustering using Ward linkage still performed the best."

### Xinzhe Zheng 2025 (2)

Xinzhe Zheng, Zhen-Qun Yang, Jiannong Cao, and Jiabei Cheng. (2025). Predicting Multi-Type Talented Students in Secondary School Using Semi-Supervised Machine Learning. arXiv. [doi:10.48550/arXiv.2509.00863](https://doi.org/10.48550/arXiv.2509.00863)

`q2 · i?` · `design · r2`

Authors' interpretation in the Clustering Results section, following visualization in Fig. 3b showing fine-tuned embeddings grouped into seven distinguished clusters. The article states this conclusion and immediately flags the small training and testing data as a limitation.

> "Thus, using clustering with fine-tuned BERT as an encoder is a valid and accurate auto labler for awards data of Hong Kong secondary school students."

## Discussion


## Related Claims
- [Unsupervised hierarchical clustering of knowledge vectors recovers expert bundle structure without bundle labels](clustering-recovers-expert-bundles.md) — related
- [Clusters computed from pre-trained LLM embeddings show low overall alignment with theory-driven Knowledge Profiles of student biology responses](llm-embedding-clusters-low-alignment-kps.md) — reports the opposite
