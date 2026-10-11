---
type: claim
title: The average effect of verified AI materials attenuates when the lowest pre-intervention marks are removed, while the threshold effect at the upper-second boundary is robust
description: The average effect of verified AI materials attenuates when the lowest pre-intervention marks are removed, while the threshold effect at the upper-second boundary is robust
id: average-effect-fragile-threshold-robust
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: dang-2026
    resource: "https://arxiv.org/abs/2610.07097"
    title: "Dang, C. T., & Nguyen, A. (2026). Verified, not generated: expert-verified AI study materials and the distribution of learning gains in a university course. https://arxiv.org/abs/2610.07097"
    author: "Dang, C. T., & Nguyen, A."
    q: 2
    i: "?"
  - id: dang-2026-2
    resource: "https://arxiv.org/abs/2610.07097"
    title: "Dang, C. T., & Nguyen, A. (2026). Verified, not generated: expert-verified AI study materials and the distribution of learning gains in a university course. https://arxiv.org/abs/2610.07097"
    author: "Dang, C. T., & Nguyen, A."
    q: 2
    i: "?"
---

# The average effect of verified AI materials attenuates when the lowest pre-intervention marks are removed, while the threshold effect at the upper-second boundary is robust

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · `q2` quasi-experiment

## Subclaims
`q2 i?` Dropping the three lowest-scoring students in the pre-intervention treated cell reduces the average effect from 2.34 to 1.88 marks (HC1 p = 0.099; clustered p = 0.041); dropping eight reduces it to 1.41 (clustered p = 0.127). [→ Dang 2026](#dang-2026)
`q2 i?` The below-30 threshold estimate remains between −19.9 and −22.9 percentage points with p ≤ 0.006 in every drop specification. [→ Dang 2026 (2)](#dang-2026-2)

## Evidence

### Dang 2026

Dang, C. T., & Nguyen, A. (2026). Verified, not generated: expert-verified AI study materials and the distribution of learning gains in a university course. https://arxiv.org/abs/2610.07097

`q2 · i?`

Sensitivity re-estimation of the difference-in-differences average effect after removing the lowest-scoring students (with both marks) from the 2023/24 Part 2 cell, and after winsorising from below (2.14 at the pooled 5th percentile, p = 0.057; 1.34 at the 10th, p = 0.173).

> "Dropping the three lowest-scoring students reduces it from 2.34 to 1.88 marks (HC1 p = 0.099; student-clustered p = 0.041), dropping five reduces it to 1.56 (clustered p = 0.085), and dropping eight reduces it to 1.41 (clustered p = 0.127)."

### Dang 2026 (2)

Dang, C. T., & Nguyen, A. (2026). Verified, not generated: expert-verified AI study materials and the distribution of learning gains in a university course. https://arxiv.org/abs/2610.07097

`q2 · i?`

Sensitivity re-estimation of the below-30 linear-probability estimate in the same exercise. The article notes the exercise is stringent by construction because it removes low marks only from the pre-intervention treated cell, biasing estimates toward zero.

> "The threshold estimate at the upper-second boundary is stable when students are removed, lying between −19.9 and −22.9 percentage points with p ≤ 0.006 in every case; winsorising below 30 leaves it unchanged by construction."

## Discussion


## Related Claims
- [Access to expert-verified AI study materials is associated with a 2.34-mark difference-in-differences advantage on a 50-mark examination component, reflecting protection from a decline rather than a rise](did-2-34-mark-advantage-verified-ai-materials.md) — related
- [The share of marks below the upper-second classification boundary fell by 24.7 percentage points, with effects significant at every threshold from 23 to 31 marks and at none above](threshold-effect-upper-second-boundary.md) — related
- [Gains from verified AI materials are concentrated in the bottom quintile, which accounts for roughly three-quarters of the average effect](gains-bottom-quintile-verified-ai.md) — related
