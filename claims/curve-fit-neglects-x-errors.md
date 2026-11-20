---
type: claim
title: "ChatGPT's curve_fit line fitting in Approach 2 neglects x-errors even when the synthetic data includes uncertainties in both variables"
description: "ChatGPT's curve_fit line fitting in Approach 2 neglects x-errors even when the synthetic data includes uncertainties in both variables"
id: curve-fit-neglects-x-errors
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
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

# ChatGPT's curve_fit line fitting in Approach 2 neglects x-errors even when the synthetic data includes uncertainties in both variables

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Despite detailed prompts, ChatGPT used a least-squares line fit that factored in only y-errors, and its chi-squared statistic likewise included only the y-errors. [→ Andrew Low and Z. Yasemin Kalender 2023](#andrew-low-and-z-yasemin-kalender-2023)

## Evidence

### Andrew Low and Z. Yasemin Kalender 2023

Andrew Low and Z. Yasemin Kalender. (2023). Data Dialogue with ChatGPT: Using Code Interpreter to Simulate and Analyse Experimental Data. [doi:10.48550/arXiv.2311.12415](https://doi.org/10.48550/arXiv.2311.12415)

`q2 · i?` · `design · r2`

Code analysis of Approach 2, where curve_fit was used with sigma set to extension errors only. The authors note the reduced chi-squared calculation also included only extension errors, though ChatGPT did not mention this, and that error bars for both variables were still plotted.

> "despite ChatGPT generating synthetic data that included uncertainties in both force and extension, the curve fit function used for the line-fitting only makes use of the y-error's (extension), and neglects to factor in the x-errors (force)."

## Discussion


## Related Claims
- [In Approach 1 ChatGPT incorrectly calculated the uncertainty in the force as a constant 2% of gravitational field strength](approach1-force-uncertainty-error.md) — related
- [ChatGPT Code Interpreter correctly plots, fits and analyses real experimental data when explicitly prompted to perform an ODR fit](chatgpt-code-interpreter-real-data-odr-analysis.md) — related
- [The quality and accuracy of ChatGPT's output on a lab activity varies significantly with the detail and specificity of the prompts](prompt-detail-determines-chatgpt-lab-output-quality.md) — a broader claim this one bears on
- [Novice learners may struggle to identify ChatGPT errors or provide the prompt detail needed for high-quality output](novice-learners-struggle-to-spot-chatgpt-errors.md) — a broader claim this one bears on
- [ChatGPT's simulated lab data is heteroscedastic and unrealistic because noise scales with the magnitude of the measured value](chatgpt-simulated-data-heteroscedastic-unrealistic.md) — related
