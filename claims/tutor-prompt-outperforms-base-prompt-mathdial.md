---
type: claim
title: "A pedagogically informed Tutor Prompt yields higher Success@N and lower Telling@N than MathDial's Base Prompt in simulated tutor-student dialogues"
description: "A pedagogically informed Tutor Prompt yields higher Success@N and lower Telling@N than MathDial's Base Prompt in simulated tutor-student dialogues"
id: tutor-prompt-outperforms-base-prompt-mathdial
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: jarosław-a-chudziak-and-adam-kostka-2025
    resource: "https://arxiv.org/abs/2507.12484"
    title: "Jarosław A. Chudziak and Adam Kostka. (2025). AI-Powered Math Tutoring: Platform for Personalized and Adaptive Education. arXiv preprint. https://arxiv.org/abs/2507.12484"
    author: Jarosław A. Chudziak and Adam Kostka
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A pedagogically informed Tutor Prompt yields higher Success@N and lower Telling@N than MathDial's Base Prompt in simulated tutor-student dialogues

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In simulated MathDial dialogues, the Tutor Prompt significantly outperformed the Base Prompt for each model, achieving superior Success@N and far lower Telling@N rates over interaction lengths (K). [→ Jarosław A. Chudziak and Adam Kostka 2025](#jarosaw-a-chudziak-and-adam-kostka-2025)

## Evidence

### Jarosław A. Chudziak and Adam Kostka 2025

Jarosław A. Chudziak and Adam Kostka. (2025). AI-Powered Math Tutoring: Platform for Personalized and Adaptive Education. arXiv preprint. https://arxiv.org/abs/2507.12484

`q2 · i?` · `design · r2`

Benchmark evaluation on the MathDial dataset simulating tutor-student interaction without external tools, comparing GPT-4o and GPT-4o-mini under the Tutor Prompt versus the Base Prompt. The article reports the Tutor Prompt "significantly outperformed the 'Base Prompt' for each model"; no effect size is printed.

> "Results (shown in Figure 4) displayed that the 'Tutor Prompt' significantly outperformed the 'Base Prompt' for each model, achieving superior Success@N and far lower Telling@N rates over interaction lengths (K)."

## Discussion


## Related Claims
- [Existing KT methods fail to beat a majority-class baseline on the small CoMTA dialogue dataset but perform significantly better on the larger MathDial dataset.](existing-kt-methods-fail-on-small-comta-but-improve-with-more-data-on-mathdial.md) — related
- [Knowledge tracing performance on tutoring dialogues is relatively low, with a maximum of around 76% AUC, which the authors take to show dialogueKT is a challenging task.](dialogue-kt-performance-is-relatively-low-compared-to-standard-kt.md) — related
