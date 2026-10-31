---
type: claim
title: "In-context examples improve LLM Bloom classification: three-shot and ten-shot prompting score at or above zero-shot on every dataset tested, and above it in most comparisons"
description: "In-context examples improve LLM Bloom classification: three-shot and ten-shot prompting score at or above zero-shot on every dataset tested, and above it in most comparisons"
id: in-context-examples-improve-bloom-classification
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-10-31
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
---

# In-context examples improve LLM Bloom classification: three-shot and ten-shot prompting score at or above zero-shot on every dataset tested, and above it in most comparisons

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-31 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across five datasets and two models (GPT-5, GPT-5-mini), three-shot and ten-shot prompting scored higher weighted F1 than zero-shot in 16 of 20 comparisons and tied it in the other four (e.g., GPT-5 on Gani: 0.75 for zero-, three- and ten-shot); zero-shot still yields reasonable performance. [→ Abdolali Faraji 2026](#abdolali-faraji-2026)

## Evidence

### Abdolali Faraji 2026

Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók. (2026). Cross-Dataset Bloom Question Classification: Supervised Models and Prompted LLMs. https://arxiv.org/abs/2606.13684 [doi:10.48550/arxiv.2606.13684](https://doi.org/10.48550/arxiv.2606.13684)

`q2 · i?` · `causal · r2`

RQ2 evaluation across five datasets and five prompting strategies (Table 3). Few-shot prompts with examples drawn from the same dataset scored above zero-shot in most comparisons and never below it; Table 3 shows four ties (GPT-5 three-shot on Mohammed 0.76 and Gani 0.75, GPT-5 ten-shot on Gani 0.75, GPT-5-mini three-shot on Yahya 0.74), although the authors' text says few-shot outperforms zero-shot across datasets. Zero-shot GPT-5 still achieved weighted F1 around 0.75 on most datasets. No significance tests are reported.

> "Both three-shot and ten-shot prompting outperform zero-shot prompting across datasets, suggesting that additional contextual information helps to align model predictions with Bloom's cognitive levels."

## Discussion

## Related Claims

- [Supervised ML/DL Bloom question classifiers trained on one dataset drop substantially in weighted F1 when tested on unseen datasets](supervised-bloom-classifiers-degrade-cross-dataset.md) — the general claim this finding bears on, with the studies behind it
- [LLMs show robust zero- and few-shot Bloom classification of OOD AI-assisted questions compared with ML and BERT models](llms-robust-ood-bloom-classification.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
- [The selected-questions-verbs prompting strategy yields the strongest LLM Bloom classification, reaching weighted F1 up to 0.84](selected-questions-verbs-best-prompt.md) — related
- [Few-shot prompting does not improve diagnostic F1 or accuracy but reduces evidence over-attribution and false-attribution](few-shot-prompting-no-f1-gain-reduces-overattribution.md) — reports the opposite
- [Under Chain-of-Thought prompting, higher Bloom-level classification accuracy correlates with lower category consistency in generated questions](negative-correlation-classification-catcons.md) — related
- [Prompting with category information or few-shot examples yields limited improvement in distribution alignment, with zero-shot closest for most models](prompting-strategies-limited-alignment-gain.md) — related
- [Dual-Lens attention aligns with expert pedagogical focus, allocating most weight to Bloom's taxonomy verbs and problem-solving steps](dual-lens-attention-aligns-expert-pedagogical-focus.md) — related
- [Few-shot learning with increasing shots generally improves GPT-4 classification performance, with the 5-shot variant strongest for Reacting to Errors (F1 0.867, AUC 0.866, TNR 0.83)](few-shot-shots-improve-classification.md) — a narrower finding that bears on this claim
- [In detecting teacher questions with zero-shot GPT-3.5-turbo, chain-of-thought prompting had slightly higher F1 and precision than Self-Ask but slightly lower recall and balanced accuracy](cot-outperforms-self-ask-zero-shot.md) — related
- [Few-shot chain-of-thought prompting outperforms zero-shot prompting for detecting teacher questions](few-shot-cot-outperforms-zero-shot-question-detection.md) — related
- [Few-shot LLM approaches outperform standalone supervised ML approaches, yet hand-crafted rules remain relevant](few-shot-llm-outperforms-ml-hcr-relevant.md) — related
