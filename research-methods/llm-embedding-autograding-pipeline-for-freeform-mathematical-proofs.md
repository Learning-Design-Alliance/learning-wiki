---
type: research-method
id: llm-embedding-autograding-pipeline-for-freeform-mathematical-proofs
title: LLM-embedding autograding pipeline for freeform mathematical proofs
description: The paper describes an automated grading process in which a student-written proof is first run through a pretrained large language model to obtain embeddings, and a custom classification model is then applied to those embeddings to calculate accuracy on various rubric points.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-27
---

# LLM-embedding autograding pipeline for freeform mathematical proofs

> **Research Method** · [All research methods](index.md)
> **Evidence** · no claims cited

## Description
The paper describes an automated grading process in which a student-written proof is first run through a pretrained large language model to obtain embeddings, and a custom classification model is then applied to those embeddings to calculate accuracy on various rubric points. Embedding selection and grading-model fitting are decoupled so the expensive semantic feature extraction is reused and a simple classifier (e.g., linear regression) suffices for the downstream grading task.

## Accounts
<!-- How each source describes or uses the method -->
- **LLM-embedding autograding pipeline for freeform mathematical proofs**: The paper describes an automated grading process in which a student-written proof is first run through a pretrained large language model to obtain embeddings, and a custom classification model is then applied to those embeddings to calculate accuracy on various rubric points. Embedding selection and grading-model fitting are decoupled so the expensive semantic feature extraction is reused and a simple classifier (e.g., linear regression) suffices for the downstream grading task. (Zhao et al. (2025))

### Claims

## Related Research Methods
-

## Key Sources
- Zhao, C., Silva, M., & Poulsen, S. (2025). Autograding Mathematical Induction Proofs with Natural Language Processing. International Journal of Artificial Intelligence in Education, 35, 3202–3232. https://doi.org/10.1007/s40593-025-00498-2
