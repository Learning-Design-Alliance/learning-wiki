---
type: claim
title: "On the Debugging Task, CoTAL raised average subscore QWK from 0.567 to 0.706 (24.5% improvement) and Total Score QWK by 0.218 (a 38.9% gain) over the Baseline"
description: "On the Debugging Task, CoTAL raised average subscore QWK from 0.567 to 0.706 (24.5% improvement) and Total Score QWK by 0.218 (a 38.9% gain) over the Baseline"
id: cotal-debugging-task-qwk-gain
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
    rigour: 3
---

# On the Debugging Task, CoTAL raised average subscore QWK from 0.567 to 0.706 (24.5% improvement) and Total Score QWK by 0.218 (a 38.9% gain) over the Baseline

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`

## Subclaims
`q2 i?` For the Debugging Task, CoTAL yielded an average QWK of 0.706 versus the Baseline's 0.567 (24.5% improvement), and Total Score QWK increased by 0.218 (a 38.9% gain). [→ Cohn 2026](#cohn-2026)

## Evidence

### Cohn 2026

Cohn, C., Ashwin T S, Mohammed, N., & Biswas, G. (2026). CoTAL: Human-in-the-Loop Prompt Engineering for Generalizable Formative Assessment Scoring and Feedback. arXiv preprint. https://arxiv.org/abs/2504.02323

`q2 · i?` · `design · r3`

Quantitative evaluation of GPT-4 scoring on Debugging Task responses from 166 sixth-grade students, comparing CoTAL to a zero-shot Baseline with Cohen's QWK on held-out test data. The article reports "a 24.5% improvement" and, for Total Score, "QWKincreasedby0.218(a38.9%gain)" (Table 5: 0.561 to 0.779).

> "FortheDebuggingTask,theBaselineimplementationachievedanaverageQWKof0.567,whereasCoTALyielded an average QWK of0.706, a 24.5% improvement."

## Discussion


## Related Claims
- [CoTAL improves GPT-4 scoring agreement with human scorers on the Rules Task, raising average subscore QWK from 0.826 to 0.916 (a 10.9% gain) over a non-prompt-engineered baseline](cotal-rules-task-qwk-gain.md) — related
- [CoTAL reduced false positives in Rules Task subscore predictions from 7 to 1 while increasing false negatives by only 1, via active-learning targeting of persistent errors](cotal-reduces-false-positives-rules-task.md) — related
