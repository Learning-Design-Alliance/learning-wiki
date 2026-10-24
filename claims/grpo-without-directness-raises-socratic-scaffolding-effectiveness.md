---
type: claim
title: "GRPO alignment without the directness reward raises Socratic scaffolding effectiveness from 0.300 to 0.633 and cuts keyword leakage from 26.7% to 13.3% on held-out questions"
description: "GRPO alignment without the directness reward raises Socratic scaffolding effectiveness from 0.300 to 0.633 and cuts keyword leakage from 26.7% to 13.3% on held-out questions"
id: grpo-without-directness-raises-socratic-scaffolding-effectiveness
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-10-17
sources:
  - id: xiaokun-wang-2026
    resource: "https://doi.org/10.48550/arxiv.2607.22996"
    title: "Xiaokun Wang, Siyu Song, Wentao Liu, Xiaodong Zou. (2026). Beyond Direct Answering: Aligning Educational LLMs as Socratic Guides via Heuristic Reinforcement Learning. arXiv preprint. https://arxiv.org/abs/2607.22996 [doi:10.48550/arxiv.2607.22996](https://doi.org/10.48550/arxiv.2607.22996)"
    author: Xiaokun Wang, Siyu Song, Wentao Liu, Xiaodong Zou
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# GRPO alignment without the directness reward raises Socratic scaffolding effectiveness from 0.300 to 0.633 and cuts keyword leakage from 26.7% to 13.3% on held-out questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-17 (automated, 1 of 1 entry) · not reviewed by a person

## Subclaims
`q2 i?` On 30 held-out questions, PT-GRPO w/o Rdir reaches SE=0.633 with 13.3% leakage, up from PT-Base's SE=0.300 with 30.0% leakage. [→ Xiaokun Wang 2026](#xiaokun-wang-2026)

## Evidence

### Xiaokun Wang 2026

Xiaokun Wang, Siyu Song, Wentao Liu, Xiaodong Zou. (2026). Beyond Direct Answering: Aligning Educational LLMs as Socratic Guides via Heuristic Reinforcement Learning. arXiv preprint. https://arxiv.org/abs/2607.22996 [doi:10.48550/arxiv.2607.22996](https://doi.org/10.48550/arxiv.2607.22996)

`q2 · i?` · `causal · r1`

Simulation-based evaluation on 30 held-out seed questions in a four-turn LLM-simulated tutoring loop, comparing PT-track systems. The article reports "GRPO without Rdir further raises SE to 0.633" with leakage cut to 13.3%; per-run SE variance is stated as roughly ±0.10.

> "Within the PT track, alignment yields a generally improving pattern: prompt-only PT-Base reaches SE=0.300; SFT alone improves to 0.500; GRPO without Rdir further raises SE to 0.633 while cutting leakage from 26.7% to 13.3%."

## Discussion


## Related Claims
- [Using the directness penalty Rdir as a GRPO reward is counterproductive: it lowers SE by 0.200 and raises leakage by 10 percentage points relative to omitting it](directness-penalty-harmful-as-grpo-reward.md) — related
- [Gradient-based GRPO alignment of a 7B model outperforms prompt engineering on scaffolding effectiveness (0.633 vs 0.400) despite the smaller backbone](grpo-parameter-training-beats-prompt-engineering-socratic.md) — related
- [The best GRPO variant also achieves the highest Conversation Depth (0.722), suggesting stronger scaffolding accompanies deeper semantic progression](grpo-without-directness-highest-conversation-depth.md) — related
- [Supervised fine-tuning on SocraticEdu provides the largest single-step SE gain (+0.200) but still leaks target terms in 26.7% of dialogues](sft-largest-single-step-gain-but-still-leaks.md) — related
- [GRPO alignment collapses Mathematical-Knowledge-for-Teaching utterances and surges Socratic-style Exploratory questions in tutor output](alignment-shifts-mkt-collapse-exploratory-surge.md) — related
- [Model scale alone does not induce Socratic behavior: unaligned Qwen-72B achieves 0% scaffolding effectiveness and 96.7% keyword leakage](scale-alone-does-not-induce-socratic-behavior.md) — related
