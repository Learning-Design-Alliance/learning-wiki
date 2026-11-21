---
type: claim
title: "Qualitative analysis finds the DPO-trained tutor's primary route to higher predicted correctness is posing concrete, feasible subtasks, an emergent behavior of training on LLMKT-derived scores"
description: "Qualitative analysis finds the DPO-trained tutor's primary route to higher predicted correctness is posing concrete, feasible subtasks, an emergent behavior of training on LLMKT-derived scores"
id: emergent-feasible-task-posing-dpo-tutor
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: alexander-scarlatos-2025
    resource: "https://doi.org/10.1007/978-3-031-98414-3_18"
    title: "Alexander Scarlatos, Naiming Liu, Jaewook Lee, Richard Baraniuk, Andrew Lan. (2025). Training LLM-based Tutors to Improve Student Learning Outcomes in Dialogues. AIED 2025. [doi:10.1007/978-3-031-98414-3_18](https://doi.org/10.1007/978-3-031-98414-3_18)"
    author: Alexander Scarlatos, Naiming Liu, Jaewook Lee, Richard Baraniuk, Andrew Lan
    q: 1
    i: "?"
    kind: design
    rigour: 2
  - id: alexander-scarlatos-2025-2
    resource: "https://doi.org/10.1007/978-3-031-98414-3_18"
    title: "Alexander Scarlatos, Naiming Liu, Jaewook Lee, Richard Baraniuk, Andrew Lan. (2025). Training LLM-based Tutors to Improve Student Learning Outcomes in Dialogues. AIED 2025. [doi:10.1007/978-3-031-98414-3_18](https://doi.org/10.1007/978-3-031-98414-3_18)"
    author: Alexander Scarlatos, Naiming Liu, Jaewook Lee, Richard Baraniuk, Andrew Lan
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Qualitative analysis finds the DPO-trained tutor's primary route to higher predicted correctness is posing concrete, feasible subtasks, an emergent behavior of training on LLMKT-derived scores

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The DPO-trained model excels at posing concrete tasks that are nontrivial but more feasible for students compared to GPT-4o, and this behavior appears to be an emergent result of training on LLMKT-derived scores. [→ Alexander Scarlatos 2025](#alexander-scarlatos-2025)
`q2 i?` Both LLMs show limitations when students give partially correct responses, sometimes ignoring student progress and focusing on irrelevant errors. [→ Alexander Scarlatos 2025 (2)](#alexander-scarlatos-2025-2)

## Evidence

### Alexander Scarlatos 2025

Alexander Scarlatos, Naiming Liu, Jaewook Lee, Richard Baraniuk, Andrew Lan. (2025). Training LLM-based Tutors to Improve Student Learning Outcomes in Dialogues. AIED 2025. [doi:10.1007/978-3-031-98414-3_18](https://doi.org/10.1007/978-3-031-98414-3_18)

`q1 · i?` · `design · r2`

Qualitative analysis of generated tutor utterances, including a worked example dialogue (Table 3), showing the DPO model asks manageable subtasks and is more likely to ask questions rather than directly instructing.

> "Overall, we find that our DPO-trained model excels at posing concrete tasks that are nontrivial, but more feasible for students compared to GPT-4o."

### Alexander Scarlatos 2025 (2)

Alexander Scarlatos, Naiming Liu, Jaewook Lee, Richard Baraniuk, Andrew Lan. (2025). Training LLM-based Tutors to Improve Student Learning Outcomes in Dialogues. AIED 2025. [doi:10.1007/978-3-031-98414-3_18](https://doi.org/10.1007/978-3-031-98414-3_18)

`q1 · i?` · `design · r2`

The qualitative analysis reports that when students give partially correct responses the models may ignore progress and focus on irrelevant errors; the authors note correctly identifying errors in math with LLMs is challenging per prior work.

> "However, both LLMs still have some limitations, particularly when students give partially correct responses."

## Discussion


## Related Claims
- [DPO training significantly increases the likelihood of correct next-turn student responses predicted by LLMKT, outperforming prompting, SFT, distillation, GPT-4o and human tutor utterances on the MathDial test set](dpo-tutor-training-raises-predicted-student-correctness.md) — related
- [In a human evaluation, the DPO-trained tutor outperforms both human tutors and GPT-4o on perceived student correctness and rubric score, with statistically significant differences](human-evaluation-dpo-beats-human-tutors-and-gpt4o.md) — related
