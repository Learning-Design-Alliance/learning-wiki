---
type: claim
title: Redundancy Principle Hurts Learning
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: redundancy-principle-hurts-learning
evidence_strength: low
sources:
  - id: trypke-et-al-2023
    resource: "https://doi.org/10.3389/fpsyg.2023.1148035"
    title: "Trypke, M., Stebner, F., & Wirth, J. (2023). Two types of redundancy in multimedia learning: a literature review. *Frontiers in Psychology, 14*, Article 1148035. [doi:10.3389/fpsyg.2023.1148035](https://doi.org/10.3389/fpsyg.2023.1148035)"
    author: "Trypke, M., Stebner, F., & Wirth, J."
    q: 3
    i: "?"
    n: "63 studies (44 in the narration+on-screen-text \"scenario 4\")"
---

# Redundancy Principle Hurts Learning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q3` peer-reviewed experiment · n=63 studies (44 in the narration+on-screen-text "scenario 4")

Presenting the same information in multiple simultaneous formats (e.g., on-screen text duplicating narration, or graphics labeled with text that repeats what is already shown) imposes extraneous cognitive load and can impair learning compared with a single well-chosen format.

## Subclaims

`q3 i?` A literature review of 63 studies finds that adding written text which duplicates narration (verbal/"working-memory-channel" redundancy) most often impairs learning, though the direction reverses for some moderators (older learners, learner-paced delivery, non-identical/abridged text). [→ Trypke et al. 2023](#trypke-et-al-2023)

## Evidence

### Trypke et al. 2023

Trypke, M., Stebner, F., & Wirth, J. (2023). Two types of redundancy in multimedia learning: a literature review. *Frontiers in Psychology, 14*, Article 1148035. [doi:10.3389/fpsyg.2023.1148035](https://doi.org/10.3389/fpsyg.2023.1148035)

`q3 · systematic literature review (63 studies)` · `i? · no pooled effect size reported` · `n=63 studies (44 in the narration+on-screen-text "scenario 4")`

This review classifies redundancy effects across 63 multimedia-learning experiments into "content redundancy" (duplicated information, independent of channel) and "working-memory channel redundancy" (two sources competing for the same processing channel). For the case closest to the classic redundancy principle — narration duplicated by identical on-screen text — the authors report that among the 44 studies adding written text to narrated visualizations, several classic experiments (e.g., [Kalyuga et al. 1999](https://doi.org/10.1002/(SICI)1099-0720(199912)13:4%3C351::AID-ACP589%3E3.0.CO;2-6), Mayer et al. 2001, Yue et al. 2013) found that "the animation, narration, and identical written text group performed worse on retention and transfer tests," and note the finding "aligns with the findings of the meta-analysis on the verbal redundancy effect, which shows that narrations accompanied by identical written text impaired learning (e.g., Adesope and Nesbit, 2012)." The review also identifies moderators — degree of overlap (abridged/keyword text is less harmful than verbatim duplication), learner age, prior knowledge, and pacing — that shift or reverse the direction of the effect, which is why the overall pattern is reported as heterogeneous rather than as one pooled effect.

## Discussion

**Mechanism.** Within [Cognitive Load Theory](../theories/cognitive-load-theory.md), redundancy is one of the classic sources of extraneous load: when learners must cross-reference two channels presenting identical content, working memory resources are spent on coordination rather than schema construction. This connects to the broader claim that [cognitive overload degrades learning](cognitive-overload-degrades-learning.md) and that [irrelevant or incoherent material hurts learning](coherence-principle-irrelevant-material-hurts-learning.md). The effect is distinct from the modality principle: narration plus graphics is generally *better* than text plus graphics, but adding verbatim on-screen text to narration pushes learners back into redundant processing.

**Boundary conditions.** The redundancy effect is not universal. Redundant material is less harmful — and sometimes helpful — when learners can control pacing (allowing them to ignore one channel), when the redundant format is not literally identical (e.g., a concise label versus a full restatement), or when learners are novices who might otherwise misinterpret sparse material. As expertise grows, the effect interacts with the expertise reversal pattern described in [expertise reversal effect](../theories/expertise-reversal-effect.md): supports that help novices become redundant for advanced learners. Designers should therefore ask whether each channel adds *new* information or merely repeats existing information, and remove the repetition when it does not.

**Design implications.** The most common practical instance is narrated animation or video with on-screen text that verbatim duplicates the narration; the redundancy principle recommends narration plus graphics without the duplicated text, reserving on-screen text for cases where audio is unavailable, the content is technical terminology, or learners are non-native listeners. Concise labels, captions that add information, and signals that direct attention are not redundancy in this sense — they add or restructure information rather than repeating it. This places redundancy alongside [coherence](coherence-principle-irrelevant-material-hurts-learning.md) and [chunking](chunking-reduces-working-memory-load.md) as tools for [cognitive load management](cognitive-load-management.md) rather than a blanket prohibition on multiple representations: dual coding of *complementary* verbal and visual information can still help, provided the two channels are not redundant.

**Open questions.** The one review recorded above reports no pooled effect size, and the meta-analysis it cites (Adesope & Nesbit 2012) could not be read here, so the size of the effect is not yet established on this page. Key open questions include how effect sizes vary across media (narration vs. text), age groups, and domains, and how much pacing control is needed to neutralize the effect.

## Related Claims

- [Coherence principle: irrelevant material hurts learning](coherence-principle-irrelevant-material-hurts-learning.md) — sibling multimedia principle; both concern removing extraneous processing
- [Cognitive overload degrades learning](cognitive-overload-degrades-learning.md) — the working-memory mechanism underlying the redundancy effect
- [Chunking reduces working memory load](chunking-reduces-working-memory-load.md) — complementary strategy for managing the same capacity limits
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) — the theoretical framework in which redundancy is defined as extraneous load
- [Expertise reversal effect](../theories/expertise-reversal-effect.md) — the same supports that aid novices can become redundant for advanced learners
- [Cognitive load reduction improves learning](cognitive-load-reduction-improves-learning.md) — the general claim that reducing extraneous load benefits outcomes, of which redundancy removal is one instance