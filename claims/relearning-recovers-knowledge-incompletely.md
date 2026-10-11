---
type: claim
title: "Teachable agents measurably but incompletely relearn unlearned knowledge, with the recovery gap to the base model widening under higher unlearning ratios (30%–50%)"
description: "Teachable agents measurably but incompletely relearn unlearned knowledge, with the recovery gap to the base model widening under higher unlearning ratios (30%–50%)"
id: relearning-recovers-knowledge-incompletely
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: jiajia-song-2026
    resource: "https://arxiv.org/abs/2603.26142"
    title: "Jiajia Song, Zhihan Guo, and Jionghao Lin. (2026). Simulating Novice Students Using Machine Unlearning and Relearning in Large Language Models. https://arxiv.org/abs/2603.26142"
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

# Teachable agents measurably but incompletely relearn unlearned knowledge, with the recovery gap to the base model widening under higher unlearning ratios (30%–50%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`

## Subclaims
`q2 i?` Both relearning strategies improve accuracy and F1 across all unlearning ratios, showing suppressed knowledge can be reacquired. [→ Jiajia Song 2026](#jiajia-song-2026)
`q2 i?` Relearned models do not fully recover base-model performance, and the gap widens at higher unlearning ratios; the F1 gap is more pronounced, suggesting persistent conceptual inconsistencies. [→ Jiajia Song 2026 (2)](#jiajia-song-2026-2)

## Evidence

### Jiajia Song 2026

Jiajia Song, Zhihan Guo, and Jionghao Lin. (2026). Simulating Novice Students Using Machine Unlearning and Relearning in Large Language Models. https://arxiv.org/abs/2603.26142

`q2 · i?` · `causal · r1`

Fig. 4 numerical results compare relearned (supervised fine-tuning on forgotten QA pairs) with unlearned models; relearned models "substantially outperform their corresponding unlearned counterparts" across all unlearning ratios.

> "Both relearning strategies consistently improve performance across all unlearning ratios. Specifically, relearned models (orange line) substantially outperform their corresponding unlearned counterparts, demonstrating that previously suppressed knowledge can be reacquired rather than being completely erased."

### Jiajia Song 2026 (2)

Jiajia Song, Zhihan Guo, and Jionghao Lin. (2026). Simulating Novice Students Using Machine Unlearning and Relearning in Large Language Models. https://arxiv.org/abs/2603.26142

`q2 · i?` · `design · r2`

Fig. 4 results show recovery is "measurable yet incomplete": relearned models never reach base-model level and the gap widens under 30%–50% unlearning, with the F1 gap more pronounced than accuracy.

> "the relearned models do not fully recover to the performance level of the base model (blue line), and the performance gap widens under higher unlearning ratios (30%–50%), indicating that knowledge recovery is measurable yet incomplete, especially when a larger portion of knowledge has been unlearned."

## Discussion


## Related Claims
- [Coach-guided interactive teaching yields higher and more progressive recovery than static relearning, particularly under moderate forgetting levels (10%–30%)](coach-guided-relearning-beats-static.md) — related
- [Relearning dynamics depend on unlearning strength: agents with 10% unlearning recover within early interaction rounds, while 30% and 50% agents show prolonged low-accuracy plateaus and delayed improvement](unlearning-ratio-moderates-relearning-trajectory.md) — a narrower finding that bears on this claim
- [Machine unlearning induces progressively stronger novice-level performance in an LLM teachable agent, with accuracy and F1 declining as the unlearning ratio increases](unlearning-induces-novice-level-degradation.md) — related
