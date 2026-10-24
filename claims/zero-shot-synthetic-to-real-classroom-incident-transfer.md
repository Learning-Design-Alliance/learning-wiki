---
type: claim
title: "Models trained on synthetic classroom incident data transfer zero-shot to real-world footage, with the proposed method best at 63.41% though a synthetic-to-real domain gap remains"
description: "Models trained on synthetic classroom incident data transfer zero-shot to real-world footage, with the proposed method best at 63.41% though a synthetic-to-real domain gap remains"
id: zero-shot-synthetic-to-real-classroom-incident-transfer
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
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

# Models trained on synthetic classroom incident data transfer zero-shot to real-world footage, with the proposed method best at 63.41% though a synthetic-to-real domain gap remains

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In zero-shot synthetic-to-real transfer, the proposed method obtains the best real-world accuracy of 63.41%, outperforming MSG3D by 4.18 percentage points and other baselines by larger margins. [→ Paritosh Parmar 2026](#paritosh-parmar-2026)
`q2 i?` All methods drop in accuracy from synthetic to real-world data, so synthetic data does not fully replace real-world data. [→ Paritosh Parmar 2026 (2)](#paritosh-parmar-2026-2)

## Evidence

### Paritosh Parmar 2026

Paritosh Parmar, Landy Lan, Hong Yang, Chen Yi, Chiat Pin Tay. (2026). Robust and Efficient Motion Reasoning for Privacy-Aware Classroom Incident Recognition. arXiv preprint. https://arxiv.org/abs/2608.05115 [doi:10.48550/arxiv.2608.05115](https://doi.org/10.48550/arxiv.2608.05115)

`q2 · i?` · `design · r2`

Zero-shot transfer experiment: models trained only on the synthetic set, evaluated directly on the 574-sample real-world test set without fine-tuning. The proposed method "obtains the best real-world accuracy of 63.41%"; accuracies only, no effect size.

> "However, our method obtains the best real-world accuracy of 63.41%, outperforming MSG3D, the strongest baseline in this setting, by 4.18 percentage points."

### Paritosh Parmar 2026 (2)

Paritosh Parmar, Landy Lan, Hong Yang, Chen Yi, Chiat Pin Tay. (2026). Robust and Efficient Motion Reasoning for Privacy-Aware Classroom Incident Recognition. arXiv preprint. https://arxiv.org/abs/2608.05115

`q2 · i?` · `design · r2`

Same zero-shot evaluation, reported as the authors' caveat on interpreting the transfer results: the drop from 71.78% to 63.41% "shows that a synthetic-to-real domain gap remains", so synthetic data provides a useful training signal but does not replace real data.

> "the decrease from 71.78% on synthetic data to 63.41% on real-world data shows that a synthetic-to-real domain gap remains."

## Discussion


## Related Claims

- [Classroom incident recognition is substantially harder than established general action-recognition benchmarks, with PoseC3D dropping from over 94% accuracy to 70.54%](classroom-incident-recognition-harder-than-general-benchmarks.md) — related
- [A distilled multi-order kinematic model outperforms pose-based baselines on a synthetic classroom incident dataset while using one-tenth as many parameters as PoseC3D](distilled-kinematic-model-outperforms-pose-baselines-synthetic-classroom-incidents.md) — related
- [The framework is robust to 15% ASR transcription noise and retains 99.6% of its ICS under zero-shot cross-domain transfer to EdNet-Math](framework-robust-asr-noise-cross-domain-transfer.md) — related
- [Distilling a multi-order hierarchical teacher into a smaller zeroth-order student lets the student outperform the teacher, and improves 4.1 percentage points in accuracy over STGCN++](distilled-student-outperforms-multiorder-teacher.md)
