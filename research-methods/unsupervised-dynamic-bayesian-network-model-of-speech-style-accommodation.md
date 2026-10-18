---
type: research-method
id: unsupervised-dynamic-bayesian-network-model-of-speech-style-accommodation
title: Unsupervised Dynamic Bayesian Network model of speech style accommodation
description: The model measures speech style accommodation from raw speech without labeled data or hand-crafted indexical features.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-18
---

# Unsupervised Dynamic Bayesian Network model of speech style accommodation

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 associational), `q2` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
The model measures speech style accommodation from raw speech without labeled data or hand-crafted indexical features. It uses latent speaking-style states and binary accommodation states over conversational turns, with acoustic-prosodic observation vectors. As the article states, "Our model embodies two premises. First, a person's speech in any turn is a function of his/her speaking style in that turn, which is influenced by their speech style in their previous turn," and style also depends on accommodation to the partner. Parameters are learned with expectation maximization and inference uses the junction tree algorithm; the accommodation score is the fraction of adjacent turns where both partners' most likely style states match.

## Accounts
<!-- How each source describes or uses the method -->
- **Unsupervised Dynamic Bayesian Network model of speech style accommodation motivated by Speech Accommodation Theory**: The model measures speech style accommodation from raw speech without labeled data or hand-crafted indexical features. It uses latent speaking-style states and binary accommodation states over conversational turns, with acoustic-prosodic observation vectors. As the article states, "Our model embodies two premises. First, a person's speech in any turn is a function of his/her speaking style in that turn, which is influenced by their speech style in their previous turn," and style also depends on accommodation to the partner. Parameters are learned with expectation maximization and inference uses the junction tree algorithm; the accommodation score is the fraction of adjacent turns where both partners' most likely style states match. (Gweon et al. (2013))

### Claims
- [The DBN accommodation measure scores real conversation pairs higher than lexically matched constructed pairs, validating it as a measure of speech style accommodation](../claims/dbn-accommodation-score-validates-real-vs-constructed-pairs.md) [+M]
- [An automatic measure of speech style accommodation significantly positively correlates with prevalence of other-oriented transacts in dyadic debates (R = .36, p < .05)](../claims/speech-accommodation-correlates-other-oriented-transacts.md) [+M]

## Related Research Methods
-

## Key Sources
- Gweon, G., Jain, M., McDonough, J., Raj, B., & Rosé, C. P. (2013). Measuring prevalence of other-oriented transactive contributions using an automated measure of speech style accommodation. Computer-Supported Collaborative Learning (2013).
