---
type: claim
title: In AQUALAB gameplay logs, the estimated RLMM person parameter is positively associated with cumulative trajectory reward (Pearson 0.5842, Spearman 0.5760)
description: In AQUALAB gameplay logs, the estimated RLMM person parameter is positively associated with cumulative trajectory reward (Pearson 0.5842, Spearman 0.5760)
id: aqualab-beta-associated-with-cumulative-reward
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
    i: 3
    kind: design
    rigour: 2
---

# In AQUALAB gameplay logs, the estimated RLMM person parameter is positively associated with cumulative trajectory reward (Pearson 0.5842, Spearman 0.5760)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · `i3` large

## Subclaims
`q2 i3` Episodes with larger estimated β achieved higher cumulative reward, with a printed Pearson correlation of 0.5842 and Spearman correlation of 0.5760. [→ Wenqian Xu 2026](#wenqian-xu-2026)

## Evidence

### Wenqian Xu 2026

Wenqian Xu, Feng Ji. (2026). Reinforcement Learning Measurement Model. arXiv. https://arxiv.org/abs/2605.09305 [doi:10.48550/arxiv.2605.09305](https://doi.org/10.48550/arxiv.2605.09305)

`q2 · i3` · `design · r2`

Empirical analysis of the February 2026 AQUALAB log export; the filtered analytic sample contained 1,133 episodes and 8,474 transitions, reduced from 106,315 raw transitions. The printed correlation r = 0.5842 (Pearson) is the effect size. The article frames this as "a validity check rather than as evidence thatˆβrepresents a pure ability construct".

> "After20block-coordinateMAPiterationsonthefiltereddataset,thecorrelationbetween ˆβandcumulative trajectory reward was 0.5842 by Pearson correlation and 0.5760 by Spearman correlation."

## Discussion


## Related Claims

- [In AQUALAB, estimated β is ordered across episode completion status (means 1.181, 1.506, 2.343; Kruskal–Wallis p = 8.62×10−29) and higher-β quintiles complete more content more efficiently](aqualab-beta-completion-and-efficiency.md) — related
- [In peg-solitaire simulations with known true abilities, the RLMM attains lower RMSE of log βj than the MDP-MM on all four original boards](rlmm-lower-rmse-than-mdp-mm-peg-solitaire.md)
- [The RLMM recovers ability parameters on peg-solitaire boards with up to more than 23 million states, where tabular MDP-MM estimation is impractical](rlmm-scales-to-millions-of-states.md)
- [RLMM runtime stays within approximately 15–20 seconds across the four peg-solitaire boards while MDP-MM runtime grows with task complexity, reaching a 19.1× speedup on the diamond board](rlmm-stable-runtime-speedup-growing-complexity.md)
- [Influence-function diagnostics identify steps 3–8 of the Big-L peg-solitaire board as the most consequential region, with the lowest-β participants showing substantially larger absolute influence values there](rlmm-influence-diagnostics-big-l-steps-3-8.md)
