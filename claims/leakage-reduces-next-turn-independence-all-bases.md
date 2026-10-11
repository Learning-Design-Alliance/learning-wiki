---
type: claim
title: Answer-revealing tutor turns are followed by less independent student work on every tutor base, a deterministic judge-invariant result
description: Answer-revealing tutor turns are followed by less independent student work on every tutor base, a deterministic judge-invariant result
id: leakage-reduces-next-turn-independence-all-bases
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: shuyi-fan-2026
    resource: "https://arxiv.org/abs/2607.28128"
    title: "Shuyi Fan, Boyuan Deng, Mengyu Xu, Jiale Liu, Hongyang Zhang, Qiaoxin Yang, Chongyang Gao. (2026). Rethinking LLM-Judged Helpfulness as a Pedagogy Signal: A Pre-Registered Audit Across Tutor Models. arXiv. https://arxiv.org/abs/2607.28128"
    author: Shuyi Fan, Boyuan Deng, Mengyu Xu, Jiale Liu, Hongyang Zhang, Qiaoxin Yang, Chongyang Gao
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Answer-revealing tutor turns are followed by less independent student work on every tutor base, a deterministic judge-invariant result

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`

## Subclaims
`q3 i?` Leakage predicted less independent student work on every base, with pooled coefficients from −0.386 to −0.592, all p<10−11. [→ Shuyi Fan 2026](#shuyi-fan-2026)

## Evidence

### Shuyi Fan 2026

Shuyi Fan, Boyuan Deng, Mengyu Xu, Jiale Liu, Hongyang Zhang, Qiaoxin Yang, Chongyang Gao. (2026). Rethinking LLM-Judged Helpfulness as a Pedagogy Signal: A Pre-Registered Audit Across Tutor Models. arXiv. https://arxiv.org/abs/2607.28128

`q3 · i?` · `causal · r2`

Deterministic process analysis across the three tutor bases (358, 379, and 442 answer-phase tutor turns), using string-match leakage detection and a reasoning detector; a replicate-clustered sensitivity analysis yielded comparable estimates on all three bases (all p≤.006).

> "Leakage predicted less independent student work on every base (βfrom −0.386to−0.592, allp<10 −11; Table 2b)."

## Discussion


## Related Claims
- [On the primary base, a turn that leaks the answer predicts a higher Opus helpfulness rating and less next-turn independent student work](per-turn-leakage-coupling-primary-base.md) — a narrower finding that bears on this claim
- [Single-turn tutors disclose answers pervasively while challenge scores are near zero across every model and subject](single-turn-answer-disclosure-challenge-near-zero.md) — related
