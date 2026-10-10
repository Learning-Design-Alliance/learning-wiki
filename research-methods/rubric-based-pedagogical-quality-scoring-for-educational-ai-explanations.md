---
type: research-method
id: rubric-based-pedagogical-quality-scoring-for-educational-ai-explanations
title: Rubric-based pedagogical quality scoring for educational AI explanations
description: "The article defines a composite pedagogical quality score on [0,1] as the mean of six binary criteria applied per response: step-by-step exposition, correct mathematical notation, worked example, query coverage, explanation depth, and proof-step granularity."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# Rubric-based pedagogical quality scoring for educational AI explanations

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article defines a composite pedagogical quality score on [0,1] as the mean of six binary criteria applied per response: step-by-step exposition, correct mathematical notation, worked example, query coverage, explanation depth, and proof-step granularity. Because "equivalent mathematical proofs can use substantially different wording", the authors argue this rubric "captures educational value independently of surface wording" and is a more appropriate primary metric than ROUGE or BLEU for mathematical educational AI, offering a reusable benchmark methodology.

## Accounts
<!-- How each source describes or uses the method -->
- **Rubric-based pedagogical quality scoring as a primary evaluation metric for educational AI in formal domains**: The article defines a composite pedagogical quality score on [0,1] as the mean of six binary criteria applied per response: step-by-step exposition, correct mathematical notation, worked example, query coverage, explanation depth, and proof-step granularity. Because "equivalent mathematical proofs can use substantially different wording", the authors argue this rubric "captures educational value independently of surface wording" and is a more appropriate primary metric than ROUGE or BLEU for mathematical educational AI, offering a reusable benchmark methodology. (Sushan Adhikari (2026))

### Claims
- [BLEU-4 scored zero on all 179 mathematical-proof responses, which the authors interpret as a property of n-gram metrics rather than system failure](../claims/bleu4-zero-mathematical-proofs-metric-limitation.md) [+M]
- [AlgoRAG answered all 179 TCS exam-style questions successfully with a mean response time of 38.0 seconds and a pedagogical quality score of 0.7620](../claims/algorag-100-success-179-tcs-questions.md) [+M]

## Related Research Methods
-

## Key Sources
- Sushan Adhikari. (2026). AlgoRAG: Retrieval-Augmented Generation for Theoretical Computer Science Education — A Comprehensive Evaluation Framework for Algorithm Analysis and Complexity Theory. arXiv preprint. https://arxiv.org/abs/2609.14572
