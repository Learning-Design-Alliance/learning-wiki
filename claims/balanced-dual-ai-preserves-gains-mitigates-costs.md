---
type: claim
title: "Dual-AI configurations whose biases bracket the participant's own view preserve performance gains while avoiding the subjective penalty and one-sided influence"
description: "Dual-AI configurations whose biases bracket the participant's own view preserve performance gains while avoiding the subjective penalty and one-sided influence"
id: balanced-dual-ai-preserves-gains-mitigates-costs
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: lai-2025
    resource: "https://doi.org/10.48550/arXiv.2508.09297"
    title: "Lai, S., Choi, J., Kim, J., Kunievsky, N., Potter, Y., & Evans, J. (2025). Biased AI improves human performance but reduces perceived helpfulness. [doi:10.48550/arXiv.2508.09297](https://doi.org/10.48550/arXiv.2508.09297)"
    author: "Lai, S., Choi, J., Kim, J., Kunievsky, N., Potter, Y., & Evans, J."
    q: 3
    i: "?"
    kind: causal
    rigour: 3
  - id: lai-2025-2
    resource: "https://doi.org/10.48550/arXiv.2508.09297"
    title: "Lai, S., Choi, J., Kim, J., Kunievsky, N., Potter, Y., & Evans, J. (2025). Biased AI improves human performance but reduces perceived helpfulness. [doi:10.48550/arXiv.2508.09297](https://doi.org/10.48550/arXiv.2508.09297)"
    author: "Lai, S., Choi, J., Kim, J., Kunievsky, N., Potter, Y., & Evans, J."
    q: 4
    i: 1
    kind: causal
    rigour: 3
---

# Dual-AI configurations whose biases bracket the participant's own view preserve performance gains while avoiding the subjective penalty and one-sided influence

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r3` · `q3`–`q4` · `i1` small
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` In fact-checking, the balanced dual-AI pair reached the highest performance (0.649 versus 0.607 for the single default, p = 0.028) while its perceived-improvement penalty was indistinguishable from baseline (adj. p = 0.093). [→ Lai 2025](#lai-2025)
`q4 i1` In investment, the balanced pair rose above the misaligned single arm (Δ = 0.39%, g = 0.23, adj. p = 0.007), landing at the midpoint of the two one-sided arms. [→ Lai 2025 (2)](#lai-2025-2)

## Evidence

### Lai 2025

Lai, S., Choi, J., Kim, J., Kunievsky, N., Potter, Y., & Evans, J. (2025). Biased AI improves human performance but reduces perceived helpfulness. [doi:10.48550/arXiv.2508.09297](https://doi.org/10.48550/arXiv.2508.09297)

`q3 · i?` · `causal · r3`

Dual-AI fact-checking condition (N = 1,500) comparing balanced, opposition, and default configurations. The balanced pair beat the single default on accuracy; a single biased assistant depressed perceived improvement (Δ = −0.566, adj. p = 0.030) and dual opposition compounded it (Δ = −1.504, adj. p < 0.001), but the balanced pair did not (adj. p = 0.093). No effect size printed for the performance contrast.

> "the balanced pair reached the highest performance (0.649 versus 0.607 for the single default; Δ = 0.042, [0.005, 0.079], p = 0.028)"

### Lai 2025 (2)

Lai, S., Choi, J., Kim, J., Kunievsky, N., Potter, Y., & Evans, J. (2025). Biased AI improves human performance but reduces perceived helpfulness. [doi:10.48550/arXiv.2508.09297](https://doi.org/10.48550/arXiv.2508.09297)

`q4 · i1` · `causal · r3`

Investment-experiment dual-AI analysis: because a single biased assistant is a coin flip on market alignment, the balanced pair hedged, outperforming the misaligned arm by 0.39% (g = 0.23) and sitting at the two one-sided arms' midpoint. The article notes this protection was structural rather than discerning—participants followed the better assistant no better than chance (adj. p = 0.890).

> "the balanced pair rose above the misaligned arm (Δ = 0.39%, [0.11%, 0.67%], g = 0.23, adj. p = 0.007) landing below the aligned one (Δ = −0.48%, [−0.73%, −0.22%], g = −0.29, adj. p < 0.001)"

## Discussion


## Related Claims
- [Participants systematically undervalue biased AI, rating it less helpful and less recommendable even when it improves their performance](perceived-helpfulness-penalty-for-biased-ai.md) — related
- [Students exposed to the biased LLM showed no awareness of its influence, reporting lower perceived AI influence than neutral-condition participants despite larger bias effects](bias-transfer-without-awareness-llm-writing.md) — related
- [Politically biased AI assistants improve fact-checking accuracy relative to a default assistant, with benefits largely direction-general](biased-ai-improves-fact-checking-accuracy.md) — related
