---
type: claim
title: GPT-4-SS performs significantly better than the NEURSS baseline on Q-OVERALL in both reference tasks without fine-tuning or extensive training data
description: GPT-4-SS performs significantly better than the NEURSS baseline on Q-OVERALL in both reference tasks without fine-tuning or extensive training data
id: gpt4-ss-outperforms-neurss-qoverall
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
source_checked: 2026-11-20
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
---

# GPT-4-SS performs significantly better than the NEURSS baseline on Q-OVERALL in both reference tasks without fine-tuning or extensive training data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · checked against its sources 2026-11-20 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Among base LLM methods without fine-tuning, GPT-4-SS achieved the highest scores across both reference tasks and significantly outperformed the NEURSS baseline on Q-OVERALL. [→ Manh Hung Nguyen 2023](#manh-hung-nguyen-2023)

## Evidence

### Manh Hung Nguyen 2023

Manh Hung Nguyen, Sebastian Tschiatschek, Adish Singla. (2023). Large Language Models for In-Context Student Modeling: Synthesizing Student's Behavior in Visual Programming. Preprint, Accepted at the EDM'24 conference. [doi:10.48550/arXiv.2310.10690](https://doi.org/10.48550/arXiv.2310.10690)

`q2 · i?` · `design · r2`

Benchmark evaluation on STUDENTSYN with 36 scenarios, blind expert annotation of synthesized attempts; the χ2 test on aggregated data across both reference tasks shows GPT-4-SS "performs signif- icantly better than the NEUR SS baseline" on Q-OVERALL (p ≤ 0.05).

> "Additionally, GPT-4-SS performs signif- icantly better than the NEUR SS baseline w.r.t. Q-OVERALL in both reference tasks (p ≤ 0.05), based on the χ2 test [42]."

## Discussion


## Related Claims
- [Fine-tuning an LLM on expert (task, solution) data significantly improves its student synthesis performance, including capturing the student's behavior](finetuning-improves-llm-ss-student-synthesis.md) — related
- [On the HoCMaze-18 reference task, fine-tuned GPT-3.5 shows no significant difference from human tutors in student attempt synthesis](gpt35-ft-ss-approaches-tutorss-hocmaze18.md) — related
- [The NEURSS baseline overfits the observed reference attempt and fails to reflect the target task layout in some scenarios](neurss-overfits-reference-attempt.md) — related
