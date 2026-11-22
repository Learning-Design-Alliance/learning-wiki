---
type: claim
title: "Learner-state conditioning is often weak: inferred states can show limited sensitivity to student errors and drift over sustained tutoring"
description: "Learner-state conditioning is often weak: inferred states can show limited sensitivity to student errors and drift over sustained tutoring"
id: learner-state-conditioning-weak-sensitivity-drift
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: sayantan-adak-2026
    resource: "https://doi.org/10.48550/arXiv.2610.15692"
    title: "Sayantan Adak, Rima Hazra, Koyel Mukherjee, Digbalay Bose, Somnath Banerjee. (2026). Do LLM Tutors Actually Teach? A Process-Centered Synthesis of the Tutoring Loop. arXiv preprint. [doi:10.48550/arXiv.2610.15692](https://doi.org/10.48550/arXiv.2610.15692)"
    author: Sayantan Adak, Rima Hazra, Koyel Mukherjee, Digbalay Bose, Somnath Banerjee
    q: 2
    i: "?"
    kind: review
    rigour: 3
---

# Learner-state conditioning is often weak: inferred states can show limited sensitivity to student errors and drift over sustained tutoring

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r3` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Conditioning on learner state can be weak: one benchmarking study finds limited sensitivity to student errors or KC information where instruction should adapt, and proficiency control drifts over sustained tutoring interactions. [→ Sayantan Adak 2026](#sayantan-adak-2026)

## Evidence

### Sayantan Adak 2026

Sayantan Adak, Rima Hazra, Koyel Mukherjee, Digbalay Bose, Somnath Banerjee. (2026). Do LLM Tutors Actually Teach? A Process-Centered Synthesis of the Tutoring Loop. arXiv preprint. [doi:10.48550/arXiv.2610.15692](https://doi.org/10.48550/arXiv.2610.15692)

`q2 · i?` · `review · r3`

The review reports, citing Borchers and Shou 2025 and Almasi and Kristensen-McLachlan 2025, that handing a tutor learner information does not reliably produce personalization; L1-to-L2 is treated as an evaluation target in itself.

> "Borchers and Shou (2025) find limited sensitivity to student er- rors or KC information where instruction should adapt; LongTutor separates access to history from diagnosis and teaching (Li et al., 2026a); and pro- ficiency control drifts over sustained tutoring (Al- masi and Kristensen-McLachlan, 2025)."

## Discussion


## Related Claims
- [Meta-behavioral pattern extraction outperforms knowledge-concept-based collaborative extraction, which fails to consistently boost performance due to data sparsity](meta-behavioral-extraction-beats-kc-based-variants.md) — related
- [Qualitative error analysis yields five recurring error types, with over-inference most prevalent (33.5%), followed by evidence misidentification (23.4%) and hallucination (19.8%)](five-error-types-llm-diagnosis-vague-evidence.md) — related
- [The simulated learner tracks a real-student KT model with calibration error 0.049, and the helpfulness rubric transfers to real classroom transcripts](educlaw-bench-simulator-calibration.md) — related
- [Judge-condition verification did not consistently improve LLM feedback quality and often propagated Peer agents' errors](judge-verification-propagates-peer-errors.md) — related
