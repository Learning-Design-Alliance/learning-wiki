---
type: claim
title: In a two-lecture user study, linear mixed models find no statistically significant effect of GPT-generated output on student MCQ performance, with a tendency toward a group-by-attempt interaction for IVDA
description: In a two-lecture user study, linear mixed models find no statistically significant effect of GPT-generated output on student MCQ performance, with a tendency toward a group-by-attempt interaction for IVDA
id: no-significant-lmm-effect-of-gpt-output-on-student-scores
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

# In a two-lecture user study, linear mixed models find no statistically significant effect of GPT-generated output on student MCQ performance, with a tendency toward a group-by-attempt interaction for IVDA

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` Based on likelihood-ratio tests, no fixed effects (attempt, group, group × attempt) are significant at α = 0.05 in either the IVDA or CV scenario. [→ Markos Stamatakis 2026](#markos-stamatakis-2026)
`q2 i?` For IVDA-MCQs the interaction effect approaches significance (LRT p = 0.058), indicating a tendency toward different performance changes between groups. [→ Markos Stamatakis 2026 (2)](#markos-stamatakis-2026-2)

## Evidence

### Markos Stamatakis 2026

Markos Stamatakis, Omkar Gavali, Joshua Berger, Christian Wartena, Anett Hoppe, and Ralph Ewerth. (2026). Are LLM-based Chatbots Good Enough to Support Computer Science Students in Multiple-Choice Exercises? https://arxiv.org/abs/2606.15919 [doi:10.48550/arxiv.2606.15919](https://doi.org/10.48550/arxiv.2606.15919)

`q2 · i?` · `causal · r2`

Linear mixed model analysis (Score ~ Group * Attempt + (1|Participant)) of user-study scores in both scenarios (Table 6, Sec. 5). The article reports "no fixed effects are significant atα= 0.05" under LRT; equivalence was not tested. No effect size printed.

> "Based on LRT, no fixed effects are significant atα= 0.05, suggesting no attempt-dependent performance differences between experimental conditions."

### Markos Stamatakis 2026 (2)

Markos Stamatakis, Omkar Gavali, Joshua Berger, Christian Wartena, Anett Hoppe, and Ralph Ewerth. (2026). Are LLM-based Chatbots Good Enough to Support Computer Science Students in Multiple-Choice Exercises? https://arxiv.org/abs/2606.15919

`q2 · i?` · `causal · r2`

LMM interaction test for the IVDA scenario (Table 6, Sec. 5): the group × attempt effect approaches significance with p = 0.058. Under Wald χ2 tests the IVDA interaction (p = 0.046) and CV group effect (p = 0.041) are significant, so evidence is mixed; the article motivates larger studies.

> "For IVDA-MCQs, the interaction effect (H3) approaches significance (p= 0.058), indicating a tendency toward different performance changes between the groups, as reflected in Group 3."

## Discussion


## Related Claims
- [GPT-4o and GPT-5.2 achieve higher accuracy and more fully correct answers on university IVDA multiple-choice questions than the smaller Mistral-7B and DeepSeek-R1 models](gpt-models-outperform-smaller-llms-on-ivda-mcqs.md) — related
- [Descriptive user-study patterns suggest GPT output may scaffold lower-prior-knowledge IVDA students but reduce performance when prior knowledge is higher (CV)](gpt-output-effect-depends-on-prior-knowledge-and-domain.md) — related
- [Model and student error patterns on IVDA MCQs show limited question-level consistency but comparable difficulty distributions for easiest and hardest questions](limited-model-student-question-level-alignment.md) — related
- [MCQ accuracy was high (above 87%) across all conditions with no significant difference between diverse and generic explanations](mcq-accuracy-no-significant-condition-difference.md) — related
- [Students perceive LLM chatbots as useful for learning but requiring critical use, reporting hallucinations, overconfidence, and dependency risks](students-view-llms-useful-but-requiring-critical-use.md) — related
