---
type: claim
title: Model performance is robust to minor prompt wording changes but sensitive to holistic rubric redesign
description: Model performance is robust to minor prompt wording changes but sensitive to holistic rubric redesign
id: rubric-structure-part-of-assessment-construct
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: moiz-imran-2026
    resource: "https://orcid.org/0000-0002-5878-2143"
    title: "Moiz Imran, Sahan Bulathwela. (2026). The Correct Answer Trap: Pedagogically-Grounded Detection and Feedback for Hidden Misconceptions. PEAF 2026: Workshop on Pedagogical Evaluation of Automated Feedback. https://orcid.org/0000-0002-5878-2143"
    author: Moiz Imran, Sahan Bulathwela
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Model performance is robust to minor prompt wording changes but sensitive to holistic rubric redesign

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Across three prompt variants on the same model and test set, balanced accuracy differed by only 1 percentage point for minor wording changes but dropped 27pp under holistic rubric redesign. [→ Moiz Imran 2026](#moiz-imran-2026)

## Evidence

### Moiz Imran 2026

Moiz Imran, Sahan Bulathwela. (2026). The Correct Answer Trap: Pedagogically-Grounded Detection and Feedback for Hidden Misconceptions. PEAF 2026: Workshop on Pedagogical Evaluation of Automated Feedback. https://orcid.org/0000-0002-5878-2143

`q2 · i?` · `causal · r2`

Prompt-variant experiment in the Method section on the same model and test set. The paper reports a "1 percentage point (pp) balanced accuracy difference" for wording changes versus a "27pp drop" for rubric redesign.

> "Testing three prompt variants on the same model and test set, we find performance robust to minor wording changes (1 percentage point (pp) balanced accuracy difference) but sensitive to holistic rubric redesign (27pp drop)."

## Discussion


## Related Claims
- [Removing detailed rubric explanations from prompts improved grading accuracy across all approaches in an ablation study](simplified-prompts-outperform-detailed-rubrics.md) — related
- [Rubric-enhanced prompting (Variant 2) raises LLM assigned scores relative to the no-rubric baseline, with model-specific gaps at particular taxonomy levels](rubric-prompting-raises-llm-assigned-scores.md) — related
