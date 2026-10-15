---
type: claim
title: Diminishing step sizes in stochastic approximation induce implicit averaging that eliminates noise effects in the long run
description: Diminishing step sizes in stochastic approximation induce implicit averaging that eliminates noise effects in the long run
id: robbins-monro-diminishing-step-sizes-implicit-averaging
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

# Diminishing step sizes in stochastic approximation induce implicit averaging that eliminates noise effects in the long run

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`

## Subclaims
`q2 i?` If the step sizes in parameter updates are allowed to go to zero in an appropriate way, implicit averaging eliminates the effects of noise in the long run. [→ Harold J. Kushner and G. George Yin 2003](#harold-j-kushner-and-g-george-yin-2003)

## Evidence

### Harold J. Kushner and G. George Yin 2003

Harold J. Kushner and G. George Yin. (2003). Stochastic Approximation and Recursive Algorithms and Applications, Second Edition. Springer-Verlag, New York. https://doi.org/10.1007/b97441

`q2 · i?` · `theoretical · r3`

Analytical statement from the Preface and Introduction of the monograph, attributed to Robbins and Monro's foundational insight. The text states there is "an implicit averaging that eliminates the eﬀects of the noise in the long run" when step sizes go to zero appropriately.

> "A major insight of Robbins and Monro was that, if the step sizes in the parameter updates are allowed to go to zero in an appropriate way as n →∞ , then there is an implicit averaging that eliminates the eﬀects of the noise in the long run."

## Discussion


## Related Claims
- [For tracking time-varying systems, the step size is kept strictly away from zero](constant-step-size-tracking-nonstationary-systems.md) — related
- [Many learning algorithms, including neural network training and Q-learning, have recursive forms of the stochastic approximation type](learning-algorithms-stochastic-approximation-recursive-forms.md) — related
- [Iterate averaging with step sizes decreasing slower than O(1/n) converges at an optimal rate](polyak-juditsky-iterate-averaging-optimal-rate.md) — a narrower finding that bears on this claim
