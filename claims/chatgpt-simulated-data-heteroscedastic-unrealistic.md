---
type: claim
title: "ChatGPT's simulated lab data is heteroscedastic and unrealistic because noise scales with the magnitude of the measured value"
description: "ChatGPT's simulated lab data is heteroscedastic and unrealistic because noise scales with the magnitude of the measured value"
id: chatgpt-simulated-data-heteroscedastic-unrealistic
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: andrew-low-and-z-yasemin-kalender-2023
    resource: "https://doi.org/10.48550/arXiv.2311.12415"
    title: "Andrew Low and Z. Yasemin Kalender. (2023). Data Dialogue with ChatGPT: Using Code Interpreter to Simulate and Analyse Experimental Data. [doi:10.48550/arXiv.2311.12415](https://doi.org/10.48550/arXiv.2311.12415)"
    author: Andrew Low and Z. Yasemin Kalender
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# ChatGPT's simulated lab data is heteroscedastic and unrealistic because noise scales with the magnitude of the measured value

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In Approach 2 the standard deviation of the added noise was proportional to the true value, so larger data points are more dispersed around the line fit, which the authors judge unrealistic for introductory lab measurements. [→ Andrew Low and Z. Yasemin Kalender 2023](#andrew-low-and-z-yasemin-kalender-2023)

## Evidence

### Andrew Low and Z. Yasemin Kalender 2023

Andrew Low and Z. Yasemin Kalender. (2023). Data Dialogue with ChatGPT: Using Code Interpreter to Simulate and Analyse Experimental Data. [doi:10.48550/arXiv.2311.12415](https://doi.org/10.48550/arXiv.2311.12415)

`q2 · i?` · `design · r2`

Code analysis of Approach 2's data generation, where noise standard deviation equalled 5% of the true value, producing dispersion that increases with magnitude. The authors conclude "we consider the simulated data to be 'unrealistic'" because metre-rule and stop-clock uncertainties would not grow this way.

> "This heteroscedasticity in the simulated data can be clearly identified by the dispersion of the data around the line-fit for larger absolute values in both Figure 4 and Figure 5."

## Discussion


## Related Claims
- [ChatGPT Code Interpreter correctly plots, fits and analyses real experimental data when explicitly prompted to perform an ODR fit](chatgpt-code-interpreter-real-data-odr-analysis.md) — related
- [Autograder accuracy on individual exams fluctuates around the expected performance, and strong deviations can be reliably detected by validation](per-exam-accuracy-fluctuates-validation-detects-deviations.md) — related
- [ChatGPT's curve_fit line fitting in Approach 2 neglects x-errors even when the synthetic data includes uncertainties in both variables](curve-fit-neglects-x-errors.md) — related
