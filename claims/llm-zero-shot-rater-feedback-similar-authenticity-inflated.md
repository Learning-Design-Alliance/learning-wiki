---
type: claim
title: LLM-generated feedback quality ratings are similar to human ratings, whereas LLM authenticity ratings are higher and presumably inaccurate
description: LLM-generated feedback quality ratings are similar to human ratings, whereas LLM authenticity ratings are higher and presumably inaccurate
id: llm-zero-shot-rater-feedback-similar-authenticity-inflated
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: coristine-a-2025
    resource: "https://doi.org/10.2196/68486"
    title: "Coristine A, Li D, Foroutan DB, Ojo TF, Menon NP, Aditya I, Cook DA, Overgaard J, Pankratz VS, Del Fiol G, Aakre CA. (2025). Virtual Patients Using Large Language Models: Scalable, Contextualized Simulation of Clinician-Patient Dialogue With Feedback. Journal of Medical Internet Research. https://doi.org/10.2196/68486"
    author: Coristine A, Li D, Foroutan DB, Ojo TF, Menon NP, Aditya I, Cook DA, Overgaard J, Pankratz VS, Del Fiol G, Aakre CA
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM-generated feedback quality ratings are similar to human ratings, whereas LLM authenticity ratings are higher and presumably inaccurate

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In paired analyses, feedback ratings differed by only 0.10 points between human and GPT raters, while authenticity ratings were significantly lower for human-generated ratings (−0.98 humanlike; −0.52 overall). [→ Coristine A 2025](#coristine-a-2025)

## Evidence

### Coristine A 2025

Coristine A, Li D, Foroutan DB, Ojo TF, Menon NP, Aditya I, Cook DA, Overgaard J, Pankratz VS, Del Fiol G, Aakre CA. (2025). Virtual Patients Using Large Language Models: Scalable, Contextualized Simulation of Clinician-Patient Dialogue With Feedback. Journal of Medical Internet Research. https://doi.org/10.2196/68486

`q2 · i?` · `design · r2`

Paired feature-matched comparison of GPT-4.0-Turbo zero-shot ratings (3 runs per conversation) against 3 blinded human raters. GPT feedback-rating ICCs were on par with human raters, but reproducibility was low due to run-to-run inconsistencies.

> "authenticity ratings (Table 4) were significantly lower (Table 5) for human-generated versus GPT-generated ratings (ie, −0.98 points for humanlike; −0.52 points overall), whereas feedback ratings were similar for both (ie, only 0.10 points higher)."

## Discussion


## Related Claims
- [GPT-4.0-Turbo outperformed GPT-3.5-Turbo in dialogue authenticity, user experience, and feedback quality](gpt4-outperforms-gpt35-vp-quality.md) — related
- [Human-clinician dialogues yield higher user experience ratings than GPT self-chat dialogues, with similar authenticity](human-clinician-higher-experience-than-self-chat.md) — related
- [LLM-powered virtual patients generate authentic patient-clinician dialogues rated favorably by blinded physician raters](llm-vp-authentic-dialogues.md) — reports the opposite
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](llm-grading-mixed-against-human-raters.md) — related
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
- [In blind verification, model selection matters more than source type: Bradley-Terry ranking interleaves human coders and LLMs, with per-model win rates spanning significant human advantage to numerical LLM advantage](bradley-terry-model-selection-matters-more-than-source-type.md) — related
- [GPT-4 achieved almost perfect inter-rater reliability with faculty after three iterations of rubric engineering on three of four medical school OEQ questions](gpt4-almost-perfect-irr-after-rubric-engineering.md) — related
