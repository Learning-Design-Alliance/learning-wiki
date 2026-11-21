---
type: claim
title: "Adding the generative stage improves or maintains MAP@k and NDCG performance for most model configurations"
description: "Adding the generative stage improves or maintains MAP@k and NDCG performance for most model configurations"
id: generative-stage-improves-map-ndcg
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
---

# Adding the generative stage improves or maintains MAP@k and NDCG performance for most model configurations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For fine-tuned Llama 3.2 3B LoRA, zero-shot Qwen 2.5 7B and fine-tuned Qwen 2.5 7B LoRA, including the generative stage leaves MAP@k and NDCG equivalent or improved. [→ Joshua Mitton 2026](#joshua-mitton-2026)

## Evidence

### Joshua Mitton 2026

Joshua Mitton, Prarthana Bhattacharyya, Digory Smith, Thomas Christie, Ralph Abboud, and Simon Woodhead. (2026). Misconception Diagnosis From Student-Tutor Dialogue: Generate, Retrieve, Rerank. arXiv preprint. [doi:10.1145/3774398.3811609](https://doi.org/10.1145/3774398.3811609)

`q2 · i?` · `design · r2`

Ablation study in Results §5.3 isolating the generative hypothesis stage across model configurations. The article reports MAP@k and NDCG "is either equivalent or improved by the inclusion of the generative stage".

> "Figures 3 and 4 show that for the fine-tuned Llama 3.2 3B LoRA model, zero-shot Qwen 2.5 7B, and fine-tuned Qwen 2.5 7B LoRA the MAP@k and NDCG performance is either equivalent or improved by the inclusion of the generative stage of the model."

## Discussion


## Related Claims
- [LoRA fine-tuning improves generated misconception style and raises cosine similarity with expert labels, letting small open-source models rival larger closed-source ones](lora-finetuning-improves-misconception-generation-style.md) — related
- [LLM reranking of retrieved misconception candidates improves performance, promoting the correct misconception to rank 1 in 73 of 229 reranked cases for Claude](llm-reranking-improves-misconception-retrieval.md) — related
- [Qwen 2.5 7B performs comparably to Claude Sonnet 4.5 for dialogue-based misconception diagnosis despite being much smaller](qwen-7b-comparable-to-claude-misconception-diagnosis.md) — related
