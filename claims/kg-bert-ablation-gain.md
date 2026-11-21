---
type: claim
title: KG-BERT knowledge-graph augmentation added +5.6 F1 points over Falcon-7B alone within the same fusion architecture
description: KG-BERT knowledge-graph augmentation added +5.6 F1 points over Falcon-7B alone within the same fusion architecture
id: kg-bert-ablation-gain
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: ben-chaabene-2025
    resource: "https://doi.org/10.48550/arXiv.2512.10441"
    title: "Ben Chaabene, N.E.H., Hammami, H., Kahloul, L. (2025). Decoding Student Minds: Leveraging Conversational Agents for Psychological and Learning Analysis. arXiv preprint. [doi:10.48550/arXiv.2512.10441](https://doi.org/10.48550/arXiv.2512.10441)"
    author: Ben Chaabene, N.E.H., Hammami, H., Kahloul, L.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# KG-BERT knowledge-graph augmentation added +5.6 F1 points over Falcon-7B alone within the same fusion architecture

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Replacing KG-BERT-augmented embeddings with Falcon-7B-only embeddings lowered accuracy from 86.7% to 81.3% and F1 from 0.84 to 0.78, a +5.6 F1-point gain attributable to the knowledge graph. [→ Ben Chaabene 2025](#ben-chaabene-2025)

## Evidence

### Ben Chaabene 2025

Ben Chaabene, N.E.H., Hammami, H., Kahloul, L. (2025). Decoding Student Minds: Leveraging Conversational Agents for Psychological and Learning Analysis. arXiv preprint. [doi:10.48550/arXiv.2512.10441](https://doi.org/10.48550/arXiv.2512.10441)

`q2 · i?` · `design · r2`

KG-BERT ablation within the 45-student cohort (Table 4): full model 86.7% accuracy / F1 0.84 versus Falcon-7B-only 81.3% / 0.78, holding all other components fixed. The authors call the results "indicative rather than conclusive" given the small sample.

> "the KG-BERT ablation shows a larger, more consistent gain (+5.6 F1 points) attributable to knowledge-graph augmentation over Falcon-7B alone, supporting-though on a still-limited sample-the claim that KG-BERT contributes beyond the base LLM"

## Discussion


## Related Claims
- [The multimodal BiLSTM fusion model outperformed text-only BERT and prosody-only SVM baselines across accuracy, F1, and Cohen's Kappa](multimodal-fusion-outperforms-unimodal-baselines.md) — related
- [Prosodic features contributed a modest +3.1 F1-point improvement, validated only on the 30% voice-containing subset of interactions](prosody-modality-ablation-gain.md) — related
