---
type: claim
title: "OmniEdu-27B achieves the best overall curriculum-grounding performance among evaluated models, raising K12-Bench EM from 52.11% to 63.12%"
description: "OmniEdu-27B achieves the best overall curriculum-grounding performance among evaluated models, raising K12-Bench EM from 52.11% to 63.12%"
id: omniedu-27b-best-curriculum-grounding-k12-bench
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
---

# OmniEdu-27B achieves the best overall curriculum-grounding performance among evaluated models, raising K12-Bench EM from 52.11% to 63.12%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` OmniEdu-27B increases K12-Bench overall EM from 52.11% to 63.12% and F1 from 73.48% to 76.69% over its base model, the best among evaluated models. [→ Hao Liang 2026](#hao-liang-2026)

## Evidence

### Hao Liang 2026

Hao Liang, Qihan Lin, Meiyi Qiang, Linzhuang Sun, Hengyi Feng, Mingrui Chen, Sizhe Qiu, Wentao Zhang. (2026). OmniEdu: Open Foundation Models for Learning and Teaching. https://arxiv.org/abs/2609.23088 [doi:10.48550/arxiv.2609.23088](https://doi.org/10.48550/arxiv.2609.23088)

`q2 · i?` · `design · r2`

Curriculum-grounding benchmark evaluation (Section 4.2, Table 1) comparing tuned and base models. The article reports OmniEdu-27B "achieving the best overall performance among the evaluated models" on K12-Bench, with gains consistent across all subtasks.

> "OmniEdu-27B increases the overall EM from 52.11% to63.12%and F1 from 73.48% to76.69%, achieving the best overall performance among the evaluated models."

## Discussion


## Related Claims
- [Education-oriented tuning improves authentic K-12 problem solving, with OmniEdu-27B's MDK12-Bench open-question correctness rising from 62.08% to 78.77%](omniedu-k12-problem-solving-gains.md) — related
- [Education-oriented instruction tuning consistently improves curriculum grounding, K-12 problem solving, and pedagogical tutoring at every evaluated model scale](omniedu-tuning-improves-all-three-educational-capability-groups.md) — a broader claim this one bears on
- [Current LLMs lack robust curriculum cognition: even the best model reaches only 57.1% exact match on K12-Bench, with prerequisite and neighbor tasks hardest](llms-lack-curriculum-cognition-k12-bench.md) — reports the opposite
- [Education-oriented tuning produces the largest gains in scaffolded instruction and use of longitudinal student evidence, with LongTutor Evidence averages rising sharply at all scales](omniedu-largest-gains-scaffolding-longitudinal-evidence.md) — related
