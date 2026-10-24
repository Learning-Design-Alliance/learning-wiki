---
type: claim
title: Theory-based agents significantly outperform non-theory agents on Problem-centered design (d = 0.28) and Activation (d = 0.29), but non-theory agents score higher on Demonstration (d = -0.23)
description: Theory-based agents significantly outperform non-theory agents on Problem-centered design (d = 0.28) and Activation (d = 0.29), but non-theory agents score higher on Demonstration (d = -0.23)
id: theory-agents-problem-centered-activation-advantage
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: mixed
newest_evidence: 2026
sources:
  - id: younghoon-jeon-2026
    resource: "https://doi.org/10.48550/arxiv.2602.10620"
    title: "YoungHoon Jeon, Suwan Kim, Haein Son, Sookbun Lee, Yeil Jeong, Unggi Lee. (2026). ISD-Agent-Bench: A Comprehensive Benchmark for Evaluating LLM-based Instructional Design Agents. Preprint. https://arxiv.org/abs/2602.10620 [doi:10.48550/arxiv.2602.10620](https://doi.org/10.48550/arxiv.2602.10620)"
    author: YoungHoon Jeon, Suwan Kim, Haein Son, Sookbun Lee, Yeil Jeong, Unggi Lee
    q: 2
    i: 1
    kind: causal
    rigour: 1
  - id: younghoon-jeon-2026-2
    resource: "https://arxiv.org/abs/2602.10620"
    title: "YoungHoon Jeon, Suwan Kim, Haein Son, Sookbun Lee, Yeil Jeong, Unggi Lee. (2026). ISD-Agent-Bench: A Comprehensive Benchmark for Evaluating LLM-based Instructional Design Agents. Preprint. https://arxiv.org/abs/2602.10620"
    author: YoungHoon Jeon, Suwan Kim, Haein Son, Sookbun Lee, Yeil Jeong, Unggi Lee
    q: 2
    i: 1
    kind: design
    rigour: 2
---

# Theory-based agents significantly outperform non-theory agents on Problem-centered design (d = 0.28) and Activation (d = 0.29), but non-theory agents score higher on Demonstration (d = -0.23)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2` · `i1` small
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i1` Theory-based agents significantly outperform non-theory agents on Problem-centered design (d = 0.28) and Activation of prior knowledge (d = 0.29), both p < 0.001. [→ YoungHoon Jeon 2026](#younghoon-jeon-2026)
`q2 i1` Non-theory agents score higher on Demonstration (d = -0.23, p < 0.001), suggesting a tradeoff between systematic coverage and depth in concrete examples. [→ YoungHoon Jeon 2026 (2)](#younghoon-jeon-2026-2)

## Evidence

### YoungHoon Jeon 2026

YoungHoon Jeon, Suwan Kim, Haein Son, Sookbun Lee, Yeil Jeong, Unggi Lee. (2026). ISD-Agent-Bench: A Comprehensive Benchmark for Evaluating LLM-based Instructional Design Agents. Preprint. https://arxiv.org/abs/2602.10620 [doi:10.48550/arxiv.2602.10620](https://doi.org/10.48550/arxiv.2602.10620)

`q2 · i1` · `causal · r1`

Group comparison of theory-based agents (React-ADDIE, ADDIE-Agent, Dick-Carey, RPISD) versus non-theory agents (Baseline, EduPlanner) across MPI dimensions from the 5,345-output labeling analysis; the printed effect sizes are d = 0.28 and d = 0.29, both p < 0.001.

> "theory-based agents significantly outperform non-theory agents on Problem-centered design (P:𝑑= 0.28) and Activation of prior knowledge (A: 𝑑= 0.29), both𝑝< 0.001."

### YoungHoon Jeon 2026 (2)

YoungHoon Jeon, Suwan Kim, Haein Son, Sookbun Lee, Yeil Jeong, Unggi Lee. (2026). ISD-Agent-Bench: A Comprehensive Benchmark for Evaluating LLM-based Instructional Design Agents. Preprint. https://arxiv.org/abs/2602.10620

`q2 · i1` · `design · r2`

Same MPI dimension comparison; on Demonstration the non-theory group scored higher with d = -0.23, p < 0.001, which the article reads as a tradeoff between systematic coverage and depth in concrete examples.

> "non-theory agents score higher on Demonstration (D:𝑑=− 0.23,𝑝< 0.001), suggesting a tradeoff between systematic coverage and depth in concrete examples."

## Discussion


## Related Claims
- [Theory-based agents show significantly better Objective-Assessment alignment (d = 0.32), while Content-Activity alignment favors non-theory agents (d = -0.19)](objective-assessment-alignment-theory-advantage.md) — related
- [Theoretical quality of agent outputs strongly correlates with benchmark performance (r = 0.656)](theoretical-quality-correlates-benchmark-performance.md) — related
- [Theoretical quality of both theory-based and non-theory agents remains stable across Easy, Medium, and Hard scenario difficulty levels](theoretical-quality-stable-across-difficulty.md) — related
- [React-ADDIE, integrating the ADDIE framework with ReAct-style reasoning, achieves the highest benchmark performance (86.49), outperforming pure theory-based agents and technique-only baselines](react-addie-highest-isd-benchmark-performance.md) — related
