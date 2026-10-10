---
type: claim
title: "The LLM observation function's per-answer mastery evidence correlates with true mastery at r = 0.68 pooled, but only r ≈ 0.15 within the weak tier, making it least reliable for low-ability learners"
description: "The LLM observation function's per-answer mastery evidence correlates with true mastery at r = 0.68 pooled, but only r ≈ 0.15 within the weak tier, making it least reliable for low-ability learners"
id: collearn-observation-function-within-tier-reliability
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: kailai-he-2026
    resource: "https://arxiv.org/abs/2609.21154"
    title: "Kailai He, Zhihao Wu, Linhai Zhang, Runcong Zhao, Yulan He, Jiazheng Li. (2026). CoLearn: An Agentic Tutor that Learns its Learner in a Human–AI Co-Learning Loop. https://arxiv.org/abs/2609.21154"
    author: Kailai He, Zhihao Wu, Linhai Zhang, Runcong Zhao, Yulan He, Jiazheng Li
    q: 2
    i: 3
    kind: design
    rigour: 2
  - id: kailai-he-2026-2
    resource: "https://arxiv.org/abs/2609.21154"
    title: "Kailai He, Zhihao Wu, Linhai Zhang, Runcong Zhao, Yulan He, Jiazheng Li. (2026). CoLearn: An Agentic Tutor that Learns its Learner in a Human–AI Co-Learning Loop. https://arxiv.org/abs/2609.21154"
    author: Kailai He, Zhihao Wu, Linhai Zhang, Runcong Zhao, Yulan He, Jiazheng Li
    q: 2
    i: 1
    kind: design
    rigour: 2
---

# The LLM observation function's per-answer mastery evidence correlates with true mastery at r = 0.68 pooled, but only r ≈ 0.15 within the weak tier, making it least reliable for low-ability learners

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2` · `i1`–`i3`

## Subclaims
`q2 i3` Per-answer mastery_evidence correlates with true mastery at Pearson r = 0.68 pooled across tiers in the 6-persona live-graded run. [→ Kailai He 2026](#kailai-he-2026)
`q2 i1` Within-tier correlations are much weaker (r ≈ 0.15 / 0.48 / 0.41 for weak/mixed/strong), weakest for low-ability personas. [→ Kailai He 2026 (2)](#kailai-he-2026-2)

## Evidence

### Kailai He 2026

Kailai He, Zhihao Wu, Linhai Zhang, Runcong Zhao, Yulan He, Jiazheng Li. (2026). CoLearn: An Agentic Tutor that Learns its Learner in a Human–AI Co-Learning Loop. https://arxiv.org/abs/2609.21154

`q2 · i3` · `design · r2`

Persona-simulation analysis (6 personas, 132 rounds) graded by the live framework model; the article reports "mastery_evidencecor- relates with true mastery at Pearson r= 0.68 pooled across tiers".

> "per-answermastery_evidencecor- relates with true mastery at Pearson r= 0.68 pooled across tiers."

### Kailai He 2026 (2)

Kailai He, Zhihao Wu, Linhai Zhang, Runcong Zhao, Yulan He, Jiazheng Li. (2026). CoLearn: An Agentic Tutor that Learns its Learner in a Human–AI Co-Learning Loop. https://arxiv.org/abs/2609.21154

`q2 · i1` · `design · r2`

Same simulation, decomposed by tier: the article reports "the within-tier correlation is much weaker ( r≈0.15 / 0.48 / 0.41)", noting the pooled figure is driven mainly by between-tier separation.

> "the within-tier correlation is much weaker ( r≈0.15 / 0.48 / 0.41), and weakest for low-ability personas."

## Discussion


## Related Claims
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [LLM choice significantly influences human-AI coding correspondence, with Claude Sonnet 4 performing best and GPT 4.1 Mini worst](llm-choice-affects-human-ai-coding-correspondence.md) — related
- [Human-LLM agreement is moderated by code properties, multi-model consensus, and model-reported confidence](agreement-moderators-tiers-consensus-confidence.md) — related
