---
type: claim
title: Under Chain-of-Thought prompting, higher Bloom-level classification accuracy correlates with lower category consistency in generated questions
description: Under Chain-of-Thought prompting, higher Bloom-level classification accuracy correlates with lower category consistency in generated questions
id: negative-correlation-classification-catcons
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: negative-corr
    title: negative-corr
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Under Chain-of-Thought prompting, higher Bloom-level classification accuracy correlates with lower category consistency in generated questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Models with higher classification accuracy tend to exhibit lower category consistency under CoT prompting, an inverse relationship the authors attribute to a generation-understanding asymmetry. [→ negative-corr](#negative-corr)

## Evidence

### negative-corr

Xiaolong Wang, Zhe Zhao, Song Lai, Chaoli Zhang, Zijie Geng, Yu Tong, Ye Wei, and Qingsong Wen. 2026. From Memorization to Creation: Evaluating the Cognitive Depth of LLM-Generated Educational Questions. Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.1 (KDD '26). https://doi.org/10.1145/3770854.3785686

`q2 · i?` · `associational · r1`

Interpretability analysis (RQ4) correlating Bloom-level classification accuracy with category consistency across the six evaluated models, quantified in Figure 5(a). The paper observes "a clear negative correlation" between the two.

> "Counterintuitively, we observe a clear negative correlation: models with higher classification accuracy tend to exhibit lower category consistency."

## Discussion


## Related Claims
- [Fine-grained prompting improves Bloom-level category consistency and knowledge coverage of generated questions in the computer science domain](fgp-improves-catcons-knowcov.md) — related
- [LLMs exhibit an inherent abstraction bias, consistently generating questions at higher-than-intended cognitive levels regardless of prompting strategy](llm-abstraction-bias-higher-order-overproduction.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
- [Higher knowledge-identification accuracy is associated with improved knowledge coverage in LLM-generated questions under Chain-of-Thought prompting](positive-correlation-identification-coverage.md) — related
- [In-context examples improve LLM Bloom classification: three-shot and ten-shot prompting outperform zero-shot across datasets](in-context-examples-improve-bloom-classification.md) — related
- [Chain-of-Thought rationale quality shows no direct correlation with the accuracy of simulated student responses](cot-rationale-quality-no-correlation-simulated-accuracy.md) — related
- [Cognitive leap is the most prevalent deviation pattern of LLM-generated questions, and fine-grained prompting amplifies upward shifts while suppressing cognitive regression](cogleap-dominant-fgp-suppresses-regression.md) — related
- [Chain-of-thought prompting outperforms Self-Ask under zero-shot conditions](cot-outperforms-self-ask-zero-shot.md) — related
