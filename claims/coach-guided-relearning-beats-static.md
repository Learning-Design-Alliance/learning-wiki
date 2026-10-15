---
type: claim
title: "Coach-guided interactive teaching yields higher and more progressive recovery than static relearning, particularly under moderate forgetting levels (10%–30%)"
description: "Coach-guided interactive teaching yields higher and more progressive recovery than static relearning, particularly under moderate forgetting levels (10%–30%)"
id: coach-guided-relearning-beats-static
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: jiajia-song-2026
    resource: "https://doi.org/10.48550/arxiv.2603.26142"
    title: "Jiajia Song, Zhihan Guo, and Jionghao Lin. (2026). Simulating Novice Students Using Machine Unlearning and Relearning in Large Language Models. https://arxiv.org/abs/2603.26142 [doi:10.48550/arxiv.2603.26142](https://doi.org/10.48550/arxiv.2603.26142)"
    author: Jiajia Song, Zhihan Guo, and Jionghao Lin
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: jiajia-song-2026-2
    resource: "https://arxiv.org/abs/2603.26142"
    title: "Jiajia Song, Zhihan Guo, and Jionghao Lin. (2026). Simulating Novice Students Using Machine Unlearning and Relearning in Large Language Models. https://arxiv.org/abs/2603.26142"
    author: Jiajia Song, Zhihan Guo, and Jionghao Lin
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Coach-guided interactive teaching yields higher and more progressive recovery than static relearning, particularly under moderate forgetting levels (10%–30%)

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 1 causal `r1`, 1 design `r2` · `q2`

## Subclaims
`q2 i?` In a three-agent teachable-agent setting, coach-guided dialogue produces consistent and progressive accuracy gains, especially under moderate unlearning. [→ Jiajia Song 2026](#jiajia-song-2026)
`q2 i?` Relearn (LLM Coach) achieves consistently higher F1 than static relearning, indicating more balanced and coherent knowledge recovery. [→ Jiajia Song 2026 (2)](#jiajia-song-2026-2)

## Evidence

### Jiajia Song 2026

Jiajia Song, Zhihan Guo, and Jionghao Lin. (2026). Simulating Novice Students Using Machine Unlearning and Relearning in Large Language Models. https://arxiv.org/abs/2603.26142 [doi:10.48550/arxiv.2603.26142](https://doi.org/10.48550/arxiv.2603.26142)

`q2 · i?` · `causal · r1`

In the Stage 3 three-agent environment (teachable, judge, and DeepSeek-V3.2 coach agents), the unlearned model as teachable agent shows "consistent and progressive gains in accuracy" across unlearning ratios versus static relearning, per Fig. 4(a).

> "Compared with static relearning, coach-guided interac- tion yields consistent and progressive gains in accuracy across unlearning ratios,"

### Jiajia Song 2026 (2)

Jiajia Song, Zhihan Guo, and Jionghao Lin. (2026). Simulating Novice Students Using Machine Unlearning and Relearning in Large Language Models. https://arxiv.org/abs/2603.26142

`q2 · i?` · `design · r2`

Fig. 4(b) F1 results show "Relearn (LLM Coach) achieves consistently higher F1 scores than static relearning", suggesting instructional feedback helps reconstruct missing conceptual links rather than memorizing answers.

> "Relearn (LLM Coach) achieves consistently higher F1 scores than static relearning, highlighting the advantage of interactive teaching in promoting more balanced and coherent knowledge recovery."

## Discussion


## Related Claims
- [Relearning dynamics depend on unlearning strength: agents with 10% unlearning recover within early interaction rounds, while 30% and 50% agents show prolonged low-accuracy plateaus and delayed improvement](unlearning-ratio-moderates-relearning-trajectory.md) — a narrower finding that bears on this claim
- [Teachable agents measurably but incompletely relearn unlearned knowledge, with the recovery gap to the base model widening under higher unlearning ratios (30%–50%)](relearning-recovers-knowledge-incompletely.md) — related
- [Machine unlearning induces progressively stronger novice-level performance in an LLM teachable agent, with accuracy and F1 declining as the unlearning ratio increases](unlearning-induces-novice-level-degradation.md) — related
- [Dialogue evidence shows coach feedback induces genuine conceptual change, shifting the agent from misconception to conceptually correct explanation rather than superficial answer alignment](dialogue-feedback-induces-conceptual-change.md) — related
- [Teaching interactions typically conclude within 30 dialogue turns, motivating a 30-turn cap to prevent dead loops](teaching-sessions-conclude-within-30-turns.md) — related
