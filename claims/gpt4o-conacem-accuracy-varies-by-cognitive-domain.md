---
type: claim
title: "GPT-4o's accuracy on the CONACEM anesthesiology exam varies significantly by cognitive domain, highest in Understanding (90.10%) and lowest in Application (76.83%) and Analysis (76.54%)"
description: "GPT-4o's accuracy on the CONACEM anesthesiology exam varies significantly by cognitive domain, highest in Understanding (90.10%) and lowest in Application (76.83%) and Analysis (76.54%)"
id: gpt4o-conacem-accuracy-varies-by-cognitive-domain
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: altermatt-fernando-r-2025
    resource: "https://doi.org/10.1186/s12909-025-08084-9"
    title: "Altermatt Fernando R., Neyem Andres, Sumonte Nicolás I., Villagrán Ignacio, Mendoza Marcelo, Lacassie Hector J., Delfino Alejandro E. (2025). Evaluating GPT-4o in high-stakes medical assessments: performance and error analysis on a Chilean anesthesiology exam. BMC Medical Education. https://doi.org/10.1186/s12909-025-08084-9"
    author: Altermatt Fernando R., Neyem Andres, Sumonte Nicolás I., Villagrán Ignacio, Mendoza Marcelo, Lacassie Hector J., Delfino Alejandro E.
    q: 3
    i: 3
    kind: design
    rigour: 2
  - id: altermatt-fernando-r-2025-2
    resource: "https://doi.org/10.1186/s12909-025-08084-9"
    title: "Altermatt Fernando R., Neyem Andres, Sumonte Nicolás I., Villagrán Ignacio, Mendoza Marcelo, Lacassie Hector J., Delfino Alejandro E. (2025). Evaluating GPT-4o in high-stakes medical assessments: performance and error analysis on a Chilean anesthesiology exam. BMC Medical Education. https://doi.org/10.1186/s12909-025-08084-9"
    author: Altermatt Fernando R., Neyem Andres, Sumonte Nicolás I., Villagrán Ignacio, Mendoza Marcelo, Lacassie Hector J., Delfino Alejandro E.
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4o's accuracy on the CONACEM anesthesiology exam varies significantly by cognitive domain, highest in Understanding (90.10%) and lowest in Application (76.83%) and Analysis (76.54%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q3` · `i3` large
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q3 i3` Across 30 simulation runs on 183 exam questions, GPT-4o achieved 83.67% overall accuracy, with a large significant effect of cognitive domain on performance (η² = 0.823). [→ Altermatt Fernando R. 2025](#altermatt-fernando-r-2025)
`q3 i?` Post-hoc tests showed significant pairwise differences between all domain pairs except Apply and Analyze (p = 0.975). [→ Altermatt Fernando R. 2025 (2)](#altermatt-fernando-r-2025-2)

## Evidence

### Altermatt Fernando R. 2025

Altermatt Fernando R., Neyem Andres, Sumonte Nicolás I., Villagrán Ignacio, Mendoza Marcelo, Lacassie Hector J., Delfino Alejandro E. (2025). Evaluating GPT-4o in high-stakes medical assessments: performance and error analysis on a Chilean anesthesiology exam. BMC Medical Education. https://doi.org/10.1186/s12909-025-08084-9

`q3 · i3` · `design · r2`

Simulation-based evaluation of GPT-4o on the CONACEM exam (183 questions, 30 independent runs, 5,490 responses). The one-way ANOVA across the four Bloom's domains yielded a large printed effect size, η² = 0.823 (also ω² = 0.817; Cohen's f = 2.155); overall accuracy was 4,595/5,490 (83.67%).

> "A one-way ANOVA confirmed a significant effect of cognitive domain on model performance, F(3, 116) = 179.49, p < 0.001, with a large effect size (η² = 0.823; ω² = 0.817; Cohen's f = 2.155)."

### Altermatt Fernando R. 2025 (2)

Altermatt Fernando R., Neyem Andres, Sumonte Nicolás I., Villagrán Ignacio, Mendoza Marcelo, Lacassie Hector J., Delfino Alejandro E. (2025). Evaluating GPT-4o in high-stakes medical assessments: performance and error analysis on a Chilean anesthesiology exam. BMC Medical Education. https://doi.org/10.1186/s12909-025-08084-9

`q3 · i?` · `design · r2`

Tukey HSD post-hoc comparisons from the same simulation evaluation, corroborated by Kruskal-Wallis tests (H = 98.76, p < 0.001, η² = 0.805) and a linear mixed-effects model. "significant pairwise differences between all domains" except Apply and Analyze; no effect size is printed for the pairwise contrasts.

> "Post-hoc Tukey HSD tests revealed significant pairwise differences between all domains (p < 0.001), except between Apply and Analyze (p = 0.975)."

## Discussion


## Related Claims
- [GPT-4o's 83.69% accuracy on CONACEM places it at the top of historical human cohort performance (median 67%, range 60–83%)](gpt4o-accuracy-top-of-human-conacem-cohorts.md) — related
- [ChatGPT-4o's accuracy on Chinese questions varied by question type, highest for A1-type (76%) and lowest for A2-type (61%)](chatgpt-4o-chinese-question-type-accuracy-varies.md) — related
- [All three LLMs exceed the 400/650-point passing threshold on a Chinese anesthesiology SRTP mock exam, with Claude 3.5 Sonnet achieving the highest mean score](llms-pass-chinese-anesthesiology-srtp-exam-claude-highest.md) — related
- [Gemini 1.5 Pro shows the highest response consistency across 30 repeated exam attempts, significantly exceeding GPT-4o but statistically comparable to Claude](gemini-highest-response-consistency-repeated-attempts.md) — related
- [Temperature parameter has a statistically significant but negligible effect on GPT-4o exam accuracy (ηG² = 0.0017), with global accuracy peaking at temperature 0.23](temperature-effect-negligible-gpt4o-accuracy.md) — related
- [Among GPT-4o's incorrect CONACEM responses, unsupported medical claims are the most common error (40.69%), followed by incorrect or vague conclusions (22.07%)](gpt4o-unsupported-medical-claims-most-common-error.md) — related
