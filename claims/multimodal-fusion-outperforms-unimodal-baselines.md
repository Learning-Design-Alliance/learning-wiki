---
type: claim
title: "The multimodal BiLSTM fusion model outperformed text-only BERT and prosody-only SVM baselines across accuracy, F1, and Cohen's Kappa"
description: "The multimodal BiLSTM fusion model outperformed text-only BERT and prosody-only SVM baselines across accuracy, F1, and Cohen's Kappa"
id: multimodal-fusion-outperforms-unimodal-baselines
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

# The multimodal BiLSTM fusion model outperformed text-only BERT and prosody-only SVM baselines across accuracy, F1, and Cohen's Kappa

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The multimodal fusion model achieved 86.7% accuracy, F1 = 0.84, and κ = 0.78, exceeding both unimodal baselines on all metrics. [→ Ben Chaabene 2025](#ben-chaabene-2025)

## Evidence

### Ben Chaabene 2025

Ben Chaabene, N.E.H., Hammami, H., Kahloul, L. (2025). Decoding Student Minds: Leveraging Conversational Agents for Psychological and Learning Analysis. arXiv preprint. [doi:10.48550/arXiv.2512.10441](https://doi.org/10.48550/arXiv.2512.10441)

`q2 · i?` · `design · r2`

Model evaluation on the study-specific dataset of 720 interactions from 45 students: multimodal fusion (86.7% accuracy, F1 0.84, κ 0.78) versus text-only BERT (78.4%, 0.76, 0.69) and prosody-only SVM (72.1%, 0.70, 0.61); the text reports a "+8.4% over BERT" F1 gain. No effect size is printed for this comparison.

> "As summarized in Table 5, the multimodal architecture outperformed both baselines across all metrics. The gain in F1-score (+8.4% over BERT) confirms that integrating semantic and prosodic features enhances the precision-recall balance"

## Discussion


## Related Claims
- [KG-BERT knowledge-graph augmentation added +5.6 F1 points over Falcon-7B alone within the same fusion architecture](kg-bert-ablation-gain.md) — related
- [Fusing transformer text classifiers with a linguistic-feature neural network significantly outperforms unimodal models for UK Key Stage classification, with ELECTRA + ANN reaching F1 = 0.996](multimodal-fusion-outperforms-unimodal-key-stage-classification.md) — a broader claim this one bears on
- [Review-reported model comparisons: a BiLSTM-based model significantly outperformed all baselines (Qiu et al.), and BERT outperformed a semantic-similarity baseline (Yeung et al.)](neural-models-outperform-baselines-review.md) — related
- [BERT-FYBIO, which uses post text plus annotated reading context, significantly outperforms a Bi-LSTM baseline for emoji prediction](bert-fybio-outperforms-bilstm.md) — related
- [In the Reason dimension, the IndoBERT–SVM baseline outperformed all BiLSTM variants, achieving QWK 0.332](svm-outperforms-bilstm-reason-dimension.md) — related
- [Prosodic features contributed a modest +3.1 F1-point improvement, validated only on the 30% voice-containing subset of interactions](prosody-modality-ablation-gain.md) — related
