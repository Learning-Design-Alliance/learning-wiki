---
type: claim
title: Many learning algorithms, including neural network training and Q-learning, have recursive forms of the stochastic approximation type
description: Many learning algorithms, including neural network training and Q-learning, have recursive forms of the stochastic approximation type
id: learning-algorithms-stochastic-approximation-recursive-forms
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-14
evidence_strength: weak
sources:
  - id: harold-j-kushner-and-g-george-yin-2003
    resource: "https://doi.org/10.1007/b97441"
    title: "Harold J. Kushner and G. George Yin. (2003). Stochastic Approximation and Recursive Algorithms and Applications, Second Edition. Springer-Verlag, New York. https://doi.org/10.1007/b97441"
    author: Harold J. Kushner and G. George Yin
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# Many learning algorithms, including neural network training and Q-learning, have recursive forms of the stochastic approximation type

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`

## Subclaims
`q2 i?` The actual recursive forms of learning algorithms in applications such as neural networks, Markov decision processes, learning automata, and repeated games are of the stochastic approximation type. [→ Harold J. Kushner and G. George Yin 2003](#harold-j-kushner-and-g-george-yin-2003)

## Evidence

### Harold J. Kushner and G. George Yin 2003

Harold J. Kushner and G. George Yin. (2003). Stochastic Approximation and Recursive Algorithms and Applications, Second Edition. Springer-Verlag, New York. https://doi.org/10.1007/b97441

`q2 · i?` · `theoretical · r3`

Statement from the Preface and Introduction, following its discussion of renewed interest in learning algorithms motivated by neural network training and on-line learning of optimal strategies in high-dimensional Markov decision processes with unknown transition probabilities. It notes noise may be pseudorandom due to simulation methods.

> "The actual recur- sive forms of the algorithms in many such applications are of the stochastic approximation type. Owing to the types of simulation methods used, the “noise” might be “pseudorandom” [184], rather than random."

## Discussion


## Related Claims
- [Diminishing step sizes in stochastic approximation induce implicit averaging that eliminates noise effects in the long run](robbins-monro-diminishing-step-sizes-implicit-averaging.md) — related
- [For tracking time-varying systems, the step size is kept strictly away from zero](constant-step-size-tracking-nonstationary-systems.md) — related
- [Iterate averaging with step sizes decreasing slower than O(1/n) converges at an optimal rate](polyak-juditsky-iterate-averaging-optimal-rate.md) — related
- [OptimNN is insensitive to optimizer learning rate and network hyperparameters, unlike plain SGD on BKT](optimnn-hyperparameter-insensitivity.md) — related
