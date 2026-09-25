---
type: claim
title: Redundancy Principle On Screen Text Hurts Learning
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: redundancy-principle-on-screen-text-hurts-learning
evidence_strength:
sources:
  - id: trypke-et-al-2023
    resource: "https://doi.org/10.3389/fpsyg.2023.1148035"
    title: "Trypke, M., Stebner, F., & Wirth, J. (2023). Two types of redundancy in multimedia learning: a literature review. *Frontiers in Psychology, 14*, Article 1148035. [doi:10.3389/fpsyg.2023.1148035](https://doi.org/10.3389/fpsyg.2023.1148035)"
    author: "Trypke, M., Stebner, F., & Wirth, J."
    q: 3
    i: "?"
    n: "63 studies (44 in the narration+on-screen-text \"scenario 4\")"
---

# Redundancy Principle On Screen Text Hurts Learning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q3` peer-reviewed experiment · n=63 studies (44 in the narration+on-screen-text "scenario 4")

Presenting the same information simultaneously as narration and as on-screen text tends to impair learning relative to narration alone, because learners split visual attention between reading and watching.

## Subclaims

`q3 i?` A literature review of 63 studies finds that adding written text which duplicates narration (verbal/"working-memory-channel" redundancy) most often impairs learning, though the direction reverses for some moderators (older learners, learner-paced delivery, non-identical/abridged text). [→ Trypke et al. 2023](#trypke-et-al-2023)

## Evidence

### Trypke et al. 2023

Trypke, M., Stebner, F., & Wirth, J. (2023). Two types of redundancy in multimedia learning: a literature review. *Frontiers in Psychology, 14*, Article 1148035. [doi:10.3389/fpsyg.2023.1148035](https://doi.org/10.3389/fpsyg.2023.1148035)

`q3 · systematic literature review (63 studies)` · `i? · no pooled effect size reported` · `n=63 studies (44 in the narration+on-screen-text "scenario 4")`

This review classifies redundancy effects across 63 multimedia-learning experiments into "content redundancy" (duplicated information, independent of channel) and "working-memory channel redundancy" (two sources competing for the same processing channel). For the case closest to the classic redundancy principle — narration duplicated by identical on-screen text — the authors report that among the 44 studies adding written text to narrated visualizations, several classic experiments (e.g., [Kalyuga et al. 1999](https://doi.org/10.1002/(SICI)1099-0720(199912)13:4%3C351::AID-ACP589%3E3.0.CO;2-6), Mayer et al. 2001, Yue et al. 2013) found that "the animation, narration, and identical written text group performed worse on retention and transfer tests," and note the finding "aligns with the findings of the meta-analysis on the verbal redundancy effect, which shows that narrations accompanied by identical written text impaired learning (e.g., Adesope and Nesbit, 2012)." The review also identifies moderators — degree of overlap (abridged/keyword text is less harmful than verbatim duplication), learner age, prior knowledge, and pacing — that shift or reverse the direction of the effect, which is why the overall pattern is reported as heterogeneous rather than as one pooled effect.

## Discussion

**Mechanism.** The redundancy effect is explained within [Cognitive Load Theory](../theories/cognitive-load-theory.md): when identical verbal information is presented as both narration and on-screen text, learners must coordinate two channels presenting the same content, and written text competes with visual material (diagrams, animations) for the limited visual channel. Narration alone leaves the visual channel free for the graphics. This is closely related to the [Coherence Principle — irrelevant material hurts learning](coherence-principle-irrelevant-material-hurts-learning.md) and to [Cognitive overload degrades learning](cognitive-overload-degrades-learning.md).

**Boundary conditions.** The effect is generally strongest when graphics are complex or presented at a fast pace, and when text is verbatim rather than supplementary. Verbatim on-screen text is the harmful case; *concise* text that adds information not in the narration is not redundancy and may help. The effect also weakens or reverses when learners control pacing (allowing them to read then listen), when there is no pictorial information to compete for visual attention, when learners are hearing-impaired, when the material is in the learner's second language, or when only brief key phrases (labels, headings) are shown rather than full sentences.

**Constraints on application.** Designers should not treat "never show text" as a rule. Captioning is required for accessibility and benefits second-language learners, so the redundancy cost must be weighed against these needs [~M]. Redundant on-screen text is most harmful in system-paced, graphics-heavy lessons; in self-paced e-learning, learners may simply ignore the text, and the measured harm shrinks or disappears [~W]. Showing only brief labels or key phrases alongside narration avoids the effect and can support reference and note-taking [~M].

**Open questions.** Most evidence comes from short multimedia lessons in laboratory or controlled settings; the durability of the effect in self-paced, real-world e-learning — where learners can simply ignore redundant text — is less well established. Primary studies still need to be added to the Evidence section before this claim can be rated.

## Related Claims

- [Coherence Principle — irrelevant material hurts learning](coherence-principle-irrelevant-material-hurts-learning.md) — sibling multimedia principle: excluding extraneous material reduces load
- [Cognitive overload degrades learning](cognitive-overload-degrades-learning.md) — the working-memory mechanism underlying the redundancy effect
- [Chunking reduces working-memory load](chunking-reduces-working-memory-load.md) — complementary load-management strategy
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) — the theoretical framework in which the redundancy effect is defined