---
type: claim
title: "Across three neural-network lectures, evidence and confidence checks retained 1,022 of 1,155 raw concept mentions (88.48%) and 312 of 400 raw relationship mentions (78.00%), yielding 172 canonical concepts and 282 graph relationships with 90.38% endpoint coverage"
description: "Across three neural-network lectures, evidence and confidence checks retained 1,022 of 1,155 raw concept mentions (88.48%) and 312 of 400 raw relationship mentions (78.00%), yielding 172 canonical concepts and 282 gra..."
id: evidence-grounded-kg-extraction-yield-three-lectures
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: sahil-al-farib-2026
    resource: "https://doi.org/10.48550/arxiv.2608.03161"
    title: "Sahil Al Farib, Momota Ahsana Meem, Sheikh Redwanul Islam, and Md. Tanvir Raihan. (2026). Evidence-Grounded Multimodal Knowledge Graph Construction for Multi-Lecture Educational Reasoning. https://arxiv.org/abs/2608.03161 [doi:10.48550/arxiv.2608.03161](https://doi.org/10.48550/arxiv.2608.03161)"
    author: Sahil Al Farib, Momota Ahsana Meem, Sheikh Redwanul Islam, and Md. Tanvir Raihan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Across three neural-network lectures, evidence and confidence checks retained 1,022 of 1,155 raw concept mentions (88.48%) and 312 of 400 raw relationship mentions (78.00%), yielding 172 canonical concepts and 282 graph relationships with 90.38% endpoint coverage

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Validation and canonicalization reduced 1,155 raw concept mentions to 172 canonical concepts and 400 raw relationship mentions to 282 final edges, retaining 88.48% of concepts and 78.00% of relationships at validation and 90.38% endpoint coverage after mapping. [→ Sahil Al Farib 2026](#sahil-al-farib-2026)

## Evidence

### Sahil Al Farib 2026

Sahil Al Farib, Momota Ahsana Meem, Sheikh Redwanul Islam, and Md. Tanvir Raihan. (2026). Evidence-Grounded Multimodal Knowledge Graph Construction for Multi-Lecture Educational Reasoning. https://arxiv.org/abs/2608.03161 [doi:10.48550/arxiv.2608.03161](https://doi.org/10.48550/arxiv.2608.03161)

`q2 · i?` · `design · r2`

Numerical results from the pipeline's final run over three lectures, reported in the Results section and Table III. The article states the reduction from 1,022 mentions to 172 nodes "is expected because course concepts recur across anchors and lectures."

> "The VLM returned 1,155 raw concept and 400 raw relationship mentions. Evidence and confidence checks retained 1,022 concepts (88.48%) and 312 relationships (78.00%). Canonicalization produced 172 concepts, and endpoint mapping retained 282 edges (90.38% of validated relationships)"

## Discussion


## Related Claims
- [On a preliminary three-question retrieval sanity check, all seed questions placed their target concept first and within the top three, with mean top-5 recall of 1.00](three-seed-retrieval-sanity-check-perfect.md) — related
