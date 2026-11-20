---
type: claim
title: "An optimizer LM can iteratively improve math word problem worksheets using an evaluator LM's judgments as the reward function"
description: "An optimizer LM can iteratively improve math word problem worksheets using an evaluator LM's judgments as the reward function"
id: instruction-optimization-improves-worksheets
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: joy-he-yueya-2024
    resource: "https://doi.org/10.48550/arXiv.2403.02795"
    title: "Joy He-Yueya, Noah D. Goodman, Emma Brunskill. (2024). Evaluating and Optimizing Educational Content with Large Language Model Judgments. arXiv preprint. [doi:10.48550/arXiv.2403.02795](https://doi.org/10.48550/arXiv.2403.02795)"
    author: Joy He-Yueya, Noah D. Goodman, Emma Brunskill
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# An optimizer LM can iteratively improve math word problem worksheets using an evaluator LM's judgments as the reward function

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Using GPT-4 as optimizer and GPT-3.5 as evaluator, the post-test score of generated worksheets improves over optimization steps until convergence. [→ Joy He-Yueya 2024](#joy-he-yueya-2024)

## Evidence

### Joy He-Yueya 2024

Joy He-Yueya, Noah D. Goodman, Emma Brunskill. (2024). Evaluating and Optimizing Educational Content with Large Language Model Judgments. arXiv preprint. [doi:10.48550/arXiv.2403.02795](https://doi.org/10.48550/arXiv.2403.02795)

`q2 · i?` · `design · r3`

Numerical optimization result shown in Figure 8: K = 3 worksheets per step over N = 19 steps, each worksheet scored by the average of three independent SEEs on a fixed low-skill student persona. Scores are LM-predicted, not measured on real students.

> "Starting with an initial worksheet that yields a low post-test score (see the first worksheet-score pair in Figure 7), we demonstrate that the optimizer LM (GPT-4) can improve the post-test score of the generated worksheets until convergence (see Figure 8)."

## Discussion


## Related Claims
- [Human teachers' preferences for LM-generated worksheets correlate significantly with evaluator LM judgments (r = 0.661), but teachers sometimes cannot distinguish worksheets the LM perceives as different](lm-judgments-align-with-teacher-preferences.md) — related
- [Optimizing prompts can vastly improve the accuracy of LLM outputs, but critical evaluation of the resulting outputs still requires domain expertise.](prompt-optimization-improves-accuracy-expertise-still-needed.md) — a broader claim this one bears on
