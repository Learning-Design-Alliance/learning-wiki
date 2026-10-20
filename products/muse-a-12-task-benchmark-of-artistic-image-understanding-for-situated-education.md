---
type: product
id: muse-a-12-task-benchmark-of-artistic-image-understanding-for-situated-education
title: "MUSE: a 12-task benchmark of artistic image understanding for situated education"
description: MUSE is a benchmark dataset developed by Luyao Zhu et al.
product_kind: dataset
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# MUSE: a 12-task benchmark of artistic image understanding for situated education

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 8 claims (8 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 8 claims rest on one study

## Description
MUSE is a benchmark dataset developed by Luyao Zhu et al. containing annotated artistic images and questions for evaluating large vision-language models' multimodal understanding in educational interaction.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **MUSE: a 12-task benchmark of artistic image understanding for situated education**: MUSE is a benchmark for evaluating large vision-language models on artistic image understanding in image-based language learning and educational interaction. It contains "2,400 questions over 1,174 images" at 1920×1080 resolution, spanning 12 tasks across five capability dimensions: visual perception, semantic understanding, affective interpretation, compositional reasoning, and cultural understanding. Images were commissioned from artists and curated to center Singaporean and Southeast Asian multicultural contexts alongside Western art traditions, with annotation by 127 trained annotators under consensus review. (Luyao Zhu et al. (2026))

### Claims

- [MUSE tasks form coherent but non-redundant capability groups, with Jigsaw Puzzle a distinct compositional capability](../claims/muse-tasks-non-redundant-capability-groups.md) [+W]
- [Performance on existing benchmarks transfers unevenly to artistic educational imagery](../claims/existing-benchmarks-transfer-unevenly-artistic-imagery.md) [+W]
- [Human performance forms the outer envelope on nearly all MUSE tasks, with the largest deficits in Relative Position, Emotion Detection, and Jigsaw Puzzle](../claims/human-vlm-gap-muse-tasks.md) [+W]
- [VLM performance on artistic educational imagery is highly task-dependent, with no model dominating across capabilities](../claims/vlm-performance-task-dependent-muse.md) [+W]
- [A recognition-versus-reasoning divide: scene recognition is comparatively mature while affective interpretation and compositional reasoning lag](../claims/recognition-reasoning-divide-muse.md) [+W]
- [Response-format reliability is a distinct evaluation concern, with invalid response rates varying independently of model scale](../claims/invalid-response-rates-distinct-evaluation-concern.md) [+W]
- [Viewpoint-aware spatial reasoning is a persistent bottleneck with poor calibration of spatial uncertainty](../claims/viewpoint-aware-spatial-reasoning-bottleneck.md) [+W]
- [VLMs show a common grounding failure: coarse semantic relevance without precise region-activity binding and entity-evidence alignment](../claims/vlm-grounding-failure-region-activity-binding.md) [+W]

## Related Products and Programmes

- [DrawEduMath](drawedumath.md)
- [MAESTRO v3.0.0 pretraining corpus and custom 4,320-recording student dataset](maestro-v300-pretraining-corpus-and-custom-4320-recording-student-dataset.md)

## Key Sources
- Luyao Zhu, Xun Wei Yee, Wei Li, Mun Thye Mak, Wee Siong Ng. (2026). MUSE: Benchmarking Large Vision-Language Models on Multi-modal Understanding in Situated Education. arXiv preprint. https://arxiv.org/abs/2609.19088
