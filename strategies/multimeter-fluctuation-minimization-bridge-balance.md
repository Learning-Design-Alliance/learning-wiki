---
type: strategy
id: multimeter-fluctuation-minimization-bridge-balance
title: Balance an AC bridge by minimizing display fluctuations of a cheap DC multimeter, simulating a sensitive galvanometer
description: "Where schools lack a sensitive galvanometer, the article has students balance the bridge with an ordinary multimeter: after approximate balancing on the ACV setting, they switch to the most sensitive DCV range (200 mV..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: todor-m-mishonov-2019
    resource: "https://arxiv.org/abs/1912.07368"
    title: "Todor M. Mishonov, Riste Popeski-Dimovski, Leonora Velkoska, Iglika M. Dimitrova, Vassil N. Gourev, Aleksander P. Petkov, Emil G. Petkov, Albert M. Varonov. (2019). The Day of the Inductance. Problem of the 7th Experimental Physics Olympiad, Skopje, 7 December 2019. https://arxiv.org/abs/1912.07368"
    author: Todor M. Mishonov, Riste Popeski-Dimovski, Leonora Velkoska, Iglika M. Dimitrova, Vassil N. Gourev, Aleksander P. Petkov, Emil G. Petkov, Albert M. Varonov
---

# Balance an AC bridge by minimizing display fluctuations of a cheap DC multimeter, simulating a sensitive galvanometer

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Where schools lack a sensitive galvanometer, the article has students balance the bridge with an ordinary multimeter: after approximate balancing on the ACV setting, they switch to the most sensitive DCV range (200 mV), where rectified residuals make the display digits run randomly; balancing is refined by minimizing the spread between the running minimum and maximum readings. As the article states, "In this way we simulate the operation of a sensitive and expensive galvanometer, which is rarely present operational in schools." The same fluctuation-minimization procedure is then used for the inductance measurement in category L.

## Design Implications

### Context
#### Requirements
- A multimeter with a 200 mV DCV range; an alternating voltage applied to the bridge; patience, since the L-category measurements "may take an hour".
#### Constraints
- Described for the case where no sensitive galvanometer is available; the article notes the display digit changes each second due to random values remaining in the averaging capacitors.

### Target Learners
- high-school students without access to sensitive galvanometers

### Target Learning Goals
- bridge balancing technique
- appreciation of measurement precision and fluctuations

## Claims

- [Misinterpretations of multimeter displays after building real circuits confused students and negatively affected performance, leading the author to reject the assumption that experimental skills need no explicit training](../claims/multimeter-misreading-hurts-real-experiment-performance.md) [+W]

## Related Strategies

- [Teach bridge analysis by transforming the π network of r, R2 and Xc into an equivalent T network so the circuit reduces to a familiar Wheatstone topology](pi-to-t-transformation-pedagogical-strategy.md)

## Examples
-

## Key Sources
- Todor M. Mishonov, Riste Popeski-Dimovski, Leonora Velkoska, Iglika M. Dimitrova, Vassil N. Gourev, Aleksander P. Petkov, Emil G. Petkov, Albert M. Varonov. (2019). The Day of the Inductance. Problem of the 7th Experimental Physics Olympiad, Skopje, 7 December 2019. https://arxiv.org/abs/1912.07368
