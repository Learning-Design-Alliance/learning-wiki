---
type: claim
title: Classifier errors cluster into three interpretable patterns, and the unknown abstention class is well classified (F1 = 0.93), reliably filtering off-topic chat
description: Classifier errors cluster into three interpretable patterns, and the unknown abstention class is well classified (F1 = 0.93), reliably filtering off-topic chat
id: classifier-error-patterns-and-abstention-f1
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: youssef-medhat-2026
    resource: "https://arxiv.org/abs/2606.10736"
    title: "Youssef Medhat, Junsoo Park, Ploy Thajchayapong and Ashok K. Goel. (2026). Detecting Knowledge Gaps from Conversational AI Interactions Using Curriculum Prerequisite Graphs. CSEDM'26: 10th Workshop on Computer Science Educational Data Mining. https://arxiv.org/abs/2606.10736"
    author: Youssef Medhat, Junsoo Park, Ploy Thajchayapong and Ashok K. Goel
    q: 2
    i: "?"
    kind: associational
    rigour: 1
  - id: youssef-medhat-2026-2
    resource: "https://arxiv.org/abs/2606.10736"
    title: "Youssef Medhat, Junsoo Park, Ploy Thajchayapong and Ashok K. Goel. (2026). Detecting Knowledge Gaps from Conversational AI Interactions Using Curriculum Prerequisite Graphs. CSEDM'26: 10th Workshop on Computer Science Educational Data Mining. https://arxiv.org/abs/2606.10736"
    author: Youssef Medhat, Junsoo Park, Ploy Thajchayapong and Ashok K. Goel
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Classifier errors cluster into three interpretable patterns, and the unknown abstention class is well classified (F1 = 0.93), reliably filtering off-topic chat

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1`–`r2` · `q2`

## Subclaims
`q2 i?` The 14 misclassified gold items cluster into surface-keyword traps (7/14), adjacent reasoning topics (5/14), and vague questions or abstention misfires (2/14). [→ Youssef Medhat 2026](#youssef-medhat-2026)
`q2 i?` The unknown abstention class dominates gold-set support (22/70 items) and is well classified at F1 = 0.93, confirming reliable filtering of off-topic chat. [→ Youssef Medhat 2026 (2)](#youssef-medhat-2026-2)

## Evidence

### Youssef Medhat 2026

Youssef Medhat, Junsoo Park, Ploy Thajchayapong and Ashok K. Goel. (2026). Detecting Knowledge Gaps from Conversational AI Interactions Using Curriculum Prerequisite Graphs. CSEDM'26: 10th Workshop on Computer Science Educational Data Mining. https://arxiv.org/abs/2606.10736

`q2 · i?` · `associational · r1`

Error analysis of the 14 misclassified gold items in the H1 evaluation section, identifying surface-keyword traps (7/14), adjacent reasoning topics (5/14), and vague questions or abstention misfires (2/14). The paper reports these as interpretable failure modes; no effect size is printed.

> "The 14 misclassified gold items cluster into three interpretable patterns:(i) Surface-keyword traps(7/14), where a strongly cued word pulls the prediction toward an unrelated topic"

### Youssef Medhat 2026 (2)

Youssef Medhat, Junsoo Park, Ploy Thajchayapong and Ashok K. Goel. (2026). Detecting Knowledge Gaps from Conversational AI Interactions Using Curriculum Prerequisite Graphs. CSEDM'26: 10th Workshop on Computer Science Educational Data Mining. https://arxiv.org/abs/2606.10736

`q2 · i?` · `associational · r2`

Per-topic performance analysis on the 70-question gold set: the abstention class accounts for 22/70 gold items with F1 = 0.93. Among substantive topics, Analogical Reasoning reaches F1 = 0.55 and Commonsense Reasoning F1 = 0.67, where most misclassifications concentrate. No effect size is printed.

> "The unknown abstention class dominates support (22/70 gold items) and is well classified (𝐹1 = 0.93 ), confirming that the model reliably filters off-topic chat"

## Discussion


## Related Claims
- [A few-shot FastFit classifier maps conversational AI teaching assistant questions to 43 curriculum topic labels with 80.0% accuracy on a 70-question gold set](fastfit-few-shot-topic-classification-80-accuracy.md) — related
- [The FastFit classifier slightly outperforms GPT-4 used directly under the same closed-label prompt on the same gold set (0.800 vs. 0.786 accuracy)](fastfit-outperforms-gpt4-direct-classification.md) — related
