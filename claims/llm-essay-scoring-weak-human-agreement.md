---
type: claim
title: Out-of-the-box LLMs agree with human essay grades far less than human raters agree with each other
description: Out-of-the-box LLMs agree with human essay grades far less than human raters agree with each other
id: llm-essay-scoring-weak-human-agreement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-10-20
recheck_by: 2029
sources:
  - id: jerin-george-mathew-2026
    resource: "https://doi.org/10.48550/arxiv.2603.23714"
    title: "Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa. (2026). LLMs Do Not Grade Essays Like Humans. https://arxiv.org/abs/2603.23714 [doi:10.48550/arxiv.2603.23714](https://doi.org/10.48550/arxiv.2603.23714)"
    author: Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Out-of-the-box LLMs agree with human essay grades far less than human raters agree with each other

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-20 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across ASAP and DREsS datasets, LLM-human score agreement (QWK below 0.30 on ASAP; at most 0.34 on DREsS) is substantially weaker than human inter-rater agreement (QWK 0.72). [→ Jerin George Mathew 2026](#jerin-george-mathew-2026)

## Evidence

### Jerin George Mathew 2026

Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa. (2026). LLMs Do Not Grade Essays Like Humans. https://arxiv.org/abs/2603.23714 [doi:10.48550/arxiv.2603.23714](https://doi.org/10.48550/arxiv.2603.23714)

`q2 · i?` · `associational · r2`

Evaluation of six GPT and Llama models prompted out-of-the-box to score essays on ASAP Tasks 1 and 7 and DREsS, compared against human ratings using QWK, Pearson correlation, and normalized MAE. Human raters reached "QW K= 0.72" while all LLMs stayed below 0.30 QWK on ASAP.

> "For the ASAP datasets, the agreement between the two human raters is relatively high (QW K= 0.72), indicating strong inter-rater reliability. In contrast, all LLMs achieve considerably lower agreement with human scores, with QWK values below 0.30 across models and tasks."

## Discussion

## Related Claims

- [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](llm-grading-mixed-against-human-raters.md) — the general claim this finding bears on, with the studies behind it
- [Newer LLM generations do not consistently agree better with human essay graders](no-consistent-generational-improvement-llm-grading.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [Few-shot prompting modestly improves LLM-human score agreement, inconsistently across datasets and models](few-shot-prompting-inconsistent-grading-gains.md) — related
- [Human inter-rater agreement on the writing rubric is imperfect: no rubric item reaches full agreement and the most discrepant rater generally falls below 80%](human-inter-rater-agreement-imperfect-upper-bound.md) — related
- [An LLM-based AI Evaluator agrees with expert human raters on collaboration transcripts at a level similar to inter-expert agreement](llm-evaluator-agreement-matches-expert-raters.md) — related
- [LLMs agree strongly with their own consensus grades (most ICC > 0.8), far more than with human teachers' grades](llm-high-consensus-agreement-circularity-risk.md) — related
- [Expert human raters established an inter-rater reliability benchmark above ICC 0.89 on all four IELTS dimensions for the essay corpus](human-inter-rater-benchmark-icc-above-089-essays.md) — related
- [AEEGS scores show high absolute agreement with 12 human expert raters' scores on mathematical Economics essay items (average-measures ICC = 0.863)](aeegs-high-agreement-human-raters-icc-0863.md) — related
- [LLM-based scoring of Spanish argumentative writing achieves 60–80% per-item accuracy, slightly below human inter-rater agreement](llm-scoring-spanish-writing-60-80-accuracy-below-human-agreement.md) — related
- [Human Graders of Open-Ended Work Agree With Each Other Less Than Treating One Grade as Ground Truth Implies](human-graders-agree-less-than-single-grade-ground-truth-implies.md) — related
- [Under single-pass deployment, Fs+CoT prompting yields the strongest agreement with teacher mean scores for music-analysis essay scoring (r = 0.795, ICC (2,1) = 0.657)](fscot-strongest-teacher-agreement-run1.md) — related
- [LLM ratings of classroom transcripts are more correlated with each other than with expert human ratings, across the same and different tasks](llm-llm-agreement-exceeds-llm-human-classroom-ratings.md) — a narrower finding that bears on this claim
- [LLM Short-Answer Graders Agree With One Human Rater More, and the Other Less, Than the Two Raters Agree With Each Other](llm-short-answer-graders-can-reach-human-rater-agreement.md) — a broader claim this one bears on
- [Claude3 and PaLM2 show substantial agreement but fall short on identifying failing grades](claude3-palm2-substantial-agreement-failing-grades.md) — reports the opposite
- [ASR-based item-level accuracy scores show moderate agreement with human raters in a Dutch word decoding and passage reading task](asr-accuracy-moderate-agreement-human-raters.md) — related
- [Feature-based MLP deep learning models predict ASAP D7 rubric scores with an average QWK of 0.72 against human raters' resolved scores, exceeding the 0.60 average agreement between the two human raters](aes-d7-rubric-qwk-072-exceeds-human-agreement.md) — related
- [ASAP contest performance comparisons across datasets were neither effective nor balanced because each dataset had a unique underlying writing construct; performance should be analyzed per writing task](asap-comparison-not-balanced-per-task.md) — related
- [The two human raters of ASAP D7 showed an average inter-rater agreement of 0.60 QWK across rubrics, with rubric-level agreements ranging from 0.46 (Ideas–Conventions) to 0.79 (Ideas–Organization)](d7-human-rater-agreement-qwk-060.md) — reports the opposite
- [LLMs can grade short-answer reading comprehension questions with accuracy comparable to human experts, supporting formative assessment grading](llm-grading-reading-comprehension-expert-comparable.md) — reports the opposite
