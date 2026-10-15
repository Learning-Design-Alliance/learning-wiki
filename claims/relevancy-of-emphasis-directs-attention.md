---
type: claim
title: Relevancy of emphasized text directs attention and influences test performance
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
evidence_strength: moderate
sources:
  - id: nist-1985
    resource: "https://eric.ed.gov/?id=ED265520"
    title: "Nist, S. L., & Hogrebe, M. C. (1985). The Effects of High and Low Relevant Text Underlining on Test Performance. [ERIC ED265520](https://eric.ed.gov/?id=ED265520)"
    author: "Nist, S. L., & Hogrebe, M. C."
    q: 3
    i: "?"
    n: 67
    kind: causal
    rigour: "?"
  - id: nist-1985-2
    resource: "https://eric.ed.gov/?id=ED265520"
    title: "Nist, S. L., & Hogrebe, M. C. (1985). The Effects of High and Low Relevant Text Underlining on Test Performance. [ERIC ED265520](https://eric.ed.gov/?id=ED265520)"
    author: "Nist, S. L., & Hogrebe, M. C."
    q: 3
    i: "?"
    n: 67
    kind: causal
    rigour: "?"
id: relevancy-of-emphasis-directs-attention
---

# Relevancy of emphasized text directs attention and influences test performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r?` · `q3`

Emphasis cues such as underlining do not simply boost learning overall — they shift attention toward whatever is emphasized, so test performance follows the *relevancy* of the marked material rather than the mere presence of marking.

## Subclaims

`q3 i?` Emphasizing high-relevant material produces higher scores on questions targeting that high-relevant material. [→ Nist 1985](#nist-1985)

`q3 i?` Emphasizing low-relevant material produces higher scores on questions targeting that low-relevant material. [→ Nist 1985 (2)](#nist-1985-2)

## Evidence

Primary evidence link: https://eric.ed.gov/?id=ED265520

### Nist 1985

Nist, S. L., & Hogrebe, M. C. (1985). The Effects of High and Low Relevant Text Underlining on Test Performance. [ERIC ED265520](https://eric.ed.gov/?id=ED265520)

`q3 · peer-reviewed experiment, not pre-registered` · `i? · F values only, no effect size printed` · `n=67` · `causal · r?`

Sixty-seven college freshmen read text passages with [underlining](../principles/annotating.md) applied to either high-relevant or low-relevant content, then completed a test with questions matched to both relevancy levels. A weighted-means ANOVA showed a significant main effect for relevancy on the high-relevant score, F(1, 49) = 13.56, p < .01: learners performed better on high-relevant questions when that material was the emphasized content. The pattern demonstrates that emphasis directs attention to the marked material, and test performance tracks what was marked.

### Nist 1985 (2)

Nist, S. L., & Hogrebe, M. C. (1985). The Effects of High and Low Relevant Text Underlining on Test Performance. [ERIC ED265520](https://eric.ed.gov/?id=ED265520)

`q3 · peer-reviewed experiment, not pre-registered` · `i? · F values only, no effect size printed` · `n=67` · `causal · r?`

In the same study, the main effect for relevancy was also significant for the low-relevant score, F(1, 40) = 6.98, p < .05. Learners scored higher on low-relevant questions when the low-relevant material was the emphasized content. Together with the high-relevant result, emphasis raised scores on whichever material was emphasized; that the effect is symmetric, of equal size regardless of the material's instructional importance, is not shown by the two F tests printed (unsourced on this page).

## Studies bearing on this claim

<!-- synthesis:start -->
*Does it matter what is cued, and what happens to attention to the rest?* This table gathers the studies behind this claim and the 9 narrower claims that bear on it: **5 distinct studies** (3 causal, 2 review), `q2`–`q3`, 2 of 5 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| Nist 1985 | q3 · causal · r? | i? | this claim; [In one experiment, students who generated their own underlining did not score significantl](experimenter-underlining-effective-as-student-underlining.md) (qualifies) |
| Mutlu-Bayraktar 2018 | q2 · causal · r1 | i? | [The change on the object being verbally described was the most detected change, seen by 10](signalled-and-cued-object-change-most-detected.md) (supports); [Among two objects with the same signalling, participants focused more on the arrow-cued ob](cueing-outcompetes-signalling-alone-for-attention.md) (supports); [Change in the most-focused central object was detected at a low rate (41.66%) unless it wa](central-object-change-detection-low-without-cueing.md) (supports); [In a multimedia animation, participants focused more on signalled objects and detected few](signalling-focuses-attention-reduces-change-detection-elsewhere.md) (qualifies) |
| [Yow 2019](https://doi.org/10.1177/2332858419878126) | q3 · causal · r1 | i3; i1 | [Audio narration with finger-tracking animation directs bilingual preschoolers' attention t](enhancing-features-direct-attention-dual-language-e-books.md) (supports); [The attention-guiding effect of narration-plus-animation is phase-dependent: target-langua](animation-phase-dependent-attention-to-print.md) (qualifies) |
| [Dunlosky et al. 2013](https://doi.org/10.1177/1529100612453266) | q3 · review · r3 | i? | [Highlighting shows low utility for improving learning outcomes](highlighting-low-utility.md) (counts against) |
| [Richard E. Mayer 2008](https://doi.org/10.1037/0003-066x.63.8.760) | q3 · review · r2 | i2 | [Signaling principle: highlighting essential words improves transfer from multimedia lesson](signaling-principle-mayer-2008.md) (supports) |
<!-- synthesis:end -->

## Discussion

**Attention follows marking, not importance.** The two findings combine into a single mechanism: emphasis acts as an [attention](../elements/attention.md) cue, and learners allocate study time and processing to cued content. This is double-edged. Marking the *right* content scaffolds selective attention and improves outcomes; marking the *wrong* content misdirects attention away from what matters, producing the same measurable shift toward trivial material. This aligns with the broader coherence finding that irrelevant material hurts learning — see [Irrelevant material hurts learning (coherence principle).](../claims/coherence-principle-irrelevant-material-hurts-learning.md) [+M]

**Design implication.** The relevancy of instructor-provided emphasis is a design decision with direct assessment consequences. Textbook highlighting, slide emphasis, and pre-annotated readings should mark content that maps onto intended learning outcomes, not decorative or incidental detail. For learner-generated marking, the quality of what students choose to underline matters as much as the act of marking — see [Annotating improves learning.](../claims/annotating-improves-learning.md) [+M]

**Boundary conditions.** Both subclaims rest on one experiment with 67 college freshmen reading expository text with underlining as the emphasis device. Generalization to other marking formats (bolding, color), other populations, and longer or more complex texts is not yet established. No effect size is printed (only F values), and outcomes were measured immediately; durability of the attention-shift effect over delay is untested here.

## Related Claims

- [Coherence Principle Irrelevant Material Hurts Learning](coherence-principle-irrelevant-material-hurts-learning.md) — the general claim this finding bears on, with the studies behind it

- [Annotating improves learning.](../claims/annotating-improves-learning.md) — learner-generated marking interacts with the relevancy of what is marked
- [Irrelevant material hurts learning (coherence principle).](../claims/coherence-principle-irrelevant-material-hurts-learning.md) — emphasis on low-relevant content is a form of irrelevant material competing for attention
- [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) — selective emphasis helps learners chunk the most relevant content first
- [Von Restorff effect and text marking.](../theories/von-restorff-effect-text-marking.md) — distinctiveness of marking underlies the attention shift
- [Highlighting shows low utility for improving learning outcomes](highlighting-low-utility.md) — related
- [Classroom interactional structures such as questions, recasts, and feedback influence students' processing of targeted content](interactional-structures-shape-content-processing.md) — related
- [Prior knowledge is not significantly related to test performance in this sample](prior-knowledge-not-related-to-performance.md) — related
- [Students' prior knowledge about a topic impacts their understanding of text as they read](prior-knowledge-impacts-text-understanding.md) — related