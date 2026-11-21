---
type: strategy
id: llm-research-verification-practices-strategy
title: Verify LLM outputs against primary sources, cross-check models against each other, prompt for reasoning, and start a new chat when errors persist
description: "Based on their semester of LLM-assisted research, the students recommend that scientists \"should be skeptical of citations and links to research papers output by LLMs\" and always verify summaries against the actual st..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: zabludoff-2025
    resource: "https://arxiv.org/archive/astro-ph"
    title: "Zabludoff, A., Chuang, C., Johnson, P. T., Liu, Y., Martinez, B. B., Shah, N., Steffes, L., & Weible, G. G. (2025). Can LLMs Produce Original Astronomy Research in a Semester? A Graduate Class Experiment. https://arxiv.org/archive/astro-ph"
    author: "Zabludoff, A., Chuang, C., Johnson, P. T., Liu, Y., Martinez, B. B., Shah, N., Steffes, L., & Weible, G. G"
---

# Verify LLM outputs against primary sources, cross-check models against each other, prompt for reasoning, and start a new chat when errors persist

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (6 for) · 5 studies (2 qualitative, 1 review, 1 associational, 1 design), `q1`–`q2` · 0 of 5 report an effect size · 6 claims rest on one study

## Description
Based on their semester of LLM-assisted research, the students recommend that scientists "should be skeptical of citations and links to research papers output by LLMs" and always verify summaries against the actual studies, since manual review of primary references is key to accuracy. They further advise asking different LLMs to cross-check each other, prompting models to explain their reasoning before the next prompt, and starting a new chat when an LLM keeps generating an incorrect result, because continuing in the same chat seems to reinforce earlier misunderstandings.

## Design Implications

### Context
#### Requirements
- Requires manual review capacity and access to primary sources such as Google or NASA ADS to verify citations, code outputs, and methodologies.
#### Constraints
- Re-prompting an LLM without providing additional information does not improve accuracy, per the students' experience.

### Target Learners
- graduate science students
- researchers adopting LLM tools

### Target Learning Goals
- conducting accurate original research with LLM assistance
- critical evaluation of AI-generated scientific content

## Claims

- [LLMs returned false citations, links, or paper summaries about 20% of the time during graduate literature research](../claims/llm-false-citations-twenty-percent.md) [+W]
- [LLMs made implicit, overly simplifying assumptions without justification and often doubled down after being corrected, including fabricating measurement uncertainties](../claims/llm-implicit-assumptions-doubling-down.md) [+W]
- [Low comment rewriting does not imply a smooth process: students describe the main effort as verifying generated code rather than revising prompts](../claims/verification-burden-shifts-work-from-rewriting-to-reviewing.md) [+W]
- [LLM responses that are incomplete or incorrect prompt students to question, verify and improve the information, fostering critical thinking through cycles of validation and correction](../claims/llm-errors-prompt-validation-cycles-critical-thinking.md) [+W]
- [High-achieving students describe selective AI use for clarification, summarisation, and workflow support while verifying outputs and keeping them subordinate to their own judgment](../claims/qualitative-selective-verification-intensive-use.md) [+W]
- [LLMs expressed unjustified confidence in recommendations based on visual inputs, asserting incorrect pin-connection diagnoses with high stated certainty](../claims/llm-unjustified-confidence-visual-recommendations.md) [+W]

## Related Strategies

- [Cautious, verified use of ChatGPT with critical cross-referencing of AI-provided sources](cautious-verified-chatgpt-use-strategy.md)
- [Frame LLM use in biomedical education around low‐stakes formative tasks with expert‐guided verification and rationale requests](llm-low-stakes-formative-use-expert-verification-strategy.md)
- [Use LLMs to improve and proofread your own writing while keeping your voice, define prompts carefully, and treat all LLM output as a draft to edit critically](llm-assisted-proposal-writing-strategy.md)

## Examples
-

## Key Sources
- Zabludoff, A., Chuang, C., Johnson, P. T., Liu, Y., Martinez, B. B., Shah, N., Steffes, L., & Weible, G. G. (2025). Can LLMs Produce Original Astronomy Research in a Semester? A Graduate Class Experiment. https://arxiv.org/archive/astro-ph
