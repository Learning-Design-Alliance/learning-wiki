---
type: claim
title: In a preliminary test, the system generated shared-scenario MCQ sets that preserved the shared-scenario structure of the QMCA
description: In a preliminary test, the system generated shared-scenario MCQ sets that preserved the shared-scenario structure of the QMCA
id: llm-shared-scenario-mcq-generation-preliminary
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: xian-wu-and-lindim-ismaili-2026
    resource: "https://doi.org/10.48550/arXiv.2607.13190"
    title: "Xian Wu and Lindim Ismaili. (2026). Reliable isomorphic physics problem generation with large language models. [doi:10.48550/arXiv.2607.13190](https://doi.org/10.48550/arXiv.2607.13190)"
    author: Xian Wu and Lindim Ismaili
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# In a preliminary test, the system generated shared-scenario MCQ sets that preserved the shared-scenario structure of the QMCA

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q1 i?` A preliminary, non-rigorous test using the Quantum Mechanics Concept Assessment found that generated questions preserved the shared-scenario structure. [→ Xian Wu and Lindim Ismaili 2026](#xian-wu-and-lindim-ismaili-2026)

## Evidence

### Xian Wu and Lindim Ismaili 2026

Xian Wu and Lindim Ismaili. (2026). Reliable isomorphic physics problem generation with large language models. [doi:10.48550/arXiv.2607.13190](https://doi.org/10.48550/arXiv.2607.13190)

`q1 · i?` · `design · r2`

Preliminary, unevaluated function test described in the work-in-progress section: the system recognized and regenerated MCQs grouped around a shared scenario using the QMCA. The article reports only that "the generated questions preserved the same structure", with no rubric evaluation.

> "We tested this function using the Quantum Mechanics Concept Assessment (QMCA) [17], which includes several instances of multiple questions based on a shared scenario. In this preliminary test, the generated questions preserved the same structure."

## Discussion


## Related Claims
- [The system did not consistently preserve distractor logic in generated MCQs, with only 59% preserving the logical structure of distractors overall and 47% for abstract-context numerical questions](llm-mcq-distractor-logic-preservation-weak.md) — related
- [The system failed to vary scenarios for abstract-context questions, using a different scenario in only 5% of such cases](llm-abstract-context-scenario-variation-fails.md) — related
- [89% of LLM-generated isomorphic MCQs were rated fully specified and solvable as written, usable without expert revision](llm-isomorphic-mcq-89-percent-directly-usable.md) — related
