---
type: claim
title: In a 10-student pilot, EduGuard produced higher post-test accuracy, larger normalized learning gain, lower calibration error, and lower overreliance than GPT-4o-mini Tutor
description: In a 10-student pilot, EduGuard produced higher post-test accuracy, larger normalized learning gain, lower calibration error, and lower overreliance than GPT-4o-mini Tutor
id: eduguard-pilot-learning-gain-overreliance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
newest_evidence: 2026
source_checked: 2026-10-20
sources:
  - id: s-m-asif-hossain-2026
    resource: "https://doi.org/10.48550/arxiv.2607.15738"
    title: "S M Asif Hossain, Ruksat Khan Shayoni, M. F. Mridha, and Jungpil Shin. (2026). EduGuard: A Safe RAG-Based LLM Tutor for Programming Education. arXiv preprint arXiv:2607.15738. https://arxiv.org/abs/2607.15738 [doi:10.48550/arxiv.2607.15738](https://doi.org/10.48550/arxiv.2607.15738)"
    author: S M Asif Hossain, Ruksat Khan Shayoni, M. F. Mridha, and Jungpil Shin
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# In a 10-student pilot, EduGuard produced higher post-test accuracy, larger normalized learning gain, lower calibration error, and lower overreliance than GPT-4o-mini Tutor

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-20 (automated, 1 of 1 entry) · not reviewed by a person

## Subclaims
`q2 i?` EduGuard produced higher immediate post-test accuracy, larger normalized learning gain, lower confidence calibration error, and lower overreliance behavior than GPT-4o-mini Tutor in a counterbalanced within-subject pilot. [→ S M Asif Hossain 2026](#s-m-asif-hossain-2026)

## Evidence

### S M Asif Hossain 2026

S M Asif Hossain, Ruksat Khan Shayoni, M. F. Mridha, and Jungpil Shin. (2026). EduGuard: A Safe RAG-Based LLM Tutor for Programming Education. arXiv preprint arXiv:2607.15738. https://arxiv.org/abs/2607.15738 [doi:10.48550/arxiv.2607.15738](https://doi.org/10.48550/arxiv.2607.15738)

`q2 · i?` · `causal · r1`

Small controlled pilot with "a counterbalanced within-subject design"; each of 10 students solved two matched programming tasks, one per tutor. Table 4 reports post-test accuracy 81.2 vs 74.2, normalized gain 0.41 vs 0.20, overreliance 17.0 vs 38.0. The article also notes students using EduGuard asked more follow-up clarification questions.

> "EduGuard produced higher immediate post-test accuracy, larger normalized learning gain, lower confidence calibration error, and lower overreliance behavior than GPT-4o-mini Tutor."

## Discussion


## Learner Variables
- [Metacognition](../learner-variables/metacognition.md) — outcome: instruction changes it

## Related Claims
- [On the MathDial problem set with SymPy access, o3-mini(high) and Claude 3.5 Sonnet achieved the highest problem-solving accuracy at 90.00%](o3-mini-highest-mathdial-accuracy.md) — related
- [A pedagogically informed Tutor Prompt yields higher Success@N and lower Telling@N than MathDial's Base Prompt in simulated tutor-student dialogues](tutor-prompt-outperforms-base-prompt-mathdial.md) — related
- [In math problem solving, a tutor-plus-peers LLM arrangement produced the strongest unassisted post-task test accuracy, with accuracy increasing monotonically from Control to Tutor + Peers](tutor-plus-peers-strongest-unassisted-math-accuracy.md) — related
- [Model selection experiments show newer models are not strict improvements, with component-specific effects on quality metrics](model-migration-component-specific-metric-effects.md) — related
- [GPT-4 generates targeted corrective feedback for 66% of student errors, but 35% of hints are too general, incorrect, or give away the answer](gpt4-feedback-66-percent-targeted-35-percent-flawed.md) — related
