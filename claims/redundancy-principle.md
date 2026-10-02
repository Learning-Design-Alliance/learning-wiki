---
type: claim
title: Redundant on-screen text impairs learning when it competes with a visualization, though written text duplicating narration alone can help
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: redundancy-principle
evidence_strength: moderate
sources:
  - id: trypke-et-al-2023
    resource: "https://doi.org/10.3389/fpsyg.2023.1148035"
    title: "Trypke, M., Stebner, F., & Wirth, J. (2023). Two types of redundancy in multimedia learning: a literature review. *Frontiers in Psychology, 14*, Article 1148035. [doi:10.3389/fpsyg.2023.1148035](https://doi.org/10.3389/fpsyg.2023.1148035)"
    author: "Trypke, M., Stebner, F., & Wirth, J."
    q: 3
    i: "?"
    n: "63 studies (44 in the narration+on-screen-text \"scenario 4\")"
    kind: review
    rigour: "?"
---

# Redundant on-screen text impairs learning when it competes with a visualization, though written text duplicating narration alone can help

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r?` · `q3` · n=63 studies (44 in the narration+on-screen-text "scenario 4")

Adding on-screen text that duplicates narration to a narrated animation or diagram, or adding redundant text to an already comprehensible graphic, is thought to overload working memory and has typically lowered learning outcomes relative to narration-plus-graphics alone. Without a visualization, written text added to narration is the opposite case: the review below reports positive effects there.

## Subclaims

`q3 i?` A literature review of 63 studies finds that adding written text which duplicates the narration of a narrated visualization most often impairs learning, though the direction reverses for some moderators (older learners, learner-paced delivery, non-identical/abridged text). Adding written text to narration with no visualization is the opposite case: the review reports positive effects there. [→ Trypke et al. 2023](#trypke-et-al-2023)

`q3 i?` The review classifies the harm as working-memory-channel redundancy between visualizations and written text, and reports positive effects of content redundancy that depend on learners' prior knowledge. [→ Trypke et al. 2023](#trypke-et-al-2023)

## Evidence

### Trypke et al. 2023

Trypke, M., Stebner, F., & Wirth, J. (2023). Two types of redundancy in multimedia learning: a literature review. *Frontiers in Psychology, 14*, Article 1148035. [doi:10.3389/fpsyg.2023.1148035](https://doi.org/10.3389/fpsyg.2023.1148035)

`q3 · systematic literature review (63 studies)` · `i? · no pooled effect size reported` · `n=63 studies (44 in the narration+on-screen-text "scenario 4")` · `review · r?`

This review classifies redundancy effects across 63 multimedia-learning experiments into "content redundancy" (duplicated information, independent of channel) and "working-memory channel redundancy" (two sources competing for the same processing channel). For the case closest to the classic redundancy principle — narration duplicated by identical on-screen text — the authors report that among the 44 studies adding written text to narrated visualizations, several classic experiments (e.g., [Kalyuga et al. 1999](https://doi.org/10.1002/(SICI)1099-0720(199912)13:4%3C351::AID-ACP589%3E3.0.CO;2-6), Mayer et al. 2001, Yue et al. 2013) found that "the animation, narration, and identical written text group performed worse on retention and transfer tests," and note the finding "aligns with the findings of the meta-analysis on the verbal redundancy effect, which shows that narrations accompanied by identical written text impaired learning (e.g., Adesope and Nesbit, 2012)." The review also identifies moderators — degree of overlap (abridged/keyword text is less harmful than verbatim duplication), learner age, prior knowledge, and pacing — that shift or reverse the direction of the effect, which is why the overall pattern is reported as heterogeneous rather than as one pooled effect. The abstract's summary is scenario by scenario: positive effects of content redundancy (depending on prior knowledge), negative effects of working-memory-channel redundancy between visualizations and written text, and positive effects of working-memory-channel redundancy between narration and written text, so the harm is specific to text competing with a visualization.

## Discussion

**Mechanism.** Within [cognitive load theory](../theories/cognitive-load-theory.md), redundant on-screen text forces learners to split visual attention between the graphic and the text while also trying to reconcile it with the narration — a classic split-attention and redundancy burden [-S]. Learners cannot read and listen to identical text in parallel; reading speed outpaces speech, so the text competes for the same visual channel as the graphic. This parallels the [coherence principle](coherence-principle-irrelevant-material-hurts-learning.md): material that adds no new information but adds processing cost hurts learning [-M].

**Boundary conditions.** The redundancy effect is strongest for novices and for fast-paced, learner-paced-unfriendly multimedia [-M]. It weakens or reverses when: (a) narration is absent (text alone with a graphic is fine — the problem is *duplication*, not text per se) [~S]; (b) learners are fluent readers with high prior knowledge, who can skim text and ignore narration (an instance of the expertise reversal pattern — see [the expertise reversal effect](../theories/expertise-reversal-effect.md)) [~M]; (c) text is short labels or signs rather than full sentences [~M]; or (d) the learner controls pacing and can integrate the channels deliberately [~W].

**Design implication.** Prefer narration plus a clean graphic; put essential words in the audio channel, and reserve on-screen text for terms, definitions, or content that must be re-read. This complements [cognitive load reduction](../principles/cognitive-load-reduction.md) and [cognitive load management](../principles/cognitive-load-management.md) guidance, and pairs with [chunking](chunking-reduces-working-memory-load.md) to keep each channel's load within working-memory limits.

**Open questions.** Most evidence comes from short, lab-based multimedia lessons; effects on longer, self-paced online courses — where learners routinely expect captions — are less settled [~W], and accessibility needs (deaf and hard-of-hearing learners) can make redundant text a necessary accommodation rather than a redundancy (see [accommodations](../elements/accommodations.md)). Designers of captioned video should treat captions as an accessibility layer, not assume they are neutral or beneficial for all learners.

## Related Claims

- [Irrelevant material hurts learning (coherence principle).](coherence-principle-irrelevant-material-hurts-learning.md) — same working-memory logic: extra material that adds no value imposes cost
- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — the overload mechanism redundancy exploits
- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — complementary strategy for managing limited working memory
- [Worked examples can become redundant or counterproductive for advanced learners.](worked-examples-less-effective-with-expertise.md) — expertise reversal: redundancy effects depend on learner expertise
- [Expertise Reversal Guidance Hurts Experts](expertise-reversal-guidance-hurts-experts.md) — related
- [Presenting words as spoken narration rather than on-screen text alongside graphics improves learning](modality-effect-narration-over-text.md) — related
- [Redundancy Effect Impairs Learning](redundancy-effect-impairs-learning.md) — possibly the same claim (merge candidate)
- [Redundancy Hurts Learning](redundancy-hurts-learning.md) — a narrower finding that bears on this claim
- [Bimodal captioned input improved L2 listening skills, generalizing to unfamiliar sentences and speakers (attributed to Charles & Trenkic, 2015)](bimodal-captioned-input-improves-segmentation.md) — related
- [Common language teaching methods such as oral drills, memorization, and fast-paced competitive activities disadvantage older learners](rote-drills-disadvantage-older-learners.md) — related
- [The redundancy effect does not hold for middle school students: adding written text to spoken narration did not significantly change achievement with either abstract or concrete animation](redundancy-effect-not-significant-middle-school.md) — a narrower finding that bears on this claim
- [Temporal contiguity (concurrent narration and animation) is associated with facilitated understanding and lower perceived cognitive load](temporal-contiguity-lower-cognitive-load.md) — related