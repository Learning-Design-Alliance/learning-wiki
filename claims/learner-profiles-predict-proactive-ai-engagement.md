---
type: claim
title: Students from higher-ranked universities and with stronger prior knowledge are more likely to adopt proactive and critical AI engagement
description: Students from higher-ranked universities and with stronger prior knowledge are more likely to adopt proactive and critical AI engagement
id: learner-profiles-predict-proactive-ai-engagement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: jingwei-yi-2026
    resource: "https://doi.org/10.48550/arxiv.2607.10101"
    title: "Jingwei Yi, Yueqi Xie, Jiyan He, Rui Ye, Junming Huang, Bin Zhu, Sean Rintel, Yu Xie, Xing Xie, and Fangzhao Wu. (2026). Learning behavior accounts for background-related advantage in AI-assisted education. https://arxiv.org/abs/2607.10101 [doi:10.48550/arxiv.2607.10101](https://doi.org/10.48550/arxiv.2607.10101)"
    author: Jingwei Yi, Yueqi Xie, Jiyan He, Rui Ye, Junming Huang, Bin Zhu, Sean Rintel, Yu Xie, Xing Xie, and Fangzhao Wu
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: jingwei-yi-2026-2
    resource: "https://arxiv.org/abs/2607.10101"
    title: "Jingwei Yi, Yueqi Xie, Jiyan He, Rui Ye, Junming Huang, Bin Zhu, Sean Rintel, Yu Xie, Xing Xie, and Fangzhao Wu. (2026). Learning behavior accounts for background-related advantage in AI-assisted education. https://arxiv.org/abs/2607.10101"
    author: Jingwei Yi, Yueqi Xie, Jiyan He, Rui Ye, Junming Huang, Bin Zhu, Sean Rintel, Yu Xie, Xing Xie, and Fangzhao Wu
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Students from higher-ranked universities and with stronger prior knowledge are more likely to adopt proactive and critical AI engagement

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` In game theory, university ranking (auniv = +0.171, P=0.010) and prior knowledge (aprior = +0.161, P=0.002) were positively associated with proactive and critical engagement. [→ Jingwei Yi 2026](#jingwei-yi-2026)
`q2 i?` In Python, prior knowledge was positively associated (aprior = +0.217, P=0.046); the overall university-ranking association was not significant, but a follow-up z-test showed mid/high-ranking students more likely than low-ranking students to engage proactively (proportion difference = +0.32, P=0.035). [→ Jingwei Yi 2026 (2)](#jingwei-yi-2026-2)

## Evidence

### Jingwei Yi 2026

Jingwei Yi, Yueqi Xie, Jiyan He, Rui Ye, Junming Huang, Bin Zhu, Sean Rintel, Yu Xie, Xing Xie, and Fangzhao Wu. (2026). Learning behavior accounts for background-related advantage in AI-assisted education. https://arxiv.org/abs/2607.10101 [doi:10.48550/arxiv.2607.10101](https://doi.org/10.48550/arxiv.2607.10101)

`q2 · i?` · `causal · r2`

OLS linear probability models within the experimental group of the 318-student randomized trial predicting the binary proactive-critical engagement indicator from learner profiles; the article reports "auniv = +0.171, P=0.010 and aprior = +0.161, P=0.002" in game theory.

> "In game theory, both university ranking and prior knowledge are positively associated with proactive and critical engagement (auniv = +0.171, P=0.010 and aprior = +0.161, P=0.002 )."

### Jingwei Yi 2026 (2)

Jingwei Yi, Yueqi Xie, Jiyan He, Rui Ye, Junming Huang, Bin Zhu, Sean Rintel, Yu Xie, Xing Xie, and Fangzhao Wu. (2026). Learning behavior accounts for background-related advantage in AI-assisted education. https://arxiv.org/abs/2607.10101

`q2 · i?` · `causal · r2`

Same OLS specification in the Python course plus a one-sided two-proportion z-test follow-up; the article reports "aprior = +0.217, P=0.046" and the significant low-versus-mid/high ranking contrast.

> "In Python, prior knowledge is also positively associated with proactive and critical engagement (aprior = +0.217, P=0.046 ). Although the overall association with university ranking is not significant (auniv = +0.161, P=0.127 ), a follow-up one-sided two-proportion z-test shows that students from mid- and high-ranking universities are more likely than students from low-ranking universities to adopt proactive and critical engagement (proportion difference= +0.32,P=0.035)."

## Discussion

## Learner Variables
- [Prior Knowledge](../learner-variables/prior-knowledge.md) — predictor: learners who differ on it differ in outcomes

## Related Claims

- [Prior Knowledge Needed For Accurate Self Assessment](prior-knowledge-needed-for-accurate-self-assessment.md) — the general claim this finding bears on, with the studies behind it
- [Exploratory, non-significant pattern suggests students with stronger learner profiles may show larger AI-assisted exam gains](exploratory-profile-interaction-ai-gains.md) — related
- [Students did not consistently detect scientific errors in ChatGPT responses, and students with stronger prior knowledge evaluated AI responses more critically](prior-knowledge-supports-critical-ai-evaluation.md) — related
- [High-achieving students less often endorse AI-supported autonomy, effective learning, and active engagement, and more often agree that reliance on AI hinders critical thinking and independent problem solving](item-level-high-achievers-hinder-critical-thinking.md) — reports the opposite
- [Accounting for learning behavior attenuates profile-related exam score differences, eliminating significance in Python](learning-behavior-attenuates-profile-score-differences.md) — related
- [Among GPT-assisted students, proactive and critical engagement patterns are associated with higher exam scores while limited engagement shows little benefit relative to control](proactive-critical-ai-engagement-higher-exam-scores.md) — related
