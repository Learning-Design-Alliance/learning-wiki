---
type: claim
title: "The quality and accuracy of ChatGPT's output on a lab activity varies significantly with the detail and specificity of the prompts"
description: "The quality and accuracy of ChatGPT's output on a lab activity varies significantly with the detail and specificity of the prompts"
id: prompt-detail-determines-chatgpt-lab-output-quality
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

# The quality and accuracy of ChatGPT's output on a lab activity varies significantly with the detail and specificity of the prompts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across three Approaches, more detailed and specific prompts produced more sophisticated data generation and analysis, including line fits with error bars and correct error propagation. [→ Andrew Low and Z. Yasemin Kalender 2023](#andrew-low-and-z-yasemin-kalender-2023)

## Evidence

### Andrew Low and Z. Yasemin Kalender 2023

Andrew Low and Z. Yasemin Kalender. (2023). Data Dialogue with ChatGPT: Using Code Interpreter to Simulate and Analyse Experimental Data. [doi:10.48550/arXiv.2311.12415](https://doi.org/10.48550/arXiv.2311.12415)

`q2 · i?` · `design · r2`

Authors' comparative analysis of three prompting Approaches on the same Spring Constant activity, summarised in Table II: Approach 1 used no line fit and had incorrect error propagation, while Approaches 2 and 3 used line fits, plotted graphs with error bars, and used correct error propagation.

> "the quality and accuracy of ChatGPT's output varied significantly across three different Approaches, highlighting the importance of prompt detail and specificity when using Code Interpreter for data generation and analysis."

## Discussion


## Related Claims
- [In Approach 1 ChatGPT incorrectly calculated the uncertainty in the force as a constant 2% of gravitational field strength](approach1-force-uncertainty-error.md) — a narrower finding that bears on this claim
- [ChatGPT Code Interpreter correctly plots, fits and analyses real experimental data when explicitly prompted to perform an ODR fit](chatgpt-code-interpreter-real-data-odr-analysis.md) — a narrower finding that bears on this claim
- [ChatGPT's curve_fit line fitting in Approach 2 neglects x-errors even when the synthetic data includes uncertainties in both variables](curve-fit-neglects-x-errors.md) — a narrower finding that bears on this claim
- [Novice learners may struggle to identify ChatGPT errors or provide the prompt detail needed for high-quality output](novice-learners-struggle-to-spot-chatgpt-errors.md) — related
- [The authors observe that more specific physical descriptions in generation prompts tend to produce more physically coherent AI-generated motion](prompt-specificity-shapes-physical-coherence.md) — a broader claim this one bears on
- [Teachers report ChatGPT-generated math questions misalign with grade level and topic, are unreliable or unanswerable, and cost time](chatgpt-brainstorming-concerns-misalignment-reliability.md) — related
- [Assessments more resistant to ChatGPT are open-ended, involve images or student-specific outputs, or do not specify expected output in detail](assessment-features-resistant-to-chatgpt.md) — related
- [Prompt specificity changes AI tutor pedagogy: a no-direct-answer guardrail alone produces uniform questioning, while a detailed guided protocol produces varied, impasse-sensitive responses](prompt-specificity-shapes-tutor-pedagogy.md) — a broader claim this one bears on
- [Prompting ChatGPT 3.5 with detailed IELTS band descriptors achieves moderate interrater agreement and good interrater consistency with official examiner grades](llm-detailed-criteria-prompt-moderate-agreement-good-consistency.md) — related
- [External plugins such as Wolfram and the Advanced Data Analysis mode significantly improve ChatGPT-4's ability to perform calculations that LLMs cannot reliably do alone](plugins-improve-chatgpt4-calculation-ability.md) — related
- [Students expected ChatGPT could serve as a substitute for the teacher in answering conceptual questions during labs](students-see-chatgpt-as-teacher-substitute-conceptual-questions.md) — related
