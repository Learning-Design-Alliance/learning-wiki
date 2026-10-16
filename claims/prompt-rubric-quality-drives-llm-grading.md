---
type: claim
title: Prompt quality and detailed scoring rubrics significantly influence the accuracy and consistency of LLM-generated grades
description: Prompt quality and detailed scoring rubrics significantly influence the accuracy and consistency of LLM-generated grades
id: prompt-rubric-quality-drives-llm-grading
status: review
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

## Studies bearing on this claim

<!-- synthesis:start -->
*When an AI model scores work against a rubric, does the rubric's wording and detail decide how closely it agrees with human markers?* This table gathers the studies behind this claim and the 8 narrower claims that bear on it: **8 distinct studies** (4 causal, 2 associational, 1 review, 1 design), `q2`–`q3`, 0 of 8 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Marcin Jukiewicz and Michał Wyrwa 2026](https://doi.org/10.3390/app16020680) | q2 / q3 · review · r3 | i? | this claim |
| [Praveen Pathak 2026](https://doi.org/10.48550/arxiv.2608.20521) | q2 · causal · r1 | i? | [Focused rubric refinement that made required physics and scoring conditions explicit reduc](explicit-rubric-conditions-reduce-ai-disagreement.md) (supports) |
| [Pei-Yu Tseng 2026](https://doi.org/10.48550/arxiv.2606.23629) | q2 · causal · r1 | i? | [Revising the rubric to operationalize pedagogical constructs raises human–machine agreemen](rubric-revision-improves-machine-alignment.md) (supports); [Combining the revised rubric with rationale-first evaluation yields the highest human–mach](combined-rubric-rationale-highest-alignment.md) (supports) |
| [Olvet DM 2026](https://doi.org/10.1007/s40670-026-02638-2) | q3 · design · r3 | i? | [GPT-4 achieved almost perfect inter-rater reliability with faculty after three iterations ](gpt4-almost-perfect-irr-after-rubric-engineering.md) (supports) |
| [Olga Manakina 2026](https://doi.org/10.48550/arxiv.2608.23814) | q2 · causal · r1 | i? | [Removing detailed rubric explanations from prompts improved grading accuracy across all ap](simplified-prompts-outperform-detailed-rubrics.md) (counts against) |
| [Alonso-Carracedo 2026](https://doi.org/10.48550/arxiv.2607.02432) | q2 · causal · r2 | i? | [Rubric-enhanced prompting (Variant 2) raises LLM assigned scores relative to the no-rubric](rubric-prompting-raises-llm-assigned-scores.md) (qualifies) |
| [Jerin George Mathew 2026](https://doi.org/10.48550/arxiv.2603.23714) | q2 · associational · r2 | i? | [Different LLMs rely on different subsets of rubric traits when assigning essay scores](llms-weight-rubric-traits-differently.md) (qualifies) |
| [Greene Nolan 2023](https://doi.org/10.51388/20.500.12265/187) | q2 · associational · r2 | i? | [Teacher and AES scores agreed most at the lowest and highest rubric points but diverged in](teacher-aes-agree-tails-diverge-middle.md) (qualifies) |
<!-- synthesis:end -->

## Discussion

## Related Claims

- [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](llm-grading-mixed-against-human-raters.md) — the general claim this finding bears on, with the studies behind it
- Model performance is robust to minor prompt wording changes but sensitive to holistic rubric redesign — related
- [AI scoring consistency approaches or exceeds 90% for most rubric items, but spelling is replaced by a deterministic LanguageTool-based approach achieving 68% accuracy with 100% consistency](ai-consistency-high-except-spelling-languagetool-replacement.md) — related
- [Prompt design significantly influences LLM accuracy on IVDA MCQs, with slide context reducing smaller-model accuracy but improving GPT models, while persona effects are inconsistent](prompt-design-affects-mcq-accuracy-asymmetrically.md) — related
- [LLM accuracy increases monotonically with prompt sophistication across semantically equivalent medical questions, with Low Literacy users scoring significantly below Prompt Engineer users](prompt-privilege-monotonic-accuracy-gap-medqa.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
- [Hint-based prompts raise ChatGPT scoring agreement with human experts to 98–100%, while no-hint prompts are unstable (Q2 precision 0.42)](hint-prompts-raise-llm-scoring-agreement.md) — a narrower finding that bears on this claim
- [Removing detailed rubric explanations from prompts improved grading accuracy across all approaches in an ablation study](simplified-prompts-outperform-detailed-rubrics.md) — reports the opposite
- [GPT models achieved high polarity agreement with instructors only for positive feedback on the Topic aspect, and could not reliably assess the other rubric aspects](gpt-polarity-agreement-low-except-topic.md) — related
