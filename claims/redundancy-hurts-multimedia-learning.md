---
type: claim
title: Redundancy Hurts Multimedia Learning
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: redundancy-hurts-multimedia-learning
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

# Redundancy Hurts Multimedia Learning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q3` peer-reviewed experiment · n=63 studies (44 in the narration+on-screen-text "scenario 4")

Presenting the same information simultaneously in multiple channels — most commonly, on-screen text that duplicates narrated speech — impairs multimedia learning compared with presenting the information once.

## Subclaims

`q3 i?` A literature review of 63 studies finds that adding written text which duplicates narration (verbal/"working-memory-channel" redundancy) most often impairs learning, though the direction reverses for some moderators (older learners, learner-paced delivery, non-identical/abridged text). [→ Trypke et al. 2023](#trypke-et-al-2023)

## Evidence

### Trypke et al. 2023

Trypke, M., Stebner, F., & Wirth, J. (2023). Two types of redundancy in multimedia learning: a literature review. *Frontiers in Psychology, 14*, Article 1148035. [doi:10.3389/fpsyg.2023.1148035](https://doi.org/10.3389/fpsyg.2023.1148035)

`q3 · systematic literature review (63 studies)` · `i? · no pooled effect size reported` · `n=63 studies (44 in the narration+on-screen-text "scenario 4")`

This review classifies redundancy effects across 63 multimedia-learning experiments into "content redundancy" (duplicated information, independent of channel) and "working-memory channel redundancy" (two sources competing for the same processing channel). For the case closest to the classic redundancy principle — narration duplicated by identical on-screen text — the authors report that among the 44 studies adding written text to narrated visualizations, several classic experiments (e.g., [Kalyuga et al. 1999](https://doi.org/10.1002/(SICI)1099-0720(199912)13:4%3C351::AID-ACP589%3E3.0.CO;2-6), Mayer et al. 2001, Yue et al. 2013) found that "the animation, narration, and identical written text group performed worse on retention and transfer tests," and note the finding "aligns with the findings of the meta-analysis on the verbal redundancy effect, which shows that narrations accompanied by identical written text impaired learning (e.g., Adesope and Nesbit, 2012)." The review also identifies moderators — degree of overlap (abridged/keyword text is less harmful than verbatim duplication), learner age, prior knowledge, and pacing — that shift or reverse the direction of the effect, which is why the overall pattern is reported as heterogeneous rather than as one pooled effect.

## Discussion

The redundancy effect is one of the core effects predicted by [Cognitive Load Theory](../theories/cognitive-load-theory.md). When learners read text and listen to narration that say the same thing, they must coordinate the two streams and reconcile them, consuming working-memory capacity that would otherwise go to schema construction. This interacts with the [modality effect](../claims/modality-principle-narration-beats-on-screen-text.md): narration plus graphics can outperform text plus graphics, but only when the narration does not duplicate on-screen text.

Key boundary conditions to document when evidence is added:

- **Learner expertise.** Redundant material can become beneficial rather than harmful for advanced learners, consistent with the [expertise reversal effect](../theories/expertise-reversal-effect.md) — experts may use redundant text as a low-effort verification aid.
- **Nature of the redundancy.** Harm is strongest for verbatim duplication of narration as on-screen text; a brief caption, heading, or label that *complements* rather than repeats narration is not redundancy in this sense and may support learning.
- **Access conditions.** Redundant on-screen text may help learners who cannot hear the narration (hearing impairment, noisy environments, non-native speakers), so accessibility needs can override the effect — a case where [cognitive load management](../principles/cognitive-load-management.md) trades off against other design goals.
- **Pacing.** Learner-controlled environments may soften the harm, since learners can pause or ignore one stream; the effect is expected to be strongest under system-paced, continuous presentation.

Both subclaims currently lack Evidence entries; the classic experimental and meta-analytic literature on the redundancy principle still needs to be added before this claim can be rated.

## Related Claims

- [Coherence principle: irrelevant material hurts learning.](coherence-principle-irrelevant-material-hurts-learning.md) — a sibling multimedia effect; both trace to avoiding extraneous processing
- [Modality principle: narration beats on-screen text.](modality-principle-narration-beats-on-screen-text.md) — defines the audio–visual split that redundancy disrupts
- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — the working-memory mechanism underlying the effect
- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — a complementary load-management strategy
- [Expertise reversal effect.](../theories/expertise-reversal-effect.md) — explains when redundancy stops hurting