---
type: research-method
id: epi2diff-framework-episode-induced-process-representations-combined-with-semantic-embeddin
title: "Epi2Diff framework: episode-induced process representations combined with semantic embeddings for item difficulty prediction"
description: Epi2Diff (Episode to Difficulty) converts model-generated reasoning traces into sentence-level episode sequences and extracts compact features capturing reasoning effort.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Epi2Diff framework: episode-induced process representations combined with semantic embeddings for item difficulty prediction

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
Epi2Diff (Episode to Difficulty) converts model-generated reasoning traces into sentence-level episode sequences and extracts compact features capturing reasoning effort. Its episode-induced process representation "combines three complementary groups of features: length features capturing the overall scale of the reasoning process, episode-distribution features characterizing its composition across episode types, and transition features encoding its local sequential organization". These 83 process features are concatenated with a Sentence-BERT item embedding, averaged across direct, weak, medium, and strong prompting profiles, and fed to a supervised predictor (XGBoost across all datasets). Code is released at the article's GitHub website.

## Accounts
<!-- How each source describes or uses the method -->
- **Epi2Diff framework: episode-induced process representations combined with semantic embeddings for item difficulty prediction**: Epi2Diff (Episode to Difficulty) converts model-generated reasoning traces into sentence-level episode sequences and extracts compact features capturing reasoning effort. Its episode-induced process representation "combines three complementary groups of features: length features capturing the overall scale of the reasoning process, episode-distribution features characterizing its composition across episode types, and transition features encoding its local sequential organization". These 83 process features are concatenated with a Sentence-BERT item embedding, averaged across direct, weak, medium, and strong prompting profiles, and fed to a supervised predictor (XGBoost across all datasets). Code is released at the article's GitHub website. (Chenguang Wang et al. (2026))

### Claims

- [Epi2Diff achieves the best performance across all four item-difficulty test sets and all reported metrics, outperforming SLM fine-tuning, LLM prompting, and supervised LLM adaptation baselines](../claims/epi2diff-best-across-four-difficulty-benchmarks.md) [+M]
- [Combining semantic and process features yields the best difficulty prediction; semantic embeddings alone trail the full model by 7.4–12.1 macro-F1 points on SAT Math](../claims/full-representation-beats-semantic-only-ablation.md) [+M]
- [Reasoning-process features are particularly useful when difficulty depends on multi-step problem solving, and the representation also generalizes to text-based assessment items](../claims/process-features-strongest-for-multistep-items.md) [+W]

## Related Research Methods
-

## Key Sources
- Chenguang Wang, Ming Li, Xinyue Zeng, Zhuochun Li, Hong Jiao, Tianyi Zhou, Dawei Zhou. (2026). Cognitive Episodes in LLM Reasoning Traces Enable Interpretable Human Item Difficulty Prediction. https://arxiv.org/abs/2606.28186
