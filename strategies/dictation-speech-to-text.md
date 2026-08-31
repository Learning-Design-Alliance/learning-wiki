---
type: strategy
title: Dictation/Speech-to-text
description: Dictation, also known as speech-to-text or voice recognition, involves using technology to convert spoken words into written text.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Dictation/Speech-to-text

> **Strategy** · [All strategies](index.md)

## Description
Dictation uses speech recognition technology to convert spoken language into written text, allowing learners to compose by voice rather than by keyboard or handwriting. The learner speaks into a microphone; the software transcribes the words into a word processor or other text field, where they can be reviewed and edited. Modern implementations range from built-in device tools (Apple Dictation, Google Voice Typing, Microsoft Dictate) to trained systems such as Dragon (Nuance).

## Design Implications

Speech-to-text removes the transcription bottleneck — handwriting mechanics, spelling, and motor execution — so working memory and attention can be allocated to idea generation, organization, and voice [Reducing extraneous transcription demands frees cognitive resources for composing.](../claims/chunking-reduces-working-memory-load.md) [+M]. This is essentially a [Cognitive Load Management](../principles/cognitive-load-management.md) move applied to writing: the technology externalizes the lowest-value component of the composition task. Its effectiveness depends on the learner's oral language proficiency and on explicit instruction in dictation conventions (punctuation commands, speaking in phrases, self-monitoring the transcript) — simply granting access without training yields poor results [~M].

### Context
#### Requirements
- A device with a microphone and reliable speech recognition software (e.g., Dragon, Google Voice Typing, Microsoft Dictate)
- A reasonably quiet environment; accuracy degrades sharply with background noise
- Explicit training in dictation skills: pacing, enunciation, verbal punctuation commands, and editing the transcript
- A workflow for error correction, since recognition errors must be caught before they become "final" text

#### Constraints
- Recognition accuracy drops with background noise, atypical pronunciation, speech impediments, and accented or non-native speech [-M] — errors can cost more cognitive effort to fix than typing would have
- Young children with inconsistent speech patterns struggle to achieve usable accuracy [-M]
- Composing aloud changes the register of writing: dictated first drafts tend toward oral syntax and run-ons unless learners are taught to monitor for this [~M]
- Over-reliance without parallel handwriting/keyboard instruction may leave transcription skills underdeveloped for contexts where dictation is unavailable [-W]
- Continuous self-monitoring of the transcript while speaking imposes its own split-attention cost for some learners [~W]

#### Implementation Variability
- **Composition dictation** — drafting essays or stories by voice, then editing the transcript
- **Note-taking** — capturing lecture content or verbal summaries of reading
- **Response accommodation** — dictated answers on assessments for students with writing disabilities ([Accommodations](../elements/accommodations.md))
- **Language learning** — speaking practice with immediate visual feedback on what was understood
- **Voice commands + dictation hybrids** — editing by voice ("capitalize that," "new paragraph") versus mouse/keyboard editing

### Target Learners
- Students with dysgraphia, fine-motor or physical disabilities, or vision impairment, for whom transcription is the primary barrier [+M]
- Students with ADHD or executive function deficits whose ideas outrun their writing speed [+W]
- Struggling writers whose oral language exceeds their written output — the gap dictation closes is precisely the transcription gap [+M]
- Second-language learners, with the caveat that accent-related recognition errors can frustrate rather than support [~W]
- Less beneficial for learners whose oral vocabulary and sentence formulation are weaker than their writing skills — dictation removes a barrier they do not have [~M]

### Target Learning Goals
- Written composition: length, organization, and quality of expressive writing
- Content-area demonstration: showing knowledge on assessments when handwriting is a barrier
- Self-regulated writing: planning and monitoring ideas without transcription load ([Self-Regulated Learning](../theories/self-regulated-learning.md))
- Phonemic awareness and word recognition, when learners visually connect spoken words to their written forms [Automatic word recognition frees resources for comprehension.](../claims/automatic-word-recognition-frees-resources-for-comprehension.md) [+W]

### Instructions
1. Assess whether transcription (not idea generation) is the actual barrier; confirm the learner's oral language is stronger than their written output.
2. Select and configure the tool — train voice profiles where supported, set language and dialect.
3. Explicitly teach dictation conventions: speaking in short phrases, verbal punctuation, and correction commands ([Practice](../elements/practice.md)).
4. Start with low-stakes dictation tasks (brainstorming, summaries) before moving to full compositions ([Provide guidance](../elements/provide-guidance.md) — verify slug before linking if unavailable).
5. Teach transcript editing as a separate, explicit skill: reading aloud to catch recognition errors, then revising for written register ([Assess performance](../elements/assess-performance.md)).
6. Fade support as transcription-independent skills develop, per [Fading](../elements/fading.md) principles [Fading support promotes transfer of responsibility.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M].

## Related Strategies
- Word prediction and spell-check supports — complementary transcription accommodations that address spelling rather than motor demands
- Keyboarding instruction — the alternative transcription bypass; often taught alongside dictation so learners have two routes
- Pre-writing and oral rehearsal strategies — dictation pairs naturally with talking out ideas before (or as) drafting

## Related Elements
- [Accommodations](../elements/accommodations.md) — dictation is a canonical assessment and instructional accommodation
- [Practice](../elements/practice.md) — dictation fluency itself requires deliberate practice
- [Coaching](../elements/coaching.md) — individualized feedback on pacing, enunciation, and editing improves accuracy
- [Articulation](../elements/articulation.md) — dictation turns oral articulation directly into written product

## Examples
- A middle school student with dysgraphia uses [Dragon](https://www.nuance.com/dragon.html) to dictate essays, producing longer, more detailed drafts than by hand.
- Google Voice Typing ([Google Docs](https://docs.google.com)) used free-of-charge for drafting and revision in 1:1 device classrooms.
- Microsoft Dictate and Immersive Reader integration in [Office/Word](https://www.microsoft.com/microsoft-365) for dictated drafting with read-back for error checking.
- Speech-to-text as a documented accommodation on state assessments under IEP/504 plans, per [CAST UDL Guidelines](https://udlguidelines.cast.org) (multiple means of action and expression).

## Key Sources
- MacArthur, C. A. (2009). Reflections on research on writing and technology for struggling writers. *Learning Disabilities Research & Practice, 24*(2), 93–102. [doi:10.1111/j.1540-5826.2009.00283.x](https://doi.org/10.1111/j.1540-5826.2009.00283.x)
- Graham, S., & Perin, D. (2007). *Writing Next: Effective strategies to improve writing of adolescents in middle and high schools.* Alliance for Excellent Education. (Meta-analysis identifying transcription skill as a bottleneck for developing writers.)
- Forgrave, K. E. (2002). Assistive technology: Empowering students with learning disabilities. *The Clearing House, 75*(3), 122–126. [doi:10.1080/00098650209599250](https://doi.org/10.1080/00098650209599250)
- Evmenova, A. S., & Behrmann, M. M. (2011). Research-based practices in creative writing: A case study of the impact of outlining and graphic organizers on writing. *Journal of Special Education Technology, 26*(4), 1–14. (Speech-to-text within a technology-supported writing intervention.)
- CAST. (2018). *Universal Design for Learning Guidelines version 2.2.* [https://udlguidelines.cast.org](https://udlguidelines.cast.org)