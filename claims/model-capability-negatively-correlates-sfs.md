---
type: claim
title: "Stronger problem-solving capability predicts lower misconception faithfulness: flip rate under generic feedback correlates negatively with SFS (Pearson r = -0.94, p = 0.002)"
description: "Stronger problem-solving capability predicts lower misconception faithfulness: flip rate under generic feedback correlates negatively with SFS (Pearson r = -0.94, p = 0.002)"
id: model-capability-negatively-correlates-sfs
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: heejin-do-2026
    resource: "https://arxiv.org/abs/2605.12748"
    title: "Heejin Do, Shashank Sonkar, Mrinmaya Sachan. (2026). Simulating Students or Sycophantic Problem Solving? On Misconception Faithfulness of LLM Simulators. Preprint. https://arxiv.org/abs/2605.12748"
    author: Heejin Do, Shashank Sonkar, Mrinmaya Sachan
    q: 2
    i: 3
    kind: causal
    rigour: 2
---

# Stronger problem-solving capability predicts lower misconception faithfulness: flip rate under generic feedback correlates negatively with SFS (Pearson r = -0.94, p = 0.002)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2` · `i3` large

## Subclaims
`q2 i3` Across the seven evaluated models, capability proxied by flip rate under generic feedback (FG) is strongly negatively correlated with SFS, with reasoning-augmented models showing higher flip rates but lower sensitivity. [→ Heejin Do 2026](#heejin-do-2026)

## Evidence

### Heejin Do 2026

Heejin Do, Shashank Sonkar, Mrinmaya Sachan. (2026). Simulating Students or Sycophantic Problem Solving? On Misconception Faithfulness of LLM Simulators. Preprint. https://arxiv.org/abs/2605.12748

`q2 · i3` · `causal · r2`

Correlational analysis across the seven evaluated LLM simulators, averaged over both datasets and prompting strategies; the figure reports Pearson r = -0.94 (p = 0.002), and the text states "Models that can solve the problem without guidance exhibit minimal sensitivity."

> "Figure 3(b)shows a strong negative correlation between model capability—proxied by the flip rate under generic feedback (FG)—and SFS. Models that can solve the problem without guidance exhibit minimal sensitivity, collapsing all feedback conditions into uniformly high flip rates."

## Discussion


## Related Claims
- [LLM student simulators exhibit near-zero Selective Flip Score, flipping at similarly high rates under targeted, misaligned, and generic feedback](llm-simulators-near-zero-sfs-indiscriminate-flipping.md) — related
- [Sycophantic failure manifests as indiscriminate correct flips rather than explicit sycophantic agreement, and SFT shifts behavior toward pushback and maintain under non-targeted feedback](sycophancy-via-correct-flip-not-verbal-agreement.md) — related
- [Multi-turn reflective interaction does not restore selective updating and destabilizes weaker simulators](multi-turn-reflection-does-not-restore-sfs.md) — related
