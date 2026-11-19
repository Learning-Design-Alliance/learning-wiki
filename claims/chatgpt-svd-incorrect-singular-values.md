---
type: claim
title: "ChatGPT produced incorrect singular values in its own SVD example, with errors of approximately 16% for the second and third singular values"
description: "ChatGPT produced incorrect singular values in its own SVD example, with errors of approximately 16% for the second and third singular values"
id: chatgpt-svd-incorrect-singular-values
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
    kind: design
    rigour: 2
---

# ChatGPT produced incorrect singular values in its own SVD example, with errors of approximately 16% for the second and third singular values

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q1 i?` For a 3×3 example ChatGPT dispensed singular values of 24.57, 9.49, and 3.63, whereas the correct singular values are 25.58, 11.36, and 3.13. [→ Natanael Karjanto 2023](#natanael-karjanto-2023)

## Evidence

### Natanael Karjanto 2023

Natanael Karjanto. (2023). Matrix diagonalization and singular value decomposition: Static SageMath and dynamic ChatGPT juxtaposed. [doi:10.48550/arXiv.2303.17163](https://doi.org/10.48550/arXiv.2303.17163)

`q1 · i?` · `design · r2`

Evaluation of a ChatGPT (March 14, 2023 version) response, shown in Figure 1, against SageMath output from A.SVD() on RDF. The article reports the correct values and states the second and third singular value errors are "approximately 16%". This is a worked comparison, not a controlled experiment.

> "values ofσ1 = 24.57,σ2 = 9.49, andσ3 = 3.63, whereas the correct singular values areσ1 = 25.58, σ2 = 11.36, andσ3 = 3.13. Although the error for the ﬁrst singular value is less than 4%, the errors for the second and third singular values are approximately 16%, which is too large to be considered acceptable."

## Discussion


## Related Claims
- [Static SageMath successfully supports (orthogonal) diagonalization and SVD construction, including verification by multiplying factors back to the original matrix](sagemath-assists-matrix-factorization.md) — related
- [Gen-AI hallucinates sources and values and produces convincing but incorrect explanations, risking student misinformation](genai-hallucination-convincing-incorrect-explanations.md) — a broader claim this one bears on
- [The March 2023 version of ChatGPT was not ready for (orthogonal) diagonalization of matrices larger than 2×2, producing erroneous characteristic polynomials and incomplete eigenvector computations](chatgpt-unreliable-orthogonal-diagonalization-beyond-2x2.md) — related
- [A common student mistake in SVD is computing eigenvalues of the original matrix instead of M^T M, and confusing reduced SVD with full SVD when the matrix lacks full rank](svd-common-mistakes-eigenvalue-confusion.md) — related
