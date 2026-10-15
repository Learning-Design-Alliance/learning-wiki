---
type: claim
title: A distilled multi-order kinematic model outperforms pose-based baselines on a synthetic classroom incident dataset while using one-tenth as many parameters as PoseC3D
description: A distilled multi-order kinematic model outperforms pose-based baselines on a synthetic classroom incident dataset while using one-tenth as many parameters as PoseC3D
id: distilled-kinematic-model-outperforms-pose-baselines-synthetic-classroom-incidents
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: paritosh-parmar-2026
    resource: "https://doi.org/10.48550/arxiv.2608.05115"
    title: "Paritosh Parmar, Landy Lan, Hong Yang, Chen Yi, Chiat Pin Tay. (2026). Robust and Efficient Motion Reasoning for Privacy-Aware Classroom Incident Recognition. arXiv preprint. https://arxiv.org/abs/2608.05115 [doi:10.48550/arxiv.2608.05115](https://doi.org/10.48550/arxiv.2608.05115)"
    author: Paritosh Parmar, Landy Lan, Hong Yang, Chen Yi, Chiat Pin Tay
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: paritosh-parmar-2026-2
    resource: "https://arxiv.org/abs/2608.05115"
    title: "Paritosh Parmar, Landy Lan, Hong Yang, Chen Yi, Chiat Pin Tay. (2026). Robust and Efficient Motion Reasoning for Privacy-Aware Classroom Incident Recognition. arXiv preprint. https://arxiv.org/abs/2608.05115"
    author: Paritosh Parmar, Landy Lan, Hong Yang, Chen Yi, Chiat Pin Tay
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A distilled multi-order kinematic model outperforms pose-based baselines on a synthetic classroom incident dataset while using one-tenth as many parameters as PoseC3D

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q2`

## Subclaims
`q2 i?` On the authors' synthetic classroom incident dataset, the proposed method reaches 71.78% accuracy, improving over PoseC3D by 1.24 percentage points and over MSG3D by 2.90 percentage points. [→ Paritosh Parmar 2026](#paritosh-parmar-2026)
`q2 i?` The proposed model uses only one-tenth as many parameters as PoseC3D while achieving superior performance on the synthetic dataset. [→ Paritosh Parmar 2026 (2)](#paritosh-parmar-2026-2)

## Evidence

### Paritosh Parmar 2026

Paritosh Parmar, Landy Lan, Hong Yang, Chen Yi, Chiat Pin Tay. (2026). Robust and Efficient Motion Reasoning for Privacy-Aware Classroom Incident Recognition. arXiv preprint. https://arxiv.org/abs/2608.05115 [doi:10.48550/arxiv.2608.05115](https://doi.org/10.48550/arxiv.2608.05115)

`q2 · i?` · `design · r2`

Comparison experiment on the authors' synthetic classroom incident dataset (80/20 train-test split) against AAGCN, STGCN++, CTRGCN, MSG3D and PoseC3D. The proposed method "achieves the highest accuracy of 71.78%"; accuracies are reported without effect sizes.

> "Our method achieves the highest accuracy of 71.78%, outperforming all compared baselines. In particular, it improves over PoseC3D, the strongest baseline on this dataset, by 1.24 percentage points, and over MSG3D by 2.90 percentage points."

### Paritosh Parmar 2026 (2)

Paritosh Parmar, Landy Lan, Hong Yang, Chen Yi, Chiat Pin Tay. (2026). Robust and Efficient Motion Reasoning for Privacy-Aware Classroom Incident Recognition. arXiv preprint. https://arxiv.org/abs/2608.05115

`q2 · i?` · `design · r2`

Efficiency comparison reported alongside the synthetic-dataset results and plotted in Figure 2 (performance vs GFLOPs, circle diameter indicating model size in million parameters). The model "uses only one-tenth as many parameters as PoseC3D"; no effect size is printed.

> "Notably, our model is computationally efficient: it uses only one-tenth as many parameters as PoseC3D, yet achieves superior performance (Figure 2)."

## Discussion


## Related Claims
- [Classroom incident recognition is substantially harder than established general action-recognition benchmarks, with PoseC3D dropping from over 94% accuracy to 70.54%](classroom-incident-recognition-harder-than-general-benchmarks.md) — related
- [Distilling a multi-order hierarchical teacher into a smaller zeroth-order student lets the student outperform the teacher, and improves 4.1 percentage points in accuracy over STGCN++](distilled-student-outperforms-multiorder-teacher.md) — related
- [Models trained on synthetic classroom incident data transfer zero-shot to real-world footage, with the proposed method best at 63.41% though a synthetic-to-real domain gap remains](zero-shot-synthetic-to-real-classroom-incident-transfer.md) — related
- [The framework is robust to 15% ASR transcription noise and retains 99.6% of its ICS under zero-shot cross-domain transfer to EdNet-Math](framework-robust-asr-noise-cross-domain-transfer.md) — related
