---
type: claim
title: DPO training significantly increases the likelihood of correct next-turn student responses predicted by LLMKT, outperforming prompting, SFT, distillation, GPT-4o and human tutor utterances on the MathDial test set
description: DPO training significantly increases the likelihood of correct next-turn student responses predicted by LLMKT, outperforming prompting, SFT, distillation, GPT-4o and human tutor utterances on the MathDial test set
id: dpo-tutor-training-raises-predicted-student-correctness
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: alexander-scarlatos-2025
    resource: "https://doi.org/10.1007/978-3-031-98414-3_18"
    title: "Alexander Scarlatos, Naiming Liu, Jaewook Lee, Richard Baraniuk, Andrew Lan. (2025). Training LLM-based Tutors to Improve Student Learning Outcomes in Dialogues. AIED 2025. [doi:10.1007/978-3-031-98414-3_18](https://doi.org/10.1007/978-3-031-98414-3_18)"
    author: Alexander Scarlatos, Naiming Liu, Jaewook Lee, Richard Baraniuk, Andrew Lan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# DPO training significantly increases the likelihood of correct next-turn student responses predicted by LLMKT, outperforming prompting, SFT, distillation, GPT-4o and human tutor utterances on the MathDial test set

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` DPO-trained Llama 3.1 8B significantly outperforms all other methods on student correctness prediction, improving over the next best method, GPT-4o, by 33%. [→ Alexander Scarlatos 2025](#alexander-scarlatos-2025)

## Evidence

### Alexander Scarlatos 2025

Alexander Scarlatos, Naiming Liu, Jaewook Lee, Richard Baraniuk, Andrew Lan. (2025). Training LLM-based Tutors to Improve Student Learning Outcomes in Dialogues. AIED 2025. [doi:10.1007/978-3-031-98414-3_18](https://doi.org/10.1007/978-3-031-98414-3_18)

`q2 · i?` · `design · r2`

Automated evaluation on the MathDial test set (588 dialogues, 3,101 tutor turns) comparing DPO, prompted baselines, SFT, Distill, GPT-4o and human tutor utterances, with correctness scored by LLMKT. The study reports a "33%" improvement over GPT-4o; Table 2 shows DPO at 0.65 accuracy versus 0.49 for GPT-4o.

> "We observe that DPO significantly outperforms all other methods on student correctness prediction, improving over the next best method, GPT-4o, by 33%."

## Discussion


## Related Claims
- [DPO training brings the pedagogical rubric performance of an 8B open-source LLM to the level of GPT-4o while improving over SFT and distillation-only training](dpo-matches-gpt4o-pedagogical-rubric.md) — related
- [Qualitative analysis finds the DPO-trained tutor's primary route to higher predicted correctness is posing concrete, feasible subtasks, an emergent behavior of training on LLMKT-derived scores](emergent-feasible-task-posing-dpo-tutor.md) — related
- [In a human evaluation, the DPO-trained tutor outperforms both human tutors and GPT-4o on perceived student correctness and rubric score, with statistically significant differences](human-evaluation-dpo-beats-human-tutors-and-gpt4o.md) — related
- [Knowledge tracing performance on tutoring dialogues is relatively low, with a maximum of around 76% AUC, which the authors take to show dialogueKT is a challenging task.](dialogue-kt-performance-is-relatively-low-compared-to-standard-kt.md) — related
- [Human annotators agree poorly on which tutor utterance will elicit correct student responses (Kendall's τ = 0.06), while agreement on pedagogical rubric scoring is higher](low-inter-rater-agreement-predicting-student-correctness.md) — related
- [LLMKT outperforms existing knowledge tracing methods at predicting student turn correctness in the CoMTA and MathDial tutoring dialogue datasets, and generally outperforms DKT-Sem.](llmkt-outperforms-existing-kt-methods-on-tutoring-dialogues.md) — related
- [ParLD-guided tutoring instructions raise simulated students' correct-answer rate to 72.22% versus 56.48% for Direct Respond on MathDial](parld-tutoring-simulation-higher-correct-rate.md) — related
