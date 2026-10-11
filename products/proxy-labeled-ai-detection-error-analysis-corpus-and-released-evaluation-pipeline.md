---
type: product
id: proxy-labeled-ai-detection-error-analysis-corpus-and-released-evaluation-pipeline
title: Proxy-labeled AI-detection error-analysis corpus and released evaluation pipeline
description: "Karr et al.'s released corpus and code evaluate commercial AI-text-detector errors using published abstracts, model rewrites, and humanized texts."
product_kind: dataset
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Proxy-labeled AI-detection error-analysis corpus and released evaluation pipeline

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · no claims cited

## Description
Karr et al.'s released corpus and code evaluate commercial AI-text-detector errors using published abstracts, model rewrites, and humanized texts.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Proxy-labeled AI-detection error-analysis corpus and released evaluation pipeline (642 OpenAlex abstracts, three rewrite conditions, two detectors, one humanizer)**: A controlled evaluation corpus and pipeline for quantifying AI-detector error rates under proxy labels. The authors sampled English abstracts from OpenAlex in chemistry, computer science, political science, and theology for 2013–2015 and 2023–2025; "After requiring 25 to 500 words and PDF access (≈20% loss), we retained 642 abstracts." Each abstract contributed an original plus three Gemini 3 Flash rewrites (refine abstract-only, refine abstract+article, new article-only), scored with Pangram 3.2 and GPTZero before and after Undetectable AI v11 humanization. Analysis code is released at the article's GitHub repository. (Jonathan A. Karr Jr. et al. (2026))

### Claims

## Related Products and Programmes
-

## Key Sources
- Jonathan A. Karr Jr., Grigorii Khvatskii, Ting Hua, and Nitesh V. Chawla. (2026). Why AI Detection Fails for Academic Integrity. Proceedings of the ACM AI Leadership Summit (AILS '26). https://arxiv.org/abs/2608.11256
