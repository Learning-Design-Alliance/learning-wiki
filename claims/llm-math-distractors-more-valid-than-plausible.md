---
type: claim
title: LLM-generated distractors for math multiple-choice questions are judged mathematically valid more often than plausible to students, and rarely reproduce the full set of human-written distractors
description: On Eedi math MCQs, the best LLM method matched all three human-authored distractors on 10.95% of test questions, and teacher-raters scored LLM distractors below human ones, with a larger gap for plausibility (2.68 vs 3.72) than validity (3.28 vs 3.99).
id: llm-math-distractors-more-valid-than-plausible
status: review
generated:
  by: claude/unspecified
  at: 2026-10-21
evidence_strength: weak
newest_evidence: 2024
sources:
  - id: feng-2024
    resource: "https://doi.org/10.18653/v1/2024.findings-naacl.193"
    title: "Feng, W., Lee, J., McNichols, H., Scarlatos, A., Smith, D., Woodhead, S., Ornelas, N. O., & Lan, A. (2024). Exploring automated distractor generation for math multiple-choice questions via large language models. In *Findings of the Association for Computational Linguistics: NAACL 2024* (pp. 3067–3082). [doi:10.18653/v1/2024.findings-naacl.193](https://doi.org/10.18653/v1/2024.findings-naacl.193)"
    author: "Feng, W., Lee, J., McNichols, H., Scarlatos, A., Smith, D., Woodhead, S., Ornelas, N. O., & Lan, A."
    q: 2
    i: "?"
    n: "1.4K MCQs (80:20 train/test split); 20 test MCQs rated by 2 evaluators"
    kind: design
    rigour: 2
---

# LLM-generated distractors for math multiple-choice questions are judged mathematically valid more often than plausible to students, and rarely reproduce the full set of human-written distractors

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · n=1.4K MCQs (80:20 train/test split); 20 test MCQs rated by 2 evaluators
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

A distractor that can be reached by some wrong reasoning is not the same as one that real students choose. Large language models produce the first more readily than the second.

## Subclaims

`q2 i?` Of five LLM approaches on a test set drawn from 1.4K Eedi math MCQs (pupils aged about 10–13), in-context learning with nearest-neighbour examples did best, yet its three generated distractors all matched the three human-authored ones on only 10.95% of questions (at least one matched on 73.85%; 38.52% of distractors matched). [→ Feng 2024](#feng-2024)

`q2 i?` Two graduate students with math-teaching experience rated LLM distractors below human-authored ones on mathematical validity (3.28 vs 3.99 on a 1–5 scale) and on plausibility to middle-school students (2.68 vs 3.72), both differences significant (p < 0.05), with the gap larger for plausibility. [→ Feng 2024](#feng-2024)

## Evidence

### Feng 2024

Feng, W., Lee, J., McNichols, H., Scarlatos, A., Smith, D., Woodhead, S., Ornelas, N. O., & Lan, A. (2024). Exploring automated distractor generation for math multiple-choice questions via large language models. In *Findings of the Association for Computational Linguistics: NAACL 2024* (pp. 3067–3082). [doi:10.18653/v1/2024.findings-naacl.193](https://doi.org/10.18653/v1/2024.findings-naacl.193)

`q2 · comparison of generation methods with blinded human rating` · `i? · means and p-values printed, no standardised effect size` · `n=1.4K MCQs (80:20 train/test split); 20 test MCQs rated by 2 evaluators` · `design · r2`

The study compares in-context learning (kNN example selection, chain-of-thought, rule-based), fine-tuning and a sampling baseline for generating three distractors per MCQ, scored by exact string match against the human-authored distractors. Each MCQ's human distractors were written to target common errors or misconceptions and come with the share of students (an average of about 4,000 responses per question) choosing each option. In the human evaluation, raters saw human and LLM distractors mixed in random order for 20 randomly sampled test questions; agreement between the two raters was fair to moderate (QWK 0.23–0.54). The authors conclude that the LLMs "can generate some mathematically valid distractors" but "are less adept at anticipating common errors or misconceptions among real students". Read from the full text.

## Discussion

The rating sample is small (20 questions, two raters with modest agreement), and exact string matching undercounts distractors that are plausible but different from the human ones, which the authors acknowledge. The direction of the result, valid more often than plausible, is the point for design: an LLM can supply the shape of an error without knowing which errors students actually make, which fits the finding that misconceptions are population- and context-specific ([Payne & Squibb 1990](algebra-mal-rules-are-unstable-skewed-and-school-specific.md)). Distractors that track real student ideas carry diagnostic information that conventional distractors do not ([Sadler 1998](instruction-can-raise-attraction-to-alternative-conceptions-before-decline.md)).

## Related Claims
- [LLMs' generation probabilities for multiple-choice distractors correlate moderately with how often students choose them](llm-distractor-likelihood-moderately-tracks-student-choices.md) — related
- [Chain-of-thought and reasoning prompting significantly improve LLM proportional match with human-authored distractors over direct prompting on both math and science MCQs](reasoning-prompting-improves-llm-distractor-match.md) — related
- [LLMs predict common distractors above chance but fall 15 percentage points below chance at predicting which errors students rarely select](llm-distractor-prediction-asymmetry.md) — related
- [On distractor-driven science items, instruction can first strengthen students' attraction to an alternative conception before that preference declines](instruction-can-raise-attraction-to-alternative-conceptions-before-decline.md) — related
- [Distractor similarity to the correct answer increases MCQ complexity](distractor-similarity-increases-complexity.md) — related
