---
type: claim
title: Education-oriented tuning produces the largest gains in scaffolded instruction and use of longitudinal student evidence, with LongTutor Evidence averages rising sharply at all scales
description: Education-oriented tuning produces the largest gains in scaffolded instruction and use of longitudinal student evidence, with LongTutor Evidence averages rising sharply at all scales
id: omniedu-largest-gains-scaffolding-longitudinal-evidence
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: hao-liang-2026
    resource: "https://arxiv.org/abs/2609.23088"
    title: "Hao Liang, Qihan Lin, Meiyi Qiang, Linzhuang Sun, Hengyi Feng, Mingrui Chen, Sizhe Qiu, Wentao Zhang. (2026). OmniEdu: Open Foundation Models for Learning and Teaching. https://arxiv.org/abs/2609.23088"
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

# Education-oriented tuning produces the largest gains in scaffolded instruction and use of longitudinal student evidence, with LongTutor Evidence averages rising sharply at all scales

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` LongTutor Evidence averages increase from 25.67% to 65.88% for OmniEdu-4B, from 5.81% to 66.63% for OmniEdu-9B, and from 36.80% to 78.20% for OmniEdu-27B. [→ Hao Liang 2026](#hao-liang-2026)
`q2 i?` OmniEdu-27B and OmniEdu-9B rank first and second in LongTutor knowledge-state diagnosis accuracy at 54.04% and 53.55%, but the article notes diagnosis remains comparatively challenging. [→ Hao Liang 2026 (2)](#hao-liang-2026-2)

## Evidence

### Hao Liang 2026

Hao Liang, Qihan Lin, Meiyi Qiang, Linzhuang Sun, Hengyi Feng, Mingrui Chen, Sizhe Qiu, Wentao Zhang. (2026). OmniEdu: Open Foundation Models for Learning and Teaching. https://arxiv.org/abs/2609.23088

`q2 · i?` · `design · r2`

Pedagogical-tutoring benchmark evaluation (Section 4.4, Table 3) on MathTutorBench, TutorBench, and LongTutor. The article reports LongTutor Evidence average gains at all three scales, indicating stronger use of student learning history.

> "The Evidence average increases from 25.67% to 65.88% for OmniEdu-4B, from 5.81% to 66.63% for OmniEdu-9B, and from 36.80% to78.20%for OmniEdu-27B."

### Hao Liang 2026 (2)

Hao Liang, Qihan Lin, Meiyi Qiang, Linzhuang Sun, Hengyi Feng, Mingrui Chen, Sizhe Qiu, Wentao Zhang. (2026). OmniEdu: Open Foundation Models for Learning and Teaching. https://arxiv.org/abs/2609.23088

`q2 · i?` · `design · r2`

LongTutor knowledge-state diagnosis results in Section 4.4. The article reports OmniEdu-27B and OmniEdu-9B ranking first and second at 54.04% and 53.55%, while noting "knowledge-state diagnosis remains comparatively challenging".

> "OmniEdu also performs particularly well on knowledge-state diagnosis, with OmniEdu-27B and OmniEdu-9B ranking first and second in diagnosis accuracy at54.04%and53.55%, respectively. However, the relatively low accuracies indicate that knowledge-state diagnosis remains comparatively challenging."

## Discussion


## Related Claims
- [Education-oriented tuning improves authentic K-12 problem solving, with OmniEdu-27B's MDK12-Bench open-question correctness rising from 62.08% to 78.77%](omniedu-k12-problem-solving-gains.md) — related
- [Education-oriented instruction tuning consistently improves curriculum grounding, K-12 problem solving, and pedagogical tutoring at every evaluated model scale](omniedu-tuning-improves-all-three-educational-capability-groups.md) — a broader claim this one bears on
- [OmniEdu-27B achieves the best overall curriculum-grounding performance among evaluated models, raising K12-Bench EM from 52.11% to 63.12%](omniedu-27b-best-curriculum-grounding-k12-bench.md) — related
