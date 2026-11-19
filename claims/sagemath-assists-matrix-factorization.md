---
type: claim
title: Static SageMath successfully supports (orthogonal) diagonalization and SVD construction, including verification by multiplying factors back to the original matrix
description: Static SageMath successfully supports (orthogonal) diagonalization and SVD construction, including verification by multiplying factors back to the original matrix
id: sagemath-assists-matrix-factorization
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2023
sources:
  - id: natanael-karjanto-2023
    resource: "https://doi.org/10.48550/arXiv.2303.17163"
    title: "Natanael Karjanto. (2023). Matrix diagonalization and singular value decomposition: Static SageMath and dynamic ChatGPT juxtaposed. [doi:10.48550/arXiv.2303.17163](https://doi.org/10.48550/arXiv.2303.17163)"
    author: Natanael Karjanto
    q: 1
    i: "?"
    kind: theoretical
    rigour: 2
---

# Static SageMath successfully supports (orthogonal) diagonalization and SVD construction, including verification by multiplying factors back to the original matrix

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r2` · `q1`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` SageMath commands computed characteristic polynomials, eigenvalues, eigenvectors, Gram-Schmidt orthogonalization, and SVD factors for the worked examples, with products returning the original matrices. [→ Natanael Karjanto 2023](#natanael-karjanto-2023)

## Evidence

### Natanael Karjanto 2023

Natanael Karjanto. (2023). Matrix diagonalization and singular value decomposition: Static SageMath and dynamic ChatGPT juxtaposed. [doi:10.48550/arXiv.2303.17163](https://doi.org/10.48550/arXiv.2303.17163)

`q1 · i?` · `theoretical · r2`

Worked demonstrations (Sections 3.1–3.3) of SageMath code for diagonalization, orthogonal diagonalization with Gram-Schmidt, and SVD, each confirmed because "the product of each matrix returns to the original matrix". Demonstrative computational examples, not a student study.

> "We conﬁrm that the construction of our SVD is correct because the product of each matrix returns to the original matrix M, that is, M = UΣV T."

## Discussion


## Related Claims
- [ChatGPT produced incorrect singular values in its own SVD example, with errors of approximately 16% for the second and third singular values](chatgpt-svd-incorrect-singular-values.md) — related
- [The March 2023 version of ChatGPT was not ready for (orthogonal) diagonalization of matrices larger than 2×2, producing erroneous characteristic polynomials and incomplete eigenvector computations](chatgpt-unreliable-orthogonal-diagonalization-beyond-2x2.md) — related
- [Undergraduate students commonly forget to normalize eigenvectors and to orthonormalize eigenvectors from the same eigenspace when performing orthogonal diagonalization](forgetting-normalization-orthogonal-diagonalization-mistakes.md) — related
