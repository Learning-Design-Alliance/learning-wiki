---
type: claim
title: On the primary base under the frozen Opus judge, ConvTutor and PedTutor do not differ significantly in judged helpfulness but are perfectly rank-separated in judged pedagogy
description: On the primary base under the frozen Opus judge, ConvTutor and PedTutor do not differ significantly in judged helpfulness but are perfectly rank-separated in judged pedagogy
id: helpfulness-pedagogy-dissociation-primary-base
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: shuyi-fan-2026
    resource: "https://doi.org/10.48550/arxiv.2607.28128"
    title: "Shuyi Fan, Boyuan Deng, Mengyu Xu, Jiale Liu, Hongyang Zhang, Qiaoxin Yang, Chongyang Gao. (2026). Rethinking LLM-Judged Helpfulness as a Pedagogy Signal: A Pre-Registered Audit Across Tutor Models. arXiv. https://arxiv.org/abs/2607.28128 [doi:10.48550/arxiv.2607.28128](https://doi.org/10.48550/arxiv.2607.28128)"
    author: Shuyi Fan, Boyuan Deng, Mengyu Xu, Jiale Liu, Hongyang Zhang, Qiaoxin Yang, Chongyang Gao
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# On the primary base under the frozen Opus judge, ConvTutor and PedTutor do not differ significantly in judged helpfulness but are perfectly rank-separated in judged pedagogy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`

## Subclaims
`q3 i?` Under Opus, a helpfulness contrast that does not differ significantly (Cliff's |δ|=0.10) sits beside a maximal pedagogy contrast (|δ|=1.0) on the same turns. [→ Shuyi Fan 2026](#shuyi-fan-2026)

## Evidence

### Shuyi Fan 2026

Shuyi Fan, Boyuan Deng, Mengyu Xu, Jiale Liu, Hongyang Zhang, Qiaoxin Yang, Chongyang Gao. (2026). Rethinking LLM-Judged Helpfulness as a Pedagogy Signal: A Pre-Registered Audit Across Tutor Models. arXiv. https://arxiv.org/abs/2607.28128 [doi:10.48550/arxiv.2607.28128](https://doi.org/10.48550/arxiv.2607.28128)

`q3 · i?` · `causal · r2`

Pre-registered within-base experiment on the Claude Sonnet 4.6 primary base with ten paired replicates per condition; judged pedagogy averaged 2.578 for ConvTutor versus 4.299 for PedTutor, with "the separation is perfect at the replicate level" reported as a manipulation check.

> "underOpus,ratingthesameturnsundertworubrics,ahelpfulness contrast that does not differ significantly (|δ|=0.10) sits beside a maximal pedagogy contrast (|δ|=1.0)."

## Discussion


## Related Claims
- [The ConvTutor–PedTutor helpfulness ordering is judge-contingent, reversing between the Opus and Sol judges on two of three tutor bases](helpfulness-ordering-judge-contingent.md) — related
- [In the Opus-only ablation, a prompt-only Socratic instruction outscores the full routed policy on judged pedagogy at near-tied helpfulness](socratic-prompt-only-matches-routed-pedagogy.md) — related
- [On the primary base, a turn that leaks the answer predicts a higher Opus helpfulness rating and less next-turn independent student work](per-turn-leakage-coupling-primary-base.md) — related
- [The leakage manipulation fires: ConvTutor leaks far more than PedTutor on the primary base, while probe accuracy saturates and cannot distinguish conditions](leakage-manipulation-check-probe-ceiling.md) — related
