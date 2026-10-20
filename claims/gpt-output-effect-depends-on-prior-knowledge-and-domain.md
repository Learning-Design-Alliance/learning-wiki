---
type: claim
title: Descriptive user-study patterns that the authors read as GPT output possibly scaffolding IVDA students and reducing CV students' performance, an interpretation by prior knowledge that the study did not measure
description: Descriptive user-study patterns that the authors read as GPT output possibly scaffolding IVDA students and reducing CV students' performance, an interpretation by prior knowledge that the study did not measure
id: gpt-output-effect-depends-on-prior-knowledge-and-domain
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: markos-stamatakis-2026
    resource: "https://doi.org/10.48550/arxiv.2606.15919"
    title: "Markos Stamatakis, Omkar Gavali, Joshua Berger, Christian Wartena, Anett Hoppe, and Ralph Ewerth. (2026). Are LLM-based Chatbots Good Enough to Support Computer Science Students in Multiple-Choice Exercises? https://arxiv.org/abs/2606.15919 [doi:10.48550/arxiv.2606.15919](https://doi.org/10.48550/arxiv.2606.15919)"
    author: Markos Stamatakis, Omkar Gavali, Joshua Berger, Christian Wartena, Anett Hoppe, and Ralph Ewerth
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: markos-stamatakis-2026-2
    resource: "https://arxiv.org/abs/2606.15919"
    title: "Markos Stamatakis, Omkar Gavali, Joshua Berger, Christian Wartena, Anett Hoppe, and Ralph Ewerth. (2026). Are LLM-based Chatbots Good Enough to Support Computer Science Students in Multiple-Choice Exercises? https://arxiv.org/abs/2606.15919"
    author: Markos Stamatakis, Omkar Gavali, Joshua Berger, Christian Wartena, Anett Hoppe, and Ralph Ewerth
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Descriptive user-study patterns that the authors read as GPT output possibly scaffolding IVDA students and reducing CV students' performance, an interpretation by prior knowledge that the study did not measure

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` In the IVDA scenario, 63.64% of Group 3 (test first without, then with GPT output) improved between attempts, while 80% of Group 1 and 60% of Group 2 showed unchanged performance (Table 5; the text says about 80% for both). [→ Markos Stamatakis 2026](#markos-stamatakis-2026)
`q2 i?` In the CV scenario the average student outperforms GPT-4o in all attempts, and the authors suggest GPT-4o outputs may reduce performance when prior knowledge is higher; prior knowledge was not measured, so this is their interpretation of the CV/IVDA difference, not a tested finding. [→ Markos Stamatakis 2026 (2)](#markos-stamatakis-2026-2)

## Evidence

### Markos Stamatakis 2026

Markos Stamatakis, Omkar Gavali, Joshua Berger, Christian Wartena, Anett Hoppe, and Ralph Ewerth. (2026). Are LLM-based Chatbots Good Enough to Support Computer Science Students in Multiple-Choice Exercises? https://arxiv.org/abs/2606.15919 [doi:10.48550/arxiv.2606.15919](https://doi.org/10.48550/arxiv.2606.15919)

`q2 · i?` · `causal · r2`

Descriptive change analysis between attempts (Table 5, Sec. 5) for the IVDA user study: "63.64 %of Group 3 improved, while18.18 %performed worse", while Table 5 shows 80% of Group 1 and 60% of Group 2 unchanged (the prose says about 80% for both). Descriptive percentages only; no test statistic or effect size.

> "In the IVDAscenario, 63.64 %of Group 3 improved, while18.18 %performed worse."

### Markos Stamatakis 2026 (2)

Markos Stamatakis, Omkar Gavali, Joshua Berger, Christian Wartena, Anett Hoppe, and Ralph Ewerth. (2026). Are LLM-based Chatbots Good Enough to Support Computer Science Students in Multiple-Choice Exercises? https://arxiv.org/abs/2606.15919

`q2 · i?` · `causal · r2`

Descriptive comparison of CV participants with GPT-4o (Table 4, Sec. 5): "the average student outperforms GPT in all attempts", similarity to GPT-4o output always over 80%, and Group 3 declined in the second attempt. The authors interpret this as possible cognitive offloading with higher prior knowledge, but the study did not measure prior knowledge or analyse students by it; no effect size printed.

> "In the CV scenario, the average student outperforms GPT in all attempts, with many achieving comparable or higher scores."

## Discussion

## Learner Variables
- [Prior Knowledge](../learner-variables/prior-knowledge.md) — moderator: an instructional effect differs with it

## Related Claims

- [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](expertise-reversal-effect.md) — the general claim this finding bears on, with the studies behind it

- [How genAI is used, not who uses it, predicts whether independent performance declines or improves](persistence-costs-concentrated-among-direct-solution-users.md) — the general claim this finding bears on, with the studies behind it
- [GPT-4o and GPT-5.2 achieve higher accuracy and more fully correct answers on university IVDA multiple-choice questions than the smaller Mistral-7B and DeepSeek-R1 models](gpt-models-outperform-smaller-llms-on-ivda-mcqs.md) — related
- [In a two-lecture user study, linear mixed models find no statistically significant effect of GPT-generated output on student MCQ performance, with a tendency toward a group-by-attempt interaction for IVDA](no-significant-lmm-effect-of-gpt-output-on-student-scores.md) — related
- [Across three physics assessments, students who declared GenAI use scored slightly higher than non-users, but none of the differences were statistically significant](genai-users-slightly-higher-scores-not-significant-physics.md) — related
- [Reviews citing one randomised trial (Bastani et al. 2025) report that unrestricted GPT-4 access in high-school mathematics raised assisted practice performance but left students worse off after withdrawal](gpt4-access-harms-learning-after-withdrawal.md) — related
