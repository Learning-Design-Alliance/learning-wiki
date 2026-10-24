---
type: claim
title: VLM performance on artistic educational imagery is highly task-dependent, with no model dominating across capabilities
description: VLM performance on artistic educational imagery is highly task-dependent, with no model dominating across capabilities
id: vlm-performance-task-dependent-muse
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: luyao-zhu-2026
    resource: "https://doi.org/10.48550/arxiv.2609.19088"
    title: "Luyao Zhu, Xun Wei Yee, Wei Li, Mun Thye Mak, Wee Siong Ng. (2026). MUSE: Benchmarking Large Vision-Language Models on Multi-modal Understanding in Situated Education. arXiv preprint. https://arxiv.org/abs/2609.19088 [doi:10.48550/arxiv.2609.19088](https://doi.org/10.48550/arxiv.2609.19088)"
    author: Luyao Zhu, Xun Wei Yee, Wei Li, Mun Thye Mak, Wee Siong Ng
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# VLM performance on artistic educational imagery is highly task-dependent, with no model dominating across capabilities

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across 30 evaluated VLMs, performance on MUSE is highly task-dependent and no model dominates across all capabilities; GPT-5.6-Sol is strongest overall, surpassing GPT-4o on 10 of 12 tasks, while GPT-4o remains superior on Activity Description and Relative Position. [→ Luyao Zhu 2026](#luyao-zhu-2026)

## Evidence

### Luyao Zhu 2026

Luyao Zhu, Xun Wei Yee, Wei Li, Mun Thye Mak, Wee Siong Ng. (2026). MUSE: Benchmarking Large Vision-Language Models on Multi-modal Understanding in Situated Education. arXiv preprint. https://arxiv.org/abs/2609.19088 [doi:10.48550/arxiv.2609.19088](https://doi.org/10.48550/arxiv.2609.19088)

`q2 · i?` · `design · r2`

Benchmark evaluation of 30 open-source and proprietary VLMs on the 12 MUSE tasks (Table 2), all run at temperature 0 and scored by accuracy or semantic similarity. The article reports that "GPT-5.6-Sol achieves the strongest overall results" while open-source models retain task-specific advantages such as Qwen3-VL-32b leading Activity Localization and Scene Classification.

> "GPT-5.6-Sol achieves the strongest overall results and surpasses GPT-4o on 10 of 12 tasks, yet GPT-4o remains superior on Activity Description and Relative Position."

## Discussion


## Related Claims
- [Performance on existing benchmarks transfers unevenly to artistic educational imagery](existing-benchmarks-transfer-unevenly-artistic-imagery.md) — related
- [Human performance forms the outer envelope on nearly all MUSE tasks, with the largest deficits in Relative Position, Emotion Detection, and Jigsaw Puzzle](human-vlm-gap-muse-tasks.md) — related
- [Response-format reliability is a distinct evaluation concern, with invalid response rates varying independently of model scale](invalid-response-rates-distinct-evaluation-concern.md) — related
- [MUSE tasks form coherent but non-redundant capability groups, with Jigsaw Puzzle a distinct compositional capability](muse-tasks-non-redundant-capability-groups.md) — related
- [A recognition-versus-reasoning divide: scene recognition is comparatively mature while affective interpretation and compositional reasoning lag](recognition-reasoning-divide-muse.md) — related
- [VLMs show a common grounding failure: coarse semantic relevance without precise region-activity binding and entity-evidence alignment](vlm-grounding-failure-region-activity-binding.md) — related
- [Some VLMs perform near chance on binary judgments of student correctness, and error-assessment behavior is idiosyncratic across models](binary-correctness-judgments-near-chance.md) — a narrower finding that bears on this claim
