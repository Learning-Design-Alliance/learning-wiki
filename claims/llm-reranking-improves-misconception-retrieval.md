---
type: claim
title: LLM reranking of retrieved misconception candidates improves performance, promoting the correct misconception to rank 1 in 73 of 229 reranked cases for Claude
description: LLM reranking of retrieved misconception candidates improves performance, promoting the correct misconception to rank 1 in 73 of 229 reranked cases for Claude
id: llm-reranking-improves-misconception-retrieval
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

# LLM reranking of retrieved misconception candidates improves performance, promoting the correct misconception to rank 1 in 73 of 229 reranked cases for Claude

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Including the reranking stage improves all metrics for Claude Sonnet 4.5 and Qwen 2.5 7B, and for fine-tuned LoRA Llama 3.2 3B. [→ Joshua Mitton 2026](#joshua-mitton-2026)
`q2 i?` Reranking promoted the correct misconception to rank 1 in 73 cases out of 229 reranked cases for Claude Sonnet 4.5. [→ Joshua Mitton 2026 (2)](#joshua-mitton-2026-2)

## Evidence

### Joshua Mitton 2026

Joshua Mitton, Prarthana Bhattacharyya, Digory Smith, Thomas Christie, Ralph Abboud, and Simon Woodhead. (2026). Misconception Diagnosis From Student-Tutor Dialogue: Generate, Retrieve, Rerank. arXiv preprint. [doi:10.1145/3774398.3811609](https://doi.org/10.1145/3774398.3811609)

`q2 · i?` · `design · r2`

Ablation in Results §5.3 testing the reranking stage across models and metrics (MAP@k, NDCG, recall, rank). For Claude Sonnet 4.5 "including the reranking stage improves all metrics"; Qwen 2.5 7B also improves across all metrics.

> "Figures 3, 4, 6 and 7 demonstrate that for Claude Sonnet 4.5 including the reranking stage improves all metrics."

### Joshua Mitton 2026 (2)

Joshua Mitton, Prarthana Bhattacharyya, Digory Smith, Thomas Christie, Ralph Abboud, and Simon Woodhead. (2026). Misconception Diagnosis From Student-Tutor Dialogue: Generate, Retrieve, Rerank. arXiv preprint. [doi:10.1145/3774398.3811609](https://doi.org/10.1145/3774398.3811609)

`q2 · i?` · `design · r2`

Discussion §6.4 case analysis of Claude Sonnet 4.5 reranking: the correct misconception was "promoted ... to rank 1 in 73 cases ... out of 229 reranked cases", typically where embedding retrieval placed it at rank 2 or lower.

> "Our re-rank approach, which re-ranks the top retrieved candidates, successfully promoted the correct misconception to rank 1 in 73 cases for Claude Sonnet 4.5 out of 229 reranked cases."

## Discussion


## Related Claims
- [Adding the generative stage improves or maintains MAP@k and NDCG performance for most model configurations](generative-stage-improves-map-ndcg.md) — related
- [Qwen 2.5 7B performs comparably to Claude Sonnet 4.5 for dialogue-based misconception diagnosis despite being much smaller](qwen-7b-comparable-to-claude-misconception-diagnosis.md) — related
- [LoRA fine-tuning improves generated misconception style and raises cosine similarity with expert labels, letting small open-source models rival larger closed-source ones](lora-finetuning-improves-misconception-generation-style.md) — related
