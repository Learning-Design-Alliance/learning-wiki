---
type: claim
title: A multi-step three-prompt model with human control between steps generated more acceptable MCQ prototypes than a single direct prompt
description: A multi-step three-prompt model with human control between steps generated more acceptable MCQ prototypes than a single direct prompt
id: multi-step-prompt-model-mcq-prototypes
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
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

# A multi-step three-prompt model with human control between steps generated more acceptable MCQ prototypes than a single direct prompt

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2`–`r3` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Under simulation conditions, the multi-step model produced 46 acceptable MCQs out of 96 (47.91%), compared with 36 of 96 (37.5%) for the one-step direct-prompt model. [→ Krushynska 2026](#krushynska-2026)
`q2 i?` The transition from one-step to multi-step model increased acceptable MCQs by more than 10%. [→ Krushynska 2026 (2)](#krushynska-2026-2)

## Evidence

### Krushynska 2026

Krushynska, T., Ursin, J., & Heilala, V. (2026). AI-Assisted Model for Generating Multiple-Choice Questions. University of Jyväskylä. Originally published 2025. [doi:10.48550/arXiv.2602.08383](https://doi.org/10.48550/arXiv.2602.08383)

`q2 · i?` · `design · r3`

Simulation of the preliminary one-step direct prompt across four AIs and multiple input conditions produced 96 items, of which "36 items (37.5%) were of sufficient quality" per Table 3.

> "In 16 cycles of simulation, performed with direct prompt to generate one and then five MCQs, a total of 96 test items were produced. Of these, 36 items (37.5%) were of sufficient quality"

### Krushynska 2026 (2)

Krushynska, T., Ursin, J., & Heilala, V. (2026). AI-Assisted Model for Generating Multiple-Choice Questions. University of Jyväskylä. Originally published 2025. [doi:10.48550/arXiv.2602.08383](https://doi.org/10.48550/arXiv.2602.08383)

`q2 · i?` · `design · r2`

Simulation of the three-prompt model under the same conditions yielded "Forty-six MCQs (47,91%) from 96 generated ones were acceptable" (Table 5). The discussion reports the transition "resulted in more than 10% increase in the number of acceptable MCQs."

> "The model incorporating a sequence of three prompts (see Fig. 1) with integrated quality criteria was applied under the same simulation conditions as the preliminary model and appeared to be more effective (Tab.5). Forty-six MCQs (47,91%) from 96 generated ones were acceptable."

## Discussion


## Related Claims
- [Distributing the three prompts among four AIs, each assigned the step it performed best, raised MCQ prototype acceptance further](distributing-prompts-among-ais-mcq.md) — related
- [In the one-step model, learning objectives as input yielded a higher proportion of acceptable MCQs than textbook fragments, but input type made no essential difference in the multi-step model](input-type-learning-objectives-vs-textbook.md) — related
- [The example-based one-step model produced about half acceptable MCQs in series, with minor correction raising example-based acceptance by 15%](mcq-series-example-based-acceptance.md) — related
- [Generative AI, when used under precise conditions, reduces the cost and time of producing high-quality MCQs without compromising quality](genai-reduces-mcq-cost-and-time.md) — a broader claim this one bears on
