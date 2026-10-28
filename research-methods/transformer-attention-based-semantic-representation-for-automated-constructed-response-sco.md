---
type: research-method
id: transformer-attention-based-semantic-representation-for-automated-constructed-response-sco
title: Transformer attention-based semantic representation for automated constructed response scoring
description: "The article describes how transformer LLMs such as BERT generate sentence-level embeddings through attention layers where \"each embedding in the sequence is compared with and modified by each other embedding based on their similarity.\" This allows word meanings to be contextually influenced, produci"
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-28
---

# Transformer attention-based semantic representation for automated constructed response scoring

> **Research Method** · [All research methods](index.md)
> **Evidence** · 1 claim (1 against) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article describes how transformer LLMs such as BERT generate sentence-level embeddings through attention layers where "each embedding in the sequence is compared with and modified by each other embedding based on their similarity." This allows word meanings to be contextually influenced, producing a classification token representing the semantic meaning of the entire sequence. After finetuning, this token predicts human scores for constructed response items, capturing relationships that bag-of-words approaches miss.

## Accounts
<!-- How each source describes or uses the method -->
- **Transformer attention-based semantic representation for automated constructed response scoring**: The article describes how transformer LLMs such as BERT generate sentence-level embeddings through attention layers where "each embedding in the sequence is compared with and modified by each other embedding based on their similarity." This allows word meanings to be contextually influenced, producing a classification token representing the semantic meaning of the entire sequence. After finetuning, this token predicts human scores for constructed response items, capturing relationships that bag-of-words approaches miss. (Morris et al. (2025))

### Claims

- [T-tests show no significant shallow-vs-transformer difference in accuracy, weighted F1 or macro-F1, but a significant ROC-AUC advantage for the shallow model](../claims/ttest-roc-auc-advantage-shallow.md) [-W]

## Related Research Methods

- [Multilingual embedding-based automated classification of self-regulated-learning think-aloud utterances](multilingual-embedding-based-automated-classification-of-self-regulated-learning-think-alo.md)

## Key Sources
- Morris, W., Holmes, L., Choi, J. S., & Crossley, S. (2025). Automated Scoring of Constructed Response Items in Math Assessment Using Large Language Models. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00418-w
