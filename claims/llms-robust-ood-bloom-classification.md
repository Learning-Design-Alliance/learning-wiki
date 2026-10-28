---
type: claim
title: LLMs show robust zero- and few-shot Bloom classification of OOD AI-assisted questions compared with ML and BERT models
description: LLMs show robust zero- and few-shot Bloom classification of OOD AI-assisted questions compared with ML and BERT models
id: llms-robust-ood-bloom-classification
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

# LLMs show robust zero- and few-shot Bloom classification of OOD AI-assisted questions compared with ML and BERT models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-4.1 and Gemini Flash 3.1 achieved OOD macro F1-scores from 0.41 to 0.79, the strongest OOD baseline performance. [→ Michael Lawrence Castanares 2026](#michael-lawrence-castanares-2026)

## Evidence

### Michael Lawrence Castanares 2026

Michael Lawrence Castanares, Princess Ventures, and Allan Tan. (2026). Evaluation of Pre-trained Models for Pedagogical Assessment of NovelAI-Assisted Educational Questions. Preprint. https://arxiv.org/abs/2609.27749 [doi:10.48550/arxiv.2609.27749](https://doi.org/10.48550/arxiv.2609.27749)

`q2 · i?` · `design · r2`

Zero- and few-shot prompting evaluation of GPT-4.1 and Gemini Flash 3.1 on the OOD Scaria and AF datasets, reported in Results Section 5.2; F1-scores ranged "0.41 to 0.79" with no effect sizes printed.

> "LLMs (GPT4.1 and Gemini-Flash 3.1 lite) showed robust classification performance with the OOD datasets, F1-scores from 0.41 to 0.79."

## Discussion

## Related Claims

- [Supervised ML/DL Bloom question classifiers trained on one dataset drop substantially in weighted F1 when tested on unseen datasets](supervised-bloom-classifiers-degrade-cross-dataset.md) — the general claim this finding bears on, with the studies behind it
- [Model accuracy on Bloom classification drops with question text length, with LLMs degrading least](bloom-signal-dilution-with-text-length.md) — related
- [Text splicing into single sentences improves ML and BERT Bloom classification on the Scaria OOD dataset](text-splicing-improves-ood-bloom-classification.md) — related
- [Feature-based ML Bloom classifiers trained on IID data degrade sharply on out-of-distribution AI-assisted questions](ml-bloom-classifiers-degrade-ood-aeq.md) — related
- [Model retraining on labeled OOD data provides the largest improvement in Bloom classification across models and datasets](model-retraining-largest-ood-improvement.md) — related
- [Appending learning objectives to questions improves Bloom classification on the AF dataset](learning-objectives-anchor-bloom-classification.md) — related
- [In-context examples improve LLM Bloom classification: three-shot and ten-shot prompting outperform zero-shot across datasets](in-context-examples-improve-bloom-classification.md) — related
- [The selected-questions-verbs prompting strategy yields the strongest LLM Bloom classification, reaching weighted F1 up to 0.84](selected-questions-verbs-best-prompt.md) — related
- [An LLM-based question-specificity classifier reached .830 knowledge and .829 scaffold accuracy without fine-tuning](question-specificity-classifier-accuracy.md) — related
- Zero-shot heuristic use of the pre-trained generative model shows stable, steadily increasing performance across pre-training, suggesting generative pre-training learns task-relevant functionality without fine-tuning — related
- [Retrained BERT relies on high-impact nouns, verbs, and adjectives for correct predictions, but this reliance is muted on the AF dataset](lime-pos-reliance-varies-by-dataset.md) — related
- [Dual-Lens attention aligns with expert pedagogical focus, allocating most weight to Bloom's taxonomy verbs and problem-solving steps](dual-lens-attention-aligns-expert-pedagogical-focus.md) — related
- [In zero-shot evaluation, GPT-4's multi-label classification results were similar to what might be expected of fine-tuned classifiers, with SetFit and GPT-3.5 showing contrasting precision/recall patterns](gpt4-zero-shot-comparable-finetuned-classifiers.md) — related
- [Attribution analysis identifies interpretable input features for BERT's classification decisions, including subjunctive verbs in alternatives and appraisal words in evaluation](attribution-analysis-identifies-bert-classification-features.md) — related
- [Zero-shot GPT-4 remains effective on imbalanced rare labels because its performance does not depend on label frequency in training data, unlike fine-tuned models.](zero-shot-gpt4-effective-on-imbalanced-rare-labels.md) — related
