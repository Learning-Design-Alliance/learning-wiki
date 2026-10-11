---
type: claim
title: A construction-focused correctness rubric underperformed behavior-focused and undefined prompts for LLM scoring of code explanations
description: A construction-focused correctness rubric underperformed behavior-focused and undefined prompts for LLM scoring of code explanations
id: construction-rubric-underperformed-llm-scoring
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: arun-balajiee-lekshmi-narayanan-2026
    resource: "https://arxiv.org/abs/2605.21614"
    title: "Arun-Balajiee Lekshmi-Narayanan, Mohammad Hassany, Peter Brusilovsky. (2026). Exploring the Effectiveness of Using LLMs for Automated Assessment of Student Self–Explanations in Programming Education. https://arxiv.org/abs/2605.21614"
    author: Arun-Balajiee Lekshmi-Narayanan, Mohammad Hassany, Peter Brusilovsky
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A construction-focused correctness rubric underperformed behavior-focused and undefined prompts for LLM scoring of code explanations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The LLM-Constr. prompt variant scored F1 = 0.89 and accuracy = 0.8, lower than the behavior-focused and no-definition variants, possibly because dataset explanations described syntax and code behavior rather than the line's role in the program. [→ Arun-Balajiee Lekshmi-Narayanan 2026](#arun-balajiee-lekshmi-narayanan-2026)

## Evidence

### Arun-Balajiee Lekshmi-Narayanan 2026

Arun-Balajiee Lekshmi-Narayanan, Mohammad Hassany, Peter Brusilovsky. (2026). Exploring the Effectiveness of Using LLMs for Automated Assessment of Student Self–Explanations in Programming Education. https://arxiv.org/abs/2605.21614

`q2 · i?` · `design · r2`

Result from the same 5-fold cross-validation comparison on the balanced dataset. The authors offer the explanation as an interpretation, suggesting prompts must balance rubrics between instructors' expectations and students' understanding of a correct explanation.

> "The LLM-Constr. potentially underperformed (for both datasets – F1 =0.89, Acc = 0.8) because the student explanations in the dataset described the "syntax and code behavior" and missed out the context of the code within the rest of the program"

## Discussion


## Related Claims
- [Growth is compartmentalized by question: on the code-tracing prompt students grew in procedural code tracing while physics correctness improved only slightly](compartmentalized-ct-growth-by-question.md) — related
- [Model performance is robust to minor prompt wording changes but sensitive to holistic rubric redesign](rubric-structure-part-of-assessment-construct.md) — related
- [Removing detailed rubric explanations from prompts improved grading accuracy across all approaches in an ablation study](simplified-prompts-outperform-detailed-rubrics.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
- [Zero-shot prompt type has minimal impact on LLM-human coding concordance](prompt-type-minimal-impact-llm-coding.md) — related
- [LLM-based automated assessment of student code self-explanations outperforms semantic similarity methods on a balanced classification task](llm-assessment-outperforms-semantic-similarity-code-explanations.md) — related
