---
type: claim
title: LoRA fine-tuning improves generated misconception style and raises cosine similarity with expert labels, letting small open-source models rival larger closed-source ones
description: LoRA fine-tuning improves generated misconception style and raises cosine similarity with expert labels, letting small open-source models rival larger closed-source ones
id: lora-finetuning-improves-misconception-generation-style
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: joshua-mitton-2026
    resource: "https://doi.org/10.1145/3774398.3811609"
    title: "Joshua Mitton, Prarthana Bhattacharyya, Digory Smith, Thomas Christie, Ralph Abboud, and Simon Woodhead. (2026). Misconception Diagnosis From Student-Tutor Dialogue: Generate, Retrieve, Rerank. arXiv preprint. [doi:10.1145/3774398.3811609](https://doi.org/10.1145/3774398.3811609)"
    author: Joshua Mitton, Prarthana Bhattacharyya, Digory Smith, Thomas Christie, Ralph Abboud, and Simon Woodhead
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: joshua-mitton-2026-2
    resource: "https://doi.org/10.1145/3774398.3811609"
    title: "Joshua Mitton, Prarthana Bhattacharyya, Digory Smith, Thomas Christie, Ralph Abboud, and Simon Woodhead. (2026). Misconception Diagnosis From Student-Tutor Dialogue: Generate, Retrieve, Rerank. arXiv preprint. [doi:10.1145/3774398.3811609](https://doi.org/10.1145/3774398.3811609)"
    author: Joshua Mitton, Prarthana Bhattacharyya, Digory Smith, Thomas Christie, Ralph Abboud, and Simon Woodhead
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LoRA fine-tuning improves generated misconception style and raises cosine similarity with expert labels, letting small open-source models rival larger closed-source ones

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Fine-tuning Llama 3.2 3B LoRA improves every model type across all metrics, and fine-tuned Qwen 2.5 7B outperforms Claude on NDCG. [→ Joshua Mitton 2026](#joshua-mitton-2026)
`q2 i?` Fine-tuned outputs show higher cosine similarity with expert-authored labels than zero-shot outputs for both open-source models. [→ Joshua Mitton 2026 (2)](#joshua-mitton-2026-2)

## Evidence

### Joshua Mitton 2026

Joshua Mitton, Prarthana Bhattacharyya, Digory Smith, Thomas Christie, Ralph Abboud, and Simon Woodhead. (2026). Misconception Diagnosis From Student-Tutor Dialogue: Generate, Retrieve, Rerank. arXiv preprint. [doi:10.1145/3774398.3811609](https://doi.org/10.1145/3774398.3811609)

`q2 · i?` · `design · r2`

Results §5.3 fine-tuning analysis: LoRA fine-tuning (about 0.5% of parameters trainable) improves all metrics for Llama 3.2 3B, and "the fine-tuning of Qwen 2.5 7B does in general improve the model across each of the metrics and notably improves the NDCG score such that the model outperforms Claude".

> "Figures 3, 4, 5, 7 and 6 all show that fine-tuning Llama 3.2 3B LoRA improves each possible model type across all metrics."

### Joshua Mitton 2026 (2)

Joshua Mitton, Prarthana Bhattacharyya, Digory Smith, Thomas Christie, Ralph Abboud, and Simon Woodhead. (2026). Misconception Diagnosis From Student-Tutor Dialogue: Generate, Retrieve, Rerank. arXiv preprint. [doi:10.1145/3774398.3811609](https://doi.org/10.1145/3774398.3811609)

`q2 · i?` · `design · r2`

Discussion §6.2, comparing zero-shot vs fine-tuned generations on the held-out 20% test set: fine-tuned outputs match the concise tutor-annotation format, with "higher cosine similarity between fine-tuned outputs and expert labels" for both open-source models.

> "We see higher cosine similarity between fine-tuned outputs and expert labels in the embedding space as compared to zero-shot misconception hypotheses for both open-source models, in Figure 5."

## Discussion


## Related Claims
- [Adding the generative stage improves or maintains MAP@k and NDCG performance for most model configurations](generative-stage-improves-map-ndcg.md) — related
- [Keyword matching outperforms zero-shot LLM classification and direct embedding on top-1-prioritising metrics for misconception diagnosis from dialogue](keyword-matching-beats-zeroshot-llm-top1-misconception.md) — related
- [LLM reranking of retrieved misconception candidates improves performance, promoting the correct misconception to rank 1 in 73 of 229 reranked cases for Claude](llm-reranking-improves-misconception-retrieval.md) — related
- [LoRA fine-tuning on control systems course data increases lexical and semantic similarity between model responses and course reference answers at both 3B and 7B model sizes](lora-improves-reference-answer-similarity-control-systems.md) — a broader claim this one bears on
- [Under identical LoRA hyperparameters and training data, the 27B Gemma model outperforms the 70B LLaMA model on every computed essay-scoring metric](model-scale-not-predictor-lora-scoring.md) — related
- [LoRA adaptation significantly increases closed-book accuracy on the PhysicsMate test set at all three Qwen3 scales](lora-adaptation-raises-bengali-physics-qa-accuracy-all-scales.md) — related
- [Qwen 2.5 7B performs comparably to Claude Sonnet 4.5 for dialogue-based misconception diagnosis despite being much smaller](qwen-7b-comparable-to-claude-misconception-diagnosis.md) — related
