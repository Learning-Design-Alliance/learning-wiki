---
type: research-method
id: sme-elicited-llm-feature-based-item-difficulty-prediction
title: SME-elicited LLM feature-based item difficulty prediction
description: A catalog of item features developed through focus groups with four subject matter experts from the assessment design team and cross-referenced with prior literature, then rated by GPT-4o for each item.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
---

# SME-elicited LLM feature-based item difficulty prediction

> **Research Method** · [All research methods](index.md)
> **Evidence** · 4 claims (3 for, 1 mixed) · 2 studies (2 design), `q2` · 1 of 2 report an effect size · 4 claims rest on one study

## Description
A catalog of item features developed through focus groups with four subject matter experts from the assessment design team and cross-referenced with prior literature, then rated by GPT-4o for each item. The process yielded "both domain-general features, which SMEs considered relevant to both subjects (e.g., Cognitive Load, Depth of Knowledge), and domain-specific features (e.g., Symbolic Reasoning for math; Figurative Language for reading)". Math items were rated on 20 targeted questions and reading items on 13, using numeric (e.g., 1-10), binary (Y/N), and DOK (1-4) scales, plus a holistic 1-100 overall difficulty rating. These ratings served as predictors in the tree-based models.

## Accounts
<!-- How each source describes or uses the method -->
- **SME-elicited feature set for LLM item evaluation, combining domain-general and domain-specific cognitive and linguistic features**: A catalog of item features developed through focus groups with four subject matter experts from the assessment design team and cross-referenced with prior literature, then rated by GPT-4o for each item. The process yielded "both domain-general features, which SMEs considered relevant to both subjects (e.g., Cognitive Load, Depth of Knowledge), and domain-specific features (e.g., Symbolic Reasoning for math; Figurative Language for reading)". Math items were rated on 20 targeted questions and reading items on 13, using numeric (e.g., 1-10), binary (Y/N), and DOK (1-4) scales, plus a holistic 1-100 overall difficulty rating. These ratings served as predictors in the tree-based models. (Pooya Razavi (2025))

### Claims

- [Feature-based models (LLM-extracted features plus metadata in random forest and gradient boosting) outperform direct LLM estimation, dummy regressor, TF-IDF, and metadata-only benchmarks, with correlations up to r = .87](../claims/feature-based-llm-models-outperform-direct-estimation-and-benchmarks.md) [+M]
- [LLM-extracted cognitive and linguistic features add predictive value beyond readily available item metadata (grade, domain, item type, word count)](../claims/llm-features-add-value-beyond-item-metadata.md) [+M]
- [The explainable feature-based model with LLM-extracted features outperforms the closed-track encoder baseline by a wide margin](../claims/explainable-model-outperforms-closed-track-baseline.md) [+W]
- [Feature-based model predictive power derives from a large and varied set of features rather than a few dominant variables](../claims/feature-importance-spread-across-many-features.md) [~W]

## Related Research Methods
-

## Key Sources
- Pooya Razavi, Sonya Powers. (2025). Estimating Item Difficulty Using Large Language Models and Tree-Based Machine Learning Algorithms. Edmentum. https://www.edmentum.com
