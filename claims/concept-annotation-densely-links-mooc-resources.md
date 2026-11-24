---
type: claim
title: "Concept-based curation densely links MOOC resources: each video has 422 related videos and each exercise 364 correlations under shared concepts"
description: "Concept-based curation densely links MOOC resources: each video has 422 related videos and each exercise 364 correlations under shared concepts"
id: concept-annotation-densely-links-mooc-resources
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-24
evidence_strength: moderate
newest_evidence: 2021
sources:
  - id: yu-et-al-2021
    resource: "https://doi.org/10.1145/3459637.3482010"
    title: "Jifan Yu, Yuquan Wang, Qingyang Zhong, Gan Luo, Yiming Mao, Kai Sun, Wenzheng Feng, Wei Xu, Shulin Cao, Kaisheng Zeng, Zijun Yao, Lei Hou, Yankai Lin, Peng Li, Jie Zhou, Bin Xu, Juanzi Li, Jie Tang, Maosong Sun. (2021). MOOCCubeX: A Large Knowledge-centered Repository for Adaptive Learning in MOOCs. Proceedings of the 30th ACM International Conference on Information and Knowledge Management (CIKM '21). https://doi.org/10.1145/3459637.3482010"
    author: Jifan Yu, Yuquan Wang, Qingyang Zhong, Gan Luo, Yiming Mao, Kai Sun, Wenzheng Feng, Wei Xu, Shulin Cao, Kaisheng Zeng, Zijun Yao, Lei Hou, Yankai Lin, Peng Li, Jie Zhou, Bin Xu, Juanzi Li, Jie Tang, Maosong Sun
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Concept-based curation densely links MOOC resources: each video has 422 related videos and each exercise 364 correlations under shared concepts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` After concept annotation, resources show rich knowledge-based connections, with each video related to 422 videos and each exercise to 364 exercises under shared concepts. [→ Yu et al. 2021](#yu-et-al-2021)

## Evidence

### Yu et al. 2021

Jifan Yu, Yuquan Wang, Qingyang Zhong, Gan Luo, Yiming Mao, Kai Sun, Wenzheng Feng, Wei Xu, Shulin Cao, Kaisheng Zeng, Zijun Yao, Lei Hou, Yankai Lin, Peng Li, Jie Zhou, Bin Xu, Juanzi Li, Jie Tang, Maosong Sun. (2021). MOOCCubeX: A Large Knowledge-centered Repository for Adaptive Learning in MOOCs. Proceedings of the 30th ACM International Conference on Information and Knowledge Management (CIKM '21). https://doi.org/10.1145/3459637.3482010

`q2 · i?` · `design · r2`

Multi-resource concept annotation stage: exercises, comments, and replies are linked to concepts via BERT-embedding matching with a 0.8 cosine-similarity threshold. The article reports "each video has 422 related videos and each exercise has 364 correlations". Counts are descriptive; no inferential test is printed.

> "And respectively measured in 3 and 1 common concepts, each video has 422 related videos and each exercise has 364 correlations, showing the richness of knowledge-based resource connections."

## Discussion


## Related Claims
- [Weakly supervised concept acquisition reaches F1 of 0.861 for concept extraction and 0.905 for prerequisite discovery on an expert-annotated evaluation set](mooccubex-concept-acquisition-f1-quality.md) — related
- [Exercising behavior in MOOCCubeX is more balanced than video watching and approximates a normal distribution](mooc-exercising-behavior-balanced-distribution.md) — related
