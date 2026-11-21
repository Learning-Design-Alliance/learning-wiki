---
type: claim
title: "Prosodic features contributed a modest +3.1 F1-point improvement, validated only on the 30% voice-containing subset of interactions"
description: "Prosodic features contributed a modest +3.1 F1-point improvement, validated only on the 30% voice-containing subset of interactions"
id: prosody-modality-ablation-gain
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

# Prosodic features contributed a modest +3.1 F1-point improvement, validated only on the 30% voice-containing subset of interactions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the voice-containing subset, full multimodal fusion (85.1% accuracy, F1 0.81) exceeded the text-only variant (79.6%, 0.77), a +3.1 F1-point contribution from prosody. [→ Ben Chaabene 2025](#ben-chaabene-2025)

## Evidence

### Ben Chaabene 2025

Ben Chaabene, N.E.H., Hammami, H., Kahloul, L. (2025). Decoding Student Minds: Leveraging Conversational Agents for Psychological and Learning Analysis. arXiv preprint. [doi:10.48550/arXiv.2512.10441](https://doi.org/10.48550/arXiv.2512.10441)

`q2 · i?` · `design · r2`

Modality ablation restricted to the 30% of interactions containing voice data (Table 4): prosody-only reached 72.1% accuracy / F1 0.70 versus 85.1% / 0.81 for full fusion on that subset. The authors flag reduced sub-sample sizes for the voice-only evaluation.

> "The modality ablation confirms that prosodic features contribute a modest but consistent improvement (+3.1 F1 points) when voice data are available"

## Discussion


## Related Claims
- [The multimodal BiLSTM fusion model outperformed text-only BERT and prosody-only SVM baselines across accuracy, F1, and Cohen's Kappa](multimodal-fusion-outperforms-unimodal-baselines.md) — related
- [KG-BERT knowledge-graph augmentation added +5.6 F1 points over Falcon-7B alone within the same fusion architecture](kg-bert-ablation-gain.md) — related
