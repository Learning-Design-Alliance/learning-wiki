---
type: claim
title: Diversity regularization λ = 0.30 was selected from a sensitivity analysis as balancing recommendation relevance and content diversity
description: Diversity regularization λ = 0.30 was selected from a sensitivity analysis as balancing recommendation relevance and content diversity
id: diversity-regularization-lambda-030
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: najem-2026
    resource: "https://doi.org/10.1007/s44217-026-02181-7"
    title: "Najem, K., Zaoui Seghroucheni, Y., & Ziti, S. (2026). Behavioral clustering for adaptive learning object recommendation in higher education using learning analytics for personalized student success. Discover Education. https://doi.org/10.1007/s44217-026-02181-7"
    author: "Najem, K., Zaoui Seghroucheni, Y., & Ziti, S."
    q: 1
    i: "?"
    kind: associational
    rigour: 1
---

# Diversity regularization λ = 0.30 was selected from a sensitivity analysis as balancing recommendation relevance and content diversity

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q1`

## Subclaims
`q2 i?` A sensitivity analysis over λ ∈ {0.10, 0.20, 0.30, 0.40, 0.50} selected λ = 0.30, which maximized intra-list diversity while keeping mean reciprocal affinity rank at 1.4 and intra-list cosine similarity at 0.41. [→ Najem 2026](#najem-2026)

## Evidence

### Najem 2026

Najem, K., Zaoui Seghroucheni, Y., & Ziti, S. (2026). Behavioral clustering for adaptive learning object recommendation in higher education using learning analytics for personalized student success. Discover Education. https://doi.org/10.1007/s44217-026-02181-7

`q1 · i?` · `associational · r1`

Numerical sensitivity analysis of the diversity regularization parameter over five λ values (Table 6); λ = 0.30 gave mean reciprocal affinity rank 1.4, intra-list cosine similarity 0.41, and 3 content types covered, versus rank 1.2 and similarity 0.92 at λ = 0.00.

> "The value λ = 0.30 was selected because it maximized intra-list diversity (measured by average pairwise cosine distance among the top-5 recommendations) while maintaining a favorable balance between recommendation relevance (mean reciprocal affinity rank = 1.4) and content diversity (intra-list cosine similarity = 0.41, covering 3 content types)."

## Discussion


## Related Claims
- Classification threshold trades sensitivity against specificity: 0.30 yields 91.3% sensitivity, 0.60 yields 89.7% specificity — related
- [The verification threshold trades hallucination reduction against over-refusal, with the default tau of 0.20 providing the best balance](eduguard-verifier-threshold-sensitivity.md) — related
