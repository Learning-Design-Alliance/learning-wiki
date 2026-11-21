---
type: claim
title: Keyword matching outperforms zero-shot LLM classification and direct embedding on top-1-prioritising metrics for misconception diagnosis from dialogue
description: Keyword matching outperforms zero-shot LLM classification and direct embedding on top-1-prioritising metrics for misconception diagnosis from dialogue
id: keyword-matching-beats-zeroshot-llm-top1-misconception
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

# Keyword matching outperforms zero-shot LLM classification and direct embedding on top-1-prioritising metrics for misconception diagnosis from dialogue

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On metrics prioritising top-1 prediction, TF-IDF keyword matching outperforms both zero-shot LLM classification and direct embedding of dialogue text. [→ Joshua Mitton 2026](#joshua-mitton-2026)

## Evidence

### Joshua Mitton 2026

Joshua Mitton, Prarthana Bhattacharyya, Digory Smith, Thomas Christie, Ralph Abboud, and Simon Woodhead. (2026). Misconception Diagnosis From Student-Tutor Dialogue: Generate, Retrieve, Rerank. arXiv preprint. [doi:10.1145/3774398.3811609](https://doi.org/10.1145/3774398.3811609)

`q2 · i?` · `design · r2`

Evaluation of three baselines (TF-IDF keyword matching, zero-shot Claude classification over 546 labels, direct MiniLM embedding) on the dialogue misconception task, reported in Results §5.1. The article states keyword matching "outperforms a zero-shot LLM classification and directly using an embedding model" on top-1 metrics.

> "Figures 3 and 4 show that keyword matching outperforms a zero-shot LLM classification and directly using an embedding model on metrics that prioritise top-1 prediction."

## Discussion


## Related Claims
- [LoRA fine-tuning improves generated misconception style and raises cosine similarity with expert labels, letting small open-source models rival larger closed-source ones](lora-finetuning-improves-misconception-generation-style.md) — related
- [Sentiment classification transfers to English under the unchanged protocol, with a frozen multilingual encoder the strongest arm at wF1 0.73 and LLMs matching it only with few-shot prompting](english-sentiment-transfer-encoder-strongest.md) — related
