---
type: strategy
id: nlg-automatic-support-mooc-forums-strategy
title: Use deep-learning NLG models to provide automatic social support to MOOC learners on discussion forums
description: "The authors propose automatic text generation as a response to scarce peer interaction in MOOC forums, where manual support from instructors and learners is infeasible \"given the vast quantity of learners on MOOCs\"."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
sources:
  - id: chenglu-li-wanli-xing-2021
    resource: "https://doi.org/10.1007/s40593-020-00235-x"
    title: "Chenglu Li & Wanli Xing. (2021). Natural Language Generation Using Deep Learning to Support MOOC Learners. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00235-x"
    author: "Chenglu Li & Wanli Xing"
---

# Use deep-learning NLG models to provide automatic social support to MOOC learners on discussion forums

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 3 studies (1 causal, 1 review, 1 design), `q1`–`q2` · 0 of 3 report an effect size · 4 claims rest on one study

## Description
The authors propose automatic text generation as a response to scarce peer interaction in MOOC forums, where manual support from instructors and learners is infeasible "given the vast quantity of learners on MOOCs". The strategy is to train deep-learning NLG models on a course's post-reply pairs and deploy them to generate replies offering informational, emotional, and community support. Their evidence indicates GPT-2 is the preferable candidate model, with support profiles close to human replies except for informational support.

## Design Implications

### Context
#### Requirements
- A corpus of post-reply pairs from the target or a similar course for fine-tuning
- Quantitative evaluation (perplexity, readability, coherence) before deployment to select the model
#### Constraints
- Informational support of generated replies was significantly weaker than human replies; near-duplicate replies can occur

### Target Learners
- MOOC learners

### Target Learning Goals
- Increased forum participation and reduced isolation and dropout through automated supportive replies

### Affordances
- Social Support Theory Three Categories Mooc

## Claims

- [GPT-2 outperformed an LSTM-based RNN on word perplexity, readability, and cosine-similarity coherence when generating MOOC forum replies](../claims/gpt2-outperformed-rnn-mooc-nlg.md) [+W]
- [A small validation survey found the trained GPT-2 model generated supportive, contextual replies comparable to humans and generalizable to a new similar MOOC](../claims/gpt2-survey-validation-generalizable.md) [+W]
- [The special issue reports that a GPT-2 model could provide supportive and contextual replies to MOOC learners to a similar extent as humans](../claims/gpt2-mooc-forum-replies-similar-to-humans.md) [+W]
- [Gemma and LLaMA produce higher-quality responses than GPT-2 by TIGERSCORE, with accuracy and comprehension gaps remaining](../claims/gemma-llama-outperform-gpt2-tigerscore.md) [+W]

## Related Strategies

- [Facilitating Discourse (Online)](facilitating-discourse-online.md)

## Examples
-

## Key Sources
- Chenglu Li & Wanli Xing. (2021). Natural Language Generation Using Deep Learning to Support MOOC Learners. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00235-x
