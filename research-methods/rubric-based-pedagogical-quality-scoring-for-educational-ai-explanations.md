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
> **Evidence** · 4 claims (4 for) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 4 claims rest on one study

## Description
The article defines a composite pedagogical quality score on [0,1] as the mean of six binary criteria applied per response: step-by-step exposition, correct mathematical notation, worked example, query coverage, explanation depth, and proof-step granularity. Because "equivalent mathematical proofs can use substantially different wording", the authors argue this rubric "captures educational value independently of surface wording" and is a more appropriate primary metric than ROUGE or BLEU for mathematical educational AI, offering a reusable benchmark methodology.

## Accounts
<!-- How each source describes or uses the method -->
- **Rubric-based pedagogical quality scoring as a primary evaluation metric for educational AI in formal domains**: The article defines a composite pedagogical quality score on [0,1] as the mean of six binary criteria applied per response: step-by-step exposition, correct mathematical notation, worked example, query coverage, explanation depth, and proof-step granularity. Because "equivalent mathematical proofs can use substantially different wording", the authors argue this rubric "captures educational value independently of surface wording" and is a more appropriate primary metric than ROUGE or BLEU for mathematical educational AI, offering a reusable benchmark methodology. (Sushan Adhikari (2026))
- **Seven pedagogical evaluation dimensions for multiple-choice coding questions**: The Validator assesses each generated question across seven pedagogical dimensions derived from established multiple-choice item-writing guidelines: question stem clarity, code validity, concept alignment, correct answer validity, distractor quality, correct answer feedback quality, and distractor feedback quality. Each dimension receives a Yes/No or Good/Poor classification output plus a rationale output explaining the assessment, producing transparent dimension-level quality signals rather than opaque aggregate scores. The dimensions cover both technical verifiability and pedagogical depth. (Xiaojing Duan et al. (2026))

### Claims
- [BLEU-4 scored zero on all 179 mathematical-proof responses, which the authors interpret as a property of n-gram metrics rather than system failure](../claims/bleu4-zero-mathematical-proofs-metric-limitation.md) [+M]
- [AlgoRAG answered all 179 TCS exam-style questions successfully with a mean response time of 38.0 seconds and a pedagogical quality score of 0.7620](../claims/algorag-100-success-179-tcs-questions.md) [+M]
- [CODE-GEN achieves human-validated success rates of 79.9% to 98.6% across seven pedagogical evaluation dimensions](../claims/code-gen-success-rates-seven-dimensions.md) [+M]
- [Distractor quality is the weakest automated dimension, with the lowest success rate (79.9%) and highest failure rate (15.6%)](../claims/code-gen-distractor-quality-weakest-dimension.md) [+M]

## Related Research Methods
-

## Key Sources
- Sushan Adhikari. (2026). AlgoRAG: Retrieval-Augmented Generation for Theoretical Computer Science Education — A Comprehensive Evaluation Framework for Algorithm Analysis and Complexity Theory. arXiv preprint. https://arxiv.org/abs/2609.14572
- Xiaojing Duan, Frederick Nwanganga, and Chaoli Wang. (2026). CODE-GEN: A Human-in-the-Loop RAG-Based Agentic AI System for Multiple-Choice Question Generation. https://arxiv.org/abs/2604.03926
