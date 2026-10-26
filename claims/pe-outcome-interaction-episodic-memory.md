---
type: claim
title: Model-derived prediction error at encoding interacts with prediction outcome in determining subsequent recognition memory
description: Model-derived prediction error at encoding interacts with prediction outcome in determining subsequent recognition memory
id: pe-outcome-interaction-episodic-memory
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2023
sources:
  - id: francesco-pupillo-2023
    resource: "https://doi.org/10.1038/s41539-023-00166-x"
    title: "Francesco Pupillo, Javier Ortiz-Tudela, Rasmus Bruckner and Yee Lee Shing. (2023). The effect of prediction error on episodic memory encoding is modulated by the outcome of the predictions. npj Science of Learning 8:18. https://doi.org/10.1038/s41539-023-00166-x"
    author: Francesco Pupillo, Javier Ortiz-Tudela, Rasmus Bruckner and Yee Lee Shing
    q: 3
    i: 3
    kind: causal
    rigour: 2
---

# Model-derived prediction error at encoding interacts with prediction outcome in determining subsequent recognition memory

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3` · `i3` large
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person
> **Design limits** · Francesco Pupillo 2023: no comparison group (read from the study by two models, 2026-10-26)

## Subclaims
`q3 i3` The effect of prediction error on memory encoding differs depending on whether the prediction was correct or incorrect (significant PE × prediction outcome interaction). [→ Francesco Pupillo 2023](#francesco-pupillo-2023)

## Evidence

### Francesco Pupillo 2023

Francesco Pupillo, Javier Ortiz-Tudela, Rasmus Bruckner and Yee Lee Shing. (2023). The effect of prediction error on episodic memory encoding is modulated by the outcome of the predictions. npj Science of Learning 8:18. https://doi.org/10.1038/s41539-023-00166-x

`q3 · i3` · `causal · r2`

Generalized linear-mixed model on data collapsed across Experiments 1 and 2 (participants as random effects), relating model-derived PE, learning rate and prediction outcome to recognition. The interaction was significant: "χ2 ð1Þ = 26.14, p < 0.001", with OR = 6.47 in Table 2.

> "Results showed that there was a significant interaction between PE and prediction outcome, χ2 ð1Þ = 26.14, p < 0.001, while the main effects of prediction outcome, learning rate, and the interaction between prediction outcome and learning rate, were not significant, ps > 0.316."

## Discussion


## Learner Variables
- [Long-Term Memory](../learner-variables/long-term-memory.md) — outcome: instruction changes it

## Related Claims
- [Recognition performance was worse overall in Experiment 2 than Experiment 1, with no moderation of the effects of interest](experiment-main-effect-recognition.md) — related
- [Estimated individual learning rates did not affect overall recognition memory or moderate the prediction-error effects](learning-rate-no-memory-effect.md) — related
- [The overall main effect of prediction error on recognition memory, independent of prediction outcome, is not significant](overall-pe-main-effect-null.md) — related
- [For correct predictions, stronger prediction errors during encoding lead to enhanced recognition memory](pe-enhances-memory-correct-predictions.md) — related
- [For incorrect predictions, stronger prediction errors during encoding lead to impaired recognition memory](pe-impairs-memory-incorrect-predictions.md) — a narrower finding that bears on this claim
- [Choice-outcome-incorporated (signed) prediction error shows a positive relationship with recognition memory](signed-pe-positive-memory-relation.md) — related
