---
type: claim
title: "Agreement metrics and expert quality judgments diverge in both directions: human consensus can encode shared conservative bias that the verifier rejects in favor of LLM coding"
description: "Agreement metrics and expert quality judgments diverge in both directions: human consensus can encode shared conservative bias that the verifier rejects in favor of LLM coding"
id: agreement-quality-divergence-human-consensus-bias
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
    kind: associational
    rigour: 2
---

# Agreement metrics and expert quality judgments diverge in both directions: human consensus can encode shared conservative bias that the verifier rejects in favor of LLM coding

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`

## Subclaims
`q2 i?` For codes with moderate-to-high human-human agreement, the blind verifier more often endorses the LLM interpretation, indicating two coders can reliably agree while both under-applying a code. [→ Liu 2026](#liu-2026)
`q2 i?` For codes with low human-LLM agreement, the verifier can still prefer the LLM application, so low agreement does not guarantee the LLM interpretation is worse. [→ Liu 2026 (2)](#liu-2026-2)

## Evidence

### Liu 2026

Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth. Preprint, no identifier printed in text. https://arxiv.org/abs/2607.28890

`q2 · i?` · `design · r2`

Per-code endorsement analysis of contested codes in the blind verification protocol (median 18 contested pairs per code, percentages indicative). The verifier endorsed the LLM application of ELA Skills Development "61% of the time when an LLM applies it but 30% when a human applies it"; Unit Planning was endorsed in 79% of LLM applications while none of its three contested human applications were endorsed.

> "ELA Skills Development (H-H = 0.48) is endorsed 61% of the time when an LLM applies it but 30% when a human applies it, and Entire Lesson Planning (H-H = 0.50) shows the same pattern (56% vs. 32%)."

### Liu 2026 (2)

Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth. Preprint, no identifier printed in text. https://arxiv.org/abs/2607.28890

`q2 · i?` · `associational · r2`

Per-code endorsement analysis of contested codes; the article states this pattern "appears across 12 codes". For Inquiry and Deep Questions, human-LLM Jaccard was 0.15, yet the verifier endorsed the LLM application (65%) far more often than the human omission (23%), so agreement alone cannot determine automatability.

> "Inquiry and Deep Questions (H-L = 0.15) shows human endorsement of 23% versus LLM endorsement of 65%. The low agreement reflects LLMs applying the code where humans do not, yet the verifier judges the LLM application appropriate far more often than the human omission."

## Discussion


## Related Claims
- [On codes requiring recognition of pedagogical intent not explicitly stated, LLMs over-apply and the blind verifier rejects their application in favor of human coding](intent-inference-codes-require-human-coders.md) — a narrower finding that bears on this claim
- [Blind expert verification shows no overall preference for human over LLM qualitative coding when sources are judged symmetrically](blind-verification-no-overall-human-preference.md) — related
- [In blind verification, model selection matters more than source type: Bradley-Terry ranking interleaves human coders and LLMs, with per-model win rates spanning significant human advantage to numerical LLM advantage](bradley-terry-model-selection-matters-more-than-source-type.md) — related
