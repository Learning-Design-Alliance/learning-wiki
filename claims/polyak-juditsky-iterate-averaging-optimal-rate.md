---
type: claim
title: Iterate averaging with step sizes decreasing slower than O(1/n) converges at an optimal rate
description: Iterate averaging with step sizes decreasing slower than O(1/n) converges at an optimal rate
id: polyak-juditsky-iterate-averaging-optimal-rate
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-14
evidence_strength: weak
newest_evidence: 2003
recheck_by: 2006
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

# Iterate averaging with step sizes decreasing slower than O(1/n) converges at an optimal rate

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`
> **Currency** · newest study 2003 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2006**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` When coefficients go to zero slower than O(1/n), the averaged iterate sequence converges to its limit at an optimal rate, allowing relatively large step sizes with offline averaging handling increased noise. [→ Harold J. Kushner and G. George Yin 2003](#harold-j-kushner-and-g-george-yin-2003)

## Evidence

### Harold J. Kushner and G. George Yin 2003

Harold J. Kushner and G. George Yin. (2003). Stochastic Approximation and Recursive Algorithms and Applications, Second Edition. Springer-Verlag, New York. https://doi.org/10.1007/b97441

`q2 · i?` · `theoretical · r3`

Analytical result reported in the Preface, attributed to Polyak and Juditsky. The monograph notes these results "have since been corroborated by numerous simulations and extended mathematically."

> "Polyak and Juditsky showed that, if the coeﬃcients ϵn go to zero “slower” than O(1/n), then the averaged sequence∑n i=1 θi/n converges to its limit at an optimal rate."

## Discussion


## Related Claims
- [For tracking time-varying systems, the step size is kept strictly away from zero](constant-step-size-tracking-nonstationary-systems.md) — related
- [Many learning algorithms, including neural network training and Q-learning, have recursive forms of the stochastic approximation type](learning-algorithms-stochastic-approximation-recursive-forms.md) — related
- [Diminishing step sizes in stochastic approximation induce implicit averaging that eliminates noise effects in the long run](robbins-monro-diminishing-step-sizes-implicit-averaging.md) — a broader claim this one bears on
- [Hyperparameter sweeps reproduce the lesson's claims: γ = 0 never solves the task while ε = 1 still converges](hyperparameter-sweeps-reproduce-lesson-claims.md) — related
