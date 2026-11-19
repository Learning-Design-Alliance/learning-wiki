---
type: claim
title: Davinci-003 API can generate questions of varying difficulty and evaluate student answers from instructions and context
description: Davinci-003 API can generate questions of varying difficulty and evaluate student answers from instructions and context
id: davinci-003-generates-graded-questions-and-evaluates-answers
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: devan-walton-2023
    resource: "https://doi.org/10.48550/arXiv.2304.02772"
    title: "Devan Walton. (2023). Personalized Cognitive Tutoring using Davinci-003 API for Adaptive Question Generation and Assessment. [doi:10.48550/arXiv.2304.02772](https://doi.org/10.48550/arXiv.2304.02772)"
    author: Devan Walton
    q: 1
    i: "?"
    kind: design
    rigour: 1
---

# Davinci-003 API can generate questions of varying difficulty and evaluate student answers from instructions and context

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r1` · `q1`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Davinci-003 API generates relevant questions with varying difficulty levels and can evaluate student responses with scores, feedback, and hints. [→ Devan Walton 2023](#devan-walton-2023)

## Evidence

### Devan Walton 2023

Devan Walton. (2023). Personalized Cognitive Tutoring using Davinci-003 API for Adaptive Question Generation and Assessment. [doi:10.48550/arXiv.2304.02772](https://doi.org/10.48550/arXiv.2304.02772)

`q1 · i?` · `design · r1`

Author demonstration in Section 2.1: worked examples of prompts and outputs for photosynthesis questions and answer evaluation, not a controlled study. The author notes the API can 'indicate the correct answer for each question using an asterisk (*).'

> "Davinci-003 API can generate questions that are relevant to the text and have varying levels of difficulty. It can also indicate the correct answer for each question using an asterisk (*)."

## Discussion


## Related Claims
- [Davinci-003 API can generate transfer questions relating a topic to a new domain](davinci-003-transfer-question-generation.md) — related
- [Switching from reference-based to contextual evaluation prompts improved GenAI grading accuracy](contextual-evaluation-prompt-improvement.md) — related
- [Hint-based prompts raise ChatGPT scoring agreement with human experts to 98–100%, while no-hint prompts are unstable (Q2 precision 0.42)](hint-prompts-raise-llm-scoring-agreement.md) — related
- [Prebuilt quiz banks of 435 questions across 65 modules decouple practice from live generation, with warm practice-request medians of 4.8 and 5.8 ms](prebuilt-quiz-banks-decouple-practice.md) — related
- [GPT-4 generates targeted corrective feedback for 66% of student errors, but 35% of hints are too general, incorrect, or give away the answer](gpt4-feedback-66-percent-targeted-35-percent-flawed.md) — related
