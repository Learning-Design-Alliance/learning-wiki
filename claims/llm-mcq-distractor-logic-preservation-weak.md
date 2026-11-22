---
type: claim
title: "The system did not consistently preserve distractor logic in generated MCQs, with only 59% preserving the logical structure of distractors overall and 47% for abstract-context numerical questions"
description: "The system did not consistently preserve distractor logic in generated MCQs, with only 59% preserving the logical structure of distractors overall and 47% for abstract-context numerical questions"
id: llm-mcq-distractor-logic-preservation-weak
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

# The system did not consistently preserve distractor logic in generated MCQs, with only 59% preserving the logical structure of distractors overall and 47% for abstract-context numerical questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Only 59% of generated MCQs preserved the logical structure of the distractors, and the authors name this as a major limitation. [→ Xian Wu and Lindim Ismaili 2026](#xian-wu-and-lindim-ismaili-2026)

## Evidence

### Xian Wu and Lindim Ismaili 2026

Xian Wu and Lindim Ismaili. (2026). Reliable isomorphic physics problem generation with large language models. [doi:10.48550/arXiv.2607.13190](https://doi.org/10.48550/arXiv.2607.13190)

`q2 · i?` · `design · r2`

Authors' evaluation of the 247 generated questions using the eight-item rubric; TABLE I reports 59% overall for distractor-logic preservation, 68% conceptual, 67% abstract context, 47% numerical. The article states the system "did not consistently preserve distractor logic".

> "One major limitation of the system is that it did not consistently preserve distractor logic."

## Discussion


## Related Claims
- [The system failed to vary scenarios for abstract-context questions, using a different scenario in only 5% of such cases](llm-abstract-context-scenario-variation-fails.md) — related
- [89% of LLM-generated isomorphic MCQs were rated fully specified and solvable as written, usable without expert revision](llm-isomorphic-mcq-89-percent-directly-usable.md) — related
- [Chain-of-thought and reasoning prompting significantly improve LLM proportional match with human-authored distractors over direct prompting on both math and science MCQs](reasoning-prompting-improves-llm-distractor-match.md) — related
- [Most LLM-generated MCQs from video transcripts met established quality criteria, with 84.05% rated clear, 86.38% containing plausible distractors, and 93.39% directly answerable](llm-mcq-video-quality-ratings-majority-clear.md) — related
- [LLMs' generation probabilities for multiple-choice distractors correlate moderately with how often students choose them](llm-distractor-likelihood-moderately-tracks-student-choices.md) — related
- [In a preliminary test, the system generated shared-scenario MCQ sets that preserved the shared-scenario structure of the QMCA](llm-shared-scenario-mcq-generation-preliminary.md) — related
