---
type: claim
title: In peg-solitaire simulations with known true abilities, the RLMM attains lower RMSE of log βj than the MDP-MM on all four original boards
description: In peg-solitaire simulations with known true abilities, the RLMM attains lower RMSE of log βj than the MDP-MM on all four original boards
id: rlmm-lower-rmse-than-mdp-mm-peg-solitaire
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: wenqian-xu-2026
    resource: "https://arxiv.org/abs/2605.09305"
    title: "Wenqian Xu, Feng Ji. (2026). Reinforcement Learning Measurement Model. arXiv. https://arxiv.org/abs/2605.09305"
    author: Wenqian Xu, Feng Ji
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# In peg-solitaire simulations with known true abilities, the RLMM attains lower RMSE of log βj than the MDP-MM on all four original boards

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across the four peg-solitaire boards from LaMar (2018), the RLMM recovered simulated person parameters more accurately than the MDP-MM, with error reductions from roughly one-third to more than two-thirds. [→ Wenqian Xu 2026](#wenqian-xu-2026)

## Evidence

### Wenqian Xu 2026

Wenqian Xu, Feng Ji. (2026). Reinforcement Learning Measurement Model. arXiv. https://arxiv.org/abs/2605.09305

`q2 · i?` · `design · r2`

Simulation study on the four peg-solitaire boards of LaMar (2018) with 200 simulated students completing 50 games per board; printed RMSE values include 0.542 vs 0.368 (tiny cross) and 0.403 vs 0.099 (diamond), showing "relative reductions in error". Scatterplots showed estimates close to the diagonal.

> "Across all four tasks, the RLMM attains lower RMSE than the MDP-MM, with relative reductions in error from roughly one-third on the smallest board to more than two-thirds on the diamond board."

## Discussion


## Related Claims
- [Influence-function diagnostics identify steps 3–8 of the Big-L peg-solitaire board as the most consequential region, with the lowest-β participants showing substantially larger absolute influence values there](rlmm-influence-diagnostics-big-l-steps-3-8.md) — related
- [The RLMM recovers ability parameters on peg-solitaire boards with up to more than 23 million states, where tabular MDP-MM estimation is impractical](rlmm-scales-to-millions-of-states.md) — related
- [RLMM runtime stays within approximately 15–20 seconds across the four peg-solitaire boards while MDP-MM runtime grows with task complexity, reaching a 19.1× speedup on the diamond board](rlmm-stable-runtime-speedup-growing-complexity.md) — related
