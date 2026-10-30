---
type: claim
title: LLM grading performance is markedly worse for open-ended history and philosophy questions than for content-based astronomy and astrobiology questions
description: LLM grading performance is markedly worse for open-ended history and philosophy questions than for content-based astronomy and astrobiology questions
id: llm-grading-worse-on-open-ended-questions
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
    kind: design
    rigour: 2
  - id: chris-impey-2024-2
    resource: "https://doi.org/10.21203/rs.3.rs-3962175/v1"
    title: "Chris Impey, Matthew Wenger, Nikhil Garuda, Shahriar Golchin, Sarah Stamer. (2024). Using Large Language Models for Automated Grading of Student Writing about Science. Preprint. https://doi.org/10.21203/rs.3.rs-3962175/v1"
    author: Chris Impey, Matthew Wenger, Nikhil Garuda, Shahriar Golchin, Sarah Stamer
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM grading performance is markedly worse for open-ended history and philosophy questions than for content-based astronomy and astrobiology questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` LLM performance was excellent for the astronomy and astrobiology courses but markedly worse in the history and philosophy class, where questions are more open-ended and rubric creation is difficult even for instructors. [→ Chris Impey 2024](#chris-impey-2024)
`q2 i?` On some history and philosophy questions, LLM agreement with the instructor was poor, with several prompts several standard deviations from instructor scores. [→ Chris Impey 2024 (2)](#chris-impey-2024-2)

## Evidence

### Chris Impey 2024

Chris Impey, Matthew Wenger, Nikhil Garuda, Shahriar Golchin, Sarah Stamer. (2024). Using Large Language Models for Automated Grading of Student Writing about Science. Preprint. https://doi.org/10.21203/rs.3.rs-3962175/v1

`q2 · i?` · `design · r2`

Authors' discussion of the course-level pattern in the grading results; the history and philosophy course involves speculation and hypothetical situations where judgment can be subjective.

> "Performance of the LLMs is excellent for the astronomy and astrobiology courses, and markedly worse in the history and philosophy class, where questions are more open-ended, and it is challenging even for an instructor to create a concrete rubric."

### Chris Impey 2024 (2)

Chris Impey, Matthew Wenger, Nikhil Garuda, Shahriar Golchin, Sarah Stamer. (2024). Using Large Language Models for Automated Grading of Student Writing about Science. Preprint. https://doi.org/10.21203/rs.3.rs-3962175/v1

`q2 · i?` · `design · r2`

Course-specific results for the history and philosophy MOOC (Table 1/Table 2); instructor scores were also lower as a percentage than in the other two courses.

> "On the third question, the agreement is poor, with three of the prompts several standard deviations away from instructor scores. On the fourth question, the agreement is again poor, with the best result obtained using the instructor model answer along with an AI-generated rubric."

## Discussion


## Related Claims
- [ASAG and AEG systems differ on answer length, grading focus, and question openness](asag-content-focus-versus-aeg-style.md) — related
- [GPT-4 generally outperforms GPT-3.5 in matching instructor grades, with lower internal variance](gpt4-outperforms-gpt35-grading-instructor-agreement.md) — related
- [In three astronomy MOOCs, GPT-3.5 and GPT-4 grades are closer to instructor grades with lower dispersion than peer grades](llm-grading-closer-to-instructor-than-peer-grading.md) — related
- [LLMs perform worse on complex, open-ended, or subjective assignments than on short, clearly formulated answers](llm-struggle-open-ended-subjective-tasks.md) — a broader claim this one bears on
- [Peer graders in these MOOCs score more leniently and with greater dispersion than the instructor](peer-grading-lenient-high-dispersion-moocs.md) — related
- [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](llm-grading-mixed-against-human-raters.md) — related
