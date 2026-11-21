---
type: strategy
id: llm-deterrence-strategies-online-lessons
title: Pair detection models with deterrence strategies such as embedded white-text LLM instructions, audio-visual formats, and disabled copy-paste
description: The article recommends pairing detection models with deterrence strategies that discourage LLM use or aid identification in self-paced online lessons.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: bhushan-2025
    resource: "https://arxiv.org/abs/2506.17196"
    title: "Bhushan, S., Thomas, D.R., Borchers, C., Raghuvanshi, I., Abboud, R., Gatz, E., Gupta, S., Koedinger, K.R. (2025). Detecting LLM-Generated Short Answers and Effects on Learner Performance. https://arxiv.org/abs/2506.17196"
    author: Bhushan, S., Thomas, D.R., Borchers, C., Raghuvanshi, I., Abboud, R., Gatz, E., Gupta, S., Koedinger, K.R
---

# Pair detection models with deterrence strategies such as embedded white-text LLM instructions, audio-visual formats, and disabled copy-paste

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 design), `q2` · 1 of 1 report an effect size · 5 claims rest on one study

## Description
The article recommends pairing detection models with deterrence strategies that discourage LLM use or aid identification in self-paced online lessons. Proposed measures include "embedding white text in scenarios with specific instructions for the LLM", employing audio-visual formats to prevent copying, and disabling copy-and-paste entirely. The authors state these strategies "not only reduce AI misuse but also make detection easier" and could also mitigate paraphrasing-tool use.

## Design Implications

### Context
#### Requirements
- Detection models paired with the deterrence measures in low-stakes online lesson scenarios
#### Constraints
- The article notes paraphrasing tools remain a significant concern and that paraphrased responses should be added to training data to improve detection

### Target Learners
- Adult learners in self-paced online micro-lessons with limited supervision

### Target Learning Goals
- Preserving academic integrity and genuine engagement with instructional material

## Claims

- [A fine-tuned GPT-4o model outperforms GPTZero at detecting LLM-generated short answers in an online lesson, achieving 80% accuracy versus GPTZero's 70%](../claims/fine-tuned-gpt4o-outperforms-gptzero-short-answers.md) [+W]
- [The fine-tuned model generalized to out-of-domain lessons with 77% overall accuracy](../claims/fine-tuned-model-out-of-domain-77.md) [+W]
- [GPTZero fails entirely on ambiguous responses, scoring an F1 of 0.00 on the uncertain class in the in-domain test set](../claims/gptzero-fails-uncertain-class.md) [+W]
- [Learners suspected of LLM misuse had significantly higher odds of answering the corresponding posttest MCQ correctly (OR = 2.37, p < .001)](../claims/llm-misuse-higher-posttest-odds.md) [+W]
- [A stylometric logistic-regression baseline outperformed GPTZero, achieving 77% accuracy on short-answer detection](../claims/stylometric-baseline-beats-gptzero.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Bhushan, S., Thomas, D.R., Borchers, C., Raghuvanshi, I., Abboud, R., Gatz, E., Gupta, S., Koedinger, K.R. (2025). Detecting LLM-Generated Short Answers and Effects on Learner Performance. https://arxiv.org/abs/2506.17196
