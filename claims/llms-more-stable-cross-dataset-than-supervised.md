---
type: claim
title: LLMs are more stable than supervised models across dataset shifts, though they do not surpass within-dataset fine-tuned performance
description: LLMs are more stable than supervised models across dataset shifts, though they do not surpass within-dataset fine-tuned performance
id: llms-more-stable-cross-dataset-than-supervised
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: abdolali-faraji-2026
    resource: "https://arxiv.org/abs/2606.13684"
    title: "Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók. (2026). Cross-Dataset Bloom Question Classification: Supervised Models and Prompted LLMs. https://arxiv.org/abs/2606.13684"
    author: Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: abdolali-faraji-2026-2
    resource: "https://arxiv.org/abs/2606.13684"
    title: "Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók. (2026). Cross-Dataset Bloom Question Classification: Supervised Models and Prompted LLMs. https://arxiv.org/abs/2606.13684"
    author: Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# LLMs are more stable than supervised models across dataset shifts, though they do not surpass within-dataset fine-tuned performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` LLM performance shows substantially less sensitivity to dataset shifts than the supervised models evaluated in RQ1. [→ Abdolali Faraji 2026](#abdolali-faraji-2026)
`q2 i?` GPT-5 consistently outperforms GPT-5-mini, but the gap is modest (average weighted F1 only 0.03 lower for the mini model). [→ Abdolali Faraji 2026 (2)](#abdolali-faraji-2026-2)

## Evidence

### Abdolali Faraji 2026

Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók. (2026). Cross-Dataset Bloom Question Classification: Supervised Models and Prompted LLMs. https://arxiv.org/abs/2606.13684

`q2 · i?` · `design · r2`

RQ2 discussion comparing Table 3 LLM results with Table 2 supervised results: LLMs did not surpass within-dataset fine-tuned performance but were comparatively stable across diverse datasets.

> "Compared to the supervised models evaluated in RQ1, LLM performance shows substantially less sensitivity to dataset shifts, indicating stronger cross-dataset robustness."

### Abdolali Faraji 2026 (2)

Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók. (2026). Cross-Dataset Bloom Question Classification: Supervised Models and Prompted LLMs. https://arxiv.org/abs/2606.13684

`q2 · i?` · `causal · r2`

RQ2 model-level comparison across all prompting strategies and datasets (Table 3): GPT-5 beat GPT-5-mini consistently, with the mini model averaging weighted F1 only 0.03 lower.

> "GPT-5 consistently performs better than GPT-5-mini; however, the performance gap remains modest, making GPT-5-mini a viable alternative when computational efficiency or cost is a concern, with an average weighted F1-score only 0.03 lower."

## Discussion


## Related Claims
- [EchoPrompt maintains cross-proxy robustness, averaging 87.06% AUROC across seven proxy models and outperforming DNA-DetectLLM by 2.70% AUROC on average](echoprompt-cross-proxy-robustness.md) — related
- [Supervised ML/DL Bloom question classifiers trained on one dataset drop substantially in weighted F1 when tested on unseen datasets](supervised-bloom-classifiers-degrade-cross-dataset.md) — related
