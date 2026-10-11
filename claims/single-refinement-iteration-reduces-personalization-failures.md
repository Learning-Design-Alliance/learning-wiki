---
type: claim
title: Authenticity and realism are the most frequent failure modes in initial LLM-personalized math problems, and a single refinement iteration substantially reduces failures
description: Authenticity and realism are the most frequent failure modes in initial LLM-personalized math problems, and a single refinement iteration substantially reduces failures
id: single-refinement-iteration-reduces-personalization-failures
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: fareya-ikram-2026
    resource: "https://arxiv.org/abs/2604.05160"
    title: "Fareya Ikram, Nischal Ashok Kumar, Junyang Lu, Hunter McNichols, Candace Walkington, Neil Heffernan, and Andrew S. Lan. (2026). A Multi-Agent Approach to Validate and Refine LLM-Generated Personalized Math Problems. arXiv preprint. https://arxiv.org/abs/2604.05160"
    author: Fareya Ikram, Nischal Ashok Kumar, Junyang Lu, Hunter McNichols, Candace Walkington, Neil Heffernan, and Andrew S. Lan
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# Authenticity and realism are the most frequent failure modes in initial LLM-personalized math problems, and a single refinement iteration substantially reduces failures

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`

## Subclaims
`q2 i?` Most quality improvements in LLM-personalized math problems occur in the first refinement iteration, with substantially reduced validator failure counts after one generate–validate–revise cycle. [→ Fareya Ikram 2026](#fareya-ikram-2026)

## Evidence

### Fareya Ikram 2026

Fareya Ikram, Nischal Ashok Kumar, Junyang Lu, Hunter McNichols, Candace Walkington, Neil Heffernan, and Andrew S. Lan. (2026). A Multi-Agent Approach to Validate and Refine LLM-Generated Personalized Math Problems. arXiv preprint. https://arxiv.org/abs/2604.05160

`q2 · i?` · `design · r3`

Quantitative analysis of validator agent failure counts across three refinement iterations, aggregated over 600 ASSISTments problems personalized to a fixed set of 20 student interest topics, shown in Fig. 2 for three strategies. The authors observe that "most improvements occur early on, with substantial reductions in failure counts after the first refinement iteration." No effect size is printed.

> "We observe that most improvements occur early on, with substantial reductions in failure counts after the first refinement iteration."

## Discussion


## Related Claims
- [Centralized Refinement with Planning converges fastest and to the lowest failure count on authenticity](centralized-planning-converges-fastest-on-authenticity.md) — related
- [Decentralized Refinement reduces realism and readability failures faster than both Centralized strategies](decentralized-refinement-faster-on-realism-readability.md) — a narrower finding that bears on this claim
- [Validator failure patterns vary by interest topic and math curriculum unit](failure-patterns-vary-by-topic-and-curriculum-unit.md) — a narrower finding that bears on this claim
- [The three refinement strategies make distinct trade-offs when personalizing problems to topics that resist natural alignment with the original math](refinement-strategy-trade-offs-in-case-analysis.md) — related
- [Validator agent reliability is highest for realism and lowest for authenticity in human evaluation](validator-reliability-highest-realism-lowest-authenticity.md) — related
- [Instructors engage LLM-generated suggestions as a controllable refinement process](instructors-use-llm-suggestions-as-controllable-refinement.md) — related
