---
type: claim
title: "A three-system human pilot (n=30) validates the VLM learner proxy: significant human posttest gain, 85.7% directional agreement, and perfect cross-system ranking consistency"
description: "A three-system human pilot (n=30) validates the VLM learner proxy: significant human posttest gain, 85.7% directional agreement, and perfect cross-system ranking consistency"
id: slate-vlm-proxy-human-pilot-validation
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
    q: 3
    i: "?"
    kind: design
    rigour: 2
  - id: jingzhuo-wu-2026-2
    resource: "https://doi.org/10.48550/arXiv.2609.06212"
    title: "Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang. (2026). SLATE: Are AI-Generated Slides Educationally Effective? A Benchmark for Language Teaching Quality and Learner Knowledge Acquisition. arXiv preprint arXiv:2609.06212. [doi:10.48550/arXiv.2609.06212](https://doi.org/10.48550/arXiv.2609.06212)"
    author: Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# A three-system human pilot (n=30) validates the VLM learner proxy: significant human posttest gain, 85.7% directional agreement, and perfect cross-system ranking consistency

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`–`q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Human learners show a significant overall posttest gain (t(29)=6.78, p<0.001), with 85.7% per-puzzle directional agreement and perfect cross-system ranking consistency (Spearman ρ=1.0) with VLM results. [→ Jingzhuo Wu 2026](#jingzhuo-wu-2026)
`q2 i?` In a content perturbation control replacing teaching content with unrelated-language material, posttest gains fall below the zero-information baseline, supporting that observed gains are content-driven. [→ Jingzhuo Wu 2026 (2)](#jingzhuo-wu-2026-2)

## Evidence

### Jingzhuo Wu 2026

Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang. (2026). SLATE: Are AI-Generated Slides Educationally Effective? A Benchmark for Language Teaching Quality and Learner Knowledge Acquisition. arXiv preprint arXiv:2609.06212. [doi:10.48550/arXiv.2609.06212](https://doi.org/10.48550/arXiv.2609.06212)

`q3 · i?` · `design · r2`

Three-system human pilot with 30 participants covering high-gain Claude Opus 4.7, intermediate-gain Claude Sonnet 4.6, and negative-gain Gemini-3.1-Pro decks; "85.7% per-puzzle directional agreement" with the VLM proxy.

> "Human learners show a significant overall posttest gain ( t(29) = 6.78, p < 0.001), with 85.7% per-puzzle directional agreement and perfect cross-system ranking consistency (Spearman ρ= 1.0) between VLM and human results."

### Jingzhuo Wu 2026 (2)

Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang. (2026). SLATE: Are AI-Generated Slides Educationally Effective? A Benchmark for Language Teaching Quality and Learner Knowledge Acquisition. arXiv preprint arXiv:2609.06212. [doi:10.48550/arXiv.2609.06212](https://doi.org/10.48550/arXiv.2609.06212)

`q2 · i?` · `causal · r1`

Content perturbation control preserving slide structure and visual design while replacing teaching content with unrelated-language material; gains "fall below the zero-information baseline", distinguishing genuine learning from contextual priming.

> "Under this condition, posttest gains fall below the zero-information baseline, con- firming that observed gains are content-driven."

## Discussion


## Related Claims
- [The cross-family LLM judge panel agrees with human domain experts on every judged axis, reaching the expert ceiling on answer-holding](educlaw-bench-judge-panel-human-validation.md) — a broader claim this one bears on
- [Gemini 2.0 Flash validated as a reliable LLM annotator of feedback focus types](gemini-flash-reliable-feedback-focus-annotator.md) — related
