---
type: theory
id: exponential-forgetting-curve-with-item-difficulty
title: Exponential Forgetting Curve with Item Difficulty
description: The article adopts a variant of the exponential forgetting curve, in which recall is binary and recall probability decays exponentially with time since last review at a rate reduced by memory strength.
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-09-24
sources:
  - id: reddy-2016
    resource: "https://doi.org/10.1145/2939672.2939850"
    title: "Reddy, S., Labutov, I., Banerjee, S., & Joachims, T. (2016). Unbounded Human Learning: Optimal Scheduling for Spaced Repetition. KDD ’16, San Francisco, CA, USA. https://doi.org/10.1145/2939672.2939850"
    author: "Reddy, S., Labutov, I., Banerjee, S., & Joachims, T"
---

# Exponential Forgetting Curve with Item Difficulty

> **Theory** · [All theories](index.md)
> **Evidence** · 13 claims (10 for, 1 mixed, 2 against) · 7 studies (5 causal, 1 design, 1 theoretical), `q2`–`q3` · 2 of 7 report an effect size · 13 claims rest on one study

## Description
The article adopts a variant of the exponential forgetting curve, in which recall is binary and recall probability decays exponentially with time since last review at a rate reduced by memory strength. It adds that "there is a constant, item-speciﬁc component of the memory decay rate" through a difficulty parameter, and its final form uses Leitner deck position as strength with a global difficulty.

## Design Implications

### Context
#### Requirements
- Log data giving the delay since last review and the item's Leitner deck position (or review count) for each interaction.
- Recall outcomes discretized to binary; in the Mnemosyne data, self-reported grades of 2 or higher count as recall.
#### Constraints
- The authors say the choice between item-specific and global difficulty is less clear from the data; the global form is chosen for practicality and tractability.
- The authors call for more sophisticated memory models that more accurately predict the effect of a review schedule on retention.

### Target Learners
- Users of flashcard software such as Mnemosyne

### Target Learning Objectives
- Predicting recall of flashcard items
- Retention of reviewed items over time

### Claims

- [Delay Term Improves Exponential Forgetting Curve Recall Prediction](../claims/delay-term-improves-exponential-forgetting-curve-recall-prediction.md) [+M]
- [Leitner Deck Position Predicts Recall Better Than Review Count](../claims/leitner-deck-position-predicts-recall-better-than-review-count.md) [+M]
- [Exponential Forgetting Models With Delay Perform Comparably To 1Pl Irt](../claims/exponential-forgetting-models-with-delay-perform-comparably-to-1pl-irt.md) [+M]
- [Item Specific Difficulty Helps Only At Low And High Leitner Decks](../claims/item-specific-difficulty-helps-only-at-low-and-high-leitner-decks.md) [~M]
- [Memory-decay-based models fit fact-learning datasets better than models insensitive to memory decay](../claims/memory-features-improve-fit-for-fact-learning-datasets.md) [+W]
- [Models able to weight performance by recency fit better on the Assistments and KDD datasets, without explicit memory-decay terms being necessary](../claims/recency-weighting-models-better-assistments-kdd.md) [-W]
- [For Chinese tone learning, simpler models insensitive to memory decay fit as well as or better than memory-feature models](../claims/simpler-models-sufficient-for-tone-learning.md) [-W]
- [The retention-interval main effect shows forgetting occurred over one week in both experiments](../claims/one-week-forgetting-main-effect-both-experiments.md) [+W]
- [The scheduling model fit the experimental data well, correlating strongly with actual final-test performance (r = 0.775) with AUC = 0.871](../claims/model-fit-recall-prediction-accuracy.md) [+W]
- [Retention declines with interval (time-dependent forgetting) across images, details, and details-per-image measures](../claims/time-dependent-forgetting-across-intervals.md) [+W]
- [Spacing effects are not always monotonic: the model captured Young's (1971) nonmonotonic spacing function](../claims/nonmonotonic-spacing-effect-young-fit.md) [+W] — attached 2026-11-26 from Philip I. Pavlik Jr. (2005), which proposed "Activation-based decay model: the long-term benefit of each practice depends on activation at the time of presentation"; tests this page's relationship.
- [MCM's parameter-free predictions match the peaks of seven spacing functions, with the optimal ISI increasing with the retention interval](../claims/mcm-parameter-free-spacing-function-predictions.md) [+W] — attached 2026-11-28 from Mozer et al. (2008), which proposed "Multiscale Context Model (MCM): a synthesis of SAM and MTS predicting the spacing function from the forgetting function".
- [MCM predicts different optimal ISIs for two different types of material studied with identical ISI and RI conditions](../claims/mcm-material-specific-peak-prediction.md) [+W] — attached 2026-11-28 from Mozer et al. (2008), which proposed "Multiscale Context Model (MCM): a synthesis of SAM and MTS predicting the spacing function from the forgetting function".

## The evidence by question
- *Does a learner model that tracks memory decay since the last review predict recall better than one that ignores it, and for which kinds of material?* [Memory-decay-based models fit fact-learning datasets better than models insensitive to memory decay](../claims/memory-features-improve-fit-for-fact-learning-datasets.md) [+M]

## Related Theories
- [Spaced Repetition](../elements/spaced-repetition.md)

## Examples

- [Learning decomposition: fit exponential learning curves to compare the relative effectiveness of types of pedagogical support](../strategies/learning-decomposition-compare-support-effectiveness.md)
- [Optimize which items appear in each study session using recall-probability-based selection probabilities](../strategies/recall-probability-item-selection-strategy.md)
- [Add reinforcement activities such as reflective exercises, spaced repetition, and active recall after technology-supported tasks](../strategies/reinforcement-activities-after-genai-tasks.md)

## Key Sources
- Reddy, S., Labutov, I., Banerjee, S., & Joachims, T. (2016). Unbounded Human Learning: Optimal Scheduling for Spaced Repetition. KDD ’16, San Francisco, CA, USA. https://doi.org/10.1145/2939672.2939850
