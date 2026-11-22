---
type: claim
title: ChatGPT Code Interpreter correctly plots, fits and analyses real experimental data when explicitly prompted to perform an ODR fit
description: ChatGPT Code Interpreter correctly plots, fits and analyses real experimental data when explicitly prompted to perform an ODR fit
id: chatgpt-code-interpreter-real-data-odr-analysis
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
    kind: qualitative
    rigour: 2
---

# ChatGPT Code Interpreter correctly plots, fits and analyses real experimental data when explicitly prompted to perform an ODR fit

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · qualitative `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` With real student data uploaded, ChatGPT performed an ODR fit and correctly calculated the spring constant, its uncertainty, and the reduced chi-squared statistic, matching the researchers' own analysis. [→ Andrew Low and Z. Yasemin Kalender 2023](#andrew-low-and-z-yasemin-kalender-2023)

## Evidence

### Andrew Low and Z. Yasemin Kalender 2023

Andrew Low and Z. Yasemin Kalender. (2023). Data Dialogue with ChatGPT: Using Code Interpreter to Simulate and Analyse Experimental Data. [doi:10.48550/arXiv.2311.12415](https://doi.org/10.48550/arXiv.2311.12415)

`q2 · i?` · `qualitative · r2`

Case-study interaction analysis of Approach 3, in which real student data in an Excel spreadsheet was uploaded and ChatGPT was explicitly prompted to "Perform an ODR fit". It returned k = 50.86 ± 2.80 N/m with reduced chi-squared 1.88 for Method 1; the authors state results were "identical to those obtained by the researchers using the same data set".

> "ChatGPT then proceeded to write and run the necessary Python code, plot a graph (Figure 6), before responding with a value for the spring constant of 50 .86 ± 2.80N/m and a reduced chi-squared statistic of 1 .88."

## Discussion


## Related Claims
- [ChatGPT's curve_fit line fitting in Approach 2 neglects x-errors even when the synthetic data includes uncertainties in both variables](curve-fit-neglects-x-errors.md) — related
- [The quality and accuracy of ChatGPT's output on a lab activity varies significantly with the detail and specificity of the prompts](prompt-detail-determines-chatgpt-lab-output-quality.md) — a broader claim this one bears on
- [Novice learners may struggle to identify ChatGPT errors or provide the prompt detail needed for high-quality output](novice-learners-struggle-to-spot-chatgpt-errors.md) — a broader claim this one bears on
- [ChatGPT's simulated lab data is heteroscedastic and unrealistic because noise scales with the magnitude of the measured value](chatgpt-simulated-data-heteroscedastic-unrealistic.md) — related
- [Analyzing data from a student-built detector introduces students to statistical methods at a level not available in standard courses](detector-data-statistics-beyond-standard-courses.md) — related
