---
type: claim
title: Adding gate-failure penalties based on predefined pedagogical criteria harms teaching performance and generalization, while training on student improvement alone allows broader capabilities to emerge
description: Adding gate-failure penalties based on predefined pedagogical criteria harms teaching performance and generalization, while training on student improvement alone allows broader capabilities to emerge
id: gate-penalties-harm-generalization-student-improvement-reward
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: weixian-xu-2026
    resource: "https://doi.org/10.48550/arXiv.2610.08778"
    title: "Weixian Xu, Yanzhe Zhang, Zora Zhiruo Wang, Changyu Chen, Diyi Yang. (2026). SHERPA: TEACHINGLLMS TOTEACHADAPTIVELY. [doi:10.48550/arXiv.2610.08778](https://doi.org/10.48550/arXiv.2610.08778)"
    author: Weixian Xu, Yanzhe Zhang, Zora Zhiruo Wang, Changyu Chen, Diyi Yang
    q: 2
    i: "?"
    kind: causal
    rigour: "?"
---

# Adding gate-failure penalties based on predefined pedagogical criteria harms teaching performance and generalization, while training on student improvement alone allows broader capabilities to emerge

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Pedagogy Average drops from 79.2% without gate penalties to 70.6% with a 0.25 penalty and 66.0% with a 0.5 penalty, and a larger penalty markedly reduces performance including OOD generalization. [→ Weixian Xu 2026](#weixian-xu-2026)

## Evidence

### Weixian Xu 2026

Weixian Xu, Yanzhe Zhang, Zora Zhiruo Wang, Changyu Chen, Diyi Yang. (2026). SHERPA: TEACHINGLLMS TOTEACHADAPTIVELY. [doi:10.48550/arXiv.2610.08778](https://doi.org/10.48550/arXiv.2610.08778)

`q2 · i?` · `causal · r?`

Ablation comparing SHERPA variants with gate-failure penalty magnitudes of 0.25 and 0.5, evaluated on held-out MathTutorBench (Figure 4). The article concludes "adding penalties based on predefined criteria harms generalization" while student-improvement rewards support broader teaching capabilities.

> "performance across all four pedagogical dimensions declines as the penalty increases, with Pedagogy Average dropping from 79.2% without gate penalties to 70.6% with a penalty of 0.25 and 66.0% with a penalty of 0.5."

## Discussion


## Related Claims
- [A screenshot-only reward was reward-hacked into producing visually convincing but unplayable games; hardening the reward with an interactivity probe and hard-fail gate reversed the collapse](reward-hacking-games-interactivity-probe.md) — related
- [SHERPA training transfers to the external MathTutorBench benchmark, raising the pedagogy average from 52.5% to 79.2% and beating PedagogicalRL on all four response-generation metrics](sherpa-transfers-mathtutorbench-pedagogy.md) — related
- [The binary reward gates govern whether the tutor tells while the masked near-transfer post-test shapes how it teaches](gates-decide-whether-tutor-tells-transfer-shapes-how.md) — related
- [A learning-gain reward alone does not separate teaching from telling: a policy trained without the binary gates hands over the solution in 61% of dialogs at the same simulated gain](learning-gain-reward-alone-does-not-separate-teaching-from-telling.md) — related
