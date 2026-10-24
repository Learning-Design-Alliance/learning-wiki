---
type: claim
title: Theoretical quality of agent outputs strongly correlates with benchmark performance (r = 0.656)
description: Theoretical quality of agent outputs strongly correlates with benchmark performance (r = 0.656)
id: theoretical-quality-correlates-benchmark-performance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: younghoon-jeon-2026
    resource: "https://doi.org/10.48550/arxiv.2602.10620"
    title: "YoungHoon Jeon, Suwan Kim, Haein Son, Sookbun Lee, Yeil Jeong, Unggi Lee. (2026). ISD-Agent-Bench: A Comprehensive Benchmark for Evaluating LLM-based Instructional Design Agents. Preprint. https://arxiv.org/abs/2602.10620 [doi:10.48550/arxiv.2602.10620](https://doi.org/10.48550/arxiv.2602.10620)"
    author: YoungHoon Jeon, Suwan Kim, Haein Son, Sookbun Lee, Yeil Jeong, Unggi Lee
    q: 2
    i: 2
    kind: design
    rigour: 2
---

# Theoretical quality of agent outputs strongly correlates with benchmark performance (r = 0.656)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · `i2` medium
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i2` Across agents, theoretical quality scores (Merrill's First Principles and Design Coherence) correlate with benchmark performance, r = 0.656, p < 0.001. [→ YoungHoon Jeon 2026](#younghoon-jeon-2026)

## Evidence

### YoungHoon Jeon 2026

YoungHoon Jeon, Suwan Kim, Haein Son, Sookbun Lee, Yeil Jeong, Unggi Lee. (2026). ISD-Agent-Bench: A Comprehensive Benchmark for Evaluating LLM-based Instructional Design Agents. Preprint. https://arxiv.org/abs/2602.10620 [doi:10.48550/arxiv.2602.10620](https://doi.org/10.48550/arxiv.2602.10620)

`q2 · i2` · `design · r2`

Analysis of 5,345 agent outputs labeled on 9 dimensions (MPI: 5, DC: 4) using GPT-4o-mini with strict 0-3 rubrics; the analysis section reports the correlation "𝑟= 0.656,𝑝< 0.001". EduPlanner showed the highest within-agent correlation (r = 0.312).

> "we find a strong positive correlation between theoretical quality scores and benchmark performance (𝑟= 0.656,𝑝< 0.001), validating that adherence to ISD principles translates to measurable quality improvements."

## Discussion


## Related Claims
- [Activity-Technology alignment is the weakest quality dimension across all agents (mean = 2.19), identifying technology integration as a universal challenge](activity-technology-alignment-weakest-dimension.md) — related
- [Theory-based agents show significantly better Objective-Assessment alignment (d = 0.32), while Content-Activity alignment favors non-theory agents (d = -0.19)](objective-assessment-alignment-theory-advantage.md) — related
- [Theory-based agents significantly outperform non-theory agents on Problem-centered design (d = 0.28) and Activation (d = 0.29), but non-theory agents score higher on Demonstration (d = -0.23)](theory-agents-problem-centered-activation-advantage.md) — related
- [Theoretical quality of both theory-based and non-theory agents remains stable across Easy, Medium, and Hard scenario difficulty levels](theoretical-quality-stable-across-difficulty.md) — related
- [Higher AI pedagogical scores are associated with exercise conversion in real student sessions](pedagogical-score-predicts-exercise-conversion.md) — related
- [The most critical challenge in integrating AI into instructional design is pedagogical alignment (14 of 28 studies, 50.0%)](ai-id-challenge-pedagogical-alignment.md) — related
- [Pedagogical-criterion breakdown shows worked examples in only about 42% of responses, the weakest criterion despite 312 practice problems in the knowledge base](algorag-worked-example-retrieval-42-percent.md) — related
- [React-ADDIE, integrating the ADDIE framework with ReAct-style reasoning, achieves the highest benchmark performance (86.49), outperforming pure theory-based agents and technique-only baselines](react-addie-highest-isd-benchmark-performance.md) — related
- [Coarse-grained tool design (5 phase-level tools) outperforms fine-grained decomposition (14 tools) for LLM-based ISD agents](coarse-grained-phase-level-tools-outperform-fine-grained.md) — related
