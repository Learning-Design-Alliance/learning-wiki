---
type: claim
title: GenAI services can be used to verify the quality of generated isomorphic problems, identifying and correcting erroneous items
description: GenAI services can be used to verify the quality of generated isomorphic problems, identifying and correcting erroneous items
id: genai-verification-of-generated-item-quality
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: zhongzhou-chen-2025
    resource: "https://doi.org/10.48550/arXiv.2508.14755"
    title: "Zhongzhou Chen. (2025). Reliable generation of isomorphic physics problems using Generative AI with prompt-chaining and tool use. [doi:10.48550/arXiv.2508.14755](https://doi.org/10.48550/arXiv.2508.14755)"
    author: Zhongzhou Chen
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GenAI services can be used to verify the quality of generated isomorphic problems, identifying and correcting erroneous items

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Of the 20 total problems in Problem Bank 1, GenAI identified and corrected 6 problems containing incorrect formula derivation in the solution text. [→ Zhongzhou Chen 2025](#zhongzhou-chen-2025)

## Evidence

### Zhongzhou Chen 2025

Zhongzhou Chen. (2025). Reliable generation of isomorphic physics problems using Generative AI with prompt-chaining and tool use. [doi:10.48550/arXiv.2508.14755](https://doi.org/10.48550/arXiv.2508.14755)

`q2 · i?` · `design · r2`

Outcome verification step (Section III.C): the yaml file was uploaded to Gemini Pro 2.5 and prompted to check answer correctness; "6 problems that contain incorrect formula derivation" were found and corrected.

> "Of the 20 total problems in Problem Bank 1, GenAI identified, and corrected, 6 problems that contain incorrect formula derivation in the solution text."

## Discussion


## Related Claims
- [LLM responses that are incomplete or incorrect prompt students to question, verify and improve the information, fostering critical thinking through cycles of validation and correction](llm-errors-prompt-validation-cycles-critical-thinking.md) — related
- [Trained students more often identify and remediate GenAI deficiencies such as visual errors and reasoning flaws](trained-students-remediate-genai-deficiencies.md) — related
- [Students rate genAI most helpful for explaining domain knowledge and least helpful for verifying solutions, while faculty recommend genAI for fewer than a third of problem-solving uses](student-faculty-misalignment-genai-problem-solving.md) — reports the opposite
- [GPT-4 grading feedback sounds plausible but frequently contains incorrect or misleading statements](gpt4-feedback-plausible-but-misleading.md) — related
- [GPT-4 tends to assume feedback is correct when it sounds convincing but incorrectly identifies the student error or provides an invalid suggestion, and has a high false positive rate on the diagnostic label.](gpt4-feedback-evaluation-shortcomings.md) — related
- [Prompt-chaining produces higher quality and more consistent isomorphic physics problems than single-prompt or simple-prompt generation](prompt-chaining-outperforms-single-prompt-isomorphic-generation.md) — related
