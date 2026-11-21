---
type: claim
title: LLM scores are more consistent across trials than human scores, with GPT-4 using explanations showing the greatest confidence
description: LLM scores are more consistent across trials than human scores, with GPT-4 using explanations showing the greatest confidence
id: llm-trial-consistency-exceeds-human-consistency
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: jie-tian-2024
    resource: "https://doi.org/10.31219/osf.io/d3nc6"
    title: "Jie Tian, Jixin Hou, Zihao Wu, Peng Shu, Ning Liu, Zhengliang Liu, Yujie Xiang, Beikang Gu, Nicholas Filla, Yiwei Li, Xianyan Chen, Keke Tang, Tianming Liu, and Xianqiao Wang. (2024). Assessing Large Language Models in Mechanical Engineering Education: A Study on Mechanics-Focused Conceptual Understanding. [doi:10.31219/osf.io/d3nc6](https://doi.org/10.31219/osf.io/d3nc6)"
    author: Jie Tian, Jixin Hou, Zihao Wu, Peng Shu, Ning Liu, Zhengliang Liu, Yujie Xiang, Beikang Gu, Nicholas Filla, Yiwei Li, Xianyan Chen, Keke Tang, Tianming Liu, and Xianqiao Wang
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# LLM scores are more consistent across trials than human scores, with GPT-4 using explanations showing the greatest confidence

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Cross-trial Pearson correlation of scores is markedly lower for human cohorts than for LLMs, with GPT-4 with explanation first highest. [→ Jie Tian 2024](#jie-tian-2024)

## Evidence

### Jie Tian 2024

Jie Tian, Jixin Hou, Zihao Wu, Peng Shu, Ning Liu, Zhengliang Liu, Yujie Xiang, Beikang Gu, Nicholas Filla, Yiwei Li, Xianyan Chen, Keke Tang, Tianming Liu, and Xianqiao Wang. (2024). Assessing Large Language Models in Mechanical Engineering Education: A Study on Mechanics-Focused Conceptual Understanding. [doi:10.31219/osf.io/d3nc6](https://doi.org/10.31219/osf.io/d3nc6)

`q2 · i?` · `causal · r1`

Consistency analysis using the mean upper-triangle Pearson correlation across trials (Figure 5c); the article reports human correlation is "significantly lower" and LLMs show greater confidence, especially GPT-4 with explanation first. No coefficient value printed.

> "Since human results are collected from different persons, The correlation is significantly lower, and LLMs all have greater confidence. Especially GPT-4 with explanation provided first."

## Discussion


## Related Claims
- [Automated judging aligns strongly with three domain experts (r = 0.82 for role fidelity) but exhibits a conservative bias, scoring ethical deviation 0.08 points lower than humans](automated-judge-human-alignment-conservative-bias.md) — related
- [Published evidence suggests LLM scoring can outperform standardized patient scoring on rubric-scored written notes, but generalizability remains open](llm-scoring-lower-incorrect-rate-than-sp.md) — related
- [Prompting LLMs to explain before answering improves their accuracy on mechanics conceptual questions](explanation-first-prompting-improves-llm-mechanics-accuracy.md) — related
- [Agreement between GPT-4's answers and human-curated answers based on its explanations was low (κ=0.504), with frequent answer-explanation mismatches](gpt4-answer-explanation-consistency-low-kappa.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [Human review of GPT-4's explanations reduced overall accuracy from 43.9% to 40.3% and 39.1%, driven mainly by LOTS and recall questions](human-curation-lowered-gpt4-accuracy-lots-recall.md) — related
- [GPT-4o–based multiagent framework achieved the highest factual consistency score of 0.769](gpt4o-highest-factual-consistency-0-769.md) — related
- [Most GPT-4 errors on TCM examination questions stemmed from misunderstanding of TCM concepts (55.3%), not misreading questions](gpt4-tcm-errors-concept-misunderstanding-55-3.md) — related
- [Gains in explaining engagement mechanisms were smaller: advanced reasoning rose from 0.55% to 9.42% and incorrect answers fell from 22.40% to 13.09%](engagement-explanations-weaker-gains.md) — related
