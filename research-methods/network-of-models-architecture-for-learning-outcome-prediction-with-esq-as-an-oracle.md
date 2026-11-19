---
type: research-method
id: network-of-models-architecture-for-learning-outcome-prediction-with-esq-as-an-oracle
title: Network of Models architecture for learning-outcome prediction with ESQ as an oracle
description: "The article proposes an end-to-end modeling framework in which multiple models work in concert, feeding results forward: individualized Bayesian Knowledge Tracing summarizes attempt-level time series into interpretable features, a deepFM Concept Mastery model produces competency across a 1,242-conce"
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
---

# Network of Models architecture for learning-outcome prediction with ESQ as an oracle

> **Research Method** · [All research methods](index.md)
> **Evidence** · no claims cited

## Description
The article proposes an end-to-end modeling framework in which multiple models work in concert, feeding results forward: individualized Bayesian Knowledge Tracing summarizes attempt-level time series into interpretable features, a deepFM Concept Mastery model produces competency across a 1,242-concept set, and these academic, behavioral, effort and test-taking features (AQ, BQ, EQ, TQ) drive the Embibe Score Quotient model that predicts the scoring potential of a learner in a test yet to be taken. The ESQ then serves as an Oracle for a nudges model that solves an inverse problem — "What state should a learner move to, from a given state in order to obtain a particular reward?" — posed as a minimization over the state change δx. The framework is extensible, allowing black-box or hand-crafted modules.

## Accounts
<!-- How each source describes or uses the method -->
- **Network of Models architecture for learning-outcome prediction with ESQ as an oracle**: The article proposes an end-to-end modeling framework in which multiple models work in concert, feeding results forward: individualized Bayesian Knowledge Tracing summarizes attempt-level time series into interpretable features, a deepFM Concept Mastery model produces competency across a 1,242-concept set, and these academic, behavioral, effort and test-taking features (AQ, BQ, EQ, TQ) drive the Embibe Score Quotient model that predicts the scoring potential of a learner in a test yet to be taken. The ESQ then serves as an Oracle for a nudges model that solves an inverse problem — "What state should a learner move to, from a given state in order to obtain a particular reward?" — posed as a minimization over the state change δx. The framework is extensible, allowing black-box or hand-crafted modules. (Chintan Donda Sayan Dasgupta Soma S Dhavala Keyur Faldu Aditi Avasthi (2020))

### Claims

## Related Research Methods
-

## Key Sources
- Chintan Donda Sayan Dasgupta Soma S Dhavala Keyur Faldu Aditi Avasthi. (2020). A FRAMEWORK FOR PREDICTING, INTERPRETING, AND IMPROVING LEARNING OUTCOMES. arXiv preprint. https://arxiv.org/abs/2010.02629v2
