---
type: strategy
id: maximize_transfer_and_generalization
aliases: [maximization_of_transfer_and_generalization]
title: Maximize Transfer and Generalization
description: Deliberately designing instruction so that knowledge and skills acquired in one context can be applied to new problems, domains, and real-world situations.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Maximize Transfer and Generalization

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (6 for) · 16 studies (7 quant-synthesis, 6 causal, 2 review, 1 associational), `q2`–`q4` · 5 of 16 report an effect size

## Description
Transfer is the application of knowledge or skills learned in one context to a new context; generalization is the abstraction of a principle from specific instances so it applies across cases. This strategy designs for both: instruction presents concepts in multiple varied contexts, requires application to novel problems, and prompts learners to abstract the underlying principles that connect cases. Near transfer (to similar problems) is far easier to achieve than far transfer (to dissimilar domains), and instruction must be deliberately engineered for the latter — it rarely emerges from single-context practice alone.

## Design Implications

Transfer depends on learners encoding knowledge in a form that is decontextualized enough to travel but concrete enough to be usable. Multiple contrasting cases support abstraction of the deep structure that single examples leave implicit [Multiple contrasting cases support abstraction of deep structure.](../claims/comparing-contrasting-cases-improves-learning.md) [+S], and prompting learners to explain how cases relate strengthens the resulting schema [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+M]. Because far transfer is notoriously difficult to produce [Barnett & Ceci document how rarely far transfer occurs without explicit support.](https://doi.org/10.1037/0033-2909.128.4.612) [~M], designs should teach the abstraction explicitly (e.g., naming the principle, comparing surface-identical and surface-different problems) rather than hoping learners will induce it from exposure.

### Context
#### Requirements
- At least two varied examples or contexts per principle, so learners can separate deep structure from surface features ([Comparing Cases](../elements/comparing-cases.md), [Analogies](../elements/analogies.md))
- Novel application tasks that differ in surface features from the instructional examples ([Application](../elements/application.md), [Practice](../elements/practice.md))
- Prompts that require learners to articulate the general principle and where else it applies ([Integration](../elements/integration.md))
- Spaced re-engagement with the principle in new contexts over time [Spaced repetition improves retention.](../claims/spaced-repetition-improves-retention.md) [+S]
- At least two or more examples or cases sharing the same deep structure but differing in surface features, presented for comparison
- Explicit identification of the generalizable principle, or prompts that lead learners to articulate it themselves ([Self-Explanation](../elements/self-explanation.md), [Analogies](../elements/analogies.md))
- Practice opportunities in varied, increasingly dissimilar contexts ([Practice](../elements/practice.md), [Case Studies](../elements/case-studies.md))
- Progressive withdrawal of scaffolding ([Fading](../elements/fading.md)) so learners eventually apply knowledge without support

#### Constraints
- Single-context practice produces knowledge tightly bound to surface features; learners then fail to recognize structurally identical problems in new clothing [Gick & Holyoak showed learners rarely notice analogous structure without explicit comparison.](https://doi.org/10.1016/0010-0285(83)90003-0) [-S]
- Far transfer to dissimilar domains frequently fails even after successful near-transfer instruction; promising broad "thinking skills" gains from a single course is not supported [Detterman's review found little evidence of far transfer in most studies.](https://doi.org/10.4324/9781315805893) [-M]
- High-similarity practice can create overconfidence: learners perform well on near variants and collapse on far ones, so assessment must sample the transfer range, not just near variants [~M]
- Adding varied contexts increases cognitive load for novices; sequencing from example comparison to independent novel application is needed rather than jumping straight to far problems [~M]
- Knowledge learned in a single context with a single example tends to remain bound to that context; learners often fail to notice that a new problem is structurally identical to one they have solved [Gick & Holyoak, 1983] [-S]
- Far transfer to dissimilar domains rarely occurs spontaneously and cannot be assumed from strong within-domain performance [Detterman, 1993] [-S]
- High surface similarity between learning and transfer tasks can produce apparent transfer that collapses when surface features change [~M]
- Excessive variability in early practice can overload novices; variability is best introduced after initial schema formation [~M]

#### Implementation Variability
- **Hugging and bridging** (Salomon & Perkins): "hugging" keeps practice close to the target application (near transfer); "bridging" explicitly prompts learners to project the principle into new domains (far transfer)
- **Forward-reaching vs. backward-reaching design**: teach material from the start in a transfer-oriented way, or later prompt learners to revisit prior learning and connect it to new problems
- **Case-based formats**: [Case Studies](../elements/case-studies.md) and problem-based scenarios situate principles in realistic contexts and support application [Case-based learning improves exam performance.](../claims/case-based-learning-improves-exam-performance.md) [+M]
- **Faded support**: begin with worked comparisons and fade to independent novel application as competence grows [Fading support promotes transfer of responsibility.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M]
- **Near-transfer design:** vary surface features while holding structure constant (e.g., isomorphic problems across contexts)
- **Far-transfer design:** use [Case Studies](../elements/case-studies.md) and [Anchored Instruction](../elements/anchored-instruction.md) embedding the target skill in authentic, ill-structured scenarios
- **Metacognitive route:** teach learners to search for analogies and ask "where else does this apply?" — transfer-appropriate monitoring
- **Hugging and bridging:** "hugging" keeps practice close to the target application; "bridging" explicitly connects learning to distant contexts [Salomon & Perkins, 1989]

### Target Learners
- Learners who already have a baseline schema in the target domain — transfer tasks presuppose something to transfer; complete novices need initial structured instruction first [~M]
- Intermediate learners benefit most from contrasting-case comparison, which reveals structure they would otherwise miss [Multiple contrasting cases support abstraction of deep structure.](../claims/comparing-contrasting-cases-improves-learning.md) [+S]
- Learners with strong prior knowledge can be given far-transfer tasks earlier; novices need near-transfer tasks first (expertise reversal pattern) [~M]
- Learners who will apply skills in settings that differ from the instructional setting (workplace, clinical, everyday contexts)
- Learners with some initial schema in place — complete novices benefit first from structured examples, then from varied practice [Example-problem sequences reduce cognitive load for novices.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+M]
- Learners prone to overestimating their readiness to apply knowledge in new settings; varied application tasks expose gaps that single-context practice hides

### Target Learning Goals
- Application objectives: using concepts to solve novel, real-world problems
- Conceptual understanding: abstracting principles from instances [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+M]
- Adaptive expertise: knowing when and how to modify learned procedures for new conditions
- Lifelong learning: recognizing structural similarity across domains ([Analogical Reasoning](../principles/analogical-reasoning.md))
- Application of principles to novel problems (near and far transfer)
- Durable, flexible knowledge rather than context-bound procedural routines

### Instructions
1. Teach the target concept with an initial worked example or model ([Demonstration](../elements/demonstration.md), [Worked Examples](../elements/worked-examples.md))
2. Present a second, surface-different example of the same principle and prompt learners to compare: "What is the same underneath?" ([Comparing Cases](../elements/comparing-cases.md)) [Multiple contrasting cases support abstraction of deep structure.](../claims/comparing-contrasting-cases-improves-learning.md) [+S]
3. Have learners state the general principle in their own words and generate one additional context where it applies ([Integration](../elements/integration.md), [Self-Explanation](../elements/self-explanation.md)) [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+M]
4. Assign a novel application task that differs in surface features but shares deep structure ([Application](../elements/application.md))
5. Provide feedback focused on process and principle use, not just answers [Feedback is most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]
6. Revisit the principle across the term in progressively more distant contexts, spaced over time [Spaced repetition improves retention.](../claims/spaced-repetition-improves-retention.md) [+S]

## Related Strategies
- [Teaching for Transfer (Hugging and Bridging)](../strategies/teaching-for-transfer.md) — the Salomon & Perkins framing of this strategy
- [Use Worked Examples](../strategies/use_worked_examples.md) — the example-comparison foundation from which transfer tasks diverge
- [Case-Based Learning](../strategies/case-based-learning.md) — situates principles in realistic contexts requiring application
- [Spaced Repetition](spaced_repetition.md) — distributed, spaced retrieval strengthens the durable memory that transfer draws on
- [Comparing Cases](comparing_cases.md) — the core mechanism for supporting abstraction across examples
- [Authentic Learning Tasks](authentic_learning_tasks.md) — grounding practice in realistic contexts increases the likelihood of application beyond the classroom
- [Teach workplace problem solving through case studies and role plays with a structured procedure](workplace-problem-solving-role-plays.md)

## Examples
- **Gick & Holyoak's radiation problem** — learners who first compared two analogous stories (the fortress and the general) were far more likely to solve Duncker's radiation problem than those given the stories without comparison prompts ([doi:10.1016/0010-0285(83)90003-0](https://doi.org/10.1016/0010-0285(83)90003-0))
- **[Case-Based Learning, Harvard Business School method](../patterns/case-based-learning-harvard-method.md)** — students apply frameworks to a new business case each session, forcing repeated transfer of the same analytical principles across industries
- **[Anchored Instruction (The Jasper Woodbury Project)](../patterns/anchored-instruction.md)** — video-based mathematical problem solving designed so that sub-skills learned in one adventure must be recombined in novel situations
- **Physics instruction with varied problem sets** — presenting the same principle (e.g., conservation of energy) across ramps, springs, and pendulums before testing on an unseen apparatus
- **[Khan Academy](https://www.khanacademy.org)** — mastery-based practice items vary numbers and contexts within a skill, requiring learners to apply the same procedure across surface variations before moving on.
- **Harvard Business School case method** — students analyze successive cases sharing managerial principles but differing in industry and context, then must apply those principles to a new case under discussion; see [Case-Based Learning](../patterns/case-based-learning.md).
- **[Jasper Woodbury Problem Solving series](https://peabody.vanderbilt.edu/research/legacy_projects/jasper/)** (Vanderbilt) — anchored video adventures in which students apply mathematical planning skills to novel "extension" problems deliberately designed to test transfer.
- **Physics by Inquiry** (McDermott, University of Washington) — students derive principles from varied experiments and must apply them to unfamiliar phenomena, with transfer tasks built into the curriculum.

## Key Sources
- Salomon, G., & Perkins, D. N. (1989). Rocky roads to transfer: Rethinking mechanism of a neglected phenomenon. *Educational Psychologist, 24*(2), 113–142. [doi:10.1207/s15326985ep2402_1](https://doi.org/10.1207/s15326985ep2402_1)
- Barnett, S. M., & Ceci, S. J. (2002). When and where do we apply what we learn? A taxonomy for far transfer. *Psychological Bulletin, 128*(4), 612–676. [doi:10.1037/0033-2909.128.4.612](https://doi.org/10.1037/0033-2909.128.4.612)
- Gick, M. L., & Holyoak, K. J. (1983). Schema induction and analogical transfer. *Cognitive Psychology, 15*(1), 1–38. [doi:10.1016/0010-0285(83)90002-6](https://doi.org/10.1016/0010-0285(83)90002-6)
- Detterman, D. K. (1993). The case for the prosecution: Transfer as an epiphenomenon. In D. K. Detterman & R. J. Sternberg (Eds.), *Transfer on trial: Intelligence, cognition, and instruction* (pp. 1–24). Ablex.
- Schwartz, D. L., Chase, C. C., Oppezzo, M. A., & Chin, D. B. (2011). Practicing versus inventing with contrasting cases: The effects of telling first on learning and transfer. *Journal of Educational Psychology, 103*(4), 759–775. [doi:10.1037/a0025140](https://doi.org/10.1037/a0025140)
- Barnett, S. M., & Ceci, S. J. (2002). When and where do we apply what we learn? A taxonomy for far transfer. *Psychological Bulletin, 128*(4), 612–637. [doi:10.1037/0033-2909.128.4.612](https://doi.org/10.1037/0033-2909.128.4.612)

<!-- merged 2026-10-09 from strategies/maximization_of_transfer_and_generalization ("Maximization of Transfer and Generalization"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Maximization of Transfer and Generalization

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 10 studies (5 causal, 3 quant-synthesis, 1 review, 1 associational), `q2`–`q4` · 2 of 10 report an effect size · 1 claim rests on one study

## Description
Maximization of transfer and generalization is the deliberate design of instruction so that what learners acquire can be applied to novel problems, contexts, and situations beyond the original learning conditions. It is carried out by varying practice conditions, using multiple contrasting examples, making underlying principles explicit, and prompting learners to abstract and articulate the generalizable structure of what they are learning. Transfer is notoriously difficult to achieve without such design effort; near transfer (to similar problems) occurs more readily than far transfer (to dissimilar contexts), and instruction must be engineered for the latter rather than assumed [Salomon & Perkins, 1989].

## Design Implications

Transfer depends on learners encoding knowledge in a form that is abstract enough to apply elsewhere but concrete enough to be usable. Multiple contrasting cases that share deep structure but differ in surface features support abstraction of the underlying principle [Multiple contrasting cases support abstraction of shared structure.](../claims/comparing-contrasting-cases-improves-learning.md) [+S]. Prompting learners to explain why a solution works — rather than only producing solutions — builds the conceptual understanding that far transfer requires [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+S]. Transfer is also improved when learners practice in varied contexts and when support is progressively withdrawn so responsibility for application shifts to the learner [Fading support promotes transfer of responsibility.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M].

### Context
#### Requirements
- At least two or more examples or cases sharing the same deep structure but differing in surface features, presented for comparison
- Explicit identification of the generalizable principle, or prompts that lead learners to articulate it themselves ([Self-Explanation](../elements/self-explanation.md), [Analogies](../elements/analogies.md))
- Practice opportunities in varied, increasingly dissimilar contexts ([Practice](../elements/practice.md), [Case Studies](../elements/case-studies.md))
- Progressive withdrawal of scaffolding ([Fading](../elements/fading.md)) so learners eventually apply knowledge without support

#### Constraints
- Knowledge learned in a single context with a single example tends to remain bound to that context; learners often fail to notice that a new problem is structurally identical to one they have solved [Gick & Holyoak, 1983] [-S]
- Far transfer to dissimilar domains rarely occurs spontaneously and cannot be assumed from strong within-domain performance [Detterman, 1993] [-S]
- High surface similarity between learning and transfer tasks can produce apparent transfer that collapses when surface features change [~M]
- Excessive variability in early practice can overload novices; variability is best introduced after initial schema formation [~M]

#### Implementation Variability
- **Near-transfer design:** vary surface features while holding structure constant (e.g., isomorphic problems across contexts)
- **Far-transfer design:** use [Case Studies](../elements/case-studies.md) and [Anchored Instruction](../elements/anchored-instruction.md) embedding the target skill in authentic, ill-structured scenarios
- **Metacognitive route:** teach learners to search for analogies and ask "where else does this apply?" — transfer-appropriate monitoring
- **Hugging and bridging:** "hugging" keeps practice close to the target application; "bridging" explicitly connects learning to distant contexts [Salomon & Perkins, 1989]

### Target Learners
- Learners who will apply skills in settings that differ from the instructional setting (workplace, clinical, everyday contexts)
- Learners with some initial schema in place — complete novices benefit first from structured examples, then from varied practice [Example-problem sequences reduce cognitive load for novices.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+M]
- Learners prone to overestimating their readiness to apply knowledge in new settings; varied application tasks expose gaps that single-context practice hides

### Target Learning Goals
- Application of principles to novel problems (near and far transfer)
- Abstraction: extracting generalizable rules and schemas from specific instances [Multiple contrasting cases support abstraction of shared structure.](../claims/comparing-contrasting-cases-improves-learning.md) [+S]
- Durable, flexible knowledge rather than context-bound procedural routines
- Adaptive expertise: knowing when and how to modify learned procedures

### Instructions
1. Teach the target concept or skill with an initial clear model or worked example ([Direct Instruction](../elements/direct-instruction.md))
2. Present a second, structurally identical case with different surface features and prompt learners to compare: "What is the same? What is different?" ([Case Studies](../elements/case-studies.md), [Analogies](../elements/analogies.md))
3. Prompt learners to state the underlying principle in their own words ([Self-Explanation](../elements/self-explanation.md), [Articulation](../elements/articulation.md))
4. Provide practice on novel problems that vary surface features and, later, structural demands ([Practice](../elements/practice.md), [Application of Knowledge](../elements/application-of-knowledge.md))
5. Fade support across the sequence — worked examples → partial examples → independent problems ([Fading](../elements/fading.md))
6. Assess transfer directly with tasks learners have not seen, not with near-duplicates of practice items ([Assessment](../elements/assessment.md))

## Related Strategies

- [Spaced Repetition](spaced_repetition.md) — distributed, spaced retrieval strengthens the durable memory that transfer draws on
- [Comparing Cases](comparing_cases.md) — the core mechanism for supporting abstraction across examples
- [Authentic Learning Tasks](authentic_learning_tasks.md) — grounding practice in realistic contexts increases the likelihood of application beyond the classroom
- [Teach workplace problem solving through case studies and role plays with a structured procedure](workplace-problem-solving-role-plays.md)

## Examples
- **[Khan Academy](https://www.khanacademy.org)** — mastery-based practice items vary numbers and contexts within a skill, requiring learners to apply the same procedure across surface variations before moving on.
- **Harvard Business School case method** — students analyze successive cases sharing managerial principles but differing in industry and context, then must apply those principles to a new case under discussion; see [Case-Based Learning](../patterns/case-based-learning.md).
- **[Jasper Woodbury Problem Solving series](https://peabody.vanderbilt.edu/research/legacy_projects/jasper/)** (Vanderbilt) — anchored video adventures in which students apply mathematical planning skills to novel "extension" problems deliberately designed to test transfer.
- **Physics by Inquiry** (McDermott, University of Washington) — students derive principles from varied experiments and must apply them to unfamiliar phenomena, with transfer tasks built into the curriculum.

## Key Sources
- Salomon, G., & Perkins, D. N. (1989). Rocky roads to transfer: Rethinking mechanism of a neglected phenomenon. *Educational Psychologist, 24*(2), 113–142. [doi:10.1207/s15326985ep2402_1](https://doi.org/10.1207/s15326985ep2402_1)
- Barnett, S. M., & Ceci, S. J. (2002). When and where do we apply what we learn? A taxonomy for far transfer. *Psychological Bulletin, 128*(4), 612–637. [doi:10.1037/0033-2909.128.4.612](https://doi.org/10.1037/0033-2909.128.4.612)
- Gick, M. L., & Holyoak, K. J. (1983). Schema induction and analogical transfer. *Cognitive Psychology, 15*(1), 1–38. [doi:10.1016/0010-0285(83)90002-6](https://doi.org/10.1016/0010-0285(83)90002-6)
- Detterman, D. K. (1993). The case for the prosecution: Transfer as an epiphenomenon. In D. K. Detterman & R. J. Sternberg (Eds.), *Transfer on trial: Intelligence, cognition, and instruction* (pp. 1–24). Ablex.
- Schwartz, D. L., Chase, C. C., Oppezzo, M. A., & Chin, D. B. (2011). Practicing versus inventing with contrasting cases: The effects of telling first on learning and transfer. *Journal of Educational Psychology, 103*(4), 759–775. [doi:10.1037/a0025140](https://doi.org/10.1037/a0025140)
-->
