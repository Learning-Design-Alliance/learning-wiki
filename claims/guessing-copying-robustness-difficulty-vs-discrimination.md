---
type: claim
title: Simulated guessing and copying rapidly degrade item difficulty estimates beyond about one-third occurrence, while discrimination and ability estimates remain robust past two-thirds, with no graceful degradation
description: Simulated guessing and copying rapidly degrade item difficulty estimates beyond about one-third occurrence, while discrimination and ability estimates remain robust past two-thirds, with no graceful degradation
id: guessing-copying-robustness-difficulty-vs-discrimination
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
evidence_strength: moderate
newest_evidence: 2014
recheck_by: 2017
sources:
  - id: gerd-kortemeyer-2014
    resource: "https://doi.org/10.1103/physrevstper.10.010118"
    title: "Gerd Kortemeyer. (2014). Extending Item Response Theory to Online Homework. [doi:10.1103/physrevstper.10.010118](https://doi.org/10.1103/physrevstper.10.010118)"
    author: Gerd Kortemeyer
    q: 1
    i: "?"
    kind: associational
    rigour: 2
  - id: gerd-kortemeyer-2014-2
    resource: "https://doi.org/10.1103/physrevstper.10.010118"
    title: "Gerd Kortemeyer. (2014). Extending Item Response Theory to Online Homework. [doi:10.1103/physrevstper.10.010118](https://doi.org/10.1103/physrevstper.10.010118)"
    author: Gerd Kortemeyer
    q: 1
    i: "?"
    kind: associational
    rigour: 1
---

# Simulated guessing and copying rapidly degrade item difficulty estimates beyond about one-third occurrence, while discrimination and ability estimates remain robust past two-thirds, with no graceful degradation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1`–`r2` · `q1`
> **Currency** · newest study 2014 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2017**: tool and model accuracy changes quickly

## Subclaims
`q1 i?` In simulation, item difficulty estimates rapidly lose agreement with clean exam values once more than a third of solutions are guessed or copied. [→ Gerd Kortemeyer 2014](#gerd-kortemeyer-2014)
`q1 i?` Discrimination and learner ability estimates show good agreement with clean exam values until more than two thirds of solutions are guessed or copied, then break down rapidly with no graceful degradation. [→ Gerd Kortemeyer 2014 (2)](#gerd-kortemeyer-2014-2)

## Evidence

### Gerd Kortemeyer 2014

Gerd Kortemeyer. (2014). Extending Item Response Theory to Online Homework. [doi:10.1103/physrevstper.10.010118](https://doi.org/10.1103/physrevstper.10.010118)

`q1 · i?` · `associational · r2`

Simulation adding guessing/copying noise to the clean exam response matrix via two parameters (occurrence percentage and success rate of 10%, 50%, 90%), tracing difficulty-estimate decay in Fig. 6. The article reports difficulty estimates are "very sensitive to the introduced noise."

> "Already if more than a third of the problem solutions are guessed or copied, the cosine similarity of the diﬃculty estimates rapidly decreases."

### Gerd Kortemeyer 2014 (2)

Gerd Kortemeyer. (2014). Extending Item Response Theory to Online Homework. [doi:10.1103/physrevstper.10.010118](https://doi.org/10.1103/physrevstper.10.010118)

`q1 · i?` · `associational · r1`

The same simulation traced for discrimination (Fig. 7) and learner ability (Fig. 8) cosine similarities. The article reports "good agree- ment with the original discrimination and ability esti- mates until more then two thirds" of solutions are guessed or copied.

> "Fig. 7 and Fig. 8 show good agree- ment with the original discrimination and ability esti- mates until more then two thirds of the problem solu- tions are guessed or copied."

## Discussion


## Related Claims
- [The simulated-respondent approach recovers the guessing parameter c at correlation 0.48, far above regression baselines, suggesting it captures genuine response behavior](simulated-respondents-recover-guessing-parameter-048.md) — related
- [Discrimination parameter recovery is weak (Pearson 0.31 for Qwen3.5-9B, below MathBERT's 0.35), with slope information partially lost through ability discretization](weak-discrimination-parameter-recovery.md) — related
- [E-M scoring leaves residual score distortion, suggesting some disengaged test responses are nonrapid rather than rapid guesses](nonrapid-disengaged-responses-residual-distortion.md) — related
- [Both item-level and test-level analyses indicate the MAP Growth measurement scales are remaining stable](map-growth-scales-remaining-stable.md) — related
- [Copying occurs on average about 12% of initial submissions nearly independent of ability, while low-ability students guess more than high-ability students](copying-12-percent-guessing-ability-dependent.md) — related
- [Introducing the learner traits stabilizes item parameter estimates: difficulty divergence is absorbed and more items show positive discrimination](learner-traits-stabilize-item-parameters.md) — related
- [System accuracy degrades progressively as noise increases, reaching zero accuracy at 98% noise](bci-accuracy-degrades-to-zero-at-98-percent-noise.md) — related
