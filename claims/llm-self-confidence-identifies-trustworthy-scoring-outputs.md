---
type: claim
title: Model self-confidence gauges LLM confidence in probability estimates and helps identify when machine-generated scoring outputs are trustworthy
description: Model self-confidence gauges LLM confidence in probability estimates and helps identify when machine-generated scoring outputs are trustworthy
id: llm-self-confidence-identifies-trustworthy-scoring-outputs
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: organisciak-2026
    resource: "https://doi.org/10.3758/s13428-026-03058-1"
    title: "Organisciak, P., & Acar, S. (2026). Know when to trust: Making AI scoring more reliable for educational assessment. Behavior Research. https://doi.org/10.3758/s13428-026-03058-1"
    author: "Organisciak, P., & Acar, S."
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# Model self-confidence gauges LLM confidence in probability estimates and helps identify when machine-generated scoring outputs are trustworthy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`

## Subclaims
`q3 i?` Model self-confidence taps LLMs' internal mechanisms to gauge confidence in probability estimates, helping identify trustworthy machine-generated outputs. [→ Organisciak 2026](#organisciak-2026)

## Evidence

### Organisciak 2026

Organisciak, P., & Acar, S. (2026). Know when to trust: Making AI scoring more reliable for educational assessment. Behavior Research. https://doi.org/10.3758/s13428-026-03058-1

`q3 · i?` · `design · r2`

One of three techniques evaluated in the study, tested on divergent thinking response scoring; the article reports it shows statistically significant positive results, with no separate effect size printed for this technique alone.

> "Model self-confidence taps into LLMs’ internal mechanisms to gauge their confidence in probability estimates, helping identify when machine-generated outputs are trustworthy."

## Discussion


## Related Claims
- [Latent (token-probability) confidence is the weakest single-source confidence signal for LLM-based ASAG, with the lowest AUROC and worst calibration](latent-confidence-weakest-asag.md) — a narrower finding that bears on this claim
- [Making trustworthiness metrics and visualizations explicit increased inter-rater reliability among learning engineers evaluating LLM responses](trustworthiness-metrics-visualizations-increase-expert-agreement.md) — related
- [Generative AI generates responses based on probability and pattern prediction, not reasoning or understanding](genai-probabilistic-prediction-not-reasoning.md) — related
- [LLM-as-judge automated evaluation can achieve human-level agreement when carefully validated](llm-as-judge-human-level-agreement-with-validation.md) — related
- [Trustworthiness metrics and visualizations surfaced previously overlooked pedagogical risks and enabled more deliberate reasoning about trade-offs between competing objectives](trustworthiness-tools-surface-risks-enable-tradeoff-reasoning.md) — related
- [Model self-confidence, weighted probabilistic scoring, and ensemble modeling each significantly improve LLM-based divergent thinking scoring, raising correlation with human judges from r = 0.781 to r = 0.823](llm-scoring-three-techniques-raise-human-judge-correlation.md) — a broader claim this one bears on
