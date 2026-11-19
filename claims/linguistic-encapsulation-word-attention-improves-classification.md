---
type: claim
title: "Explicitly encapsulating linguistic information together with word-level attention improves BloomNet's performance significantly over RoBERTa alone"
description: "Explicitly encapsulating linguistic information together with word-level attention improves BloomNet's performance significantly over RoBERTa alone"
id: linguistic-encapsulation-word-attention-improves-classification
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: abdul-waheed-2021
    resource: "https://doi.org/10.48550/arXiv.2108.07249"
    title: "Abdul Waheed, Muskan Goyal, Nimisha Mittal, Deepak Gupta, Ashish Khanna, Moolchand Sharma. (2021). BloomNet: A Robust Transformer based model for Bloom's Learning Outcome Classification. arXiv. [doi:10.48550/arXiv.2108.07249](https://doi.org/10.48550/arXiv.2108.07249)"
    author: Abdul Waheed, Muskan Goyal, Nimisha Mittal, Deepak Gupta, Ashish Khanna, Moolchand Sharma
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Explicitly encapsulating linguistic information together with word-level attention improves BloomNet's performance significantly over RoBERTa alone

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Adding hierarchical word attention and POS/NER linguistic encapsulation to RoBERTa raised IID accuracy from 82.00 to 87.50, a statistically significant difference (p < 0.004). [→ Abdul Waheed 2021](#abdul-waheed-2021)

## Evidence

### Abdul Waheed 2021

Abdul Waheed, Muskan Goyal, Nimisha Mittal, Deepak Gupta, Ashish Khanna, Moolchand Sharma. (2021). BloomNet: A Robust Transformer based model for Bloom's Learning Outcome Classification. arXiv. [doi:10.48550/arXiv.2108.07249](https://doi.org/10.48550/arXiv.2108.07249)

`q2 · i?` · `causal · r2`

Ablation study (Table 3) reporting mean IID accuracy and Macro-F1: RoBERTa 82.00/81.67, +WA 84.11/84.10, +POS-NER 84.64/84.48, +WA+POS-NER 87.50/87.23. The authors state that "Linguistic Encapsulation along with Word level attention yields significantly better (p <0.004) results".

> "Linguistic Encap- sulation along with Word level attention yields signiﬁ- cantly better (p <0.004) results."

## Discussion


## Related Claims
- [BloomNet outperforms all considered baseline models on both IID and OOD classification of Bloom's taxonomy course learning outcomes](bloomnet-outperforms-baselines-bloom-classification.md) — related
- [Attention-based neural classifiers outperformed vanilla neural models on Bloom's taxonomy question classification](attention-models-beat-vanilla-neural-baselines.md) — related
