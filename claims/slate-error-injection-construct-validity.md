---
type: claim
title: Error injection validation shows each SLATE dimension selectively degrades under its targeted corruption, and answer leakage inflates posttest scores while destroying far-transfer performance
description: Error injection validation shows each SLATE dimension selectively degrades under its targeted corruption, and answer leakage inflates posttest scores while destroying far-transfer performance
id: slate-error-injection-construct-validity
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: jingzhuo-wu-2026
    resource: "https://doi.org/10.48550/arXiv.2609.06212"
    title: "Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang. (2026). SLATE: Are AI-Generated Slides Educationally Effective? A Benchmark for Language Teaching Quality and Learner Knowledge Acquisition. arXiv preprint arXiv:2609.06212. [doi:10.48550/arXiv.2609.06212](https://doi.org/10.48550/arXiv.2609.06212)"
    author: Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: jingzhuo-wu-2026-2
    resource: "https://doi.org/10.48550/arXiv.2609.06212"
    title: "Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang. (2026). SLATE: Are AI-Generated Slides Educationally Effective? A Benchmark for Language Teaching Quality and Learner Knowledge Acquisition. arXiv preprint arXiv:2609.06212. [doi:10.48550/arXiv.2609.06212](https://doi.org/10.48550/arXiv.2609.06212)"
    author: Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Error injection validation shows each SLATE dimension selectively degrades under its targeted corruption, and answer leakage inflates posttest scores while destroying far-transfer performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Knowledge corruption drops D1 by 4.5 points while leaving D2/D3 nearly intact; pedagogical corruption drops D2 by 4.4 points; visual corruption drops D3 by 5.3 points. [→ Jingzhuo Wu 2026](#jingzhuo-wu-2026)
`q2 i?` Assessment-integrity corruption inflates posttest scores by 0.5 points while destroying far-transfer performance (−5.0 points), showing answer leakage creates artificial gains without genuine learning. [→ Jingzhuo Wu 2026 (2)](#jingzhuo-wu-2026-2)

## Evidence

### Jingzhuo Wu 2026

Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang. (2026). SLATE: Are AI-Generated Slides Educationally Effective? A Benchmark for Language Teaching Quality and Learner Knowledge Acquisition. arXiv preprint arXiv:2609.06212. [doi:10.48550/arXiv.2609.06212](https://doi.org/10.48550/arXiv.2609.06212)

`q2 · i?` · `causal · r2`

Controlled error-injection study (§5.2, Appendix E) corrupting strong reference decks along four failure families; each perturbation selectively degrades its target dimension, supporting "interpretable instructional properties rather than surface fluency."

> "Each perturbation degrades its target dimen- sion most severely: knowledge corruption drops D1 by 4.5 points (on a 10-point scale) while leaving D2/D3 nearly intact; pedagogical corruption drops D2 by 4.4 points; and visual corruption drops D3 by 5.3 points."

### Jingzhuo Wu 2026 (2)

Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang. (2026). SLATE: Are AI-Generated Slides Educationally Effective? A Benchmark for Language Teaching Quality and Learner Knowledge Acquisition. arXiv preprint arXiv:2609.06212. [doi:10.48550/arXiv.2609.06212](https://doi.org/10.48550/arXiv.2609.06212)

`q2 · i?` · `design · r2`

Same error-injection study: the assessment-integrity family is diagnostically distinct, inflating posttest by "0.5 points" while far transfer falls "−5.0 points", so leakage produces artificial gains.

> "Assessment-integrity corruption is diagnostically distinct: it inflates posttest scores by 0.5 points while destroying far-transfer perfor- mance (−5.0 points), confirming that answer leak- age creates artificial gains without genuine learning."

## Discussion


## Related Claims
- [Across 10 frontier slide-generation systems, pedagogical design (D2) correlates more strongly with learning gain (ρ=0.72) than content validity (D1, ρ=0.38)](slate-d2-pedagogical-design-gain-correlation.md) — related
- [Temporal leakage from shuffled neighboring epochs inflates EEG familiarity classification, with peak weighted F1 dropping from 0.9853 (CNN, stratified) to 0.6038 (CNN, Group K-Fold)](temporal-leakage-inflates-eeg-familiarity-classification.md) — related
- [KC-sequence expansion causes label leakage that degrades KT model performance, shown by sharp drops on a correlated-KC dataset](kt-label-leakage-degrades-correlated-kc-performance.md) — related
- [False reference solutions degrade LLM absolute marking accuracy but leave rank-order agreement largely intact](false-solutions-degrade-accuracy-not-ranking.md) — related
