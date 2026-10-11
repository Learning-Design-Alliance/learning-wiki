---
type: claim
title: React-ADDIE, integrating the ADDIE framework with ReAct-style reasoning, achieves the highest benchmark performance (86.49), outperforming pure theory-based agents and technique-only baselines
description: React-ADDIE, integrating the ADDIE framework with ReAct-style reasoning, achieves the highest benchmark performance (86.49), outperforming pure theory-based agents and technique-only baselines
id: react-addie-highest-isd-benchmark-performance
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: younghoon-jeon-2026
    resource: "https://arxiv.org/abs/2602.10620"
    title: "YoungHoon Jeon, Suwan Kim, Haein Son, Sookbun Lee, Yeil Jeong, Unggi Lee. (2026). ISD-Agent-Bench: A Comprehensive Benchmark for Evaluating LLM-based Instructional Design Agents. Preprint. https://arxiv.org/abs/2602.10620"
    author: YoungHoon Jeon, Suwan Kim, Haein Son, Sookbun Lee, Yeil Jeong, Unggi Lee
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# React-ADDIE, integrating the ADDIE framework with ReAct-style reasoning, achieves the highest benchmark performance (86.49), outperforming pure theory-based agents and technique-only baselines

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` On 1,017 test scenarios evaluated with three LLMs, React-ADDIE achieves the highest mean score (86.49) versus ADDIE-Agent (82.96) and Baseline (84.07). [→ YoungHoon Jeon 2026](#younghoon-jeon-2026)

## Evidence

### YoungHoon Jeon 2026

YoungHoon Jeon, Suwan Kim, Haein Son, Sookbun Lee, Yeil Jeong, Unggi Lee. (2026). ISD-Agent-Bench: A Comprehensive Benchmark for Evaluating LLM-based Instructional Design Agents. Preprint. https://arxiv.org/abs/2602.10620

`q2 · i?` · `causal · r1`

Benchmark experiment on 1,017 test scenarios with three base LLMs (Gemini-3-Flash, GPT-5-mini, Solar-Pro3), scored by a cross-provider multi-judge protocol. The results section reports "React-ADDIE achieves the highest mean score (86.49)" with the named comparison agents' scores as printed.

> "React-ADDIE's integration of ADDIE theory with ReAct-style reasoning outperforms both pure theory-based agents (ADDIE-Agent: 82.96, which uses the same ADDIE framework but with fine-grained 14-tool decomposition) and technique-only approaches (Baseline: 84.07)."

## Discussion


## Related Claims
- [Coarse-grained tool design (5 phase-level tools) outperforms fine-grained decomposition (14 tools) for LLM-based ISD agents](coarse-grained-phase-level-tools-outperform-fine-grained.md) — related
- [Agentic frameworks built on GPT-3.5 and GPT-4 show significant performance gains on the HumanEval benchmark over zero-shot baselines](agentic-frameworks-humaneval-gains.md) — a broader claim this one bears on
