---
type: element
id: proximity
title: Proximity
description: Placing related text and graphics close together on the page or screen so learners can process them as a single unit rather than searching and holding them in working memory.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Proximity

> **Element** · [All elements](index.md)

## Description
Proximity (spatial contiguity) is the design principle that related pieces of information — a label and the object it names, an explanation and the graphic it describes, feedback and the work it addresses — should be placed near one another rather than separated. When corresponding words and images are integrated, learners do not have to visually search for connections or hold one representation in working memory while locating the other.

## Design Implications

Integrating text with corresponding graphics reduces extraneous cognitive load imposed by visual search and split attention, producing better learning than separated presentations [Integrating text and graphics near each other improves learning compared to separated presentation.](../claims/spatial-contiguity-improves-learning.md) [+S]. The effect is strongest when learners would otherwise need to hold one representation in memory while scanning for its referent — the classic split-attention condition [Split-attention between multiple sources degrades learning when integration is required.](../claims/split-attention-effect-degrades-learning.md) [+S]. Proximity applies at every scale: annotation placement on diagrams, captions under video frames, feedback adjacent to the error, and legend items positioned on the chart itself rather than in a remote key.

### Context
#### Requirements
- A clear correspondence between the verbal and visual elements being integrated — proximity only helps when the elements genuinely refer to each other
- Layout control over the presentation medium (print, slides, screen design); proximity cannot be enacted where the platform forces separation
- Small enough integrated units that the combined display does not itself overload working memory ([Chunking](../principles/chunking.md))

#### Constraints
- Over-integration can clutter a display; when labels and annotations crowd a graphic, the added density becomes its own source of extraneous load [~M] — integrate selectively, not maximally
- Small screens and responsive layouts frequently separate text from graphics; proximity must be re-designed per breakpoint, not assumed from the desktop version
- Proximity does not compensate for incoherent content — placing a confusing explanation next to a confusing diagram yields integrated confusion
- When learners must mentally integrate *temporal* rather than spatial information, proximity alone is insufficient; synchronized presentation ([Modality](../strategies/modality.md), segmenting) is required [~S]

### Target Learners
- Novices, who lack the prior knowledge to hold a separated representation in mind while searching for its referent [Integrating text and graphics near each other improves learning compared to separated presentation.](../claims/spatial-contiguity-improves-learning.md) [+S]
- Low-working-memory learners, who are disproportionately harmed by split-attention layouts [Split-attention between multiple sources degrades learning when integration is required.](../claims/split-attention-effect-degrades-learning.md) [+S]
- Experts may not benefit and can suffer from over-integrated displays, consistent with the expertise-reversal pattern [Guidance that helps novices can hinder experts by forcing redundant processing.](../claims/expertise-reversal-effect.md) [~M]

### Target Learning Goals
- Conceptual understanding of systems, structures, and processes depicted in diagrams or animations
- Terminology learning: binding labels to visual referents
- Interpretation of data displays, maps, and technical illustrations

### Affordances
- [Cognitive Load Management](../principles/cognitive-load-management.md) — proximity directly reduces extraneous load from visual search and split attention, freeing working memory for schema construction
- [Multimedia Learning](../principles/multimedia-learning.md) — spatial contiguity is one of Mayer's core principles for combining words and pictures effectively
- [Clear Structure](../principles/clear-structure-presentation.md) — proximity is a layout-level expression of structure: the physical arrangement signals which elements belong together
- [Signaling](../strategies/signaling.md) — works in concert with proximity; cues direct attention to the correspondences that integrated placement makes physically adjacent

## Related Elements
- [Modality](../strategies/modality.md) — the temporal companion: narrating graphics rather than separating text from them
- [Segmenting](../strategies/segmenting.md) — controls pacing of integrated multimedia so learners can process each unit
- [Signaling](../strategies/signaling.md) — highlights the correspondences that proximity places side by side
- [Worked Examples](worked-examples.md) — step annotations should appear adjacent to the solution lines they explain
- [Feedback](feedback.md) — corrective information placed next to the learner's error is processed more readily than feedback in a separate panel

## Patterns That Use This Element
- [Cognitive Load Reduction](../patterns/cognitive-load-reduction-clt-scaffolding-approach.md) — proximity is a primary technique for eliminating split attention
- [Multimedia Learning Design](../patterns/multimedia-learning.md) — one of the core contiguity principles governing word–image integration
- [Direct Instruction](../patterns/direct-instruction.md) — tightly integrated presentation materials exemplify its emphasis on unambiguous, low-load exposition

## Examples

**[Anatomy & Physiology Revealed](https://www.mheducation.com)** — McGraw-Hill's dissection software places labels and structures directly on layered cadaver imagery rather than in a separate key.

**Khan Academy exercise hints** — hints appear inline beneath the problem step they address, keeping corrective explanation adjacent to the work it explains.

**Textbook annotation design** — well-designed science textbooks (e.g., Campbell Biology) place figure callouts and process labels directly on diagrams instead of requiring readers to cross-reference a caption paragraph.

**Slide design practice** — replacing "bullet list on left, screenshot on right" layouts with labeled screenshots, so each point sits on the part of the image it describes.

## Key Sources
- Mayer, R. E. (2021). *Multimedia learning* (3rd ed.). Cambridge University Press. [doi:10.1017/9781316941355](https://doi.org/10.1017/9781316941355)
- Mayer, R. E., & Fiorella, L. (2014). Twelve principles of multimedia learning based on cognitive load theory. In R. Brunken, F. Paas, & J. L. Plass (Eds.), *Cognitive load theory* (pp. 229–250). Cambridge University Press. [doi:10.1017/cbo9781139547369.005](https://doi.org/10.1017/cbo9781139547369.005)
- Sweller, J., Ayres, P., & Kalyuga, S. (2011). *Cognitive load theory*. Springer. [doi:10.1007/978-1-4419-8126-4](https://doi.org/10.1007/978-1-4419-8126-4)
- Clark, R. C., & Mayer, R. E. (2016). *E-Learning and the science of instruction* (4th ed.). Wiley. [doi:10.1002/9781119239086](https://doi.org/10.1002/9781119239086)
- Ginns, P. (2006). Integrating information: A meta-analysis of the spatial contiguity and temporal contiguity effects. *Learning and Instruction, 16*(6), 511–525. [doi:10.1016/j.learninstruc.2006.10.001](https://doi.org/10.1016/j.learninstruc.2006.10.001)