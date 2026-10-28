---
type: claim
title: Pre-finetuning without key phrases does not improve scoring performance and slightly lowers it relative to the BERT baseline
description: Pre-finetuning without key phrases does not improve scoring performance and slightly lowers it relative to the BERT baseline
id: prefinetuning-without-key-phrases-no-gain
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: funayama-2025
    resource: "https://doi.org/10.1007/s40593-025-00474-w"
    title: "Funayama, H., Matsubayashi, Y., Asazuma, Y., Mizumoto, T., & Inui, K. (2025). Cross-prompt Pre-finetuning of Language Models for Short Answer Scoring. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00474-w"
    author: "Funayama, H., Matsubayashi, Y., Asazuma, Y., Mizumoto, T., & Inui, K."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Pre-finetuning without key phrases does not improve scoring performance and slightly lowers it relative to the BERT baseline

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Simply pre-finetuning on other prompts without key-phrase inputs slightly lowered model performance compared with the BERT baseline. [→ Funayama 2025](#funayama-2025)

## Evidence

### Funayama 2025

Funayama, H., Matsubayashi, Y., Asazuma, Y., Mizumoto, T., & Inui, K. (2025). Cross-prompt Pre-finetuning of Language Models for Short Answer Scoring. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00474-w

`q2 · i?` · `causal · r2`

In the same five-setting BERT experiment on the RIKEN dataset, the 2-phase setting without key phrases underperformed the baseline, and using key phrases without pre-finetuning also did not improve performance. The authors attribute this to key phrases remaining "unchanged throughout the training phase, thus failing to provide any dynamic cues."

> "2-phase w/o key phrase slightly lowered the model performance compared with the BERT baseline. This result indicates that simply pre-ﬁnetuning on other prompts cannot effectively improve model performance."

## Discussion


## Related Claims
- [Two-phase cross-prompt pre-finetuning with key phrases significantly improves short answer scoring accuracy when in-prompt training data is limited](cross-prompt-prefinetuning-key-phrases-low-resource-gain.md) — related
- [The pre-finetuned model learns a scoring principle: predicted scores correlate strongly and negatively with edit distance between answers and key phrases](model-learns-scoring-principle-key-phrase-similarity.md) — related
- [Pre-finetuning performance increases with the number of distinct prompts used, holding total pre-finetuning answers fixed](more-prompts-better-prefinetuning.md) — related
- [Cross-prompt pre-finetuning shows no significant benefit when sufficient (200-answer) in-prompt training data is available](prefinetuning-no-benefit-sufficient-data.md) — related
