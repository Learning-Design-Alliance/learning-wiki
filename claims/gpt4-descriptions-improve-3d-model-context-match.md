---
type: claim
title: GPT-4 context descriptions improve story-matched 3D model generation quality from 3.2 to 4.6 out of 5
description: GPT-4 context descriptions improve story-matched 3D model generation quality from 3.2 to 4.6 out of 5
id: gpt4-descriptions-improve-3d-model-context-match
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: wang-yibo-2024
    resource: "https://doi.org/10.48550/arXiv.2405.13701"
    title: "WANG Yibo, MAO Yuanyuan, Lik-Hang Lee, NI Shi-ting, WANG Zeyu, GU Xiaole, HUI Pan. (2024). Metabook: A Mobile-to-Headset Pipeline for 3D Story Book Creation in Augmented Reality. [doi:10.48550/arXiv.2405.13701](https://doi.org/10.48550/arXiv.2405.13701)"
    author: WANG Yibo, MAO Yuanyuan, Lik-Hang Lee, NI Shi-ting, WANG Zeyu, GU Xiaole, HUI Pan
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# GPT-4 context descriptions improve story-matched 3D model generation quality from 3.2 to 4.6 out of 5

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Models generated with GPT-4 descriptions scored 4.6/5 versus 3.2/5 baseline for story matchness. [→ WANG Yibo 2024](#wang-yibo-2024)

## Evidence

### WANG Yibo 2024

WANG Yibo, MAO Yuanyuan, Lik-Hang Lee, NI Shi-ting, WANG Zeyu, GU Xiaole, HUI Pan. (2024). Metabook: A Mobile-to-Headset Pipeline for 3D Story Book Creation in Augmented Reality. [doi:10.48550/arXiv.2405.13701](https://doi.org/10.48550/arXiv.2405.13701)

`q2 · i?` · `causal · r1`

Workshop comparative experiment using 25 example items; I6 generated models via TripoAI with or without GPT-4 descriptions, and I1–I5 rated matchness on a 5-point scale. Descriptive means only; no inferential test is printed.

> "In the baseline and experimental groups, the generated models received scores of 3.2 out of 5 and 4.6 out of 5, respectively."

## Discussion


## Related Claims
- [The IRead question generation model, fine-tuned on in-text OpenStax questions, matched reference questions in human ratings and outperformed zero-shot GPT-4 on automatic metrics](iread-qg-model-evaluation-performance.md) — related
- [Chain-of-thought and reasoning prompting significantly improve LLM proportional match with human-authored distractors over direct prompting on both math and science MCQs](reasoning-prompting-improves-llm-distractor-match.md) — related
- [GPT-4 (CoT) prompting achieves the highest recall but the lowest F1 score among GPT baselines because most of its generated questions do not match ground truth](gpt4-cot-highest-recall-lowest-f1.md) — related
- [GPT-3-generated cues matched hand-crafted cues in offensiveness, contextual relevance, semantic relatedness, and divergence level](gpt3-cue-quality-comparable.md) — related
