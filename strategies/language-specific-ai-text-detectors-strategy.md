---
type: strategy
id: language-specific-ai-text-detectors-strategy
title: Improve or develop language-specific AI-text detection algorithms for academic settings where students do not write in English
description: The article recommends that institutions and developers address the weakness of current AI-text detectors in non-English academic settings.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: željana-bašić-2023
    resource: "https://arxiv.org/abs/2302.04536"
    title: "Željana Bašić, Ana Banovac, Ivana Kružić, Ivan Jerković. (2023). Better by You, better than Me? ChatGPT-3 as writing assistance in students' essays. University Department of Forensic Sciences, University of Split. https://arxiv.org/abs/2302.04536"
    author: Željana Bašić, Ana Banovac, Ivana Kružić, Ivan Jerković
---

# Improve or develop language-specific AI-text detection algorithms for academic settings where students do not write in English

> **Strategy** · [All strategies](index.md)
> **Evidence** · 9 claims (9 for) · 5 studies (2 review, 2 qualitative, 1 theoretical), `q1`–`q2` · 0 of 5 report an effect size · 9 claims rest on one study

## Description
The article recommends that institutions and developers address the weakness of current AI-text detectors in non-English academic settings. Because "most classifiers are intended for English and usually have disclaimers for performance in other languages", the authors argue this "raises the necessity of improving existing algorithms for different languages or developing language-specific ones". In their Croatian-language study, the available detector produced false positives on human-written control essays.

## Design Implications

### Context
#### Requirements
- Detection tools must be applied to student writing in the language it was actually produced in; the article chose its classifier only after other programs failed to recognize a ChatGPT-generated Croatian text as AI-assisted
#### Constraints
- The article notes detectors of AI-generated text are developing daily and highly reliable tools are only a matter of time, so the recommendation is tied to current detector limitations

### Target Learners
- second-year master's students in forensic sciences writing in Croatian

### Target Learning Goals
- academic essay writing
- academic integrity assessment

## Claims

- [AI-text detectors misclassify authentic TOEFL essays by non-native English speakers at a mean false-positive rate of 61.3% across seven detectors, far more often than native-speaker essays](../claims/detector-61-3-percent-false-positives-non-native-toefl.md) [+W]
- [AI-detection tools produce inequitable outcomes, disadvantaging non-native English speakers through false positives](../claims/ai-detection-tools-inequitable-false-positives.md) [+W]
- [A detector can achieve high aggregate accuracy while producing materially different over-detection rates across author groups](../claims/aggregate-accuracy-group-fairness-detectors.md) [+W]
- [Detection-centered academic integrity regimes are unreliable and potentially biased, making sole reliance on AI detectors unsuitable for high-stakes decisions](../claims/ai-detection-unreliable-biased-high-stakes.md) [+W]
- [In a documented exploratory audit, one human-authored manuscript received materially different classifications from five commercial detectors, spanning 0% human to Human Generated](../claims/multi-tool-audit-cross-tool-inconsistency.md) [+W]
- [Independent evaluation found commercial AI-text detectors neither sufficiently accurate nor sufficiently reliable for high-stakes use](../claims/detectors-insufficient-accuracy-high-stakes.md) [+W]
- [Universities disabling AI detection cite false-positive risk at scale, and detector influence persists in individual grading, journal screening, and institutions without policy revision](../claims/detector-false-positives-at-scale-institutional-retreat.md) [+W]
- [AI text detectors can return high AI-detection scores for human-written academic text, raising fairness concerns about authenticity evaluation](../claims/ai-detectors-misscore-human-written-text.md) [+W]
- [A majority of universities with faculty guidelines discourage reliance on AI detection tools due to unreliability and bias](../claims/universities-discourage-ai-detection-tools.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Željana Bašić, Ana Banovac, Ivana Kružić, Ivan Jerković. (2023). Better by You, better than Me? ChatGPT-3 as writing assistance in students' essays. University Department of Forensic Sciences, University of Split. https://arxiv.org/abs/2302.04536
