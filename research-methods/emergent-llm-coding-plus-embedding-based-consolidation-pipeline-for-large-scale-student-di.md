---
type: research-method
id: emergent-llm-coding-plus-embedding-based-consolidation-pipeline-for-large-scale-student-di
title: Emergent LLM coding plus embedding-based consolidation pipeline for large-scale student-discourse taxonomies
description: A two-step methodological framework, framed as the LLM analog of open coding in grounded theory, for converting large student-tutor transcript corpora into interpretable discourse categories.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Emergent LLM coding plus embedding-based consolidation pipeline for large-scale student-discourse taxonomies

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 qualitative), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A two-step methodological framework, framed as the LLM analog of open coding in grounded theory, for converting large student-tutor transcript corpora into interpretable discourse categories. Step 1 asks an LLM coder to assign each turn an emergent free-text label using the previous four conversational turns as context, yielding 833 unique raw labels. Step 2 consolidates near-paraphrase labels via text embeddings, cosine distance, and agglomerative clustering with average linkage at a distance threshold of 0.40, followed by LLM-generated canonical category names, producing 357 consolidated categories. The approach follows computational grounded theory, letting categories be discovered rather than projected from a fixed codebook.

## Accounts
<!-- How each source describes or uses the method -->
- **Emergent LLM coding plus embedding-based consolidation pipeline for large-scale student-discourse taxonomies**: A two-step methodological framework, framed as the LLM analog of open coding in grounded theory, for converting large student-tutor transcript corpora into interpretable discourse categories. Step 1 asks an LLM coder to assign each turn an emergent free-text label using the previous four conversational turns as context, yielding 833 unique raw labels. Step 2 consolidates near-paraphrase labels via text embeddings, cosine distance, and agglomerative clustering with average linkage at a distance threshold of 0.40, followed by LLM-generated canonical category names, producing 357 consolidated categories. The approach follows computational grounded theory, letting categories be discovered rather than projected from a fixed codebook. (Syed Furqan Abbas Hashmi et al. (2026))

### Claims
- [The emergent LLM coding pipeline reaches substantial agreement with expert human coding (Cohen's κ = 0.78, raw agreement 84%) on a stratified 10% sample](../claims/llm-discourse-coding-kappa-078-expert-agreement.md) [+M]
- [Student discourse with a Socratic AI physics tutor concentrates sharply: of 357 consolidated categories, the top 25 cover roughly half of all student turns](../claims/ai-tutor-discourse-concentrates-top-categories.md) [+M]

## Related Research Methods
-

## Key Sources
- Syed Furqan Abbas Hashmi and N. Sanjay Rebello. (2026). A bottom-up taxonomy of student discourse with a Socratic AI physics tutor. https://arxiv.org/abs/2608.07373
