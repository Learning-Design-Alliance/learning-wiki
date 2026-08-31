---
type: strategy
title: Maximize Transfer and Generalization
description: Deliberately designing instruction so that knowledge and skills acquired in one context can be applied to new problems, domains, and real-world situations.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Maximize Transfer and Generalization

## Description
Transfer is the application of knowledge or skills learned in one context to a new context; generalization is the abstraction of a principle from specific instances so it applies across cases. This strategy designs for both: instruction presents concepts in multiple varied contexts, requires application to novel problems, and prompts learners to abstract the underlying principles that connect cases. Near transfer (to similar problems) is far easier to achieve than far transfer (to dissimilar domains), and instruction must be deliberately engineered for the latter — it rarely emerges from single-context practice alone.

## Design Implications

Transfer depends on learners encoding knowledge in a form that is decontextualized enough to travel but concrete enough to be usable. Multiple contrasting cases support abstraction of the deep structure that single examples leave implicit [Multiple contrasting cases support abstraction of deep structure.](../claims/multiple-contrasting-cases-support-abstraction.md) [+S], and prompting learners to explain how cases relate strengthens the resulting schema [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+M]. Because far transfer is notoriously difficult to produce [Barnett & Ceci document how rarely far transfer occurs without explicit support.](https://doi.org/10.1037/0033-2909.128.4.612) [~M], designs should teach the abstraction explicitly (e.g., naming the principle, comparing surface-identical and surface-different problems) rather than hoping learners will induce it from exposure.

### Context
#### Requirements
- At least two varied examples or contexts per principle, so learners can separate deep structure from surface features ([Comparing Cases](../elements/comparing-cases.md), [Analogies](../elements/analogies.md))
- Novel application tasks that differ in surface features from the instructional examples ([Application](../elements/application.md), [Practice](../elements/practice.md))
- Prompts that require learners to articulate the general principle and where else it applies ([Integration](../elements/integration.md))
- Spaced re-engagement with the principle in new contexts over time [Spaced repetition improves retention.](../claims/spaced-repetition-improves-retention.md) [+S]

#### Constraints
- Single-context practice produces knowledge tightly bound to surface features; learners then fail to recognize structurally identical problems in new clothing [Gick & Holyoak showed learners rarely notice analogous structure without explicit comparison.](https://doi.org/10.1016/0010-0285(83)90003-0) [-S]
- Far transfer to dissimilar domains frequently fails even after successful near-transfer instruction; promising broad "thinking skills" gains from a single course is not supported [Detterman's review found little evidence of far transfer in most studies.](https://doi.org/10.4324/9781315805893) [-M]
- High-similarity practice can create overconfidence: learners perform well on near variants and collapse on far ones, so assessment must sample the transfer range, not just near variants [~M]
- Adding varied contexts increases cognitive load for novices; sequencing from example comparison to independent novel application is needed rather than jumping straight to far problems [~M]

#### Implementation Variability
- **Hugging and bridging** (Salomon & Perkins): "hugging" keeps practice close to the target application (near transfer); "bridging" explicitly prompts learners to project the principle into new domains (far transfer)
- **Forward-reaching vs. backward-reaching design**: teach material from the start in a transfer-oriented way, or later prompt learners to revisit prior learning and connect it to new problems
- **Case-based formats**: [Case Studies](../elements/case-studies.md) and problem-based scenarios situate principles in realistic contexts and support application [Case-based learning improves exam performance.](../claims/case-based-learning-improves-exam-performance.md) [+M]
- **Faded support**: begin with worked comparisons and fade to independent novel application as competence grows [Fading support promotes transfer of responsibility.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M]

### Target Learners
- Learners who already have a baseline schema in the target domain — transfer tasks presuppose something to transfer; complete novices need initial structured instruction first [~M]
- Intermediate learners benefit most from contrasting-case comparison, which reveals structure they would otherwise miss [Multiple contrasting cases support abstraction of deep structure.](../claims/multiple-contrasting-cases-support-abstraction.md) [+S]
- Learners with strong prior knowledge can be given far-transfer tasks earlier; novices need near-transfer tasks first (expertise reversal pattern) [~M]

### Target Learning Goals
- Application objectives: using concepts to solve novel, real-world problems
- Conceptual understanding: abstracting principles from instances [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+M]
- Adaptive expertise: knowing when and how to modify learned procedures for new conditions
- Lifelong learning: recognizing structural similarity across domains ([Analogical Reasoning](../principles/analogical-reasoning.md))

### Instructions
1. Teach the target concept with an initial worked example or model ([Demonstration](../elements/demonstration.md), [Worked Examples](../elements/worked-examples.md))
2. Present a second, surface-different example of the same principle and prompt learners to compare: "What is the same underneath?" ([Comparing Cases](../elements/comparing-cases.md)) [Multiple contrasting cases support abstraction of deep structure.](../claims/multiple-contrasting-cases-support-abstraction.md) [+S]
3. Have learners state the general principle in their own words and generate one additional context where it applies ([Integration](../elements/integration.md), [Self-Explanation](../elements/self-explanation.md)) [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+M]
4. Assign a novel application task that differs in surface features but shares deep structure ([Application](../elements/application.md))
5. Provide feedback focused on process and principle use, not just answers [Feedback is most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]
6. Revisit the principle across the term in progressively more distant contexts, spaced over time [Spaced repetition improves retention.](../claims/spaced-repetition-improves-retention.md) [+S]

## Related Strategies
- [Teaching for Transfer (Hugging and Bridging)](../strategies/teaching-for-transfer.md) — the Salomon & Perkins framing of this strategy
- [Use Worked Examples](../strategies/use_worked_examples.md) — the example-comparison foundation from which transfer tasks diverge
- [Case-Based Learning](../strategies/case-based-learning.md) — situates principles in realistic contexts requiring application

## Examples
- **Gick & Holyoak's radiation problem** — learners who first compared two analogous stories (the fortress and the general) were far more likely to solve Duncker's radiation problem than those given the stories without comparison prompts ([doi:10.1016/0010-0285(83)90003-0](https://doi.org/10.1016/0010-0285(83)90003-0))
- **[Case-Based Learning, Harvard Business School method](../patterns/case-based-learning-harvard-method.md)** — students apply frameworks to a new business case each session, forcing repeated transfer of the same analytical principles across industries
- **[Anchored Instruction (The Jasper Woodbury Project)](../patterns/anchored-instruction.md)** — video-based mathematical problem solving designed so that sub-skills learned in one adventure must be recombined in novel situations
- **Physics instruction with varied problem sets** — presenting the same principle (e.g., conservation of energy) across ramps, springs, and pendulums before testing on an unseen apparatus

## Key Sources
- Salomon, G., & Perkins, D. N. (1989). Rocky roads to transfer: Rethinking mechanism of a neglected phenomenon. *Educational Psychologist, 24*(2), 113–142. [doi:10.1207/s15326985ep2402_1](https://doi.org/10.1207/s15326985ep2402_1)
- Barnett, S. M., & Ceci, S. J. (2002). When and where do we apply what we learn? A taxonomy for far transfer. *Psychological Bulletin, 128*(4), 612–676. [doi:10.1037/0033-2909.128.4.612](https://doi.org/10.1037/0033-2909.128.4.612)
- Gick, M. L., & Holyoak, K. J. (1983). Schema induction and analogical transfer. *Cognitive Psychology, 15*(1), 1–38. [doi:10.1016/0010-0285(83)90002-6](https://doi.org/10.1016/0010-0285(83)90002-6)
- Detterman, D. K. (1993). The case for the prosecution: Transfer as an epiphenomenon. In D. K. Detterman & R. J. Sternberg (Eds.), *Transfer on trial: Intelligence, cognition, and instruction* (pp. 1–24). Ablex.
- Schwartz, D. L., Chase, C. C., Oppezzo, M. A., & Chin, D. B. (2011). Practicing versus inventing with contrasting cases: The effects of telling first on learning and transfer. *Journal of Educational Psychology, 103*(4), 759–775. [doi:10.1037/a0025140](https://doi.org/10.1037/a0025140)