---
type: element
id: epistemic-network-analysis-weighted-density
title: Epistemic network analysis and its weighted density statistic for analyzing SKIVE element co-occurrence in epistemic games
description: Epistemic network analysis (ENA) is a non-parametric analytic method developed for epistemic game data; the article focuses on its social-network based variant.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-26
sources:
  - id: sweet-2012
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM"
    title: "Sweet, S. J., & Rupp, A. A. (2012). Using the ECD Framework to Support Evidentiary Reasoning in the Context of a Simulation Study for Detecting Learner Differences in Epistemic Games. Journal of Educational Data Mining, Special Issue, Article 5, Volume 4. https://jedm.educationaldatamining.org/index.php/JEDM"
    author: "Sweet, S. J., & Rupp, A. A"
---

# Epistemic network analysis and its weighted density statistic for analyzing SKIVE element co-occurrence in epistemic games

> **Element** · [All elements](index.md)
> **Evidence** · 6 claims (6 for) · 2 studies (1 design, 1 theoretical), `q2` · 1 of 2 report an effect size · 6 claims rest on one study

## Description
Epistemic network analysis (ENA) is a non-parametric analytic method developed for epistemic game data; the article focuses on its social-network based variant. Chat utterances are automatically scored into binary indicators of SKIVE element use, aggregated into adjacency and cumulative adjacency matrices across evidentiary segments. The weighted density (WD) statistic summarizes, for each learner, "the total number of unique pair-wise associations / connections between SKIVE elements", and the article evaluates its utility via a simulation study in Land Science.

## Design Implications

### Context
#### Requirements
- Utterances coded automatically at a fine grain size into binary indicators of SKIVE element use, organized into evidentiary segments
- Adjacency and cumulative adjacency matrices built from the binary codes, from which WD is computed
#### Constraints
- The article notes that for these data "there is currently no prototypical statistical analytic method – certainly no parametric one that we know of – that can be applied directly to these data"

### Target Learners
- individual learners playing epistemic games such as Land Science
- pairs of learners collaborating via group chat

### Target Learning Goals
- characterizing emerging expertise as connections among skills, knowledge, identity, values, and epistemological reasoning elements
- summarizing accumulated evidence of mastery across evidentiary segments

### Claims
<!-- Claims bearing on this element, each a link to a claim page followed by its evidence tag, e.g. [+M] -->
- [In the simulation, task complexity and task difficulty explain the majority of variance in the individual-learner WD statistic, with some effect of task specificity](../claims/task-complexity-and-difficulty-dominate-wd-variance.md) [+W]
- [In simulated epistemic games, the weighted density statistic distinguishes simulated learner types with distinct mastery trajectories, with the expert trajectory showing the largest WD values](../claims/wd-detects-simulated-learner-trajectory-differences.md) [+W]
- [The WD statistic is more useful for differentiating between simulated learner types when games are played longer](../claims/longer-games-sharpen-wd-learner-differentiation.md) [+W]
- [In pairwise WD analyses, learner trajectory similarity dominates variation in percentage-overlap values (57.90% of variation) while remaining design factors are essentially zero](../claims/trajectory-similarity-dominates-wd-pair-overlap.md) [+W]
- [Easy, highly specific simulated tasks compress the range of the WD statistic across learner types, while well-designed tasks widen it](../claims/easy-highly-specific-tasks-shrink-wd-range.md) [+W]
- [Segmentation boundary choices differentially affect statistics computed on epistemic-game process data](../claims/segmentation-boundaries-differentially-affect-statistics.md) [+W]

## Related Elements
- 

## Examples

- [Use the WD statistic during gameplay as a quick screening tool for pairing learners with likely different profiles](../strategies/wd-gameplay-screening-for-learner-pairing.md)

## Key Sources
- Sweet, S. J., & Rupp, A. A. (2012). Using the ECD Framework to Support Evidentiary Reasoning in the Context of a Simulation Study for Detecting Learner Differences in Epistemic Games. Journal of Educational Data Mining, Special Issue, Article 5, Volume 4. https://jedm.educationaldatamining.org/index.php/JEDM
