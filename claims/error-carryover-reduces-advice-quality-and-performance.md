---
type: claim
title: Carryover of user errors into AI advice reduces both advice quality and final ranking accuracy
description: Carryover of user errors into AI advice reduces both advice quality and final ranking accuracy
id: error-carryover-reduces-advice-quality-and-performance
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: cansu-koyuturk-2026
    resource: "https://arxiv.org/abs/2605.18372"
    title: "Cansu Koyuturk, Sabrina Guidotti, and Dimitri Ognibene. (2026). The Hidden Cost of Contextual Sycophancy: an AI Literacy Intervention in Human–AI Collaboration. https://arxiv.org/abs/2605.18372"
    author: Cansu Koyuturk, Sabrina Guidotti, and Dimitri Ognibene
    q: 3
    i: "?"
    kind: causal
    rigour: 2
  - id: cansu-koyuturk-2026-2
    resource: "https://arxiv.org/abs/2605.18372"
    title: "Cansu Koyuturk, Sabrina Guidotti, and Dimitri Ognibene. (2026). The Hidden Cost of Contextual Sycophancy: an AI Literacy Intervention in Human–AI Collaboration. https://arxiv.org/abs/2605.18372"
    author: Cansu Koyuturk, Sabrina Guidotti, and Dimitri Ognibene
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Carryover of user errors into AI advice reduces both advice quality and final ranking accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3`

## Subclaims
`q3 i?` Advice quality was negatively associated with the proportion of user errors carried over into the assistant's advice (b = -0.390, p < .001), while positively associated with overall overlap (b = 0.933, p < .001). [→ Cansu Koyuturk 2026](#cansu-koyuturk-2026)
`q3 i?` Carryover of user errors significantly reduced final ranking accuracy (b = -0.092, p < .001), whereas overall overlap was not significant. [→ Cansu Koyuturk 2026 (2)](#cansu-koyuturk-2026-2)

## Evidence

### Cansu Koyuturk 2026

Cansu Koyuturk, Sabrina Guidotti, and Dimitri Ognibene. (2026). The Hidden Cost of Contextual Sycophancy: an AI Literacy Intervention in Human–AI Collaboration. https://arxiv.org/abs/2605.18372

`q3 · i?` · `causal · r2`

Regression modeling advice quality as a function of user–assistant overlap (proportion of shared items between the user's initial ranking and the assistant's advice) and error carryover in the 60-participant experiment. The article reports "b = -0.390, SE = 0.043, z = -9.08, p < .001" for carryover.

> "Advice quality was positively associated with overall overlap, b = 0.933, SE = 0.128, z = 7.31, p < .001, but negatively associated with the proportion of user errors carried over into the assistant’s advice, b = -0.390, SE = 0.043, z = -9.08, p < .001."

### Cansu Koyuturk 2026 (2)

Cansu Koyuturk, Sabrina Guidotti, and Dimitri Ognibene. (2026). The Hidden Cost of Contextual Sycophancy: an AI Literacy Intervention in Human–AI Collaboration. https://arxiv.org/abs/2605.18372

`q3 · i?` · `causal · r2`

Regression of final ranking accuracy on error carryover and overlap in the same experiment. The article reports "b = -0.092, SE = 0.021, z = -4.39, p < .001" for carryover, with overall overlap not significant.

> "Carryover of user errors significantly reduced final performance, b = -0.092, SE = 0.021, z = -4.39, p < .001, whereas overall overlap was not significant."

## Discussion


## Related Claims
- [Users' baseline ranking accuracy significantly predicts the quality of the AI assistant's advice](baseline-accuracy-predicts-advice-quality.md) — related
- [Users' baseline ranking accuracy significantly predicts their final ranking accuracy after AI collaboration, with no other significant effects](baseline-accuracy-predicts-final-ranking-accuracy.md) — related
- [The prompting intervention did not reduce general propagation of user errors into AI advice](intervention-did-not-reduce-error-propagation.md) — related
- [The sycophancy-focused intervention significantly reduced the assistant's positional mirroring of incorrect user rankings and rank-order alignment](intervention-reduced-positional-mimicry.md) — related
