---
type: claim
title: Temperature parameter has a statistically significant but negligible effect on GPT-4o exam accuracy (ηG² = 0.0017), with global accuracy peaking at temperature 0.23
description: Temperature parameter has a statistically significant but negligible effect on GPT-4o exam accuracy (ηG² = 0.0017), with global accuracy peaking at temperature 0.23
id: temperature-effect-negligible-gpt4o-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: altermatt-fernando-r-2025
    resource: "https://doi.org/10.1186/s12909-025-08084-9"
    title: "Altermatt Fernando R., Neyem Andres, Sumonte Nicolás I., Villagrán Ignacio, Mendoza Marcelo, Lacassie Hector J., Delfino Alejandro E. (2025). Evaluating GPT-4o in high-stakes medical assessments: performance and error analysis on a Chilean anesthesiology exam. BMC Medical Education. https://doi.org/10.1186/s12909-025-08084-9"
    author: Altermatt Fernando R., Neyem Andres, Sumonte Nicolás I., Villagrán Ignacio, Mendoza Marcelo, Lacassie Hector J., Delfino Alejandro E.
    q: 2
    i: 0
    kind: causal
    rigour: 1
---

# Temperature parameter has a statistically significant but negligible effect on GPT-4o exam accuracy (ηG² = 0.0017), with global accuracy peaking at temperature 0.23

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2` · `i0` negligible
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i0` Repeated measures ANOVA across 30 temperature settings showed a significant but negligible temperature effect (F(29, 5278) = 1.773, p = 0.0065, ηG² = 0.0017); accuracy ranged from 80.5% to 86.3%, peaking at temperature 0.23 (86.3%). [→ Altermatt Fernando R. 2025](#altermatt-fernando-r-2025)

## Evidence

### Altermatt Fernando R. 2025

Altermatt Fernando R., Neyem Andres, Sumonte Nicolás I., Villagrán Ignacio, Mendoza Marcelo, Lacassie Hector J., Delfino Alejandro E. (2025). Evaluating GPT-4o in high-stakes medical assessments: performance and error analysis on a Chilean anesthesiology exam. BMC Medical Education. https://doi.org/10.1186/s12909-025-08084-9

`q2 · i0` · `causal · r1`

Simulation analysis varying temperature across 30 runs with Greenhouse-Geisser correction. The printed effect size ηG² = 0.0017 is negligible (below d = 0.2 equivalent); the authors state accuracy "variations remaining within a narrow range (80.5% to 86.3%)".

> "Repeated measures ANOVA showed significant effects of temperature on accuracy (F(29, 5278) = 1.773, p = 0.0065, ηG² = 0.0017). Global accuracy reached its peak at temperature 0.23 (86.3%), with secondary peaks at 0.52 (85.2%) and 1.0 (85.8%)."

## Discussion


## Related Claims
- [GPT-4o's accuracy on the CONACEM anesthesiology exam varies significantly by cognitive domain, highest in Understanding (90.10%) and lowest in Application (76.83%) and Analysis (76.54%)](gpt4o-conacem-accuracy-varies-by-cognitive-domain.md) — related
- [All three LLMs show near-perfect answer reproducibility under repeated API testing at zero temperature, highest for Claude 3.5 Sonnet (99.9%)](llm-kmle-reproducibility-near-perfect.md) — related
- [Bootstrapped self-consistency at temperature 1.0 flags potentially incorrect GPT-4 answers: about half of inconsistent responses were incorrect versus about 5% of consistent ones](bootstrapping-self-consistency-flags-incorrect-answers.md) — related
- [Gemini 1.5 Pro shows the highest response consistency across 30 repeated exam attempts, significantly exceeding GPT-4o but statistically comparable to Claude](gemini-highest-response-consistency-repeated-attempts.md) — related
