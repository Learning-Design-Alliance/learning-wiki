---
type: claim
title: On the HoCMaze-18 reference task, fine-tuned GPT-3.5 shows no significant difference from human tutors in student attempt synthesis
description: On the HoCMaze-18 reference task, fine-tuned GPT-3.5 shows no significant difference from human tutors in student attempt synthesis
id: gpt35-ft-ss-approaches-tutorss-hocmaze18
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: manh-hung-nguyen-2023
    resource: "https://doi.org/10.48550/arXiv.2310.10690"
    title: "Manh Hung Nguyen, Sebastian Tschiatschek, Adish Singla. (2023). Large Language Models for In-Context Student Modeling: Synthesizing Student's Behavior in Visual Programming. Preprint, Accepted at the EDM'24 conference. [doi:10.48550/arXiv.2310.10690](https://doi.org/10.48550/arXiv.2310.10690)"
    author: Manh Hung Nguyen, Sebastian Tschiatschek, Adish Singla
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: manh-hung-nguyen-2023-2
    resource: "https://doi.org/10.48550/arXiv.2310.10690"
    title: "Manh Hung Nguyen, Sebastian Tschiatschek, Adish Singla. (2023). Large Language Models for In-Context Student Modeling: Synthesizing Student's Behavior in Visual Programming. Preprint, Accepted at the EDM'24 conference. [doi:10.48550/arXiv.2310.10690](https://doi.org/10.48550/arXiv.2310.10690)"
    author: Manh Hung Nguyen, Sebastian Tschiatschek, Adish Singla
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# On the HoCMaze-18 reference task, fine-tuned GPT-3.5 shows no significant difference from human tutors in student attempt synthesis

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q1`–`q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For HoCMaze-18, there is no significant difference between GPT-3.5ft-SS and human tutors (TUTORSS); equivalence was not tested beyond this comparison. [→ Manh Hung Nguyen 2023](#manh-hung-nguyen-2023)

## Evidence

### Manh Hung Nguyen 2023

Manh Hung Nguyen, Sebastian Tschiatschek, Adish Singla. (2023). Large Language Models for In-Context Student Modeling: Synthesizing Student's Behavior in Visual Programming. Preprint, Accepted at the EDM'24 conference. [doi:10.48550/arXiv.2310.10690](https://doi.org/10.48550/arXiv.2310.10690)

`q2 · i?` · `design · r2`

STUDENTSYN benchmark results comparing fine-tuned GPT-3.5 with the human-tutor oracle TUTORSS on HoCMaze-18 (Q-OVERALL 0.82 vs 0.85); the article reports "no significant difference" (p >0.05).

> "Remarkably, for HoCMaze-18, there is no significant difference between the performances of GPT-3.5ft-SS and human tutors in TUTOR SS (p >0.05)."

### Manh Hung Nguyen 2023 (2)

Manh Hung Nguyen, Sebastian Tschiatschek, Adish Singla. (2023). Large Language Models for In-Context Student Modeling: Synthesizing Student's Behavior in Visual Programming. Preprint, Accepted at the EDM'24 conference. [doi:10.48550/arXiv.2310.10690](https://doi.org/10.48550/arXiv.2310.10690)

`q1 · i?` · `design · r2`

Qualitative example analysis of one HoCMaze-18 scenario where the student's misconception is ignoring conditionals; GPT-3.5ft-SS reproduces the misconception while adapting to the target task, scored "Q-OVERALL = 1", close to the human tutor's code.

> "Student code synthesized by GPT-3.5ft-SS has the same misconception observed in C STUT ref , while adapting to T tar (Q-OVERALL = 1)."

## Discussion


## Related Claims
- [Fine-tuning an LLM on expert (task, solution) data significantly improves its student synthesis performance, including capturing the student's behavior](finetuning-improves-llm-ss-student-synthesis.md) — a broader claim this one bears on
- [Fine-tuning frontier LLMs on authentic tutoring data improves performance on all six conversational and pedagogical benchmarks, moving values toward human-tutor levels](fine-tuning-authentic-data-improves-pedagogical-benchmarks.md) — a broader claim this one bears on
- [A fine-tuned student model paired with GPT-4 produces conversational statistics closer to human-AI dialogues than two prompt-engineered base models](fine-tuned-student-model-approximates-human-ai-dialogue.md) — related
- [GPT-4-SS performs significantly better than the NEURSS baseline on Q-OVERALL in both reference tasks without fine-tuning or extensive training data](gpt4-ss-outperforms-neurss-qoverall.md) — related
