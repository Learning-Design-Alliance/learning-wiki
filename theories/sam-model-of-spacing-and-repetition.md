---
type: theory
id: sam-model-of-spacing-and-repetition
title: SAM Model of Spacing and Repetition
description: "In Raaijmakers' application of the Search of Associative Memory model, a repeated item adds to its existing memory trace only if that trace is retrieved at the repetition; otherwise a new trace is stored, and context that drifts between presentations makes spaced traces richer in contextual cues."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-11-28
---

# SAM Model of Spacing and Repetition

> **Theory** · [All theories](index.md)
> **Evidence** · 8 claims (3 for, 3 mixed, 2 against) · 3 studies (2 theoretical, 1 causal), `q1`–`q2` · 0 of 3 report an effect size · 8 claims rest on one study

## Description
Raaijmakers (2003) applied the Search of Associative Memory (SAM) theory of Raaijmakers and Shiffrin (1980, 1981) to spacing and repetition, extending the version Mensink and Raaijmakers (1988, 1989) built for interference paradigms. Memory holds traces, or "images", that carry item, associative and contextual information, and recall is a search cued by the test item and the current context. Context fluctuates over time: following Stimulus Sampling Theory, elements move at random between an active set and an inactive set, so the context at a repetition overlaps less with the context at the first presentation the longer the gap.

The spacing assumption is about what a repetition does. If, at the second presentation, the item's existing trace is retrieved, new information is added to that trace; if it is not retrieved, a new trace is stored. A spaced repetition adds contextual elements the first trace lacked, so the trace can be reached from more test contexts later, provided the first trace is still retrieved at the repetition. Raaijmakers describes the model as a mathematical version of Glenberg's (1979) Component-Levels theory. The model reproduces the spacing-by-retention-interval interaction in Rumelhart's (1967) data, a nonmonotonic spacing function in Young's (1971) data, the basic pattern of Glenberg's (1976) data, and the Ross and Landauer (1978) finding that spacing does not help recall of at least one of two different items each presented once.

Mozer et al. (2009) note the model's limit: its single exponential context drift fixes the time scale it can work on, so the same parameters cannot explain spacing over both hours and months. Their [multiscale context model](multiscale-context-model-of-spacing.md) keeps SAM's retrieval-dependent update and contextual drift and adds several time scales.

## Implications

### Context
- Continuous paired-associate and list-learning paradigms with lags measured in items or minutes and short retention intervals.
- At short retention intervals massed presentation can beat spaced presentation, and the model predicts that reversal.

### Target Learners
- Adults in laboratory verbal-learning studies.

### Target Learning Objectives
- Recall of repeated paired associates and list items.

## Claims
- [The SAM spacing model fits Rumelhart's 1967 continuous paired-associate data well and captures a spacing-interval by retention-interval interaction](../claims/sam-spacing-model-fits-rumelhart-1967-interaction.md) [+M]
- [The SAM spacing model can generate non-monotonic spacing effects, as shown by its fit to Young's 1971 data](../claims/sam-model-generates-nonmonotonic-spacing-young-1971.md) [+M]
- [The SAM spacing model captures the basic characteristics of Glenberg's 1976 data, though a competing model fit better on an assumption the article calls artificial](../claims/sam-fit-glenberg-1976-reed-comparison.md) [~M]
- [At short retention intervals massed presentation is superior to spaced presentation, reversing the spacing effect](../claims/massed-superior-short-retention-interval.md) [~M]
- [The SAM spacing model is presented as predicting the Ross–Landauer finding of no spacing effect for recall of at least one of two different items each presented once](../claims/sam-model-predicts-ross-landauer-or-finding.md) [+W]
- [Assuming zero retrieval probability for traces not retrieved at a prior trial simplifies the model while changing predicted recall probabilities by no more than 0.5%](../claims/nonretrieved-trace-assumption-small-effect.md) [~W]
- [Spacing effects occur on many time scales, and the single-scale SAM model cannot explain effects across different time scales](../claims/sam-single-time-scale-limitation.md) [-W]
- [The activation-based ACT–R model closely mirrors the experiment's data and fits better than the Raaijmakers SAM model on the restricted data set](../claims/actr-model-fits-experiment-better-than-sam.md) [-W]

## Related Theories
- [Study-Phase Retrieval (Reminding) Account of the Spacing Effect](study-phase-retrieval-account-of-spacing.md): the verbal account whose retrieval-dependent update SAM formalises.
- [Multiscale Context Model of Spacing](multiscale-context-model-of-spacing.md): extends SAM to several time scales.
- [Activation-Based ACT-R Model of the Spacing Effect](act-r-activation-model-of-spacing.md): a rival computational account.
- [Encoding Specificity Principle](encoding-specificity-principle.md): SAM's contextual cues are a formal version of the idea that retrieval depends on overlap with the encoding context.

## Examples
- [Spaced learning](../principles/spaced-learning.md)

## Key Sources
- Raaijmakers, J. G. W. (2003). Spacing and repetition effects in human memory: Application of the SAM model. *Cognitive Science, 27*(3), 431-452. [doi:10.1207/s15516709cog2703_5](https://doi.org/10.1207/s15516709cog2703_5)
