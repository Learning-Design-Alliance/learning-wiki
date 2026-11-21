---
type: research-method
id: state-alignment-score
title: State Alignment score
description: "An evaluation metric that measures how closely a model's responses align with a given state's curriculum standards across the selected divergent topics."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# State Alignment score

> **Research Method** · [All research methods](index.md)
> **Evidence** · no claims cited

## Description
An evaluation metric that measures how closely a model's responses align with a given state's curriculum standards across the selected divergent topics. States in the same cluster as a response receive an alignment score of 1, states in the middle "somewhere in between" cluster receive a midpoint score of 0.5, and states in more distant clusters contribute 0; scores are aggregated to a state-level value from 0 to 1, where 1 indicates perfect alignment across all topics. The metric is computed by assigning model responses to clusters using Llama-3.3-70B classifications of focus and emphasis.

## Accounts
<!-- How each source describes or uses the method -->
- **State Alignment score: a 0-1 metric mapping LLM responses to state curriculum clusters**: An evaluation metric that measures how closely a model's responses align with a given state's curriculum standards across the selected divergent topics. States in the same cluster as a response receive an alignment score of 1, states in the middle "somewhere in between" cluster receive a midpoint score of 0.5, and states in more distant clusters contribute 0; scores are aggregated to a state-level value from 0 to 1, where 1 indicates perfect alignment across all topics. The metric is computed by assigning model responses to clusters using Llama-3.3-70B classifications of focus and emphasis. (Lisa Korver et al. (2026))

### Claims

## Related Research Methods
-

## Key Sources
- Lisa Korver, Tomo Lazovich, Shereif Reda. (2026). Large Language Models in K-12 Education: Alignment with State Curriculum Standards and Student Personas. https://arxiv.org/abs/2606.04846
