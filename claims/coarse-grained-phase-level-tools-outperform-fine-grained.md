---
type: claim
title: Coarse-grained tool design (5 phase-level tools) outperforms fine-grained decomposition (14 tools) for LLM-based ISD agents
description: Coarse-grained tool design (5 phase-level tools) outperforms fine-grained decomposition (14 tools) for LLM-based ISD agents
id: coarse-grained-phase-level-tools-outperform-fine-grained
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: younghoon-jeon-2026
    resource: "https://doi.org/10.48550/arxiv.2602.10620"
    title: "YoungHoon Jeon, Suwan Kim, Haein Son, Sookbun Lee, Yeil Jeong, Unggi Lee. (2026). ISD-Agent-Bench: A Comprehensive Benchmark for Evaluating LLM-based Instructional Design Agents. Preprint. https://arxiv.org/abs/2602.10620 [doi:10.48550/arxiv.2602.10620](https://doi.org/10.48550/arxiv.2602.10620)"
    author: YoungHoon Jeon, Suwan Kim, Haein Son, Sookbun Lee, Yeil Jeong, Unggi Lee
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Coarse-grained tool design (5 phase-level tools) outperforms fine-grained decomposition (14 tools) for LLM-based ISD agents

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` A 5 phase-level-tool agent (React-ADDIE) scored higher than the same-theory 14-tool agent (ADDIE-Agent: 82.96). [→ YoungHoon Jeon 2026](#younghoon-jeon-2026)

## Evidence

### YoungHoon Jeon 2026

YoungHoon Jeon, Suwan Kim, Haein Son, Sookbun Lee, Yeil Jeong, Unggi Lee. (2026). ISD-Agent-Bench: A Comprehensive Benchmark for Evaluating LLM-based Instructional Design Agents. Preprint. https://arxiv.org/abs/2602.10620 [doi:10.48550/arxiv.2602.10620](https://doi.org/10.48550/arxiv.2602.10620)

`q2 · i?` · `causal · r1`

Comparison within the benchmark experiment between React-ADDIE (5 phase-level tools) and ADDIE-Agent (14 specialized tools with fine-grained phase decomposition), both grounded in ADDIE; the conclusion states the coarse-grained design "outperforms fine-grained decomposition (14 tools)".

> "A key finding is that coarse-grained tool design (5 phase-level tools) outperforms fine-grained decomposition (14 tools), suggesting that holistic reasoning with systematic structure yields optimal results."

## Discussion


## Related Claims
- [React-ADDIE, integrating the ADDIE framework with ReAct-style reasoning, achieves the highest benchmark performance (86.49), outperforming pure theory-based agents and technique-only baselines](react-addie-highest-isd-benchmark-performance.md) — related
- [Theoretical quality of both theory-based and non-theory agents remains stable across Easy, Medium, and Hard scenario difficulty levels](theoretical-quality-stable-across-difficulty.md) — related
- [Theoretical quality of agent outputs strongly correlates with benchmark performance (r = 0.656)](theoretical-quality-correlates-benchmark-performance.md) — related
