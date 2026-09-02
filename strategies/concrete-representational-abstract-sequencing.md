---
type: strategy
id: concrete-representational-abstract-sequencing
title: Concrete Representational Abstract Sequencing
description: Teach a concept first with physical or concrete materials, then with visual representations, then with abstract symbols, fading across stages as understanding consolidates.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Concrete Representational Abstract Sequencing

> **Strategy** · [All strategies](index.md)

## Description
Concrete Representational Abstract (CRA) sequencing teaches a new concept in three stages: first with concrete objects learners can manipulate (counters, base-ten blocks, fraction tiles), then with drawn or diagrammatic representations of the same structure, and finally with abstract notation (symbols, equations, algorithms). Each stage is explicitly connected to the previous one — the same problem is shown in all three forms — so the abstract symbols inherit meaning from the concrete and pictorial experiences rather than being memorized as arbitrary marks.

## Design Implications

CRA sequencing manages the transition from embodied, perceptual understanding to symbolic fluency, reducing the risk that symbols are manipulated without meaning [Cognitive overload degrades learning when representational demands exceed working memory capacity.](../claims/cognitive-overload-degrades-learning.md) [+M]. The critical design feature is *fading* — the sequence works because representations become progressively more abstract, not because concrete materials are used per se; staying too long at the concrete stage can impede generalization [Concreteness fading supports transfer better than sustained concrete or early abstract instruction.](../claims/example-problem-sequences-reduce-cognitive-load.md) [~M]. Explicit linking across stages (e.g., writing the equation beside the drawing while manipulating objects) is what builds the mapping between representations.

### Context
#### Requirements
- Concrete materials that genuinely model the target mathematical structure (place value, proportionality), not merely decorate it
- A parallel representational form (drawings, diagrams, number lines) that maps one-to-one onto the concrete materials
- Explicit connection language and side-by-side presentation so learners see the *same* problem in multiple forms
- A planned transition point to abstract notation, with continued access to representations as a fallback ([Fading](../elements/fading.md))

#### Constraints
- Concrete materials that are perceptually rich but structurally misleading (e.g., brightly colored, distracting manipulatives) can divert attention from the target concept [Decorative illustrations do not improve learning and can reduce it.](../claims/decorative-illustrations-do-not-improve-learning.md) [-M]
- Prolonged reliance on concrete objects without fading can bind understanding to specific materials and block transfer to symbols [~M]
- Learners with strong prior knowledge of the abstract form may find the concrete stage redundant and demotivating [Guidance becomes less effective as learner expertise increases.](../claims/expertise-reversal-effect.md) [~M]
- Poorly chosen manipulatives (e.g., using the same color for ones and tens) can actively model the wrong structure [-M]

#### Implementation Variability
- **Gradual vs. simultaneous:** fade stage by stage, or present all three representations side by side from the start for learners who can handle the load
- **Virtual manipulatives:** digital tools (e.g., Brainingcamp, Didax virtual manipulatives) can substitute for physical objects, with similar effects in meta-analytic comparisons [~M]
- **Domain extension:** CRA originated in mathematics but the logic applies to science (physical models → diagrams → formal notation) and programming (physical artifacts → flowcharts → code)

### Target Learners
- Elementary and middle-grades students encountering a mathematical concept for the first time [+M]
- Learners with learning disabilities or working memory constraints, for whom CRA is one of the better-evidenced mathematics interventions [+S]
- Less beneficial for advanced learners already fluent in symbolic manipulation [Guidance becomes less effective as learner expertise increases.](../claims/expertise-reversal-effect.md) [~M]

### Target Learning Goals
- Conceptual understanding: grasping *why* an algorithm or symbolic procedure works
- Procedural fluency grounded in meaning rather than rote steps
- Representational flexibility: moving fluently among concrete, pictorial, and symbolic forms

### Instructions
1. **Concrete stage:** introduce the concept with manipulable objects; learners solve several problems physically ([Act It Out](../elements/act-it-out.md))
2. **Bridge:** while objects are still present, record the same problem in pictures and begin writing symbols alongside ([Annotating](../principles/annotating.md))
3. **Representational stage:** replace objects with student-drawn or provided diagrams; solve the same problem types ([Dual coding improves recall when verbal and visual channels are used together.](../claims/dual-coding-improves-recall.md) [+S])
4. **Abstract stage:** move to symbols alone, keeping representations available on request; connect new abstract problems back to a remembered representation ([Application](../elements/application.md))
5. **Assess across representations:** check that learners can translate among all three forms, not just execute the abstract procedure ([Assessment](../elements/assessment.md))

## Related Strategies
- [Worked Examples](worked-examples.md) — CRA stages can be delivered as worked examples with representations fading to abstract
- [Manipulatives](manipulatives.md) — the concrete stage's core materials and their design constraints
- [Multiple Representations](multiple-representations.md) — the broader principle of linking forms; CRA is a temporal sequencing of it

## Examples
- **[Cognitively Guided Instruction](../patterns/cognitively-guided-instruction-cgi-for-math.md)** — builds arithmetic understanding from children's informal, concrete modeling strategies toward abstract number sentences
- **[Concrete-Representational-Abstract instruction for fractions](https://pubmed.ncbi.nlm.nih.gov/12815749/)** — Butler, Miller, Crehan, Babbitt & Pierce (2003) compared CRA and representational-only treatments for teaching fraction concepts to secondary students with learning disabilities; both improved, CRA strongest for subtraction
- **[National Library of Virtual Manipulatives](https://nlvm.usu.edu)** — free virtual manipulatives (base-ten blocks, algebra tiles) supporting the concrete-to-representational transition in digital contexts
- **Singapore Math / Math in Focus** — published curriculum built on the concrete–pictorial–abstract sequence, using bar models as the representational bridge to algebraic reasoning

## Key Sources
- Bruner, J. S. (1966). *Toward a theory of instruction*. Harvard University Press.
- Carbonneau, K. J., Marley, S. C., & Selig, J. P. (2013). A meta-analysis of the efficacy of teaching mathematics with concrete manipulatives. *Journal of Educational Psychology, 105*(2), 380–400. [doi:10.1037/a0031084](https://doi.org/10.1037/a0031084)
- Butler, F. M., Miller, S. P., Crehan, K., Babbitt, B., & Pierce, T. (2003). Fraction instruction for students with mathematics disabilities: Comparing two teaching sequences. *Learning Disabilities Research & Practice, 18*(2), 99–111. [doi:10.1111/1540-5826.00066](https://doi.org/10.1111/1540-5826.00066)
- Fyfe, E. R., McNeil, N. M., Son, J. Y., & Goldstone, R. L. (2014). Concreteness fading in mathematics and science instruction: A systematic review. *Educational Psychology Review, 26*(1), 9–25. [doi:10.1007/s10648-014-9249-3](https://doi.org/10.1007/s10648-014-9249-3)
- Bouck, E. C., Satsangi, R., & Park, J. (2018). The concrete–representational–abstract approach for students with learning disabilities: An evidence-based practice synthesis. *Remedial and Special Education, 39*(4), 211–228. [doi:10.1177/0741932517721712](https://doi.org/10.1177/0741932517721712)