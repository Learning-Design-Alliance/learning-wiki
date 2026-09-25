---
type: claim
title: Split Attention Effect Integration Improves Learning
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: split-attention-effect-integration-improves-learning
evidence_strength: moderate
sources:
  - id: schroeder-cenkci-2018
    resource: "https://doi.org/10.1007/s10648-018-9435-9"
    title: "Schroeder, N. L., & Cenkci, A. T. (2018). Spatial contiguity and spatial split-attention effects in multimedia learning environments: A meta-analysis. *Educational Psychology Review, 30*(3), 679–701. [doi:10.1007/s10648-018-9435-9](https://doi.org/10.1007/s10648-018-9435-9)"
    author: "Schroeder, N. L., & Cenkci, A. T."
    q: 4
    i: 2
    n: 2426 (58 independent comparisons)
---

# Split Attention Effect Integration Improves Learning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q4` pre-registered or meta-analytic · `i2` medium · n=2426 (58 independent comparisons)

When instructional material requires learners to mentally integrate information that is physically or temporally separated (e.g., a diagram with its explanation placed elsewhere), presenting the sources in an integrated format reduces extraneous cognitive load and improves learning.

## Subclaims

`q4 i2` A meta-analysis of 58 independent comparisons (n=2426) found that spatially integrating mutually referring text and diagrams produced a medium-to-large learning benefit over spatially separated presentation, g=0.63. [→ Schroeder Cenkci 2018](#schroeder-cenkci-2018)

## Evidence

### Schroeder Cenkci 2018

Schroeder, N. L., & Cenkci, A. T. (2018). Spatial contiguity and spatial split-attention effects in multimedia learning environments: A meta-analysis. *Educational Psychology Review, 30*(3), 679–701. [doi:10.1007/s10648-018-9435-9](https://doi.org/10.1007/s10648-018-9435-9)

`q4 · random-effects meta-analysis` · `i2 · medium-to-large effect, g=0.63` · `n=2426 (58 independent comparisons)`

A random-effects meta-analysis pooled 58 independent comparisons (total n=2426) drawn from the multimedia-learning literature contrasting spatially integrated designs (text and diagrams placed together) against spatially separated designs requiring learners to search back and forth between sources. Integrated designs produced an overall effect size of g=0.63 (p<0.001), a medium-to-large advantage consistent with the split-attention/spatial-contiguity account: physically co-locating mutually referring information removes the search-and-match burden that separated presentation imposes on working memory. The authors also examined numerous intervention- and context-related moderators and found the benefit held broadly across them, though (per the abstract) more remained to be understood about exactly which conditions maximize the effect.

## Discussion

**Mechanism.** Split attention is a core extraneous-load effect within [Cognitive Load Theory](../theories/cognitive-load-theory.md). When two mutually referring sources of information (such as a diagram and a caption, or a graphic and narrated text) are separated in space or time, learners must hold one source in working memory while searching for the other, consuming working-memory resources that would otherwise support schema construction. Physically integrating the sources — embedding labels in a diagram, placing text adjacent to the relevant graphic element — or temporally synchronizing them removes the need for this search-and-hold process [~M].

**Boundary conditions.** Integration is only beneficial when the separated sources are *mutually indispensable*: each is unintelligible without the other. When one source is redundant (e.g., a caption that fully restates what the diagram shows), integrating or presenting both can impose unnecessary load, and removing the redundant source is preferable — see [Coherence principle: irrelevant material hurts learning.](coherence-principle-irrelevant-material-hurts-learning.md) [~M]. Integration may also lose its benefit, or reverse, as expertise develops, because experts can self-integrate separated sources and may find integrated formats redundant — consistent with the [expertise reversal effect](../theories/expertise-reversal-effect.md) [~M]. Integration also does not help when sources can be understood sequentially and independently; in that case separation imposes little or no integration cost.

**Open questions.** Most supporting work comes from controlled laboratory-style experiments with novices in technical domains (geometry, statistics, electrical circuits). Generalization to long-form digital learning environments, mobile layouts, and learner-controlled integration (e.g., allowing learners to toggle between split and integrated views) remains under-researched [~W].

**Design implications.** For novice audiences, designers should place explanatory text directly at the point of reference on a graphic, embed labels within diagrams rather than in legends, and temporally synchronize narration with the animation segment it describes. Before integrating, check whether each source is indispensable; if not, cut the redundant one rather than merging it. These recommendations pair naturally with [Cognitive Load Management](../principles/cognitive-load-management.md) and [Chunking](../principles/chunking.md) when structuring complex multimedia materials.

## Related Claims

- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — the working-memory bottleneck that split attention exploits
- [Coherence principle: irrelevant material hurts learning.](coherence-principle-irrelevant-material-hurts-learning.md) — the complementary extraneous-load effect governing when to remove rather than integrate material
- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — a related strategy for managing working-memory constraints
- [Cognitive Load Reduction Improves Learning](cognitive-load-reduction-improves-learning.md) — the broader claim that reducing extraneous load benefits outcomes
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) — the theoretical framework in which the split-attention effect is situated