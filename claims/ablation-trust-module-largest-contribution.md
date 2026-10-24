---
type: claim
title: "Ablations show the trustworthiness module contributes most to performance, and the explanation generator cuts human review time by 41%"
description: "Ablations show the trustworthiness module contributes most to performance, and the explanation generator cuts human review time by 41%"
id: ablation-trust-module-largest-contribution
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: li-2025
    resource: "https://doi.org/10.3390/info16100882"
    title: "Li, Y.; Yang, H.; Fang, Q. (2025). Towards Trustworthy and Explainable-by-Design Large Language Models for Automated Teacher Assessment. Information 2025, 16, 882. https://doi.org/10.3390/info16100882"
    author: Li, Y.; Yang, H.; Fang, Q.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Ablations show the trustworthiness module contributes most to performance, and the explanation generator cuts human review time by 41%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Removing the trustworthiness constraints causes the most severe performance drop (ICS −9.2%, ExpScore −14.7%), followed by disabling hierarchical attention (ICS −6.8%); the explanation generator reduces human review time by 41%. [→ Li 2025](#li-2025)

## Evidence

### Li 2025

Li, Y.; Yang, H.; Fang, Q. (2025). Towards Trustworthy and Explainable-by-Design Large Language Models for Automated Teacher Assessment. Information 2025, 16, 882. https://doi.org/10.3390/info16100882

`q2 · i?` · `design · r2`

Component-wise ablation study (§5.6, Table 11) on the TeacherEval-2023 test set, removing each module individually; review-time impact is +63% for the trustworthiness module, +38% for hierarchical attention, and +112% for the explanation generator.

> "Removing the trustworthiness constraints causes the most severe performance drop (ICS −9.2%, ExpScore−14.7%), followed by disabling hierarchical attention (ICS−6.8%). The dynamic explanation generator, while contributing modestly to raw accuracy (+3.1% ICS), reduces human review time by 41% through structured justifications."

## Discussion


## Related Claims
- [Removing the cognitive load module causes the largest ablation performance drop, while state fusion has a smaller effect](cognitive-load-module-largest-ablation-drop.md) — related
- [Ablations show each CogEvolution module contributes: removing ICAP perception, structured retrieval, or evolutionary update degrades mistake precision, learning-curve fit, and alignment](cogevolution-ablation-module-contributions.md) — related
- [In the EduAgent framework, removing past cognitive states from memory significantly reduced simulation performance](eduagent-ablation-contextual-memory-critical.md) — related
- [Ablation study shows metadata-enriched embeddings produce the largest accuracy drop, while attention masking, KV caching and dynamic batching primarily support inference efficiency](ablation-metadata-embeddings-largest-accuracy-drop.md) — related
- [Each pedagogical verification component contributes to a distinct quality dimension: layout verification most strongly](verification-components-ablation-contributions.md) — related
- [Federated aggregation is the primary driver of performance gains, contributing an average 11.99% improvement](federated-aggregation-primary-performance-driver.md) — related
- [Static Knowledge Grounding and Dynamic Personal Memory are complementary: removing both yields the largest quality degradation](skg-dpm-complementary-ablation-deeptutor.md) — related
