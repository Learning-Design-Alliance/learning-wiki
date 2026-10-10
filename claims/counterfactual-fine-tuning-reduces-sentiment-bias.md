---
type: claim
title: Counterfactual fine-tuning reduces sentiment bias in LLM-generated forum replies
description: Counterfactual fine-tuning reduces sentiment bias in LLM-generated forum replies
id: counterfactual-fine-tuning-reduces-sentiment-bias
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: liu-2025
    resource: "https://doi.org/10.18608/jla.2025.8885"
    title: "Liu, Z., Xing, W., Jiao, X., & Li, C. (2025). Exploring Fairness and Explainability in LLM-Generated Support for Online Learning Discussion Forums. Journal of Learning Analytics, 12(3), 8–33. https://doi.org/10.18608/jla.2025.8885"
    author: "Liu, Z., Xing, W., Jiao, X., & Li, C."
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Counterfactual fine-tuning reduces sentiment bias in LLM-generated forum replies

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Fine-tuning on combined original and counterfactual data yields more balanced sentiment distributions across gender. [→ Liu 2025](#liu-2025)

## Evidence

### Liu 2025

Liu, Z., Xing, W., Jiao, X., & Li, C. (2025). Exploring Fairness and Explainability in LLM-Generated Support for Online Learning Discussion Forums. Journal of Learning Analytics, 12(3), 8–33. https://doi.org/10.18608/jla.2025.8885

`q2 · i?` · `causal · r1`

The study fine-tuned GPT-2, Gemma, and LLaMA3 with both original and GPT-4-generated counterfactual post data and compared ADSD fairness metrics against originally fine-tuned models; the article reports that "counterfactual fine-tuning shows promise in reducing this bias, resulting in more balanced sentiment distributions."

> "Notably, counterfactual fine-tuning shows promise in reducing this bias, resulting in more balanced sentiment distributions."

## Discussion


## Related Claims
- [LLM-generated forum replies are more neutral and less varied in sentiment than human replies](llm-replies-more-neutral-than-human.md) — related
- [Sentiment scores of LLM-generated replies differ significantly from human replies under both classifiers](llm-vs-human-sentiment-significant-difference.md) — related
- [Fine-tuned GPT-4o-mini delivers equitable name-detection performance across cultural and gender groups, reducing cultural biases present in baseline models](fine-tuned-gpt4o-mini-equitable-across-culture-gender.md) — related
- [Both fine-tuned models show regression toward the mean in score-wise bias, and error rises monotonically above score 3.0, with high scores hardest to predict](score-wise-bias-regression-to-mean-awe.md) — related
