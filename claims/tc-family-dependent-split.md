---
type: claim
title: Termination Control (TC) shows family-dependent splits, suggesting transfer may take different forms across model families rather than a single phase
description: Termination Control (TC) shows family-dependent splits, suggesting transfer may take different forms across model families rather than a single phase
id: tc-family-dependent-split
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
sources:
  - id: noguchi-2026
    resource: "https://doi.org/10.48550/arXiv.2604.27454"
    title: "Noguchi, M. (2026). Exploring Applications of Transfer-State Large Language Models: Cognitive Profiling and Socratic AI Tutoring. [doi:10.48550/arXiv.2604.27454](https://doi.org/10.48550/arXiv.2604.27454)"
    author: Noguchi, M.
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Termination Control (TC) shows family-dependent splits, suggesting transfer may take different forms across model families rather than a single phase

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` TC showed a −2 difference (external closure in transfer) in the Sonnet 4.5 family, a +2 difference (internal closure in transfer) in the GPT-5.4 family, and 0 in the Gemini 3 Thinking family. [→ Noguchi 2026](#noguchi-2026)

## Evidence

### Noguchi 2026

Noguchi, M. (2026). Exploring Applications of Transfer-State Large Language Models: Cognitive Profiling and Socratic AI Tutoring. [doi:10.48550/arXiv.2604.27454](https://doi.org/10.48550/arXiv.2604.27454)

`q2 · i?` · `causal · r1`

Seven-indicator rating results (three-coder medians, Table 3): TC diverged by family — Sonnet 4.5 difference −2, GPT-5.4 +2, Gemini 3 Thinking 0. The article reports inter-coder reliability for TC of κ = 0.71 (substantial) and tentatively suggests an externally referential pattern in the Sonnet family versus a self-contained termination pattern in the GPT family.

> "In the Sonnet 4.5 family, transfer showed TC = −1 (external closure), whereas non-transfer showed TC = +1 (internal closure), yielding a difference of −2."

## Discussion


## Related Claims
- [LA_dir and QD function as auxiliary discriminators of transfer, while EH and RL showed zero differences in all families](auxiliary-indicators-la-dir-qd.md) — related
- [SU_dir (survival/continuity direction) shows positive transfer-side differences across all three tested model families and is the most reliable cognitive-profile indicator (kappa = 0.83)](su-dir-central-transfer-signature.md) — related
- [LLM conditions in a transfer state outperform corresponding non-transfer conditions on Socratic tutoring-context indicators, with a large descriptive effect size (d = 1.27)](transfer-state-llm-socratic-tutoring-advantage.md) — related
