---
type: claim
title: Undergraduate students commonly forget to normalize eigenvectors and to orthonormalize eigenvectors from the same eigenspace when performing orthogonal diagonalization
description: Undergraduate students commonly forget to normalize eigenvectors and to orthonormalize eigenvectors from the same eigenspace when performing orthogonal diagonalization
id: forgetting-normalization-orthogonal-diagonalization-mistakes
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2028
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

# Undergraduate students commonly forget to normalize eigenvectors and to orthonormalize eigenvectors from the same eigenspace when performing orthogonal diagonalization

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r2` · `q1`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2028: baselines and conditions change

## Subclaims
`q1 i?` Students frequently forget to normalize eigenvectors to unit vectors and fail to convert non-orthogonal eigenvectors from a shared eigenspace into an orthonormal set during orthogonal diagonalization. [→ Natanael Karjanto 2023](#natanael-karjanto-2023)

## Evidence

### Natanael Karjanto 2023

Natanael Karjanto. (2023). Matrix diagonalization and singular value decomposition: Static SageMath and dynamic ChatGPT juxtaposed. [doi:10.48550/arXiv.2303.17163](https://doi.org/10.48550/arXiv.2303.17163)

`q1 · i?` · `theoretical · r2`

Authors' observational report of mistakes observed among linear algebra learners, presented as motivating examples rather than a systematic study. The article notes "several students often forget to normalize the associated eigenvectors" and that the Gram-Schmidt process fixes eigenvectors sharing an eigenspace.

> "For orthogonal diagonalization, several students often forget to normalize the associated eigenvectors to become unit vectors. In other cases, when one eigenvalue yields two associated eigenvectors, some students also forget to transform the set of eigenvectors into an orthonormal set"

## Discussion


## Related Claims
- [Static SageMath successfully supports (orthogonal) diagonalization and SVD construction, including verification by multiplying factors back to the original matrix](sagemath-assists-matrix-factorization.md) — related
- [A common student mistake in SVD is computing eigenvalues of the original matrix instead of M^T M, and confusing reduced SVD with full SVD when the matrix lacks full rank](svd-common-mistakes-eigenvalue-confusion.md) — related
