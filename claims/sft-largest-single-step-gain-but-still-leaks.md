---
type: claim
title: "Supervised fine-tuning on SocraticEdu provides the largest single-step SE gain (+0.200) but still leaks target terms in 26.7% of dialogues"
description: "Supervised fine-tuning on SocraticEdu provides the largest single-step SE gain (+0.200) but still leaks target terms in 26.7% of dialogues"
id: sft-largest-single-step-gain-but-still-leaks
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
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

# Supervised fine-tuning on SocraticEdu provides the largest single-step SE gain (+0.200) but still leaks target terms in 26.7% of dialogues

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` SFT alone improves SE from 0.300 to 0.500 over the prompted baseline, yet leaks target terms in 26.7% of dialogues. [→ Xiaokun Wang 2026](#xiaokun-wang-2026)

## Evidence

### Xiaokun Wang 2026

Xiaokun Wang, Siyu Song, Wentao Liu, Xiaodong Zou. (2026). Beyond Direct Answering: Aligning Educational LLMs as Socratic Guides via Heuristic Reinforcement Learning. arXiv preprint. https://arxiv.org/abs/2607.22996 [doi:10.48550/arxiv.2607.22996](https://doi.org/10.48550/arxiv.2607.22996)

`q2 · i?` · `causal · r1`

Training-trajectory analysis of the PT track (RQ1 discussion, Table 3 and Figure 2). The article reports "SFT provides the largest single-step gain inSE(+0.200 over PT-Base)" while leakage remains at 26.7%.

> "SFT provides the largest single-step gain inSE(+0.200 over PT-Base) by instilling basic questioning patterns from SocraticEdu, but it still leaks target terms in 26.7% of dialogues."

## Discussion


## Related Claims
- [GRPO alignment without the directness reward raises Socratic scaffolding effectiveness from 0.300 to 0.633 and cuts keyword leakage from 26.7% to 13.3% on held-out questions](grpo-without-directness-raises-socratic-scaffolding-effectiveness.md) — related
