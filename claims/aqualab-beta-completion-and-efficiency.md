---
type: claim
title: In AQUALAB, estimated β is ordered across episode completion status (means 1.181, 1.506, 2.343; Kruskal–Wallis p = 8.62×10−29) and higher-β quintiles complete more content more efficiently
description: In AQUALAB, estimated β is ordered across episode completion status (means 1.181, 1.506, 2.343; Kruskal–Wallis p = 8.62×10−29) and higher-β quintiles complete more content more efficiently
id: aqualab-beta-completion-and-efficiency
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: wenqian-xu-2026
    resource: "https://doi.org/10.48550/arxiv.2605.09305"
    title: "Wenqian Xu, Feng Ji. (2026). Reinforcement Learning Measurement Model. arXiv. https://arxiv.org/abs/2605.09305 [doi:10.48550/arxiv.2605.09305](https://doi.org/10.48550/arxiv.2605.09305)"
    author: Wenqian Xu, Feng Ji
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: wenqian-xu-2026-2
    resource: "https://arxiv.org/abs/2605.09305"
    title: "Wenqian Xu, Feng Ji. (2026). Reinforcement Learning Measurement Model. arXiv. https://arxiv.org/abs/2605.09305"
    author: Wenqian Xu, Feng Ji
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# In AQUALAB, estimated β is ordered across episode completion status (means 1.181, 1.506, 2.343; Kruskal–Wallis p = 8.62×10−29) and higher-β quintiles complete more content more efficiently

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Mean estimated β rises from incomplete to task-complete to job-complete episodes, with a highly significant Kruskal–Wallis group difference. [→ Wenqian Xu 2026](#wenqian-xu-2026)
`q2 i?` From the lowest to the highest β quintile, completed tasks and jobs increase, and steps per completed task decline steadily. [→ Wenqian Xu 2026 (2)](#wenqian-xu-2026-2)

## Evidence

### Wenqian Xu 2026

Wenqian Xu, Feng Ji. (2026). Reinforcement Learning Measurement Model. arXiv. https://arxiv.org/abs/2605.09305 [doi:10.48550/arxiv.2605.09305](https://doi.org/10.48550/arxiv.2605.09305)

`q2 · i?` · `design · r2`

Descriptive analysis of episode completion status in AQUALAB (Figure 10); the article reports the distribution of ˆβ is ordered across incomplete, task-complete-only, and job-complete episodes. Only the test statistic is printed, so no effect size is reported.

> "The corresponding mean estimates were 1.181, 1.506, and 2.343, respectively, and the overall group difference was highly significant under a Kruskal–Wallis test (p= 8.62×10 −29)."

### Wenqian Xu 2026 (2)

Wenqian Xu, Feng Ji. (2026). Reinforcement Learning Measurement Model. arXiv. https://arxiv.org/abs/2605.09305

`q2 · i?` · `design · r2`

Quintile-based efficiency summaries in AQUALAB (Figures 11 and 12); completion rates and counts rise across quintiles, and median steps per completed task decline. The article notes steps to first job completion are "naturally harder to interpret" because they are defined only for episodes that complete a job.

> "Theclearestpatternappearsinsteps per completed task, which declines steadily asˆβincreases."

## Discussion


## Related Claims

- [In AQUALAB gameplay logs, the estimated RLMM person parameter is positively associated with cumulative trajectory reward (Pearson 0.5842, Spearman 0.5760)](aqualab-beta-associated-with-cumulative-reward.md) — related
- [In peg-solitaire simulations with known true abilities, the RLMM attains lower RMSE of log βj than the MDP-MM on all four original boards](rlmm-lower-rmse-than-mdp-mm-peg-solitaire.md)
- [The RLMM recovers ability parameters on peg-solitaire boards with up to more than 23 million states, where tabular MDP-MM estimation is impractical](rlmm-scales-to-millions-of-states.md)
- [RLMM runtime stays within approximately 15–20 seconds across the four peg-solitaire boards while MDP-MM runtime grows with task complexity, reaching a 19.1× speedup on the diamond board](rlmm-stable-runtime-speedup-growing-complexity.md)
- [Influence-function diagnostics identify steps 3–8 of the Big-L peg-solitaire board as the most consequential region, with the lowest-β participants showing substantially larger absolute influence values there](rlmm-influence-diagnostics-big-l-steps-3-8.md)
- [Prompt-count distributions differ significantly across assignments, with moderate prompting most common and extended prompting (10+) rare except in Algorithms (18.0%)](prompt-count-distributions-differ-across-assignments.md) — related
