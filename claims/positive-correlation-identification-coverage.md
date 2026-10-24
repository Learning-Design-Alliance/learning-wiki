---
type: claim
title: Higher knowledge-identification accuracy is associated with improved knowledge coverage in LLM-generated questions under Chain-of-Thought prompting
description: Higher knowledge-identification accuracy is associated with improved knowledge coverage in LLM-generated questions under Chain-of-Thought prompting
id: positive-correlation-identification-coverage
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: positive-corr
    title: positive-corr
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Higher knowledge-identification accuracy is associated with improved knowledge coverage in LLM-generated questions under Chain-of-Thought prompting

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Knowledge identification accuracy correlates positively with knowledge coverage; GLM-4-9B (84.5%), Qwen2.5-7B (83.8%), and Spark Max (81.6%) achieve the highest identification accuracies with corresponding coverage rates of 85.45%, 83.98%, and 78.03%. [→ positive-corr](#positive-corr)

## Evidence

### positive-corr

Xiaolong Wang, Zhe Zhao, Song Lai, Chaoli Zhang, Zijie Geng, Yu Tong, Ye Wei, and Qingsong Wen. 2026. From Memorization to Creation: Evaluating the Cognitive Depth of LLM-Generated Educational Questions. Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.1 (KDD '26). https://doi.org/10.1145/3770854.3785686

`q2 · i?` · `associational · r1`

Interpretability analysis (RQ5) relating knowledge-identification accuracy to knowledge coverage across models under CoT prompting, shown in Figures 4 and 5(b). The paper reports "a strong positive correlation".

> "There is a strong positive correlation: higher knowledge identification accuracy is associated with improved knowledge coverage."

## Discussion


## Related Claims
- [Under Chain-of-Thought prompting, higher Bloom-level classification accuracy correlates with lower category consistency in generated questions](negative-correlation-classification-catcons.md) — related
- [Fine-grained prompting improves Bloom-level category consistency and knowledge coverage of generated questions in the computer science domain](fgp-improves-catcons-knowcov.md) — related
- [Chain-of-Thought rationale quality shows no direct correlation with the accuracy of simulated student responses](cot-rationale-quality-no-correlation-simulated-accuracy.md) — related
