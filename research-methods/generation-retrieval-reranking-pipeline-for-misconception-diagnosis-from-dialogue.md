---
type: research-method
id: generation-retrieval-reranking-pipeline-for-misconception-diagnosis-from-dialogue
title: Generation-retrieval-reranking pipeline for misconception diagnosis from dialogue
description: A three-stage architecture for diagnosing student misconceptions from student-tutor dialogue.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# Generation-retrieval-reranking pipeline for misconception diagnosis from dialogue

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A three-stage architecture for diagnosing student misconceptions from student-tutor dialogue. Stage 1 uses an LLM with LoRA adapters to "generate a plausible hypothesis for a misconception that the student could have". Stage 2 embeds the generated hypothesis and each ground-truth misconception label with MiniLM-L6-v2 and retrieves the top-k candidates by cosine similarity. Stage 3 uses a second fine-tuned LLM to rerank the top-k labels, better capturing their semantics, and the highest-ranked label is the prediction. LoRA layers for stages 1 and 3 are trained separately, keeping about 0.5% of parameters trainable.

## Accounts
<!-- How each source describes or uses the method -->
- **Generation-retrieval-reranking pipeline for misconception diagnosis from dialogue**: A three-stage architecture for diagnosing student misconceptions from student-tutor dialogue. Stage 1 uses an LLM with LoRA adapters to "generate a plausible hypothesis for a misconception that the student could have". Stage 2 embeds the generated hypothesis and each ground-truth misconception label with MiniLM-L6-v2 and retrieves the top-k candidates by cosine similarity. Stage 3 uses a second fine-tuned LLM to rerank the top-k labels, better capturing their semantics, and the highest-ranked label is the prediction. LoRA layers for stages 1 and 3 are trained separately, keeping about 0.5% of parameters trainable. (Joshua Mitton et al. (2026))

### Claims
- [LLM reranking of retrieved misconception candidates improves performance, promoting the correct misconception to rank 1 in 73 of 229 reranked cases for Claude](../claims/llm-reranking-improves-misconception-retrieval.md) [+M]
- [Adding the generative stage improves or maintains MAP@k and NDCG performance for most model configurations](../claims/generative-stage-improves-map-ndcg.md) [+M]

## Related Research Methods
-

## Key Sources
- Joshua Mitton, Prarthana Bhattacharyya, Digory Smith, Thomas Christie, Ralph Abboud, and Simon Woodhead. (2026). Misconception Diagnosis From Student-Tutor Dialogue: Generate, Retrieve, Rerank. arXiv preprint. https://arxiv.org/abs/2602.02414
