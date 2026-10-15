---
type: claim
title: Most reported student–LLM matches involved short snippets, and raising the minimum match length rapidly reduced coverage, making it a key review-workload control
description: Most reported student–LLM matches involved short snippets, and raising the minimum match length rapidly reduced coverage, making it a key review-workload control
id: minimum-match-length-controls-coverage
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
  - id: runlong-ye-2026-2
    resource: "https://arxiv.org/abs/2610.00863"
    title: "Runlong Ye, Jing Fan, Angela Zavaleta Bernuy, Oscar Karnalim, Paul Denny, Juho Leinonen, and Michael Liut. (2026). Correctness, Convergence, and AI-Generated Code Detection: A Longitudinal Study of Student and Large Language Model Code in Introductory Programming. https://arxiv.org/abs/2610.00863"
    author: Runlong Ye, Jing Fan, Angela Zavaleta Bernuy, Oscar Karnalim, Paul Denny, Juho Leinonen, and Michael Liut
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Most reported student–LLM matches involved short snippets, and raising the minimum match length rapidly reduced coverage, making it a key review-workload control

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 associational `r2` · `q2`

## Subclaims
`q2 i?` Across cohorts, the median reported overlap spanned 8–9 lines and 97.0–99.4% of cross-matches contained fewer than 30 matched lines. [→ Runlong Ye 2026](#runlong-ye-2026)
`q2 i?` At a 30-line minimum, 2.9–3.5% of 2021 student files and 10.8–16.7% of 2025 LLM attempts still had a match; at 50 lines student-file coverage was near zero and LLM-attempt coverage fell to 0.5–1.1%. [→ Runlong Ye 2026 (2)](#runlong-ye-2026-2)

## Evidence

### Runlong Ye 2026

Runlong Ye, Jing Fan, Angela Zavaleta Bernuy, Oscar Karnalim, Paul Denny, Juho Leinonen, and Michael Liut. (2026). Correctness, Convergence, and AI-Generated Code Detection: A Longitudinal Study of Student and Large Language Model Code in Introductory Programming. https://arxiv.org/abs/2610.00863 [doi:10.48550/arxiv.2610.00863](https://doi.org/10.48550/arxiv.2610.00863)

`q2 · i?` · `associational · r2`

Distributional analysis of MOSS-reported matched-line counts for student–LLM cross-matches across the three cohorts, with docstrings retained as submitted or generated. The article reports the median and the share under 30 lines.

> "Across cohorts, the median reported overlap spanned 8–9 lines, and 97.0–99.4% of cross-matches contained fewer than 30 matched lines."

### Runlong Ye 2026 (2)

Runlong Ye, Jing Fan, Angela Zavaleta Bernuy, Oscar Karnalim, Paul Denny, Juho Leinonen, and Michael Liut. (2026). Correctness, Convergence, and AI-Generated Code Detection: A Longitudinal Study of Student and Large Language Model Code in Introductory Programming. https://arxiv.org/abs/2610.00863

`q2 · i?` · `associational · r2`

Post-processing sensitivity analysis (Figure 4) applying minimum match length filters to the same student–LLM match lists while keeping the MOSS algorithm unchanged, reporting retained shares of student files and LLM attempts by threshold.

> "At 30 lines, 2.9–3.5% of 2021 historical-reference student files and 10.8–16.7% of 2025 LLM attempts still had a match. At 50 lines, student-file coverage was near zero, and LLM-attempt coverage fell to 0.5–1.1%."

## Discussion


## Related Claims
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [Student submissions matched the LLM-generated reference bank more often in later cohorts, with 2025 incidence 1.76–2.12 times the 2021 rate, persisting among full-pass submissions](student-llm-match-incidence-rose-across-cohorts.md) — related
