---
type: claim
title: Interleaving Improves Discrimination
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
id: interleaving-improves-discrimination
evidence_strength: unrated
newest_evidence: 2019
sources:
  - id: kornell-bjork-2008
    resource: "https://doi.org/10.1111/j.1467-9280.2008.02127.x"
    title: "Kornell, N., & Bjork, R. A. (2008). Learning concepts and categories: Is spacing the enemy of induction? *Psychological Science, 19*(6), 585–592. [doi:10.1111/j.1467-9280.2008.02127.x](https://doi.org/10.1111/j.1467-9280.2008.02127.x)"
    author: "Kornell, N., & Bjork, R. A."
    q: 3
    i: "?"
    kind: causal
    rigour: "?"
  - id: rohrer-taylor-2007
    resource: "https://doi.org/10.1007/s11251-007-9015-8"
    title: "Rohrer, D., & Taylor, K. (2007). The shuffling of mathematics problems improves learning. *Instructional Science, 35*(6), 481–498. [doi:10.1007/s11251-007-9015-8](https://doi.org/10.1007/s11251-007-9015-8)"
    author: "Rohrer, D., & Taylor, K."
    q: 3
    i: "?"
    kind: causal
    rigour: "?"
  - id: brunmair-richter-2019
    resource: "https://doi.org/10.1037/bul0000209"
    title: "Brunmair, M., & Richter, T. (2019). Similarity matters: A meta-analysis of interleaved learning and its moderators. *Psychological Bulletin, 145*(11), 1029–1052. [doi:10.1037/bul0000209](https://doi.org/10.1037/bul0000209)"
    author: "Brunmair, M., & Richter, T."
    q: 4
    i: "?"
    kind: quant-synthesis
    rigour: "?"
---

# Interleaving Improves Discrimination

> **Claim** · [All claims](index.md)
> **Evidence** · 3 studies · 2 causal `r?`, 1 quant-synthesis `r?` · `q3`–`q4`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person

Interleaving — mixing different problem or category types within a practice sequence rather than blocking them — improves learners' ability to discriminate between confusable concepts and select the appropriate strategy.

## Subclaims

`q3 i?` Learners who studied paintings by different artists interleaved were better at classifying *new* paintings by those artists than learners who studied each artist in a block — and the majority believed blocking had served them better. [→ Kornell & Bjork 2008](#kornell-bjork-2008)

`q3 i?` Mathematics practice shuffled across problem types produced far better delayed test performance than the same problems practised in blocks, despite worse performance during practice itself. [→ Rohrer & Taylor 2007](#rohrer-taylor-2007)

`q4 i?` Meta-analysis found a reliable overall interleaving benefit that depends on the similarity of the categories being learned: interleaving helps most where categories are confusable, and can fail where they are not. [→ Brunmair & Richter 2019](#brunmair-richter-2019)

## Evidence

### Kornell & Bjork 2008

Kornell, N., & Bjork, R. A. (2008). Learning concepts and categories: Is spacing the enemy of induction? *Psychological Science, 19*(6), 585–592. [doi:10.1111/j.1467-9280.2008.02127.x](https://doi.org/10.1111/j.1467-9280.2008.02127.x)

`q3` · `i? · the abstract prints no effect size; the full text may` · `causal · r?`

Participants studied paintings by a number of artists, interleaved or blocked, then classified previously unseen paintings. Interleaving produced better induction. The metacognitive result is the memorable one: most participants judged blocking to have been more effective, including many whose own scores contradicted them.

### Rohrer & Taylor 2007

Rohrer, D., & Taylor, K. (2007). The shuffling of mathematics problems improves learning. *Instructional Science, 35*(6), 481–498. [doi:10.1007/s11251-007-9015-8](https://doi.org/10.1007/s11251-007-9015-8)

`q3` · `i? · no source text available to check; the entry prints no effect size` · `causal · r?`

Students practised mathematics problems of several types either blocked by type or shuffled. Blocked practice produced better accuracy during practice and much worse accuracy on a delayed test. The study is the clearest demonstration that practice-time performance and retention can move in opposite directions on the same manipulation.

### Brunmair & Richter 2019

Brunmair, M., & Richter, T. (2019). Similarity matters: A meta-analysis of interleaved learning and its moderators. *Psychological Bulletin, 145*(11), 1029–1052. [doi:10.1037/bul0000209](https://doi.org/10.1037/bul0000209)

`q4` · `i? · the abstract prints no effect size; the full text may` · `quant-synthesis · r?`

A meta-analysis of interleaved against blocked learning across materials. The overall effect favoured interleaving, and the dominant moderator was the similarity between categories: high-similarity, confusable categories gained most, and the benefit diminished or reversed as categories became more distinct. This is the result that turns interleaving from a universal recommendation into a conditional one.

## Discussion

**Mechanism.** The leading account is discriminative contrast: when exemplars of different categories appear adjacent in a mixed sequence, learners are forced to notice the features that distinguish them, whereas blocked practice allows a single strategy to be applied repeatedly without comparison. Interleaving also induces desirable difficulties — retrieval of the appropriate strategy from long-term memory rather than holding it active across a block — which can depress practice performance while improving delayed test performance. This retrieval demand connects interleaving to the broader spacing family of effects.

**Boundary conditions.** Benefits are largest when the interleaved categories are highly confusable (e.g., volume of prisms vs. cones, painting styles of similar artists) and when each item is still accompanied by feedback. Interleaving unrelated topics, or interleaving before learners have any initial exposure to the categories, can produce confusion and overload — consistent with the broader pattern in [Cognitive Load Theory](../theories/cognitive-load-theory.md) that germane comparison demands must fit within working-memory limits (see [Chunking reduces working memory load](../claims/chunking-reduces-working-memory-load.md)) [~M]. A common hybrid is to block briefly for initial exposure, then interleave.

**Performance paradox.** Learners in interleaved conditions typically perform worse during practice yet better on delayed tests, so subjective ratings of learning often diverge from actual outcomes [-W]. Designers and learners should not treat practice fluency as evidence of learning — a miscalibration risk that also motivates [Assessment for Learning](../principles/assessment-for-learning.md) approaches in which judgments of progress are checked against actual performance.

**Expertise.** As with other desirable difficulties, the advantage may shrink or reverse for very advanced learners who already discriminate fluently [~M] — see [Expertise Reversal Effect](../theories/expertise-reversal-effect.md).

**Design implications.** Where the goal is strategy selection among confusable problem types — the typical case in mathematics and perceptual classification — interleaved sequencing is the default recommendation, with brief blocked exposure first for novices. Where the goal is fluency within a single procedure, blocking remains appropriate. Sequencing decisions should be treated as a load-management lever (see [Cognitive Load Management](../principles/cognitive-load-management.md)) rather than a fixed rule.

**Open questions.** Most evidence comes from perceptual-category and mathematics learning with short retention intervals; the durability of effects over months and their generality to other domains remain to be established. Until controlled studies are added to the Evidence section, the strength of this claim cannot be rated.

**On this page's `evidence_strength: unrated`.** The rating predates these sources and should be
revisited: a meta-analysis plus two well-cited experiments would normally support at least *moderate*.
The reason to raise it deliberately rather than automatically is the moderator — the claim as titled
is about *discrimination*, which is the condition under which the evidence is strongest, so the
narrow claim may be better supported than a general "interleaving improves learning" would be.

## Related Claims

- [Cognitive overload degrades learning](../claims/cognitive-overload-degrades-learning.md) — interleaving adds comparison demands that can overwhelm novices if unmanaged
- [Chunking reduces working memory load](../claims/chunking-reduces-working-memory-load.md) — capacity limits constrain how much interleaved contrast learners can process
- [Expertise Reversal Effect](../theories/expertise-reversal-effect.md) — desirable difficulties can lose their advantage as expertise grows
- [Cognitive Load Management](../principles/cognitive-load-management.md) — sequencing choices (blocked vs. interleaved) are a core load-management lever
- [Assessment for Learning](../principles/assessment-for-learning.md) — the practice-performance paradox makes external checks on learning essential when interleaving
- [Interleaving category examples improves inductive category learning for visual and mathematical materials, but not for expository texts or word categories](interleaving-improves-inductive-learning.md) — a broader claim this one bears on
- [Learners Misjudge Spacing Benefits](learners-misjudge-spacing-benefits.md) — related
- [Interleaving benefits are small for mathematical tasks and absent or reversed for expository texts and words](interleaving-limited-for-math-texts-and-words.md) — related
- [The interleaving effect generalizes to visual materials, with the largest effects for paintings](interleaving-strongest-for-paintings-visual-materials.md) — a broader claim this one bears on
- [Interleaved practice produces higher mathematics test scores than blocked practice in a classroom experiment](interleaved-practice-higher-math-test-scores.md) — related
- [The interleaving benefit is not caused by spacing, and the benefit extends to delayed tests](interleaving-not-spacing-persists-over-delay.md) — related
- [Interleaving is especially useful for inductive, subtle pattern learning without a clear verbal rule, but can equal or exceed blocking in rule-based domains too](interleaving-rule-based-learning-boundary.md) — related
- [Interleaving benefits transfer to novel items from a learned category, with effect sizes of up to 0.66](interleaving-transfer-benefit-meta-analysis.md) — possibly the same claim (merge candidate)
- [Evidence on working memory capacity as a moderator of the interleaving effect is mixed, but WM does not appear to be a major barrier to classroom use](working-memory-mixed-moderator-interleaving.md) — related
- [Learners overwhelmingly judge blocking more effective than interleaving even when their test performance favors interleaving](metacognitive-illusion-blocking-interleaving.md) — possibly the same claim (merge candidate)
- [Sequencing rather than concept selection explains most of the EVOL–PPO-vanilla EP gap on ASSIST15 L=10](sequencing-explains-evol-ppo-gap.md) — related
- [Interleaving during concept learning benefits memory of studied items, with effect sizes (Hedges' g) of up to 0.65](interleaving-memory-benefit-meta-analysis.md) — related
- [Interleaved practice yields better category learning than blocked practice, and students who choose interleaved practice outperform those who choose blocked practice on novel materials](interleaving-effect-category-learning-paintings.md) — a broader claim this one bears on
- [Even when motivated to distinguish and informed that differences matter, learners in Experiment 1 blocked 68% of their study sequence choices](blocking-persists-despite-motivation-and-instruction.md) — related
- [Combining utility value of distinguishing with conditional knowledge fosters interleaving of confusable categories (Abel et al., 2024)](utility-value-conditional-knowledge-foster-interleaving.md) — related
- [In Experiment 1, personalized feedback after the test made students significantly more positive about interleaved studying, yet they still did not consider it more effective or desirable than blocked studying](feedback-improves-interleaved-considerations-exp1.md) — related
- [In Experiment 1, students' prospective judgments of learning were higher for blocked studying even though actual test performance was higher for interleaved studying](jol-outcome-dissociation-interleaved-exp1.md) — related
- [Interleaving—presenting different concepts in alternation rather than repeating the same concept—improves students' discrimination among similar concepts, terms, and principles](interleaving-improves-discrimination-similar-concepts.md) — possibly the same claim (merge candidate)