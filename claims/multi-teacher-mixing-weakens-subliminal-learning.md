---
type: claim
title: Mixing data from multiple teachers weakens subliminal learning even when teachers share the same bias
description: Mixing data from multiple teachers weakens subliminal learning even when teachers share the same bias
id: multi-teacher-mixing-weakens-subliminal-learning
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
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

# Mixing data from multiple teachers weakens subliminal learning even when teachers share the same bias

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Even 10% data from an unbiased teacher substantially reduces trait transmission and 25% nearly eliminates it; a 50/50 mix of two same-bias teachers of different architectures also weakens transmission. [→ Simon Schrodi 2025](#simon-schrodi-2025)

## Evidence

### Simon Schrodi 2025

Simon Schrodi, Elias Kempf, Fazl Barez, Thomas Brox. (2025). Towards Understanding Subliminal Learning: When and How Hidden Biases Transfer. [doi:10.48550/arXiv.2509.23886](https://doi.org/10.48550/arXiv.2509.23886)

`q2 · i?` · `causal · r2`

Teacher-mixing experiments on Qwen students, combining finetuning data from a biased teacher with data from an unbiased control teacher at varying ratios, and separately mixing biased Qwen and biased Gemma data. A 50/50 same-bias cross-architecture mix weakened transmission for ‘owl’ and ‘penguin’ but was less effective for ‘eagle’.

> "Figure 7a shows that even 10% unbiased data substantially reduces trait transmission, and 25% nearly eliminates it."

## Discussion


## Related Claims
- [Divergence tokens also drive subliminal transfer of misaligned tendencies](divergence-tokens-drive-misalignment-transfer.md) — related
- Meaning-preserving prompt paraphrasings usually suppress subliminal learning, even when done by the biased teacher — related
