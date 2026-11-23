---
type: claim
title: Curriculum learning with easy-to-hard data ordering yields better final performance than shuffled vanilla learning on both benchmarks
description: Curriculum learning with easy-to-hard data ordering yields better final performance than shuffled vanilla learning on both benchmarks
id: yoda-curriculum-learning-improves-robustness
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: jianqiao-lu-2024
    resource: "https://doi.org/10.48550/arXiv.2401.15670"
    title: "Jianqiao Lu, Wanjun Zhong, Yufei Wang, Zhijiang Guo, Qi Zhu, Wenyong Huang, Yanlin Wang, Fei Mi, Baojun Wang, Yasheng Wang, Lifeng Shang, Xin Jiang, Qun Liu. (2024). YODA: Teacher-Student Progressive Learning for Language Models. arXiv. [doi:10.48550/arXiv.2401.15670](https://doi.org/10.48550/arXiv.2401.15670)"
    author: Jianqiao Lu, Wanjun Zhong, Yufei Wang, Zhijiang Guo, Qi Zhu, Wenyong Huang, Yanlin Wang, Fei Mi, Baojun Wang, Yasheng Wang, Lifeng Shang, Xin Jiang, Qun Liu
    q: 2
    i: "?"
    kind: causal
    rigour: "?"
---

# Curriculum learning with easy-to-hard data ordering yields better final performance than shuffled vanilla learning on both benchmarks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Curriculum learning (80% current-complexity / 20% other levels per phase) produces learning curves that continually improve and better final performances than vanilla shuffled training. [→ Jianqiao Lu 2024](#jianqiao-lu-2024)

## Evidence

### Jianqiao Lu 2024

Jianqiao Lu, Wanjun Zhong, Yufei Wang, Zhijiang Guo, Qi Zhu, Wenyong Huang, Yanlin Wang, Fei Mi, Baojun Wang, Yasheng Wang, Lifeng Shang, Xin Jiang, Qun Liu. (2024). YODA: Teacher-Student Progressive Learning for Language Models. arXiv. [doi:10.48550/arXiv.2401.15670](https://doi.org/10.48550/arXiv.2401.15670)

`q2 · i?` · `causal · r?`

Curriculum learning analysis (§4.4, Figure 3): training data arranged by complexity level i into basic, intermediate, and advanced phases with weighted sampling, compared against randomly shuffled vanilla learning on GSM8K and MATH. Figure 3 plots test accuracy across phases for both conditions.

> "curriculum learning derives robust learning curves that continually improve performance and yield better final performances compared with vanilla learning on both datasets"

## Discussion


## Related Claims
- [A fully learned curriculum (deterministic ordering of generator inputs) makes GTN training more effective than other curriculum variants](gtn-full-curriculum-outperforms-other-variants.md) — related
- [Sequencing rather than concept selection explains most of the EVOL–PPO-vanilla EP gap on ASSIST15 L=10](sequencing-explains-evol-ppo-gap.md) — related
- [Problem-difficulty-based curricula consistently outperform random shuffling, with gains of up to 3–6% on easier datasets](problem-difficulty-curricula-beat-shuffled-baseline.md) — related
