---
type: claim
title: Distilling a multi-order hierarchical teacher into a smaller zeroth-order student lets the student outperform the teacher, and improves 4.1 percentage points in accuracy over STGCN++
description: Distilling a multi-order hierarchical teacher into a smaller zeroth-order student lets the student outperform the teacher, and improves 4.1 percentage points in accuracy over STGCN++
id: distilled-student-outperforms-multiorder-teacher
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

# Distilling a multi-order hierarchical teacher into a smaller zeroth-order student lets the student outperform the teacher, and improves 4.1 percentage points in accuracy over STGCN++

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q2`

## Subclaims
`q2 i?` In ablations, distilling the multi-order hierarchical teacher into a single zeroth-order student allows the student to outperform the teacher, and imposing the smaller-student condition further enables it to outperform the much larger hierarchical teacher. [→ Paritosh Parmar 2026](#paritosh-parmar-2026)
`q2 i?` Compared with the base STGCN++ model, the proposed method improves accuracy by 4.1 percentage points and macro-F1 by 5.2 percentage points, mainly via better recognition of kick, sit, and run. [→ Paritosh Parmar 2026 (2)](#paritosh-parmar-2026-2)

## Evidence

### Paritosh Parmar 2026

Paritosh Parmar, Landy Lan, Hong Yang, Chen Yi, Chiat Pin Tay. (2026). Robust and Efficient Motion Reasoning for Privacy-Aware Classroom Incident Recognition. arXiv preprint. https://arxiv.org/abs/2608.05115 [doi:10.48550/arxiv.2608.05115](https://doi.org/10.48550/arxiv.2608.05115)

`q2 · i?` · `design · r2`

Ablation study (Figure 8, panel 3) comparing zeroth-order teacher, multi-order hierarchical teacher, and distilled students with and without the size condition. The authors hypothesize the student internalizes multi-order motion reasoning; accuracies only, no effect size.

> "we observe that distilling a multi-order hierarchical teacher into a single zeroth-order student allows the student to outperform the teacher. Third, imposing the condition in Equation 11 further enables the student to outperform the much larger hierarchical teacher."

### Paritosh Parmar 2026 (2)

Paritosh Parmar, Landy Lan, Hong Yang, Chen Yi, Chiat Pin Tay. (2026). Robust and Efficient Motion Reasoning for Privacy-Aware Classroom Incident Recognition. arXiv preprint. https://arxiv.org/abs/2608.05115

`q2 · i?` · `design · r2`

Ablation-reported gains over the STGCN++ base model: "improves accuracy by 4.1 percentage points and macro-F1 by 5.2 percentage points", attributed in the Appendix mainly to better kick, sit, and run recognition and reduced confusion of kick and sit with the other class.

> "Furthermore, compared with the base model, STGCN++ [10], the proposed method improves accuracy by 4.1 percentage points and macro-F1 by 5.2 percentage points."

## Discussion


## Related Claims

- [A distilled multi-order kinematic model outperforms pose-based baselines on a synthetic classroom incident dataset while using one-tenth as many parameters as PoseC3D](distilled-kinematic-model-outperforms-pose-baselines-synthetic-classroom-incidents.md) — related
- [Models trained on synthetic classroom incident data transfer zero-shot to real-world footage, with the proposed method best at 63.41% though a synthetic-to-real domain gap remains](zero-shot-synthetic-to-real-classroom-incident-transfer.md)
