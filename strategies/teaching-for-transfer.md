---
type: strategy
title: Teaching For Transfer
description: Designing instruction so that knowledge and skills acquired in one context are applied in new, dissimilar contexts.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Teaching For Transfer

## Description
Teaching for transfer is the deliberate design of instruction so that what learners acquire can be applied beyond the conditions of original learning — to new problems, domains, or situations. It is carried out by teaching abstract principles alongside multiple concrete instances, prompting learners to make comparisons and abstractions themselves, and practicing application in varied contexts rather than a single one.

## Design Implications

Transfer does not happen automatically; near transfer is common but far transfer is rare without explicit support [Salomon & Perkins' review finds far transfer requires deliberate abstraction and mindful application.](../claims/analogical-reasoning-improves-transfer.md) [+M]. The core mechanism is abstraction: learners must extract a general schema from specific cases, which is aided by comparing multiple cases rather than studying one in depth [Multiple varied cases support schema abstraction better than a single case.](../claims/cognitive-flexibility-theory-multiple-cases.md) [+M]. Prompting learners to map a taught principle onto a novel problem — rather than hoping they will notice the similarity — reliably improves transfer performance [Explicit prompts to compare source and target problems improve analogical transfer.](../claims/analogical-reasoning-improves-transfer.md) [+S].

### Context
#### Requirements
- Instruction organized around generalizable principles, not surface procedures ([Advance Organizers](../elements/advance-organizers.md) can frame these up front)
- Multiple, varied examples illustrating the same underlying structure ([Case Studies](../elements/case-studies.md), [Analogies](analogies.md))
- Explicit prompts asking learners to identify what is common across cases and how it applies to a new one ([Application](../elements/application.md) tasks)
- Practice in contexts that differ from the original learning context

#### Constraints
- Single-context practice produces knowledge tightly bound to that context; learners fail to retrieve it elsewhere [-S] — this is the classic "inert knowledge" problem
- Transfer fails when learners encode examples by surface features (story details) rather than deep structure; without comparison prompts they do not spontaneously map analogs [+S for prompted, -S for unprompted]
- High [Cognitive Load Management](../principles/cognitive-load-management.md) demands during initial learning leave few resources for abstraction; teaching for transfer before fluency is established can overload novices [~M]
- Far transfer to dissimilar domains is much harder to achieve than near transfer, and claims of easy far transfer are frequently overstated in the literature [-M]

#### Implementation Variability
- **Hugging** (Salomon & Perkins): teaching a principle and then immediately "hugging" it with applications close to the original context — suits near transfer
- **Bridging**: explicitly prompting learners to bridge the principle to distant domains ("Where else does this apply?") — suits far transfer
- **Multiple-case comparison**: sequencing several dissimilar cases sharing one structure, then having learners articulate the invariant ([Case-Based Learning](case-based-learning.md))
- **Metacognitive prompting**: teaching self-question routines ("What is this problem an instance of?") so learners transfer without external prompts

### Target Learners
- Learners who already have basic fluency in the target skill; abstraction attempts before fluency tend to fail [~M]
- Intermediate learners benefit most from comparing multiple cases [Multiple varied cases support schema abstraction better than a single case.](../claims/cognitive-flexibility-theory-multiple-cases.md) [+M]
- Novices need more scaffolding and fewer, more similar cases before variation is productive [~M]

### Target Learning Goals
- Conceptual understanding: grasping principles that generalize across instances
- Problem-solving: recognizing novel problems as instances of known structures
- Dispositional goals: cultivating the inclination to look for applications of what one knows (transfer "propensity," not just capacity)

### Instructions
1. Identify the generalizable principle behind the target content and state it explicitly ([Advance Organizers](../elements/advance-organizers.md))
2. Teach the principle in one concrete context until learners understand it
3. Present 2–3 additional cases that share the deep structure but differ in surface features ([Case Studies](../elements/case-studies.md), [Analogies](analogies.md))
4. Prompt learners to articulate what the cases have in common and name the principle themselves ([Articulation](../elements/articulation.md))
5. Assign application tasks in a novel context, with prompts asking learners to identify which principle applies ([Application](../elements/application.md))
6. Fade the prompts as learners develop the habit of searching for applications themselves

## Related Strategies
- [Analogical Reasoning](../principles/analogical-reasoning.md) — the cognitive mechanism underlying most transfer; comparing source and target structures
- [Activating Prior Knowledge](../strategies/activating-prior-knowledge.md) — transfer depends on retrieving relevant prior learning at the right moment
- [Case-Based Learning](case-based-learning.md) — the multiple-case structure that supports schema abstraction

## Examples
- **Gick & Holyoak's radiation problem studies** — learners who read a fortress-and-general story and were explicitly prompted to use it solved Duncker's tumor problem at far higher rates than those who read the story without a transfer prompt; the canonical demonstration that analogical transfer requires prompting.
- **[Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md)** — its articulation and reflection phases push learners to abstract principles from their own and experts' performance so they carry beyond the apprenticeship setting.
- **Project Zero's "Teaching for Understanding" framework (Harvard GSE)** — organizes curriculum around generative topics and "throughlines" so students repeatedly apply understanding in new performances: https://pz.harvard.edu/projects/teaching-for-understanding

## Key Sources
- Salomon, G., & Perkins, D. N. (1989). Rocky roads to transfer: Rethinking mechanisms of a neglected phenomenon. *Educational Psychologist, 24*(2), 113–142. [doi:10.1207/s15326985ep2402_1](https://doi.org/10.1207/s15326985ep2402_1)
- Barnett, S. M., & Ceci, S. J. (2002). When and where do we apply what we learn? A taxonomy for far transfer. *Psychological Bulletin, 128*(4), 612–637. [doi:10.1037/0033-2909.128.4.612](https://doi.org/10.1037/0033-2909.128.4.612)
- Gick, M. L., & Holyoak, K. J. (1983). Schema induction and analogical transfer. *Cognitive Psychology, 15*(1), 1–38. [doi:10.1016/0010-0285(83)90002-6](https://doi.org/10.1016/0010-0285(83)90002-6)
- Perkins, D. N., & Salomon, G. (1988). Teaching for transfer. *Educational Leadership, 46*(1), 22–32.