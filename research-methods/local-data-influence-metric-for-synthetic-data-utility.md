---
type: research-method
id: local-data-influence-metric-for-synthetic-data-utility
title: Local data influence metric for synthetic data utility
description: "Local data influence is the framework's measure of a synthetic data point's utility: the change in the student model's reference loss before and after one-step training on that point, approximating influence functions locally following Yu et al."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
---

# Local data influence metric for synthetic data utility

> **Research Method** · [All research methods](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Local data influence is the framework's measure of a synthetic data point's utility: the change in the student model's reference loss before and after one-step training on that point, approximating influence functions locally following Yu et al. (2024b). It is used to characterize the student's learning preferences and to construct the preference dataset for DPO. The article defines that "A positive Im indicates that the data benefits the student's reference performance, while a negative Im shows the opposite", with a theoretical derivation in Appendix B.

## Accounts
<!-- How each source describes or uses the method -->
- **Local data influence metric for measuring synthetic data utility to a student model**: Local data influence is the framework's measure of a synthetic data point's utility: the change in the student model's reference loss before and after one-step training on that point, approximating influence functions locally following Yu et al. (2024b). It is used to characterize the student's learning preferences and to construct the preference dataset for DPO. The article defines that "A positive Im indicates that the data benefits the student's reference performance, while a negative Im shows the opposite", with a theoretical derivation in Appendix B. (Xiaochuan Li et al. (2024))

### Claims
- [Local data influence captures student data preferences better than LLM-as-a-Judge or training loss, and optimizing the teacher beats bootstrapping](../claims/local-influence-and-teacher-optimization-ablations.md) [+M]

## Related Research Methods
-

## Key Sources
- Xiaochuan Li, Zichun Yu, Chenyan Xiong. (2024). MONTESSORI-INSTRUCT: GENERATE INFLUENTIAL TRAINING DATA TAILORED FOR STUDENT LEARNING. Preprint. https://arxiv.org/abs/2410.14208
