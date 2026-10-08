---
type: claim
title: "When self-transitions are excluded, the L statistic's chance value becomes 1/(n−1)² for a state space with n affective states, so past L results excluding self-transitions were likely misinterpreted"
description: "When self-transitions are excluded, the L statistic's chance value becomes 1/(n−1)² for a state space with n affective states, so past L results excluding self-transitions were likely misinterpreted"
id: l-chance-value-nonzero-self-transitions-excluded
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

# When self-transitions are excluded, the L statistic's chance value becomes 1/(n−1)² for a state space with n affective states, so past L results excluding self-transitions were likely misinterpreted

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`

## Subclaims
`q2 i?` Removing self-transitions violates the independence assumption, so the L value at chance is 1/(n−1)² rather than zero when n > 2 affective states are observed. [→ Jeffrey Matayoshi and Shamya Karumbaiah 2020](#jeffrey-matayoshi-and-shamya-karumbaiah-2020)

## Evidence

### Jeffrey Matayoshi and Shamya Karumbaiah 2020

Jeffrey Matayoshi and Shamya Karumbaiah. (2020). Adjusting the L Statistic when Self-Transitions are Excluded in Affect Dynamics. Journal of Educational Data Mining, Volume 12, No 4. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/478

`q2 · i?` · `theoretical · r3`

Theoretical analysis reported in the introduction, attributing the finding to Karumbaiah et al. (2019): excluding self-transitions breaks independence, so "we can then no longer assume that zero represents the at chance value of L" and past results were likely misinterpreted.

> "as observed by Karumbaiah et al. (2019), removing self-transitions violates the assumption of independence between Bnext and Aprev, as the next state can now only take on values other than A."

## Discussion


## Related Claims
- [Simulations show L* values at chance stay centered at zero even when one affective state's base rate is disproportionately high](l-star-chance-zero-nonuniform-base-rates-simulation.md) — related
- [Simulations with two dominant base rates also show L* at chance centered at zero](l-star-chance-zero-two-dominant-base-rates.md) — related
- [On real student data, L with self-transitions removed makes all transitions from flow appear positive and significant, while L* gives a mix of signs with the only significant value negative](l-star-student-data-more-coherent-than-l.md) — related
- [Theoretical ranges differ sharply: L with self-transitions removed is bounded below by −1 (individual base rates) or −2 (averaged), while L* is bounded by −k+1 (individual) or has no finite lower bound (averaged)](l-and-l-star-theoretical-value-ranges.md) — related
