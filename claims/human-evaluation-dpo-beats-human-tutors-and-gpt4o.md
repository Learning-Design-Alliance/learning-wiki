---
type: claim
title: In a human evaluation, the DPO-trained tutor outperforms both human tutors and GPT-4o on perceived student correctness and rubric score, with statistically significant differences
description: In a human evaluation, the DPO-trained tutor outperforms both human tutors and GPT-4o on perceived student correctness and rubric score, with statistically significant differences
id: human-evaluation-dpo-beats-human-tutors-and-gpt4o
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
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

# In a human evaluation, the DPO-trained tutor outperforms both human tutors and GPT-4o on perceived student correctness and rubric score, with statistically significant differences

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` DPO outperforms both human tutors and GPT-4o on both metrics, with all differences statistically significant (p < 0.05) according to a paired t-test. [→ Alexander Scarlatos 2025](#alexander-scarlatos-2025)

## Evidence

### Alexander Scarlatos 2025

Alexander Scarlatos, Naiming Liu, Jaewook Lee, Richard Baraniuk, Andrew Lan. (2025). Training LLM-based Tutors to Improve Student Learning Outcomes in Dialogues. AIED 2025. [doi:10.1007/978-3-031-98414-3_18](https://doi.org/10.1007/978-3-031-98414-3_18)

`q2 · i?` · `design · r2`

Human evaluation with two independent volunteer university students ranking 50 evaluation instances (10 dialogues, 5 tutor turns each) among human, GPT-4o and DPO utterances. DPO achieved a correctness rank of 1.75 versus 2.12 (Human) and 2.13 (GPT-4o), and a rubric score of 8.55.

> "We see that DPO outperforms both human tutors and GPT-4o on both metrics, with all differences statistically significant (p <0.05) according to a paired t-test."

## Discussion


## Related Claims
- [DPO training brings the pedagogical rubric performance of an 8B open-source LLM to the level of GPT-4o while improving over SFT and distillation-only training](dpo-matches-gpt4o-pedagogical-rubric.md) — possibly the same claim (merge candidate)
- [DPO training significantly increases the likelihood of correct next-turn student responses predicted by LLMKT, outperforming prompting, SFT, distillation, GPT-4o and human tutor utterances on the MathDial test set](dpo-tutor-training-raises-predicted-student-correctness.md) — related
- [Human annotators agree poorly on which tutor utterance will elicit correct student responses (Kendall's τ = 0.06), while agreement on pedagogical rubric scoring is higher](low-inter-rater-agreement-predicting-student-correctness.md) — related
- [Qualitative analysis finds the DPO-trained tutor's primary route to higher predicted correctness is posing concrete, feasible subtasks, an emergent behavior of training on LLMKT-derived scores](emergent-feasible-task-posing-dpo-tutor.md) — related
- [DPO training on GPT-4 rubric annotations with mismatched feedback significantly improves the correctness and alignment of Llama 2-generated math feedback compared to zero-shot and SFT baselines.](dpo-score-mismatch-improves-math-feedback.md) — related
- [Insight's instructor-verified feedback showed higher selectivity and pedagogical suitability than GPT-4o-generated feedback, while GPT-4o showed higher completeness](insight-feedback-beats-gpt4o-selectivity-suitability.md) — related
