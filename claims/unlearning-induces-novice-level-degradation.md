---
type: claim
title: Machine unlearning induces progressively stronger novice-level performance in an LLM teachable agent, with accuracy and F1 declining as the unlearning ratio increases
description: Machine unlearning induces progressively stronger novice-level performance in an LLM teachable agent, with accuracy and F1 declining as the unlearning ratio increases
id: unlearning-induces-novice-level-degradation
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
    kind: design
    rigour: 2
  - id: jiajia-song-2026-2
    resource: "https://arxiv.org/abs/2603.26142"
    title: "Jiajia Song, Zhihan Guo, and Jionghao Lin. (2026). Simulating Novice Students Using Machine Unlearning and Relearning in Large Language Models. https://arxiv.org/abs/2603.26142"
    author: Jiajia Song, Zhihan Guo, and Jionghao Lin
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Machine unlearning induces progressively stronger novice-level performance in an LLM teachable agent, with accuracy and F1 declining as the unlearning ratio increases

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 1 causal `r1`, 1 design `r2` · `q2`

## Subclaims
`q2 i?` The unlearned model shows a clear, consistent decline in MCQ accuracy and F1 as unlearning ratio rises from 10% to 50%, indicating knowledge loss rather than noise. [→ Jiajia Song 2026](#jiajia-song-2026)
`q2 i?` The base pretrained model remains stable across all unlearning ratios, so the degradation is attributable to the unlearning procedure. [→ Jiajia Song 2026 (2)](#jiajia-song-2026-2)

## Evidence

### Jiajia Song 2026

Jiajia Song, Zhihan Guo, and Jionghao Lin. (2026). Simulating Novice Students Using Machine Unlearning and Relearning in Large Language Models. https://arxiv.org/abs/2603.26142 [doi:10.48550/arxiv.2603.26142](https://doi.org/10.48550/arxiv.2603.26142)

`q2 · i?` · `design · r2`

Numerical evaluation shown in Fig. 4 across five random seeds compares the unlearned Mistral-7B-Instruct model against the base model under 10%–50% unlearning ratios; "a clear and consistent decline in both accuracy and F1 score" reflects targeted knowledge loss.

> "The unlearned model (green line) exhibits a clear and consistent decline in both accuracy and F1 score as the unlearning ratio increases, dropping from around 0.75 at 10% to below 0.5 from the 40% unlearning ratio onward."

### Jiajia Song 2026 (2)

Jiajia Song, Zhihan Guo, and Jionghao Lin. (2026). Simulating Novice Students Using Machine Unlearning and Relearning in Large Language Models. https://arxiv.org/abs/2603.26142

`q2 · i?` · `causal · r1`

Fig. 4 numerical results show the unmodified base model "maintains a consistently high accuracy (around 0.85)" across ratios, indicating the degradation is attributable to unlearning rather than randomness or evaluation variance.

> "the base model (blue line), defined as the original pretrained model without any further fine-tuning or modification for a specific task, maintains a consistently high accuracy (around 0.85) and F1 scores (around 0.77) across all unlearning ratios."

## Discussion


## Related Claims
- [Coach-guided interactive teaching yields higher and more progressive recovery than static relearning, particularly under moderate forgetting levels (10%–30%)](coach-guided-relearning-beats-static.md) — related
- [Teachable agents measurably but incompletely relearn unlearned knowledge, with the recovery gap to the base model widening under higher unlearning ratios (30%–50%)](relearning-recovers-knowledge-incompletely.md) — related
- [Relearning dynamics depend on unlearning strength: agents with 10% unlearning recover within early interaction rounds, while 30% and 50% agents show prolonged low-accuracy plateaus and delayed improvement](unlearning-ratio-moderates-relearning-trajectory.md) — related
- [Dialogue evidence shows coach feedback induces genuine conceptual change, shifting the agent from misconception to conceptually correct explanation rather than superficial answer alignment](dialogue-feedback-induces-conceptual-change.md) — related
