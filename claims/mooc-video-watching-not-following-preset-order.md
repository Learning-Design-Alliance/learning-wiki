---
type: claim
title: "Students' actual video watching behaviors in MOOCs do not follow the preset course order, indicating a need for adaptive sequence recommendations"
description: "Students' actual video watching behaviors in MOOCs do not follow the preset course order, indicating a need for adaptive sequence recommendations"
id: mooc-video-watching-not-following-preset-order
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

# Students' actual video watching behaviors in MOOCs do not follow the preset course order, indicating a need for adaptive sequence recommendations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In the learning recommendation task on MOOCCubeX, sequential recommendation models performed acceptably while the syllabus-order baseline underperformed, indicating students' actual video watching behaviors are not following the preset order. [→ Yu et al. 2021](#yu-et-al-2021)

## Evidence

### Yu et al. 2021

Jifan Yu, Yuquan Wang, Qingyang Zhong, Gan Luo, Yiming Mao, Kai Sun, Wenzheng Feng, Wei Xu, Shulin Cao, Kaisheng Zeng, Zijun Yao, Lei Hou, Yankai Lin, Peng Li, Jie Zhou, Bin Xu, Juanzi Li, Jie Tang, Maosong Sun. (2021). MOOCCubeX: A Large Knowledge-centered Repository for Adaptive Learning in MOOCs. Proceedings of the 30th ACM International Conference on Information and Knowledge Management (CIKM '21). https://doi.org/10.1145/3459637.3482010

`q2 · i?` · `design · r2`

Learning recommendation application on MOOCCubeX: next-video recommendation over watching sequences of 33,650 students, evaluated with leave-one-out NDCG and Recall against baselines including GRU4Rec and CASER. The article reports the sequential models' "performance ... is still acceptable" and interprets that students do not follow the preset order. No effect size is printed.

> "At the same time, the performance of the sequential rec- ommendation models (GRU4Rec, CASER) is still acceptable. This phenomenon indicates that students’ actual video watching be- haviors are not following the preset order."

## Discussion


## Related Claims
- [Video watching behavior in MOOCCubeX is extremely long-tailed: 28.5% of students watched the most popular video while 39.2% of videos were watched only once](mooc-video-watching-long-tailed-distribution.md) — related
- [MOOC video-watching behaviors fall into four patterns that reveal different aspects of knowledge dependencies](mooc-video-watching-patterns-dependencies.md) — related
- [Clickstream features predict students' next click state while watching MOOC video lectures](clickstream-predicts-next-click-state-mooc.md) — related
