---
type: claim
title: "In blind verification, model selection matters more than source type: Bradley-Terry ranking interleaves human coders and LLMs, with per-model win rates spanning significant human advantage to numerical LLM advantage"
description: "In blind verification, model selection matters more than source type: Bradley-Terry ranking interleaves human coders and LLMs, with per-model win rates spanning significant human advantage to numerical LLM advantage"
id: bradley-terry-model-selection-matters-more-than-source-type
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
---

# In blind verification, model selection matters more than source type: Bradley-Terry ranking interleaves human coders and LLMs, with per-model win rates spanning significant human advantage to numerical LLM advantage

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Per-model win rates against human coders ranged from 58.8% (Claude Opus, p = 0.092) down to 37.3% (Claude Haiku, p = 0.013); GPT-4o (39.8%, p = 0.048) and Claude Haiku were preferred significantly less often than human coders. [→ Liu 2026](#liu-2026)
`q2 i?` The Bradley-Terry ranking interleaves the eight sources: Claude Opus ranks first but is statistically indistinguishable from Coder 1, GPT-5.5 and Gemini Flash rank above two of the three human coders, and the 0.875 log-unit spread among LLMs dwarfs the 0.063 log-unit gap between the best LLM and the best human coder. [→ Liu 2026 (2)](#liu-2026-2)

## Evidence

### Liu 2026

Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth. Preprint, no identifier printed in text. https://arxiv.org/abs/2607.28890

`q2 · i?` · `design · r2`

Per-model binomial tests of LLM win rates in decisive Human vs. LLM pairs of the blind verification protocol (Table 4; roughly 102–106 decisive pairs per model). Win rates ran from 58.8% (Claude Opus) to 37.3% (Claude Haiku); only GPT-4o and Claude Haiku fell significantly below 50%.

> "Claude Opus and Gemini Flash were preferred over human coders more often than not, though neither difference reaches per-model significance. GPT-5.5 shows no directional preference. GPT-4o and Claude Haiku were preferred significantly less often than human coders (p = 0.048 and p = 0.013), confirming lower coding quality as judged by the verifier."

### Liu 2026 (2)

Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth. Preprint, no identifier printed in text. https://arxiv.org/abs/2607.28890

`q2 · i?` · `design · r2`

Bradley-Terry model fit to all 801 decisive blind comparisons over the eight verified sources (Figure 3, log-scale ability estimates with 95% bootstrap intervals). The figure note adds that the "0.875 log-unit spread among LLMs dwarfs the 0.063 log-unit gap between the best LLM and the best human coder".

> "Claude Opus occupies the top position with a confidence interval overlapping substantially with Coder 1, so the two are statistically indistinguishable. GPT-5.5 and Gemini Flash rank above two of the three human coders, Claude Haiku ranks below all of them, and GPT-4o is the only source whose interval does not overlap with any human coder."

## Discussion


## Related Claims
- [Human-LLM agreement is moderated by code properties, multi-model consensus, and model-reported confidence](agreement-moderators-tiers-consensus-confidence.md) — related
- [Agreement metrics and expert quality judgments diverge in both directions: human consensus can encode shared conservative bias that the verifier rejects in favor of LLM coding](agreement-quality-divergence-human-consensus-bias.md) — related
- [Blind expert verification shows no overall preference for human over LLM qualitative coding when sources are judged symmetrically](blind-verification-no-overall-human-preference.md) — a broader claim this one bears on
- [On codes requiring recognition of pedagogical intent not explicitly stated, LLMs over-apply and the blind verifier rejects their application in favor of human coding](intent-inference-codes-require-human-coders.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [Human-human agreement (average κ = 0.644) was lower than the best LLM-LLM agreement (average κ = 0.856) across constructs](human-human-agreement-lower-than-llm-llm.md) — related
- [Zero-shot prompt type has minimal impact on LLM-human coding concordance](prompt-type-minimal-impact-llm-coding.md) — related
