---
type: product
id: itell-intelligent-textbook-for-enhanced-language-learning
title: iTELL (Intelligent Textbook for Enhanced Language Learning)
description: iTELL is a computational framework and interactive intelligent-textbook web application developed by Morris et al.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-28
---

# iTELL (Intelligent Textbook for Enhanced Language Learning)

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
iTELL is a computational framework and interactive intelligent-textbook web application developed by Morris et al. that lets learners write end-of-section summaries and provides automated LLM-based scoring and feedback.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **iTELL summary feedback pipeline with pre-scoring filters**: iTELL (Intelligent Textbook for Enhanced Language Learning) is a computational framework that converts machine-readable textbooks into interactive web-apps in which students write end-of-section summaries that are scored automatically by the study's LLMs. Before scoring, summaries pass a filter component: "The filter ensures that the summary is between 50 and 200 words, and the summary is passed through a semantic similarity measure using Doc2Vec (Le & Mikolov, 2014) that assesses whether the summary is on topic." Summaries that heavily borrow from the source or contain offensive language are rejected without LLM analysis, which the authors say ensures only effortful summaries reach the models and reduces computational load. (Morris et al. (2025))

### Claims
- [On new crowd-sourced Prolific summaries, the Content model generalized well (r = 0.70) but the Wording model predicted human scores poorly (r = 0.29)](../claims/prolific-generalizability-content-strong-wording-weak.md) [+M]
- [Including the textbook source text in the model input improves automated summary scoring accuracy, with Longformer explaining 82% of Content and 70% of Wording score variance versus 67% and 41% for summary-only RoBERTa](../claims/longformer-source-text-outperforms-roberta-summary-scoring.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Morris, W., Crossley, S., Holmes, L., Ou, C., Dascalu, M., & McNamara, D. (2025). Formative Feedback on Student-Authored Summaries in Intelligent Textbooks Using Large Language Models. International Journal of Artificial Intelligence in Education, 35, 1022–1043. https://doi.org/10.1007/s40593-024-00395-0
