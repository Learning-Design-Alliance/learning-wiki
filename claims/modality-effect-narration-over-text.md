---
type: claim
title: Presenting words as spoken narration rather than on-screen text alongside graphics improves learning
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: modality-effect-narration-over-text
aliases: [modality-principle-narration-beats-on-screen-text, modality-principle-spoken-narration-beats-on-screen-text]
evidence_strength: unrated
sources:
  - id: ginns-2005
    resource: "https://doi.org/10.1016/j.learninstruc.2005.07.001"
    title: "Ginns, P. (2005). Meta-analysis of the modality effect. *Learning and Instruction, 15*(4), 313–331. [doi:10.1016/j.learninstruc.2005.07.001](https://doi.org/10.1016/j.learninstruc.2005.07.001)"
    author: Ginns, P.
    q: 4
    i: "?"
    n: 43 independent effects
  - id: mayer-and-moreno-1998
    resource: "https://doi.org/10.1037/0022-0663.90.2.312"
    title: "Mayer, R. E., & Moreno, R. (1998). A split-attention effect in multimedia learning: Evidence for dual processing systems in working memory. *Journal of Educational Psychology, 90*(2), 312–320. [doi:10.1037/0022-0663.90.2.312](https://doi.org/10.1037/0022-0663.90.2.312)"
    author: "Mayer, R. E., & Moreno, R."
    q: 3
    i: "?"
    n: 146
---

# Presenting words as spoken narration rather than on-screen text alongside graphics improves learning

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q3`–`q4`

Presenting words as spoken narration rather than on-screen text — alongside graphics or animation — improves learning, because distributing information across the auditory and visual channels reduces overload in the visual channel.

## Subclaims

`q4 i?` A meta-analysis of 43 independent effects found that presenting words as audio narration rather than on-screen text alongside graphics improved learning, with the benefit moderated by element interactivity, pacing, and field of study. [→ Ginns 2005](#ginns-2005)

`q3 i?` College students who heard words narrated aurally alongside computer-presented animation integrated words and pictures more easily than students who read the same words as on-screen text. [→ Mayer and Moreno 1998](#mayer-and-moreno-1998)

## Evidence

### Ginns 2005

Ginns, P. (2005). Meta-analysis of the modality effect. *Learning and Instruction, 15*(4), 313–331. [doi:10.1016/j.learninstruc.2005.07.001](https://doi.org/10.1016/j.learninstruc.2005.07.001)

`q4 · meta-analysis (43 independent effects: 39 between-subjects, 4 within-subjects)` · `i? · no pooled effect size available in what was read` · `n=43 independent effects`

A meta-analysis of the modality effect literature, pooling 43 independent effects (39 between-subjects designs, 4 within-subjects designs) comparing visual-plus-narration presentations against visual-plus-on-screen-text presentations. The major hypotheses about the instructional benefit of splitting text and graphics across the auditory and visual channels were supported, and the size of the benefit was moderated by level of element interactivity (material complexity) and by whether presentation was system-paced or learner-paced, and varied between fields of study. The strongest effect appeared under system-paced conditions, where visual-channel overload is most acute — consistent with [Cognitive Load Theory](../theories/cognitive-load-theory.md)'s account of the effect.

### Mayer and Moreno 1998

Mayer, R. E., & Moreno, R. (1998). A split-attention effect in multimedia learning: Evidence for dual processing systems in working memory. *Journal of Educational Psychology, 90*(2), 312–320. [doi:10.1037/0022-0663.90.2.312](https://doi.org/10.1037/0022-0663.90.2.312)

`q3 · peer-reviewed experiment` · `i? · no effect size available in what was read` · `n=146`

An experiment with 146 college students learning from a computer-based animation of lightning formation. Learners who heard the explanatory words as spoken narration alongside the animation were able to integrate the verbal and pictorial material more easily than learners who read the identical words as on-screen text alongside the same animation — the split-attention/modality effect the meta-analysis above later synthesized across studies. The authors interpret the result as evidence for a dual-channel (auditory/visual) working-memory architecture rather than a single visual-processing bottleneck.

## Discussion

The modality effect is a core prediction of [Cognitive Load Theory](../theories/cognitive-load-theory.md) and its dual-channel account of working memory: when graphics and written words both compete for visual processing, narration offloads verbal material to the auditory channel, freeing visual resources for the diagram or animation. This mechanism is closely related to the [dual coding](../theories/dual-coding-theory.md) tradition, though the two literatures make somewhat different predictions and should not be conflated. It is one of several working-memory interventions alongside [chunking](chunking-reduces-working-memory-load.md) and broader [cognitive load management](cognitive-load-management.md).

Several boundary conditions are well established in the literature and should guide design. The effect is strongest for **fast-paced, system-paced, graphics-heavy material** (e.g., animations) where the visual channel is genuinely overloaded [~M]; with learner-paced or static graphics, learners can self-manage the split attention and the benefit shrinks or disappears [~M]. The effect also shows an **expertise reversal** pattern: for advanced learners, narration can become redundant with the graphic and depress performance [-M] — see [Expertise Reversal Effect](../theories/expertise-reversal-effect.md). Finally, the effect applies to *explaining* words accompanying graphics, not to all text: narrating everything on screen violates the redundancy principle when text duplicates narration verbatim [-M].

Open questions include how the effect interacts with learner control over pacing, whether it holds for learners with auditory processing difficulties or non-native language proficiency [~W], and how it manifests in mobile or noisy listening environments where narration quality degrades [~W].

*Merged from “Modality Principle Narration Beats On Screen Text” (modality-principle-narration-beats-on-screen-text):* **Mechanism.** The modality principle is grounded in cognitive load theory and the dual-channel assumption of multimedia learning: the visual channel processes both graphics and text, so replacing on-screen text with narration offloads verbal material to the auditory channel and reduces the risk of visual overload [~M]. This is closely related to the broader account in [Cognitive Load Theory](../theories/cognitive-load-theory.md) and to [Coherence Principle: irrelevant material hurts learning](coherence-principle-irrelevant-material-hurts-learning.md).

**Boundary conditions.** The principle applies when words accompany graphics that the learner must inspect simultaneously. It does not apply to text-only material, to content the learner must re-read at their own pace (e.g., complex definitions or technical terms), or to learners with limited listening proficiency or hearing impairments. Narration that disappears can impose memory demands that static text does not, so designers should keep narrated segments short and avoid redundancy with identical on-screen text.

**Constraints on application.** The effect is strongest for system-paced lessons where learners cannot control the flow of information; in learner-paced environments, learners can compensate by switching attention between text and graphics, which weakens or eliminates the narration advantage [~M]. Presenting identical words as both narration and on-screen text (redundancy) can actively depress performance relative to narration alone, particularly for novices [-M]. For learners who are non-native listeners, hearing-impaired, or working with dense technical terminology that must be consulted repeatedly, on-screen text is the better choice and narration can impose extraneous transience costs [-M].

**Open questions.** Effect sizes vary with pacing (learner-controlled vs. system-paced lessons), learner expertise, and language proficiency. Evidence entries are needed to quantify these moderators before the claim can be rated for strength.

*Merged from “Modality Principle Spoken Narration Beats On Screen Text” (modality-principle-spoken-narration-beats-on-screen-text):* **Mechanism.** The modality principle follows from the dual-channel assumption of [Cognitive Load Theory](../theories/cognitive-load-theory.md): visual working memory must handle both pictures and written words, whereas spoken narration offloads verbal processing to the auditory channel. This reduces the risk of [cognitive overload degrading learning](cognitive-overload-degrades-learning.md), especially when graphics and words are presented simultaneously. It is closely related to [cognitive load management](cognitive-load-management.md) as a design goal: the modality choice is one of the most direct levers for redistributing load across channels.

**Boundary conditions.** The benefit is strongest for novices and for fast-paced, system-paced multimedia where learners cannot control the pace. With learner-paced environments, long or complex text, or learners who need to re-read (e.g., second-language learners or those with hearing impairments), on-screen text can be equal or superior — an instance of the [expertise reversal effect](../theories/expertise-reversal-effect.md) and a reminder that modality choices interact with learner characteristics. Narration should also respect the [coherence principle](coherence-principle-irrelevant-material-hurts-learning.md): adding audio does not help if it introduces irrelevant material.

**Design implications.** Prefer narration over on-screen text when words accompany animated or system-paced graphics, and keep narration conversational rather than formal. Do not duplicate the same words in both narration and on-screen text — redundancy reintroduces the visual-channel competition the modality principle is meant to avoid. Where learners must consult reference text (definitions, code, formulas), retain it as text rather than reading it aloud. Where pacing control is available, [chunking](chunking-reduces-working-memory-load.md) the material into segments gives learners the pause-and-replay capacity that narration otherwise removes.

**Open questions.** Most supporting evidence comes from short, lab-style lessons in well-structured domains; generalization to lengthy, complex, or self-paced online courses remains an active research question. The meta-analysis recorded above was read as an abstract and gives no pooled effect size.

## Related Claims

- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — the overload mechanism the modality effect is designed to prevent
- [Coherence principle: irrelevant material hurts learning.](coherence-principle-irrelevant-material-hurts-learning.md) — a companion multimedia principle governing what to exclude alongside how to present words
- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — an alternative route to the same working-memory bottleneck
- [Cognitive load reduction improves learning.](cognitive-load-reduction-improves-learning.md) — the broader family of load-reducing design interventions
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) — the theoretical framework from which the modality effect is derived
- [Dual Coding Theory](../theories/dual-coding-theory.md) — theoretical background on combining verbal and visual channels
- [Expertise reversal effect.](../theories/expertise-reversal-effect.md) — why the narration advantage fades or reverses for advanced learners
- [Dual Coding Improves Learning](dual-coding-improves-learning.md) — related
- [Dual Coding Improves Recall](dual-coding-improves-recall.md) — related
- [Audio narration with finger-tracking animation directs bilingual preschoolers' attention to the target-language print in dual-language e-books, including the nondominant language](enhancing-features-direct-attention-dual-language-e-books.md) — related
- [Expertise Reversal Guidance Hurts Experts](expertise-reversal-guidance-hurts-experts.md) — related
- [Redundant on-screen text duplicates of narration or graphics impair learning](redundancy-principle.md) — related
- [Redundancy Effect Impairs Learning](redundancy-effect-impairs-learning.md) — related
- [Redundancy Hurts Learning](redundancy-hurts-learning.md) — related
- [Screencast design findings: static vs. dynamic screen movement, explicit vs. implicit narration, and handwriting preferred though typefaces judged more legible](screencast-design-movement-narration-handwriting.md) — related
- [A majority of surveyed teachers report presenting words and corresponding graphics simultaneously, consistent with the modality effect](teachers-report-simultaneous-words-graphics-presentation.md) — related
