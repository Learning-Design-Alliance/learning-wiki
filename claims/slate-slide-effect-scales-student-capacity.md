---
type: claim
title: "In the ablation study, slide effects scale with student-model capacity (negative ↓1.4% for the 3B model), puzzle context is the strongest factor, and full-frame presentation outperforms 3-frame sampling by ~3%"
description: "In the ablation study, slide effects scale with student-model capacity (negative ↓1.4% for the 3B model), puzzle context is the strongest factor, and full-frame presentation outperforms 3-frame sampling by ~3%"
id: slate-slide-effect-scales-student-capacity
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: jingzhuo-wu-2026
    resource: "https://doi.org/10.48550/arXiv.2609.06212"
    title: "Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang. (2026). SLATE: Are AI-Generated Slides Educationally Effective? A Benchmark for Language Teaching Quality and Learner Knowledge Acquisition. arXiv preprint arXiv:2609.06212. [doi:10.48550/arXiv.2609.06212](https://doi.org/10.48550/arXiv.2609.06212)"
    author: Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: jingzhuo-wu-2026-2
    resource: "https://doi.org/10.48550/arXiv.2609.06212"
    title: "Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang. (2026). SLATE: Are AI-Generated Slides Educationally Effective? A Benchmark for Language Teaching Quality and Learner Knowledge Acquisition. arXiv preprint arXiv:2609.06212. [doi:10.48550/arXiv.2609.06212](https://doi.org/10.48550/arXiv.2609.06212)"
    author: Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: jingzhuo-wu-2026-3
    resource: "https://doi.org/10.48550/arXiv.2609.06212"
    title: "Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang. (2026). SLATE: Are AI-Generated Slides Educationally Effective? A Benchmark for Language Teaching Quality and Learner Knowledge Acquisition. arXiv preprint arXiv:2609.06212. [doi:10.48550/arXiv.2609.06212](https://doi.org/10.48550/arXiv.2609.06212)"
    author: Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# In the ablation study, slide effects scale with student-model capacity (negative ↓1.4% for the 3B model), puzzle context is the strongest factor, and full-frame presentation outperforms 3-frame sampling by ~3%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · causal `r1`–`r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Slide effects scale monotonically with student VLM capacity: ↓1.4% for Qwen2.5-VL-3B, then ↑4.3, ↑4.0, and ↑5.0% for larger models, consistent with the expertise reversal effect. [→ Jingzhuo Wu 2026](#jingzhuo-wu-2026)
`q2 i?` Puzzle context is the strongest single factor (↑5.6 to ↑12.5%), but slides alone partially compensate for missing context (↑4.1 to ↑10.0% over the zero-information baseline). [→ Jingzhuo Wu 2026 (2)](#jingzhuo-wu-2026-2)
`q2 i?` Full-frame presentation outperforms 3-frame sampling by ~3%, indicating intermediate slides contain valuable instructional content. [→ Jingzhuo Wu 2026 (3)](#jingzhuo-wu-2026-3)

## Evidence

### Jingzhuo Wu 2026

Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang. (2026). SLATE: Are AI-Generated Slides Educationally Effective? A Benchmark for Language Teaching Quality and Learner Knowledge Acquisition. arXiv preprint arXiv:2609.06212. [doi:10.48550/arXiv.2609.06212](https://doi.org/10.48550/arXiv.2609.06212)

`q2 · i?` · `causal · r1`

Controlled ablation with four student VLMs across six conditions using Claude Opus 4.7 slides (Table 4); the smallest model shows a negative slide effect and the trend is "systematic and capacity-dependent".

> "The monotonic scaling of slide effects across the four models ( ↓ 1.4, ↑ 4.3, ↑ 4.0, ↑ 5.0%) rules out the possibility that the 8B result is an isolated artifact: the trend is systematic and capacity-dependent."

### Jingzhuo Wu 2026 (2)

Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang. (2026). SLATE: Are AI-Generated Slides Educationally Effective? A Benchmark for Language Teaching Quality and Learner Knowledge Acquisition. arXiv preprint arXiv:2609.06212. [doi:10.48550/arXiv.2609.06212](https://doi.org/10.48550/arXiv.2609.06212)

`q2 · i?` · `causal · r2`

Effect decomposition in the same ablation (Table 4, Figure 3): context effects of "↑ 5.6 to ↑ 12.5%" exceed slide-only compensation effects of "↑ 4.1 to ↑ 10.0%" across the four student models.

> "Second, puzzle context is the strongest single factor (↑ 5.6 to ↑ 12.5%), but slides alone can partially compensate for missing context (↑ 4.1 to ↑ 10.0% gain over zero-information baseline)."

### Jingzhuo Wu 2026 (3)

Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang. (2026). SLATE: Are AI-Generated Slides Educationally Effective? A Benchmark for Language Teaching Quality and Learner Knowledge Acquisition. arXiv preprint arXiv:2609.06212. [doi:10.48550/arXiv.2609.06212](https://doi.org/10.48550/arXiv.2609.06212)

`q2 · i?` · `causal · r2`

Condition comparison B versus V3 in the ablation (Table 4): full-frame decks beat 3-frame sampling "by ∼3%" for the larger student models, though the 3B model shows ↓0.2.

> "Third, full-frame presentation outper- forms 3-frame sampling by ∼3%, confirming that intermediate slides contain valuable instructional content."

## Discussion


## Related Claims
- [CDPK performance scales with model size, with a sharp Pareto-frontier drop-off below around 8B parameters](cdpk-scales-with-model-size-dropoff-below-8b.md) — related
