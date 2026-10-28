---
type: claim
title: "In zero-shot evaluation, GPT-4's multi-label classification results were similar to what might be expected of fine-tuned classifiers, with SetFit and GPT-3.5 showing contrasting precision/recall patterns"
description: "In zero-shot evaluation, GPT-4's multi-label classification results were similar to what might be expected of fine-tuned classifiers, with SetFit and GPT-3.5 showing contrasting precision/recall patterns"
id: gpt4-zero-shot-comparable-finetuned-classifiers
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: michael-j-parker-2024
    resource: "https://doi.org/10.1007/s40593-024-00414-0"
    title: "Michael J. Parker, Caitlin Anderson, Claire Stone, YeaRim Oh. (2024). A Large Language Model Approach to Educational Survey Feedback Analysis. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00414-0"
    author: Michael J. Parker, Caitlin Anderson, Claire Stone, YeaRim Oh
    q: 3
    i: "?"
    kind: design
    rigour: 2
  - id: michael-j-parker-2024-2
    resource: "https://doi.org/10.1007/s40593-024-00414-0"
    title: "Michael J. Parker, Caitlin Anderson, Claire Stone, YeaRim Oh. (2024). A Large Language Model Approach to Educational Survey Feedback Analysis. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00414-0"
    author: Michael J. Parker, Caitlin Anderson, Claire Stone, YeaRim Oh
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# In zero-shot evaluation, GPT-4's multi-label classification results were similar to what might be expected of fine-tuned classifiers, with SetFit and GPT-3.5 showing contrasting precision/recall patterns

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q3`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` Zero-shot GPT-4 results on the consensus-rows evaluation were similar to what might be expected of fine-tuned classifiers. [→ Michael J. Parker 2024](#michael-j-parker-2024)
`q3 i?` SetFit showed relatively high precision and lower recall, while GPT-3.5 followed the converse pattern. [→ Michael J. Parker 2024 (2)](#michael-j-parker-2024-2)

## Evidence

### Michael J. Parker 2024

Michael J. Parker, Caitlin Anderson, Claire Stone, YeaRim Oh. (2024). A Large Language Model Approach to Educational Survey Feedback Analysis. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00414-0

`q3 · i?` · `design · r2`

In the results section comparing LLMs with SetFit (a SentenceTransformers fine-tuning approach) on the multi-label classification task, the authors report that "the zero-shot results for GPT-4 are similar to what might be expected of fine-tuned classifiers". No specific metric values are printed in the provided text.

> "For the consensus rows evaluation, the zero-shot results for GPT-4 are similar to what might be expected of fine-tuned classifiers (Meidinger & Aßenmacher, 2021)."

### Michael J. Parker 2024 (2)

Michael J. Parker, Caitlin Anderson, Claire Stone, YeaRim Oh. (2024). A Large Language Model Approach to Educational Survey Feedback Analysis. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00414-0

`q3 · i?` · `design · r2`

The same comparison section reports differentiated model profiles: "SetFit having relatively high precision and lower recall, and GPT-3.5 following the converse pattern". No numeric precision or recall values are printed in the provided text.

> "The other models have strengths and weaknesses, with SetFit having relatively high precision and lower recall, and GPT-3.5 following the converse pattern."

## Discussion


## Related Claims
- [LLMs show robust zero- and few-shot Bloom classification of OOD AI-assisted questions compared with ML and BERT models](llms-robust-ood-bloom-classification.md) — related
- [Supervised ML/DL Bloom question classifiers trained on one dataset drop substantially in weighted F1 when tested on unseen datasets](supervised-bloom-classifiers-degrade-cross-dataset.md) — related
- [Frontier LLMs achieve the best balance between detecting misconceptions in correct-answer cases and not over-flagging correct students, while fine-tuned local models achieve under 58% TM recall](frontier-llms-best-balance-tm-detection.md) — related
- [Fine-tuned LaBSE achieves about 86.5% accuracy classifying all answers as correct or incorrect on a large multilingual dataset](finetuned-labse-86-5-percent-autograding-accuracy.md) — related
- [Zero-shot GPT-4 remains effective on imbalanced rare labels because its performance does not depend on label frequency in training data, unlike fine-tuned models.](zero-shot-gpt4-effective-on-imbalanced-rare-labels.md) — related
- [All surveyed automatic question difficulty prediction studies frame the task as supervised learning, mostly as classification of pre-defined difficulty categories](difficulty-prediction-supervised-dominant.md) — related
- [LLMs cannot effectively perform in-context learning for short answer scoring, but cross-prompt pre-finetuning substantially boosts their zero-shot performance](llm-icl-insufficient-prefinetuning-boosts-zero-shot.md) — related
- [The IRead question generation model, fine-tuned on in-text OpenStax questions, matched reference questions in human ratings and outperformed zero-shot GPT-4 on automatic metrics](iread-qg-model-evaluation-performance.md) — related
