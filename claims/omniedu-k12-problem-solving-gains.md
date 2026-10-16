---
type: claim
title: "Education-oriented tuning improves authentic K-12 problem solving, with OmniEdu-27B's MDK12-Bench open-question correctness rising from 62.08% to 78.77%"
description: "Education-oriented tuning improves authentic K-12 problem solving, with OmniEdu-27B's MDK12-Bench open-question correctness rising from 62.08% to 78.77%"
id: omniedu-k12-problem-solving-gains
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

# Education-oriented tuning improves authentic K-12 problem solving, with OmniEdu-27B's MDK12-Bench open-question correctness rising from 62.08% to 78.77%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` On MDK12-Bench, OmniEdu-27B improves the overall score from 46.04% to 57.76%, with open-question correctness rising from 62.08% to 78.77%. [→ Hao Liang 2026](#hao-liang-2026)
`q2 i?` On EXAMS-V, the improvement is particularly pronounced for OmniEdu-4B, whose overall accuracy increases from 44.69% to 57.62%. [→ Hao Liang 2026 (2)](#hao-liang-2026-2)

## Evidence

### Hao Liang 2026

Hao Liang, Qihan Lin, Meiyi Qiang, Linzhuang Sun, Hengyi Feng, Mingrui Chen, Sizhe Qiu, Wentao Zhang. (2026). OmniEdu: Open Foundation Models for Learning and Teaching. https://arxiv.org/abs/2609.23088 [doi:10.48550/arxiv.2609.23088](https://doi.org/10.48550/arxiv.2609.23088)

`q2 · i?` · `design · r2`

K-12 problem-solving benchmark evaluation (Section 4.3, Table 2) on GAOKAO-Bench, EXAMS-V, and MDK12-Bench. The article reports the MDK12-Bench overall score rising from 46.04% to 57.76% with open-question correctness "rising substantially from 62.08% to78.77%".

> "On MDK12-Bench, OmniEdu-27B improves the overall score from 46.04% to57.76%, with open-question correctness rising substantially from 62.08% to78.77%."

### Hao Liang 2026 (2)

Hao Liang, Qihan Lin, Meiyi Qiang, Linzhuang Sun, Hengyi Feng, Mingrui Chen, Sizhe Qiu, Wentao Zhang. (2026). OmniEdu: Open Foundation Models for Learning and Teaching. https://arxiv.org/abs/2609.23088

`q2 · i?` · `design · r2`

EXAMS-V evaluation within the Section 4.3 problem-solving results. The article states the improvement is "particularly pronounced for OmniEdu-4B", with overall accuracy increasing from 44.69% to 57.62%.

> "On EXAMS-V, the improvement is particularly pronounced for OmniEdu-4B, whose overall accuracy increases from 44.69% to 57.62%."

## Discussion


## Related Claims
- [OmniEdu-27B achieves the best overall curriculum-grounding performance among evaluated models, raising K12-Bench EM from 52.11% to 63.12%](omniedu-27b-best-curriculum-grounding-k12-bench.md) — related
- [Specializing models for K-12 education does not require a broad loss of general capability, with MMMU-Pro accuracy increasing at all three scales](omniedu-general-capability-retained-after-specialization.md) — related
- [Education-oriented instruction tuning consistently improves curriculum grounding, K-12 problem solving, and pedagogical tutoring at every evaluated model scale](omniedu-tuning-improves-all-three-educational-capability-groups.md) — a broader claim this one bears on
- [K12-Train-Full achieves the best overall performance on three multimodal educational benchmarks, and textual and visual supervision are complementary](k12-train-full-multimodal-complementarity.md) — related
- [Education-oriented tuning produces the largest gains in scaffolded instruction and use of longitudinal student evidence, with LongTutor Evidence averages rising sharply at all scales](omniedu-largest-gains-scaffolding-longitudinal-evidence.md) — related
