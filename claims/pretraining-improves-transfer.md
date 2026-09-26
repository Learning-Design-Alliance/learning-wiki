---
type: claim
title: Pretraining Improves Transfer
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: pretraining-improves-transfer
evidence_strength:
sources:
  - id: delgado-and-mayer-2024
    resource: "https://doi.org/10.1111/jcal.13099"
    title: "Delgado, C. Y., & Mayer, R. E. (2024). Implementing Pretraining to Optimise Learning in Immersive Virtual Reality. *Journal of Computer Assisted Learning, 41*(1). [doi:10.1111/jcal.13099](https://doi.org/10.1111/jcal.13099)"
    author: "Delgado, C. Y., & Mayer, R. E."
    q: 3
    i: "?"
    n: 93
---

# Pretraining Improves Transfer

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q3` peer-reviewed experiment · n=93

Learners who receive instruction on key concepts, terms, or characteristics of a system *before* the main instruction show better transfer than learners who receive the same content integrated into or after the main instruction.

## Subclaims

`q3 i?` A randomized experiment giving learners a pretraining video naming the parts and functions of an unfamiliar tool before an immersive-VR procedural lesson produced better knowledge-test scores and fewer errors on a subsequent real-world transfer task than the same lesson with no pretraining. [→ Delgado and Mayer 2024](#delgado-and-mayer-2024)

## Evidence

### Delgado and Mayer 2024

Delgado, C. Y., & Mayer, R. E. (2024). Implementing Pretraining to Optimise Learning in Immersive Virtual Reality. *Journal of Computer Assisted Learning, 41*(1). [doi:10.1111/jcal.13099](https://doi.org/10.1111/jcal.13099)

`q3 · peer-reviewed randomized experiment` · `i? · no standardized effect size reported` · `n=93`

Ninety-three participants were randomly assigned to a pretraining group (who watched a video naming the parts and characteristics of a micropipette before an immersive virtual-reality lesson) or a no-pretraining group (who went straight into the same VR lesson). After the VR training phase and an in-VR test, all participants performed a modified version of the task in a real-life setting, plus a knowledge test and cognitive-load, presence, and self-efficacy measures. The pretraining group scored significantly higher on the knowledge test and made fewer errors on the real-life transfer task than the no-pretraining group, with lower reported cognitive load and no group differences in presence, self-efficacy, or errors during the in-VR test itself — i.e., pretraining's benefit showed up specifically on transfer to the real-world task, not on performance inside the VR lesson.

## Discussion

**Mechanism.** Pretraining is one of the classic cognitive load management techniques: by naming key concepts and their characteristics before the main lesson, it reduces the extraneous processing learners would otherwise spend simultaneously building a mental model of the system and deciphering new terminology. This aligns with [Cognitive Load Theory](../theories/cognitive-load-theory.md) and with the broader claim that [cognitive overload degrades learning](cognitive-overload-degrades-learning.md). Pretraining is closely related to [advance organizers](../elements/advance-organizers.md) and to [activation](activation-improves-learning.md) of prior knowledge, but is narrower: it front-loads specific conceptual vocabulary needed to understand the upcoming instruction, rather than providing a general organizing structure.

**Moderators and boundary conditions.** Pretraining is expected to benefit learners who lack familiarity with the domain's key concepts — the same novice population for which [worked examples](../elements/demonstration.md) and [chunking](chunking-reduces-working-memory-load.md) help most. For learners who already know the pretraining content, it risks redundancy and wasted time, consistent with the expertise-reversal pattern described in [Expertise Reversal Effect](../theories/expertise-reversal-effect.md). Pretraining is most plausible when the main instruction is complex, interactive, or multimedia-based (e.g., simulations, animations), where simultaneous processing of new names and new dynamics is most likely to overload working memory.

**Design implications.** In practice, pretraining means a short, focused primer — names of components, key terms, or the main characteristics of a system — delivered before a simulation, animation, or complex explanation, not a lengthy preliminary unit. The primer should be minimal: content that merely duplicates the main instruction adds time without reducing load. Where the main instruction is already simple or the audience is expert, the pretraining segment can be cut or folded into the lesson itself.

**Open questions.** The one study recorded above is a single VR experiment read as an abstract, with no standardized effect size; the original multimedia pretraining experiments, and how widely the effect holds across domains, are not yet recorded here. Until then, this page should be treated as a theoretically motivated hypothesis rather than an empirically rated claim. Key open questions include whether pretraining benefits persist to delayed transfer tests, whether the effect holds in classroom settings (as opposed to controlled multimedia experiments), and how long the pretraining segment can be before it stops paying for itself in reduced load during the main instruction.

## Related Claims

- [Advance organizers improve learning](advance-organizers-improve-learning.md) — front-loading structure before instruction, a close cousin of pretraining
- [Activation improves learning](activation-improves-learning.md) — prior-knowledge activation as a precondition for new learning
- [Chunking reduces working memory load](chunking-reduces-working-memory-load.md) — the working-memory constraint pretraining addresses
- [Cognitive overload degrades learning](cognitive-overload-degrades-learning.md) — the failure mode pretraining is designed to prevent
- [Analogical reasoning improves transfer](analogical-reasoning-improves-transfer.md) — another route to transfer via well-structured prior knowledge
- [Embedding pretraining outperforms end-to-end training in DynEmb, avoiding the overfitting that end-to-end training exhibits](embedding-pretraining-beats-end-to-end-training-dynemb.md) — related
- [Whole-task performance improves transfer of complex skills to real-world settings.](whole-task-performance-improves-transfer.md) — related