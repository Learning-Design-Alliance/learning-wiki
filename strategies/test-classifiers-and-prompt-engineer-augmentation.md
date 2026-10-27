---
type: strategy
id: test-classifiers-and-prompt-engineer-augmentation
title: Test multiple classifier models with augmented data and prompt-engineer the generator to find the best augmentation setup
description: "A practical recipe drawn from the study's findings: because classifier models \"do not rise in performance equally\", practitioners should augment their training data, apply additional fine-tuning to several candidate B..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
sources:
  - id: keith-cochran-2025
    resource: "https://doi.org/10.1007/s40593-025-00473-x"
    title: "Keith Cochran, Clayton Cohn, Jean-François Rouet, Peter Hastings. (2025). Comparing Text Augmentation by GPT-3.5 and Llama3 for Evaluating Student Responses. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00473-x"
    author: Keith Cochran, Clayton Cohn, Jean-François Rouet, Peter Hastings
---

# Test multiple classifier models with augmented data and prompt-engineer the generator to find the best augmentation setup

> **Strategy** · [All strategies](index.md)
> **Evidence** · 7 claims (4 for, 3 mixed) · 2 studies (1 causal, 1 design), `q2` · 0 of 2 report an effect size · 7 claims rest on one study

## Description
A practical recipe drawn from the study's findings: because classifier models "do not rise in performance equally", practitioners should augment their training data, apply additional fine-tuning to several candidate BERT-based models, and keep training "until peak model performance is achieved". The authors further suggest future gains from prompt engineering that guides generators toward more suitable alternative texts rather than simple rewording. In the study this meant fine-tuning 15,120 model configurations and comparing six augmentation methods by micro-F1.

## Design Implications

### Context
#### Requirements
- Access to at least two pre-trained BERT-based classifiers suitable for the target language
- Sufficient labeled student responses to balance and augment per label
- Compute resources for repeated fine-tuning; the study needed over eight weeks of continuous GPU usage
#### Constraints
- The efficacy of the resulting feedback to students was beyond the scope of the paper
- The best augmentation level varied with the dataset and model chosen, so it must be determined empirically

### Target Learners
- K-12 students whose written responses are automatically evaluated

### Target Learning Goals
- Accurate automated classification of student written responses for timely feedback

## Claims

- [Fine-tuning BERT-based classifiers on LLM-augmented student-response data outperforms unaugmented training for all tested concepts](../claims/llm-augmentation-beats-unaugmented-small-education-data.md) [+W]
- [LLM-generated responses outperform self-augmentation when augmenting small educational classification datasets](../claims/llm-generated-beats-self-augmentation.md) [+W]
- [Augmentation levels below 20x produce unreliable classification performance in small educational datasets](../claims/low-augmentation-levels-unreliable.md) [+W]
- [Datasets with entropy below 0.5 are difficult to augment enough to beat majority-label guessing](../claims/low-entropy-datasets-resist-augmentation.md) [~W]
- [Self- and GPT-augmented performance peaks and degrades after 55x–89x augmentation, while Llama-augmented performance keeps rising toward 100x](../claims/performance-peak-augmentation-llama-rises.md) [~W]
- [Higher LLM temperature settings yield the best English augmentation performance, with Llama temperature 2 the top generator overall](../claims/temperature-affects-augmentation-performance.md) [+W]
- [In the Overview dimension, augmentation produced a marginal QWK decrease (ΔQWK = −0.006) despite improving macro-F1, the only dimension with this trade-off](../claims/overview-augmentation-qwk-tradeoff.md) [~W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Keith Cochran, Clayton Cohn, Jean-François Rouet, Peter Hastings. (2025). Comparing Text Augmentation by GPT-3.5 and Llama3 for Evaluating Student Responses. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00473-x
