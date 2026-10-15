---
type: claim
title: Dialogue evidence shows coach feedback induces genuine conceptual change, shifting the agent from misconception to conceptually correct explanation rather than superficial answer alignment
description: Dialogue evidence shows coach feedback induces genuine conceptual change, shifting the agent from misconception to conceptually correct explanation rather than superficial answer alignment
id: dialogue-feedback-induces-conceptual-change
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
    kind: design
    rigour: 2
---

# Dialogue evidence shows coach feedback induces genuine conceptual change, shifting the agent from misconception to conceptually correct explanation rather than superficial answer alignment

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Before instruction the agent misinterpreted exception chaining as error-hiding for security; after coach feedback it selected the correct option and gave a conceptually accurate explanation. [→ Jiajia Song 2026](#jiajia-song-2026)

## Evidence

### Jiajia Song 2026

Jiajia Song, Zhihan Guo, and Jionghao Lin. (2026). Simulating Novice Students Using Machine Unlearning and Relearning in Large Language Models. https://arxiv.org/abs/2603.26142 [doi:10.48550/arxiv.2603.26142](https://doi.org/10.48550/arxiv.2603.26142)

`q2 · i?` · `design · r2`

Qualitative dialogue comparison in Table 1 (10% unlearning split): the agent moved from Option A with a security misunderstanding of the from keyword to Option B with an explanation that "fromis used to explicitly preserve and link the exception cause".

> "This shift reflects a correction of the underlying mental model rather than superficial answer alignment, demonstrating genuine conceptual change induced through interaction."

## Discussion


## Related Claims
- [Coach-guided interactive teaching yields higher and more progressive recovery than static relearning, particularly under moderate forgetting levels (10%–30%)](coach-guided-relearning-beats-static.md) — related
- [Peer Discussion Improves Conceptual Understanding](peer-discussion-improves-conceptual-understanding.md) — related
- [Conflict-based instruction improves science conceptual learning, though staged contradictions helped only learners who reported being confused, and no study isolates disequilibrium as the mechanism](cognitive-disequilibrium-motivates-conceptual-change.md) — a broader claim this one bears on
- [Sycophantic failure manifests as indiscriminate correct flips rather than explicit sycophantic agreement, and SFT shifts behavior toward pushback and maintain under non-targeted feedback](sycophancy-via-correct-flip-not-verbal-agreement.md) — related
- [Step-by-step automated annotations accelerated correction of procedural misconceptions, with intervention students rectifying fundamental errors weeks before control peers](automated-annotations-accelerate-misconception-correction.md) — related
- [Instruction that confronts science misconceptions (conceptual-conflict interventions, refutation text) produces conceptual change more often than standard exposition](misconceptions-interfere-with-new-learning.md) — a broader claim this one bears on
- [Machine unlearning induces progressively stronger novice-level performance in an LLM teachable agent, with accuracy and F1 declining as the unlearning ratio increases](unlearning-induces-novice-level-degradation.md) — related
