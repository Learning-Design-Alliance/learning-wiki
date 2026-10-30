---
type: claim
title: Demographic disparities in automatic scoring are concentrated at the item level, tied to class distributions and item difficulty
description: Demographic disparities in automatic scoring are concentrated at the item level, tied to class distributions and item difficulty
id: item-level-disparity-class-distribution-difficulty
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: nico-andersen-2025
    resource: "https://doi.org/10.1007/s40593-025-00495-5"
    title: "Nico Andersen, Julia Mang, Frank Goldhammer, Fabian Zehner. (2025). Algorithmic Fairness in Automatic Short Answer Scoring. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00495-5"
    author: Nico Andersen, Julia Mang, Frank Goldhammer, Fabian Zehner
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: nico-andersen-2025-2
    resource: "https://doi.org/10.1007/s40593-025-00495-5"
    title: "Nico Andersen, Julia Mang, Frank Goldhammer, Fabian Zehner. (2025). Algorithmic Fairness in Automatic Short Answer Scoring. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00495-5"
    author: Nico Andersen, Julia Mang, Frank Goldhammer, Fabian Zehner
    q: 2
    i: "?"
    kind: associational
    rigour: 3
---

# Demographic disparities in automatic scoring are concentrated at the item level, tied to class distributions and item difficulty

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2`–`r3` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` At the item level, significant demographic disparities appeared on a minority of items (four for gender, favoring girls and boys two each; several for language, favoring foreign speakers), concentrated around easier items for language groups. [→ Nico Andersen 2025](#nico-andersen-2025)
`q2 i?` On item R219Q02 the classifier recognized all correct responses (TPR = 1) but almost no incorrect ones (FPR = .85), so the group with more incorrect responses (boys, Y = .82 vs. girls' Y = .90) was favored more. [→ Nico Andersen 2025 (2)](#nico-andersen-2025-2)

## Evidence

### Nico Andersen 2025

Nico Andersen, Julia Mang, Frank Goldhammer, Fabian Zehner. (2025). Algorithmic Fairness in Automatic Short Answer Scoring. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00495-5

`q2 · i?` · `associational · r2`

Item-level analysis (RQ2) of scoring bias D and disparity DD per item for the RoBERTa-SVM, illustrated in Figs. 3 and 4. Significant gender differences were distributed across items of intermediate and low difficulty; language disparities centered around easier items.

> "Concerning gender, there were four items with a significant demographic disparity. Two items favored girls and two favored boys."

### Nico Andersen 2025 (2)

Nico Andersen, Julia Mang, Frank Goldhammer, Fabian Zehner. (2025). Algorithmic Fairness in Automatic Short Answer Scoring. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00495-5

`q2 · i?` · `associational · r3`

Case analysis of item R219Q02 from the appendix item metrics: scoring accuracy was identical for both groups, but incorrect responses were substantially more frequent for boys (Y = .82 vs. .90 for girls), so the high FPR favored boys, overestimating both groups but substantially higher in boys.

> "Particularly striking were the metrics for the significant item R219Q02—with TPRR219Q02 =1 and FPRR219Q02 = .85—for which the classifier recognized all correct responses as such but recognized almost no incorrect ones and, accordingly, falsely scored them as positives."

## Discussion


## Related Claims
- [The most accurate scorer showed no gender disparity but a small significant language-background disparity favoring foreign-language speakers](language-bias-favors-foreign-speakers-roberta-svm.md) — related
