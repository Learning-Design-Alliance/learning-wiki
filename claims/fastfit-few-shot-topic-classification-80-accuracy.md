---
type: claim
title: "A few-shot FastFit classifier maps conversational AI teaching assistant questions to 43 curriculum topic labels with 80.0% accuracy on a 70-question gold set"
description: "A few-shot FastFit classifier maps conversational AI teaching assistant questions to 43 curriculum topic labels with 80.0% accuracy on a 70-question gold set"
id: fastfit-few-shot-topic-classification-80-accuracy
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: youssef-medhat-2026
    resource: "https://arxiv.org/abs/2606.10736"
    title: "Youssef Medhat, Junsoo Park, Ploy Thajchayapong and Ashok K. Goel. (2026). Detecting Knowledge Gaps from Conversational AI Interactions Using Curriculum Prerequisite Graphs. CSEDM'26: 10th Workshop on Computer Science Educational Data Mining. https://arxiv.org/abs/2606.10736"
    author: Youssef Medhat, Junsoo Park, Ploy Thajchayapong and Ashok K. Goel
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A few-shot FastFit classifier maps conversational AI teaching assistant questions to 43 curriculum topic labels with 80.0% accuracy on a 70-question gold set

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` A FastFit classifier trained on 1,046 LLM-labeled questions achieves 80.0% accuracy and macro F1 = 0.669 on a human-annotated 70-question gold set with a 43-class label space. [→ Youssef Medhat 2026](#youssef-medhat-2026)

## Evidence

### Youssef Medhat 2026

Youssef Medhat, Junsoo Park, Ploy Thajchayapong and Ashok K. Goel. (2026). Detecting Knowledge Gaps from Conversational AI Interactions Using Curriculum Prerequisite Graphs. CSEDM'26: 10th Workshop on Computer Science Educational Data Mining. https://arxiv.org/abs/2606.10736

`q2 · i?` · `design · r2`

Evaluation of the FastFit classifier on a 70-question gold set labeled by a course teaching assistant using the course textbook as ground truth, in a 43-class label space. The paper reports "80.0% accuracy across 43 labels" and macro F1 = 0.669 (weighted F1: 0.856). No effect size is printed.

> "Evaluated on 1,340 question events from 164 students in a graduate-level AI course, our classifier achieves 80.0% accuracy across 43 labels (42 curriculum topics plus an “unknown” abstention class)."

## Discussion


## Related Claims
- [Classifier errors cluster into three interpretable patterns, and the unknown abstention class is well classified (F1 = 0.93), reliably filtering off-topic chat](classifier-error-patterns-and-abstention-f1.md) — related
- [The FastFit classifier slightly outperforms GPT-4 used directly under the same closed-label prompt on the same gold set (0.800 vs. 0.786 accuracy)](fastfit-outperforms-gpt4-direct-classification.md) — possibly the same claim (merge candidate)
