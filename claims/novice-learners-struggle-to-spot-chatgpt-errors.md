---
type: claim
title: Novice learners may struggle to identify ChatGPT errors or provide the prompt detail needed for high-quality output
description: Novice learners may struggle to identify ChatGPT errors or provide the prompt detail needed for high-quality output
id: novice-learners-struggle-to-spot-chatgpt-errors
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2023
sources:
  - id: andrew-low-and-z-yasemin-kalender-2023
    resource: "https://doi.org/10.48550/arXiv.2311.12415"
    title: "Andrew Low and Z. Yasemin Kalender. (2023). Data Dialogue with ChatGPT: Using Code Interpreter to Simulate and Analyse Experimental Data. [doi:10.48550/arXiv.2311.12415](https://doi.org/10.48550/arXiv.2311.12415)"
    author: Andrew Low and Z. Yasemin Kalender
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Novice learners may struggle to identify ChatGPT errors or provide the prompt detail needed for high-quality output

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` The authors' experience suggests novices might not recognise flaws in ChatGPT output or supply expert-like prompt detail, so caution and critical thinking remain necessary. [→ Andrew Low and Z. Yasemin Kalender 2023](#andrew-low-and-z-yasemin-kalender-2023)

## Evidence

### Andrew Low and Z. Yasemin Kalender 2023

Andrew Low and Z. Yasemin Kalender. (2023). Data Dialogue with ChatGPT: Using Code Interpreter to Simulate and Analyse Experimental Data. [doi:10.48550/arXiv.2311.12415](https://doi.org/10.48550/arXiv.2311.12415)

`q1 · i?` · `design · r2`

Authors' interpretation from their interaction study, not a tested result: Approach 1's prompts were deliberately written to mimic a novice user and novice learner, and the resulting output contained an incorrect force uncertainty and no line fit. High-quality output required expert-like prompts and scrutiny of the Python code.

> "our experience in this study suggests that novice learners might struggle to identify ChatGPT errors, or to provide the necessary level of prompt detail when questioning ChatGPT."

## Discussion


## Related Claims
- [In Approach 1 ChatGPT incorrectly calculated the uncertainty in the force as a constant 2% of gravitational field strength](approach1-force-uncertainty-error.md) — a narrower finding that bears on this claim
- [ChatGPT Code Interpreter correctly plots, fits and analyses real experimental data when explicitly prompted to perform an ODR fit](chatgpt-code-interpreter-real-data-odr-analysis.md) — a narrower finding that bears on this claim
- [ChatGPT's curve_fit line fitting in Approach 2 neglects x-errors even when the synthetic data includes uncertainties in both variables](curve-fit-neglects-x-errors.md) — a narrower finding that bears on this claim
- [GenAI novices develop prompting strategies through trial and error, starting from zero-shot prompts and refining them after unsatisfactory outputs](novices-refine-prompts-trial-and-error.md) — related
- [Reviewed literature reports risks of overreliance, AI errors in complex tasks, and students' uncritical acceptance of AI-generated outputs](ai-math-risks-overreliance-errors-uncritical-trust.md) — a broader claim this one bears on
- [The quality and accuracy of ChatGPT's output on a lab activity varies significantly with the detail and specificity of the prompts](prompt-detail-determines-chatgpt-lab-output-quality.md) — related
- [GenAI feedback limitations require students to exercise evaluative judgement](genai-limitations-require-evaluative-judgement.md) — a broader claim this one bears on
- [Participants' prompting was often limited, with poorly formulated prompts leading to vague or unhelpful outputs](poorly-formulated-prompts-vague-outputs.md) — a narrower finding that bears on this claim
- [Iterative prompt refinement and expert pilot-testing may partly explain favorable LLM virtual patient output quality](iterative-prompt-refinement-expert-testing-improves-output.md) — related
- [ChatGPT provided vague, partially incorrect, or irrelevant guidance on lab-specific procedures, leading some groups to abandon it](chatgpt-unreliable-lab-procedure-guidance.md) — related
- [In the software project, junior developers without language experience wrote code with GenAI (Co-Pilot) under a detailed design, but this augmentation depends on high-quality design](code-project-junior-developers-copilot.md) — related
