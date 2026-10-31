---
type: claim
title: Few-shot learning with increasing shots generally improves GPT-4 classification performance, with the 5-shot variant strongest for Reacting to Errors (F1 0.867, AUC 0.866, TNR 0.83)
description: Few-shot learning with increasing shots generally improves GPT-4 classification performance, with the 5-shot variant strongest for Reacting to Errors (F1 0.867, AUC 0.866, TNR 0.83)
id: few-shot-shots-improve-classification
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: jionghao-lin-2024
    resource: "https://arxiv.org/abs/2405.00970"
    title: "Jionghao Lin, Zifei Han, Danielle R. Thomas, Ashish Gurung, Shivang Gupta, Vincent Aleven, Kenneth R. Koedinger. (2024). How Can I Get It Right? Using GPT to Rephrase Incorrect Trainee Responses. arXiv preprint. https://arxiv.org/abs/2405.00970"
    author: Jionghao Lin, Zifei Han, Danielle R. Thomas, Ashish Gurung, Shivang Gupta, Vincent Aleven, Kenneth R. Koedinger
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: jionghao-lin-2024-2
    resource: "https://arxiv.org/abs/2405.00970"
    title: "Jionghao Lin, Zifei Han, Danielle R. Thomas, Ashish Gurung, Shivang Gupta, Vincent Aleven, Kenneth R. Koedinger. (2024). How Can I Get It Right? Using GPT to Rephrase Incorrect Trainee Responses. arXiv preprint. https://arxiv.org/abs/2405.00970"
    author: Jionghao Lin, Zifei Han, Danielle R. Thomas, Ashish Gurung, Shivang Gupta, Vincent Aleven, Kenneth R. Koedinger
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Few-shot learning with increasing shots generally improves GPT-4 classification performance, with the 5-shot variant strongest for Reacting to Errors (F1 0.867, AUC 0.866, TNR 0.83)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For Reacting to Errors, the 5-shot learning approach presented the highest F1, AUC, and TNR scores at 0.867, 0.866, and 0.83, respectively. [→ Jionghao Lin 2024](#jionghao-lin-2024)

## Evidence

### Jionghao Lin 2024

Jionghao Lin, Zifei Han, Danielle R. Thomas, Ashish Gurung, Shivang Gupta, Vincent Aleven, Kenneth R. Koedinger. (2024). How Can I Get It Right? Using GPT to Rephrase Incorrect Trainee Responses. arXiv preprint. https://arxiv.org/abs/2405.00970

`q2 · i?` · `design · r2`

Results section evaluation of zero-shot and 1-5-shot GPT-4 classifiers on the Reacting to Errors lesson responses; the 5-shot configuration achieved the reported "highest F1, AUC, and TNR scores".

> "When utilizing two-way few-shot learning approaches, the 5-shot learning approach presented the highest F1, AUC, and TNR scores at 0.867, 0.866, and 0.83, respectively."

### Jionghao Lin 2024 (2)

Jionghao Lin, Zifei Han, Danielle R. Thomas, Ashish Gurung, Shivang Gupta, Vincent Aleven, Kenneth R. Koedinger. (2024). How Can I Get It Right? Using GPT to Rephrase Incorrect Trainee Responses. arXiv preprint. https://arxiv.org/abs/2405.00970

`q2 · i?` · `design · r2`

Discussion-section interpretation of the Table 7 classification results across the three lessons; the authors state the few-shot approach "generally tends to improve" performance with increasing shots.

> "By comparing the classification performance with zero-shot learning, the few-shot learning approach, especially with increasing shots, generally tends to improve the model's classification performance."

## Discussion


## Related Claims
- [Classification was weakest for the Determining What Students Know lesson, where zero-shot learning scored F1 0.66 and AUC 0.668](classification-weakest-determining-students-know.md) — related
- [A GPT-4 few-shot binary classifier effectively identifies correct/incorrect trainee responses across three tutor-training lessons, with average F1 of 0.84 and AUC of 0.85](gpt4-few-shot-classifies-trainee-responses.md) — a broader claim this one bears on
- [In-context examples improve LLM Bloom classification: three-shot and ten-shot prompting score at or above zero-shot on every dataset tested, and above it in most comparisons](in-context-examples-improve-bloom-classification.md) — a broader claim this one bears on
- [For Reacting to Errors, GPT-4 rephrasings were rated more accurate than human rephrasings (few-shot p < 0.01, zero-shot p < 0.05) with no significant responsiveness difference](gpt4-rephrasing-reacting-to-errors-accuracy.md) — related
