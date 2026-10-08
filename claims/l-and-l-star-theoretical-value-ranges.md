---
type: claim
title: "Theoretical ranges differ sharply: L with self-transitions removed is bounded below by −1 (individual base rates) or −2 (averaged), while L* is bounded by −k+1 (individual) or has no finite lower bound (averaged)"
description: "Theoretical ranges differ sharply: L with self-transitions removed is bounded below by −1 (individual base rates) or −2 (averaged), while L* is bounded by −k+1 (individual) or has no finite lower bound (averaged)"
id: l-and-l-star-theoretical-value-ranges
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

# Theoretical ranges differ sharply: L with self-transitions removed is bounded below by −1 (individual base rates) or −2 (averaged), while L* is bounded by −k+1 (individual) or has no finite lower bound (averaged)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`

## Subclaims
`q2 i?` The minimum values of L and L* depend on both the statistic used and the base-rate computation procedure, as established by Theorems 3–6. [→ Jeffrey Matayoshi and Shamya Karumbaiah 2020](#jeffrey-matayoshi-and-shamya-karumbaiah-2020)

## Evidence

### Jeffrey Matayoshi and Shamya Karumbaiah 2020

Jeffrey Matayoshi and Shamya Karumbaiah. (2020). Adjusting the L Statistic when Self-Transitions are Excluded in Affect Dynamics. Journal of Educational Data Mining, Volume 12, No 4. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/478

`q2 · i?` · `theoretical · r3`

Mathematical derivation (Theorems 3–6) establishing: L ranges [−1, 1] or [−2, 1] with self-transitions removed (individual vs averaged base rates); L* ranges [−k+1, 1] or (−∞, 1] with transitions to A removed. Maximum value is 1 for both statistics.

> "The results show that the minimum values differ greatly based on the statistic used (L or L∗), as well as the procedure used to compute the base rates (per sequence or over all sequences)."

## Discussion


## Related Claims
- [On real student data, L with self-transitions removed makes all transitions from flow appear positive and significant, while L* gives a mix of signs with the only significant value negative](l-star-student-data-more-coherent-than-l.md) — related
- [Simulations show L* values at chance stay centered at zero even when one affective state's base rate is disproportionately high](l-star-chance-zero-nonuniform-base-rates-simulation.md) — related
- [Simulations with two dominant base rates also show L* at chance centered at zero](l-star-chance-zero-two-dominant-base-rates.md) — related
- [When self-transitions are excluded, the L statistic's chance value becomes 1/(n−1)² for a state space with n affective states, so past L results excluding self-transitions were likely misinterpreted](l-chance-value-nonzero-self-transitions-excluded.md) — related
