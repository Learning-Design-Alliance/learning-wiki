---
type: claim
title: AI-generated scores show weak agreement with instructor grading of physics lab reports (ρ = 0.38, MAE = 1.01), with the AI assigning lower scores on average
description: AI-generated scores show weak agreement with instructor grading of physics lab reports (ρ = 0.38, MAE = 1.01), with the AI assigning lower scores on average
id: ai-batch-grading-weak-agreement-instructor-scores
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: marcos-abreu-2026
    resource: "https://doi.org/10.1088/1361-6552/ae8110"
    title: "Marcos Abreu, Alvaro Suárez, Cecilia Stari, Arturo C. Marti. (2026). Exploring the potential of ChatGPT for feedback and evaluation in experimental physics. [doi:10.1088/1361-6552/ae8110](https://doi.org/10.1088/1361-6552/ae8110)"
    author: Marcos Abreu, Alvaro Suárez, Cecilia Stari, Arturo C. Marti
    q: 2
    i: 3
    kind: design
    rigour: 2
---

# AI-generated scores show weak agreement with instructor grading of physics lab reports (ρ = 0.38, MAE = 1.01), with the AI assigning lower scores on average

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · `i3` large
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i3` The Spearman rank correlation between AI and instructor scores was ρ = 0.38, indicating a weak association in the relative ordering of reports. [→ Marcos Abreu 2026](#marcos-abreu-2026)
`q2 i?` The AI assigned lower scores on average than instructors (7.91 vs. 8.63) with a mean absolute error of 1.01. [→ Marcos Abreu 2026](#marcos-abreu-2026)

## Evidence

### Marcos Abreu 2026

Marcos Abreu, Alvaro Suárez, Cecilia Stari, Arturo C. Marti. (2026). Exploring the potential of ChatGPT for feedback and evaluation in experimental physics. [doi:10.1088/1361-6552/ae8110](https://doi.org/10.1088/1361-6552/ae8110)

`q2 · i3` · `design · r2`

Quantitative comparison in the Results section of AI batch grading versus official instructor grading of 57 randomly sampled reports from 150 submissions, using the same 10-point rubric. The study reports "a weak association between both grading systems" with ρ = 0.38, means of 7.91 (AI) vs. 8.63 (instructors), and MAE = 1.01.

> "The Spearman rank correlation coefficient (ρ= 0.38) indicates a weak association between both grading systems in terms of the relative ordering of reports. On average, the AI assigned lower scores than the instructors (7.91 vs. 8.63)."

## Discussion


## Related Claims
- [Out-of-the-box LLMs agree with human essay grades far less than human raters agree with each other](llm-essay-scoring-weak-human-agreement.md) — related
- [LLM-generated total scores showed moderate agreement with faculty ratings of VSP history-taking performance (ICC(2,1)=0.51)](llm-vsp-scoring-moderate-agreement-faculty.md) — related
- [LLM marking agrees with human markers on only about half of graded Physics answers, and assigns higher, less variable normalized scores than humans](llm-marking-concordance-with-humans-about-half.md) — related
