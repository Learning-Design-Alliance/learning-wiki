---
type: claim
title: Self Explanation Prompts Improve Learning
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
id: se-1
evidence_strength:
---

# Self Explanation Prompts Improve Learning

> **Claim** · [All claims](index.md)

Prompting learners to explain to themselves how new material relates to what they already know — and why steps in a solution or text make sense — improves learning outcomes relative to studying the same material without such prompts.

## Subclaims

<!-- TODO -->

## Evidence

<!-- TODO -->

## Discussion

**Mechanism.** Self-explanation prompts work by forcing learners to go beyond passive restatement: they map new information onto prior knowledge, expose gaps in understanding, and help learners infer the underlying principles behind worked steps or textual claims. This aligns with the broader generative-learning position that learning improves when learners actively construct connections rather than receive explanations — see [Activation improves learning](activation-improves-learning.md) [+M] and [Active learning improves exam performance](active-learning-improves-exam-performance.md) [+S].

**Boundary conditions.** The benefit is strongest for novices, who otherwise skip self-explanation or do it shallowly. For more advanced learners, prompts can become redundant or interrupt fluent processing — the same expertise-reversal pattern documented for [worked examples](../elements/demonstration.md) and formalized in [expertise reversal](../theories/expertise-reversal-effect.md) [~M]. Prompt design also matters: open-ended "explain why" prompts can overload limited working memory if the material is high in element interactivity, in which case providing the key explanation (an "assisted" or scaffolded prompt) can outperform pure self-generation [~M]. This connects to [Cognitive overload degrades learning](cognitive-overload-degrades-learning.md) [-S] and [Chunking reduces working memory load](chunking-reduces-working-memory-load.md) [+S], and situates the strategy within [cognitive load management](../principles/cognitive-load-management.md).

**Prompt placement and format.** Prompts can be attached to worked steps, textual passages, or multimedia segments. Principle-based prompts ("what principle does this step illustrate?") and gap-targeted prompts tend to focus explanation on the deep structure of the material, whereas vague prompts ("explain this to yourself") risk eliciting paraphrase rather than genuine elaboration [~W]. Written explanations impose more load than oral or prompted-selection formats, so designers of [annotating](annotating-improves-learning.md)-style tasks should weigh response format against material complexity.

**Open questions.** Evidence entries are still needed to establish effect sizes, the durability of gains on delayed tests, and how prompt type (principle-based vs. goal-based vs. gap-targeted) moderates outcomes. Until studies are added, treat the claim as directionally supported but unquantified.

## Related Claims

- [Worked examples reduce unnecessary search for novices.](worked-examples-reduce-novice-search.md) — self-explanation prompts are frequently layered onto worked examples to deepen their processing
- [Worked examples can become redundant or counterproductive for advanced learners.](worked-examples-expertise-reversal.md) — the same expertise-reversal moderation likely applies to explanation prompts
- [Activation improves learning.](activation-improves-learning.md) — self-explanation operates partly by connecting new material to activated prior knowledge
- [Annotating improves learning.](annotating-improves-learning.md) — a related generative strategy in which learners produce written elaborations during study
- [Cognitive load reduction improves learning.](cognitive-load-reduction-improves-learning.md) — prompt design must avoid adding extraneous load that offsets generative benefits