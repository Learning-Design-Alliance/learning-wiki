---
type: claim
title: In a blinded study with 50 learners, TACTutor receives the highest overall mean rating (5.54/7) and is rated above its backbone across all four teaching-behavior dimensions (+0.39 overall)
description: In a blinded study with 50 learners, TACTutor receives the highest overall mean rating (5.54/7) and is rated above its backbone across all four teaching-behavior dimensions (+0.39 overall)
id: tactutor-highest-blinded-learner-rating-5-54
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: dongjie-yang-2026
    resource: "https://doi.org/10.48550/arxiv.2608.03952"
    title: "Dongjie Yang, Siyan Lin, Leixian Shen, Rui Sheng, Huamin Qu, and Zixin Chen. (2026). TACT: Taxonomy-Aligned Post-Training for Pedagogically Adaptive English Tutoring. https://arxiv.org/abs/2608.03952 [doi:10.48550/arxiv.2608.03952](https://doi.org/10.48550/arxiv.2608.03952)"
    author: Dongjie Yang, Siyan Lin, Leixian Shen, Rui Sheng, Huamin Qu, and Zixin Chen
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: dongjie-yang-2026-2
    resource: "https://arxiv.org/abs/2608.03952"
    title: "Dongjie Yang, Siyan Lin, Leixian Shen, Rui Sheng, Huamin Qu, and Zixin Chen. (2026). TACT: Taxonomy-Aligned Post-Training for Pedagogically Adaptive English Tutoring. https://arxiv.org/abs/2608.03952"
    author: Dongjie Yang, Siyan Lin, Leixian Shen, Rui Sheng, Huamin Qu, and Zixin Chen
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# In a blinded study with 50 learners, TACTutor receives the highest overall mean rating (5.54/7) and is rated above its backbone across all four teaching-behavior dimensions (+0.39 overall)

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q2`

## Subclaims
`q2 i?` In a blinded, within-participant Prolific study (n=50, 200 conversations), TACTutor achieved the highest mean score (5.54), within 0.09 points of both proprietary tutors, and was rated above its backbone across all four dimensions (+0.39 overall). [→ Dongjie Yang 2026](#dongjie-yang-2026)
`q2 i?` The gains over the backbone were concentrated in encouragement (+0.58), guiding (+0.40), and scaffolding (+0.38), with self-correction improving more modestly (+0.20). [→ Dongjie Yang 2026 (2)](#dongjie-yang-2026-2)

## Evidence

### Dongjie Yang 2026

Dongjie Yang, Siyan Lin, Leixian Shen, Rui Sheng, Huamin Qu, and Zixin Chen. (2026). TACT: Taxonomy-Aligned Post-Training for Pedagogically Adaptive English Tutoring. https://arxiv.org/abs/2608.03952 [doi:10.48550/arxiv.2608.03952](https://doi.org/10.48550/arxiv.2608.03952)

`q2 · i?` · `design · r2`

Blinded, within-participant interactive evaluation with 50 real-world learners via Prolific; each participant held four conversations with anonymous tutors, yielding 200 conversations, with 1-7 ratings on guiding, scaffolding, encouragement, and self-correction support. The article reports the "highest mean score(5.54)"; no significance test is printed.

> "TACTutor achieved the highest mean score(5.54), within 0.09 points of both proprietary tutors, and was rated above its backbone across all four dimensions (+0.39overall)."

### Dongjie Yang 2026 (2)

Dongjie Yang, Siyan Lin, Leixian Shen, Rui Sheng, Huamin Qu, and Zixin Chen. (2026). TACT: Taxonomy-Aligned Post-Training for Pedagogically Adaptive English Tutoring. https://arxiv.org/abs/2608.03952

`q2 · i?` · `design · r2`

Dimension-level descriptive rating differences from the same blinded learner study. The article reports gains "concentrated inencouragement(+0.58),guiding(+0.40), and scaffolding(+0.38)"; self-correction improved more modestly (+0.20). No significance test is printed.

> "The gains were not uniform, but con- centrated inencouragement(+0.58),guiding(+0.40), and scaffolding(+0.38). This pattern suggests that taxonomy- aligned post-training changes the tutor's interactional pro- file toward more supportive and process-oriented responses, rather than producing only a general improvement in con- versational quality."

## Discussion


## Related Claims
- [Taxonomy-guided post-training raises TACTutor's TACT_Overall on TACTBench from 0.629 (backbone) to 0.832, the highest among evaluated models](tactutor-raises-tactbench-overall-0-629-to-0-832.md) — related
- [Post-training improves TACTutor's auxiliary guardrail flags on TACTBench: accept rate rises from 0.603 to 0.872 and leak-or-overhelp falls from 0.346 to 0.026](tactutor-guardrail-flags-improve-accept-leak.md) — related
- [TACTutor shows no degradation relative to its Qwen backbone on external educational benchmarks, with scores rising on MRBench, TutorBench, LongTutor, and DeepTutor](tactutor-no-degradation-external-benchmarks.md) — related
