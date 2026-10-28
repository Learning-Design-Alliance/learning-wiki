---
type: claim
title: Feature-based ML Bloom classifiers trained on IID data degrade sharply on out-of-distribution AI-assisted questions
description: Feature-based ML Bloom classifiers trained on IID data degrade sharply on out-of-distribution AI-assisted questions
id: ml-bloom-classifiers-degrade-ood-aeq
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: michael-lawrence-castanares-2026
    resource: "https://doi.org/10.48550/arxiv.2609.27749"
    title: "Michael Lawrence Castanares, Princess Ventures, and Allan Tan. (2026). Evaluation of Pre-trained Models for Pedagogical Assessment of NovelAI-Assisted Educational Questions. Preprint. https://arxiv.org/abs/2609.27749 [doi:10.48550/arxiv.2609.27749](https://doi.org/10.48550/arxiv.2609.27749)"
    author: Michael Lawrence Castanares, Princess Ventures, and Allan Tan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Feature-based ML Bloom classifiers trained on IID data degrade sharply on out-of-distribution AI-assisted questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` TFPOS-IDF ML models reach macro F1 around 0.88 on IID data but drop to 0.48 (Scaria) and 0.18-0.20 (AF) on OOD AI-generated questions. [→ Michael Lawrence Castanares 2026](#michael-lawrence-castanares-2026)

## Evidence

### Michael Lawrence Castanares 2026

Michael Lawrence Castanares, Princess Ventures, and Allan Tan. (2026). Evaluation of Pre-trained Models for Pedagogical Assessment of NovelAI-Assisted Educational Questions. Preprint. https://arxiv.org/abs/2609.27749 [doi:10.48550/arxiv.2609.27749](https://doi.org/10.48550/arxiv.2609.27749)

`q2 · i?` · `design · r2`

Numerical evaluation (5-fold cross-validation on IID-Lau, transfer to OOD Scaria and AF datasets) of TFPOS-IDF ML classifiers. XGBoost fell from "0.88" IID to "0.48±0.02" and "0.18±0.02" OOD; no effect sizes are printed.

> "With TFPOS-IDF as features, all models show high F1-score ( 0.88) with the IID datasets, particularly XGBoost. However, their performance decreased with the OOD dataset to 0.48±0.02 (Scaria, XGBoost) and 0.18±0.02 (AF, XGBoost)."

## Discussion


## Related Claims
- [LLMs show robust zero- and few-shot Bloom classification of OOD AI-assisted questions compared with ML and BERT models](llms-robust-ood-bloom-classification.md) — related
- [Text splicing into single sentences improves ML and BERT Bloom classification on the Scaria OOD dataset](text-splicing-improves-ood-bloom-classification.md) — related
- [Model accuracy on Bloom classification drops with question text length, with LLMs degrading least](bloom-signal-dilution-with-text-length.md) — related
- [AI-generated OOD question datasets are longer, syntactically deeper, and overlap less with Bloom trigger verbs than human-curated IID data](ood-aeq-textual-characteristics-differ-iid.md) — related
- [Appending learning objectives to questions improves Bloom classification on the AF dataset](learning-objectives-anchor-bloom-classification.md) — related
- [Model retraining on labeled OOD data provides the largest improvement in Bloom classification across models and datasets](model-retraining-largest-ood-improvement.md) — related
- [Transfer between two specific datasets is asymmetric: Sangodiah-trained models transfer unusually well to Gani questions](sangodiah-gani-asymmetric-transfer.md) — related
- [Supervised ML/DL Bloom question classifiers trained on one dataset drop substantially in weighted F1 when tested on unseen datasets](supervised-bloom-classifiers-degrade-cross-dataset.md) — related
- [LLM-assigned difficulty labels fail to predict empirical item difficulty in classroom retrieval practice (ρ=0.06), as do co-generated Bloom levels (ρ=0.02)](llm-difficulty-labels-fail-to-predict-empirical-item-difficulty.md) — related
- [Retrained BERT relies on high-impact nouns, verbs, and adjectives for correct predictions, but this reliance is muted on the AF dataset](lime-pos-reliance-varies-by-dataset.md) — related
- [Attribution analysis identifies interpretable input features for BERT's classification decisions, including subjunctive verbs in alternatives and appraisal words in evaluation](attribution-analysis-identifies-bert-classification-features.md) — related
