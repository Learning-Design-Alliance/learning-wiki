---
type: claim
title: Pattern-based KC similarity retrieves bundle-aligned programming learning items better than code-embedding and other KC baselines in both retrieval directions
description: Pattern-based KC similarity retrieves bundle-aligned programming learning items better than code-embedding and other KC baselines in both retrieval directions
id: pattern-kc-retrieval-outperforms-baselines
status: draft
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
  - id: muntasir-hoq-2026-2
    resource: "https://arxiv.org/abs/2607.05409"
    title: "Muntasir Hoq, Griffin Pitts, Zhangqi Duan, Arun Balajiee Lekshmi Narayanan, Mohammad Hassany, Andrew Lan, Peter Brusilovsky and Bita Akram. (2026). Automated Recommendation of Programming Learning Content Using Pattern-based Knowledge Components. CSEDM'26: 10th Educational Data Mining in Computer Science Education Workshop. https://arxiv.org/abs/2607.05409"
    author: Muntasir Hoq, Griffin Pitts, Zhangqi Duan, Arun Balajiee Lekshmi Narayanan, Mohammad Hassany, Andrew Lan, Peter Brusilovsky and Bita Akram
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Pattern-based KC similarity retrieves bundle-aligned programming learning items better than code-embedding and other KC baselines in both retrieval directions

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q2`

## Subclaims
`q2 i?` For worked-example retrieval, the pattern-based KC approach achieved Top-5 accuracy of 0.89, MRR 0.81, and mAP 0.82, outperforming code2vec, ontology-based KCs, and remaining baselines. [→ Muntasir Hoq 2026](#muntasir-hoq-2026)
`q2 i?` For challenge retrieval, the pattern-based KC approach ranked best with Top-5 0.90, MRR 0.80, and mAP 0.79. [→ Muntasir Hoq 2026 (2)](#muntasir-hoq-2026-2)

## Evidence

### Muntasir Hoq 2026

Muntasir Hoq, Griffin Pitts, Zhangqi Duan, Arun Balajiee Lekshmi Narayanan, Mohammad Hassany, Andrew Lan, Peter Brusilovsky and Bita Akram. (2026). Automated Recommendation of Programming Learning Content Using Pattern-based Knowledge Components. CSEDM'26: 10th Educational Data Mining in Computer Science Education Workshop. https://arxiv.org/abs/2607.05409 [doi:10.48550/arxiv.2607.05409](https://doi.org/10.48550/arxiv.2607.05409)

`q2 · i?` · `design · r2`

Retrieval evaluation on the PCEX corpus treating expert-defined bundle membership as ground truth, with self-matches prevented. The pattern-based KC model ranked candidates by cosine similarity of IDF-weighted knowledge vectors; "outperforming code2vec embeddings" and ontology-based KCs on all three rank-based metrics.

> "For worked-example retrieval, the pattern-based KC approach achieves Top-5 accuracy of 0.89%, MRR= 0.81%, and mAP= 0.82%, outperforming code2vec embeddings (Top-5= 0.83%, MRR= 0.71%, mAP= 0.71%), ontology-based KCs (Top-5= 0.88%, MRR= 0.67%, mAP= 0.65%), and the remaining baselines."

### Muntasir Hoq 2026 (2)

Muntasir Hoq, Griffin Pitts, Zhangqi Duan, Arun Balajiee Lekshmi Narayanan, Mohammad Hassany, Andrew Lan, Peter Brusilovsky and Bita Akram. (2026). Automated Recommendation of Programming Learning Content Using Pattern-based Knowledge Components. CSEDM'26: 10th Educational Data Mining in Computer Science Education Workshop. https://arxiv.org/abs/2607.05409

`q2 · i?` · `design · r2`

The second retrieval direction on the same PCEX test set, recommending challenges for a target worked example. The pattern-based KC model "again ranks best" across the five baselines on Top-5, MRR, and mAP as reported in Table 1.

> "For challenge retrieval, the pattern-based KC approach again ranks best with Top-5= 0.90%, MRR= 0.80%, and mAP= 0.79% (Table 1)."

## Discussion


## Related Claims
- [Unsupervised hierarchical clustering of knowledge vectors recovers expert bundle structure without bundle labels](clustering-recovers-expert-bundles.md) — related
- [IDF reweighting of knowledge vectors improves retrieval over binary KC-incidence vectors, with the largest gains in mAP](idf-reweighting-improves-kc-retrieval.md) — related
- Representing exercises by KC name descriptions outperformed ID-based representation when aligning an LLM to knowledge tracing — related
