---
type: claim
title: "Bootstrapped self-consistency at temperature 1.0 flags potentially incorrect GPT-4 answers: about half of inconsistent responses were incorrect versus about 5% of consistent ones"
description: "Bootstrapped self-consistency at temperature 1.0 flags potentially incorrect GPT-4 answers: about half of inconsistent responses were incorrect versus about 5% of consistent ones"
id: bootstrapping-self-consistency-flags-incorrect-answers
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: joost-c-f-de-winter-2024
    resource: "https://doi.org/10.1007/s40593-023-00372-z"
    title: "Joost C. F. de Winter. (2024). Can ChatGPT Pass High School Exams on English Language Comprehension? International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00372-z"
    author: Joost C. F. de Winter
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# Bootstrapped self-consistency at temperature 1.0 flags potentially incorrect GPT-4 answers: about half of inconsistent responses were incorrect versus about 5% of consistent ones

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Over 50 repetitions per exam at temperature 1.0, GPT-4-0314 was inconsistent on 23 of 124 questions (43% of them incorrect) and GPT-4-0613 on 25 (56% incorrect), while only 4 of the consistent responses of each version were incorrect. [→ Joost C. F. de Winter 2024](#joost-c-f-de-winter-2024)

## Evidence

### Joost C. F. de Winter 2024

Joost C. F. de Winter. (2024). Can ChatGPT Pass High School Exams on English Language Comprehension? International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00372-z

`q3 · i?` · `design · r2`

Bootstrapping analysis submitting each exam to GPT-4 50 times (API 'n' parameter set to 50) at temperature 1.0, with answers classified as consistently correct, consistently incorrect, or inconsistent. Among inconsistent responses, "10 or 43% for GPT-4-0314; 14 or 56% for GPT-4-0613" were incorrect.

> "Our analysis showed that out of 124 questions across the three exams combined, GPT-4-0314 displayed inconsistency in 23 cases (19%), while GPT-4-0613 displayed inconsistency in 25 cases (20%)"

## Discussion


## Related Claims
- [GPT-4's March and June 2023 versions showed no notable overall difference on the English exams, but differed on individual questions](gpt4-march-june-versions-comparable-overall.md) — related
- [Self-consistency did not improve GPT-4's answer accuracy on these exams, unlike in chain-of-thought tasks](self-consistency-no-accuracy-gain-reading-exams.md) — related
- [Exam questions that GPT-4 answered inconsistently or incorrectly were harder for human examinees, who scored about 63–68% on them versus about 75% on the rest](gpt4-inconsistent-questions-harder-for-students.md) — related
- [GPT-3.5 passes Dutch VWO English reading comprehension exams with a mean grade of 7.3 with re-prompting, and 6.5 when only its first responses are scored](gpt35-passes-dutch-vwo-english-exams.md) — related
- [GPT-4 significantly outperforms the average Dutch student on VWO English reading comprehension, scoring 8.3 (March) and 8.1 (June) without re-prompting](gpt4-outperforms-average-student-english-exams.md) — related
- [The authors argue that LLMs such as GPT-3 threaten OBE validity by enabling answers without deep understanding, particularly in unproctored settings](llms-threaten-obe-validity-argument.md) — related
- [MELD analysis found no completion matched the MRCP sample paper at 95% or more, suggesting ChatGPT-4 was unlikely trained on it](meld-analysis-suggests-no-mrcp-training-data-memorisation.md) — related
- [ChatGPT versions were inconsistent, matching scores in all 3 runs for only 18% and 10% of encounters.](llm-inconsistent-across-runs.md) — related
- [GPT-4o was the most inconsistent chatbot, with 19 questions answered correctly in the first round answered incorrectly in the second](gpt-4o-most-inconsistent-across-rounds.md) — related
- [Temperature parameter has a statistically significant but negligible effect on GPT-4o exam accuracy (ηG² = 0.0017), with global accuracy peaking at temperature 0.23](temperature-effect-negligible-gpt4o-accuracy.md) — related
- [Concise, focused case summaries are associated with ChatGPT-4 reaching the correct diagnosis](concise-summaries-associated-correct-diagnosis.md) — related
- [Temperature settings (0.3, 0.6, 1.3) did not significantly affect GPT-4o accuracy on EUNACOM questions](temperature-no-effect-eunacom-accuracy.md) — related
- [LLMs can self-correct errors within a single session but revert to the original incorrect responses when the same questions are re-entered in a new session](llm-self-correction-does-not-persist-across-sessions.md) — related
- [ChatGPT 4.0 had the most uniquely correct and fewest uniquely incorrect responses among the three LLMs across both languages](chatgpt-4-most-unique-correct-responses-venn.md) — related
- [GPT-4 self-agreement between Korean and English versions is 72.6%, with correct answers derived only from English in 14.1% of cases](gpt4-self-agreement-korean-english-72-6-percent.md) — related
- [ChatGPT scored 47% on the first-semester final exam, with a realistic hand-graded score between 46% and 50%](chatgpt-exam-47-percent-no-dialogue.md) — related
- [Excluding zero-scoring answers, AI averages rise to 65.6% (GPT-4) and 56.7% (GPT-3.5), suggesting a use case for AI-provided hints](ai-hint-use-case-excluding-zero-scores.md) — related
- [ChatGPT based on GPT-4 solves the FCI accurately, scoring on average 83% correct](chatgpt-gpt4-solves-fci-accurately.md) — related
- [GPT-4 answers 65.8% of university assessment questions correctly by majority vote and can produce correct answers for 85.1% of questions with at least one prompting strategy](gpt4-answers-65-8-percent-majority-vote.md) — related
- [GPT-4 can override correct reasoning with default answers to technical physics questions, such as reverting to 9.81 m/s² for gravitational acceleration.](gpt4-default-answer-override.md) — related
- [GPT-4o's incorrect answers are far from random, gravitating toward specific incorrect answers](gpt4o-consistent-incorrect-answers.md) — related
- [GPT-5 Thinking scores 27/30 and 25/30 on the author's two comprehensive physics final exams, with errors clustered on ray tracing and circuit interpretation](gpt5-final-exam-scores-27-25-of-30.md) — related
- [A GPT-4o verification layer reduced the rate of incorrect feedback from 23% to 1.2% in the feedback-matching pipeline](gpt4o-verification-reduces-incorrect-feedback.md) — related
