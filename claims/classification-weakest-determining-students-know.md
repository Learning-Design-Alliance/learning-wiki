---
type: claim
title: Classification was weakest for the Determining What Students Know lesson, where zero-shot learning scored F1 0.66 and AUC 0.668
description: Classification was weakest for the Determining What Students Know lesson, where zero-shot learning scored F1 0.66 and AUC 0.668
id: classification-weakest-determining-students-know
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
---

# Classification was weakest for the Determining What Students Know lesson, where zero-shot learning scored F1 0.66 and AUC 0.668

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For Determining What Students Know, the zero-shot approach resulted in an F1 score of 0.66 and AUC of 0.668, the lowest across the three lessons, though its TNR of 0.828 was high. [→ Jionghao Lin 2024](#jionghao-lin-2024)

## Evidence

### Jionghao Lin 2024

Jionghao Lin, Zifei Han, Danielle R. Thomas, Ashish Gurung, Shivang Gupta, Vincent Aleven, Kenneth R. Koedinger. (2024). How Can I Get It Right? Using GPT to Rephrase Incorrect Trainee Responses. arXiv preprint. https://arxiv.org/abs/2405.00970

`q2 · i?` · `design · r2`

Results-section analysis of classifier performance on the Determining What Students Know lesson; zero-shot performance was lowest across lessons while the zero-shot model was "adept at identifying true negative cases".

> "the zero-shot learning approach resulted in an F1 score of 0.66 and AUC of 0.668, the lowest across the three lessons. Interestingly, the zero-shot model had a higher TNR score of 0.828"

## Discussion


## Related Claims
- [Few-shot learning with increasing shots generally improves GPT-4 classification performance, with the 5-shot variant strongest for Reacting to Errors (F1 0.867, AUC 0.866, TNR 0.83)](few-shot-shots-improve-classification.md) — related
- [A GPT-4 few-shot binary classifier effectively identifies correct/incorrect trainee responses across three tutor-training lessons, with average F1 of 0.84 and AUC of 0.85](gpt4-few-shot-classifies-trainee-responses.md) — a broader claim this one bears on
- [For Determining What Students Know, no significant difference in accuracy or responsiveness was found between GPT-4 and human rephrasings](gpt4-rephrasing-no-difference-determining-students-know.md) — related
