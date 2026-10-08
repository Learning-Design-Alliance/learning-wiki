---
type: claim
title: "Simulations show L* values at chance stay centered at zero even when one affective state's base rate is disproportionately high"
description: "Simulations show L* values at chance stay centered at zero even when one affective state's base rate is disproportionately high"
id: l-star-chance-zero-nonuniform-base-rates-simulation
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
sources:
  - id: jeffrey-matayoshi-and-shamya-karumbaiah-2020
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/478"
    title: "Jeffrey Matayoshi and Shamya Karumbaiah. (2020). Adjusting the L Statistic when Self-Transitions are Excluded in Affect Dynamics. Journal of Educational Data Mining, Volume 12, No 4. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/478"
    author: Jeffrey Matayoshi and Shamya Karumbaiah
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# Simulations show L* values at chance stay centered at zero even when one affective state's base rate is disproportionately high

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`

## Subclaims
`q2 i?` In simulated sequences with base rates varying from uniform to highly non-uniform, L* at chance remains close to zero, with maximum 0.002 and minimum -0.002. [→ Jeffrey Matayoshi and Shamya Karumbaiah 2020](#jeffrey-matayoshi-and-shamya-karumbaiah-2020)

## Evidence

### Jeffrey Matayoshi and Shamya Karumbaiah 2020

Jeffrey Matayoshi and Shamya Karumbaiah. (2020). Adjusting the L Statistic when Self-Transitions are Excluded in Affect Dynamics. Journal of Educational Data Mining, Volume 12, No 4. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/478

`q2 · i?` · `theoretical · r3`

First simulation study: 24 sets of 50,000 randomly generated sequences of 21 states, with the base rate of A ranging from 0.25 to 0.94. Individual and mean base-rate methods gave "essentially identical" results, indicating insensitivity to unequal base rates.

> "the L∗ values are indeed very close to, and centered at, zero. The maximum and minimum values are 0.002 and -0.002, respectively."

## Discussion


## Related Claims
- [Theoretical ranges differ sharply: L with self-transitions removed is bounded below by −1 (individual base rates) or −2 (averaged), while L* is bounded by −k+1 (individual) or has no finite lower bound (averaged)](l-and-l-star-theoretical-value-ranges.md) — related
- [When self-transitions are excluded, the L statistic's chance value becomes 1/(n−1)² for a state space with n affective states, so past L results excluding self-transitions were likely misinterpreted](l-chance-value-nonzero-self-transitions-excluded.md) — related
- [Simulations with two dominant base rates also show L* at chance centered at zero](l-star-chance-zero-two-dominant-base-rates.md) — related
