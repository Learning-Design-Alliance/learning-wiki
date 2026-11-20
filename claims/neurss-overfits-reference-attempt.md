---
type: claim
title: The NEURSS baseline overfits the observed reference attempt and fails to reflect the target task layout in some scenarios
description: The NEURSS baseline overfits the observed reference attempt and fails to reflect the target task layout in some scenarios
id: neurss-overfits-reference-attempt
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
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# The NEURSS baseline overfits the observed reference attempt and fails to reflect the target task layout in some scenarios

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q1 i?` In the investigated example scenario, NEURSS synthesized code that overfits the reference attempt and uses turnLeft blocks instead of turnRight blocks, scoring Q-OVERALL = 0. [→ Manh Hung Nguyen 2023](#manh-hung-nguyen-2023)

## Evidence

### Manh Hung Nguyen 2023

Manh Hung Nguyen, Sebastian Tschiatschek, Adish Singla. (2023). Large Language Models for In-Context Student Modeling: Synthesizing Student's Behavior in Visual Programming. Preprint, Accepted at the EDM'24 conference. [doi:10.48550/arXiv.2310.10690](https://doi.org/10.48550/arXiv.2310.10690)

`q1 · i?` · `design · r2`

Case analysis of the Figure 6 example scenario (student misconception: ignoring conditionals): NEURSS "failing to reflect the layout of T tar" and scoring Q-OVERALL = 0, while Llama2-70Bft-SS partially reflected the task (0.5).

> "the NEUR SS baseline synthesized a code that overfits C STUT ref , failing to reflect the layout of T tar as it uses turnLeft blocks instead of turnRight blocks (Q- OVERALL = 0)"

## Discussion


## Related Claims
- [GPT-4-SS performs significantly better than the NEURSS baseline on Q-OVERALL in both reference tasks without fine-tuning or extensive training data](gpt4-ss-outperforms-neurss-qoverall.md) — related
- [Fine-tuning an LLM on expert (task, solution) data significantly improves its student synthesis performance, including capturing the student's behavior](finetuning-improves-llm-ss-student-synthesis.md) — related
