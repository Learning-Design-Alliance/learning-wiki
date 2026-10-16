---
type: claim
title: For tracking time-varying systems, the step size is kept strictly away from zero
description: For tracking time-varying systems, the step size is kept strictly away from zero
id: constant-step-size-tracking-nonstationary-systems
status: review
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

# For tracking time-varying systems, the step size is kept strictly away from zero

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`

## Subclaims
`q2 i?` When the underlying processes are nonstationary and the optimal parameter value changes with time, the step size is kept strictly away from zero to allow tracking. [→ Harold J. Kushner and G. George Yin 2003](#harold-j-kushner-and-g-george-yin-2003)

## Evidence

### Harold J. Kushner and G. George Yin 2003

Harold J. Kushner and G. George Yin. (2003). Stochastic Approximation and Recursive Algorithms and Applications, Second Edition. Springer-Verlag, New York. https://doi.org/10.1007/b97441

`q2 · i?` · `theoretical · r3`

Motivational statement from the Preface and Introduction describing practice in signal processing and communications applications, where step size is often a small constant or random. The text says "one keepsϵn strictly away from zero in order to allow “tracking.”"

> "The underlying processes are often nonstationary and the optimal value of θ can change with time. Then one keepsϵn strictly away from zero in order to allow “tracking.”"

## Discussion


## Related Claims
- [Iterate averaging with step sizes decreasing slower than O(1/n) converges at an optimal rate](polyak-juditsky-iterate-averaging-optimal-rate.md) — related
- [Diminishing step sizes in stochastic approximation induce implicit averaging that eliminates noise effects in the long run](robbins-monro-diminishing-step-sizes-implicit-averaging.md) — related
- [Many learning algorithms, including neural network training and Q-learning, have recursive forms of the stochastic approximation type](learning-algorithms-stochastic-approximation-recursive-forms.md) — related
