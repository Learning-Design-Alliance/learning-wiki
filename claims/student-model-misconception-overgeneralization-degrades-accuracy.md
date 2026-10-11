---
type: claim
title: Instruction-tuning a student model on a single misconception overgeneralizes the error across problems and degrades correct-solving accuracy
description: Instruction-tuning a student model on a single misconception overgeneralizes the error across problems and degrades correct-solving accuracy
id: student-model-misconception-overgeneralization-degrades-accuracy
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: naiming-liu-2026
    resource: "https://arxiv.org/abs/2604.00818"
    title: "Naiming Liu, Xinghe Chen, Richard Baraniuk, Mrinmaya Sachan, and Shashank Sonkar. (2026). Misconception Acquisition Dynamics in Large Language Models. https://arxiv.org/abs/2604.00818"
    author: Naiming Liu, Xinghe Chen, Richard Baraniuk, Mrinmaya Sachan, and Shashank Sonkar
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Instruction-tuning a student model on a single misconception overgeneralizes the error across problems and degrades correct-solving accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Naive single-misconception training causes LLMs to overgeneralize erroneous reasoning to problem types where the misconception should not apply, degrading correct solving. [→ Naiming Liu 2026](#naiming-liu-2026)

## Evidence

### Naiming Liu 2026

Naiming Liu, Xinghe Chen, Richard Baraniuk, Mrinmaya Sachan, and Shashank Sonkar. (2026). Misconception Acquisition Dynamics in Large Language Models. https://arxiv.org/abs/2604.00818

`q2 · i?` · `causal · r2`

Instruction-tuning experiments across Llama-3.1-8B-Instruct, Phi-4-4B-Mini, and Qwen-3-4B-Instruct on single misconceptions showed that as Misconception Accuracy rose, Overall Correct Accuracy and CANA declined; the article reports "a dramatic decline in OCA andCANA" with no effect size printed.

> "Instead, naive training causes models to overgeneralize erroneous reasoning patterns, degrading their ability to solve even problems where the misconception should not apply."

## Discussion


## Related Claims
- [Mixing correct examples into student-model training resolves the misconception-accuracy trade-off, with correct examples as low as 25% preserving both properties](mixing-correct-examples-resolves-student-model-tradeoff.md) — related
- [LLM error simulation rarely fails, but the model is less likely to reproduce a targeted distractor on problems with longer correct solutions](error-simulation-accurate-but-longer-solutions-harder.md) — related
- [Learner errors arise from interlingual transfer, intralingual overgeneralization, cultural interference, and communicative strategies](error-sources-interlingual-intralingual-cultural.md) — related
- [On the misconception-annotated math dataset, LLMs predominantly follow a solve-first, error-injection process aligned with misconception-based distractor design](llms-solve-first-error-injection-edi.md) — related
- [Incorporating example problems does not necessarily improve LLM teaching and can degrade it via a shift to example-specific error correction](example-problems-degrade-llm-teaching.md) — related
