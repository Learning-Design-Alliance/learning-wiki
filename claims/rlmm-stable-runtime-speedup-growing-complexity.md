---
type: claim
title: RLMM runtime stays within approximately 15–20 seconds across the four peg-solitaire boards while MDP-MM runtime grows with task complexity, reaching a 19.1× speedup on the diamond board
description: RLMM runtime stays within approximately 15–20 seconds across the four peg-solitaire boards while MDP-MM runtime grows with task complexity, reaching a 19.1× speedup on the diamond board
id: rlmm-stable-runtime-speedup-growing-complexity
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

# RLMM runtime stays within approximately 15–20 seconds across the four peg-solitaire boards while MDP-MM runtime grows with task complexity, reaching a 19.1× speedup on the diamond board

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` RLMM estimation runtime remains stable as state-space size grows, whereas MDP-MM runtime increases by an order of magnitude from the tiny cross to the diamond board. [→ Wenqian Xu 2026](#wenqian-xu-2026)

## Evidence

### Wenqian Xu 2026

Wenqian Xu, Feng Ji. (2026). Reinforcement Learning Measurement Model. arXiv. https://arxiv.org/abs/2605.09305

`q2 · i?` · `design · r2`

Runtime comparison of the second estimation stage on the four peg-solitaire boards (Table 4): MDP-MM 35.30 s to 370.53 s versus RLMM 16.45 s to 19.35 s, with printed speedups up to 19.1×. The article attributes stability to avoiding "repeatedlysolvingthefullMDPduringparameterupdates".

> "Incontrast,theruntimeoftheRLMMremainsstableacrossallfourenvironments,stayingwithinanarrow rangeofapproximately15–20seconds."

## Discussion


## Related Claims
- [Influence-function diagnostics identify steps 3–8 of the Big-L peg-solitaire board as the most consequential region, with the lowest-β participants showing substantially larger absolute influence values there](rlmm-influence-diagnostics-big-l-steps-3-8.md) — related
- [In peg-solitaire simulations with known true abilities, the RLMM attains lower RMSE of log βj than the MDP-MM on all four original boards](rlmm-lower-rmse-than-mdp-mm-peg-solitaire.md) — related
- [The RLMM recovers ability parameters on peg-solitaire boards with up to more than 23 million states, where tabular MDP-MM estimation is impractical](rlmm-scales-to-millions-of-states.md) — related
