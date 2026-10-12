---
type: claim
title: Prompt quality and detailed scoring rubrics significantly influence the accuracy and consistency of LLM-generated grades
description: Prompt quality and detailed scoring rubrics significantly influence the accuracy and consistency of LLM-generated grades
id: prompt-rubric-quality-drives-llm-grading
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: marcin-jukiewicz-and-michał-wyrwa-2026
    resource: "https://doi.org/10.3390/app16020680"
    title: "Marcin Jukiewicz and Michał Wyrwa. (2026). Can ChatGPT Replace the Teacher in Assessment? A Review of Research on the Use of Large Language Models in Grading and Providing Feedback. Appl. Sci. 2026, 16, 680. https://doi.org/10.3390/app16020680"
    author: Marcin Jukiewicz and Michał Wyrwa
    q: 3
    i: "?"
    kind: review
    rigour: 3
  - id: marcin-jukiewicz-and-michał-wyrwa-2026-2
    resource: "https://doi.org/10.3390/app16020680"
    title: "Marcin Jukiewicz and Michał Wyrwa. (2026). Can ChatGPT Replace the Teacher in Assessment? A Review of Research on the Use of Large Language Models in Grading and Providing Feedback. Appl. Sci. 2026, 16, 680. https://doi.org/10.3390/app16020680"
    author: Marcin Jukiewicz and Michał Wyrwa
    q: 2
    i: "?"
    kind: review
    rigour: 3
---

# Prompt quality and detailed scoring rubrics significantly influence the accuracy and consistency of LLM-generated grades

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · review `r3` · `q2`–`q3`

## Subclaims
`q3 i?` Testing prompts beforehand and using detailed scoring rubrics supplemented with sample correct answers is especially vital for consistent and effective grading. [→ Marcin Jukiewicz and Michał Wyrwa 2026](#marcin-jukiewicz-and-micha-wyrwa-2026)
`q2 i?` In one reviewed study, using a detailed rubric improved AI grading accuracy by 9% and F1 by 15% compared to classical general scoring. [→ Marcin Jukiewicz and Michał Wyrwa 2026 (2)](#marcin-jukiewicz-and-micha-wyrwa-2026-2)

## Evidence

### Marcin Jukiewicz and Michał Wyrwa 2026

Marcin Jukiewicz and Michał Wyrwa. (2026). Can ChatGPT Replace the Teacher in Assessment? A Review of Research on the Use of Large Language Models in Grading and Providing Feedback. Appl. Sci. 2026, 16, 680. https://doi.org/10.3390/app16020680

`q3 · i?` · `review · r3`

The review's RQ4 synthesis identifies prompting as the heaviest influence on grading outcomes, with rubrics and exemplar answers named as vital for consistency. No effect size is printed for this synthesis-level statement.

> "The final outcome is especially heavily influenced by the prompt given to the GenAI. Testing prompts beforehand and focusing on their precision, for instance by having detailed scoring rubrics supplemented with sample correct answers, seem to be especially vital for consistent and effective grading"

### Marcin Jukiewicz and Michał Wyrwa 2026 (2)

Marcin Jukiewicz and Michał Wyrwa. (2026). Can ChatGPT Replace the Teacher in Assessment? A Review of Research on the Use of Large Language Models in Grading and Providing Feedback. Appl. Sci. 2026, 16, 680. https://doi.org/10.3390/app16020680

`q2 · i?` · `review · r3`

The review reports, from a single chemistry study in its table, that detailed rubrics improved accuracy by 9% and F1 by 15% over general scoring. These are printed percentage improvements, not standardized effect sizes.

> "Using a detailed rubric (i.e., breaking grading into many small criteria) improves AI's results by 9% (accuracy) and 15% (F1) compared to classical, general scoring."

## Discussion


## Related Claims
- [Model performance is robust to minor prompt wording changes but sensitive to holistic rubric redesign](rubric-structure-part-of-assessment-construct.md) — related
- [AI scoring consistency approaches or exceeds 90% for most rubric items, but spelling is replaced by a deterministic LanguageTool-based approach achieving 68% accuracy with 100% consistency](ai-consistency-high-except-spelling-languagetool-replacement.md) — related
- [Prompt design significantly influences LLM accuracy on IVDA MCQs, with slide context reducing smaller-model accuracy but improving GPT models, while persona effects are inconsistent](prompt-design-affects-mcq-accuracy-asymmetrically.md) — related
- [LLM accuracy increases monotonically with prompt sophistication across semantically equivalent medical questions, with Low Literacy users scoring significantly below Prompt Engineer users](prompt-privilege-monotonic-accuracy-gap-medqa.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
- [Hint-based prompts raise ChatGPT scoring agreement with human experts to 98–100%, while no-hint prompts are unstable (Q2 precision 0.42)](hint-prompts-raise-llm-scoring-agreement.md) — a narrower finding that bears on this claim
- [Removing detailed rubric explanations from prompts improved grading accuracy across all approaches in an ablation study](simplified-prompts-outperform-detailed-rubrics.md) — reports the opposite
