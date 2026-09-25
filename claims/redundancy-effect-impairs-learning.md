---
type: claim
title: Redundancy Effect Impairs Learning
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: redundancy-effect-impairs-learning
evidence_strength: weak
sources:
  - id: trypke-et-al-2023
    resource: "https://doi.org/10.3389/fpsyg.2023.1148035"
    title: "Trypke, M., Stebner, F., & Wirth, J. (2023). Two types of redundancy in multimedia learning: a literature review. *Frontiers in Psychology, 14*, Article 1148035. [doi:10.3389/fpsyg.2023.1148035](https://doi.org/10.3389/fpsyg.2023.1148035)"
    author: "Trypke, M., Stebner, F., & Wirth, J."
    q: 3
    i: "?"
    n: "63 studies (44 in the narration+on-screen-text \"scenario 4\")"
---

# Redundancy Effect Impairs Learning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q3` peer-reviewed experiment · n=63 studies (44 in the narration+on-screen-text "scenario 4")

When the same information is presented simultaneously through multiple channels — such as narrated text duplicating on-screen text, or graphics labeled with both text and redundant audio — learning is impaired relative to presenting the information once, because learners must coordinate and re-process identical material.

## Subclaims

`q3 i?` A literature review of 63 studies finds that adding written text which duplicates narration (verbal/"working-memory-channel" redundancy) most often impairs learning, though the direction reverses for some moderators (older learners, learner-paced delivery, non-identical/abridged text). [→ Trypke et al. 2023](#trypke-et-al-2023)

## Evidence

### Trypke et al. 2023

Trypke, M., Stebner, F., & Wirth, J. (2023). Two types of redundancy in multimedia learning: a literature review. *Frontiers in Psychology, 14*, Article 1148035. [doi:10.3389/fpsyg.2023.1148035](https://doi.org/10.3389/fpsyg.2023.1148035)

`q3 · systematic literature review (63 studies)` · `i? · no pooled effect size reported` · `n=63 studies (44 in the narration+on-screen-text "scenario 4")`

This review classifies redundancy effects across 63 multimedia-learning experiments into "content redundancy" (duplicated information, independent of channel) and "working-memory channel redundancy" (two sources competing for the same processing channel). For the case closest to the classic redundancy principle — narration duplicated by identical on-screen text — the authors report that among the 44 studies adding written text to narrated visualizations, several classic experiments (e.g., [Kalyuga et al. 1999](https://doi.org/10.1002/(SICI)1099-0720(199912)13:4%3C351::AID-ACP589%3E3.0.CO;2-6), Mayer et al. 2001, Yue et al. 2013) found that "the animation, narration, and identical written text group performed worse on retention and transfer tests," and note the finding "aligns with the findings of the meta-analysis on the verbal redundancy effect, which shows that narrations accompanied by identical written text impaired learning (e.g., Adesope and Nesbit, 2012)." The review also identifies moderators — degree of overlap (abridged/keyword text is less harmful than verbatim duplication), learner age, prior knowledge, and pacing — that shift or reverse the direction of the effect, which is why the overall pattern is reported as heterogeneous rather than as one pooled effect.

## Discussion

The redundancy effect is one of the classic effects predicted by [Cognitive Load Theory](../theories/cognitive-load-theory.md). The proposed mechanism is that when identical information is presented in two formats, working memory resources are consumed holding one representation while the learner maps it onto the other, and the learner may be forced to process both even though one is sufficient [-M]. This is distinct from the [coherence principle](coherence-principle-irrelevant-material-hurts-learning.md), where the harm comes from *irrelevant* rather than duplicated material — redundant material is relevant, just unnecessarily repeated. Both effects operate through the same underlying constraint that [cognitive overload degrades learning](cognitive-overload-degrades-learning.md) [-M].

The effect is strongly moderated by learner expertise [~S]. For novices, redundant duplication of essential information can impair learning; for more advanced learners, the same duplication may be harmless or even helpful, consistent with the [expertise reversal effect](../theories/expertise-reversal-effect.md) [~S]. Designers should therefore treat redundancy as a novice-focused constraint and fade redundant support as competence develops — the same fading logic that governs when [worked examples can become counterproductive for advanced learners](worked-examples-expertise-reversal.md).

Boundary conditions worth noting: redundancy in the strict CLT sense refers to *same-information* duplication. Complementary material that adds new information (e.g., a diagram with genuinely explanatory labels, or narration that elaborates rather than reads the text) is not redundant and does not fall under this claim. Similarly, signposting or structural cues that help learners navigate material may look like redundancy but serve a different function — see [clear structure improves learning](clear-structure-improves-learning.md) [+M].

Practical implications for multimedia design: avoid on-screen text that verbatim duplicates narration [-M]; prefer graphics with concise integrated labels over graphics plus redundant audio [-M]; and when accessibility requires captions, consider whether they duplicate or complement the audio track. Where duplication is unavoidable (e.g., regulatory or accessibility requirements), giving learners control over pacing may reduce the coordination cost, though this interaction is not yet well quantified [~W]. Consolidating information so it need not be duplicated at all — for example through [chunking](chunking-reduces-working-memory-load.md) — is a complementary mitigation [+M].

Open questions: the exact magnitude of the effect across domains and media, and how it interacts with learner control (e.g., self-paced versus system-paced multimedia), remain areas where this page needs primary evidence before specific design thresholds can be recommended.

## Related Claims

- [Coherence principle: irrelevant material hurts learning.](coherence-principle-irrelevant-material-hurts-learning.md) — adjacent CLT effect; harm from extraneous rather than duplicated material
- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — the working-memory mechanism through which redundancy exerts its cost
- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — one mitigation: consolidating information so it need not be duplicated
- [Worked examples can become redundant or counterproductive for advanced learners.](worked-examples-expertise-reversal.md) — expertise reversal applied to example-based support
- [Expertise reversal effect](../theories/expertise-reversal-effect.md) — the moderator that makes redundancy harmful for novices but not experts
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) — the parent theory predicting the effect