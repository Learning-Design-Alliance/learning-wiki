---
type: claim
title: Singleton search training induces value-driven relational attention regardless of target-distractor similarity
description: Singleton search training induces value-driven relational attention regardless of target-distractor similarity
id: singleton-training-relational-attention-both-similarities
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
sources:
  - id: oudeng-jia-2025
    resource: "https://doi.org/10.1038/s41539-025-00342-1"
    title: "Oudeng Jia, Qingsong Tan, Sihan Zhang, Ke Jia & Mengyuan Gong. (2025). The precision of attention selection during reward learning influences the mechanisms of value-driven attention. npj Science of Learning 10:49. https://doi.org/10.1038/s41539-025-00342-1"
    author: "Oudeng Jia, Qingsong Tan, Sihan Zhang, Ke Jia & Mengyuan Gong"
    q: 3
    i: 2
    kind: causal
    rigour: 2
  - id: oudeng-jia-2025-2
    resource: "https://doi.org/10.1038/s41539-025-00342-1"
    title: "Oudeng Jia, Qingsong Tan, Sihan Zhang, Ke Jia & Mengyuan Gong. (2025). The precision of attention selection during reward learning influences the mechanisms of value-driven attention. npj Science of Learning 10:49. https://doi.org/10.1038/s41539-025-00342-1"
    author: "Oudeng Jia, Qingsong Tan, Sihan Zhang, Ke Jia & Mengyuan Gong"
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Singleton search training induces value-driven relational attention regardless of target-distractor similarity

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3` · `i2` medium

## Subclaims
`q3 i2` In Experiments 1a and 1b, distractors matching the previously high-rewarded feature relationship produced significantly slower RTs than low-reward relational distractors, at both low and high target-distractor similarity. [→ Oudeng Jia 2025](#oudeng-jia-2025)
`q3 i?` A mixed ANOVA found no reward × experiment interaction, indicating the relational effect did not differ between similarity conditions. [→ Oudeng Jia 2025 (2)](#oudeng-jia-2025-2)

## Evidence

### Oudeng Jia 2025

Oudeng Jia, Qingsong Tan, Sihan Zhang, Ke Jia & Mengyuan Gong. (2025). The precision of attention selection during reward learning influences the mechanisms of value-driven attention. npj Science of Learning 10:49. https://doi.org/10.1038/s41539-025-00342-1

`q3 · i2` · `causal · r2`

Two-day training/test experiment (N = 40 per experiment). Paired t-tests on relation-match condition RTs showed "slower RTs when the distractor had a relationship previously associated with high reward than low reward", with printed Cohen's d = 0.400 (Experiment 1a) and d = 0.427 (Experiment 1b).

> "Paired t-test analyses on data from the relation-match condition showed signiﬁcantly slower RTs when the distractor had a relationship previously associated with high reward than low reward, in both experiments (Experiment 1a: t(39) = 2.53, p = 0.016, Cohen ’s d = 0.400, 95% CI = [0.075, 0.720]; Experiment 1b: t(39) = 2.70,p = 0.010, Cohen’s d = 0.427, 95% CI = [0.100, 0.748])."

### Oudeng Jia 2025 (2)

Oudeng Jia, Qingsong Tan, Sihan Zhang, Ke Jia & Mengyuan Gong. (2025). The precision of attention selection during reward learning influences the mechanisms of value-driven attention. npj Science of Learning 10:49. https://doi.org/10.1038/s41539-025-00342-1

`q3 · i?` · `causal · r2`

Mixed ANOVA across Experiments 1a and 1b found "an absence of an interaction effect (p = 0.865; BF01 = 4.538)", supporting that relational coding of reward-associated features occurred regardless of target-distractor similarity during training. No effect size was printed for the null interaction.

> "A two-way mixed ANOVA (reward history: high- vs. low-reward × experiment: 1a vs. 1b) on RTs suggested an absence of an interaction effect (p = 0.865; BF01 = 4.538)."

## Discussion


## Related Claims
- [Cross-experiment analysis shows reward effects on feature relationships depend jointly on search mode and target-distractor similarity](cross-experiment-relational-effect-interaction.md) — related
- [Feature search training among dissimilar distractors produces reward learning of both feature values and feature relationships](feature-search-dissimilar-relational-attention.md) — related
- [Target-distractor similarity manipulation validated: low-similarity search is faster than high-similarity search](similarity-manipulation-validation-control-exp1.md) — related
- [High-reward distractors matching trained feature values slow search RTs in singleton search training regardless of target-distractor similarity](value-driven-capture-trained-feature-values-singleton-search.md) — related
- [Feature search training among similar distractors abolishes value-driven relational attention](feature-search-similar-relational-attention-abolished.md) — reports the opposite
- [Feature search training among similar distractors (Experiment 2b) shows no relational reward effect and only marginal feature-value capture](exp2b-null-relational-effect.md) — reports the opposite
- [Reward-associated distractors elicited attentional capture rather than suppression in Experiment 2c](reward-distractor-capture-not-suppression-exp2c.md) — related
