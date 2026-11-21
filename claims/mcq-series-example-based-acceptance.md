---
type: claim
title: "The example-based one-step model produced about half acceptable MCQs in series, with minor correction raising example-based acceptance by 15%"
description: "The example-based one-step model produced about half acceptable MCQs in series, with minor correction raising example-based acceptance by 15%"
id: mcq-series-example-based-acceptance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
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
    rigour: 2
---

# The example-based one-step model produced about half acceptable MCQs in series, with minor correction raising example-based acceptance by 15%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2`–`r3` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Both series-generation simulations (prototype as example vs. concept derived from prototype) produced 29 of 60 acceptable MCQs (48.33%). [→ Krushynska 2026](#krushynska-2026)
`q2 i?` After minor correction, example-based series acceptance rose to 63.33%, while concept-derived series rose only 3.33%. [→ Krushynska 2026 (2)](#krushynska-2026-2)

## Evidence

### Krushynska 2026

Krushynska, T., Ursin, J., & Heilala, V. (2026). AI-Assisted Model for Generating Multiple-Choice Questions. University of Jyväskylä. Originally published 2025. [doi:10.48550/arXiv.2602.08383](https://doi.org/10.48550/arXiv.2602.08383)

`q2 · i?` · `design · r3`

Simulation transforming six prototypes into series via two prompt variants across four AIs; Table 8 shows "29 from 60–48,33 %" acceptable under human evaluation for both variants.

> "Both simulations were repeated three times using MCQ-prototypes from three disciplines: immunology, microbiology and biochemistry; 9 quality criteria were applied. The model produced about a half of acceptable MCQs"

### Krushynska 2026 (2)

Krushynska, T., Ursin, J., & Heilala, V. (2026). AI-Assisted Model for Generating Multiple-Choice Questions. University of Jyväskylä. Originally published 2025. [doi:10.48550/arXiv.2602.08383](https://doi.org/10.48550/arXiv.2602.08383)

`q2 · i?` · `design · r2`

Post-hoc minor corrections raised example-based series acceptance to 63.33% but concept-derived series only to 51.66%, because concept-derived items "had more serious weaknesses."

> "After minor correction, the acceptance of example-based series rose by 15%. While MCQs, generated though deriving the concept, had more serious weaknesses. Among them, only two additional items (3,33%) could be fixed by minor correction."

## Discussion


## Related Claims
- [Distributing the three prompts among four AIs, each assigned the step it performed best, raised MCQ prototype acceptance further](distributing-prompts-among-ais-mcq.md) — related
- [A multi-step three-prompt model with human control between steps generated more acceptable MCQ prototypes than a single direct prompt](multi-step-prompt-model-mcq-prototypes.md) — related
- [In the one-step model, learning objectives as input yielded a higher proportion of acceptable MCQs than textbook fragments, but input type made no essential difference in the multi-step model](input-type-learning-objectives-vs-textbook.md) — related
