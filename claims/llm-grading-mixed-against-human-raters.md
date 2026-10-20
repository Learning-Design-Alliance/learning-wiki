---
type: claim
title: "LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks"
description: "LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks"
id: llm-grading-mixed-against-human-raters
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
---

# LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r3` · `q3`

## Subclaims
`q3 i?` Across the reviewed studies, GenAI performed worse than humans in 11 cases and comparably in 12 cases for grading quality. [→ Marcin Jukiewicz and Michał Wyrwa 2026](#marcin-jukiewicz-and-micha-wyrwa-2026)
`q3 i?` For shorter, more straightforward tasks GenAI performance tends to be similar to human graders, while longer, complex, or subjective assignments reveal a lack of nuance. [→ Marcin Jukiewicz and Michał Wyrwa 2026](#marcin-jukiewicz-and-micha-wyrwa-2026)

## Evidence

### Marcin Jukiewicz and Michał Wyrwa 2026

Marcin Jukiewicz and Michał Wyrwa. (2026). Can ChatGPT Replace the Teacher in Assessment? A Review of Research on the Use of Large Language Models in Grading and Providing Feedback. Appl. Sci. 2026, 16, 680. https://doi.org/10.3390/app16020680

`q3 · i?` · `review · r3`

The review's synthesis of 42 empirical studies reports the tally of grading comparisons: "GenAI performed worse than humans in 11 cases" and was comparable in 12. No pooled effect size is printed, so no magnitude is reported.

> "The analyzed studies yield mixed results when comparing GenAI and human assessment. GenAI performed worse than humans in 11 cases. In 12 instances, its effectiveness was comparable to human ratings."

## Studies bearing on this claim

<!-- synthesis:start -->
*Can a language model score learners' written constructed responses as a trained human marker would, and on which tasks?* This table gathers the studies behind this claim and the 16 narrower claims that bear on it: **12 distinct studies** (5 design, 3 associational, 2 review, 1 causal, 1 qualitative), `q1`–`q3`, 2 of 12 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Marcin Jukiewicz and Michał Wyrwa 2026](https://doi.org/10.3390/app16020680) | q2 / q3 · review · r3 | i? | this claim; [Prompt quality and detailed scoring rubrics significantly influence the accuracy and consi](prompt-rubric-quality-drives-llm-grading.md) (qualifies); [Newer LLM generations such as GPT-4 generally outperform GPT-3.5 in short-answer grading a](gpt4-advantage-uneven-across-tasks.md) (qualifies) |
| [Jerin George Mathew 2026](https://doi.org/10.48550/arxiv.2603.23714) | q2 · associational · r2 | i? | [Out-of-the-box LLMs agree with human essay grades far less than human raters agree with ea](llm-essay-scoring-weak-human-agreement.md) (supports); [LLMs overrate short underdeveloped essays and over-penalize minor language errors in well-](llm-overrate-short-essays-overpenalize-errors.md) (supports); [Different LLMs rely on different subsets of rubric traits when assigning essay scores](llms-weight-rubric-traits-differently.md) (supports) |
| [Marcin Jukiewicz 2025](https://doi.org/10.48550/arxiv.2509.26483) | q2 · design · r2 | i? | [Even the best LLM grader reaches only moderate agreement with human teachers, below the th](llm-grading-moderate-human-agreement-icc.md) (supports) |
| [Habibullah 2026](https://doi.org/10.48550/arxiv.2609.29333) | q2 · causal · r2 | i?; i2 | [Six closed-model configurations grade at or below the human inter-grader floor of 2.61/35 ](closed-llm-graders-below-human-floor.md) (qualifies) |
| [Pecuchova 2025](https://doi.org/10.1007/s40593-025-00517-2) | q2 · design · r2 | i? | [Claude3 and PaLM2 show substantial agreement but fall short on identifying failing grades](claude3-palm2-substantial-agreement-failing-grades.md) (qualifies) |
| [Jan Cvengros and Gerd Kortemeyer 2026](https://doi.org/10.1007/s44163-026-01606-4) | q2 · design · r2 | i? | [AI-assigned total scores on a handwritten chemistry exam align strongly with TA-assigned t](ai-total-scores-align-with-ta-grades-chemistry-exam.md) (qualifies) |
| [Olvet DM 2026](https://doi.org/10.1007/s40670-026-02638-2) | q2 / q3 · design · r3 | i? | [Most faculty–GPT-4 scoring discrepancies were only one-point differences, shrinking across](oeq-scoring-discrepancies-mostly-one-point.md) (qualifies); [Adding a model answer to the GPT-4 prompt was counterproductive, lowering scoring reliabil](model-answer-in-prompt-lowered-reliability.md) (qualifies) |
| [Praveen Pathak 2026](https://doi.org/10.48550/arxiv.2608.20521) | q2 · design · r3 | i? | [The revised Round II grading workflow reduced AI over-awarding and total-score MAD, most c](revised-workflow-reduces-overawarding-mad.md) (qualifies) |
| [Cohn 2026](https://doi.org/10.48550/arxiv.2504.02323) | q1 · qualitative · r1 | i? | [Despite generally accurate feedback, the LLM's scoring explanations could be unpredictable](llm-logical-inconsistency-scoring-feedback.md) (supports) |
| Markus S. Feser & Paul L. Tschisgale 2026 | q3 · associational · r2 | i2 | [Lower linguistic quality of physics explanations is associated with higher odds that AI-ba](ai-scoring-underestimates-linguistically-weak-physics-explanations.md) (supports) |
| [Long DY 2026](https://doi.org/10.3389/feduc.2025.1648661) | q2 · review · r2 | i? | [In one reviewed study, GPT-4 automated essay scoring showed score inflation, with AI–human](gpt4-essay-score-inflation.md) (supports) |
| [floden](https://doi.org/10.51388/20.500.12265/293) | q2 · associational · r? | i? | [ChatGPT's exam scores were within 10% of human grades 70% of the time in a study of AI-bas](chatgpt-grading-within-10-percent-human.md) (qualifies) |
<!-- synthesis:end -->

## Discussion


## Related Claims
- [ChatGPT's exam scores were within 10% of human grades 70% of the time in a study of AI-based grading](chatgpt-grading-within-10-percent-human.md) — related
- [LLM-generated feedback is more comprehensive in volume than human feedback but is sometimes too generic, abstract, or misaligned with the assigned grade](llm-feedback-volume-vs-quality.md) — a narrower finding that bears on this claim
- LLM choice significantly influences human-AI coding correspondence, with Claude Sonnet 4 performing best and GPT 4.1 Mini worst — related
- [A short strict-grader preamble knocks 14 of 17 open-weights LLM graders out of the graded band on a computer-vision exam, with three stopping grading outright](llm-grader-strict-persona-collapse.md) — related
- [Purpose-built chatbot effects on educational performance are mixed, with some studies showing no benefits or worse outcomes than comparison conditions](educational-performance-mixed-ai-chatbots.md) — a broader claim this one bears on
- [LLMs perform worse on complex, open-ended, or subjective assignments than on short, clearly formulated answers](llm-struggle-open-ended-subjective-tasks.md) — related
- [AI scoring shows a systematic conservative bias, under-grading writing so 15.3% (2024) and 16.5% (2025) of human-passing tests would fail under AI scoring](ai-scoring-systematic-under-grading-bias-pass-fail.md) — related
- [Course Context Raised an LLM Grader's Agreement on Terse Answers and Lowered It on Long Ones](course-context-helps-sparse-items-and-dilutes-rich-ones.md) — related
- [In one study of five LLMs scoring 60 undergraduate essays on IELTS rubric dimensions, systematic underestimation of human scores was the dominant bias trend, with some models also compressing scores into a narrow range](llm-essay-scoring-systematic-underestimation.md) — related
- [Higher-scoring students tend to be more reliable graders (except the very best), and students are least biased when grading peers with similar scores](grader-grade-relates-to-grading-reliability.md) — related
- [In a self-referential framework, LLMs, particularly GPT-4.1, tend to outperform a single operational human rater at identifying relative weaknesses (negative feedback) across several Language and Content aspects](llms-outperform-single-rater-negative-feedback.md) — related
- [Newer LLM generations such as GPT-4 generally outperform GPT-3.5 in short-answer grading accuracy, but this advantage is not consistent across all tasks and domains](gpt4-advantage-uneven-across-tasks.md) — related
- [ChatGPT-3.5 feedback on EAP argumentative essays aligns closely with human instructor scoring and identifies surface-level issues, but is less effective on rhetorical structure and contextual nuance](chatgpt-feedback-aligns-with-human-scoring-but-weak-on-rhetorical-structure.md) — a narrower finding that bears on this claim
- [LLM Short-Answer Graders Agree With One Human Rater More, and the Other Less, Than the Two Raters Agree With Each Other](llm-short-answer-graders-can-reach-human-rater-agreement.md) — related
- [Sentence embedding models reach only moderate agreement and need human supervision for open-ended grading](embedding-models-moderate-agreement-need-supervision.md) — a narrower finding that bears on this claim
- [Newer LLM generations do not consistently agree better with human essay graders](no-consistent-generational-improvement-llm-grading.md) — related
- [LLMs overrate short underdeveloped essays and over-penalize minor language errors in well-developed essays](llm-overrate-short-essays-overpenalize-errors.md) — related
- [Claude3 and PaLM2 show substantial agreement but fall short on identifying failing grades](claude3-palm2-substantial-agreement-failing-grades.md) — related
- [Even the best LLM grader reaches only moderate agreement with human teachers, below the threshold for good reliability](llm-grading-moderate-human-agreement-icc.md) — related
- [Pooling Repeated LLM Grades Does Not Improve Agreement on Short Answers](pooling-repeated-llm-grades-does-not-improve-agreement.md) — a narrower finding that bears on this claim
