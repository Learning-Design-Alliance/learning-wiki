---
type: claim
title: "Weak supervision combined with model-assisted labeling cut expert annotators' labeling time by 70% while maintaining accuracy comparable to traditional labeling"
description: "Weak supervision combined with model-assisted labeling cut expert annotators' labeling time by 70% while maintaining accuracy comparable to traditional labeling"
id: weak-supervision-model-assisted-labeling-reduces-annotation-time
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
sources:
  - id: debajyoti-datta-2021
    resource: "https://doi.org/10.48550/arXiv.2112.00985"
    title: "Debajyoti Datta, Maria Phillips, James P Bywater, Jennifer Chiu, Ginger S. Watson, Laura E. Barnes, Donald E Brown. (2021). Evaluation of mathematical questioning strategies using data collected through weak supervision. NeurIPS 2021 Workshop on Math AI for Education (MATHAI4ED). [doi:10.48550/arXiv.2112.00985](https://doi.org/10.48550/arXiv.2112.00985)"
    author: Debajyoti Datta, Maria Phillips, James P Bywater, Jennifer Chiu, Ginger S. Watson, Laura E. Barnes, Donald E Brown
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Weak supervision combined with model-assisted labeling cut expert annotators' labeling time by 70% while maintaining accuracy comparable to traditional labeling

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Expert annotators using weak supervision plus model-assisted labeling took 70% less time to label data than with classical labeling, with annotator accuracy of 0.84 versus 0.82 and higher agreement (kappa 0.61 versus 0.52). [→ Debajyoti Datta 2021](#debajyoti-datta-2021)

## Evidence

### Debajyoti Datta 2021

Debajyoti Datta, Maria Phillips, James P Bywater, Jennifer Chiu, Ginger S. Watson, Laura E. Barnes, Donald E Brown. (2021). Evaluation of mathematical questioning strategies using data collected through weak supervision. NeurIPS 2021 Workshop on Math AI for Education (MATHAI4ED). [doi:10.48550/arXiv.2112.00985](https://doi.org/10.48550/arXiv.2112.00985)

`q2 · i?` · `design · r2`

Annotation comparison reported in Table 2 of the paper: classical labeling (n=1730 utterances, accuracy 0.82, kappa 0.52, mean time 15.2 seconds) versus weak supervision plus model-assisted labeling (n=3983, accuracy 0.84, kappa 0.61, model-assisted agreement 0.70, mean time 10.4 seconds). The paper states "expert annotators take 70% less time to label data."

> "Model-assisted labeling signiﬁcantly beneﬁts the annotation pipeline since expert annotators take 70% less time to label data."

## Discussion


## Related Claims
- [GPT-4o's final-turn correctness labeling on CoMTA is only slightly less accurate than expert human annotators, which the authors read as close to human-level performance on a challenging task.](gpt-4o-final-turn-correctness-labeling-is-close-to-human-level.md) — related
- [A few-shot FastFit classifier maps conversational AI teaching assistant questions to 43 curriculum topic labels with 80.0% accuracy on a 70-question gold set](fastfit-few-shot-topic-classification-80-accuracy.md) — related
- [Adding regex-based rules to few-shot LLM labeling improves agreement with human annotation (0.818 to 0.852 overall)](regex-rules-improve-fewshot-llm-labeling-accuracy.md) — related
