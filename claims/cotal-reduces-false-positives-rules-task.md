---
type: claim
title: CoTAL reduced false positives in Rules Task subscore predictions from 7 to 1 while increasing false negatives by only 1, via active-learning targeting of persistent errors
description: CoTAL reduced false positives in Rules Task subscore predictions from 7 to 1 while increasing false negatives by only 1, via active-learning targeting of persistent errors
id: cotal-reduces-false-positives-rules-task
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: cohn-2026
    resource: "https://arxiv.org/abs/2504.02323"
    title: "Cohn, C., Ashwin T S, Mohammed, N., & Biswas, G. (2026). CoTAL: Human-in-the-Loop Prompt Engineering for Generalizable Formative Assessment Scoring and Feedback. arXiv preprint. https://arxiv.org/abs/2504.02323"
    author: "Cohn, C., Ashwin T S, Mohammed, N., & Biswas, G."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# CoTAL reduced false positives in Rules Task subscore predictions from 7 to 1 while increasing false negatives by only 1, via active-learning targeting of persistent errors

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On the Rules Task, CoTAL reduced false positives in individual subscores from 7 to 1 while increasing false negatives by only 1; active learning favored false positives over false negatives by a 2:1 ratio. [→ Cohn 2026](#cohn-2026)

## Evidence

### Cohn 2026

Cohn, C., Ashwin T S, Mohammed, N., & Biswas, G. (2026). CoTAL: Human-in-the-Loop Prompt Engineering for Generalizable Formative Assessment Scoring and Feedback. arXiv preprint. https://arxiv.org/abs/2504.02323

`q2 · i?` · `design · r2`

Error analysis of the Rules Task scoring evaluation (test set of 32 instances), counting LLM false positives and false negatives per subscore under Baseline versus CoTAL. The article reports CoTAL "reducedfalsepositivesinindividualsubscoresfrom7to1" and that active learning deliberately weighted this trade-off.

> "CoTALreducedfalsepositivesinindividualsubscoresfrom7to1whileonlyincreasingfalsenegativesby1.Thiswas explicitly addressed during Active Learning, which favored false positives over false negatives by a 2:1 ratio."

## Discussion


## Related Claims
- [On the Debugging Task, CoTAL raised average subscore QWK from 0.567 to 0.706 (24.5% improvement) and Total Score QWK by 0.218 (a 38.9% gain) over the Baseline](cotal-debugging-task-qwk-gain.md) — related
- [CoTAL improves GPT-4 scoring agreement with human scorers on the Rules Task, raising average subscore QWK from 0.826 to 0.916 (a 10.9% gain) over a non-prompt-engineered baseline](cotal-rules-task-qwk-gain.md) — related
