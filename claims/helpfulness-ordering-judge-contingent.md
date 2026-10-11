---
type: claim
title: The ConvTutor–PedTutor helpfulness ordering is judge-contingent, reversing between the Opus and Sol judges on two of three tutor bases
description: The ConvTutor–PedTutor helpfulness ordering is judge-contingent, reversing between the Opus and Sol judges on two of three tutor bases
id: helpfulness-ordering-judge-contingent
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

# The ConvTutor–PedTutor helpfulness ordering is judge-contingent, reversing between the Opus and Sol judges on two of three tutor bases

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`

## Subclaims
`q3 i?` The helpfulness ordering reversed between Opus and Sol on the Sonnet and GPT-5.5 bases, replicating only on Gemini. [→ Shuyi Fan 2026](#shuyi-fan-2026)

## Evidence

### Shuyi Fan 2026

Shuyi Fan, Boyuan Deng, Mengyu Xu, Jiale Liu, Hongyang Zhang, Qiaoxin Yang, Chongyang Gao. (2026). Rethinking LLM-Judged Helpfulness as a Pedagogy Signal: A Pre-Registered Audit Across Tutor Models. arXiv. https://arxiv.org/abs/2607.28128

`q3 · i?` · `causal · r2`

Post hoc cross-judge robustness audit in which GPT-5.6 Sol rescored the identical 1,179 confirmatory answer-phase tutor turns under the frozen rubrics; on the GPT-5.5 base the two contrasts were "significant and opposite" (Opus −0.376 vs. Sol +0.086).

> "The ConvTutor–PedTutor helpfulness ordering reversed between OpusandSolontwoofthreebases(Table2a)."

## Discussion


## Related Claims
- [On the primary base under the frozen Opus judge, ConvTutor and PedTutor do not differ significantly in judged helpfulness but are perfectly rank-separated in judged pedagogy](helpfulness-pedagogy-dissociation-primary-base.md) — related
- [In blind verification, model selection matters more than source type: Bradley-Terry ranking interleaves human coders and LLMs, with per-model win rates spanning significant human advantage to numerical LLM advantage](bradley-terry-model-selection-matters-more-than-source-type.md) — a broader claim this one bears on
- [On the primary base, a turn that leaks the answer predicts a higher Opus helpfulness rating and less next-turn independent student work](per-turn-leakage-coupling-primary-base.md) — related
- [In the Opus-only ablation, a prompt-only Socratic instruction outscores the full routed policy on judged pedagogy at near-tied helpfulness](socratic-prompt-only-matches-routed-pedagogy.md) — related
