---
type: research-method
id: evp-guided-llm-pipeline-for-word-level-cefr-prediction
title: EVP-guided LLM pipeline for word-level CEFR prediction
description: A replicable pipeline that combines the English Vocabulary Profile with LLMs to predict the CEFR level of each word in L2 learner text in context.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# EVP-guided LLM pipeline for word-level CEFR prediction

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A replicable pipeline that combines the English Vocabulary Profile with LLMs to predict the CEFR level of each word in L2 learner text in context. Sentences are lemmatised with spaCy and each lemma is mapped to its EVP entries; each target word is highlighted in square brackets, candidate EVP options (with PoS and brief definitions) plus a 'None of the other options' choice are presented to the LLM, and the option with the highest average softmax probability over logits is selected. The article describes that "we use spaCy to lemmatise each word and map the resulting lemma to its corresponding entries in the EVP," filtering irrelevant entries per run. The method handles multi-word expressions by evaluating reference words in context.

## Accounts
<!-- How each source describes or uses the method -->
- **EVP-guided LLM pipeline for word-level CEFR prediction**: A replicable pipeline that combines the English Vocabulary Profile with LLMs to predict the CEFR level of each word in L2 learner text in context. Sentences are lemmatised with spaCy and each lemma is mapped to its EVP entries; each target word is highlighted in square brackets, candidate EVP options (with PoS and brief definitions) plus a 'None of the other options' choice are presented to the LLM, and the option with the highest average softmax probability over logits is selected. The article describes that "we use spaCy to lemmatise each word and map the resulting lemma to its corresponding entries in the EVP," filtering irrelevant entries per run. The method handles multi-word expressions by evaluating reference words in context. (Stefano Bannò et al. (2025))

### Claims
- [LLMs outperform a PoS-based baseline and a random baseline on word-level CEFR prediction of L2 learner writing, with the largest gains on ambiguous words](../claims/llms-beat-pos-baseline-word-level-cefr.md) [+M]
- [LLMs can identify the intended EVP meaning of polysemous words in context, with accuracy decreasing as the number of candidate meanings increases](../claims/llm-evp-sense-disambiguation-accuracy.md) [+M]

## Related Research Methods
-

## Key Sources
- Stefano Bannò, Kate M. Knill, Mark J. F. Gales. (2025). Exploiting the English Vocabulary Profile for L2 word-level vocabulary assessment with LLMs. arXiv. https://arxiv.org/abs/2506.02758
