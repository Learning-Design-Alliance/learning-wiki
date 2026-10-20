---
type: claim
title: The LLM-judge separates weak submissions but its ranking of the strongest systems has almost no agreement with crowd ranking (Spearman ρ = −0.17)
description: The LLM-judge separates weak submissions but its ranking of the strongest systems has almost no agreement with crowd ranking (Spearman ρ = −0.17)
id: llm-judge-ranks-strongest-systems-poorly
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: lin-2026
    resource: "https://doi.org/10.48550/arxiv.2608.08852"
    title: "Lin, Yi-Cheng; Guo, Yu-Kai; Chen, Szu-Chi; Feng, Bo-Han; Hsu, Yun-Man; Hsieh, Hsiang; Lin, Yu-Jung; Wu, Yue-Ling; Dong, Jia-Kai; Cheng, An-Yu; Huang, Yu-Han; Ieong, Lok-Lam; Chen, Kuan-Yu; Tchouang, Ming-Douo; Sun, Shao-Hua; Lin, Che; Ding, Jian-Jiun; Lee, Hung-yi. (2026). Findings of the First Teaching Monster Challenge: A Benchmark of Pedagogical Content Knowledge in AI Agents. arXiv. https://arxiv.org/abs/2608.08852 [doi:10.48550/arxiv.2608.08852](https://doi.org/10.48550/arxiv.2608.08852)"
    author: Lin, Yi-Cheng; Guo, Yu-Kai; Chen, Szu-Chi; Feng, Bo-Han; Hsu, Yun-Man; Hsieh, Hsiang; Lin, Yu-Jung; Wu, Yue-Ling; Dong, Jia-Kai; Cheng, An-Yu; Huang, Yu-Han; Ieong, Lok-Lam; Chen, Kuan-Yu; Tchouang, Ming-Douo; Sun, Shao-Hua; Lin, Che; Ding, Jian-Jiun; Lee, Hung-yi
    q: 2
    i: 1
    kind: design
    rigour: 3
---

# The LLM-judge separates weak submissions but its ranking of the strongest systems has almost no agreement with crowd ranking (Spearman ρ = −0.17)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2` · `i1` small

## Subclaims
`q2 i1` The judge's ranking of the ten shortlisted systems correlates negatively with the crowd's Elo ranking (ρ = −0.17); the eventual winner ranked fourth under the judge while the judge's top two finished eighth and tenth with the crowd. [→ Lin 2026](#lin-2026)

## Evidence

### Lin 2026

Lin, Yi-Cheng; Guo, Yu-Kai; Chen, Szu-Chi; Feng, Bo-Han; Hsu, Yun-Man; Hsieh, Hsiang; Lin, Yu-Jung; Wu, Yue-Ling; Dong, Jia-Kai; Cheng, An-Yu; Huang, Yu-Han; Ieong, Lok-Lam; Chen, Kuan-Yu; Tchouang, Ming-Douo; Sun, Shao-Hua; Lin, Che; Ding, Jian-Jiun; Lee, Hung-yi. (2026). Findings of the First Teaching Monster Challenge: A Benchmark of Pedagogical Content Knowledge in AI Agents. arXiv. https://arxiv.org/abs/2608.08852 [doi:10.48550/arxiv.2608.08852](https://doi.org/10.48550/arxiv.2608.08852)

`q2 · i1` · `design · r3`

Comparison of Layer 1 judge ranking against Layer 2 crowd Elo ranking for the ten shortlisted systems, showing "almostno agreement" (ρ = −0.17). The mismatch is not measurement noise: judge scores were stable across repeated runs (median within-cell SD 0.14), and tsunumon's 90% Elo interval overlapped neither Team 67's nor Kuro's.

> "itsrankingofthesetenhasalmostno agreement with the Layer 2 crowd ranking (Spearmanρ= −0.17).tsunumon, the eventual winner, ranks only fourth under the judge, while the judge's top two,Team 67andKuro,finisheighthandtenthwiththecrowd."

## Discussion


## Related Claims
- [Judge and crowd broadly agree on which criteria matter, but the judge's near-identical top scores make its ranking of strong systems essentially random](judge-crowd-agree-on-criteria-but-scores-separate-nothing.md) — related
- [Only the challenge winner clearly beat the organizer baselines; most shortlisted systems have not yet improved on a commercial generator or well-chosen human-made video](only-winner-beat-organizer-baselines.md) — related
- [Independent LLM evaluators agreed on agent rankings but differed markedly in leniency, with ceiling effects compressing between-agent discrimination](llm-evaluator-leniency-ceiling-effects.md) — related
- [Human raters' preferences align with the LLM judge on TutorBench (Pearson r = 0.82 across metric-level win rates)](human-llm-judge-preference-alignment-deeptutor.md) — related
- [Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested](within-judge-stability-llm-rubric.md) — related
