---
type: claim
title: "The competence paradox: broadly capable LLMs cannot genuinely unknow expert knowledge when simulating novices"
description: "The competence paradox: broadly capable LLMs cannot genuinely unknow expert knowledge when simulating novices"
id: competence-paradox-llm-student-simulation
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: zhihao-yuan-2026
    resource: "https://arxiv.org/abs/2601.05473"
    title: "Zhihao Yuan, Yunze Xiao, Ming Li, Weihao Xuan, Richard Tong, Mona Diab, Tom Mitchell. (2026). Towards Valid Student Simulation with Large Language Models. https://arxiv.org/abs/2601.05473"
    author: Zhihao Yuan, Yunze Xiao, Ming Li, Weihao Xuan, Richard Tong, Mona Diab, Tom Mitchell
    q: 1
    i: "?"
---

# The competence paradox: broadly capable LLMs cannot genuinely unknow expert knowledge when simulating novices

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q1` argument or single case

## Subclaims
`q1 i?` LLM-based simulators exhibit a competence paradox rooted in prior-knowledge entanglement: prompted novices still reason with expert priors, so errors resemble superficial deviations from expert reasoning rather than stable, diagnosis-relevant misconceptions. [→ Zhihao Yuan 2026](#zhihao-yuan-2026)

## Evidence

### Zhihao Yuan 2026

Zhihao Yuan, Yunze Xiao, Ming Li, Weihao Xuan, Richard Tong, Mona Diab, Tom Mitchell. (2026). Towards Valid Student Simulation with Large Language Models. https://arxiv.org/abs/2601.05473

`q1 · i?`

Theoretical argument in the formalization section: the article argues the competence paradox is rooted in an irreducible prior-knowledge entanglement problem, since mainstream LLMs are trained to be broadly capable and self-correcting. No empirical evaluation is offered; the authors state the claim is not validated through direct pedagogical interaction.

> "Unlike human learners, they cannot genuinely “unknow” solution schemas or expert heuristics once internalized, so even when prompted to act like a novice, their latent reasoning trajectories remain shaped by expert priors"

## Discussion


## Related Claims
- [LLM student simulators exhibit near-zero Selective Flip Score, flipping at similarly high rates under targeted, misaligned, and generic feedback](llm-simulators-near-zero-sfs-indiscriminate-flipping.md) — related
- [Stronger problem-solving capability predicts lower misconception faithfulness: flip rate under generic feedback correlates negatively with SFS (Pearson r = -0.94, p = 0.002)](model-capability-negatively-correlates-sfs.md) — related
- [Multi-turn reflective interaction does not restore selective updating and destabilizes weaker simulators](multi-turn-reflection-does-not-restore-sfs.md) — related
- [Chain-of-Thought rationale quality shows no direct correlation with the accuracy of simulated student responses](cot-rationale-quality-no-correlation-simulated-accuracy.md) — related
