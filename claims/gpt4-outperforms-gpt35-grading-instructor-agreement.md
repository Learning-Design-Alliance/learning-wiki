---
type: claim
title: GPT-4 generally outperforms GPT-3.5 in matching instructor grades, with lower internal variance
description: GPT-4 generally outperforms GPT-3.5 in matching instructor grades, with lower internal variance
id: gpt4-outperforms-gpt35-grading-instructor-agreement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2024
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

# GPT-4 generally outperforms GPT-3.5 in matching instructor grades, with lower internal variance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` GPT-4 returned answers closer to instructor grades than GPT-3.5 for 3 of 4 prompts in astronomy, 3 of 4 in astrobiology, but only 2 of 4 in history and philosophy. [→ Chris Impey 2024](#chris-impey-2024)
`q2 i?` Bootstrap standard deviations of LLM scores were comparable to or lower than instructor standard deviations more often for GPT-4 than GPT-3.5 in each course. [→ Chris Impey 2024 (2)](#chris-impey-2024-2)

## Evidence

### Chris Impey 2024

Chris Impey, Matthew Wenger, Nikhil Garuda, Shahriar Golchin, Sarah Stamer. (2024). Using Large Language Models for Automated Grading of Student Writing about Science. Preprint. https://doi.org/10.21203/rs.3.rs-3962175/v1

`q2 · i?` · `design · r2`

RMS agreement analysis (Table 3) comparing GPT-4 and GPT-3.5 against instructor grades per prompt; the advantage of GPT-4 was smallest in the history and philosophy course.

> "GPT-4 returns answers closer to instructor grades than GPT-3.5 for 3 out of the 4 prompts for the astronomy class and 3 out of the 4 prompts for the astrobiology class, but only 2 out of the 4 prompts for the history and philosophy class."

### Chris Impey 2024 (2)

Chris Impey, Matthew Wenger, Nikhil Garuda, Shahriar Golchin, Sarah Stamer. (2024). Using Large Language Models for Automated Grading of Student Writing about Science. Preprint. https://doi.org/10.21203/rs.3.rs-3962175/v1

`q2 · i?` · `design · r2`

Bootstrap resampling (10,000 samples) of LLM scores; the article reports 63% vs 75% of astronomy questions meeting the criterion for GPT-3.5 vs GPT-4, and states these differences reflect lower internal variance for GPT-4.

> "Bootstrap resampling of the LLM scores yields standard deviations comparable to or lower than the standard deviations of scores from the instructor. For the astronomy course, across all the four prompts, this is true for 63% (12/19) of the questions using GPT-3.5 and 75% (15/20) of the questions using GPT-4."

## Discussion


## Related Claims
- [LLM grading performance is markedly worse for open-ended history and philosophy questions than for content-based astronomy and astrobiology questions](llm-grading-worse-on-open-ended-questions.md) — related
- [GPT-4 grading agrees best with the instructor when the prompt includes the instructor's model answer with a rubric, and worst with an AI-generated rubric alone](prompt-design-model-answer-plus-rubric-best.md) — related
- [In three astronomy MOOCs, GPT-3.5 and GPT-4 grades are closer to instructor grades with lower dispersion than peer grades](llm-grading-closer-to-instructor-than-peer-grading.md) — a broader claim this one bears on
