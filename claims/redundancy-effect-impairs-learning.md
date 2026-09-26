---
type: claim
title: Redundancy Effect Impairs Learning
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: redundancy-effect-impairs-learning
aliases: [redundancy-harms-learning, redundancy-hurts-multimedia-learning, redundancy-principle-hurts-learning, redundancy-principle-on-screen-text-hurts-learning, redundant-on-screen-text-hurts-learning]
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

`q3 i?` A literature review of 63 studies finds that adding written text which duplicates the narration of a narrated visualization most often impairs learning, though the direction reverses for some moderators (older learners, learner-paced delivery, non-identical/abridged text). Adding written text to narration with no visualization is the opposite case: the review reports positive effects there. [→ Trypke et al. 2023](#trypke-et-al-2023)

## Evidence

### Trypke et al. 2023

Trypke, M., Stebner, F., & Wirth, J. (2023). Two types of redundancy in multimedia learning: a literature review. *Frontiers in Psychology, 14*, Article 1148035. [doi:10.3389/fpsyg.2023.1148035](https://doi.org/10.3389/fpsyg.2023.1148035)

`q3 · systematic literature review (63 studies)` · `i? · no pooled effect size reported` · `n=63 studies (44 in the narration+on-screen-text "scenario 4")`

This review classifies redundancy effects across 63 multimedia-learning experiments into "content redundancy" (duplicated information, independent of channel) and "working-memory channel redundancy" (two sources competing for the same processing channel). For the case closest to the classic redundancy principle — narration duplicated by identical on-screen text — the authors report that among the 44 studies adding written text to narrated visualizations, several classic experiments (e.g., [Kalyuga et al. 1999](https://doi.org/10.1002/(SICI)1099-0720(199912)13:4%3C351::AID-ACP589%3E3.0.CO;2-6), Mayer et al. 2001, Yue et al. 2013) found that "the animation, narration, and identical written text group performed worse on retention and transfer tests," and note the finding "aligns with the findings of the meta-analysis on the verbal redundancy effect, which shows that narrations accompanied by identical written text impaired learning (e.g., Adesope and Nesbit, 2012)." The review also identifies moderators — degree of overlap (abridged/keyword text is less harmful than verbatim duplication), learner age, prior knowledge, and pacing — that shift or reverse the direction of the effect, which is why the overall pattern is reported as heterogeneous rather than as one pooled effect. The abstract's summary is scenario by scenario: positive effects of content redundancy (depending on prior knowledge), negative effects of working-memory-channel redundancy between visualizations and written text, and positive effects of working-memory-channel redundancy between narration and written text, so the harm is specific to text competing with a visualization.

## Discussion

The redundancy effect is one of the classic effects predicted by [Cognitive Load Theory](../theories/cognitive-load-theory.md). The proposed mechanism is that when identical information is presented in two formats, working memory resources are consumed holding one representation while the learner maps it onto the other, and the learner may be forced to process both even though one is sufficient [-M]. This is distinct from the [coherence principle](coherence-principle-irrelevant-material-hurts-learning.md), where the harm comes from *irrelevant* rather than duplicated material — redundant material is relevant, just unnecessarily repeated. Both effects operate through the same underlying constraint that [cognitive overload degrades learning](cognitive-overload-degrades-learning.md) [-M].

The effect is strongly moderated by learner expertise [~S]. For novices, redundant duplication of essential information can impair learning; for more advanced learners, the same duplication may be harmless or even helpful, consistent with the [expertise reversal effect](../theories/expertise-reversal-effect.md) [~S]. Designers should therefore treat redundancy as a novice-focused constraint and fade redundant support as competence develops — the same fading logic that governs when [worked examples can become counterproductive for advanced learners](worked-examples-less-effective-with-expertise.md).

Boundary conditions worth noting: redundancy in the strict CLT sense refers to *same-information* duplication. Complementary material that adds new information (e.g., a diagram with genuinely explanatory labels, or narration that elaborates rather than reads the text) is not redundant and does not fall under this claim. Similarly, signposting or structural cues that help learners navigate material may look like redundancy but serve a different function — see [clear structure improves learning](clear-structure-improves-learning.md) [+M].

Practical implications for multimedia design: avoid on-screen text that verbatim duplicates narration [-M]; prefer graphics with concise integrated labels over graphics plus redundant audio [-M]; and when accessibility requires captions, consider whether they duplicate or complement the audio track. Where duplication is unavoidable (e.g., regulatory or accessibility requirements), giving learners control over pacing may reduce the coordination cost, though this interaction is not yet well quantified [~W]. Consolidating information so it need not be duplicated at all — for example through [chunking](chunking-reduces-working-memory-load.md) — is a complementary mitigation [+M].

Open questions: the exact magnitude of the effect across domains and media, and how it interacts with learner control (e.g., self-paced versus system-paced multimedia), remain areas where this page needs primary evidence before specific design thresholds can be recommended.

*Merged from “Redundancy Harms Learning” (redundancy-harms-learning):* **Mechanism.** Under [cognitive load theory](../theories/cognitive-load-theory.md), redundancy is one of the classic sources of extraneous load: when identical content is duplicated across channels, learners must reconcile the copies, consuming working-memory resources that could otherwise go to schema construction [~M]. The most-studied case is simultaneous narration of identical on-screen text, which forces visual attention and auditory processing onto the same words rather than letting visuals carry the diagram and narration carry the explanation. This is a core multimedia-design principle: duplication across channels degrades learning relative to narration-plus-graphics [~M].

**Boundary conditions.** The redundancy effect is not universal. It is primarily a *novice* phenomenon; as expertise grows, redundant formats can become helpful rather than harmful — the same expertise-reversal pattern documented for [worked examples](worked-examples-less-effective-with-expertise.md) and formalized in the [expertise reversal effect](../theories/expertise-reversal-effect.md) [~M]. Redundant on-screen text may also help when learners cannot process audio (hearing impairment, noisy environments, non-native listeners), when text serves as a navigational or reference aid rather than a duplicate of narration, or when pacing is fully learner-controlled [~W]. The effect applies to *identical* duplication; complementary information across channels (e.g., narration plus a non-redundant diagram) is beneficial, not harmful — see the [coherence principle](coherence-principle-irrelevant-material-hurts-learning.md) for the related harm from irrelevant material.

**Design implication.** Prefer a single well-chosen presentation of each idea. When using narration with visuals, keep on-screen text minimal and non-duplicative rather than a verbatim transcript. Where accessibility or environment demands captions or transcripts, treat them as an accommodation (see [Accommodations](../elements/accommodations.md)) rather than a default for all learners. This pairs naturally with [cognitive load management](../principles/cognitive-load-management.md) and [chunking](chunking-reduces-working-memory-load.md) as part of a broader extraneous-load audit of instructional materials.

**Open questions.** The one review recorded above reports no pooled effect size, and finds the effect moderated by text overlap, learner age and pacing. The interaction between redundancy and learner-controlled pacing, and the threshold of expertise at which redundancy flips from harmful to helpful, remain under-specified.

*Merged from “Redundancy Hurts Multimedia Learning” (redundancy-hurts-multimedia-learning):* The redundancy effect is one of the core effects predicted by [Cognitive Load Theory](../theories/cognitive-load-theory.md). When learners read text and listen to narration that say the same thing, they must coordinate the two streams and reconcile them, consuming working-memory capacity that would otherwise go to schema construction. This interacts with the [modality effect](modality-effect-narration-over-text.md): narration plus graphics can outperform text plus graphics, but only when the narration does not duplicate on-screen text.

Key boundary conditions to document when evidence is added:

- **Learner expertise.** Redundant material can become beneficial rather than harmful for advanced learners, consistent with the [expertise reversal effect](../theories/expertise-reversal-effect.md) — experts may use redundant text as a low-effort verification aid.
- **Nature of the redundancy.** Harm is strongest for verbatim duplication of narration as on-screen text; a brief caption, heading, or label that *complements* rather than repeats narration is not redundancy in this sense and may support learning.
- **Access conditions.** Redundant on-screen text may help learners who cannot hear the narration (hearing impairment, noisy environments, non-native speakers), so accessibility needs can override the effect — a case where [cognitive load management](../principles/cognitive-load-management.md) trades off against other design goals.
- **Pacing.** Learner-controlled environments may soften the harm, since learners can pause or ignore one stream; the effect is expected to be strongest under system-paced, continuous presentation.

Both subclaims currently lack Evidence entries; the classic experimental and meta-analytic literature on the redundancy principle still needs to be added before this claim can be rated.

*Merged from “Redundancy Principle Hurts Learning” (redundancy-principle-hurts-learning):* **Mechanism.** Within [Cognitive Load Theory](../theories/cognitive-load-theory.md), redundancy is one of the classic sources of extraneous load: when learners must cross-reference two channels presenting identical content, working memory resources are spent on coordination rather than schema construction. This connects to the broader claim that [cognitive overload degrades learning](cognitive-overload-degrades-learning.md) and that [irrelevant or incoherent material hurts learning](coherence-principle-irrelevant-material-hurts-learning.md). The effect is distinct from the modality principle: narration plus graphics is generally *better* than text plus graphics, but adding verbatim on-screen text to narration pushes learners back into redundant processing.

**Boundary conditions.** The redundancy effect is not universal. Redundant material is less harmful — and sometimes helpful — when learners can control pacing (allowing them to ignore one channel), when the redundant format is not literally identical (e.g., a concise label versus a full restatement), or when learners are novices who might otherwise misinterpret sparse material. As expertise grows, the effect interacts with the expertise reversal pattern described in [expertise reversal effect](../theories/expertise-reversal-effect.md): supports that help novices become redundant for advanced learners. Designers should therefore ask whether each channel adds *new* information or merely repeats existing information, and remove the repetition when it does not.

**Design implications.** The most common practical instance is narrated animation or video with on-screen text that verbatim duplicates the narration; the redundancy principle recommends narration plus graphics without the duplicated text, reserving on-screen text for cases where audio is unavailable, the content is technical terminology, or learners are non-native listeners. Concise labels, captions that add information, and signals that direct attention are not redundancy in this sense — they add or restructure information rather than repeating it. This places redundancy alongside [coherence](coherence-principle-irrelevant-material-hurts-learning.md) and [chunking](chunking-reduces-working-memory-load.md) as tools for [cognitive load management](cognitive-load-management.md) rather than a blanket prohibition on multiple representations: dual coding of *complementary* verbal and visual information can still help, provided the two channels are not redundant.

**Open questions.** The one review recorded above reports no pooled effect size, and the meta-analysis it cites (Adesope & Nesbit 2012) could not be read here, so the size of the effect is not yet established on this page. Key open questions include how effect sizes vary across media (narration vs. text), age groups, and domains, and how much pacing control is needed to neutralize the effect.

*Merged from “Redundancy Principle On Screen Text Hurts Learning” (redundancy-principle-on-screen-text-hurts-learning):* **Mechanism.** The redundancy effect is explained within [Cognitive Load Theory](../theories/cognitive-load-theory.md): when identical verbal information is presented as both narration and on-screen text, learners must coordinate two channels presenting the same content, and written text competes with visual material (diagrams, animations) for the limited visual channel. Narration alone leaves the visual channel free for the graphics. This is closely related to the [Coherence Principle — irrelevant material hurts learning](coherence-principle-irrelevant-material-hurts-learning.md) and to [Cognitive overload degrades learning](cognitive-overload-degrades-learning.md).

**Boundary conditions.** The effect is generally strongest when graphics are complex or presented at a fast pace, and when text is verbatim rather than supplementary. Verbatim on-screen text is the harmful case; *concise* text that adds information not in the narration is not redundancy and may help. The effect also weakens or reverses when learners control pacing (allowing them to read then listen), when there is no pictorial information to compete for visual attention, when learners are hearing-impaired, when the material is in the learner's second language, or when only brief key phrases (labels, headings) are shown rather than full sentences.

**Constraints on application.** Designers should not treat "never show text" as a rule. Captioning is required for accessibility and benefits second-language learners, so the redundancy cost must be weighed against these needs [~M]. Redundant on-screen text is most harmful in system-paced, graphics-heavy lessons; in self-paced e-learning, learners may simply ignore the text, and the measured harm shrinks or disappears [~W]. Showing only brief labels or key phrases alongside narration avoids the effect and can support reference and note-taking [~M].

**Open questions.** Most evidence comes from short multimedia lessons in laboratory or controlled settings; the durability of the effect in self-paced, real-world e-learning — where learners can simply ignore redundant text — is less well established. Primary studies still need to be added to the Evidence section before this claim can be rated.

*Merged from “Redundant On Screen Text Hurts Learning” (redundant-on-screen-text-hurts-learning):* **Mechanism.** The redundancy effect is usually explained within [Cognitive Load Theory](../theories/cognitive-load-theory.md): visual and verbal channels have limited capacity, and when identical text duplicates narration, learners must visually scan the text while listening, splitting attention between two presentations of the same content rather than integrating words with the picture. This connects to the broader claim that [cognitive overload degrades learning](cognitive-overload-degrades-learning.md) and that [irrelevant or extraneous material hurts learning](coherence-principle-irrelevant-material-hurts-learning.md). Note the contrast with [dual coding theory](../theories/dual-coding-theory.md): dual coding predicts benefits when visual and verbal information are *complementary* (e.g., a diagram plus narration), whereas redundancy involves *identical* verbal information in two channels, which adds processing without adding information.

**Boundary conditions.** The effect is expected to be strongest when text and narration are presented simultaneously and verbatim, when the material is fast-paced, and when learners are novices. Redundant text may be less harmful — or even helpful — when learners can control pacing, when the text is not verbatim (e.g., labels or keywords on a diagram), when narration is unavailable or hard to hear, or for learners who benefit from reading support (e.g., second-language learners or those with hearing difficulties). These moderators are plausible from theory but need empirical support on this page.

**Design implications.** Where narration is used, avoid displaying the full transcript on screen at the same time; if text is needed for accessibility, consider making it available on demand rather than simultaneously. Reserve on-screen text for content that is *not* spoken — labels, keywords, and captions on diagrams — so that the visual channel adds information rather than duplicating it. This pairs naturally with [chunking](chunking-reduces-working-memory-load.md) and other [cognitive load management](../principles/cognitive-load-management.md) strategies.

**Open questions.** Studies still need to be added to establish the effect size, the role of pacing and learner control, and whether short keyword-level redundancy differs from full-sentence duplication.

## Related Claims

- [Coherence principle: irrelevant material hurts learning.](coherence-principle-irrelevant-material-hurts-learning.md) — adjacent CLT effect; harm from extraneous rather than duplicated material
- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — the working-memory mechanism through which redundancy exerts its cost
- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — one mitigation: consolidating information so it need not be duplicated
- [Worked examples can become redundant or counterproductive for advanced learners.](worked-examples-less-effective-with-expertise.md) — expertise reversal applied to example-based support
- [Expertise reversal effect](../theories/expertise-reversal-effect.md) — the moderator that makes redundancy harmful for novices but not experts
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) — the parent theory predicting the effect
- [Cognitive load reduction improves learning.](cognitive-load-reduction-improves-learning.md) — the general principle this claim instantiates
- [Clear structure improves learning.](clear-structure-improves-learning.md) — a positive-design counterpart: one well-organized presentation instead of duplicated ones
- [Modality principle: narration beats on-screen text.](modality-effect-narration-over-text.md) — defines the audio–visual split that redundancy disrupts
- [Dual coding theory.](../theories/dual-coding-theory.md) — explains why complementary (not redundant) visual–verbal pairing helps learning
- [Instructional support suited to novices can have negative effects for more expert learners (expertise-reversal effect), so instructional design should be tailored to learner experience](expertise-reversal-effect-redundant-support-harms-experts.md) — related
- [Expertise Reversal Guidance Hurts Experts](expertise-reversal-guidance-hurts-experts.md) — related
- [Laptop note-taking tends toward verbatim transcription and shallower learning than longhand note-taking](laptop-notes-verbatim-shallower.md) — related
- [Multimedia Principle Improves Learning](multimedia-principle-improves-learning.md) — related
- [Redundant on-screen text duplicates of narration or graphics impair learning](redundancy-principle.md) — possibly the same claim (merge candidate)
- [Redundancy Hurts Learning](redundancy-hurts-learning.md) — a narrower finding that bears on this claim
- [Redundant text in the diagram did not affect posttest accuracy or difficulty ratings](redundant-text-no-effect-posterior-probability-lesson.md) — related
- [Interesting but irrelevant details impair learning](seductive-details-effect.md) — related
- [Despite ignorance of CLT, surveyed teachers report using some of its principles when designing instructions](teachers-use-clt-principles-despite-ignorance.md) — related
