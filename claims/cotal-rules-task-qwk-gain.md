---
type: claim
title: "CoTAL improves GPT-4 scoring agreement with human scorers on the Rules Task, raising average subscore QWK from 0.826 to 0.916 (a 10.9% gain) over a non-prompt-engineered baseline"
description: "CoTAL improves GPT-4 scoring agreement with human scorers on the Rules Task, raising average subscore QWK from 0.826 to 0.916 (a 10.9% gain) over a non-prompt-engineered baseline"
id: cotal-rules-task-qwk-gain
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

# CoTAL improves GPT-4 scoring agreement with human scorers on the Rules Task, raising average subscore QWK from 0.826 to 0.916 (a 10.9% gain) over a non-prompt-engineered baseline

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`

## Subclaims
`q2 i?` Applying CoTAL to the Rules Task raised average subscore QWK from 0.826 (Baseline) to 0.916, an average increase of 0.090 (10.9%), and Total Score QWK from 0.930 to 0.968. [→ Cohn 2026](#cohn-2026)

## Evidence

### Cohn 2026

Cohn, C., Ashwin T S, Mohammed, N., & Biswas, G. (2026). CoTAL: Human-in-the-Loop Prompt Engineering for Generalizable Formative Assessment Scoring and Feedback. arXiv preprint. https://arxiv.org/abs/2504.02323

`q2 · i?` · `design · r3`

Quantitative evaluation of GPT-4 scoring on held-out test responses (n=32 test instances for Total Score) from 158 sixth-grade students' Rules Task responses, using Cohen's QWK against human consensus scores. The evaluation found "an average increase of 0.090 (10.9%) over the Baseline"; Total Score QWK rose from 0.930 to 0.968 (Table 4).

> "Applying CoTALresultedinanaverageQWKof0.916,whichrepresentsanaverageincreaseof0.090(10.9%)overtheBaseline whileusingCoTAL."

## Discussion


## Related Claims
- [On the Debugging Task, CoTAL raised average subscore QWK from 0.567 to 0.706 (24.5% improvement) and Total Score QWK by 0.218 (a 38.9% gain) over the Baseline](cotal-debugging-task-qwk-gain.md) — related
- [CoTAL reduced false positives in Rules Task subscore predictions from 7 to 1 while increasing false negatives by only 1, via active-learning targeting of persistent errors](cotal-reduces-false-positives-rules-task.md) — related
- [In the Overview dimension, augmentation produced a marginal QWK decrease (ΔQWK = −0.006) despite improving macro-F1, the only dimension with this trade-off](overview-augmentation-qwk-tradeoff.md) — related
- [Despite generally accurate feedback, the LLM's scoring explanations could be unpredictable and prone to logical inconsistency, failing to award points even when citing the correct rubric directive](llm-logical-inconsistency-scoring-feedback.md) — related
