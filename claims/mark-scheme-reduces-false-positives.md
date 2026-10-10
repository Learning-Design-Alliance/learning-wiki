---
type: claim
title: Including a mark scheme in the prompt does not change misconception detection but significantly reduces false positives against correct-reasoning students
description: Including a mark scheme in the prompt does not change misconception detection but significantly reduces false positives against correct-reasoning students
id: mark-scheme-reduces-false-positives
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: moiz-imran-2026
    resource: "https://orcid.org/0000-0002-5878-2143"
    title: "Moiz Imran, Sahan Bulathwela. (2026). The Correct Answer Trap: Pedagogically-Grounded Detection and Feedback for Hidden Misconceptions. PEAF 2026: Workshop on Pedagogical Evaluation of Automated Feedback. https://orcid.org/0000-0002-5878-2143"
    author: Moiz Imran, Sahan Bulathwela
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Including a mark scheme in the prompt does not change misconception detection but significantly reduces false positives against correct-reasoning students

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Removing the mark scheme from Gemma 4's prompt leaves TM detection unchanged but raises the TC false positive rate from 18.0% to 25.4% (p < 0.001). [→ Moiz Imran 2026](#moiz-imran-2026)

## Evidence

### Moiz Imran 2026

Moiz Imran, Sahan Bulathwela. (2026). The Correct Answer Trap: Pedagogically-Grounded Detection and Feedback for Hidden Misconceptions. PEAF 2026: Workshop on Pedagogical Evaluation of Automated Feedback. https://orcid.org/0000-0002-5878-2143

`q2 · i?` · `causal · r2`

Ablation experiment on Gemma 4 reported in Results. The paper reports the false positive rate rising "from 18.0% to 25.4%" with p < 0.001, while TM detection is unchanged; no effect size is printed.

> "An ablation removing the mark scheme from Gemma 4’s prompt leaves TM detection unchanged but raises the TC false positive rate from 18.0% to 25.4% (𝑝 <0.001 )."

## Discussion


## Related Claims
- [A reasoning-capable open-weight model detects 84% of hidden misconceptions but at realistic prevalence false alarms outnumber genuine detections roughly 8 to 1](reasoning-model-detection-false-alarm-tradeoff.md) — related
- [At natural TM prevalence (1.6%), even the best model generates roughly 4.3 false alarms per genuine detection, making fully automated stand-alone screening not viable on its own](false-alarms-make-standalone-screening-impractical.md) — related
- [A task-specific prompt with explicit guidance about correct-answer cases significantly outperforms literature-based PedCoT prompting on TM test cases (84% vs 59% accuracy)](task-specific-prompt-beats-pedcot-prompting.md) — related
