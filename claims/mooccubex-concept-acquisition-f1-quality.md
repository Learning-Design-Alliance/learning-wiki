---
type: claim
title: Weakly supervised concept acquisition reaches F1 of 0.861 for concept extraction and 0.905 for prerequisite discovery on an expert-annotated evaluation set
description: Weakly supervised concept acquisition reaches F1 of 0.861 for concept extraction and 0.905 for prerequisite discovery on an expert-annotated evaluation set
id: mooccubex-concept-acquisition-f1-quality
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-24
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
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

# Weakly supervised concept acquisition reaches F1 of 0.861 for concept extraction and 0.905 for prerequisite discovery on an expert-annotated evaluation set

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Expert evaluation of randomly sampled videos found concept extraction F1 of 0.861 and prerequisite discovery F1 of 0.905. [→ Yu et al. 2021](#yu-et-al-2021)

## Evidence

### Yu et al. 2021

Jifan Yu, Yuquan Wang, Qingyang Zhong, Gan Luo, Yiming Mao, Kai Sun, Wenzheng Feng, Wei Xu, Shulin Cao, Kaisheng Zeng, Zijun Yao, Lei Hou, Yankai Lin, Peng Li, Jie Zhou, Bin Xu, Juanzi Li, Jie Tang, Maosong Sun. (2021). MOOCCubeX: A Large Knowledge-centered Repository for Adaptive Learning in MOOCs. Proceedings of the 30th ACM International Conference on Information and Knowledge Management (CIKM '21). https://doi.org/10.1145/3459637.3482010

`q2 · i?` · `design · r2`

Expert annotation evaluation: 200 videos from 6 courses in different disciplines were annotated by three domain experts for concepts and relationships, with results double-checked. The article reports the "F1-score of concept extraction on the evaluation set is 0.861" and prerequisite discovery F1 of 0.905. No effect size is printed.

> "Finally, the F1-score of concept extraction on the evaluation set is 0.861, and the F1-score of prerequisite discovery is 0.905, reflecting the high quality of our concept acquisition."

## Discussion


## Related Claims
- [Concept-based curation densely links MOOC resources: each video has 422 related videos and each exercise 364 correlations under shared concepts](concept-annotation-densely-links-mooc-resources.md) — related
- [A DistilBERT dialogue-act classifier trained on weakly supervised data reached an average F1 score of 0.71 for the mathematical questioning scenario](distilbert-dialogue-act-f1-0-71-weak-supervision.md) — related
