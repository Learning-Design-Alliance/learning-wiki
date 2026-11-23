---
type: claim
title: Divergence tokens also drive subliminal transfer of misaligned tendencies
description: Divergence tokens also drive subliminal transfer of misaligned tendencies
id: divergence-tokens-drive-misalignment-transfer
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: simon-schrodi-2025
    resource: "https://doi.org/10.48550/arXiv.2509.23886"
    title: "Simon Schrodi, Elias Kempf, Fazl Barez, Thomas Brox. (2025). Towards Understanding Subliminal Learning: When and How Hidden Biases Transfer. [doi:10.48550/arXiv.2509.23886](https://doi.org/10.48550/arXiv.2509.23886)"
    author: Simon Schrodi, Elias Kempf, Fazl Barez, Thomas Brox
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Divergence tokens also drive subliminal transfer of misaligned tendencies

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The divergence-token masking result replicates when the transferred trait is misaligned behavior rather than an animal preference. [→ Simon Schrodi 2025](#simon-schrodi-2025)

## Evidence

### Simon Schrodi 2025

Simon Schrodi, Elias Kempf, Fazl Barez, Thomas Brox. (2025). Towards Understanding Subliminal Learning: When and How Hidden Biases Transfer. [doi:10.48550/arXiv.2509.23886](https://doi.org/10.48550/arXiv.2509.23886)

`q2 · i?` · `causal · r2`

Replication of the loss-masking experiment with a misaligned Qwen teacher trained on risky financial advice, measuring emergent-misalignment responses in the student. Masking divergence tokens out of the loss suppressed misalignment transfer, consistent with the animal-preference results.

> "We repeated the experiment from Figure 3, but now transferred misaligned tendencies. For the misaligned teacher, we used aQwenmodel trained on risky financial advice from Turner et al. (2025). Figure 8 shows that divergence tokens drive subliminal learning here, too."

## Discussion


## Related Claims
- Meaning-preserving prompt paraphrasings usually suppress subliminal learning, even when done by the biased teacher — related
- [Mixing data from multiple teachers weakens subliminal learning even when teachers share the same bias](multi-teacher-mixing-weakens-subliminal-learning.md) — related
