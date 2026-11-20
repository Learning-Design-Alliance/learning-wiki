---
type: claim
title: "In Approach 1 ChatGPT incorrectly calculated the uncertainty in the force as a constant 2% of gravitational field strength"
description: "In Approach 1 ChatGPT incorrectly calculated the uncertainty in the force as a constant 2% of gravitational field strength"
id: approach1-force-uncertainty-error
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

# In Approach 1 ChatGPT incorrectly calculated the uncertainty in the force as a constant 2% of gravitational field strength

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The generated Python code for Method 1 of Approach 1 propagated an incorrect force uncertainty, missing a factor of the mass. [→ Andrew Low and Z. Yasemin Kalender 2023](#andrew-low-and-z-yasemin-kalender-2023)

## Evidence

### Andrew Low and Z. Yasemin Kalender 2023

Andrew Low and Z. Yasemin Kalender. (2023). Data Dialogue with ChatGPT: Using Code Interpreter to Simulate and Analyse Experimental Data. [doi:10.48550/arXiv.2311.12415](https://doi.org/10.48550/arXiv.2311.12415)

`q2 · i?` · `design · r2`

Analysis of the Python code ChatGPT wrote in Approach 1 for Method 1. The authors show the correct expression reduces to ∆F = F × 0.02, so ChatGPT's expression "was missing a factor of m". Method 2's error propagation in the same Approach was correct.

> "the uncertainty in the force, ∆ F , was incorrectly calculated as ∆ F = g × 0.02 (highlighted in red in the code above), which would imply that each force value had a constant uncertainty equal to 2% of the gravitational field strength."

## Discussion


## Related Claims
- [ChatGPT's curve_fit line fitting in Approach 2 neglects x-errors even when the synthetic data includes uncertainties in both variables](curve-fit-neglects-x-errors.md) — related
- [The quality and accuracy of ChatGPT's output on a lab activity varies significantly with the detail and specificity of the prompts](prompt-detail-determines-chatgpt-lab-output-quality.md) — a broader claim this one bears on
- [Novice learners may struggle to identify ChatGPT errors or provide the prompt detail needed for high-quality output](novice-learners-struggle-to-spot-chatgpt-errors.md) — a broader claim this one bears on
