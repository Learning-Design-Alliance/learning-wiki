---
type: claim
title: "A student's choice of incorrect answer on a diagnostic question reveals information about the nature of their misconception"
description: "A student's choice of incorrect answer on a diagnostic question reveals information about the nature of their misconception"
id: wrong-answer-choice-reveals-misconception
aliases: [incorrect-answer-choice-reveals-misconception]
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
newest_evidence: 2020
recheck_by: 2023
sources:
  - id: zichao-wang-2020
    resource: "https://doi.org/10.48550/arXiv.2007.12061"
    title: "Zichao Wang, Angus Lamb, Evgeny Saveliev, Pashmina Cameron, Yordan Zaykov, José Miguel Hernández-Lobato, Richard E. Turner, Richard G. Baraniuk, Craig Barton, Simon Peyton Jones, Simon Woodhead, Cheng Zhang. (2020). Instructions and Guide for Diagnostic Questions: The NeurIPS 2020 Education Challenge. [doi:10.48550/arXiv.2007.12061](https://doi.org/10.48550/arXiv.2007.12061)"
    author: Zichao Wang, Angus Lamb, Evgeny Saveliev, Pashmina Cameron, Yordan Zaykov, José Miguel Hernández-Lobato, Richard E. Turner, Richard G. Baraniuk, Craig Barton, Simon Peyton Jones, Simon Woodhead, Cheng Zhang
    q: 1
    i: "?"
    kind: theoretical
    rigour: "?"
  - id: wang-et-al-2020
    resource: "https://arxiv.org/abs/2007.12061"
    title: "Zichao Wang, Angus Lamb, Evgeny Saveliev, Pashmina Cameron, Yordan Zaykov, José Miguel Hernández-Lobato, Richard E. Turner, Richard G. Baraniuk, Craig Barton, Simon Peyton Jones, Simon Woodhead, Cheng Zhang. (2020). Instructions and Guide for Diagnostic Questions: The NeurIPS 2020 Education Challenge. https://arxiv.org/abs/2007.12061"
    author: Zichao Wang, Angus Lamb, Evgeny Saveliev, Pashmina Cameron, Yordan Zaykov, José Miguel Hernández-Lobato, Richard E. Turner, Richard G. Baraniuk, Craig Barton, Simon Peyton Jones, Simon Woodhead, Cheng Zhang
    q: 1
    i: "?"
    kind: theoretical
    rigour: 1
---

# A student's choice of incorrect answer on a diagnostic question reveals information about the nature of their misconception

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · theoretical `r1` · `q1`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims

`q1 i?` If a student answers a diagnostic question incorrectly, the specific incorrect option chosen indicates the nature of the misconception they hold, information educators would otherwise have to guess at. [→ Zichao Wang 2020](#zichao-wang-2020)

`q1 i?` On a well-designed diagnostic question, the specific incorrect answer a student selects discloses valuable information about the nature of their misconception, which helps educators address it. [→ Wang et al. 2020](#wang-et-al-2020)

## Evidence

### Zichao Wang 2020

Zichao Wang, Angus Lamb, Evgeny Saveliev, Pashmina Cameron, Yordan Zaykov, José Miguel Hernández-Lobato, Richard E. Turner, Richard G. Baraniuk, Craig Barton, Simon Peyton Jones, Simon Woodhead, Cheng Zhang. (2020). Instructions and Guide for Diagnostic Questions: The NeurIPS 2020 Education Challenge. [doi:10.48550/arXiv.2007.12061](https://doi.org/10.48550/arXiv.2007.12061)

`q1 · i?` · `theoretical · r?`

Theoretical argument in the article's background section, attributed to prior work on diagnostic questions (citing Wylie and Wiliam). No empirical data are reported for this statement in the article itself; it grounds the competition's answer-prediction task.

> "If a student gets a diagnostic question wrong, educators are not left to guess why. The student's choice of incorrect answer reveals something about the nature of their misconception which is valuable information in seeking to help them resolve it"

### Wang et al. 2020

Zichao Wang, Angus Lamb, Evgeny Saveliev, Pashmina Cameron, Yordan Zaykov, José Miguel Hernández-Lobato, Richard E. Turner, Richard G. Baraniuk, Craig Barton, Simon Peyton Jones, Simon Woodhead, Cheng Zhang. (2020). Instructions and Guide for Diagnostic Questions: The NeurIPS 2020 Education Challenge. https://arxiv.org/abs/2007.12061

`q1 · i?` · `theoretical · r1`

Theoretical argument from the article's background section on formative assessment, citing prior work on diagnostic questions. It asserts that "educators are not left to guess why" because the selected distractor carries diagnostic information about the student's misconception.

> "If a student gets a diagnostic question wrong, educators are not left to guess why. The student's choice of incorrect answer reveals something about the nature of their misconception which is valuable information in seeking to help them resolve it"

## Discussion



## Related Claims

- [LLMs' generation probabilities for multiple-choice distractors correlate moderately with how often students choose them](llm-distractor-likelihood-moderately-tracks-student-choices.md) — related
- [LLM-generated categories of incorrect explanations do not align with the multiple-choice distractors of the original EMCS questions](llm-incorrect-explanation-categories-differ-from-mc-distractors.md) — related
- [TAs often selected answer choices incorporating both correct and incorrect ideas, which frequently misled them away from students' most common alternate conceptions](tas-partially-correct-idea-reasoning-misleads.md) — related
- [EJSS dashboard data can reveal students' specific misconceptions, e.g. confusing an angle with its complement in vector problems](ejss-dashboard-reveals-vector-angle-misconception.md) — related
- [LLMs predict common distractors above chance but fall 15 percentage points below chance at predicting which errors students rarely select](llm-distractor-prediction-asymmetry.md) — related
- [Transition matrix analysis of FCI Question 18 shows post-instruction movement to better incorrect answer choices that dichotomous scoring does not reveal](transition-matrices-richer-than-dichotomous-scoring.md) — related
