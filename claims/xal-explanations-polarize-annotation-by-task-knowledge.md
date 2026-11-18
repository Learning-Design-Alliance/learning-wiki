---
type: claim
title: "Local explanations polarize annotation outcomes by task knowledge: they help high-knowledge annotators label better but impair low-knowledge annotators' judgment"
description: "Local explanations polarize annotation outcomes by task knowledge: they help high-knowledge annotators label better but impair low-knowledge annotators' judgment"
id: xal-explanations-polarize-annotation-by-task-knowledge
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2021
sources:
  - id: bhavya-ghai-2021
    resource: "https://doi.org/10.1145/3432934"
    title: "Bhavya Ghai, Q. Vera Liao, Yunfeng Zhang, Rachel K. E. Bellamy, and Klaus Mueller. (2021). Explainable Active Learning (XAL): Toward AI Explanations as Interfaces for Machine Teachers. Originally published 2020. [doi:10.1145/3432934](https://doi.org/10.1145/3432934)"
    author: Bhavya Ghai, Q. Vera Liao, Yunfeng Zhang, Rachel K. E. Bellamy, and Klaus Mueller
    q: 2
    i: "?"
    kind: causal
    rigour: "?"
  - id: bhavya-ghai-2021-2
    resource: "https://doi.org/10.1145/3432934"
    title: "Bhavya Ghai, Q. Vera Liao, Yunfeng Zhang, Rachel K. E. Bellamy, and Klaus Mueller. (2021). Explainable Active Learning (XAL): Toward AI Explanations as Interfaces for Machine Teachers. Originally published 2020. [doi:10.1145/3432934](https://doi.org/10.1145/3432934)"
    author: Bhavya Ghai, Q. Vera Liao, Yunfeng Zhang, Rachel K. E. Bellamy, and Klaus Mueller
    q: 2
    i: "?"
    kind: causal
    rigour: "?"
---

# Local explanations polarize annotation outcomes by task knowledge: they help high-knowledge annotators label better but impair low-knowledge annotators' judgment

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r?` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Human labeling accuracy showed a significant XAL × Task Knowledge interaction (β = 0.67, SE = 0.29, p = 0.03), the opposite direction of hypothesis H4. [→ Bhavya Ghai 2021](#bhavya-ghai-2021)
`q2 i?` Among trials where annotators agreed with the model, explanations increased wrong agreement for low task knowledge annotators (XAL × Task Knowledge, β = −0.89, SE = 0.45, p = 0.05). [→ Bhavya Ghai 2021 (2)](#bhavya-ghai-2021-2)

## Evidence

### Bhavya Ghai 2021

Bhavya Ghai, Q. Vera Liao, Yunfeng Zhang, Rachel K. E. Bellamy, and Klaus Mueller. (2021). Explainable Active Learning (XAL): Toward AI Explanations as Interfaces for Machine Teachers. Originally published 2020. [doi:10.1145/3432934](https://doi.org/10.1145/3432934)

`q2 · i?` · `causal · r?`

Analysis of human accuracy (percentage of labels consistent with ground truth) in the crowdsourced AL experiment, plotted in Figure 3 after a median split on task knowledge. The regression, with CL as reference, found a significant positive XAL × Task Knowledge interaction (β = 0.67, SE = 0.29, p = 0.03).

> "While explanations helped those with high task knowledge to provide better labels, it impaired the judgment of those with low task knowledge."

### Bhavya Ghai 2021 (2)

Bhavya Ghai, Q. Vera Liao, Yunfeng Zhang, Rachel K. E. Bellamy, and Klaus Mueller. (2021). Explainable Active Learning (XAL): Toward AI Explanations as Interfaces for Machine Teachers. Originally published 2020. [doi:10.1145/3432934](https://doi.org/10.1145/3432934)

`q2 · i?` · `causal · r?`

Zoom-in analysis of trials where participants agreed with model predictions, measuring the percentage of wrong agreement inconsistent with ground truth (Figure 4). The article interprets this as an "anchoring effect" on those with low task knowledge; no such effect was found for incorrect disagreement.

> "We found a significant interaction between XAL and Task Knowledge, using CL as a reference level (β =−0.89, SE = 0.45, p = 0.05)."

## Discussion


## Related Claims
- [Local explanations in active learning calibrate annotators' trust in deploying the model across learning stages, lowering trust in an early-stage model and raising it for a late-stage model](xal-explanations-calibrate-trust-across-learning-stages.md) — related
- [Explanations reduce annotator satisfaction only for those with low Need for Cognition](xal-satisfaction-depends-on-need-for-cognition.md) — related
- [Annotators without AI experience show exceptionally high trust in an unexplained active learning model, and explanations bring their trust to an appropriate level](xal-appropriates-trust-for-ai-inexperienced-annotators.md) — related
- [Model learning outcomes after 20 queries did not differ across AL, CL, and XAL conditions; only learning stage mattered](xal-model-performance-did-not-differ-across-conditions.md) — related
