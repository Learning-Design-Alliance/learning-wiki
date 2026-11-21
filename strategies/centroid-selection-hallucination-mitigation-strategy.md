---
type: strategy
id: centroid-selection-hallucination-mitigation-strategy
title: Mitigate LLM hallucination in generated hint pathways by generating 30 responses per question and selecting the response closest to the centroid embedding
description: For the learning gain study, the authors reduced hallucination in PromptHive-generated multi-hint pathways by generating each response 30 times and choosing the most representative response.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: mohi-reza-2024
    resource: "https://arxiv.org/abs/2410.16547"
    title: "Mohi Reza, Ioannis Anastasopoulos, Shreya Bhandari, Zachary A Pardos. (2024). PromptHive: Bringing Subject Matter Experts Back to the Forefront with Collaborative Prompt Engineering for Educational Content Creation. arXiv preprint. https://arxiv.org/abs/2410.16547"
    author: Mohi Reza, Ioannis Anastasopoulos, Shreya Bhandari, Zachary A Pardos
---

# Mitigate LLM hallucination in generated hint pathways by generating 30 responses per question and selecting the response closest to the centroid embedding

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
For the learning gain study, the authors reduced hallucination in PromptHive-generated multi-hint pathways by generating each response 30 times and choosing the most representative response. They vectorized all responses to a question with SentenceTransformer, computed the centroid vector, and "used cosine similarity to find the response closest to the centroid vector, which represents the most representative response out of our 30". This adapts self-consistency prompting, which prior work cited by the article reports achieved near 0% hallucination in College Algebra worked solutions.

## Design Implications

### Context
#### Requirements
- An LLM capable of reliably adhering to a specified output schema (the article used GPT4o's schema adherence)
- An embedding model (SentenceTransformer) to vectorize candidate responses and compute a centroid
#### Constraints
- Demonstrated for multi-hint pathways rather than worked solutions; required manual formatting fixes afterward, taking the second and third authors 3h15m and 6h19m respectively

### Target Learners
- college-level math students

### Target Learning Goals
- accurate, hallucination-free multi-hint tutoring pathways for algebra problems

## Claims

- [ChatGPT 3.5 produced low-quality hints for 32% of problems, reducible to near 0% for algebra and 13% for statistics via the self-consistency technique](../claims/chatgpt-hint-error-rate-self-consistency.md) [+M]

## Related Strategies

- [Incorporate pre-delivery LLM-based evaluation approaches into GenAI-powered personalised SRL scaffolding systems to mitigate hallucinations](pre-delivery-llm-evaluation-mitigate-hallucinations.md)
- [Apply human quality-check supervision before deploying LLM-generated hint content in tutoring systems](human-quality-checks-for-llm-hints.md)
- [Use embedding-based strategy measures to suggest maximally different alternative solution approaches and foster divergent thinking](suggest-maximally-different-alternative-strategies.md)

## Examples
-

## Key Sources
- Mohi Reza, Ioannis Anastasopoulos, Shreya Bhandari, Zachary A Pardos. (2024). PromptHive: Bringing Subject Matter Experts Back to the Forefront with Collaborative Prompt Engineering for Educational Content Creation. arXiv preprint. https://arxiv.org/abs/2410.16547
