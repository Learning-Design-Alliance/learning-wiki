---
type: claim
title: "GPT-4's grading accuracy correlates with its problem-solving ability, and a mark scheme removes this dependence"
description: "GPT-4's grading accuracy correlates with its problem-solving ability, and a mark scheme removes this dependence"
id: gpt4-solving-grading-correlation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: mok-2025
    resource: "https://doi.org/10.1088/1361-6552/adb92b"
    title: "Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli. (2025). Using AI Large Language Models for Grading in Education: A Hands-On Test for Physics. arXiv. Originally published 2024. [doi:10.1088/1361-6552/adb92b](https://doi.org/10.1088/1361-6552/adb92b)"
    author: Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: mok-2025-2
    resource: "https://doi.org/10.1088/1361-6552/adb92b"
    title: "Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli. (2025). Using AI Large Language Models for Grading in Education: A Hands-On Test for Physics. arXiv. Originally published 2024. [doi:10.1088/1361-6552/adb92b](https://doi.org/10.1088/1361-6552/adb92b)"
    author: Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4's grading accuracy correlates with its problem-solving ability, and a mark scheme removes this dependence

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For GPT-4 blind grading, the deviation between GPT-4 and human grades is high where GPT-4 solved the problem poorly and low where it solved it well (r = −0.66). [→ Mok 2025](#mok-2025)
`q2 i?` With a mark scheme, the solving-grading relationship is effectively removed, with a near-flat best-fit line (r = −0.12). [→ Mok 2025 (2)](#mok-2025-2)

## Evidence

### Mok 2025

Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli. (2025). Using AI Large Language Models for Grading in Education: A Hands-On Test for Physics. arXiv. Originally published 2024. [doi:10.1088/1361-6552/adb92b](https://doi.org/10.1088/1361-6552/adb92b)

`q2 · i?` · `causal · r1`

Difference-plot analysis (Fig. 15) using human grade as a proxy for GPT-4's problem-solving success; without a mark scheme the fit is y = (−0.44 ± 0.05)x + (42 ± 4), r = −0.66.

> "One can see from Fig. 15 that there is a correlation between GPT-4 ability to solve a problem and its ability to grade. At low values of average human grade where GPT-4 has solved the problem poorly, the deviation between human and GPT-4 grades is high, and GPT-4 grades poorly."

### Mok 2025 (2)

Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli. (2025). Using AI Large Language Models for Grading in Education: A Hands-On Test for Physics. arXiv. Originally published 2024. [doi:10.1088/1361-6552/adb92b](https://doi.org/10.1088/1361-6552/adb92b)

`q2 · i?` · `design · r2`

Same Fig. 15 analysis with mark-scheme grading: y = (−0.08 ± 0.07)x + (7 ± 5), r = −0.12; the article explains GPT-4 can rely on the mark scheme when it cannot gauge the solution itself.

> "Then, upon applying the mark scheme, this behaviour is effectively removed, as indicated by the near flat line of best fit."

## Discussion


## Related Claims
- [Providing a mark scheme substantially improves LLM grading accuracy and consistency, with GPT-4 shifting closest to human grades](mark-scheme-improves-llm-grading.md) — related
- [Blind LLM grading of undergraduate physics solutions is substantially more lenient than human grading, driven by mathematical hallucinations](llm-blind-grading-lenient-hallucinations.md) — related
- [In one reviewed study, GPT-4 automated essay scoring showed score inflation, with AI–human rating discrepancies exceeding 1.5 standard deviations in 38% of graduate-level bibliographies](gpt4-essay-score-inflation.md) — related
- [Human Graders of Open-Ended Work Agree With Each Other Less Than Treating One Grade as Ground Truth Implies](human-graders-agree-less-than-single-grade-ground-truth-implies.md) — related
- [GPT-4 performs exceptionally well on coding tasks and simple single-step problems, but poorly on multi-step problems, longer prose, and interdisciplinary problems.](gpt4-strong-coding-weak-multistep-prose.md) — related
