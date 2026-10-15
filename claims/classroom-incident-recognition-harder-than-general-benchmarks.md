---
type: claim
title: "Classroom incident recognition is substantially harder than established general action-recognition benchmarks, with PoseC3D dropping from over 94% accuracy to 70.54%"
description: "Classroom incident recognition is substantially harder than established general action-recognition benchmarks, with PoseC3D dropping from over 94% accuracy to 70.54%"
id: classroom-incident-recognition-harder-than-general-benchmarks
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: paritosh-parmar-2026
    resource: "https://doi.org/10.48550/arxiv.2608.05115"
    title: "Paritosh Parmar, Landy Lan, Hong Yang, Chen Yi, Chiat Pin Tay. (2026). Robust and Efficient Motion Reasoning for Privacy-Aware Classroom Incident Recognition. arXiv preprint. https://arxiv.org/abs/2608.05115 [doi:10.48550/arxiv.2608.05115](https://doi.org/10.48550/arxiv.2608.05115)"
    author: Paritosh Parmar, Landy Lan, Hong Yang, Chen Yi, Chiat Pin Tay
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Classroom incident recognition is substantially harder than established general action-recognition benchmarks, with PoseC3D dropping from over 94% accuracy to 70.54%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` PoseC3D, reported to achieve over 94% accuracy on NTURGBD and FineGym, reaches only 70.54% on the classroom incident dataset, which the authors attribute to viewpoint variation, subject diversity, noisy pose trajectories, and fine-grained differences between safety-related actions. [→ Paritosh Parmar 2026](#paritosh-parmar-2026)

## Evidence

### Paritosh Parmar 2026

Paritosh Parmar, Landy Lan, Hong Yang, Chen Yi, Chiat Pin Tay. (2026). Robust and Efficient Motion Reasoning for Privacy-Aware Classroom Incident Recognition. arXiv preprint. https://arxiv.org/abs/2608.05115 [doi:10.48550/arxiv.2608.05115](https://doi.org/10.48550/arxiv.2608.05115)

`q2 · i?` · `design · r2`

Cross-benchmark comparison in the synthetic-dataset results section: the same PoseC3D model scores over 94% on established benchmarks but only 70.54% on the classroom incident dataset. The authors state the task "remains far from solved"; accuracies only, no effect size.

> "PoseC3D [11] has been reported to achieve over 94% accuracy on established benchmarks such as NTURGBD [26] and FineGym [37], but reaches only 70.54% accuracy on our classroom incident dataset."

## Discussion


## Related Claims
- [A distilled multi-order kinematic model outperforms pose-based baselines on a synthetic classroom incident dataset while using one-tenth as many parameters as PoseC3D](distilled-kinematic-model-outperforms-pose-baselines-synthetic-classroom-incidents.md) — related
- [Models trained on synthetic classroom incident data transfer zero-shot to real-world footage, with the proposed method best at 63.41% though a synthetic-to-real domain gap remains](zero-shot-synthetic-to-real-classroom-incident-transfer.md) — related
