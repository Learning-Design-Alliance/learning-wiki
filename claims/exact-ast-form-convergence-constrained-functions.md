---
type: claim
title: On tightly specified functions, LLMs converged on a few exact AST forms (1–14 per 1,000 files) while an open-ended function remained diverse, and source was associated with exact form for all five functions
description: On tightly specified functions, LLMs converged on a few exact AST forms (1–14 per 1,000 files) while an open-ended function remained diverse, and source was associated with exact form for all five functions
id: exact-ast-form-convergence-constrained-functions
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: runlong-ye-2026
    resource: "https://arxiv.org/abs/2610.00863"
    title: "Runlong Ye, Jing Fan, Angela Zavaleta Bernuy, Oscar Karnalim, Paul Denny, Juho Leinonen, and Michael Liut. (2026). Correctness, Convergence, and AI-Generated Code Detection: A Longitudinal Study of Student and Large Language Model Code in Introductory Programming. https://arxiv.org/abs/2610.00863"
    author: Runlong Ye, Jing Fan, Angela Zavaleta Bernuy, Oscar Karnalim, Paul Denny, Juho Leinonen, and Michael Liut
    q: 2
    i: "?"
---

# On tightly specified functions, LLMs converged on a few exact AST forms (1–14 per 1,000 files) while an open-ended function remained diverse, and source was associated with exact form for all five functions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment

## Subclaims
`q2 i?` Source and exact form were associated for all five functions (Pearson's χ2, BH-adjusted q < .001), with Cramér's V ranging from 0.30 for loopy_madness to 0.96 for is_square and sum_string. [→ Runlong Ye 2026](#runlong-ye-2026)

## Evidence

### Runlong Ye 2026

Runlong Ye, Jing Fan, Angela Zavaleta Bernuy, Oscar Karnalim, Paul Denny, Juho Leinonen, and Michael Liut. (2026). Correctness, Convergence, and AI-Generated Code Detection: A Longitudinal Study of Student and Large Language Model Code in Introductory Programming. https://arxiv.org/abs/2610.00863

`q2 · i?`

Pearson's chi-square tests of independence on source-by-form contingency tables from full eligible-file counts, with Benjamini–Hochberg false-discovery control within the five-function family. Cramér's V ranged from 0.30 to 0.96.

> "Source and exact form were associated for all five functions (Pearson's 𝜒 2, BH-adjusted 𝑞<. 001), with Cramér's 𝑉 ranging from 0.30 for loopy_madness to 0.96 for is_square and sum_string."

## Discussion


## Related Claims
- [Student solutions became less varied on four of five selected functions by 2025, with exact-form declines of 18.4–51.1%, while the open-ended loopy_madness did not decline](student-exact-form-diversity-declined-constrained-functions.md) — related
- [Solutions from different LLM providers converged broadly on most CS1 labs, with cross-LLM MOSS match rates of about 88% pooled across labs but only 13.18–22.11% on Lab 10](cross-llm-convergence-task-dependent.md) — related
- [LLMs across five models generate diverse erroneous Java code, with mean AST edit distances varying by model and prompting strategy](llms-generate-diverse-erroneous-java-code-varying-by-model-and-prompt.md) — related
