---
type: claim
title: Providing a mark scheme substantially improves LLM grading accuracy and consistency, with GPT-4 shifting closest to human grades
description: Providing a mark scheme substantially improves LLM grading accuracy and consistency, with GPT-4 shifting closest to human grades
id: mark-scheme-improves-llm-grading
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: mok-2025
    resource: "https://doi.org/10.1088/1361-6552/adb92b"
    title: "Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli. (2025). Using AI Large Language Models for Grading in Education: A Hands-On Test for Physics. arXiv. Originally published 2024. [doi:10.1088/1361-6552/adb92b](https://doi.org/10.1088/1361-6552/adb92b)"
    author: Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: mok-2025-2
    resource: "https://doi.org/10.1088/1361-6552/adb92b"
    title: "Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli. (2025). Using AI Large Language Models for Grading in Education: A Hands-On Test for Physics. arXiv. Originally published 2024. [doi:10.1088/1361-6552/adb92b](https://doi.org/10.1088/1361-6552/adb92b)"
    author: Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli
    q: 2
    i: 3
    kind: design
    rigour: 2
  - id: mok-2025-3
    resource: "https://doi.org/10.1088/1361-6552/adb92b"
    title: "Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli. (2025). Using AI Large Language Models for Grading in Education: A Hands-On Test for Physics. arXiv. Originally published 2024. [doi:10.1088/1361-6552/adb92b](https://doi.org/10.1088/1361-6552/adb92b)"
    author: Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli
    q: 2
    i: 3
    kind: causal
    rigour: 1
---

# Providing a mark scheme substantially improves LLM grading accuracy and consistency, with GPT-4 shifting closest to human grades

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · design `r2` · `q2` · `i3` large
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly
> **Design limits** · Mok 2024 (3): the intervention came bundled with another change (read from the study by two models, 2026-11-20)

## Subclaims
`q2 i?` Introducing a mark scheme shifts each LLM's best-fit line closer to the y = x line, rectifying over-leniency to various extents. [→ Mok 2025](#mok-2025)
`q2 i3` With a mark scheme, GPT-4's best-fit line lies very close to y = x (r = 0.80), and it sometimes grades harsher than humans by failing to recognise equivalent solutions. [→ Mok 2025 (2)](#mok-2025-2)
`q2 i3` Mark-scheme grading raises the Pearson correlation coefficient for every LLM, on average by 0.085, with GPT-4 most consistent at r = 0.8. [→ Mok 2025 (3)](#mok-2025-3)

## Evidence

### Mok 2025

Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli. (2025). Using AI Large Language Models for Grading in Education: A Hands-On Test for Physics. arXiv. Originally published 2024. [doi:10.1088/1361-6552/adb92b](https://doi.org/10.1088/1361-6552/adb92b)

`q2 · i?` · `design · r2`

Regression comparison of blind versus mark-scheme grading across the four LLMs (Figs. 10-14). Gemini and Claude improve but remain fairly lenient; the article reports the shift "closer to the ideal line" for all models.

> "Introducing a mark scheme into the grading approach appears to rectify over-leniency in grading to various extents, causing the best-fit line to shift closer to the ideal line."

### Mok 2025 (2)

Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli. (2025). Using AI Large Language Models for Grading in Education: A Hands-On Test for Physics. arXiv. Originally published 2024. [doi:10.1088/1361-6552/adb92b](https://doi.org/10.1088/1361-6552/adb92b)

`q2 · i3` · `design · r2`

Results-section analysis of GPT-4 mark-scheme grading (Fig. 13: y = (0.92 ± 0.07)x + (7 ± 5), r = 0.80). Harshness cases arose from GPT-4 "sticking to the exact solution given by the mark scheme too rigidly", e.g. awarding only 2/7 marks for equivalent expressions.

> "Thie use of the mark scheme on GPT-4 causes by far the largest shift to the line of best fit, placing it very close to the y = x line. In fact, the use of the mark scheme for GPT-4 shows a new behaviour, with many cases when the LLM is marking harsher than the humans."

### Mok 2025 (3)

Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli. (2025). Using AI Large Language Models for Grading in Education: A Hands-On Test for Physics. arXiv. Originally published 2024. [doi:10.1088/1361-6552/adb92b](https://doi.org/10.1088/1361-6552/adb92b)

`q2 · i3` · `causal · r1`

Grading-consistency analysis using Pearson r across blind and mark-scheme conditions for all four LLMs; the article prints the average r increase of 0.085 and reports GPT-4 with a mark scheme as most consistent at r = 0.8.

> "It can be observed that with the use of the mark scheme, the correlation coefficient increases, and LLM grading becomes slightly more consistent and less distributed. This is not surprising since grading based on a mark scheme is a more systematic approach. On average (per LLM), the increase in r-value is 0.085."

## Discussion


## Related Claims
- [GPT-4's grading accuracy correlates with its problem-solving ability, and a mark scheme removes this dependence](gpt4-solving-grading-correlation.md) — related
- [Blind LLM grading of undergraduate physics solutions is substantially more lenient than human grading, driven by mathematical hallucinations](llm-blind-grading-lenient-hallucinations.md) — related
- [Prompt quality and detailed scoring rubrics significantly influence the accuracy and consistency of LLM-generated grades](prompt-rubric-quality-drives-llm-grading.md) — a broader claim this one bears on
- [Graded Exemplars Shift an LLM Grader by the Level They Are Marked At](graded-exemplars-shift-an-llm-grader-by-the-level-they-are-marked-at.md) — related
- [In one study of five LLMs scoring 60 undergraduate essays on IELTS rubric dimensions, systematic underestimation of human scores was the dominant bias trend, with some models also compressing scores into a narrow range](llm-essay-scoring-systematic-underestimation.md) — related
