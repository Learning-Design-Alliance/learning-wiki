---
type: strategy
id: concrete-examples
aliases: [use_concrete_examples]
title: Concrete Examples
description: Grounding abstract concepts, principles, or procedures in specific, tangible instances that learners can examine before generalizing.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Concrete Examples

> **Strategy** · [All strategies](index.md)
> **Evidence** · 8 claims (6 for, 2 against) · 15 studies (9 causal, 3 quant-synthesis, 3 review), `q2`–`q4` · 2 of 15 report an effect size · 1 claim rests on one study

## Description
Concrete examples anchor abstract ideas in specific, tangible instances — a worked physics problem for the principle of conservation, a real negotiation transcript for game theory, a particular poem for the concept of meter. The strategy is carried out by presenting one or more instances first (or alongside the abstraction), then helping learners map features of the example onto the general principle.

## Design Implications

Concrete examples reduce the working-memory and knowledge demands of abstraction by giving learners something specific to reason about, which is especially valuable when the concept itself is unfamiliar [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+M]. Examples are most powerful when learners first explore cases and then receive the general rule — a sequence that supports schema induction better than rule-first presentation [Exploration before explanation improves learning from subsequent instruction.](../claims/comparing-contrasting-cases-improves-learning.md) [+M]. Multiple varied examples are generally needed for transfer, since a single example tends to be encoded as a specific story rather than a generalizable structure [Analogical reasoning improves transfer.](../claims/analogical-reasoning-improves-transfer.md) [+M].

### Context
#### Requirements
- Examples that genuinely instantiate the target concept, not merely adjacent to it
- Explicit mapping between example features and the abstract principle — learners rarely extract the deep structure unaided
- Multiple, varied examples when the goal is transfer rather than recognition ([Comparing Cases](../elements/comparing-cases.md) supports this)
- Connection to what learners already know ([Analogies](../elements/analogies.md) and [Activation](../elements/activation.md) of prior knowledge)
- Examples whose surface features genuinely instantiate the target concept's structure, with the mapping made explicit
- Multiple examples varying in surface details when the goal is generalization, ideally presented for comparison
- A follow-on step that asks learners to apply the concept to a new instance or generate their own example

#### Constraints
- Overly rich, seductive details in an example can divert attention from the target concept and depress learning [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [-M] — concreteness helps only when surface features support, not compete with, the abstraction
- A single example encourages overgeneralization of its incidental features; learners may treat the example's specifics as part of the rule
- Concrete materials can impede expert-like abstract reasoning in some domains; purely concrete instantiations sometimes produce *worse* transfer than abstract representations [~M] (Kaminski et al., 2008)
- Examples without explicit mapping leave learners to guess the intended correspondence, often anchoring on surface similarity [~M]
- Concrete detail can act as seductive, extraneous material when it is vivid but structurally irrelevant [Coherence principle: irrelevant material hurts learning.](../claims/coherence-principle-irrelevant-material-hurts-learning.md) [-S]
- Examples alone, without abstraction prompts or practice, produce knowledge that fails to transfer to new problem types

#### Implementation Variability
- **Example-first vs. rule-first:** presenting cases before the rule (productive failure / "a time for telling") versus interleaving rule and example; example-first tends to build better schemas for novices
- **Concrete-to-abstract fading:** starting with physical or situational instances and progressively introducing symbolic notation
- **Interleaved examples and practice:** alternating [Worked Examples](../elements/worked-examples.md) with problems to solve
- **Contrasting cases:** pairing correct and incorrect or near-miss examples to sharpen discrimination
- **Worked examples**: fully solved instances with reasoning made visible; effective for procedural learning, especially when faded progressively
- **Contrasting cases**: two or more examples differing on a critical dimension, presented side by side so the dimension becomes visible
- **Case studies**: extended, realistic instances used to situate concepts in authentic complexity
- **Self-explanation prompts**: asking learners to state *why* an example is an instance of the concept, which forces abstraction

### Target Learners
- Novices who lack the prior knowledge to parse abstract statements meaningfully [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]
- Learners in domains with high symbolic density (mathematics, statistics, economics) where notation outpaces intuition
- Less necessary for learners with well-developed schemas, who can often reason directly with abstractions and may find concrete instantiations redundant or distracting [~M]
- Novices, who lack the schemas to instantiate abstract rules on their own and depend on external examples to build them [+M]
- Less beneficial for advanced learners, who can often reason from abstract principles directly and may find concrete scaffolds redundant or distracting [~M]

### Target Learning Goals
- Concept formation: understanding what a category, principle, or definition means in practice
- Schema induction: extracting generalizable structure from instances [Analogical reasoning improves transfer.](../claims/analogical-reasoning-improves-transfer.md) [+M]
- Transfer: applying principles to novel situations (requires multiple varied examples) [Multiple varied cases support flexible transfer.](../claims/cognitive-flexibility-theory-multiple-cases.md) [+M]
- Concept learning and categorization: recognizing new instances of a defined class
- Procedural skill: seeing a rule applied before applying it
- Transfer: generalizing a principle across varied surface contexts (requires multiple varied examples)
- Misconception repair: contrasting correct and incorrect instances sharpens critical features

### Instructions
1. Identify the abstract concept or principle and its essential features.
2. Select or construct 2–3 examples that vary in surface features but share the deep structure ([Case Studies](../elements/case-studies.md) work well for rich domains).
3. Present the first example and make the mapping explicit — name which features carry the concept and which are incidental.
4. Have learners [Compare](../elements/comparing-cases.md) the examples to induce the common structure, or compare an example with a [Non-Example](../elements/non-examples.md).
5. State or elicit the general rule, then ask learners to apply it to a new, dissimilar case ([Application](../elements/application.md)).

## Related Strategies
- [Analogies](analogies.md) — a concrete example drawn from a familiar domain, used explicitly for structural mapping
- [Case-Based Learning](case-based-learning.md) — extended, authentic examples as the primary vehicle of instruction
- [Worked Examples](worked-examples-first.md) — concrete examples applied to problem-solving procedures
- Use worked examples — a concrete example applied to problem solving, with solution steps as the concrete content
- Use analogies and analogical comparison — a special case where the example comes from a different, familiar domain
- Use contrasting cases — the multi-example variant that guards against overgeneralization
- Teach with case studies — extended narrative examples used for complex, ill-structured domains

## Examples
- **Kaminski, Sloutsky & Heckler's math learning studies (2008)** — demonstrated that novices learning an abstract mathematical group structure from a concrete "mixing liquids" cover story transferred less well than those learning from abstract symbols, a caution about unexamined concreteness.
- **[Desmos](https://www.desmos.com) classroom activities** — introduce function concepts through concrete, manipulable instances (a marbleslide, a Ferris wheel) before formal notation.
- **[Physics Education Technology (PhET) simulations](https://phet.colorado.edu)** — concrete, manipulable instances of abstract physical principles (charge, waves) with explicit visual mappings to the underlying model.
- **Statistics teaching with real datasets** — teaching p-values first through a single concrete study (e.g., a coin-flipping or tea-tasting example) before the formal definition.
- **Statistics teaching with contrasting contexts**: Presenting the same chi-square test worked on three different datasets (medical, sports, consumer) so students extract the decision procedure rather than memorizing one scenario.
- **[Khan Academy](https://www.khanacademy.org)** — Every abstract math concept is introduced through concrete worked instances with visual models before symbolic notation is emphasized.
- **[Physics Education Technology (PhET) simulations](https://phet.colorado.edu)** — Concrete, manipulable instances of abstract physical principles (e.g., charges and fields), letting learners ground equations in observable behavior.
- **Case-based teaching at Harvard Business School** — Extended real-world cases serve as concrete instances from which students abstract management principles ([case-based learning improves exam performance](../claims/case-based-learning-improves-exam-performance.md) [+M]).

## Key Sources
- Kaminski, J. A., Sloutsky, V. M., & Heckler, A. F. (2008). The advantage of abstract examples in learning math. *Science, 320*(5875), 454–455. [doi:10.1126/science.1154659](https://doi.org/10.1126/science.1154659)
- Schwartz, D. L., & Bransford, J. D. (1998). A time for telling. *Cognition and Instruction, 16*(4), 475–522. [doi:10.1207/s1532690xci1604_4](https://doi.org/10.1207/s1532690xci1604_2)
- van Gog, T., & Rummel, N. (2010). Example-based learning: Integrating cognitive and social-cognitive research perspectives. *Educational Psychology Review, 22*(2), 155–174. [doi:10.1007/s10648-010-9134-7](https://doi.org/10.1007/s10648-010-9134-7)
- Clark, R. C., & Mayer, R. E. (2016). *E-Learning and the Science of Instruction* (4th ed.). Wiley. [doi:10.1002/9781119239086](https://doi.org/10.1002/9781119239086)
- Rawson, K. A., Thomas, R. C., & Jacoby, L. L. (2015). The power of examples: Illustrative examples enhance conceptual learning of declarative concepts. *Educational Psychology Review, 27*(3), 483–504. [doi:10.1007/s10648-014-9273-3](https://doi.org/10.1007/s10648-014-9273-3)
- Schwartz, D. L., Chase, C. C., Oppezzo, M. A., & Chin, D. B. (2011). Practicing versus inventing with contrasting cases: The effects of telling first on learning and transfer. *Journal of Educational Psychology, 103*(4), 759–775. [doi:10.1037/a0025140](https://doi.org/10.1037/a0025140)
- Sweller, J., Ayres, P., & Kalyuga, S. (2011). *Cognitive load theory*. Springer. [doi:10.1007/978-1-4419-8126-4](https://doi.org/10.1007/978-1-4419-8126-4)
- Gentner, D., Loewenstein, J., & Thompson, L. (2003). Learning and transfer: A general role for analogical encoding. *Journal of Educational Psychology, 95*(2), 393–408. [doi:10.1037/0022-0663.95.2.393](https://doi.org/10.1037/0022-0663.95.2.393)
- Mayer, R. E. (2014). Cognitive theory of multimedia learning. In R. E. Mayer (Ed.), *The Cambridge Handbook of Multimedia Learning* (2nd ed., pp. 43–71). Cambridge University Press. [doi:10.1017/CBO9781139547369.005](https://doi.org/10.1017/CBO9781139547369.005)

<!-- merged 2026-10-13 from strategies/use_concrete_examples ("Use Concrete Examples"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Use Concrete Examples

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (6 for) · 13 studies (7 causal, 3 quant-synthesis, 3 review), `q2`–`q4` · 2 of 13 report an effect size

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
-->
