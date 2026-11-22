---
type: claim
title: "The system failed to vary scenarios for abstract-context questions, using a different scenario in only 5% of such cases"
description: "The system failed to vary scenarios for abstract-context questions, using a different scenario in only 5% of such cases"
id: llm-abstract-context-scenario-variation-fails
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

# The system failed to vary scenarios for abstract-context questions, using a different scenario in only 5% of such cases

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For questions with abstract contexts, the system generated a different scenario in only 5% of cases, largely randomizing numerical values instead. [→ Xian Wu and Lindim Ismaili 2026](#xian-wu-and-lindim-ismaili-2026)

## Evidence

### Xian Wu and Lindim Ismaili 2026

Xian Wu and Lindim Ismaili. (2026). Reliable isomorphic physics problem generation with large language models. [doi:10.48550/arXiv.2607.13190](https://doi.org/10.48550/arXiv.2607.13190)

`q2 · i?` · `design · r2`

Rubric evaluation of generated questions by context type; TABLE I reports 5% for scenario difference on abstract-context questions versus 99% conceptual and 97% numerical-with-context. The article says the system "did not perform well in changing the scenario for questions with abstract contexts".

> "In addition, the system did not perform well in changing the scenario for questions with abstract contexts."

## Discussion


## Related Claims
- [The system did not consistently preserve distractor logic in generated MCQs, with only 59% preserving the logical structure of distractors overall and 47% for abstract-context numerical questions](llm-mcq-distractor-logic-preservation-weak.md) — related
- [In a preliminary test, LLM generation of context-rich problems with changed thematic focus was unsatisfactory, replacing surface cover stories rather than redesigning scenarios](llm-context-rich-problem-generation-unsatisfactory.md) — related
- [Prompt-chaining produces higher quality and more consistent isomorphic physics problems than single-prompt or simple-prompt generation](prompt-chaining-outperforms-single-prompt-isomorphic-generation.md) — related
- [In a preliminary test, the system generated shared-scenario MCQ sets that preserved the shared-scenario structure of the QMCA](llm-shared-scenario-mcq-generation-preliminary.md) — related
