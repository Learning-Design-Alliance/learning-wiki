---
type: claim
title: Cross-prompt pre-finetuning shows no significant benefit when sufficient (200-answer) in-prompt training data is available
description: Cross-prompt pre-finetuning shows no significant benefit when sufficient (200-answer) in-prompt training data is available
id: prefinetuning-no-benefit-sufficient-data
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

# Cross-prompt pre-finetuning shows no significant benefit when sufficient (200-answer) in-prompt training data is available

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` There was no significant improvement in performance when 200 answers were used for training. [→ Funayama 2025](#funayama-2025)

## Evidence

### Funayama 2025

Funayama, H., Matsubayashi, Y., Asazuma, Y., Mizumoto, T., & Inui, K. (2025). Cross-prompt Pre-finetuning of Language Models for Short Answer Scoring. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00474-w

`q2 · i?` · `causal · r2`

In the BERT experiment varying finetuning data size (10, 25, 50, 100, 200 instances), the article reports no statistically significant difference at 200 answers; equivalence was not tested. The article states pre-finetuning "is not beneﬁcial when sufﬁcient training data are available."

> "However, there was no signiﬁcant improvement in performance when 200 answers were used for training, indicating that pre-ﬁnetuning is not beneﬁcial when sufﬁcient training data are available."

## Discussion


## Related Claims
- [Cross-prompt finetuning of a pre-finetuned 8B LLM on 50 instances per prompt achieves average QWK of 0.85, comparable to professional human graders (0.87)](cross-prompt-finetuning-8b-human-level.md) — related
- [Two-phase cross-prompt pre-finetuning with key phrases significantly improves short answer scoring accuracy when in-prompt training data is limited](cross-prompt-prefinetuning-key-phrases-low-resource-gain.md) — related
- [Pre-finetuning performance increases with the number of distinct prompts used, holding total pre-finetuning answers fixed](more-prompts-better-prefinetuning.md) — related
- [Pre-finetuning without key phrases does not improve scoring performance and slightly lowers it relative to the BERT baseline](prefinetuning-without-key-phrases-no-gain.md) — related
