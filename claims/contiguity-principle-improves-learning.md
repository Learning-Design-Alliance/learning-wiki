---
type: claim
title: Contiguity Principle Improves Learning
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: contiguity-principle-improves-learning
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

# Contiguity Principle Improves Learning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q4` pre-registered or meta-analytic · `i2` medium · n=2426 (58 independent comparisons)

Presenting corresponding words and pictures near each other in space (spatial contiguity) and in time (temporal contiguity) improves learning compared with separated presentation.

## Subclaims

`q4 i2` A meta-analysis of 58 independent comparisons (n=2426) found that spatially integrating mutually referring text and diagrams produced a medium-to-large learning benefit over spatially separated presentation, g=0.63. [→ Schroeder Cenkci 2018](#schroeder-cenkci-2018)

## Evidence

### Schroeder Cenkci 2018

Schroeder, N. L., & Cenkci, A. T. (2018). Spatial contiguity and spatial split-attention effects in multimedia learning environments: A meta-analysis. *Educational Psychology Review, 30*(3), 679–701. [doi:10.1007/s10648-018-9435-9](https://doi.org/10.1007/s10648-018-9435-9)

`q4 · random-effects meta-analysis` · `i2 · medium-to-large effect, g=0.63` · `n=2426 (58 independent comparisons)`

A random-effects meta-analysis pooled 58 independent comparisons (total n=2426) drawn from the multimedia-learning literature contrasting spatially integrated designs (text and diagrams placed together) against spatially separated designs requiring learners to search back and forth between sources. Integrated designs produced an overall effect size of g=0.63 (p<0.001), a medium-to-large advantage consistent with the split-attention/spatial-contiguity account: physically co-locating mutually referring information removes the search-and-match burden that separated presentation imposes on working memory. The authors also examined numerous intervention- and context-related moderators and found the benefit held broadly across them, though (per the abstract) more remained to be understood about exactly which conditions maximize the effect.

## Discussion

**What the recorded evidence covers.** The meta-analysis above tests spatial contiguity only (integrated against separated text and graphics). Temporal contiguity, narration presented at the same time as the animation it describes, is not tested by anything recorded here.

The contiguity principle is one of the core principles of [Cognitive Load Theory](../theories/cognitive-load-theory.md) and Mayer's multimedia learning research. The proposed mechanism is that when corresponding words and images are separated — a caption on a different page from its diagram, or narration delivered long before or after the animation it describes — learners must hold one representation in working memory while searching for its partner, imposing extraneous load that displaces [schema construction](../principles/cognitive-load-management.md). Integrating them reduces that load, consistent with the broader claim that [cognitive load reduction improves learning](../claims/cognitive-load-reduction-improves-learning.md) [+S].

Two variants are usually distinguished:

- **Spatial contiguity.** Printed words should be placed on or next to the part of the graphic they describe, rather than in a caption box or separate legend. This is closely related to the split-attention effect, where physically integrating multiple sources of information removes the need to mentally integrate them [+M].
- **Temporal contiguity.** Narration and animation should be presented simultaneously rather than successively. Successive presentation forces learners to hold the first representation in memory until the second arrives [+M].

Boundary conditions follow from the same mechanism. Integration benefits are largest for novices and for complex, element-interactive material; for experts, integrated formats can become redundant and even hurt performance, consistent with the [expertise reversal effect](../theories/expertise-reversal-effect.md) [~M]. Spatial integration can also backfire when the graphic is simple enough that separation imposes little search cost, or when on-screen text placement occludes essential parts of a dynamic visual [-W].

**Open questions.** Most supporting evidence comes from short laboratory-style multimedia lessons; effects in longer, authentic curricula and with interactive or learner-paced media are less well established [~W]. The relative contribution of spatial versus temporal contiguity when both are manipulated together also remains underexplored.

**Design implications.** In practice, contiguity is usually cheap to implement: place labels directly on diagram parts instead of numbered legends, keep captions on the same screen as their figures, and synchronize narration with the animation segment it describes rather than playing it before or after. In slide-based and video instruction, this means avoiding "title first, diagram later" layouts and avoiding narration that runs ahead of the visuals. Because the mechanism is load reduction rather than added content, contiguity improvements should not increase lesson duration — a useful sanity check that the change is targeting extraneous, not germane, load.

## Related Claims

- [Coherence principle: irrelevant material hurts learning.](coherence-principle-irrelevant-material-hurts-learning.md) — sister multimedia principle: removing extraneous material complements integrating word–picture pairs
- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — the working-memory mechanism contiguity is designed to prevent
- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — related load-reduction strategy operating on information structure rather than layout
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) — the theoretical framework in which split-attention and contiguity effects were developed