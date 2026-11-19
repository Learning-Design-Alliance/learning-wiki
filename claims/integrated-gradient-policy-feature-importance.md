---
type: claim
title: "Integrated-gradient analysis found pretest score and math anxiety were the most influential features on the learned policy's pedagogical choices"
description: "Integrated-gradient analysis found pretest score and math anxiety were the most influential features on the learned policy's pedagogical choices"
id: integrated-gradient-policy-feature-importance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2024
sources:
  - id: sherry-ruan-2024
    resource: "https://doi.org/10.1007/s10994-023-06423-9"
    title: "Sherry Ruan, Allen Nie, William Steenbergen, Jiayu He, JQ Zhang, Meng Guo, Yao Liu, Kyle Dang Nguyen, Catherine Y Wang, Rui Ying, James A Landay, Emma Brunskill. (2024). Reinforcement Learning Tutor Better Supported Lower Performers in a Math Task. Originally published 2023. [doi:10.1007/s10994-023-06423-9](https://doi.org/10.1007/s10994-023-06423-9)"
    author: Sherry Ruan, Allen Nie, William Steenbergen, Jiayu He, JQ Zhang, Meng Guo, Yao Liu, Kyle Dang Nguyen, Catherine Y Wang, Rui Ying, James A Landay, Emma Brunskill
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: sherry-ruan-2024-2
    resource: "https://doi.org/10.1007/s10994-023-06423-9"
    title: "Sherry Ruan, Allen Nie, William Steenbergen, Jiayu He, JQ Zhang, Meng Guo, Yao Liu, Kyle Dang Nguyen, Catherine Y Wang, Rui Ying, James A Landay, Emma Brunskill. (2024). Reinforcement Learning Tutor Better Supported Lower Performers in a Math Task. Originally published 2023. [doi:10.1007/s10994-023-06423-9](https://doi.org/10.1007/s10994-023-06423-9)"
    author: Sherry Ruan, Allen Nie, William Steenbergen, Jiayu He, JQ Zhang, Meng Guo, Yao Liu, Kyle Dang Nguyen, Catherine Y Wang, Rui Ying, James A Landay, Emma Brunskill
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Integrated-gradient analysis found pretest score and math anxiety were the most influential features on the learned policy's pedagogical choices

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Integrated-gradient attribution on the study 2 distilled policy identified pretest score and math anxiety score as the most influential contextual features; other student features had little to no effect. [→ Sherry Ruan 2024](#sherry-ruan-2024)
`q2 i?` Students with higher pretest scores were more likely to receive direct hints, while low-performing, higher math-anxiety students received more guided prompts. [→ Sherry Ruan 2024 (2)](#sherry-ruan-2024-2)

## Evidence

### Sherry Ruan 2024

Sherry Ruan, Allen Nie, William Steenbergen, Jiayu He, JQ Zhang, Meng Guo, Yao Liu, Kyle Dang Nguyen, Catherine Y Wang, Rui Ying, James A Landay, Emma Brunskill. (2024). Reinforcement Learning Tutor Better Supported Lower Performers in a Math Task. Originally published 2023. [doi:10.1007/s10994-023-06423-9](https://doi.org/10.1007/s10994-023-06423-9)

`q2 · i?` · `causal · r2`

Explainable-AI analysis (integrated gradients) decomposing the distilled policy deployed in study 2 into per-feature attributions (Table 3). This is an analysis of the learned policy, not a human-outcome experiment; no effect size is printed.

> "This analysis selected student's pretest score and their math anxiety score as the most inﬂuential contextual features on the AI guide's chosen response. Other student features had little to no eﬀect."

### Sherry Ruan 2024 (2)

Sherry Ruan, Allen Nie, William Steenbergen, Jiayu He, JQ Zhang, Meng Guo, Yao Liu, Kyle Dang Nguyen, Catherine Y Wang, Rui Ying, James A Landay, Emma Brunskill. (2024). Reinforcement Learning Tutor Better Supported Lower Performers in a Math Task. Originally published 2023. [doi:10.1007/s10994-023-06423-9](https://doi.org/10.1007/s10994-023-06423-9)

`q2 · i?` · `causal · r2`

Interpretation of the attribution table and Figure 6 action probabilities by pretest group (Bottom 0-2, Top 6-8) and anxiety level. The article offers the productive-struggle reading as the authors' interpretation, and says such observed interactions could inform expert analysis and hypothesis generation.

> "Students with higher pretest scores were more likely to receive direct hints: such students may require less of the productive struggle needed to learn new mathematics."

## Discussion


## Related Claims
- [Attribution analysis identifies interpretable input features for BERT's classification decisions, including subjunctive verbs in alternatives and appraisal words in evaluation](attribution-analysis-identifies-bert-classification-features.md) — related
- [Feature-based model predictive power derives from a large and varied set of features rather than a few dominant variables](feature-importance-spread-across-many-features.md) — related
- [Female participants reported significantly higher maths anxiety and general anxiety, while males reported higher maths self-efficacy and maths interest](sex-differences-maths-anxiety-motivation-means.md) — related
- [In a simulated tutoring agent, removing the behavioral-safety constraint (C3) appears to cause collapse to near-single-action policies, which the authors read as C3 being the most influential safeguard, though its ablation does not differ significantly from removing C1 in RHSI](c3-ablation-policy-collapse.md) — related
