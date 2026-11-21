---
type: claim
title: DPO training brings the pedagogical rubric performance of an 8B open-source LLM to the level of GPT-4o while improving over SFT and distillation-only training
description: DPO training brings the pedagogical rubric performance of an 8B open-source LLM to the level of GPT-4o while improving over SFT and distillation-only training
id: dpo-matches-gpt4o-pedagogical-rubric
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

# DPO training brings the pedagogical rubric performance of an 8B open-source LLM to the level of GPT-4o while improving over SFT and distillation-only training

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` DPO achieves similar scores to GPT-4o on the pedagogical rubric, with both scoring very high on all rubric items and the overall score, and improves over distillation on almost all metrics. [→ Alexander Scarlatos 2025](#alexander-scarlatos-2025)

## Evidence

### Alexander Scarlatos 2025

Alexander Scarlatos, Naiming Liu, Jaewook Lee, Richard Baraniuk, Andrew Lan. (2025). Training LLM-based Tutors to Improve Student Learning Outcomes in Dialogues. AIED 2025. [doi:10.1007/978-3-031-98414-3_18](https://doi.org/10.1007/978-3-031-98414-3_18)

`q2 · i?` · `design · r2`

Automated rubric evaluation (GPT-4o as judge) on the MathDial test set shows DPO (overall 9.37) at a level similar to GPT-4o (9.40), both "scoring very high on all rubric items"; the SFT model scores far lower (overall 4.73).

> "Additionally, DPO achieves similar scores to GPT-4o on the pedagogical rubric, with both methods scoring very high on all rubric items and the overall score."

## Discussion


## Related Claims
- [DPO training significantly increases the likelihood of correct next-turn student responses predicted by LLMKT, outperforming prompting, SFT, distillation, GPT-4o and human tutor utterances on the MathDial test set](dpo-tutor-training-raises-predicted-student-correctness.md) — related
- [Supervised fine-tuning does not outperform zero-shot prompting on rubric score for math feedback generation, and ROUGE-L and BERTScore are unreliable estimates of feedback quality.](sft-ineffective-reference-metrics-unreliable.md) — related
- [Fine-tuned 8B LLMs generate K-2 stories with difficulty-related metric scores statistically significantly different from (mostly better than) zero-shot GPT-4o and Llama 3.3 70B](finetuned-8b-llms-beat-zero-shot-large-models-on-difficulty-metrics.md) — related
- [In one essay-feedback system, fine-tuned models produced no usable deep-level feedback output, so only directly prompted LLMs were evaluated; the authors suggest prompting may be more effective than supervised fine-tuning for this task](sft-less-effective-than-prompting-for-feedback-generation.md) — related
- [GRPO with an SFS-aligned reward yields more consistent improvements than DPO, achieving the highest SFS overall](grpo-sfs-reward-beats-dpo.md) — related
- [Supervised fine-tuning on misconception-faithful demonstrations sharply improves SFS (up to +0.555 on Malrule for Qwen3-4B)](sft-improves-selective-update-behavior.md) — related
- [In a human evaluation, the DPO-trained tutor outperforms both human tutors and GPT-4o on perceived student correctness and rubric score, with statistically significant differences](human-evaluation-dpo-beats-human-tutors-and-gpt4o.md) — possibly the same claim (merge candidate)
- [Fine-tuning on interaction traces narrows an 8B model's gap to GPT-5 on interactive response quality except correctness](refine-finetuning-narrows-gap-to-gpt5.md) — related
