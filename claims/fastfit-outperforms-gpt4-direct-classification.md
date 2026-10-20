---
type: claim
title: The FastFit classifier slightly outperforms GPT-4 used directly under the same closed-label prompt on the same gold set (0.800 vs. 0.786 accuracy)
description: The FastFit classifier slightly outperforms GPT-4 used directly under the same closed-label prompt on the same gold set (0.800 vs.
id: fastfit-outperforms-gpt4-direct-classification
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: youssef-medhat-2026
    resource: "https://doi.org/10.48550/arxiv.2606.10736"
    title: "Youssef Medhat, Junsoo Park, Ploy Thajchayapong and Ashok K. Goel. (2026). Detecting Knowledge Gaps from Conversational AI Interactions Using Curriculum Prerequisite Graphs. CSEDM'26: 10th Workshop on Computer Science Educational Data Mining. https://arxiv.org/abs/2606.10736 [doi:10.48550/arxiv.2606.10736](https://doi.org/10.48550/arxiv.2606.10736)"
    author: Youssef Medhat, Junsoo Park, Ploy Thajchayapong and Ashok K. Goel
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The FastFit classifier slightly outperforms GPT-4 used directly under the same closed-label prompt on the same gold set (0.800 vs. 0.786 accuracy)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On the same 70-question gold set with the same 43-class label space, FastFit scores 0.800 accuracy / 0.669 macro F1, slightly above GPT-4 direct's 0.786 / 0.654. [→ Youssef Medhat 2026](#youssef-medhat-2026)

## Evidence

### Youssef Medhat 2026

Youssef Medhat, Junsoo Park, Ploy Thajchayapong and Ashok K. Goel. (2026). Detecting Knowledge Gaps from Conversational AI Interactions Using Curriculum Prerequisite Graphs. CSEDM'26: 10th Workshop on Computer Science Educational Data Mining. https://arxiv.org/abs/2606.10736 [doi:10.48550/arxiv.2606.10736](https://doi.org/10.48550/arxiv.2606.10736)

`q2 · i?` · `design · r2`

Comparison in the Method section (Table 1) of GPT-4 applied directly at inference time as a baseline versus the pipeline's FastFit classifier on the same gold set. The paper reports FastFit "slightly under" reversed: GPT-4 direct scores "0.786 accuracy / 0.654 macro F1" versus FastFit's 0.800/0.669. No significance test is printed.

> "on the same 70-question gold set with the same 43-class label space, GPT-4 used directly under the same closed-label prompt scores 0.786 accuracy / 0.654 macro F1, slightly under FastFit’s 0.800/0.669 (Table 1)."

## Discussion


## Related Claims

- [Classifier errors cluster into three interpretable patterns, and the unknown abstention class is well classified (F1 = 0.93), reliably filtering off-topic chat](classifier-error-patterns-and-abstention-f1.md) — related
- [A few-shot FastFit classifier maps conversational AI teaching assistant questions to 43 curriculum topic labels with 80.0% accuracy on a 70-question gold set](fastfit-few-shot-topic-classification-80-accuracy.md) — possibly the same claim (merge candidate)
- [Adding regex-based rules to few-shot LLM labeling improves agreement with human annotation (0.818 to 0.852 overall)](regex-rules-improve-fewshot-llm-labeling-accuracy.md) — related
