---
type: product
id: proxy-labeled-ai-detection-error-analysis-corpus-and-released-evaluation-pipeline
title: Proxy-labeled AI-detection error-analysis corpus and released evaluation pipeline
description: "Karr et al.'s released corpus and code evaluate commercial AI-text-detector errors using published abstracts, model rewrites, and humanized texts."
product_kind: dataset
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Proxy-labeled AI-detection error-analysis corpus and released evaluation pipeline

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 14 claims (9 for, 5 mixed) · 5 studies (2 design, 1 causal, 1 review, 1 theoretical), `q2`–`q3` · 1 of 5 report an effect size · 14 claims rest on one study

## Description
Karr et al.'s released corpus and code evaluate commercial AI-text-detector errors using published abstracts, model rewrites, and humanized texts.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Proxy-labeled AI-detection error-analysis corpus and released evaluation pipeline (642 OpenAlex abstracts, three rewrite conditions, two detectors, one humanizer)**: A controlled evaluation corpus and pipeline for quantifying AI-detector error rates under proxy labels. The authors sampled English abstracts from OpenAlex in chemistry, computer science, political science, and theology for 2013–2015 and 2023–2025; "After requiring 25 to 500 words and PDF access (≈20% loss), we retained 642 abstracts." Each abstract contributed an original plus three Gemini 3 Flash rewrites (refine abstract-only, refine abstract+article, new article-only), scored with Pangram 3.2 and GPTZero before and after Undetectable AI v11 humanization. Analysis code is released at the article's GitHub repository. (Jonathan A. Karr Jr. et al. (2026))

### Claims

- [After humanization with Undetectable AI, fewer than 4% of AI-labeled rewrites remain detectable (FNR > 96%) for Pangram and GPTZero](../claims/humanization-drives-detection-below-4-percent.md) [+M]
- [Light AI-assisted edits to human-written abstracts are flagged by commercial detectors at 64–80% (Pangram) and 38–49% (GPTZero) rates](../claims/light-ai-edits-flagged-at-high-rates.md) [+M]
- [No detection threshold simultaneously keeps original flag rates, light-edit capture, and AI-pool false negatives low](../claims/no-threshold-satisfies-all-three-error-rates.md) [+M]
- [Detector flag rates on 2023–2025 original abstracts vary sharply by domain, with non-STEM rates far above STEM](../claims/non-stem-abstracts-flagged-more-than-stem.md) [+M]
- [Inter-detector agreement between Pangram and GPTZero collapses after humanization, so a single vendor flag is not a reliable consensus signal](../claims/detector-agreement-collapses-after-humanization.md) [+M]
- [Independent evaluation found commercial AI-text detectors neither sufficiently accurate nor sufficiently reliable for high-stakes use](../claims/detectors-insufficient-accuracy-high-stakes.md) [+W]
- [Elevated detector scores track long-token and Academic Word List density, with numeric and non-alphabetic token ratios correlating negatively](../claims/detector-scores-track-long-token-and-awl-density.md) [~W]
- [Comparative studies report that AI detection tools do not reliably distinguish human-written from AI-generated text](../claims/ai-detection-tools-not-reliably-distinguishing.md) [+W]
- [A detector can achieve high aggregate accuracy while producing materially different over-detection rates across author groups](../claims/aggregate-accuracy-group-fairness-detectors.md) [~W]
- [In a documented exploratory audit, one human-authored manuscript received materially different classifications from five commercial detectors, spanning 0% human to Human Generated](../claims/multi-tool-audit-cross-tool-inconsistency.md) [+W]
- [A linear mixed-effects model of detection error showed significant paper type, tool, and interaction effects, with underestimation largest for fully AI-generated papers and Pangram consistently producing the smallest errors](../claims/mixed-model-detection-error-underestimation.md) [+W]
- [All four detection tools classified 100% of fully human-written papers as true negatives, with false positives nearly absent](../claims/all-tools-accurate-on-human-written-papers.md) [~W]
- [Humanization works by systematically suppressing detector-salient surface cues — long-token ratio, AWL density, and lexical diversity — rather than fragmenting syntax](../claims/humanization-suppresses-detector-salient-cues.md) [~W]
- [The stylometric detector misclassified 4 of 18 independently authored documents as GPT-assisted (FPR 22.2%) and 2 of 18 GPT-assisted documents (FNR 11.1%), with wide confidence intervals](../claims/stylometric-detector-fpr-22-fnr-11.md) [~W]

## Related Products and Programmes
-

## Key Sources
- Jonathan A. Karr Jr., Grigorii Khvatskii, Ting Hua, and Nitesh V. Chawla. (2026). Why AI Detection Fails for Academic Integrity. Proceedings of the ACM AI Leadership Summit (AILS '26). https://arxiv.org/abs/2608.11256
