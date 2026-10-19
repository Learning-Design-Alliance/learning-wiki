---
type: claim
title: Influence-function diagnostics identify steps 3–8 of the Big-L peg-solitaire board as the most consequential region, with the lowest-β participants showing substantially larger absolute influence values there
description: Influence-function diagnostics identify steps 3–8 of the Big-L peg-solitaire board as the most consequential region, with the lowest-β participants showing substantially larger absolute influence values there
id: rlmm-influence-diagnostics-big-l-steps-3-8
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
---

# Influence-function diagnostics identify steps 3–8 of the Big-L peg-solitaire board as the most consequential region, with the lowest-β participants showing substantially larger absolute influence values there

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On the Big-L board, the lowest-β group exhibits substantially larger absolute influence values in steps 3–8 than both the highest-β group and remaining participants, marking a structural bottleneck. [→ Wenqian Xu 2026](#wenqian-xu-2026)

## Evidence

### Wenqian Xu 2026

Wenqian Xu, Feng Ji. (2026). Reinforcement Learning Measurement Model. arXiv. https://arxiv.org/abs/2605.09305 [doi:10.48550/arxiv.2605.09305](https://doi.org/10.48550/arxiv.2605.09305)

`q2 · i?` · `design · r2`

Influence-function analysis of simulated trajectories on the Big-L board (Figures 5 and 6). The article links the pattern to a collapse in the number of remaining solution paths around steps 3–8, so errors there "removestructuralresourcesrequiredforlaterconnectivity".

> "Forsteps3–8,thelowest-βgroupexhibitssubstantiallylargerabsoluteinfluencevaluesthanboththehighest- βgroup and the remaining participants."

## Discussion


## Related Claims

- [The RLMM recovers ability parameters on peg-solitaire boards with up to more than 23 million states, where tabular MDP-MM estimation is impractical](rlmm-scales-to-millions-of-states.md) — related
- [In peg-solitaire simulations with known true abilities, the RLMM attains lower RMSE of log βj than the MDP-MM on all four original boards](rlmm-lower-rmse-than-mdp-mm-peg-solitaire.md) — related
- [RLMM runtime stays within approximately 15–20 seconds across the four peg-solitaire boards while MDP-MM runtime grows with task complexity, reaching a 19.1× speedup on the diamond board](rlmm-stable-runtime-speedup-growing-complexity.md) — related
- [In AQUALAB, estimated β is ordered across episode completion status (means 1.181, 1.506, 2.343; Kruskal–Wallis p = 8.62×10−29) and higher-β quintiles complete more content more efficiently](aqualab-beta-completion-and-efficiency.md)
