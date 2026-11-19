---
type: claim
title: A common student mistake in SVD is computing eigenvalues of the original matrix instead of M^T M, and confusing reduced SVD with full SVD when the matrix lacks full rank
description: A common student mistake in SVD is computing eigenvalues of the original matrix instead of M^T M, and confusing reduced SVD with full SVD when the matrix lacks full rank
id: svd-common-mistakes-eigenvalue-confusion
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
    kind: qualitative
    rigour: 1
---

# A common student mistake in SVD is computing eigenvalues of the original matrix instead of M^T M, and confusing reduced SVD with full SVD when the matrix lacks full rank

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · qualitative `r1` · `q1`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2028: baselines and conditions change

## Subclaims
`q1 i?` Some students compute eigenvalues of A itself and take square roots as singular values, instead of finding eigenvalues of A^T A. [→ Natanael Karjanto 2023](#natanael-karjanto-2023)
`q1 i?` Students who cannot find missing orthonormal eigenvectors for rank-deficient matrices produce a reduced SVD and confuse it with full SVD. [→ Natanael Karjanto 2023](#natanael-karjanto-2023)

## Evidence

### Natanael Karjanto 2023

Natanael Karjanto. (2023). Matrix diagonalization and singular value decomposition: Static SageMath and dynamic ChatGPT juxtaposed. [doi:10.48550/arXiv.2303.17163](https://doi.org/10.48550/arXiv.2303.17163)

`q1 · i?` · `qualitative · r1`

Authors' observational account of learner difficulties with SVD, including the eigenvector-finding error and the difficulty of completing the decomposition for rank-deficient matrices. No counts or effect sizes are printed; the report is illustrative rather than a measured study.

> "instead of finding the eigenalues ofAT A, some students calculated the eigenvalues ofA, took their square root, and designated them as singular values. Another difﬁculty occurs when the matrix does not have a full rank"

## Discussion


## Related Claims
- [Undergraduate students commonly forget to normalize eigenvectors and to orthonormalize eigenvectors from the same eigenspace when performing orthogonal diagonalization](forgetting-normalization-orthogonal-diagonalization-mistakes.md) — related
- [ChatGPT produced incorrect singular values in its own SVD example, with errors of approximately 16% for the second and third singular values](chatgpt-svd-incorrect-singular-values.md) — related
