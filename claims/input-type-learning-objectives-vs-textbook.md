---
type: claim
title: In the one-step model, learning objectives as input yielded a higher proportion of acceptable MCQs than textbook fragments, but input type made no essential difference in the multi-step model
description: In the one-step model, learning objectives as input yielded a higher proportion of acceptable MCQs than textbook fragments, but input type made no essential difference in the multi-step model
id: input-type-learning-objectives-vs-textbook
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: krushynska-2026
    resource: "https://doi.org/10.48550/arXiv.2602.08383"
    title: "Krushynska, T., Ursin, J., & Heilala, V. (2026). AI-Assisted Model for Generating Multiple-Choice Questions. University of Jyväskylä. Originally published 2025. [doi:10.48550/arXiv.2602.08383](https://doi.org/10.48550/arXiv.2602.08383)"
    author: "Krushynska, T., Ursin, J., & Heilala, V."
    q: 2
    i: "?"
    kind: design
    rigour: 3
  - id: krushynska-2026-2
    resource: "https://doi.org/10.48550/arXiv.2602.08383"
    title: "Krushynska, T., Ursin, J., & Heilala, V. (2026). AI-Assisted Model for Generating Multiple-Choice Questions. University of Jyväskylä. Originally published 2025. [doi:10.48550/arXiv.2602.08383](https://doi.org/10.48550/arXiv.2602.08383)"
    author: "Krushynska, T., Ursin, J., & Heilala, V."
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# In the one-step model, learning objectives as input yielded a higher proportion of acceptable MCQs than textbook fragments, but input type made no essential difference in the multi-step model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r3` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` With the direct prompt, learning objectives yielded 47.91% acceptable MCQs versus 27.08% for textbook fragments. [→ Krushynska 2026](#krushynska-2026)
`q2 i?` In the multi-step model there was no essential difference between the two input types. [→ Krushynska 2026 (2)](#krushynska-2026-2)

## Evidence

### Krushynska 2026

Krushynska, T., Ursin, J., & Heilala, V. (2026). AI-Assisted Model for Generating Multiple-Choice Questions. University of Jyväskylä. Originally published 2025. [doi:10.48550/arXiv.2602.08383](https://doi.org/10.48550/arXiv.2602.08383)

`q2 · i?` · `design · r3`

One-step simulation across four AIs (Table 3): learning-objectives input outperformed textbook fragments, "47.91% vs. 27.08%" acceptable items.

> "In this model, formulating learning objectives yielded a higher proportion of acceptable MCQs than uploading textbook fragments (47.91% vs. 27.08%)."

### Krushynska 2026 (2)

Krushynska, T., Ursin, J., & Heilala, V. (2026). AI-Assisted Model for Generating Multiple-Choice Questions. University of Jyväskylä. Originally published 2025. [doi:10.48550/arXiv.2602.08383](https://doi.org/10.48550/arXiv.2602.08383)

`q2 · i?` · `design · r3`

Multi-step simulation (Table 5) found "no essential difference" between input types; the discussion cautions the one-step input advantage rested on a single example and is unlikely to generalize.

> "There was no essential difference between using textbook fragments or learning objectives in the initial prompt. Both types of input were revealed as applicable."

## Discussion


## Related Claims
- [Distributing the three prompts among four AIs, each assigned the step it performed best, raised MCQ prototype acceptance further](distributing-prompts-among-ais-mcq.md) — related
- [A multi-step three-prompt model with human control between steps generated more acceptable MCQ prototypes than a single direct prompt](multi-step-prompt-model-mcq-prototypes.md) — related
- [The example-based one-step model produced about half acceptable MCQs in series, with minor correction raising example-based acceptance by 15%](mcq-series-example-based-acceptance.md) — related
