---
type: claim
title: Differences in student pass-rate distributions between test splits explain the smaller INSIDE-over-SFT improvement on test_NP
description: Differences in student pass-rate distributions between test splits explain the smaller INSIDE-over-SFT improvement on test_NP
id: pass-rate-distribution-explains-split-gap
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: rose-niousha-2026
    resource: "https://arxiv.org/abs/2608.10492"
    title: "Rose Niousha, Minwoo Kang, Narges Norouzi. (2026). INSIDE the Student's Mind: Jointly Modeling Latent Reasoning and Action in LLM Student Simulators. Published as a conference paper at COLM 2026. https://arxiv.org/abs/2608.10492"
    author: Rose Niousha, Minwoo Kang, Narges Norouzi
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Differences in student pass-rate distributions between test splits explain the smaller INSIDE-over-SFT improvement on test_NP

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` test_OP students fail at 55% and succeed at 28% (roughly 2:1), whereas test_NP students fail at 47% and succeed at 34% (roughly 1.4:1); where failures are more common, INSIDE has more mismatch over SFT to correct. [→ Rose Niousha 2026](#rose-niousha-2026)

## Evidence

### Rose Niousha 2026

Rose Niousha, Minwoo Kang, Narges Norouzi. (2026). INSIDE the Student's Mind: Jointly Modeling Latent Reasoning and Action in LLM Student Simulators. Published as a conference paper at COLM 2026. https://arxiv.org/abs/2608.10492

`q2 · i?` · `design · r2`

Distributional analysis (Appendix D, Figure 4) of exact pass-rate mass by split for student, SFT, and INSIDE submissions. The article reports both splits concentrate mass at pass rates 0 and 1 (83% and 81%), and that on test_OP SFT underestimates complete failure (43% vs. 55%) and overestimates complete success (40% vs. 28%), which INSIDE better corrects.

> "test_OP students fail at 55% and succeed at 28% (roughly 2:1), whereas test_NP students fail at 47% and succeed at 34% (roughly 1.4:1). This helps explain the smaller INSIDE–SFT gap on test_NP."

## Discussion


## Related Claims
- [Prompting-based student simulators maintain artificially high pass rates (~80%) from the first submission step, while fine-tuned models track real students' low-start, sharp-increase trajectories](prompted-simulators-artificially-high-pass-rates.md) — related
- [Fine-tuning with INSIDE internal dialogue achieves the lowest Wasserstein distances to real student code distributions on test_OP across all action-fidelity metrics](inside-lowest-wasserstein-action-fidelity-test-op.md) — related
- [INSIDE fine-tuning achieves the highest alignment between generated internal dialogue and ground-truth student code edits, up to 57.9%](inside-highest-reasoning-alignment-57-9.md) — related
- [Pass@1 is not a sufficient success metric for soft barriers because it conflates successful barriers with model generation failures](pass1-false-narrative-soft-barriers.md) — related
