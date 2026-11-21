---
type: claim
title: Student references to a nonexistent attachment increased the chance that LLMs of all sizes hallucinated equations, the most common error type for large models
description: Student references to a nonexistent attachment increased the chance that LLMs of all sizes hallucinated equations, the most common error type for large models
id: fictitious-attachment-references-trigger-llm-hallucinated-equations
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: lachlan-mcginness-and-peter-baumgartner-2025
    resource: "https://doi.org/10.1103/v8f8-s11v"
    title: "Lachlan McGinness and Peter Baumgartner. (2025). Can Large Language Models Correctly Interpret Equations with Errors?. [doi:10.1103/v8f8-s11v](https://doi.org/10.1103/v8f8-s11v)"
    author: Lachlan McGinness and Peter Baumgartner
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: lachlan-mcginness-and-peter-baumgartner-2025-2
    resource: "https://doi.org/10.1103/v8f8-s11v"
    title: "Lachlan McGinness and Peter Baumgartner. (2025). Can Large Language Models Correctly Interpret Equations with Errors?. [doi:10.1103/v8f8-s11v](https://doi.org/10.1103/v8f8-s11v)"
    author: Lachlan McGinness and Peter Baumgartner
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Student references to a nonexistent attachment increased the chance that LLMs of all sizes hallucinated equations, the most common error type for large models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` References to an attachment the model was never shown increased hallucinated equations across all model sizes, and this was the most common error type for large models. [→ Lachlan McGinness and Peter Baumgartner 2025](#lachlan-mcginness-and-peter-baumgartner-2025)
`q2 i?` For 400B+ consensus models, fictitious attachment or false reference accounted for 9 of 24 total errors, exceeding every other category. [→ Lachlan McGinness and Peter Baumgartner 2025 (2)](#lachlan-mcginness-and-peter-baumgartner-2025-2)

## Evidence

### Lachlan McGinness and Peter Baumgartner 2025

Lachlan McGinness and Peter Baumgartner. (2025). Can Large Language Models Correctly Interpret Equations with Errors?. [doi:10.1103/v8f8-s11v](https://doi.org/10.1103/v8f8-s11v)

`q2 · i?` · `design · r2`

Error-category analysis of translations of the 200 typed responses found that LLMs hallucinate equations when students reference an attachment, even though no attachment was shown to the model. The paper reports that "students made reference to an attachment" increased hallucination for all model sizes.

> "Interestingly we found that if students made reference to an attachment that this increased the chance that LLMs of all sizes would hallucinate equations. This was the most common type of error for large models."

### Lachlan McGinness and Peter Baumgartner 2025 (2)

Lachlan McGinness and Peter Baumgartner. (2025). Can Large Language Models Correctly Interpret Equations with Errors?. [doi:10.1103/v8f8-s11v](https://doi.org/10.1103/v8f8-s11v)

`q2 · i?` · `design · r2`

Manual classification of the twenty-four errors in the consensus responses of Deepseek 671B and Llama 405B (Table II) found fictitious attachment / false reference the most frequent category. The paper reports these models "most commonly made errors when students made reference to an attachment that did not exist".

> "These models most commonly made errors when students made reference to an attachment that did not exist. In these cases the model would hallucinate equations."

## Discussion


## Related Claims
- [Smaller LLMs more often used undefined symbols, missed equations, and hallucinated equations; a 14B parameter model (Phi4) achieved only about 70% accuracy on the task](small-llms-undefined-symbols-phi4-70-percent.md) — related
- [Qualitative error analysis yields five recurring error types, with over-inference most prevalent (33.5%), followed by evidence misidentification (23.4%) and hallucination (19.8%)](five-error-types-llm-diagnosis-vague-evidence.md) — related
- [Zero-shot LLM errors follow four recurring patterns: over-interpretation, failure to detect relevant information, hallucination, and failure to generate a response](llm-competency-error-patterns-four-types.md) — related
