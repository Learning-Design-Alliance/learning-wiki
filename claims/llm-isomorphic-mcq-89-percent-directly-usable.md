---
type: claim
title: "89% of LLM-generated isomorphic MCQs were rated fully specified and solvable as written, usable without expert revision"
description: "89% of LLM-generated isomorphic MCQs were rated fully specified and solvable as written, usable without expert revision"
id: llm-isomorphic-mcq-89-percent-directly-usable
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: xian-wu-and-lindim-ismaili-2026
    resource: "https://doi.org/10.48550/arXiv.2607.13190"
    title: "Xian Wu and Lindim Ismaili. (2026). Reliable isomorphic physics problem generation with large language models. [doi:10.48550/arXiv.2607.13190](https://doi.org/10.48550/arXiv.2607.13190)"
    author: Xian Wu and Lindim Ismaili
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# 89% of LLM-generated isomorphic MCQs were rated fully specified and solvable as written, usable without expert revision

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In an evaluation of 247 generated questions from 19 trials, 89% of LLM-generated isomorphic MCQs were fully specified and solvable as written. [→ Xian Wu and Lindim Ismaili 2026](#xian-wu-and-lindim-ismaili-2026)

## Evidence

### Xian Wu and Lindim Ismaili 2026

Xian Wu and Lindim Ismaili. (2026). Reliable isomorphic physics problem generation with large language models. [doi:10.48550/arXiv.2607.13190](https://doi.org/10.48550/arXiv.2607.13190)

`q2 · i?` · `design · r2`

Rubric-based evaluation of the system's output: 13 source MCQs were run through the website in 20 trials, of which 19 succeeded, producing 247 questions rated independently by two authors. The article reports "89% of the generated questions were fully specified and solvable as written".

> "Based on the evaluation results, 89% of the generated questions were fully specified and solvable as written, suggesting that most of the LLM-generated questions can be used directly as instructional content without expert revision."

## Discussion


## Related Claims
- [The system did not consistently preserve distractor logic in generated MCQs, with only 59% preserving the logical structure of distractors overall and 47% for abstract-context numerical questions](llm-mcq-distractor-logic-preservation-weak.md) — related
- [AI-generated assessment items frequently need faculty correction, supporting AI as a draft generator within quality assurance](genai-assessment-items-draft-generator-quality-assurance.md) — related
- [Blind expert assessment of GPT-4-generated MCQs found the majority valid as exam questions, with problematic-question rates varying by field](gpt4-blind-assessment-majority-valid.md) — a broader claim this one bears on
- [Most LLM-generated MCQs from video transcripts met established quality criteria, with 84.05% rated clear, 86.38% containing plausible distractors, and 93.39% directly answerable](llm-mcq-video-quality-ratings-majority-clear.md) — related
- [ChatGPT generated usable MCQs roughly five times faster than educator panels but with a 44% rejection rate](chatgpt-mcq-generation-speed-rejection-tradeoff.md) — related
- [In the one human-vs-LLM comparison, human-written MCQs outperformed ChatGPT-generated MCQs in quality and validity, while AI was far faster](humans-outperform-chatgpt-mcq-quality.md) — related
- [Most reviewed studies (5 of 8) demonstrated that LLMs can produce MCQs valid for medical exams](llm-mcq-generation-majority-valid.md) — a broader claim this one bears on
- [Claude 3.5 Sonnet achieved the highest overall performance (86.28%), accuracy (85.57%), and clarity (91.73%) in generating USMLE-style medical ethics MCQs](claude-35-sonnet-highest-ethics-mcq-performance.md) — related
- [In a preliminary test, the system generated shared-scenario MCQ sets that preserved the shared-scenario structure of the QMCA](llm-shared-scenario-mcq-generation-preliminary.md) — related
