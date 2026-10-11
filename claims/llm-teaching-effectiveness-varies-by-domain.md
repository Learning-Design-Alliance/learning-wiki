---
type: claim
title: LLM teaching effectiveness varies substantially across subject domains, strongest where knowledge points apply directly and weakest in physics and chemistry
description: LLM teaching effectiveness varies substantially across subject domains, strongest where knowledge points apply directly and weakest in physics and chemistry
id: llm-teaching-effectiveness-varies-by-domain
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: zheng-li-2026
    resource: "https://arxiv.org/abs/2601.21375"
    title: "Zheng Li, Siyao Song, Jingyuan Ma, Rui Li, Ying Zeng, Minghao Li, Zhifang Sui. (2026). TeachBench: A Syllabus-Grounded Framework for Evaluating Teaching Ability in Large Language Models. https://arxiv.org/abs/2601.21375"
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

# LLM teaching effectiveness varies substantially across subject domains, strongest where knowledge points apply directly and weakest in physics and chemistry

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` Across six additional subjects, teaching outcomes rank Mathematics, History, and Politics strongest, Geography and Biology intermediate, and Physics and Chemistry weakest. [→ Zheng Li 2026](#zheng-li-2026)
`q2 i?` In physics and chemistry, teaching often fails to help or even hurts: e.g., Qwen3-235B shows -6.30 accuracy change in Chemistry and -5.65 in Physics versus gains in Politics and History. [→ Zheng Li 2026 (2)](#zheng-li-2026-2)

## Evidence

### Zheng Li 2026

Zheng Li, Siyao Song, Jingyuan Ma, Rui Li, Ying Zeng, Minghao Li, Zhifang Sui. (2026). TeachBench: A Syllabus-Grounded Framework for Evaluating Teaching Ability in Large Language Models. https://arxiv.org/abs/2601.21375

`q2 · i?` · `causal · r2`

Cross-domain experiment (Table 4) evaluating teacher agents on Biology, Chemistry, Physics, Politics, History, and Geography subsets, showing "substantial variation in teaching outcomes across domains" and domain dependence of LLM teaching capability.

> "Across domains, we observe a clear performance ranking. Mathematics, History, and Politics exhibit the strongest teaching outcomes, followed by Geography and Biology, while Physics and Chemistry show the weakest performance."

### Zheng Li 2026 (2)

Zheng Li, Siyao Song, Jingyuan Ma, Rui Li, Ying Zeng, Minghao Li, Zhifang Sui. (2026). TeachBench: A Syllabus-Grounded Framework for Evaluating Teaching Ability in Large Language Models. https://arxiv.org/abs/2601.21375

`q2 · i?` · `design · r2`

Table 4 row for Qwen3-235B: accuracy changes of -6.30 in Chemistry and -5.65 in Physics versus +2.95 in Politics and +4.65 in History, illustrating that teaching can reduce student accuracy in integration-heavy domains. Values are descriptive; no significance tests are reported.

> "Qwen3-235B 77.12 -1.22 65.85 -6.30 66.28 -5.65 81.69 2.95 82.03 4.65 77.14 -2.59"

## Discussion


## Related Claims
- [Multi-turn interaction amplifies pedagogical harm: mean harm rises 6-11 percentage points across subjects and pedagogical-relationship harm surges from 17.7% to 77.8%](multi-turn-dialogue-amplifies-tutor-harm.md) — related
- [Harm profiles are subject-dependent: metacognitive harm crosses 90% in all three subjects in multi-turn, peaking at 97.44% for Qwen2.5-32B in Mathematics](tutor-harm-subject-dependent-mitigations.md) — related
- [VietEduQwen improves over its base model across all eight exam subjects, with the largest gains in STEM disciplines, and its residual errors concentrate in multi-step computation and cross-concept integration](vieteduqwen-subject-wise-stem-gains-error-modes.md) — related
- [LLMs struggle most with Chemistry riddles, with best EM accuracy at or below 75% versus above 90% in other subjects](llms-struggle-most-chemistry-nsmq-riddles.md) — related
- [Multi-turn teaching by LLM teacher agents yields larger student gains than knowledge-point exposure alone](multi-turn-teaching-beats-knowledge-point-exposure.md) — related
