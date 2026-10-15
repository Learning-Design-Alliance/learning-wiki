---
type: claim
title: "Student solutions became less varied on four of five selected functions by 2025, with exact-form declines of 18.4–51.1%, while the open-ended loopy_madness did not decline"
description: "Student solutions became less varied on four of five selected functions by 2025, with exact-form declines of 18.4–51.1%, while the open-ended loopy_madness did not decline"
id: student-exact-form-diversity-declined-constrained-functions
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: runlong-ye-2026
    resource: "https://doi.org/10.48550/arxiv.2610.00863"
    title: "Runlong Ye, Jing Fan, Angela Zavaleta Bernuy, Oscar Karnalim, Paul Denny, Juho Leinonen, and Michael Liut. (2026). Correctness, Convergence, and AI-Generated Code Detection: A Longitudinal Study of Student and Large Language Model Code in Introductory Programming. https://arxiv.org/abs/2610.00863 [doi:10.48550/arxiv.2610.00863](https://doi.org/10.48550/arxiv.2610.00863)"
    author: Runlong Ye, Jing Fan, Angela Zavaleta Bernuy, Oscar Karnalim, Paul Denny, Juho Leinonen, and Michael Liut
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Student solutions became less varied on four of five selected functions by 2025, with exact-form declines of 18.4–51.1%, while the open-ended loopy_madness did not decline

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` Relative to 2021, distinct exact AST forms per 1,000 files in 2025 were lower by 51.1% for my_and, 25.4% for exists_triangle, 22.9% for sum_string, and 18.4% for is_square, but 5.1% higher for loopy_madness with an interval including zero. [→ Runlong Ye 2026](#runlong-ye-2026)

## Evidence

### Runlong Ye 2026

Runlong Ye, Jing Fan, Angela Zavaleta Bernuy, Oscar Karnalim, Paul Denny, Juho Leinonen, and Michael Liut. (2026). Correctness, Convergence, and AI-Generated Code Detection: A Longitudinal Study of Student and Large Language Model Code in Introductory Programming. https://arxiv.org/abs/2610.00863 [doi:10.48550/arxiv.2610.00863](https://doi.org/10.48550/arxiv.2610.00863)

`q2 · i?` · `associational · r2`

Cohort comparison of distinct serialized AST forms across 2021, 2023, and 2025 using each cohort's full eligible pool, with Poisson 95% intervals and an exact interval on the 2021-to-2025 rate ratio (Figure 3). The four declines exclude zero; the loopy_madness interval does not.

> "Relative to 2021, the number of exact forms per 1,000 files in 2025 was lower by 51.1% for my_and (95% CI 35–64%), 25.4% for exists_triangle (16–34%), 22.9% for sum_string (14–31%), and 18.4% for is_square (7–28%)."

## Discussion


## Related Claims
- [On tightly specified functions, LLMs converged on a few exact AST forms (1–14 per 1,000 files) while an open-ended function remained diverse, and source was associated with exact form for all five functions](exact-ast-form-convergence-constrained-functions.md) — related
