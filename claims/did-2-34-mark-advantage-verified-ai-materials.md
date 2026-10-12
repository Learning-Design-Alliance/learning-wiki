---
type: claim
title: Access to expert-verified AI study materials is associated with a 2.34-mark difference-in-differences advantage on a 50-mark examination component, reflecting protection from a decline rather than a rise
description: Access to expert-verified AI study materials is associated with a 2.34-mark difference-in-differences advantage on a 50-mark examination component, reflecting protection from a decline rather than a rise
id: did-2-34-mark-advantage-verified-ai-materials
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
    kind: causal
    rigour: 2
  - id: dang-2026-2
    resource: "https://arxiv.org/abs/2610.07097"
    title: "Dang, C. T., & Nguyen, A. (2026). Verified, not generated: expert-verified AI study materials and the distribution of learning gains in a university course. https://arxiv.org/abs/2610.07097"
    author: "Dang, C. T., & Nguyen, A."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Access to expert-verified AI study materials is associated with a 2.34-mark difference-in-differences advantage on a 50-mark examination component, reflecting protection from a decline rather than a rise

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` In a two-cohort difference-in-differences design (170 students, 340 marks), access to verified AI materials was associated with a 2.34-mark advantage (p = 0.045 HC1; p = 0.013 clustered). [→ Dang 2026](#dang-2026)
`q2 i?` The estimate reflects the treated half holding its level while the untreated half declined: Part 2 rose by a non-significant 0.73 marks while Part 1 fell by 1.61 marks (p = 0.021). [→ Dang 2026 (2)](#dang-2026-2)

## Evidence

### Dang 2026

Dang, C. T., & Nguyen, A. (2026). Verified, not generated: expert-verified AI study materials and the distribution of learning gains in a university course. https://arxiv.org/abs/2610.07097

`q2 · i?` · `causal · r2`

Difference-in-differences analysis of examination marks in a compulsory first-year economics course, one treated course-half in 2024/25 against a contemporaneous untreated half and a pre-intervention cohort (85 students per cell; 340 observations). The article reports the estimate as 0.33 standard deviations of the pre-intervention Part 2 distribution, an intention-to-treat effect of "access".

> "The coefficient on Part 2 × Post is 2.341 in all three specifications, identical by construction in a balanced two-by-two panel, with p = 0.045 (HC1), 0.013 (student-clustered) and 0.013 (within-student)."

### Dang 2026 (2)

Dang, C. T., & Nguyen, A. (2026). Verified, not generated: expert-verified AI study materials and the distribution of learning gains in a university course. https://arxiv.org/abs/2610.07097

`q2 · i?` · `causal · r2`

Decomposition of the difference-in-differences estimate in the same OLS analysis: the treated half's mean rose non-significantly, and the article states the estimate "describes protection from a decline rather than a rise". H1 receives qualified support pending the sensitivity results.

> "Part 2 marks rose by 0.73, which is not significant (p = 0.441), while Part 1 marks fell by 1.61 (p = 0.021)."

## Discussion


## Related Claims
- [The average effect of verified AI materials attenuates when the lowest pre-intervention marks are removed, while the threshold effect at the upper-second boundary is robust](average-effect-fragile-threshold-robust.md) — related
- [Gains from verified AI materials are concentrated in the bottom quintile, which accounts for roughly three-quarters of the average effect](gains-bottom-quintile-verified-ai.md) — a narrower finding that bears on this claim
- [The share of marks below the upper-second classification boundary fell by 24.7 percentage points, with effects significant at every threshold from 23 to 31 marks and at none above](threshold-effect-upper-second-boundary.md) — related
- [AI access raises unaided essay quality in both sessions, while AI-generated text detectable in Session One essays disappears by Session Two](genai-raises-unaided-essay-quality.md) — related
- [Mark dispersion narrowed in the treated half alone, with the Part 2 standard deviation falling from 7.09 to 5.03 while Part 1's was unchanged](dispersion-narrowed-treated-half.md) — related
