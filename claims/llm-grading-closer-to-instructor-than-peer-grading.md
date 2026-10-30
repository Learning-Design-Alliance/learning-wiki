---
type: claim
title: In three astronomy MOOCs, GPT-3.5 and GPT-4 grades are closer to instructor grades with lower dispersion than peer grades
description: In three astronomy MOOCs, GPT-3.5 and GPT-4 grades are closer to instructor grades with lower dispersion than peer grades
id: llm-grading-closer-to-instructor-than-peer-grading
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: chris-impey-2024
    resource: "https://doi.org/10.21203/rs.3.rs-3962175/v1"
    title: "Chris Impey, Matthew Wenger, Nikhil Garuda, Shahriar Golchin, Sarah Stamer. (2024). Using Large Language Models for Automated Grading of Student Writing about Science. Preprint. https://doi.org/10.21203/rs.3.rs-3962175/v1"
    author: Chris Impey, Matthew Wenger, Nikhil Garuda, Shahriar Golchin, Sarah Stamer
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: chris-impey-2024-2
    resource: "https://doi.org/10.21203/rs.3.rs-3962175/v1"
    title: "Chris Impey, Matthew Wenger, Nikhil Garuda, Shahriar Golchin, Sarah Stamer. (2024). Using Large Language Models for Automated Grading of Student Writing about Science. Preprint. https://doi.org/10.21203/rs.3.rs-3962175/v1"
    author: Chris Impey, Matthew Wenger, Nikhil Garuda, Shahriar Golchin, Sarah Stamer
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# In three astronomy MOOCs, GPT-3.5 and GPT-4 grades are closer to instructor grades with lower dispersion than peer grades

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across three MOOC courses, both LLMs produced grades closer to instructor grades and with lower dispersion than peer grades. [→ Chris Impey 2024](#chris-impey-2024)
`q2 i?` Normalized-score scatter between instructor and GPT-4 was smaller than between instructor and peer graders in all three courses (15% vs 27%, 17% vs 22%, 26% vs 38%). [→ Chris Impey 2024 (2)](#chris-impey-2024-2)

## Evidence

### Chris Impey 2024

Chris Impey, Matthew Wenger, Nikhil Garuda, Shahriar Golchin, Sarah Stamer. (2024). Using Large Language Models for Automated Grading of Student Writing about Science. Preprint. https://doi.org/10.21203/rs.3.rs-3962175/v1

`q2 · i?` · `causal · r1`

Three-way comparison of instructor, peer, and LLM grades across the astronomy, astrobiology, and history and philosophy MOOCs; the article reports both LLMs "closer to the instructor grades and have lower dispersion than peer grades" in all three courses.

> "Summarizing the three-way comparison between instructor grades, peer review grades, and the grades assigned by the LLMs, both GPT-3.5 and GPT-4 generally produce grades that are closer to the instructor grades and have lower dispersion than peer grades. This is true for all three courses."

### Chris Impey 2024 (2)

Chris Impey, Matthew Wenger, Nikhil Garuda, Shahriar Golchin, Sarah Stamer. (2024). Using Large Language Models for Automated Grading of Student Writing about Science. Preprint. https://doi.org/10.21203/rs.3.rs-3962175/v1

`q2 · i?` · `design · r2`

Normalized-score comparison reported in the results section: instructor-to-GPT-4 scatter of 15% vs instructor-to-peer 27% (astronomy) and 17% vs 22% (astrobiology); the history and philosophy course showed 26% vs 38%.

> "For the introductory course, the mean scatter in normalized scores is 15% between the instructor and GPT-4, as opposed to 27% between the instructor and peer graders. For the astrobiology course, the mean scatter in normalized scores is 17% between instructor and GPT-4, as opposed to 22% between instructor and peer graders."

## Discussion


## Related Claims
- [For individual students, GPT-4 grades match instructor grades more closely than peer grades do, with smaller dispersion](gpt4-individual-student-grading-beats-peer-grading.md) — a narrower finding that bears on this claim
- [Peer graders in these MOOCs score more leniently and with greater dispersion than the instructor](peer-grading-lenient-high-dispersion-moocs.md) — related
- [GPT-4 generally outperforms GPT-3.5 in matching instructor grades, with lower internal variance](gpt4-outperforms-gpt35-grading-instructor-agreement.md) — a narrower finding that bears on this claim
- [LLM grading performance is markedly worse for open-ended history and philosophy questions than for content-based astronomy and astrobiology questions](llm-grading-worse-on-open-ended-questions.md) — related
