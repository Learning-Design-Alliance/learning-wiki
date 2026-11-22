---
type: claim
title: "Four of 10 frontier systems produce negative learning gains, and all systems with visual aid completeness below 80% produce negative gains"
description: "Four of 10 frontier systems produce negative learning gains, and all systems with visual aid completeness below 80% produce negative gains"
id: slate-negative-gains-low-visual-completeness
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: jingzhuo-wu-2026
    resource: "https://doi.org/10.48550/arXiv.2609.06212"
    title: "Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang. (2026). SLATE: Are AI-Generated Slides Educationally Effective? A Benchmark for Language Teaching Quality and Learner Knowledge Acquisition. arXiv preprint arXiv:2609.06212. [doi:10.48550/arXiv.2609.06212](https://doi.org/10.48550/arXiv.2609.06212)"
    author: Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: jingzhuo-wu-2026-2
    resource: "https://doi.org/10.48550/arXiv.2609.06212"
    title: "Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang. (2026). SLATE: Are AI-Generated Slides Educationally Effective? A Benchmark for Language Teaching Quality and Learner Knowledge Acquisition. arXiv preprint arXiv:2609.06212. [doi:10.48550/arXiv.2609.06212](https://doi.org/10.48550/arXiv.2609.06212)"
    author: Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Four of 10 frontier systems produce negative learning gains, and all systems with visual aid completeness below 80% produce negative gains

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Four systems produce negative gains on D4, a failure mode the article says artifact-based rubrics do not detect. [→ Jingzhuo Wu 2026](#jingzhuo-wu-2026)
`q2 i?` Visual aid completeness appears necessary: all systems with VA%<80% produce negative gains. [→ Jingzhuo Wu 2026 (2)](#jingzhuo-wu-2026-2)

## Evidence

### Jingzhuo Wu 2026

Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang. (2026). SLATE: Are AI-Generated Slides Educationally Effective? A Benchmark for Language Teaching Quality and Learner Knowledge Acquisition. arXiv preprint arXiv:2609.06212. [doi:10.48550/arXiv.2609.06212](https://doi.org/10.48550/arXiv.2609.06212)

`q2 · i?` · `design · r2`

Main results (Table 3): D4 gains measured against the 23.78% pretest baseline show negative gains for Kimi-K2.6, GLM-5.1, DeepSeek-V4-Pro, and Gemini-3.1-Pro, down to "↓2.51" for Gemini-3.1-Pro.

> "Four systems produce negative gains, confirming that SLATE discriminates systems on instructional effectiveness rather than artifact plausibility alone."

### Jingzhuo Wu 2026 (2)

Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang. (2026). SLATE: Are AI-Generated Slides Educationally Effective? A Benchmark for Language Teaching Quality and Learner Knowledge Acquisition. arXiv preprint arXiv:2609.06212. [doi:10.48550/arXiv.2609.06212](https://doi.org/10.48550/arXiv.2609.06212)

`q2 · i?` · `design · r2`

Observation across the 10 systems in Table 3 relating D3 visual aid completeness (VA%) to D4 gain: every system with "V A%<80%" produced a negative gain, though visual completeness alone does not explain the dissociation.

> "This dissociation is not explained by visual design alone, though visual completeness appears necessary: all systems with V A%<80% produce negative gains."

## Discussion


## Related Claims
- [Across 10 frontier slide-generation systems, pedagogical design (D2) correlates more strongly with learning gain (ρ=0.72) than content validity (D1, ρ=0.38)](slate-d2-pedagogical-design-gain-correlation.md) — related
- [An exploratory LLM-judge audit labels knowledge gaps (39.1%) and reasoning errors (26.9%) as the most frequent failure modes among incorrect frontier-model responses](llm-judge-audit-failure-modes.md) — related
