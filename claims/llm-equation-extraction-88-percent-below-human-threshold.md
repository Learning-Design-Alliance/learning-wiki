---
type: claim
title: "Frontier open-source LLMs translated complex typed student physics responses at about 88% accuracy, 8.5% below the 96.5% human-grader agreement threshold"
description: "Frontier open-source LLMs translated complex typed student physics responses at about 88% accuracy, 8.5% below the 96.5% human-grader agreement threshold"
id: llm-equation-extraction-88-percent-below-human-threshold
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
---

# Frontier open-source LLMs translated complex typed student physics responses at about 88% accuracy, 8.5% below the 96.5% human-grader agreement threshold

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The best model-and-technique combination reached 88% accuracy on equation extraction, which is 8.5% below the 96.5% ceiling implied by marker agreement on ambiguous responses. [→ Lachlan McGinness and Peter Baumgartner 2025](#lachlan-mcginness-and-peter-baumgartner-2025)

## Evidence

### Lachlan McGinness and Peter Baumgartner 2025

Lachlan McGinness and Peter Baumgartner. (2025). Can Large Language Models Correctly Interpret Equations with Errors?. [doi:10.1103/v8f8-s11v](https://doi.org/10.1103/v8f8-s11v)

`q2 · i?` · `design · r2`

Evaluation of open-source LLM equation extraction from a sample of 200 typed responses to a 2023 Australian Physics Olympiad question, scored by Z3-verified equivalence with the marking team's equation lists. The paper reports that "the highest accuracy score achieved by any model and condition was 88%", below the 96.5% threshold.

> "Figure 2 shows that the highest accuracy score achieved by any model and condition was 88%. This is 8 .5% below the desired threshold of 96.5% where the markers find the responses unambiguous."

## Discussion


## Related Claims
- [Even the best LLM grader reaches only moderate agreement with human teachers, below the threshold for good reliability](llm-grading-moderate-human-agreement-icc.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](llm-grading-mixed-against-human-raters.md) — related
- [Sentence embedding models reach only moderate agreement and need human supervision for open-ended grading](embedding-models-moderate-agreement-need-supervision.md) — related
- [Full-scale LLM versions consistently achieve higher agreement with human grades than their mini and nano counterparts](full-scale-llms-outperform-mini-nano-grading.md) — related
