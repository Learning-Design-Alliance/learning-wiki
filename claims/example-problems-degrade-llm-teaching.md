---
type: claim
title: Incorporating example problems does not necessarily improve LLM teaching and can degrade it via a shift to example-specific error correction
description: Incorporating example problems does not necessarily improve LLM teaching and can degrade it via a shift to example-specific error correction
id: example-problems-degrade-llm-teaching
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
    rigour: 1
  - id: zheng-li-2026-2
    resource: "https://arxiv.org/abs/2601.21375"
    title: "Zheng Li, Siyao Song, Jingyuan Ma, Rui Li, Ying Zeng, Minghao Li, Zhifang Sui. (2026). TeachBench: A Syllabus-Grounded Framework for Evaluating Teaching Ability in Large Language Models. https://arxiv.org/abs/2601.21375"
    author: Zheng Li, Siyao Song, Jingyuan Ma, Rui Li, Ying Zeng, Minghao Li, Zhifang Sui
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Incorporating example problems does not necessarily improve LLM teaching and can degrade it via a shift to example-specific error correction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q1`–`q2`

## Subclaims
`q2 i?` Adding example problems to knowledge-point instruction often reduces measured teaching effectiveness at Pass@1 (e.g., Gemini-2.5-Pro drops from 7.60 to 3.33 points improvement). [→ Zheng Li 2026](#zheng-li-2026)
`q1 i?` Qualitative dialogue analysis shows teachers with example problems shift from syllabus-grounded instruction to example-driven explanation and error correction, fragmenting teaching. [→ Zheng Li 2026 (2)](#zheng-li-2026-2)

## Evidence

### Zheng Li 2026

Zheng Li, Siyao Song, Jingyuan Ma, Rui Li, Ying Zeng, Minghao Li, Zhifang Sui. (2026). TeachBench: A Syllabus-Grounded Framework for Evaluating Teaching Ability in Large Language Models. https://arxiv.org/abs/2601.21375

`q2 · i?` · `causal · r1`

Mathematics-subset experiment comparing teacher agents with and without example problems (Table 3): Gemini-2.5-Pro-Example gains 3.33 Pass@1 points versus 7.60 without; Claude-4-Opus-Example gains 2.69 versus 7.12. The authors state the pattern is "consistent across models and evaluation settings".

> "Focusing on Pass@1, we observe that adding example problems often reduces the measured teaching effectiveness. Although knowledge-point-based instruction yields substantial improvements, augmenting it with example problems does not reliably enhance instruction and can even degrade performance under the current interaction design."

### Zheng Li 2026 (2)

Zheng Li, Siyao Song, Jingyuan Ma, Rui Li, Ying Zeng, Minghao Li, Zhifang Sui. (2026). TeachBench: A Syllabus-Grounded Framework for Evaluating Teaching Ability in Large Language Models. https://arxiv.org/abs/2601.21375

`q1 · i?` · `design · r2`

Qualitative case study of teaching dialogues (Appendix B) finding that with examples, teaching "degrades into example-specific error correction rather than systematic instruction", with unnecessary interaction overhead and limited conceptual generalization for unmastered points.

> "when example problems are provided, teacher agents tend to shift from syllabus-grounded instruction to example-driven explanation, often asking the student agent to solve examples and focusing on correcting errors."

## Discussion


## Related Claims
- [Minimal guidance is less effective for novices than explicit instruction](minimal-guidance-less-effective-for-novices.md) — related
- [Instruction-tuning a student model on a single misconception overgeneralizes the error across problems and degrades correct-solving accuracy](student-model-misconception-overgeneralization-degrades-accuracy.md) — related
- [Decorative Illustrations Do Not Improve Learning](seductive-details-effect.md) — a broader claim this one bears on
- [Multi-turn teaching by LLM teacher agents yields larger student gains than knowledge-point exposure alone](multi-turn-teaching-beats-knowledge-point-exposure.md) — related
- [Pass@1 is not a sufficient success metric for soft barriers because it conflates successful barriers with model generation failures](pass1-false-narrative-soft-barriers.md) — related
