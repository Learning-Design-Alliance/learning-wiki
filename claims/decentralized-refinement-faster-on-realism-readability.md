---
type: claim
title: Decentralized Refinement reduces realism and readability failures faster than both Centralized strategies
description: Decentralized Refinement reduces realism and readability failures faster than both Centralized strategies
id: decentralized-refinement-faster-on-realism-readability
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: fareya-ikram-2026
    resource: "https://doi.org/10.48550/arxiv.2604.05160"
    title: "Fareya Ikram, Nischal Ashok Kumar, Junyang Lu, Hunter McNichols, Candace Walkington, Neil Heffernan, and Andrew S. Lan. (2026). A Multi-Agent Approach to Validate and Refine LLM-Generated Personalized Math Problems. arXiv preprint. https://arxiv.org/abs/2604.05160 [doi:10.48550/arxiv.2604.05160](https://doi.org/10.48550/arxiv.2604.05160)"
    author: Fareya Ikram, Nischal Ashok Kumar, Junyang Lu, Hunter McNichols, Candace Walkington, Neil Heffernan, and Andrew S. Lan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Decentralized Refinement reduces realism and readability failures faster than both Centralized strategies

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` For realism and readability, Decentralized Refinement converges to a low failure count faster than both Centralized strategies, achieving minimal failure counts by the second refinement iteration. [→ Fareya Ikram 2026](#fareya-ikram-2026)

## Evidence

### Fareya Ikram 2026

Fareya Ikram, Nischal Ashok Kumar, Junyang Lu, Hunter McNichols, Candace Walkington, Neil Heffernan, and Andrew S. Lan. (2026). A Multi-Agent Approach to Validate and Refine LLM-Generated Personalized Math Problems. arXiv preprint. https://arxiv.org/abs/2604.05160 [doi:10.48550/arxiv.2604.05160](https://doi.org/10.48550/arxiv.2604.05160)

`q2 · i?` · `causal · r2`

Comparison of three refinement strategies on 600 ASSISTments problems under identical settings (maximum of k=3 refinement iterations, GPT-5.2 with temperature= 0), with failure counts plotted in Fig. 2. The article reports the convergence contrast between Decentralized Refinement and the two Centralized strategies for realism and readability; no effect size is printed.

> "For realism and readability, we observe that Decentralized Refinement converges to a low failure count faster than both Centralized strategies, achieving minimal failure counts by the second refinement iteration."

## Discussion


## Related Claims
- [Centralized Refinement with Planning converges fastest and to the lowest failure count on authenticity](centralized-planning-converges-fastest-on-authenticity.md) — related
- [Authenticity and realism are the most frequent failure modes in initial LLM-personalized math problems, and a single refinement iteration substantially reduces failures](single-refinement-iteration-reduces-personalization-failures.md) — a broader claim this one bears on
- [The three refinement strategies make distinct trade-offs when personalizing problems to topics that resist natural alignment with the original math](refinement-strategy-trade-offs-in-case-analysis.md) — related
- [Validator failure patterns vary by interest topic and math curriculum unit](failure-patterns-vary-by-topic-and-curriculum-unit.md) — related
