---
type: claim
title: Multi-turn teaching by LLM teacher agents yields larger student gains than knowledge-point exposure alone
description: Multi-turn teaching by LLM teacher agents yields larger student gains than knowledge-point exposure alone
id: multi-turn-teaching-beats-knowledge-point-exposure
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: zheng-li-2026
    resource: "https://doi.org/10.48550/arxiv.2601.21375"
    title: "Zheng Li, Siyao Song, Jingyuan Ma, Rui Li, Ying Zeng, Minghao Li, Zhifang Sui. (2026). TeachBench: A Syllabus-Grounded Framework for Evaluating Teaching Ability in Large Language Models. https://arxiv.org/abs/2601.21375 [doi:10.48550/arxiv.2601.21375](https://doi.org/10.48550/arxiv.2601.21375)"
    author: Zheng Li, Siyao Song, Jingyuan Ma, Rui Li, Ying Zeng, Minghao Li, Zhifang Sui
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: zheng-li-2026-2
    resource: "https://arxiv.org/abs/2601.21375"
    title: "Zheng Li, Siyao Song, Jingyuan Ma, Rui Li, Ying Zeng, Minghao Li, Zhifang Sui. (2026). TeachBench: A Syllabus-Grounded Framework for Evaluating Teaching Ability in Large Language Models. https://arxiv.org/abs/2601.21375"
    author: Zheng Li, Siyao Song, Jingyuan Ma, Rui Li, Ying Zeng, Minghao Li, Zhifang Sui
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Multi-turn teaching by LLM teacher agents yields larger student gains than knowledge-point exposure alone

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` On the Gaokao Mathematics subset, explicit multi-turn teaching interactions improve student Pass@1 accuracy substantially more than providing knowledge points without interaction (e.g., 7.63 points for the strongest teacher vs. 4.37 for knowledge-only). [→ Zheng Li 2026](#zheng-li-2026)
`q2 i?` Qwen3-235B-A22B-Instruct-2507 achieves the strongest teaching performance among evaluated models, with the largest Pass@1 improvement of 7.63 points. [→ Zheng Li 2026 (2)](#zheng-li-2026-2)

## Evidence

### Zheng Li 2026

Zheng Li, Siyao Song, Jingyuan Ma, Rui Li, Ying Zeng, Minghao Li, Zhifang Sui. (2026). TeachBench: A Syllabus-Grounded Framework for Evaluating Teaching Ability in Large Language Models. https://arxiv.org/abs/2601.21375 [doi:10.48550/arxiv.2601.21375](https://doi.org/10.48550/arxiv.2601.21375)

`q2 · i?` · `causal · r2`

Simulation-style controlled experiment on the Gaokao Mathematics subset with Qwen2.5-7B-Instruct as student agent. Knowledge-point exposure alone yields a "4.37 points" Pass@1 gain over the no-teaching baseline, which the authors call "only modest benefits".

> "Qwen2.5-7B-Instruct(Knowledge) improves Pass@1 accuracy by 4.37 points over the no-teaching baseline. This result indicates that access to structured knowledge alone provides only modest benefits."

### Zheng Li 2026 (2)

Zheng Li, Siyao Song, Jingyuan Ma, Rui Li, Ying Zeng, Minghao Li, Zhifang Sui. (2026). TeachBench: A Syllabus-Grounded Framework for Evaluating Teaching Ability in Large Language Models. https://arxiv.org/abs/2601.21375

`q2 · i?` · `design · r2`

Same Mathematics-subset evaluation across multiple teacher agents, each running three independent teaching sessions with 64 repeated student evaluations. Qwen3-235B-A22B-Instruct-2507 achieves the "largest Pass@1 im- provement of 7.63 points", and gains from teaching consistently exceed knowledge-only exposure.

> "Among the evaluated models, Qwen3-235B- A22B-Instruct-2507 achieves the strongest teach- ing performance, yielding the largest Pass@1 im- provement of 7.63 points."

## Discussion


## Related Claims
- [Incorporating example problems does not necessarily improve LLM teaching and can degrade it via a shift to example-specific error correction](example-problems-degrade-llm-teaching.md) — related
- [Teaching primarily helps the student agent realize existing potential rather than raise its absolute performance ceiling](teaching-narrow-pass-gap-not-ceiling.md) — related
- [LLM teaching effectiveness varies substantially across subject domains, strongest where knowledge points apply directly and weakest in physics and chemistry](llm-teaching-effectiveness-varies-by-domain.md) — related
- [In math problem solving, a tutor-plus-peers LLM arrangement produced the strongest unassisted post-task test accuracy, with accuracy increasing monotonically from Control to Tutor + Peers](tutor-plus-peers-strongest-unassisted-math-accuracy.md) — related
- [Learning By Teaching Improves Tutor Learning](learning-by-teaching-improves-tutor-learning.md) — related
- [Multi-turn interaction amplifies pedagogical harm: mean harm rises 6-11 percentage points across subjects and pedagogical-relationship harm surges from 17.7% to 77.8%](multi-turn-dialogue-amplifies-tutor-harm.md) — related
- [Example-based instructional activities yield larger effects when delivered jointly by ICT and teachers than by teachers alone](examples-joint-ict-teacher-delivery-larger-effects.md) — related
