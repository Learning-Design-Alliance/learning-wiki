---
type: claim
title: "The leakage manipulation fires: ConvTutor leaks far more than PedTutor on the primary base, while probe accuracy saturates and cannot distinguish conditions"
description: "The leakage manipulation fires: ConvTutor leaks far more than PedTutor on the primary base, while probe accuracy saturates and cannot distinguish conditions"
id: leakage-manipulation-check-probe-ceiling
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
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

# The leakage manipulation fires: ConvTutor leaks far more than PedTutor on the primary base, while probe accuracy saturates and cannot distinguish conditions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` ConvTutor's mean per-session leakage fraction is 43.0% against 6.4% for PedTutor (P1 supported). [→ Shuyi Fan 2026](#shuyi-fan-2026)

## Evidence

### Shuyi Fan 2026

Shuyi Fan, Boyuan Deng, Mengyu Xu, Jiale Liu, Hongyang Zhang, Qiaoxin Yang, Chongyang Gao. (2026). Rethinking LLM-Judged Helpfulness as a Pedagogy Signal: A Pre-Registered Audit Across Tutor Models. arXiv. https://arxiv.org/abs/2607.28128 [doi:10.48550/arxiv.2607.28128](https://doi.org/10.48550/arxiv.2607.28128)

`q3 · i?` · `causal · r2`

Deterministic manipulation check on the primary base with ten paired replicates; independence moved in the predicted direction but did not separate (P3 inconclusive), and probe accuracy saturated (0.77 to 1.00 across probe phases in all three conditions).

> "ConvTutor’s mean per-session leakage fraction is 43.0% against 6.4% for PedTutor (P1 supported: paired difference+0.365, 95% CI[+0.217,+0.516], nine of ten replicate pairs; Table 2)."

## Discussion


## Related Claims
- [On the primary base under the frozen Opus judge, ConvTutor and PedTutor do not differ significantly in judged helpfulness but are perfectly rank-separated in judged pedagogy](helpfulness-pedagogy-dissociation-primary-base.md) — related
- [On the primary base, a turn that leaks the answer predicts a higher Opus helpfulness rating and less next-turn independent student work](per-turn-leakage-coupling-primary-base.md) — related
- [Answer-revealing tutor turns are followed by less independent student work on every tutor base, a deterministic judge-invariant result](leakage-reduces-next-turn-independence-all-bases.md) — related
- [A contingent tutor surrendered the full answer in one session in sixteen, against one in six for the question-only tutor](contingent-scaffolding-surrenders-full-answer-least.md) — related
