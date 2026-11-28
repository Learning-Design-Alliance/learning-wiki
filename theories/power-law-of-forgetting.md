---
type: theory
id: power-law-of-forgetting
title: Power Law of Forgetting
description: "Retention falls with time as a power function (or another negatively accelerated curve of the same family, such as the hyperbola), steep at first and ever slower, rather than at the constant rate an exponential curve implies."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-11-28
---

# Power Law of Forgetting

> **Theory** · [All theories](index.md)
> **Evidence** · 11 claims (4 for, 7 mixed) · 2 studies (1 causal, 1 quant-synthesis), `q2` · 0 of 2 report an effect size · 11 claims rest on one study

## Description
The power law of forgetting holds that retention declines with the time since learning as a power function, R = a·t^-b: most of the loss comes early, and the rate of loss keeps slowing as time passes. Wixted and Ebbesen (1991) compared six candidate functions across word recall, face recognition, pigeon delayed matching-to-sample and a reanalysis of Ebbinghaus's savings data, and the simple power function accounted for the most variance in each. Rubin and Wenzel (1996) fitted 105 two-parameter functions to 210 published retention data sets. Four fitted best and could rarely be told apart: the logarithmic, the power, the exponential in the square root of time and the hyperbola in the square root of time. All four fall more slowly over time than an exponential does.

The family matters for models that schedule practice. A hyperbolic retrievability term, R = 1/(1 + t/h), belongs to it and is what spaced-repetition schedulers use; the exponential curve, R = e^(-t/h), is its main rival ([Exponential Forgetting Curve with Item Difficulty](exponential-forgetting-curve-with-item-difficulty.md)). Rubin and Wenzel's result is a caution for any model that commits to one form: with the data available, the power, logarithmic and square-root-of-time curves fit about equally well.

## Implications

### Context
- Retention measured by recall, recognition or d' under constant response bias, over intervals from seconds to weeks.
- The fit holds for most data sets regardless of participant population and materials when initial learning is controlled; testing procedure changes the shape more.

### Target Learners
- Adults and children in laboratory memory studies; Rubin and Wenzel report that retention, as distinct from initial learning, does not change with age over the ages tested.

### Target Learning Objectives
- Retention of verbal material, faces and associations over a delay.

## Claims
- [Forgetting across recall, recognition, and animal memory tasks is best described by a simple power function of time relative to five alternatives](../claims/forgetting-follows-power-function.md) [+M]
- [In short-term free recall of words, the power function fit the forgetting curve best (98.0% variance accounted for)](../claims/word-recall-power-function-fit.md) [+M]
- [Ebbinghaus's 1885 savings function, reanalyzed, declines as a power function of time (97.8% variance accounted for)](../claims/ebbinghaus-savings-power-function.md) [+M]
- [When d' is the dependent measure under constant response bias, forgetting also declines as a power function of time](../claims/d-prime-forgetting-power-function.md) [+M]
- [Across 210 retention data sets, the best-fitting two-parameter functions are the logarithmic, power, exponential-in-square-root-of-time, and hyperbola-in-square-root-of-time functions](../claims/four-best-fitting-retention-functions.md) [~M]
- [The four best-fitting retention functions are difficult to distinguish with available data, and the same set of four fits most data sets except autobiographical memory](../claims/retention-functions-indistinguishable-autobiographical-exception.md) [~M]
- [Participant population and materials have little effect on retention-function shape when initial learning level is controlled; testing procedures have a minor influence except savings](../claims/retention-shape-robust-to-population-materials.md) [~M]
- [Relearning measured in percent savings yields a differently shaped retention function that falls much less rapidly than recall and other standard testing procedures](../claims/savings-retention-function-differs-from-recall.md) [~M]
- [Existing data indicate retention, as opposed to initial learning, is not affected by age over the range of ages tested, or at most only under specific conditions and assumptions](../claims/retention-not-affected-by-age.md) [~M]
- [Fitting retention functions to untransformed versus transformed data changes the r2 values but not the rank ordering of the four common functions](../claims/untransformed-fits-preserve-function-ranking.md) [~M]
- [The power law of forgetting has stated scope limits: it may not hold above 90% correct, at very short intervals, or over months to years](../claims/power-law-forgetting-scope-limits.md) [~W]

## Related Theories
- [Exponential Forgetting Curve with Item Difficulty](exponential-forgetting-curve-with-item-difficulty.md): the rival functional form.
- [Activation-Based ACT-R Model of the Spacing Effect](act-r-activation-model-of-spacing.md): its activation equation sums power-law-decaying traces.
- [Multiscale Context Model of Spacing](multiscale-context-model-of-spacing.md): obtains a power-like curve by summing exponential traces on several time scales.

## Examples
- [Spaced learning](../principles/spaced-learning.md)

## Key Sources
- Wixted, J. T., & Ebbesen, E. B. (1991). On the form of forgetting. *Psychological Science, 2*(6), 409-415. [doi:10.1111/j.1467-9280.1991.tb00175.x](https://doi.org/10.1111/j.1467-9280.1991.tb00175.x)
- Rubin, D. C., & Wenzel, A. E. (1996). One hundred years of forgetting: A quantitative description of retention. *Psychological Review, 103*(4), 734-760. [doi:10.1037/0033-295X.103.4.734](https://doi.org/10.1037/0033-295X.103.4.734)
