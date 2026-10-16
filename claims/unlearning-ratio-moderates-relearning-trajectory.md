---
type: claim
title: "Relearning dynamics depend on unlearning strength: agents with 10% unlearning recover within early interaction rounds, while 30% and 50% agents show prolonged low-accuracy plateaus and delayed improvement"
description: "Relearning dynamics depend on unlearning strength: agents with 10% unlearning recover within early interaction rounds, while 30% and 50% agents show prolonged low-accuracy plateaus and delayed improvement"
id: unlearning-ratio-moderates-relearning-trajectory
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: jiajia-song-2026
    resource: "https://doi.org/10.48550/arxiv.2603.26142"
    title: "Jiajia Song, Zhihan Guo, and Jionghao Lin. (2026). Simulating Novice Students Using Machine Unlearning and Relearning in Large Language Models. https://arxiv.org/abs/2603.26142 [doi:10.48550/arxiv.2603.26142](https://doi.org/10.48550/arxiv.2603.26142)"
    author: Jiajia Song, Zhihan Guo, and Jionghao Lin
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Relearning dynamics depend on unlearning strength: agents with 10% unlearning recover within early interaction rounds, while 30% and 50% agents show prolonged low-accuracy plateaus and delayed improvement

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Lower-unlearning agents exhibit early performance recovery and steady accuracy increases; higher-unlearning agents show prolonged plateaus, sporadic correct responses, and delayed improvement. [→ Jiajia Song 2026](#jiajia-song-2026)

## Evidence

### Jiajia Song 2026

Jiajia Song, Zhihan Guo, and Jionghao Lin. (2026). Simulating Novice Students Using Machine Unlearning and Relearning in Large Language Models. https://arxiv.org/abs/2603.26142 [doi:10.48550/arxiv.2603.26142](https://doi.org/10.48550/arxiv.2603.26142)

`q2 · i?` · `causal · r2`

Qualitative analysis of interaction trajectories (Fig. 5, Exception Handling topic) under LLM-coach instruction: 10%-unlearning agents "begin toexhibitperformancerecoverywithintheearlyinteractionrounds" while 30% and 50% agents show prolonged low-accuracy plateaus and delayed improvement.

> "teachable agents with a lower unlearning ratio (10%) begin toexhibitperformancerecoverywithintheearlyinteractionrounds,followedbya steady increase in both rolling and cumulative accuracy."

## Discussion


## Related Claims
- [Coach-guided interactive teaching yields higher and more progressive recovery than static relearning, particularly under moderate forgetting levels (10%–30%)](coach-guided-relearning-beats-static.md) — a broader claim this one bears on
- [Teachable agents measurably but incompletely relearn unlearned knowledge, with the recovery gap to the base model widening under higher unlearning ratios (30%–50%)](relearning-recovers-knowledge-incompletely.md) — a broader claim this one bears on
- [Machine unlearning induces progressively stronger novice-level performance in an LLM teachable agent, with accuracy and F1 declining as the unlearning ratio increases](unlearning-induces-novice-level-degradation.md) — related
