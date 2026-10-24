---
type: claim
title: "VLMs show a common grounding failure: coarse semantic relevance without precise region-activity binding and entity-evidence alignment"
description: "VLMs show a common grounding failure: coarse semantic relevance without precise region-activity binding and entity-evidence alignment"
id: vlm-grounding-failure-region-activity-binding
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
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

# VLMs show a common grounding failure: coarse semantic relevance without precise region-activity binding and entity-evidence alignment

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Error analysis across Activity Localization, Activity Description, and Remote Interaction reveals that models capture coarse semantic relevance but accept plausible relations without verifying joint alignment of entities, regions, and evidence. [→ Luyao Zhu 2026](#luyao-zhu-2026)

## Evidence

### Luyao Zhu 2026

Luyao Zhu, Xun Wei Yee, Wei Li, Mun Thye Mak, Wee Siong Ng. (2026). MUSE: Benchmarking Large Vision-Language Models on Multi-modal Understanding in Situated Education. arXiv preprint. https://arxiv.org/abs/2609.19088 [doi:10.48550/arxiv.2609.19088](https://doi.org/10.48550/arxiv.2609.19088)

`q2 · i?` · `design · r2`

Cross-task error analysis of incorrect option and evidence-selection type distributions across models for three tasks (Figure 8). The article reports that in Activity Localization models "usually select semantically relevant people or activities rather than random regions, but fail to identify the complete target extent."

> "In Remote Interaction, mismatched region-text pairs dominate, showing that models often accept plausible relations without verifying whether entities, regions, and evidence are jointly aligned."

## Discussion


## Related Claims
- [MLLMs show recurring failures in fine-grained quantitative estimation, often identifying the encoding and measurement strategy but misestimating precise values](mllm-fine-grained-quantitative-misestimation-scivis.md) — a narrower finding that bears on this claim
- [Some VLMs perform near chance on binary judgments of student correctness, and error-assessment behavior is idiosyncratic across models](binary-correctness-judgments-near-chance.md) — related
- [Human performance forms the outer envelope on nearly all MUSE tasks, with the largest deficits in Relative Position, Emotion Detection, and Jigsaw Puzzle](human-vlm-gap-muse-tasks.md) — related
- [VLM performance on artistic educational imagery is highly task-dependent, with no model dominating across capabilities](vlm-performance-task-dependent-muse.md) — related
- [Some MLLM failures occur when a higher-level SciVis interpretation is grounded in an unsupported visual encoding rather than the encoding specified by the visualization and caption](mllm-encoding-mapping-error-unsupported-grounding.md) — a narrower finding that bears on this claim
