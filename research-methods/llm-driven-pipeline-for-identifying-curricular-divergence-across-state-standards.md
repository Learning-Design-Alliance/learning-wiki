---
type: research-method
id: llm-driven-pipeline-for-identifying-curricular-divergence-across-state-standards
title: LLM-driven pipeline for identifying curricular divergence across state standards
description: An automated framework that retrieves relevant chunks from state standards documents using Fordham Institute topics as keywords, prompts Llama-3.3-70B to generate subtopic lists and narrative-framing descriptions, clusters the descriptions with BERTopic, and then has the LLM generate evaluation prom
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# LLM-driven pipeline for identifying curricular divergence across state standards

> **Research Method** · [All research methods](index.md)
> **Evidence** · no claims cited

## Description
An automated framework that retrieves relevant chunks from state standards documents using Fordham Institute topics as keywords, prompts Llama-3.3-70B to generate subtopic lists and narrative-framing descriptions, clusters the descriptions with BERTopic, and then has the LLM generate evaluation prompts defining each cluster. The authors note BERTopic clusters "are not entirely accurate," so clusters are refined via LLM self-reflection until classification is stable, and the authors manually inspected each cluster. It identified five topics with sufficient state variation: the Secession Crisis, Westward Expansion and Manifest Destiny, the Industrial Revolution, the Vietnam War, and World War I.

## Accounts
<!-- How each source describes or uses the method -->
- **LLM-driven pipeline for identifying curricular divergence across state standards (RAG retrieval, BERTopic clustering, LLM-refined evaluation prompts)**: An automated framework that retrieves relevant chunks from state standards documents using Fordham Institute topics as keywords, prompts Llama-3.3-70B to generate subtopic lists and narrative-framing descriptions, clusters the descriptions with BERTopic, and then has the LLM generate evaluation prompts defining each cluster. The authors note BERTopic clusters "are not entirely accurate," so clusters are refined via LLM self-reflection until classification is stable, and the authors manually inspected each cluster. It identified five topics with sufficient state variation: the Secession Crisis, Westward Expansion and Manifest Destiny, the Industrial Revolution, the Vietnam War, and World War I. (Lisa Korver et al. (2026))

### Claims

## Related Research Methods
-

## Key Sources
- Lisa Korver, Tomo Lazovich, Shereif Reda. (2026). Large Language Models in K-12 Education: Alignment with State Curriculum Standards and Student Personas. https://arxiv.org/abs/2606.04846
