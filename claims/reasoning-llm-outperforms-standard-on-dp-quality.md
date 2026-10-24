---
type: claim
title: A reasoning-oriented LLM outperformed a standard LLM on scenario quality and feasibility of generated design problems, with no differences on alignment, cognitive complexity, or clarity
description: A reasoning-oriented LLM outperformed a standard LLM on scenario quality and feasibility of generated design problems, with no differences on alignment, cognitive complexity, or clarity
id: reasoning-llm-outperforms-standard-on-dp-quality
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: ahmad-d-suleiman-2026
    resource: "https://doi.org/10.48550/arxiv.2607.11032"
    title: "Ahmad D. Suleiman, Daqing Hou, and Maliha Noushin Raida. (2026). LLM-Generated Design Problems for Assessing Higher-Order Thinking in Project-Based Learning. arXiv preprint arXiv:2607.11032. https://arxiv.org/abs/2607.11032 [doi:10.48550/arxiv.2607.11032](https://doi.org/10.48550/arxiv.2607.11032)"
    author: Ahmad D. Suleiman, Daqing Hou, and Maliha Noushin Raida
    q: 2
    i: 3
    kind: design
    rigour: 2
---

# A reasoning-oriented LLM outperformed a standard LLM on scenario quality and feasibility of generated design problems, with no differences on alignment, cognitive complexity, or clarity

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · `i3` large
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i3` The reasoning-oriented LLM scored significantly higher than the standard LLM on scenario quality (0.97 vs. 0.77, p<0.001, d=0.88) and feasibility (1.00 vs. 0.94, p=0.018, d=0.55). [→ Ahmad D. Suleiman 2026](#ahmad-d-suleiman-2026)
`q2 i?` No statistically significant differences between the two LLMs were observed for alignment, cognitive complexity, or clarity/specificity (p>0.05). [→ Ahmad D. Suleiman 2026](#ahmad-d-suleiman-2026)

## Evidence

### Ahmad D. Suleiman 2026

Ahmad D. Suleiman, Daqing Hou, and Maliha Noushin Raida. (2026). LLM-Generated Design Problems for Assessing Higher-Order Thinking in Project-Based Learning. arXiv preprint arXiv:2607.11032. https://arxiv.org/abs/2607.11032 [doi:10.48550/arxiv.2607.11032](https://doi.org/10.48550/arxiv.2607.11032)

`q2 · i3` · `design · r2`

Expert evaluation of 80 DPs (10 per project from GPT-4o and Gemini 2.5 Pro) using two-tailed t-tests and Cohen's d found the reasoning model "significantly outperformed the standard LLM onscenario quality" with d=0.88 and higher feasibility with d=0.55.

> "the reasoning-oriented LLM significantly outperformed the standard LLM onscenario quality(SQ: 0.97 vs. 0.77, 𝑝< 0.001,𝑑= 0.88), indicating more realistic and contextually rich scenarios supporting transfer. It also achieved higherfeasibility(FS: 1.00 vs. 0.94, 𝑝= 0.018,𝑑= 0.55)"

## Discussion


## Related Claims
- [Students rated DPs positively, did not distinguish the two LLMs, and disagreed with experts on the same DPs, rating feasibility significantly lower](student-perceptions-of-dps-differ-from-experts.md) — related
- [Half of LLM-generated design problems received perfect expert ratings, though common failure modes included scenarios too similar to the original project and ambiguous scope](llm-dp-quality-failure-modes.md) — related
- [Ablating expert-informed structural components lowered LLM-judge scores on all dimensions, with largest drops in challenge quality, intent alignment, and domain grounding](ablation-structural-components-lower-judge-scores.md) — related
