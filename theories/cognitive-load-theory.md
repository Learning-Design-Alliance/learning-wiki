---
type: theory
title: Cognitive Load Theory
description: Cognitive Load Theory (CLT) proposes that learning is constrained by the limited capacity of working memory.
status: review
generated:
  by: claude/unspecified
  at: 2026-04-06
sources:
  - id: sweller-1988
    resource: "https://doi.org/10.1207/s15516709cog1202_4"
    title: "Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science, 12*(2), 257–285"
    author: Sweller, J
  - id: sweller-1998
    resource: "https://doi.org/10.1023/A:1022193728205"
    title: "Sweller, J., van Merriënboer, J. J. G., & Paas, F. G. W. C. (1998). Cognitive architecture and instructional design. *Educational Psychology Review, 10*(3), 251–296"
    author: "Sweller, J., van Merriënboer, J. J. G., & Paas, F. G. W. C"
  - id: paas-2003
    resource: "https://doi.org/10.1207/S15326985EP3801_1"
    title: "Paas, F., Renkl, A., & Sweller, J. (2003). Cognitive load theory and instructional design: Recent developments. *Educational Psychologist, 38*(1), 1–4"
    author: "Paas, F., Renkl, A., & Sweller, J"
  - id: sweller-2019
    resource: "https://doi.org/10.1007/s10648-019-09465-5"
    title: "Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). Cognitive architecture and instructional design: 20 years later. *Educational Psychology Review, 31*(2), 261–292"
    author: "Sweller, J., van Merriënboer, J. J. G., & Paas, F"
  - id: van-merriënboer-2018
    resource: "https://doi.org/10.4324/9781315113210"
    title: "van Merriënboer, J. J. G., & Kirschner, P. A. (2018). *Ten steps to complex learning* (3rd ed.). Routledge"
    author: "van Merriënboer, J. J. G., & Kirschner, P. A"
---

# Cognitive Load Theory

> **Theory** · [All theories](index.md)

## Description
Cognitive Load Theory (CLT) proposes that learning is constrained by the limited capacity of working memory. When the total cognitive demand of a learning task exceeds that capacity, learning breaks down — not because the learner lacks ability, but because the instructional design has exhausted the resources available for processing. The theory distinguishes three sources of load and argues that effective instruction reduces unnecessary load to free capacity for the mental work that actually builds schema.

CLT was developed by John Sweller and colleagues in the 1980s–1990s, drawing on George Miller's work on working memory limits and Alan Baddeley's model of working memory components. Its central claim is that instructional design should treat working memory capacity as the binding constraint: the question is not just "what should I teach?" but "how much mental demand does this design impose, and on what?"

## Three Types of Load

**Intrinsic load** is inherent to the material itself — determined by the number of interacting elements the learner must hold in mind simultaneously. High-element-interactivity content (e.g., parsing a sentence, debugging a recursive function) cannot be simplified without distorting it; but it can be sequenced so simpler schemas are built first.

**Extraneous load** is imposed by poor instructional design — split-attention effects, redundant information, unnecessary navigation, irrelevant detail. Extraneous load consumes working memory capacity without contributing to learning. This is the type CLT most directly targets: the primary design goal is to eliminate it.

**Germane load** (in revised CLT) refers to the cognitive effort invested in schema construction and automation — the work that actually produces learning. Earlier formulations treated germane load as a third type to be increased; current CLT treats it as the portion of intrinsic load that is productively engaged, not a separate load type.

## Implications

### Context
- Applies wherever learning requires holding multiple interacting elements in working memory simultaneously — mathematics, programming, language acquisition, clinical reasoning, reading comprehension
- Effect is strongest with novices; as expertise develops, previously separated elements are chunked into single schemas and cease to impose separate load demands (the basis of the [expertise reversal effect](expertise-reversal-effect.md))
- Design choices that reduce extraneous load are never harmful; but scaffolding that reduces intrinsic load too aggressively can prevent the element-interactivity processing needed for schema formation

### Target Learners
- Novices with limited prior knowledge in the domain benefit most from CLT-informed design
- Experts may find the same scaffolds redundant or distracting — what reduces load for a novice can introduce it for an expert
- Learners with limited working memory capacity (e.g., younger children, learners under high cognitive stress) are most sensitive to extraneous load

### Target Learning Objectives
- Procedural skill acquisition: learning to execute multi-step processes
- Conceptual understanding of content with high element interactivity
- Transfer: schema formation is the mechanism by which knowledge transfers to new problems

## Claims

- [Example–problem sequences reduce cognitive load and improve learning outcomes](../claims/worked-examples-example-problem-sequences.md) [+S] — example-based sequences reduce load compared to problem-only practice for novices; provides direct experimental evidence for the worked example effect as a CLT application
- [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M] — worked examples reduce unnecessary search load, freeing working memory for schema construction
- [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M] — expertise reversal: as schemas develop, the same guidance that reduced load for novices begins to impose redundancy load on more experienced learners

## Related Theories

- [Situated Learning](situated-learning.md) — CLT treats working memory as an individual cognitive limit; situated learning argues that cognition is distributed across tools, people, and environment, which can extend effective working memory capacity
- [Self-Regulated Learning](self-regulated-learning.md) — SRL requires learners to monitor and regulate their own processing; CLT explains why novices often cannot self-regulate effectively — metacognitive monitoring itself consumes working memory
- [Dual Coding Theory](dual-coding-theory.md) — Paivio's dual coding theory (separate verbal and visual channels) is a compatible model; multimedia learning theory (Mayer) applies both CLT and dual coding to instructional media design
- [Constructivism](constructivism.md) — tension point: constructivist approaches favor active discovery, which can impose high extraneous load; CLT favors explicit instruction for novices, but converges with constructivism for more expert learners (see expertise reversal)

## Examples

**[Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md)** — implements CLT by sequencing the modeling → coaching → fading arc: the modeling phase offloads element-interactivity processing onto the expert's narrated demonstration, reducing load during initial acquisition and fading support as schemas form.

**[Demonstration](../elements/demonstration.md)** — the worked example is CLT's most direct instructional expression; by presenting a fully solved problem, demonstration eliminates the search component of problem solving, which is the primary source of extraneous load for novices.

**[Use Worked Examples](../strategies/use_worked_examples.md)** — concrete application of CLT's worked example effect; the study-then-solve cycle is a direct implementation of the example-problem sequence shown to reduce load and improve transfer.

## Key Sources
- Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science, 12*(2), 257–285. [doi:10.1207/s15516709cog1202_4](https://doi.org/10.1207/s15516709cog1202_4)
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. G. W. C. (1998). Cognitive architecture and instructional design. *Educational Psychology Review, 10*(3), 251–296. [doi:10.1023/A:1022193728205](https://doi.org/10.1023/A:1022193728205)
- Paas, F., Renkl, A., & Sweller, J. (2003). Cognitive load theory and instructional design: Recent developments. *Educational Psychologist, 38*(1), 1–4. [doi:10.1207/S15326985EP3801_1](https://doi.org/10.1207/S15326985EP3801_1)
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). Cognitive architecture and instructional design: 20 years later. *Educational Psychology Review, 31*(2), 261–292. [doi:10.1007/s10648-019-09465-5](https://doi.org/10.1007/s10648-019-09465-5)
- van Merriënboer, J. J. G., & Kirschner, P. A. (2018). *Ten steps to complex learning* (3rd ed.). Routledge. [doi:10.4324/9781315113210](https://doi.org/10.4324/9781315113210)
