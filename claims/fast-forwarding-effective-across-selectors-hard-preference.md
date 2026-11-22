---
type: claim
title: "Fast-Forwarding reduces overpractice across all problem selectors (0.1% to 35.7%), with the largest reduction for selectors that preferentially select difficult problems"
description: "Fast-Forwarding reduces overpractice across all problem selectors (0.1% to 35.7%), with the largest reduction for selectors that preferentially select difficult problems"
id: fast-forwarding-effective-across-selectors-hard-preference
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: meng-xia-2025
    resource: "https://doi.org/10.1007/978-3-032-03870-8_37"
    title: "Meng Xia, Robin Schmucker, Conrad Borchers, and Vincent Aleven. (2025). Optimizing Mastery Learning by Fast-Forwarding Over-Practice Steps. arXiv preprint arXiv:2506.17577. [doi:10.1007/978-3-032-03870-8_37](https://doi.org/10.1007/978-3-032-03870-8_37)"
    author: Meng Xia, Robin Schmucker, Conrad Borchers, and Vincent Aleven
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: meng-xia-2025-2
    resource: "https://doi.org/10.1007/978-3-032-03870-8_37"
    title: "Meng Xia, Robin Schmucker, Conrad Borchers, and Vincent Aleven. (2025). Optimizing Mastery Learning by Fast-Forwarding Over-Practice Steps. arXiv preprint arXiv:2506.17577. [doi:10.1007/978-3-032-03870-8_37](https://doi.org/10.1007/978-3-032-03870-8_37)"
    author: Meng Xia, Robin Schmucker, Conrad Borchers, and Vincent Aleven
    q: 2
    i: 3
    kind: design
    rigour: 2
---

# Fast-Forwarding reduces overpractice across all problem selectors (0.1% to 35.7%), with the largest reduction for selectors that preferentially select difficult problems

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2` · `i3` large
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Fast-Forwarding consistently reduced overpractice across all problem selectors, ranging from 0.1% to 35.7%. [→ Meng Xia 2025](#meng-xia-2025)
`q2 i3` The mastery-hard selector showed the largest overpractice reduction (35.7%) with lower between-student variation, a between-selector effect the authors report as a substantial effect size of 3.4 SD. [→ Meng Xia 2025 (2)](#meng-xia-2025-2)

## Evidence

### Meng Xia 2025

Meng Xia, Robin Schmucker, Conrad Borchers, and Vincent Aleven. (2025). Optimizing Mastery Learning by Fast-Forwarding Over-Practice Steps. arXiv preprint arXiv:2506.17577. [doi:10.1007/978-3-032-03870-8_37](https://doi.org/10.1007/978-3-032-03870-8_37)

`q2 · i?` · `causal · r2`

RQ2 simulation assuming unlimited practice time, comparing Fast-Forwarding applied to random, deterministic, mastery easy, mastery hard, and focused practice selectors. The paper reports reductions "ranging from 0.1% to 35.7%" across selectors; no standardized effect size for this range is printed.

> "Notably, Fast-Forwarding consistently reduced overpractice across all problem selectors, ranging from 0.1% to 35.7%."

### Meng Xia 2025 (2)

Meng Xia, Robin Schmucker, Conrad Borchers, and Vincent Aleven. (2025). Optimizing Mastery Learning by Fast-Forwarding Over-Practice Steps. arXiv preprint arXiv:2506.17577. [doi:10.1007/978-3-032-03870-8_37](https://doi.org/10.1007/978-3-032-03870-8_37)

`q2 · i3` · `design · r2`

RQ2 simulation across selection regimes. The paper states mastery hard showed the largest reduction (35.7%) with lower between-student variation, "corresponding to a substantial effect size of 3.4SD". Mastery easy showed only marginal reductions; focused practice showed 7.9% (0.41 SD).

> "the mastery hard problem selector was more desirable based on the reported largest reduction in overpractice (35.7%; RQ1)and lower between-student variation, corresponding to a substantial effect size of 3.4SD."

## Discussion


## Related Claims
- [Fast-Forwarding reduces overpractice by 35.7% under the legacy mastery-hard problem selector in a simulated linear equation-solving tutor with limited practice time](fast-forwarding-reduces-overpractice-35-7-percent-mastery-hard.md) — a narrower finding that bears on this claim
- [A prefer-harder problem-selection constraint reduces overpractice for the risk-averse strategy in the equation-solving dataset](prefer-harder-constraint-reduces-overpractice.md) — related
- [Fast-Forwarding did not change underpractice (M = 0.44 vs. M = 0.43), indicating overall mastery levels do not suffer](fast-forwarding-underpractice-unchanged.md) — related
- [The redesign showed no reliable evidence of reducing overpractice beyond 80% mastery](no-overpractice-reduction-evidence.md) — reports the opposite
