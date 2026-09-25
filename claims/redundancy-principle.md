---
type: claim
title: Redundant on-screen text duplicates of narration or graphics impair learning
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
---

# Redundant on-screen text duplicates of narration or graphics impair learning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q3` peer-reviewed experiment · n=63 studies (44 in the narration+on-screen-text "scenario 4")

Presenting the same information simultaneously as narration and verbatim on-screen text, or adding redundant text to an already comprehensible graphic, overloads working memory and typically lowers learning outcomes relative to narration-plus-graphics alone.

## Subclaims

`q3 i?` A literature review of 63 studies finds that adding written text which duplicates narration (verbal/"working-memory-channel" redundancy) most often impairs learning, though the direction reverses for some moderators (older learners, learner-paced delivery, non-identical/abridged text). [→ Trypke et al. 2023](#trypke-et-al-2023)

## Evidence

### Trypke et al. 2023

Trypke, M., Stebner, F., & Wirth, J. (2023). Two types of redundancy in multimedia learning: a literature review. *Frontiers in Psychology, 14*, Article 1148035. [doi:10.3389/fpsyg.2023.1148035](https://doi.org/10.3389/fpsyg.2023.1148035)

`q3 · systematic literature review (63 studies)` · `i? · no pooled effect size reported` · `n=63 studies (44 in the narration+on-screen-text "scenario 4")`

This review classifies redundancy effects across 63 multimedia-learning experiments into "content redundancy" (duplicated information, independent of channel) and "working-memory channel redundancy" (two sources competing for the same processing channel). For the case closest to the classic redundancy principle — narration duplicated by identical on-screen text — the authors report that among the 44 studies adding written text to narrated visualizations, several classic experiments (e.g., [Kalyuga et al. 1999](https://doi.org/10.1002/(SICI)1099-0720(199912)13:4%3C351::AID-ACP589%3E3.0.CO;2-6), Mayer et al. 2001, Yue et al. 2013) found that "the animation, narration, and identical written text group performed worse on retention and transfer tests," and note the finding "aligns with the findings of the meta-analysis on the verbal redundancy effect, which shows that narrations accompanied by identical written text impaired learning (e.g., Adesope and Nesbit, 2012)." The review also identifies moderators — degree of overlap (abridged/keyword text is less harmful than verbatim duplication), learner age, prior knowledge, and pacing — that shift or reverse the direction of the effect, which is why the overall pattern is reported as heterogeneous rather than as one pooled effect.

## Discussion

**Mechanism.** Within [cognitive load theory](../theories/cognitive-load-theory.md), redundant on-screen text forces learners to split visual attention between the graphic and the text while also trying to reconcile it with the narration — a classic split-attention and redundancy burden [-S]. Learners cannot read and listen to identical text in parallel; reading speed outpaces speech, so the text competes for the same visual channel as the graphic. This parallels the [coherence principle](coherence-principle-irrelevant-material-hurts-learning.md): material that adds no new information but adds processing cost hurts learning [-M].

**Boundary conditions.** The redundancy effect is strongest for novices and for fast-paced, learner-paced-unfriendly multimedia [-M]. It weakens or reverses when: (a) narration is absent (text alone with a graphic is fine — the problem is *duplication*, not text per se) [~S]; (b) learners are fluent readers with high prior knowledge, who can skim text and ignore narration (an instance of the expertise reversal pattern — see [the expertise reversal effect](../theories/expertise-reversal-effect.md)) [~M]; (c) text is short labels or signs rather than full sentences [~M]; or (d) the learner controls pacing and can integrate the channels deliberately [~W].

**Design implication.** Prefer narration plus a clean graphic; put essential words in the audio channel, and reserve on-screen text for terms, definitions, or content that must be re-read. This complements [cognitive load reduction](../principles/cognitive-load-reduction.md) and [cognitive load management](../principles/cognitive-load-management.md) guidance, and pairs with [chunking](chunking-reduces-working-memory-load.md) to keep each channel's load within working-memory limits.

**Open questions.** Most evidence comes from short, lab-based multimedia lessons; effects on longer, self-paced online courses — where learners routinely expect captions — are less settled [~W], and accessibility needs (deaf and hard-of-hearing learners) can make redundant text a necessary accommodation rather than a redundancy (see [accommodations](../elements/accommodations.md)). Designers of captioned video should treat captions as an accessibility layer, not assume they are neutral or beneficial for all learners.

## Related Claims

- [Irrelevant material hurts learning (coherence principle).](coherence-principle-irrelevant-material-hurts-learning.md) — same working-memory logic: extra material that adds no value imposes cost
- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — the overload mechanism redundancy exploits
- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — complementary strategy for managing limited working memory
- [Worked examples can become redundant or counterproductive for advanced learners.](worked-examples-expertise-reversal.md) — expertise reversal: redundancy effects depend on learner expertise