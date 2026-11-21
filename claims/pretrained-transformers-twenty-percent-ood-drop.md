---
type: claim
title: "All pretrained transformer models showed a significant performance drop of about 20% between IID and OOD data, and OOD performance correlated linearly with IID performance"
description: "All pretrained transformer models showed a significant performance drop of about 20% between IID and OOD data, and OOD performance correlated linearly with IID performance"
id: pretrained-transformers-twenty-percent-ood-drop
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
sources:
  - id: abdul-waheed-2021
    resource: "https://doi.org/10.48550/arXiv.2108.07249"
    title: "Abdul Waheed, Muskan Goyal, Nimisha Mittal, Deepak Gupta, Ashish Khanna, Moolchand Sharma. (2021). BloomNet: A Robust Transformer based model for Bloom's Learning Outcome Classification. arXiv. [doi:10.48550/arXiv.2108.07249](https://doi.org/10.48550/arXiv.2108.07249)"
    author: Abdul Waheed, Muskan Goyal, Nimisha Mittal, Deepak Gupta, Ashish Khanna, Moolchand Sharma
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# All pretrained transformer models showed a significant performance drop of about 20% between IID and OOD data, and OOD performance correlated linearly with IID performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Pretrained transformer-based models lost roughly 20% performance moving from IID to OOD evaluation, and models weaker on IID data were also weaker on OOD data. [→ Abdul Waheed 2021](#abdul-waheed-2021)

## Evidence

### Abdul Waheed 2021

Abdul Waheed, Muskan Goyal, Nimisha Mittal, Deepak Gupta, Ashish Khanna, Moolchand Sharma. (2021). BloomNet: A Robust Transformer based model for Bloom's Learning Outcome Classification. arXiv. [doi:10.48550/arXiv.2108.07249](https://doi.org/10.48550/arXiv.2108.07249)

`q2 · i?` · `design · r2`

OOD generalisation evaluation on Dataset2, unseen during training. The authors state that "we notice significant performance drop ( 20%)" across all pretrained transformer models, and that OOD and IID performance is linearly correlated, so weak IID models such as VDCNN and LSTM were also weak OOD.

> "but in our case we notice significant performance drop ( 20%) between IID and OOD data across all the pretrained transformer based models in our experiment which is same for other models as well"

## Discussion


## Related Claims
- [Supervised ML/DL Bloom question classifiers trained on one dataset drop substantially in weighted F1 when tested on unseen datasets](supervised-bloom-classifiers-degrade-cross-dataset.md) — a broader claim this one bears on
- [Feature-based ML Bloom classifiers trained on IID data degrade sharply on out-of-distribution AI-assisted questions](ml-bloom-classifiers-degrade-ood-aeq.md) — related
- [Model accuracy on Bloom classification drops with question text length, with LLMs degrading least](bloom-signal-dilution-with-text-length.md) — related
- [BloomNet outperforms all considered baseline models on both IID and OOD classification of Bloom's taxonomy course learning outcomes](bloomnet-outperforms-baselines-bloom-classification.md) — related
- [Parsers trained on MUDT outperform UD-trained baselines in-domain, and cross-domain transfer is asymmetric with performance degrading sharply when UD-trained models are applied to MUDT data](mudt-parsers-outperform-ud-baselines.md) — a narrower finding that bears on this claim
- [NTKT maintains stable performance on unseen cold-start questions while baselines show a significant drop between seen and unseen questions](ntkt-question-cold-start-stability.md) — a narrower finding that bears on this claim
