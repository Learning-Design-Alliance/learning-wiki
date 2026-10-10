---
type: claim
title: Human-LLM agreement is moderated by code properties, multi-model consensus, and model-reported confidence
description: Human-LLM agreement is moderated by code properties, multi-model consensus, and model-reported confidence
id: agreement-moderators-tiers-consensus-confidence
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: liu-2026
    resource: "https://arxiv.org/abs/2607.28890"
    title: "Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth. Preprint, no identifier printed in text. https://arxiv.org/abs/2607.28890"
    author: "Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: liu-2026-2
    resource: "https://arxiv.org/abs/2607.28890"
    title: "Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth. Preprint, no identifier printed in text. https://arxiv.org/abs/2607.28890"
    author: "Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: liu-2026-3
    resource: "https://arxiv.org/abs/2607.28890"
    title: "Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth. Preprint, no identifier printed in text. https://arxiv.org/abs/2607.28890"
    author: "Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M."
    q: 2
    i: 1
    kind: associational
    rigour: 2
---

# Human-LLM agreement is moderated by code properties, multi-model consensus, and model-reported confidence

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · design `r2` · `q2` · `i1` small

## Subclaims
`q2 i?` The 72 codes stratify into three agreement tiers: surface-identifiable codes exceed 0.4 Jaccard, inference-dependent codes fall below 0.2, with high-frequency codes such as Non-Educational at 0.05. [→ Liu 2026](#liu-2026)
`q2 i?` Human endorsement of a code rises monotonically with the number of models agreeing on it, from 12.2% when one of five models assigns it to 63.0% when all five converge. [→ Liu 2026 (2)](#liu-2026-2)
`q2 i1` Pooled across models, agreement rises with model-reported confidence (point-biserial r = 0.197, p < 0.001), but the shape and strength of this signal differ by model. [→ Liu 2026 (3)](#liu-2026-3)

## Evidence

### Liu 2026

Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth. Preprint, no identifier printed in text. https://arxiv.org/abs/2607.28890

`q2 · i?` · `design · r2`

Code-level stratification of mean human-LLM Jaccard across the 72-code instrument. Tier 1 (8 codes above 0.4) carries concrete task language; Tier 2 (roughly 30 codes, 0.2 to 0.4) needs some inference; Tier 3 (roughly 35 codes below 0.2) requires inferring intent, including Non-Educational at Jaccard 0.05.

> "Tier 1 codes (above 0.4, 8 codes) are marked by concrete task language identifiable from surface cues, such as Grading (0.63), Generate Feedback to Students (0.57), and Learning Standards Alignment (0.46)."

### Liu 2026 (2)

Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth. Preprint, no identifier printed in text. https://arxiv.org/abs/2607.28890

`q2 · i?` · `design · r2`

Multi-model consensus analysis relating the number of the five LLMs assigning a code to the rate of human endorsement (Table 3). The relationship is "monotonically increasing"; conversely, 32% of human-assigned codes are assigned by no model, which the authors read as interpretations requiring human expertise.

> "Endorsement rises monotonically with model agreement, from 12.2% when a single model assigns a code to 63.0% when all five converge."

### Liu 2026 (3)

Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth. Preprint, no identifier printed in text. https://arxiv.org/abs/2607.28890

`q2 · i1` · `associational · r2`

Confidence-bin analysis with identical bins for every model (Figure 2). Pooled agreement rose from 29% below 0.7 to 66% at 0.9 or above (point-biserial r = 0.197, p < 0.001); Claude Opus rose monotonically from 17% to 83%, while GPT-4o never reported confidence above 0.9 and Gemini Flash was nearly flat between 0.5 and 0.9.

> "Pooled, agreement rises with confidence (66% at 0.9 or above vs. 29% below 0.7; point-biserial r = 0.197, p < 0.001), but model-level patterns differ in shape."

## Discussion


## Related Claims
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [In blind verification, model selection matters more than source type: Bradley-Terry ranking interleaves human coders and LLMs, with per-model win rates spanning significant human advantage to numerical LLM advantage](bradley-terry-model-selection-matters-more-than-source-type.md) — related
- [LLM choice significantly influences human-AI coding correspondence, with Claude Sonnet 4 performing best and GPT 4.1 Mini worst](llm-choice-affects-human-ai-coding-correspondence.md) — related
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
- [AI-teacher diagnostic agreement was higher in the Diagnostic Review class and varied by issue type, with local language issues best diagnosed](ai-teacher-agreement-issue-type-variation.md) — related
