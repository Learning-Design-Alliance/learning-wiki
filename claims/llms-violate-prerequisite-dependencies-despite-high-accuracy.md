---
type: claim
title: LLMs satisfy mathematical prerequisite dependencies far less often than human learners despite matching or exceeding human accuracy
description: LLMs satisfy mathematical prerequisite dependencies far less often than human learners despite matching or exceeding human accuracy
id: llms-violate-prerequisite-dependencies-despite-high-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: peng-cui-2026
    resource: "https://doi.org/10.18653/2026.findings-emnlp.494"
    title: "Peng Cui, Heejin Do, and Mrinmaya Sachan. (2026). Do LLMs Exhibit Coherent Knowledge Structures in Mathematical Reasoning? A Perspective from Knowledge Space Theory. arXiv. [doi:10.18653/2026.findings-emnlp.494](https://doi.org/10.18653/2026.findings-emnlp.494)"
    author: Peng Cui, Heejin Do, and Mrinmaya Sachan
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: peng-cui-2026-2
    resource: "https://doi.org/10.18653/2026.findings-emnlp.494"
    title: "Peng Cui, Heejin Do, and Mrinmaya Sachan. (2026). Do LLMs Exhibit Coherent Knowledge Structures in Mathematical Reasoning? A Perspective from Knowledge Space Theory. arXiv. [doi:10.18653/2026.findings-emnlp.494](https://doi.org/10.18653/2026.findings-emnlp.494)"
    author: Peng Cui, Heejin Do, and Mrinmaya Sachan
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# LLMs satisfy mathematical prerequisite dependencies far less often than human learners despite matching or exceeding human accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Human learners reach perfect prerequisite satisfaction (PSR = 1.0) on 72.7% of their correct answers, while the best LLM reaches only 48.16%. [→ Peng Cui 2026](#peng-cui-2026)
`q2 i?` On the verified subset, human learners achieve PSR = 1 on 81.6% of questions versus 55.7% for the best-performing LLM, and the human–LLM gap remains comparable when annotation errors are removed. [→ Peng Cui 2026 (2)](#peng-cui-2026-2)

## Evidence

### Peng Cui 2026

Peng Cui, Heejin Do, and Mrinmaya Sachan. (2026). Do LLMs Exhibit Coherent Knowledge Structures in Mathematical Reasoning? A Perspective from Knowledge Space Theory. arXiv. [doi:10.18653/2026.findings-emnlp.494](https://doi.org/10.18653/2026.findings-emnlp.494)

`q2 · i?` · `associational · r2`

Evaluation of eight LLMs and real student response records from the XES3G5M knowledge tracing dataset, scoring the Prerequisite Satisfaction Ratio of correctly answered questions. The article reports that human learners reach a "perfect PSR of 1.0" on 72.7% of questions and that the best model, QWEN3-80B-INSTRUCT, reaches only 48.16%.

> "For human learners, the vast majority of questions (72.7%) achieve a perfect PSR of 1.0, indicating that human correct answers are almost always grounded in mastery of the prerequisite knowledge."

### Peng Cui 2026 (2)

Peng Cui, Heejin Do, and Mrinmaya Sachan. (2026). Do LLMs Exhibit Coherent Knowledge Structures in Mathematical Reasoning? A Perspective from Knowledge Space Theory. arXiv. [doi:10.18653/2026.findings-emnlp.494](https://doi.org/10.18653/2026.findings-emnlp.494)

`q2 · i?` · `associational · r2`

Repetition of the PSR evaluation on XESverified, a 400-question manually verified subset that controls for LLM concept-annotation errors. The article notes the human–LLM gap stays comparable (25.9 vs. 24.54 percentage points), showing PSR is "robust to a moderate level of concept annotation error".

> "the proportion of questions with PSR = 1 shows the same overall pattern, with human learners at 81.6% against 55.7% for the best-performing LLM."

## Discussion


## Related Claims
- [Structural knowledge deficits in LLMs remain invisible to accuracy-based and LLM-as-judge reasoning evaluations](psr-invisible-to-accuracy-and-llm-judge-evaluation.md) — a broader claim this one bears on
- [Frontier LLMs achieve the best balance between detecting misconceptions in correct-answer cases and not over-flagging correct students, while fine-tuned local models achieve under 58% TM recall](frontier-llms-best-balance-tm-detection.md) — related
- [GPT-4's error-diagnosis accuracy varies by error type: near-perfect on correct answers, weakest on Wrong Field and multiple-error responses](gpt4-diagnosis-accuracy-varies-by-error-type.md) — related
