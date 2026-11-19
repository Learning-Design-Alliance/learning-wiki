---
type: claim
title: The March 2023 version of ChatGPT was not ready for (orthogonal) diagonalization of matrices larger than 2×2, producing erroneous characteristic polynomials and incomplete eigenvector computations
description: The March 2023 version of ChatGPT was not ready for (orthogonal) diagonalization of matrices larger than 2×2, producing erroneous characteristic polynomials and incomplete eigenvector computations
id: chatgpt-unreliable-orthogonal-diagonalization-beyond-2x2
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
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

# The March 2023 version of ChatGPT was not ready for (orthogonal) diagonalization of matrices larger than 2×2, producing erroneous characteristic polynomials and incomplete eigenvector computations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r2` · `q1`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q1 i?` ChatGPT made calculation mistakes in the characteristic polynomial of a 3×3 symmetric matrix and could not complete the third eigenvector. [→ Natanael Karjanto 2023](#natanael-karjanto-2023)
`q1 i?` For the same symmetric matrix B used elsewhere in the article, ChatGPT gave an incorrect characteristic polynomial, a false eigenvalue set, and incomplete calculations; regenerating responses did not help. [→ Natanael Karjanto 2023](#natanael-karjanto-2023)

## Evidence

### Natanael Karjanto 2023

Natanael Karjanto. (2023). Matrix diagonalization and singular value decomposition: Static SageMath and dynamic ChatGPT juxtaposed. [doi:10.48550/arXiv.2303.17163](https://doi.org/10.48550/arXiv.2303.17163)

`q1 · i?` · `theoretical · r2`

ChatGPT inquiry task (version of March 14, 2023) orthogonally diagonalizing a 3×3 symmetric matrix; the chatbot's erroneous characteristic polynomial and false eigenvalues are reported verbatim. The article concludes "the current version of ChatGPT does not seem ready for the (orthogonal) diagonalization of a simple matrix beyond 2× 2."

> "Unfortunately , ChatGPT provided an incorrect answer for this matrix diagonalization. Its computation for the characteristic polynomial was erroneous: λ3− 9λ2 + 24λ, which gives a false set of eigenvalues: λ1 = 0, λ2 = 3, and λ3 = 6."

## Discussion


## Related Claims
- [ChatGPT produced incorrect singular values in its own SVD example, with errors of approximately 16% for the second and third singular values](chatgpt-svd-incorrect-singular-values.md) — related
- [Static SageMath successfully supports (orthogonal) diagonalization and SVD construction, including verification by multiplying factors back to the original matrix](sagemath-assists-matrix-factorization.md) — related
