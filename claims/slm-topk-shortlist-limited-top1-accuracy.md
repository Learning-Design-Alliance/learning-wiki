---
type: claim
title: Fine-tuned SLMs retrieve the correct concept within a top-K shortlist but have limited top-1 accuracy
description: Fine-tuned SLMs retrieve the correct concept within a top-K shortlist but have limited top-1 accuracy
id: slm-topk-shortlist-limited-top1-accuracy
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: zhiwei-yang-2026
    resource: "https://arxiv.org/abs/2609.36982"
    title: "Zhiwei Yang, Jiahua Yang, Huiru Lin, Xing Chen, and Quanlong Guan. (2026). SRJudge: Empowering Large Language Models with Selective Reasoning for Fine-Grained Knowledge Concept Tagging. arXiv preprint. https://arxiv.org/abs/2609.36982"
    author: Zhiwei Yang, Jiahua Yang, Huiru Lin, Xing Chen, and Quanlong Guan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fine-tuned SLMs retrieve the correct concept within a top-K shortlist but have limited top-1 accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Preliminary experiments show traditional SLMs capture the correct option within the top-K shortlist but their accuracy remains limited when relying solely on the top-1 prediction. [→ Zhiwei Yang 2026](#zhiwei-yang-2026)

## Evidence

### Zhiwei Yang 2026

Zhiwei Yang, Jiahua Yang, Huiru Lin, Xing Chen, and Quanlong Guan. (2026). SRJudge: Empowering Large Language Models with Selective Reasoning for Fine-Grained Knowledge Concept Tagging. arXiv preprint. https://arxiv.org/abs/2609.36982

`q2 · i?` · `design · r2`

Preliminary study (Table 1) fine-tuning Chinese-BERT, Chinese-RoBERTa and Conan-embedding on the three datasets, reporting ACC and ACC@5; for example Chinese-BERT reaches ACC@5 of 0.9377 on S Bio versus ACC of 0.7216. The article attributes the gap to semantic similarity among concepts within the top-K candidates.

> "traditional SLMs can effectively capture the correct options within the topKshortlist, but their accuracy remains limited when relying solely on the top-1 prediction."

## Discussion


## Related Claims
- [On a preliminary three-question retrieval sanity check, all seed questions placed their target concept first and within the top three, with mean top-5 recall of 1.00](three-seed-retrieval-sanity-check-perfect.md) — related
- [Each SRJudge component contributes: the Reasoner and Judger add measurable F1 gains over the Selector alone](srjudge-ablation-components-contribute.md) — related
