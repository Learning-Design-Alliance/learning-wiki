---
type: research-method
id: two-phase-cross-prompt-pre-finetuning-approach-for-automated-short-answer-scoring
title: Two-phase cross-prompt pre-finetuning approach for automated short answer scoring
description: "A training framework in which an SAS model is first pre-finetuned on already annotated prompts using rubric key phrases concatenated with each answer, so it learns \"the task's general property (i.e., a principle of scoring): an answer receives a high score if it contains the information speciﬁed by "
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-28
---

# Two-phase cross-prompt pre-finetuning approach for automated short answer scoring

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 causal), `q2` · 1 of 1 report an effect size · 3 claims rest on one study

## Description
A training framework in which an SAS model is first pre-finetuned on already annotated prompts using rubric key phrases concatenated with each answer, so it learns "the task's general property (i.e., a principle of scoring): an answer receives a high score if it contains the information speciﬁed by the rubric." The pre-finetuned model is then finetuned on a new target prompt without requiring access to the cross-prompt data, resolving data accessibility because the second phase "needs access to only the parameters of the pre-ﬁnetuned model." The approach was instantiated with both a BERT regression model and open-source LLMs.

## Accounts
<!-- How each source describes or uses the method -->
- **Two-phase cross-prompt pre-finetuning approach for automated short answer scoring**: A training framework in which an SAS model is first pre-finetuned on already annotated prompts using rubric key phrases concatenated with each answer, so it learns "the task's general property (i.e., a principle of scoring): an answer receives a high score if it contains the information speciﬁed by the rubric." The pre-finetuned model is then finetuned on a new target prompt without requiring access to the cross-prompt data, resolving data accessibility because the second phase "needs access to only the parameters of the pre-ﬁnetuned model." The approach was instantiated with both a BERT regression model and open-source LLMs. (Funayama et al. (2025))

### Claims
- [Two-phase cross-prompt pre-finetuning with key phrases significantly improves short answer scoring accuracy when in-prompt training data is limited](../claims/cross-prompt-prefinetuning-key-phrases-low-resource-gain.md) [+M]
- [Pre-finetuning without key phrases does not improve scoring performance and slightly lowers it relative to the BERT baseline](../claims/prefinetuning-without-key-phrases-no-gain.md) [+M]
- [The pre-finetuned model learns a scoring principle: predicted scores correlate strongly and negatively with edit distance between answers and key phrases](../claims/model-learns-scoring-principle-key-phrase-similarity.md) [+M]

## Related Research Methods
-

## Key Sources
- Funayama, H., Matsubayashi, Y., Asazuma, Y., Mizumoto, T., & Inui, K. (2025). Cross-prompt Pre-finetuning of Language Models for Short Answer Scoring. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00474-w
