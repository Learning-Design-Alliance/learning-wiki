---
type: claim
title: "Simulated quenching yields higher expected enrollment gains (31.9%–32.3%) than stochastic hill climbing (31.4%) at equal iteration counts, at runtime cost proportional to the temperature-holding parameter"
description: "Simulated quenching yields higher expected enrollment gains (31.9%–32.3%) than stochastic hill climbing (31.4%) at equal iteration counts, at runtime cost proportional to the temperature-holding parameter"
id: simulated-quenching-beats-hill-climbing
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: weak
sources:
  - id: vinhthuy-phan-2022
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/609"
    title: "Vinhthuy Phan, Laura Wright, Bridgette Decent. (2022). Optimizing Financial Aid Allocation to Improve Access and Affordability to Higher Education. Journal of Educational Data Mining, Volume 14, No 3. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/609"
    author: Vinhthuy Phan, Laura Wright, Bridgette Decent
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Simulated quenching yields higher expected enrollment gains (31.9%–32.3%) than stochastic hill climbing (31.4%) at equal iteration counts, at runtime cost proportional to the temperature-holding parameter

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` With both methods set to 100 iterations, simulated quenching achieves a higher increase in expected enrollment than stochastic hill climbing, and the increase grows with higher values of the parameter M. [→ Vinhthuy Phan 2022](#vinhthuy-phan-2022)

## Evidence

### Vinhthuy Phan 2022

Vinhthuy Phan, Laura Wright, Bridgette Decent. (2022). Optimizing Financial Aid Allocation to Improve Access and Affordability to Higher Education. Journal of Educational Data Mining, Volume 14, No 3. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/609

`q2 · i?` · `design · r2`

Runtime and performance comparison in Table 6, with the optimization objective set to enrollment and both methods run for N = 100 iterations. The article reports simulated quenching is slower than hill climbing by a constant directly proportional to M, and the enrollment gain grows with M from 1 to 11.

> "In terms of expected change in enrollment, simulated quenching has a higher increase (from 31.9% to 32.3%) than stochastic hill climbing (31.4%)."

## Discussion


## Related Claims
- [Optimizing enrollment alone is costly: it raises enrollment 32% but requires a 48% budget increase and raises average unmet need by $3320, while adding revenue and unmet-need objectives yields balanced gains](multi-objective-optimization-beats-enrollment-only.md) — related
- [Seven budget-friendly strategies increase expected accessibility by 105%–112% while limiting budget increase to less than 7% and keeping unmet-need increases under $500](seven-budget-friendly-accessibility-strategies.md) — related
