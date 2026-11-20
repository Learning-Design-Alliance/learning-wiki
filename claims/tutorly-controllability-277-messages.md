---
type: claim
title: "Expert evaluators assessed Tutorly's prompt-pipeline controllability by annotating 277 dialogue messages against a hierarchical intent label scheme across three video topics"
description: "Expert evaluators assessed Tutorly's prompt-pipeline controllability by annotating 277 dialogue messages against a hierarchical intent label scheme across three video topics"
id: tutorly-controllability-277-messages
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: wengxi-li-2024
    resource: "https://doi.org/10.48550/arXiv.2405.12946"
    title: "Wengxi Li, Roy Pea, Nick Haber, and Hari Subramonyam. (2024). Tutorly: Turning Programming Videos Into Apprenticeship Learning Environments with LLMs. [doi:10.48550/arXiv.2405.12946](https://doi.org/10.48550/arXiv.2405.12946)"
    author: Wengxi Li, Roy Pea, Nick Haber, and Hari Subramonyam
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Expert evaluators assessed Tutorly's prompt-pipeline controllability by annotating 277 dialogue messages against a hierarchical intent label scheme across three video topics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Three expert evaluators independently labeled 277 instructor dialogue messages across exploratory data analysis, machine learning, and game development videos, and the labels were compared to ground truth from the DSL files using precision, recall, and F1-score. [→ Wengxi Li 2024](#wengxi-li-2024)

## Evidence

### Wengxi Li 2024

Wengxi Li, Roy Pea, Nick Haber, and Hari Subramonyam. (2024). Tutorly: Turning Programming Videos Into Apprenticeship Learning Environments with LLMs. [doi:10.48550/arXiv.2405.12946](https://doi.org/10.48550/arXiv.2405.12946)

`q2 · i?` · `design · r2`

Controllability evaluation in which three expert evaluators labeled messages for three topics (EDA 124 utterances, ML 89, game development 64) against a hierarchical scheme of knowledge, method, interaction, and intent, compared with ground truth extracted from the DSL files using "the precision, recall, and F1-score metrics".

> "Using this method, the evaluators annotated a total of 277 dialogue messages from the instructor."

## Discussion


## Related Claims
- [The emergent LLM coding pipeline reaches substantial agreement with expert human coding (Cohen's κ = 0.78, raw agreement 84%) on a stratified 10% sample](llm-discourse-coding-kappa-078-expert-agreement.md) — related
- [Adding regex-based rules to few-shot LLM labeling improves agreement with human annotation (0.818 to 0.852 overall)](regex-rules-improve-fewshot-llm-labeling-accuracy.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [In a within-subject study, Tutorly improved post-test performance from 61.9% to 76.6% for learners studying exploratory data analysis from a streamcast](tutorly-within-subject-post-test-gain.md) — related
