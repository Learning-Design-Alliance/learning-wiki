---
type: claim
title: On the primary base, a turn that leaks the answer predicts a higher Opus helpfulness rating and less next-turn independent student work
description: On the primary base, a turn that leaks the answer predicts a higher Opus helpfulness rating and less next-turn independent student work
id: per-turn-leakage-coupling-primary-base
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

# On the primary base, a turn that leaks the answer predicts a higher Opus helpfulness rating and less next-turn independent student work

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`

## Subclaims
`q3 i?` Both legs of the pre-registered J2 coupling hold on the primary base (n=358 answer-phase tutor turns). [→ Shuyi Fan 2026](#shuyi-fan-2026)

## Evidence

### Shuyi Fan 2026

Shuyi Fan, Boyuan Deng, Mengyu Xu, Jiale Liu, Hongyang Zhang, Qiaoxin Yang, Chongyang Gao. (2026). Rethinking LLM-Judged Helpfulness as a Pedagogy Signal: A Pre-Registered Audit Across Tutor Models. arXiv. https://arxiv.org/abs/2607.28128 [doi:10.48550/arxiv.2607.28128](https://doi.org/10.48550/arxiv.2607.28128)

`q3 · i?` · `causal · r2`

Pre-registered per-turn mixed-effects coupling on the Sonnet base (n=358); descriptively, leaky turns were rated 4.95 versus 4.67 and followed by a reasoning attempt 33% versus 73% of the time. Both associations persisted in the matched visible-turn re-analysis (n=256).

> "Under Opus, a turn that leaks the answer predicts a higher helpfulness rating (coefficient+0.303, 95% CI[+0.169,+0.437],p=9.1×10 −6); deterministically, it is followed by less independent student work on the followingturn(−0.386,CI[−0.495,−0.276],p=5.6×10 −12)."

## Discussion


## Related Claims
- [The ConvTutor–PedTutor helpfulness ordering is judge-contingent, reversing between the Opus and Sol judges on two of three tutor bases](helpfulness-ordering-judge-contingent.md) — related
- [On the primary base under the frozen Opus judge, ConvTutor and PedTutor do not differ significantly in judged helpfulness but are perfectly rank-separated in judged pedagogy](helpfulness-pedagogy-dissociation-primary-base.md) — related
- [The leakage manipulation fires: ConvTutor leaks far more than PedTutor on the primary base, while probe accuracy saturates and cannot distinguish conditions](leakage-manipulation-check-probe-ceiling.md) — related
- [Answer-revealing tutor turns are followed by less independent student work on every tutor base, a deterministic judge-invariant result](leakage-reduces-next-turn-independence-all-bases.md) — a broader claim this one bears on
- [In the Opus-only ablation, a prompt-only Socratic instruction outscores the full routed policy on judged pedagogy at near-tied helpfulness](socratic-prompt-only-matches-routed-pedagogy.md) — related
