---
type: claim
title: Supervised ML/DL Bloom question classifiers trained on one dataset drop substantially in weighted F1 when tested on unseen datasets
description: Supervised ML/DL Bloom question classifiers trained on one dataset drop substantially in weighted F1 when tested on unseen datasets
id: supervised-bloom-classifiers-degrade-cross-dataset
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: abdolali-faraji-2026
    resource: "https://doi.org/10.48550/arxiv.2606.13684"
    title: "Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók. (2026). Cross-Dataset Bloom Question Classification: Supervised Models and Prompted LLMs. https://arxiv.org/abs/2606.13684 [doi:10.48550/arxiv.2606.13684](https://doi.org/10.48550/arxiv.2606.13684)"
    author: Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: abdolali-faraji-2026-2
    resource: "https://arxiv.org/abs/2606.13684"
    title: "Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók. (2026). Cross-Dataset Bloom Question Classification: Supervised Models and Prompted LLMs. https://arxiv.org/abs/2606.13684"
    author: Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Supervised ML/DL Bloom question classifiers trained on one dataset drop substantially in weighted F1 when tested on unseen datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` TFPOSIDF+SVM cross-dataset weighted F1 drops by an average of 0.25 relative to within-dataset test scores. [→ Abdolali Faraji 2026](#abdolali-faraji-2026)
`q2 i?` Fine-tuned BERT cross-dataset weighted F1 drops by an average of 0.28 relative to within-dataset test scores. [→ Abdolali Faraji 2026 (2)](#abdolali-faraji-2026-2)

## Evidence

### Abdolali Faraji 2026

Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók. (2026). Cross-Dataset Bloom Question Classification: Supervised Models and Prompted LLMs. https://arxiv.org/abs/2606.13684 [doi:10.48550/arxiv.2606.13684](https://doi.org/10.48550/arxiv.2606.13684)

`q2 · i?` · `causal · r2`

Cross-dataset generalization evaluation (RQ1) over five Bloom-annotated datasets, each serving once as training source with an 80/20 split. The SVM model's unseen-dataset weighted F1 scores ranged 0.40–0.70, an "average of 0.25" drop.

> "For TFPOSIDF+SVM, test scores range from 0.68 to 0.82 depending on the training dataset, but performance decreases on unseen datasets by an average of 0.25, ranging between 0.40 and 0.70."

### Abdolali Faraji 2026 (2)

Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók. (2026). Cross-Dataset Bloom Question Classification: Supervised Models and Prompted LLMs. https://arxiv.org/abs/2606.13684

`q2 · i?` · `design · r2`

Same cross-dataset evaluation protocol (RQ1); the fine-tuned BERT reference model's weighted F1 fell from 0.76–0.91 within-dataset to 0.31–0.76 on unseen datasets, an average drop of 0.28.

> "Similarly, fine-tuned BERT achieves test scores between 0.76 and 0.91, which drop on average by 0.28 when evaluated on other datasets, ranging from 0.31 to 0.76."

## Studies bearing on this claim

<!-- synthesis:start -->
*Can a model tag questions by Bloom level reliably enough to use the tags in a course?* This table gathers the studies behind this claim and the 7 narrower claims that bear on it: **3 distinct studies** (2 causal, 1 design), `q2`, 0 of 3 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Abdolali Faraji 2026](https://doi.org/10.48550/arxiv.2606.13684) | q2 · causal · r2 | i? | this claim; [LLMs are more stable than supervised models across dataset shifts, though they do not surp](llms-more-stable-cross-dataset-than-supervised.md) (qualifies); [In-context examples improve LLM Bloom classification: three-shot and ten-shot prompting sc](in-context-examples-improve-bloom-classification.md) (qualifies) |
| [Michael Lawrence Castanares 2026](https://doi.org/10.48550/arxiv.2609.27749) | q2 · design · r2 | i? | [Feature-based ML Bloom classifiers trained on IID data degrade sharply on out-of-distribut](ml-bloom-classifiers-degrade-ood-aeq.md) (supports); [Model accuracy on Bloom classification drops with question text length, with LLMs degradin](bloom-signal-dilution-with-text-length.md) (supports); [LLMs show robust zero- and few-shot Bloom classification of OOD AI-assisted questions comp](llms-robust-ood-bloom-classification.md) (qualifies); [Model retraining on labeled OOD data provides the largest improvement in Bloom classificat](model-retraining-largest-ood-improvement.md) (qualifies) |
| [social-fgp](https://doi.org/10.1145/3770854.3785686) | q2 · causal · r1 | i? | [The Bloom-driven framework generalizes to social-science questions, with automated rubrics](social-science-generalization-human-agreement.md) (supports) |
<!-- synthesis:end -->

## Discussion


## Related Claims
- [LLMs are more stable than supervised models across dataset shifts, though they do not surpass within-dataset fine-tuned performance](llms-more-stable-cross-dataset-than-supervised.md) — related
- [Transfer between two specific datasets is asymmetric: Sangodiah-trained models transfer unusually well to Gani questions](sangodiah-gani-asymmetric-transfer.md) — a narrower finding that bears on this claim
- [Feature-based ML Bloom classifiers trained on IID data degrade sharply on out-of-distribution AI-assisted questions](ml-bloom-classifiers-degrade-ood-aeq.md) — related
- [The framework is robust to 15% ASR transcription noise and retains 99.6% of its ICS under zero-shot cross-domain transfer to EdNet-Math](framework-robust-asr-noise-cross-domain-transfer.md) — related
- [Offloading is decodable from metacognitive monitoring and control brain processes](neural-metacognitive-decoding-offloading.md) — related
- [Grading skill transfers across exams: an adapter fine-tuned on one exam improves grading on the unseen other, though transfer stops short of in-domain performance](grading-skill-transfers-across-exams.md) — related
- [In zero-shot evaluation, GPT-4's multi-label classification results were similar to what might be expected of fine-tuned classifiers, with SetFit and GPT-3.5 showing contrasting precision/recall patterns](gpt4-zero-shot-comparable-finetuned-classifiers.md) — related
- [A fine-tuned SBERT Transformer SAG model for German approximates but does not beat hand-crafted feature-based models in unseen-question evaluation](german-transformer-sag-approximates-feature-models.md) — a narrower finding that bears on this claim
- [Science readability models trained on context-specific corpora fail to generalize to unseen test corpora in all three languages](science-ara-models-poor-generalization-unseen-corpora.md) — a narrower finding that bears on this claim
- [SAG model prediction performance varies widely across corpora even with the same architecture, so benchmark results cannot predict performance on new data sets](sag-performance-varies-across-corpora.md) — a narrower finding that bears on this claim
- [Few-shot LLM approaches outperform standalone supervised ML approaches, yet hand-crafted rules remain relevant](few-shot-llm-outperforms-ml-hcr-relevant.md) — related
