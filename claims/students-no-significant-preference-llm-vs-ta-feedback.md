---
type: claim
title: Students showed no significant overall preference between LLM and TA feedback, preferred LLM feedback on correctly answered questions, and disliked only Nvidia-70B feedback on incorrect answers
description: Students showed no significant overall preference between LLM and TA feedback, preferred LLM feedback on correctly answered questions, and disliked only Nvidia-70B feedback on incorrect answers
id: students-no-significant-preference-llm-vs-ta-feedback
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: pavlin-g-poliˇcar-2025
    resource: "https://doi.org/10.1093/bioinformatics/btaf196"
    title: "Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan. (2025). Automated Assignment Grading with Large Language Models: Insights from a Bioinformatics Course. [doi:10.1093/bioinformatics/btaf196](https://doi.org/10.1093/bioinformatics/btaf196)"
    author: Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: pavlin-g-poliˇcar-2025-2
    resource: "https://doi.org/10.1093/bioinformatics/btaf196"
    title: "Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan. (2025). Automated Assignment Grading with Large Language Models: Insights from a Bioinformatics Course. [doi:10.1093/bioinformatics/btaf196](https://doi.org/10.1093/bioinformatics/btaf196)"
    author: Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: pavlin-g-poliˇcar-2025-3
    resource: "https://doi.org/10.1093/bioinformatics/btaf196"
    title: "Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan. (2025). Automated Assignment Grading with Large Language Models: Insights from a Bioinformatics Course. [doi:10.1093/bioinformatics/btaf196](https://doi.org/10.1093/bioinformatics/btaf196)"
    author: Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Students showed no significant overall preference between LLM and TA feedback, preferred LLM feedback on correctly answered questions, and disliked only Nvidia-70B feedback on incorrect answers

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Overall, students exhibited no significant preferences for any grader, with slight preference for Llama-405Bq4. [→ Pavlin G. Poliˇcar 2025](#pavlin-g-policar-2025)
`q2 i?` Students seemed to prefer LLM-written feedback over TA feedback, particularly for correctly answered questions; on incorrect answers TA feedback achieved similar satisfaction. [→ Pavlin G. Poliˇcar 2025 (2)](#pavlin-g-policar-2025-2)
`q2 i?` For Nvidia-70B, students were around 15% more likely to respond negatively than when graded by a human TA. [→ Pavlin G. Poliˇcar 2025 (3)](#pavlin-g-policar-2025-3)

## Evidence

### Pavlin G. Poliˇcar 2025

Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan. (2025). Automated Assignment Grading with Large Language Models: Insights from a Bioinformatics Course. [doi:10.1093/bioinformatics/btaf196](https://doi.org/10.1093/bioinformatics/btaf196)

`q2 · i?` · `causal · r2`

Blind survey of 1,527 student satisfaction ratings, analyzed with a Bayesian mixed-effects ordered-probit regression with grader, exercise, and student factors: 'overall, students exhibit no significant preferences for any of the graders.'

> "With the exception of Llama-405Bq4, which students appear to prefer slightly, the results indicate that, overall, students exhibit no significant preferences for any of the graders."

### Pavlin G. Poliˇcar 2025 (2)

Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan. (2025). Automated Assignment Grading with Large Language Models: Insights from a Bioinformatics Course. [doi:10.1093/bioinformatics/btaf196](https://doi.org/10.1093/bioinformatics/btaf196)

`q2 · i?` · `causal · r2`

Correctness-split analysis using two sets of grader factors linked by a Gaussian hyperprior: 'students seem to prefer feedback written by LLMs over feedback written by human TAs,' especially on correctly answered questions; TA feedback matched LLM satisfaction on incorrect answers.

> "Interestingly, although the effect size is small, students seem to prefer feedback written by LLMs over feedback written by human TAs. This holds particularly true for feedback to correctly answered questions."

### Pavlin G. Poliˇcar 2025 (3)

Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan. (2025). Automated Assignment Grading with Large Language Models: Insights from a Bioinformatics Course. [doi:10.1093/bioinformatics/btaf196](https://doi.org/10.1093/bioinformatics/btaf196)

`q2 · i?` · `causal · r2`

Grader-specific analysis on incorrectly answered questions: for Nvidia-70B 'students were around 15% more likely to respond negatively than if they were graded by a human TA,' the exception the article reports among the LLMs.

> "One notable exception to this is Nvidia-70B, for which students were around 15% more likely to respond negatively than if they were graded by a human TA."

## Discussion


## Related Claims
- [In a real classroom, all six evaluated LLMs except Llama-8B graded student text answers with classification accuracy between 85% and 90% against TA gold-standard grades](llm-graders-match-ta-grading-accuracy.md) — related
- [Health care professionals rated GPT-4V's explanations nearly on par with expert explanations when answers were correct, but overwhelmingly preferred expert explanations when answers were incorrect](explanation-preference-correct-versus-incorrect.md) — related
- [Students found ChatGPT responses useful but insufficient in depth and detail compared with TA responses](students-find-chatgpt-useful-but-lacking-depth.md) — related
- [Students rated human TA responses more favorably overall but preferred ChatGPT responses 40% of the time](students-prefer-human-ta-responses-but-40-percent-prefer-chatgpt.md) — related
