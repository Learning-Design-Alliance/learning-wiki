---
type: strategy
title: Use Concrete Examples
description: Ground abstract concepts, rules, and procedures in specific, vivid instances that learners can inspect before generalizing.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Use Concrete Examples

## Description
Concrete examples anchor abstract ideas — principles, formulas, categories, procedures — in specific instances a learner can directly inspect. The strategy is carried out by pairing every abstraction with one or more worked instances, then explicitly mapping features of the example back onto the abstract structure so learners extract the general rule rather than memorizing the surface story.

## Design Implications

Concrete examples reduce the working-memory and inferential burden of learning from abstract statements alone, letting learners build schemas from observable structure before generalizing [Concrete examples support schema construction for novices better than abstract presentation alone.](../claims/cognitive-overload-degrades-learning.md) [+M]. Their effectiveness depends on learners attending to the deep structure, not the surface details: multiple varied examples, or explicit comparison of cases, are needed to prevent learners from binding the concept to irrelevant features of a single instance [Comparing contrasting cases improves learning.](../claims/comparing-contrasting-cases-improves-learning.md) [+S]. Examples should be familiar and well-mapped; seductive but poorly aligned details impair learning [Coherence principle: irrelevant material hurts learning.](../claims/coherence-principle-irrelevant-material-hurts-learning.md) [+S].

### Context
#### Requirements
- Examples whose surface features genuinely instantiate the target concept's structure, with the mapping made explicit
- Familiar contexts drawn from learners' prior experience ([Activation](../principles/activation.md) of relevant knowledge)
- Multiple examples varying in surface details when the goal is generalization, ideally presented for comparison
- A follow-on step that asks learners to apply the concept to a new instance or generate their own example

#### Constraints
- A single example risks overgeneralization: learners encode incidental surface features as part of the concept [Comparing contrasting cases improves learning.](../claims/comparing-contrasting-cases-improves-learning.md) [-M]
- Concrete detail can act as seductive, extraneous material when it is vivid but structurally irrelevant [Coherence principle: irrelevant material hurts learning.](../claims/coherence-principle-irrelevant-material-hurts-learning.md) [-S]
- Learners with higher expertise benefit less from concrete grounding and may prefer abstract symbolic representations [Expertise reversal: guidance that helps novices can hinder experts.](../claims/cognitive-overload-degrades-learning.md) [~M]
- Examples alone, without abstraction prompts or practice, produce knowledge that fails to transfer to new problem types

#### Implementation Variability
- **Worked examples**: fully solved instances with reasoning made visible; effective for procedural learning, especially when faded progressively
- **Contrasting cases**: two or more examples differing on a critical dimension, presented side by side so the dimension becomes visible
- **Analogies**: mapping a familiar domain onto an unfamiliar one; effective when the mapping is explicit and learners are warned about where it breaks down [Analogical reasoning improves transfer.](../claims/analogical-reasoning-improves-transfer.md) [+M]
- **Case studies**: extended, realistic instances used to situate concepts in authentic complexity
- **Self-explanation prompts**: asking learners to state *why* an example is an instance of the concept, which forces abstraction

### Target Learners
- Novices, who lack the schemas to instantiate abstract rules on their own and depend on external examples to build them [+M]
- Learners in domains with high element interactivity (mathematics, statistics, programming, science), where abstract statements alone overload working memory [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+M]
- Less beneficial for advanced learners, who can often reason from abstract principles directly and may find concrete scaffolds redundant or distracting [~M]

### Target Learning Goals
- Concept learning and categorization: recognizing new instances of a defined class
- Procedural skill: seeing a rule applied before applying it
- Transfer: generalizing a principle across varied surface contexts (requires multiple varied examples)
- Misconception repair: contrasting correct and incorrect instances sharpens critical features

### Instructions
1. Identify the abstract target — the principle, rule, or category learners must generalize.
2. Select or construct 2–3 examples that vary in surface features but share the target structure; include at least one familiar context to activate prior knowledge.
3. Present the first example with the mapping made explicit: label which features carry the concept and which are incidental.
4. Have learners compare the examples to surface the invariant structure, or prompt them to self-explain why each is an instance ([Comparing Cases](../claims/comparing-contrasting-cases-improves-learning.md)).
5. Follow with application: learners classify new instances, solve an analogous problem, or generate their own example and defend it.
6. Fade concreteness over time — move from concrete instances toward symbolic or abstract representations as expertise develops.

## Related Strategies
- Use worked examples — a concrete example applied to problem solving, with solution steps as the concrete content
- Use analogies and analogical comparison — a special case where the example comes from a different, familiar domain
- Use contrasting cases — the multi-example variant that guards against overgeneralization
- Teach with case studies — extended narrative examples used for complex, ill-structured domains

## Examples
- **Statistics teaching with contrasting contexts**: Presenting the same chi-square test worked on three different datasets (medical, sports, consumer) so students extract the decision procedure rather than memorizing one scenario.
- **[Khan Academy](https://www.khanacademy.org)** — Every abstract math concept is introduced through concrete worked instances with visual models before symbolic notation is emphasized.
- **[Physics Education Technology (PhET) simulations](https://phet.colorado.edu)** — Concrete, manipulable instances of abstract physical principles (e.g., charges and fields), letting learners ground equations in observable behavior.
- **Case-based teaching at Harvard Business School** — Extended real-world cases serve as concrete instances from which students abstract management principles ([case-based learning improves exam performance](../claims/case-based-learning-improves-exam-performance.md) [+M]).

## Key Sources
- Rawson, K. A., Thomas, R. C., & Jacoby, L. L. (2015). The power of examples: Illustrative examples enhance conceptual learning of declarative concepts. *Educational Psychology Review, 27*(3), 483–504. [doi:10.1007/s10648-014-9273-3](https://doi.org/10.1007/s10648-014-9273-3)
- Schwartz, D. L., Chase, C. C., Oppezzo, M. A., & Chin, D. B. (2011). Practicing versus inventing with contrasting cases: The effects of telling first on learning and transfer. *Journal of Educational Psychology, 103*(4), 759–775. [doi:10.1037/a0025140](https://doi.org/10.1037/a0025140)
- Sweller, J., Ayres, P., & Kalyuga, S. (2011). *Cognitive load theory*. Springer. [doi:10.1007/978-1-4419-8126-4](https://doi.org/10.1007/978-1-4419-8126-4)
- Gentner, D., Loewenstein, J., & Thompson, L. (2003). Learning and transfer: A general role for analogical encoding. *Journal of Educational Psychology, 95*(2), 393–408. [doi:10.1037/0022-0663.95.2.393](https://doi.org/10.1037/0022-0663.95.2.393)
- Mayer, R. E. (2014). Cognitive theory of multimedia learning. In R. E. Mayer (Ed.), *The Cambridge Handbook of Multimedia Learning* (2nd ed., pp. 43–71). Cambridge University Press. [doi:10.1017/CBO9781139547369.005](https://doi.org/10.1017/CBO9781139547369.005)