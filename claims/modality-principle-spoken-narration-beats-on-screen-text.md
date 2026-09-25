---
type: claim
title: Modality Principle Spoken Narration Beats On Screen Text
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: modality-principle-spoken-narration-beats-on-screen-text
evidence_strength: weak
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

# Modality Principle Spoken Narration Beats On Screen Text

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q3`–`q4`

Presenting words as spoken narration rather than as on-screen text improves learning from graphics-based multimedia, because narration and pictures can be processed in parallel by separate channels while text and pictures compete for the same visual channel.

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

**Mechanism.** The modality principle follows from the dual-channel assumption of [Cognitive Load Theory](../theories/cognitive-load-theory.md): visual working memory must handle both pictures and written words, whereas spoken narration offloads verbal processing to the auditory channel. This reduces the risk of [cognitive overload degrading learning](cognitive-overload-degrades-learning.md), especially when graphics and words are presented simultaneously. It is closely related to [cognitive load management](cognitive-load-management.md) as a design goal: the modality choice is one of the most direct levers for redistributing load across channels.

**Boundary conditions.** The benefit is strongest for novices and for fast-paced, system-paced multimedia where learners cannot control the pace. With learner-paced environments, long or complex text, or learners who need to re-read (e.g., second-language learners or those with hearing impairments), on-screen text can be equal or superior — an instance of the [expertise reversal effect](../theories/expertise-reversal-effect.md) and a reminder that modality choices interact with learner characteristics. Narration should also respect the [coherence principle](coherence-principle-irrelevant-material-hurts-learning.md): adding audio does not help if it introduces irrelevant material.

**Design implications.** Prefer narration over on-screen text when words accompany animated or system-paced graphics, and keep narration conversational rather than formal. Do not duplicate the same words in both narration and on-screen text — redundancy reintroduces the visual-channel competition the modality principle is meant to avoid. Where learners must consult reference text (definitions, code, formulas), retain it as text rather than reading it aloud. Where pacing control is available, [chunking](chunking-reduces-working-memory-load.md) the material into segments gives learners the pause-and-replay capacity that narration otherwise removes.

**Open questions.** Most supporting evidence comes from short, lab-style lessons in well-structured domains; generalization to lengthy, complex, or self-paced online courses remains an active research question. The meta-analysis recorded above was read as an abstract and gives no pooled effect size.

## Related Claims

- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — the load mechanism the modality principle is designed to avoid
- [Coherence principle: irrelevant material hurts learning.](coherence-principle-irrelevant-material-hurts-learning.md) — narration must still exclude extraneous content
- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — complementary strategy for managing limited working memory
- [Cognitive Load Theory.](../theories/cognitive-load-theory.md) — the theoretical framework underlying the principle
- [Expertise reversal effect.](../theories/expertise-reversal-effect.md) — why the narration advantage fades or reverses for advanced learners