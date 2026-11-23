---
type: claim
title: "Human learners' knowledge states subsume weaker learners' nearly perfectly, while LLMs show substantially lower and more fragmented subsumption"
description: "Human learners' knowledge states subsume weaker learners' nearly perfectly, while LLMs show substantially lower and more fragmented subsumption"
id: llms-lack-coherent-knowledge-subsumption
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: peng-cui-2026
    resource: "https://doi.org/10.18653/2026.findings-emnlp.494"
    title: "Peng Cui, Heejin Do, and Mrinmaya Sachan. (2026). Do LLMs Exhibit Coherent Knowledge Structures in Mathematical Reasoning? A Perspective from Knowledge Space Theory. arXiv. [doi:10.18653/2026.findings-emnlp.494](https://doi.org/10.18653/2026.findings-emnlp.494)"
    author: Peng Cui, Heejin Do, and Mrinmaya Sachan
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: peng-cui-2026-2
    resource: "https://doi.org/10.18653/2026.findings-emnlp.494"
    title: "Peng Cui, Heejin Do, and Mrinmaya Sachan. (2026). Do LLMs Exhibit Coherent Knowledge Structures in Mathematical Reasoning? A Perspective from Knowledge Space Theory. arXiv. [doi:10.18653/2026.findings-emnlp.494](https://doi.org/10.18653/2026.findings-emnlp.494)"
    author: Peng Cui, Heejin Do, and Mrinmaya Sachan
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Human learners' knowledge states subsume weaker learners' nearly perfectly, while LLMs show substantially lower and more fragmented subsumption

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Human learner groups of different performance levels exhibit high normalized knowledge overlap, whereas LLM–human overlap is substantially lower and stronger models show even less alignment with human learners. [→ Peng Cui 2026](#peng-cui-2026)
`q2 i?` Closed-source models (GPT-4.1-MINI and Claude) show considerably lower overlap with open-source models and only 0.38 overlap with each other, suggesting LLMs do not share one consistent knowledge structure. [→ Peng Cui 2026 (2)](#peng-cui-2026-2)

## Evidence

### Peng Cui 2026

Peng Cui, Heejin Do, and Mrinmaya Sachan. (2026). Do LLMs Exhibit Coherent Knowledge Structures in Mathematical Reasoning? A Perspective from Knowledge Space Theory. arXiv. [doi:10.18653/2026.findings-emnlp.494](https://doi.org/10.18653/2026.findings-emnlp.494)

`q2 · i?` · `associational · r2`

Numerical analysis of normalized Knowledge Overlap Coefficients (Eq. 7) between knowledge states of eight LLMs and simulated human ability groups (accuracy 0.64, 0.80, 0.89) drawn from student logs. The article reports human learner groups exhibit high overlap consistent with structured subsumption, while this LLM–human overlap is "substantially lower".

> "the overlap between LLMs and human learners (upper-right) is substantially lower, and stronger models appear to show even less alignment with human learners."

### Peng Cui 2026 (2)

Peng Cui, Heejin Do, and Mrinmaya Sachan. (2026). Do LLMs Exhibit Coherent Knowledge Structures in Mathematical Reasoning? A Perspective from Knowledge Space Theory. arXiv. [doi:10.18653/2026.findings-emnlp.494](https://doi.org/10.18653/2026.findings-emnlp.494)

`q2 · i?` · `associational · r2`

Pairwise normalized KOC comparison among the evaluated LLMs. Open-source models share relatively strong mutual overlap, but the article attributes the closed-source divergence to shared training corpora among open-source models versus "more diverse and proprietary data sources" for closed-source models.

> "the two closed-source models, GPT-4.1-MINIand CLAUDE, show considerably lower overlap with open-source models, and only 0.38 overlap with each other."

## Discussion


## Related Claims
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
- [Score variance differed markedly: Olympiad participants' scores showed substantially higher variance than LLM scores, with o1-preview's scores the most narrowly distributed](score-variance-students-higher-than-llms.md) — related
- [ZPDs of different LLMs differ significantly: Z✗→✓ and Z✗→✗ examples overlap little across models while Z✓ examples are largely shared](zpd-overlap-low-across-models.md) — related
