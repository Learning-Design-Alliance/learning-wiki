---
type: claim
title: A GPT-4 few-shot binary classifier effectively identifies correct/incorrect trainee responses across three tutor-training lessons, with average F1 of 0.84 and AUC of 0.85
description: A GPT-4 few-shot binary classifier effectively identifies correct/incorrect trainee responses across three tutor-training lessons, with average F1 of 0.84 and AUC of 0.85
id: gpt4-few-shot-classifies-trainee-responses
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: jionghao-lin-2024
    resource: "https://arxiv.org/abs/2405.00970"
    title: "Jionghao Lin, Zifei Han, Danielle R. Thomas, Ashish Gurung, Shivang Gupta, Vincent Aleven, Kenneth R. Koedinger. (2024). How Can I Get It Right? Using GPT to Rephrase Incorrect Trainee Responses. arXiv preprint. https://arxiv.org/abs/2405.00970"
    author: Jionghao Lin, Zifei Han, Danielle R. Thomas, Ashish Gurung, Shivang Gupta, Vincent Aleven, Kenneth R. Koedinger
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A GPT-4 few-shot binary classifier effectively identifies correct/incorrect trainee responses across three tutor-training lessons, with average F1 of 0.84 and AUC of 0.85

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Using a few-shot approach, GPT-4 effectively identifies correct/incorrect trainees' responses from three training lessons with an average F1 score of 0.84 and an AUC score of 0.85. [→ Jionghao Lin 2024](#jionghao-lin-2024)

## Evidence

### Jionghao Lin 2024

Jionghao Lin, Zifei Han, Danielle R. Thomas, Ashish Gurung, Shivang Gupta, Vincent Aleven, Kenneth R. Koedinger. (2024). How Can I Get It Right? Using GPT to Rephrase Incorrect Trainee Responses. arXiv preprint. https://arxiv.org/abs/2405.00970

`q2 · i?` · `design · r2`

Evaluation of zero-shot and two-way few-shot GPT-4 classifiers on 383 analyzed trainee responses from three scenario-based lessons, using F1, AUC, NPV and TNR. The abstract reports the "average F1 score of 0.84" and "AUC score of 0.85" for the few-shot approach.

> "using a few-shot approach, the GPT-4 model effectively identifies correct/incorrect trainees' responses from three training lessons with an average F1 score of 0.84 and an AUC score of 0.85"

## Discussion


## Related Claims
- [Classification was weakest for the Determining What Students Know lesson, where zero-shot learning scored F1 0.66 and AUC 0.668](classification-weakest-determining-students-know.md) — a narrower finding that bears on this claim
- [Few-shot learning with increasing shots generally improves GPT-4 classification performance, with the 5-shot variant strongest for Reacting to Errors (F1 0.867, AUC 0.866, TNR 0.83)](few-shot-shots-improve-classification.md) — a narrower finding that bears on this claim
- [GPT-4o's final-turn correctness labeling on CoMTA is only slightly less accurate than expert human annotators, which the authors read as close to human-level performance on a challenging task.](gpt-4o-final-turn-correctness-labeling-is-close-to-human-level.md) — related
- [LLMs prompted with diverse strategies can analyze educational survey feedback and generate corrective tutor feedback at or above expert human performance in specific scenarios](llm-prompting-human-level-educational-feedback.md) — related
