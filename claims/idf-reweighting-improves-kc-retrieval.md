---
type: claim
title: IDF reweighting of knowledge vectors improves retrieval over binary KC-incidence vectors, with the largest gains in mAP
description: IDF reweighting of knowledge vectors improves retrieval over binary KC-incidence vectors, with the largest gains in mAP
id: idf-reweighting-improves-kc-retrieval
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: muntasir-hoq-2026
    resource: "https://doi.org/10.48550/arxiv.2607.05409"
    title: "Muntasir Hoq, Griffin Pitts, Zhangqi Duan, Arun Balajiee Lekshmi Narayanan, Mohammad Hassany, Andrew Lan, Peter Brusilovsky and Bita Akram. (2026). Automated Recommendation of Programming Learning Content Using Pattern-based Knowledge Components. CSEDM'26: 10th Educational Data Mining in Computer Science Education Workshop. https://arxiv.org/abs/2607.05409 [doi:10.48550/arxiv.2607.05409](https://doi.org/10.48550/arxiv.2607.05409)"
    author: Muntasir Hoq, Griffin Pitts, Zhangqi Duan, Arun Balajiee Lekshmi Narayanan, Mohammad Hassany, Andrew Lan, Peter Brusilovsky and Bita Akram
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# IDF reweighting of knowledge vectors improves retrieval over binary KC-incidence vectors, with the largest gains in mAP

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Removing IDF reweighting lowered challenge retrieval to Top-5 85%, MRR 75%, and mAP 68%, so IDF yielded gains of +5, +5, and +11 percentage points respectively. [→ Muntasir Hoq 2026](#muntasir-hoq-2026)

## Evidence

### Muntasir Hoq 2026

Muntasir Hoq, Griffin Pitts, Zhangqi Duan, Arun Balajiee Lekshmi Narayanan, Mohammad Hassany, Andrew Lan, Peter Brusilovsky and Bita Akram. (2026). Automated Recommendation of Programming Learning Content Using Pattern-based Knowledge Components. CSEDM'26: 10th Educational Data Mining in Computer Science Education Workshop. https://arxiv.org/abs/2607.05409 [doi:10.48550/arxiv.2607.05409](https://doi.org/10.48550/arxiv.2607.05409)

`q2 · i?` · `design · r2`

Ablation study on the PCEX corpus replacing IDF-weighted knowledge vectors with binary KC-incidence vectors. The article reports the printed percentage-point gains and interprets them as "supporting the value of down-weighting ubiquitous KCs".

> "For challenge retrieval, IDF yields a +5 pp gain in Top-5 accuracy (90% vs. 85%), a +5% pp gain in MRR (80% vs. 75%), and a +11pp gain in mAP (79% vs.68%), supporting the value of down-weighting ubiquitous KCs."

## Discussion


## Related Claims
- [Pattern-based KC similarity retrieves bundle-aligned programming learning items better than code-embedding and other KC baselines in both retrieval directions](pattern-kc-retrieval-outperforms-baselines.md) — related
