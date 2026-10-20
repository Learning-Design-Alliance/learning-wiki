---
type: claim
title: Specializing models for K-12 education does not require a broad loss of general capability, with MMMU-Pro accuracy increasing at all three scales
description: Specializing models for K-12 education does not require a broad loss of general capability, with MMMU-Pro accuracy increasing at all three scales
id: omniedu-general-capability-retained-after-specialization
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: hao-liang-2026
    resource: "https://doi.org/10.48550/arxiv.2609.23088"
    title: "Hao Liang, Qihan Lin, Meiyi Qiang, Linzhuang Sun, Hengyi Feng, Mingrui Chen, Sizhe Qiu, Wentao Zhang. (2026). OmniEdu: Open Foundation Models for Learning and Teaching. https://arxiv.org/abs/2609.23088 [doi:10.48550/arxiv.2609.23088](https://doi.org/10.48550/arxiv.2609.23088)"
    author: Hao Liang, Qihan Lin, Meiyi Qiang, Linzhuang Sun, Hengyi Feng, Mingrui Chen, Sizhe Qiu, Wentao Zhang
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: hao-liang-2026-2
    resource: "https://arxiv.org/abs/2609.23088"
    title: "Hao Liang, Qihan Lin, Meiyi Qiang, Linzhuang Sun, Hengyi Feng, Mingrui Chen, Sizhe Qiu, Wentao Zhang. (2026). OmniEdu: Open Foundation Models for Learning and Teaching. https://arxiv.org/abs/2609.23088"
    author: Hao Liang, Qihan Lin, Meiyi Qiang, Linzhuang Sun, Hengyi Feng, Mingrui Chen, Sizhe Qiu, Wentao Zhang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Specializing models for K-12 education does not require a broad loss of general capability, with MMMU-Pro accuracy increasing at all three scales

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` MMMU-Pro overall accuracy increases from 50.46% to 52.60% for 4B, from 58.38% to 60.75% for 9B, and from 64.97% to 67.98% for 27B after education-oriented tuning. [→ Hao Liang 2026](#hao-liang-2026)
`q2 i?` Across the three scales, tuning generally improves IFEval metrics and improves both GPQA Main and Diamond accuracy. [→ Hao Liang 2026 (2)](#hao-liang-2026-2)

## Evidence

### Hao Liang 2026

Hao Liang, Qihan Lin, Meiyi Qiang, Linzhuang Sun, Hengyi Feng, Mingrui Chen, Sizhe Qiu, Wentao Zhang. (2026). OmniEdu: Open Foundation Models for Learning and Teaching. https://arxiv.org/abs/2609.23088 [doi:10.48550/arxiv.2609.23088](https://doi.org/10.48550/arxiv.2609.23088)

`q2 · i?` · `design · r2`

General-capability retention evaluation (Section 4.5) of base versus tuned models on IFEval, GPQA, and MMMU-Pro. The article reports MMMU-Pro overall accuracy increases at all three scales, though changes vary by MMMU-Pro discipline.

> "MMMU-Pro overall accuracy increases from 50.46% to 52.60% for 4B, from 58.38% to 60.75% for 9B, and from 64.97% to 67.98% for 27B."

### Hao Liang 2026 (2)

Hao Liang, Qihan Lin, Meiyi Qiang, Linzhuang Sun, Hengyi Feng, Mingrui Chen, Sizhe Qiu, Wentao Zhang. (2026). OmniEdu: Open Foundation Models for Learning and Teaching. https://arxiv.org/abs/2609.23088

`q2 · i?` · `design · r2`

Section 4.5 auxiliary diagnostics of instruction following (IFEval) and scientific reasoning (GPQA). The article reports tuning "generally improves IFEval metrics and improves both GPQA Main and Diamond accuracy".

> "Across the three scales, tuning generally improves IFEval metrics and improves both GPQA Main and Diamond accuracy."

## Discussion


## Related Claims
- [Education-oriented instruction tuning consistently improves curriculum grounding, K-12 problem solving, and pedagogical tutoring at every evaluated model scale](omniedu-tuning-improves-all-three-educational-capability-groups.md) — a broader claim this one bears on
- [Education-oriented tuning improves authentic K-12 problem solving, with OmniEdu-27B's MDK12-Bench open-question correctness rising from 62.08% to 78.77%](omniedu-k12-problem-solving-gains.md) — related
- [LoRA adaptation significantly increases closed-book accuracy on the PhysicsMate test set at all three Qwen3 scales](lora-adaptation-raises-bengali-physics-qa-accuracy-all-scales.md) — related
- [A single difficulty-weighted SFT run on a vision-language base model reaches 61.64% overall accuracy on TutorBench, surpassing Gemini-3 Pro (58.52%)](difficulty-weighted-sft-transfers-tutorbench.md) — related
- [Education-oriented tuning produces the largest gains in scaffolded instruction and use of longitudinal student evidence, with LongTutor Evidence averages rising sharply at all scales](omniedu-largest-gains-scaffolding-longitudinal-evidence.md) — related
