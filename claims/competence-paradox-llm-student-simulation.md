---
type: claim
title: "The competence paradox: broadly capable LLMs cannot genuinely unknow expert knowledge when simulating novices"
description: "The competence paradox: broadly capable LLMs cannot genuinely unknow expert knowledge when simulating novices"
id: competence-paradox-llm-student-simulation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
newest_evidence: 2026
source_checked: 2026-10-17
recheck_by: 2029
sources:
  - id: zhihao-yuan-2026
    resource: "https://doi.org/10.48550/arxiv.2601.05473"
    title: "Zhihao Yuan, Yunze Xiao, Ming Li, Weihao Xuan, Richard Tong, Mona Diab, Tom Mitchell. (2026). Towards Valid Student Simulation with Large Language Models. https://arxiv.org/abs/2601.05473 [doi:10.48550/arxiv.2601.05473](https://doi.org/10.48550/arxiv.2601.05473)"
    author: Zhihao Yuan, Yunze Xiao, Ming Li, Weihao Xuan, Richard Tong, Mona Diab, Tom Mitchell
    q: 1
    i: "?"
    kind: theoretical
    rigour: 2
---

# The competence paradox: broadly capable LLMs cannot genuinely unknow expert knowledge when simulating novices

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r2` · `q1`
> **Currency** · newest study 2026 · checked against its sources 2026-10-17 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q1 i?` LLM-based simulators exhibit a competence paradox rooted in prior-knowledge entanglement: prompted novices still reason with expert priors, so errors resemble superficial deviations from expert reasoning rather than stable, diagnosis-relevant misconceptions. [→ Zhihao Yuan 2026](#zhihao-yuan-2026)

## Evidence

### Zhihao Yuan 2026

Zhihao Yuan, Yunze Xiao, Ming Li, Weihao Xuan, Richard Tong, Mona Diab, Tom Mitchell. (2026). Towards Valid Student Simulation with Large Language Models. https://arxiv.org/abs/2601.05473 [doi:10.48550/arxiv.2601.05473](https://doi.org/10.48550/arxiv.2601.05473)

`q1 · i?` · `theoretical · r2`

Theoretical argument in the formalization section: the article argues the competence paradox is rooted in an irreducible prior-knowledge entanglement problem, since mainstream LLMs are trained to be broadly capable and self-correcting. No empirical evaluation is offered; the authors state the claim is not validated through direct pedagogical interaction.

> "Unlike human learners, they cannot genuinely “unknow” solution schemas or expert heuristics once internalized, so even when prompted to act like a novice, their latent reasoning trajectories remain shaped by expert priors"

## Discussion


## Related Claims
- [LLM student simulators exhibit near-zero Selective Flip Score, flipping at similarly high rates under targeted, misaligned, and generic feedback](llm-simulators-near-zero-sfs-indiscriminate-flipping.md) — related
- [Stronger problem-solving capability predicts lower misconception faithfulness: flip rate under generic feedback correlates negatively with SFS (Pearson r = -0.94, p = 0.002)](model-capability-negatively-correlates-sfs.md) — related
- [Multi-turn reflective interaction does not restore selective updating and destabilizes weaker simulators](multi-turn-reflection-does-not-restore-sfs.md) — related
- [Chain-of-Thought rationale quality shows no direct correlation with the accuracy of simulated student responses](cot-rationale-quality-no-correlation-simulated-accuracy.md) — related
- [EducaSim's LLM-based speaker oracle distinguishes it from prior simulation tools on multi-agent interaction](educasim-llm-oracle-multi-agent-speaker-selection.md) — related
