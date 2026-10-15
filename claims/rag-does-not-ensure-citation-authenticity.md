---
type: claim
title: LLM-generated lessons produced inauthentic references even when combined with RAG over verified academic papers
description: LLM-generated lessons produced inauthentic references even when combined with RAG over verified academic papers
id: rag-does-not-ensure-citation-authenticity
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: jionghao-lin-2025
    resource: "https://doi.org/10.48550/arxiv.2506.17356"
    title: "Jionghao Lin, Jiarui Rao, Sandy Yiyang Zhao, Yuting Wang, Ashish Gurung, Amanda Barany, Jaclyn Ocumpaugh, Ryan S. Baker, and Kenneth R. Koedinger. (2025). Automatic Large Language Models Creation of Interactive Learning Lessons. arXiv preprint. https://arxiv.org/abs/2506.17356 [doi:10.48550/arxiv.2506.17356](https://doi.org/10.48550/arxiv.2506.17356)"
    author: Jionghao Lin, Jiarui Rao, Sandy Yiyang Zhao, Yuting Wang, Ashish Gurung, Amanda Barany, Jaclyn Ocumpaugh, Ryan S. Baker, and Kenneth R. Koedinger
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM-generated lessons produced inauthentic references even when combined with RAG over verified academic papers

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The Conclusion section consistently underperformed in generating authentic references across all segment configurations, even with the three-segment approach combined with RAG. [→ Jionghao Lin 2025](#jionghao-lin-2025)

## Evidence

### Jionghao Lin 2025

Jionghao Lin, Jiarui Rao, Sandy Yiyang Zhao, Yuting Wang, Ashish Gurung, Amanda Barany, Jaclyn Ocumpaugh, Ryan S. Baker, and Kenneth R. Koedinger. (2025). Automatic Large Language Models Creation of Interactive Learning Lessons. arXiv preprint. https://arxiv.org/abs/2506.17356 [doi:10.48550/arxiv.2506.17356](https://doi.org/10.48550/arxiv.2506.17356)

`q2 · i?` · `design · r2`

Consensus ratings (Table 2) show Authenticity of References scored 0/3 for all segmentations except four segments (1/3). The article states the RAG approach "does not inherently address the issue of citation authenticity."

> "Even with the optimal segment configuration (i.e., three segments) combined with the RAG approach—which integrated academic papers containing verified references—the model still produced references that did not exist (see Table A3 in Digital Appendix)."

## Discussion


## Related Claims
- [Of 30 verified hallucinated references, 13 appeared entirely fabricated and 17 were hybrid references combining a real title with fabricated authorship or metadata](hybrid-hallucinated-references-real-title-fake-authors.md) — related
- [Of 100 human-audited claims, 39 are fully verifiable, 55 partially verifiable, and 6 not verifiable, with main responses showing stronger provenance than follow-ups](human-audit-claim-verifiability.md) — related
