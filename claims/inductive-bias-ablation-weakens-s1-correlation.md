---
type: claim
title: Ablating the inductive bias components monotonically weakens the correlation between annotated mechanistic-reasoning evidence and posterior mass on state S1
description: Ablating the inductive bias components monotonically weakens the correlation between annotated mechanistic-reasoning evidence and posterior mass on state S1
id: inductive-bias-ablation-weakens-s1-correlation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: gili-2026
    resource: "https://doi.org/10.48550/arXiv.2604.21870"
    title: "Gili, Kaitlin, Nistala, Mainak, Wendell, Kristen, and Hughes, Michael C. (2026). Locating acts of mechanistic reasoning in student team conversations with mechanistic machine learning. [doi:10.48550/arXiv.2604.21870](https://doi.org/10.48550/arXiv.2604.21870)"
    author: Gili, Kaitlin, Nistala, Mainak, Wendell, Kristen, and Hughes, Michael C.
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Ablating the inductive bias components monotonically weakens the correlation between annotated mechanistic-reasoning evidence and posterior mass on state S1

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q1 i?` On held-out test transcripts, the desired strong positive correlation for state S1 decreases as feedback components are ablated from human feedback, to classifier feedback, to no system state, to no feedback. [→ Gili 2026](#gili-2026)

## Evidence

### Gili 2026

Gili, Kaitlin, Nistala, Mainak, Wendell, Kristen, and Hughes, Michael C. (2026). Locating acts of mechanistic reasoning in student team conversations with mechanistic machine learning. [doi:10.48550/arXiv.2604.21870](https://doi.org/10.48550/arXiv.2604.21870)

`q1 · i?` · `design · r2`

Model-evaluation experiment (Table I) on two held-out test transcripts with unseen students, comparing HSRDM variants with human, classifier, weakened, and no feedback. The article reports the correlation between annotated evidence strength and posterior mass on S1 decreases across ablations; no effect size for the difference is printed.

> "For good models, the desired behavior is a strong positive correlation for state S1 (bold). We observe the correlation decrease as we ablate inductive bias components in the model architecture."

## Discussion


## Related Claims
- [Each pedagogical verification component contributes to a distinct quality dimension: layout verification most strongly](verification-components-ablation-contributions.md) — related
