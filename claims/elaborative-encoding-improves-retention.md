---
type: claim
title: Elaborative Encoding Improves Retention
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: elaborative-encoding-improves-retention
evidence_strength: pending
sources:
  - id: bisra-et-al-2018
    resource: "https://doi.org/10.1007/s10648-018-9434-x"
    title: "Bisra, K., Liu, Q., Nesbit, J. C., Salimi, F., & Winne, P. H. (2018). Inducing self-explanation: A meta-analysis. *Educational Psychology Review, 30*(3), 703–725. [doi:10.1007/s10648-018-9434-x](https://doi.org/10.1007/s10648-018-9434-x)"
    author: "Bisra, K., Liu, Q., Nesbit, J. C., Salimi, F., & Winne, P. H."
    q: 4
    i: 2
    n: 69 effect sizes (64 research reports)
    kind: quant-synthesis
    rigour: "?"
---

# Elaborative Encoding Improves Retention

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · quant-synthesis `r?` · `q4` · `i2` medium · n=69 effect sizes (64 research reports)

Elaborative encoding — connecting new material to prior knowledge through self-explanation, examples, analogies, and "why" and "how" questions — produces more durable memory traces than rote rehearsal.

## Subclaims

`q4 i2` Prompting learners to self-explain — a core elaborative-encoding operationalization — produces a medium-sized average improvement in learning outcomes across a wide range of instructional conditions, tasks, and educational levels. [→ Bisra et al. 2018](#bisra-et-al-2018)

## Evidence

### Bisra et al. 2018

Bisra, K., Liu, Q., Nesbit, J. C., Salimi, F., & Winne, P. H. (2018). Inducing self-explanation: A meta-analysis. *Educational Psychology Review, 30*(3), 703–725. [doi:10.1007/s10648-018-9434-x](https://doi.org/10.1007/s10648-018-9434-x)

`q4 · well-powered meta-analysis` · `i2 · medium effect, g=0.55` · `n=69 effect sizes (64 research reports)` · `quant-synthesis · r?`

A systematic search of bibliographic databases identified 69 effect sizes from 64 research reports comparing learning outcomes for participants who received self-explanation prompts against comparison conditions while studying or solving problems. A random-effects model gave an overall weighted mean effect size of Hedges' g = 0.55, and the authors coded 20 moderator variables (task type — solving problems, studying worked examples, studying text — subject area, education level, type of inducement, and treatment duration), concluding self-explanation prompts are a potentially powerful intervention across a range of instructional conditions.

## Studies bearing on this claim

<!-- synthesis:start -->
*Does having learners generate their own elaborations improve learning, compared with no elaboration or with elaborations supplied to them?* This table gathers the studies behind this claim and the 7 narrower claims that bear on it: **4 distinct studies** (2 causal, 1 quant-synthesis, 1 review), `q2`–`q4`, 2 of 4 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Bisra et al. 2018](https://doi.org/10.1007/s10648-018-9434-x) | q4 · quant-synthesis · r? | i2 · medium effect, g=0.55 | this claim |
| [Xiong 2014](https://doi.org/10.5539/jel.v3n4p1) | q2 · causal · r2 | i? | [Self-generated elaboration improves procedural knowledge more than instructor-assisted ela](self-generated-elaboration-improves-procedural-knowledge-accounting.md) (supports); [Self-generated elaboration improves intellectual skills more than instructor-assisted elab](self-generated-elaboration-improves-intellectual-skills.md) (supports); [Cognitive elaboration strategy significantly affects overall posttest performance, with se](elaboration-strategy-affects-posttest-performance.md) (supports); [Elaboration strategy does not significantly affect students' attitudes toward the learning](elaboration-strategy-no-attitude-effect.md) (qualifies); [GPA, pretest score, and self-generated elaboration jointly predict intellectual skills but](gpa-pretest-elaboration-interaction-intellectual-skills.md) (qualifies) |
| Gagne 1981 | q2 · causal · r? | i2; i? | [Elaborative processing of prose enhances later retrievability, accounting for roughly 30% ](elaborative-processing-enhances-retrieval.md) (supports) |
| [Karpicke 2017](https://doi.org/10.1016/b978-0-12-809324-5.21055-9) | q2 · review · r3 | i? | [Whether prompting students to construct explanations during retrieval adds benefit beyond ](adding-explanation-prompts-to-free-recall-retrieval-has-mixed-effects.md) (qualifies) |
<!-- synthesis:end -->

## Discussion

**Mechanism.** Elaboration is typically explained through the depth-of-processing framework: richer, more meaningful processing creates more retrieval routes than shallow repetition. In practice, elaboration overlaps with several related operations — [activation](activation-improves-learning.md) of prior knowledge, [analogical reasoning](analogical-reasoning-improves-transfer.md), and [chunking](chunking-reduces-working-memory-load.md) — so isolating its unique contribution is difficult. Elaborative interrogation ("why is this true?") and self-explanation are the two most-studied operationalizations; both ask learners to integrate new material with what they already know rather than re-read it.

**Boundary conditions.** Elaboration is effortful and depends on working-memory capacity; learners with low prior knowledge may generate inaccurate elaborations that are then encoded and later retrieved as errors. Quality of elaboration matters more than quantity — self-generated connections to relevant prior knowledge support retention, while forced or superficial elaboration ("this word reminds me of my dog") may add processing load without adding meaning. This connects to [cognitive overload](cognitive-overload-degrades-learning.md): elaboration demands working-memory resources that overload can consume, so prompting learners to elaborate dense or unfamiliar material can backfire. Designers should therefore scaffold elaboration — provide partial prompts, worked examples of good elaborations, or [advance organizers](advance-organizers-improve-learning.md) that supply the knowledge to connect to — rather than issuing open-ended "explain this to yourself" instructions to novices.

**Moderators to expect.** When evidence is populated, likely moderators include prior knowledge (elaboration should benefit learners who have relevant knowledge to connect to), accuracy of self-generated elaborations (errors encoded during elaboration are later retrieved as errors), and outcome type — elaboration plausibly supports retention and comprehension more than it supports transfer, where [analogical reasoning](analogical-reasoning-improves-transfer.md) across cases does more work. Time pressure is a further moderator: elaborative strategies are slower than restudy, so under fixed study time the benefit can shrink or reverse.

**Open questions.** The evidence base for this claim still needs to be populated — studies comparing elaborative interrogation and self-explanation against restudy, and work on when elaboration helps retention versus transfer, should be added before this page is treated as authoritative.

## Related Claims

- [Activation improves learning.](activation-improves-learning.md) — elaboration works by connecting new material to activated prior knowledge
- [Analogical reasoning improves transfer.](analogical-reasoning-improves-transfer.md) — analogies are a core elaborative strategy
- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — elaboration organizes material into meaningful units
- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — elaboration demands working-memory resources that overload can consume
- [Advance organizers improve learning.](advance-organizers-improve-learning.md) — organizers supply the prior-knowledge structure that elaboration connects to
- [Generative Learning Improves Retention](generative-processing-improves-learning.md) — possibly the same claim (merge candidate)
- [Prompting learners to self-explain improves understanding and problem solving on immediate tests by a moderate average amount, with little evidence yet on delayed or classroom gains.](self-explanation-improves-conceptual-understanding.md) — possibly the same claim (merge candidate)
- [Revised post-teaching prompts (RPTAA) advanced candidates' capacity for more sophisticated analysis compared with the original prompts (PTAA)](revised-prompts-advance-sophisticated-analysis.md) — a narrower finding that bears on this claim
- [Language becomes an operational medium in AI-supported design, with risks of narrowing exploration](language-operational-medium-design-ai.md) — related
- [Immediate Elaborated Feedback in a formative assessment game significantly improved students' programming knowledge, interest, and problem-solving versus systems without immediate feedback](immediate-elaborated-feedback-improves-programming-learning.md) — related
- [Self-explanation prompting is potentially effective across a range of instructional conditions](self-explanation-effective-across-instructional-conditions.md) — possibly the same claim (merge candidate)
- [Students who self-explain worked examples learn more effectively than those who do not, and the quality of self-explanations relates to explaining deep structure](self-explanation-effect-worked-examples.md) — a narrower finding that bears on this claim
