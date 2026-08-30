---
type: element
title: Pre-Class Video/Lecture
description: Instructional content is delivered via video or recorded lecture before in-class activities, freeing class time for active learning.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Pre-Class Video/Lecture

## Description
Instructional content — exposition, worked demonstrations, or recorded lectures — is delivered via video before class, so that synchronous time can be spent on application, discussion, and feedback rather than first exposure. The video functions as the initial-instruction component of a [Flipped Classroom](../patterns/flipped-classroom.md), shifting information transmission outside the group learning space.

## Design Implications

Pre-class video works only when paired with accountability and application: students who watch without a follow-up task learn little, and class time that merely re-lectures the video undermines the design [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [+S]. Videos should be short, segmentable, and aligned to specific in-class activities; multimedia design principles (signaling, segmenting, conversational narration) measurably improve learning from video [Media presentations combining narration and relevant visuals affect recall and retention.](../claims/media-combinations-affect-recall-and-retention.md) [+M].

### Context
#### Requirements
- Short segments (roughly 6 minutes or less) matched to a single objective; engagement drops sharply with longer videos [Video length and production style affect student engagement.](https://doi.org/10.1145/2556325.2566239) [+M]
- Embedded questions or note-taking prompts that require active processing, not passive viewing [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+M]
- A low-stakes accountability mechanism (quiz, ticket-in, [Check-Ins](../principles/check-ins.md)) so instructors can verify completion before class
- In-class activities that *depend* on the video content, creating a reason to watch

#### Constraints
- Without accountability or in-class dependence, completion rates collapse and the flip fails [-M]
- Re-lecturing video content in class signals that preparation was optional and erodes the norm [-M]
- Students with weak prior knowledge may misinterpret first-exposure video without a mechanism for questions; the video cannot respond to confusion the way live instruction can [~M]
- Requires reliable device and bandwidth access; assigning video as homework can widen equity gaps [~W]
- For complex or high-load material, a single unsegmented lecture video overloads working memory [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+M]

### Target Learners
- Undergraduates and professionals with the self-regulation to complete asynchronous work [Self-monitoring improves self-regulation.](../claims/self-monitoring-improves-self-regulation.md) [+M]
- STEM and procedural domains where demonstrations translate well to video
- Less effective for novices with no prior knowledge base, who benefit more from guided first exposure with immediate question-answering [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M] — the flip assumes learners can extract structure from unguided exposure

### Target Learning Goals
- First-exposure knowledge acquisition (facts, concepts, procedures) moved out of class to reserve class time for higher-order goals
- Procedural preparation: students arrive ready to [Practice](practice.md) or apply rather than to hear content for the first time
- Not well suited as the sole vehicle for conceptual change or discussion-dependent goals

### Affordances
- [Cognitive Load Theory](../principles/cognitive-load-theory.md) — video allows precise segmenting, pausing, and signaling that live lecture cannot; learners control pace and can re-watch difficult segments, managing intrinsic load themselves
- [Direct Instruction](../principles/direct-instruction.md) — the video is a scripted, reusable form of explicit first exposure, delivering the same clear explanation to every learner
- [Active Learning](../principles/active-learning.md) — the entire rationale is to convert contact time from transmission to active learning; the video is the enabling condition, not the intervention itself
- [Chunking](../principles/chunking.md) — short, single-objective videos enact chunking by presenting one concept per segment
- [Clear Structure](../principles/clear-structure-presentation.md) — a video with explicit objectives, signaling, and a predictable format reduces extraneous processing

## Related Elements
- [Assigned Readings](assigned-readings.md) — the text-based alternative for pre-class first exposure; video offers better control of pace and tone, text offers faster skimming and search
- [Practice](practice.md) — the in-class activity the video should feed into
- [Assessment](assessment.md) — low-stakes pre-class quizzes serve as both accountability and retrieval practice
- [Class Discussion](class-discussion.md) — a common use of the freed class time
- [Advance Organizers](advance-organizers.md) — a framing device that can precede the video to orient viewing

## Patterns That Use This Element
- [Flipped Classroom](../patterns/flipped-classroom.md) — the defining element; first exposure via video, application in class
- [Blended Learning](../patterns/blended-learning.md) — the online/in-person boundary the video marks

## Examples

**[Khan Academy](https://www.khanacademy.org)** — Short narrated problem-solving videos designed for pre-class or pre-practice viewing, paired with exercises that depend on them.

**[Edpuzzle](https://edpuzzle.com)** — Platform for embedding questions into existing videos, enforcing accountability and active viewing during pre-class assignments.

**[3Blue1Brown](https://www.3blue1brown.com)** — Visually rich animated mathematics explanations illustrating how signaling and dynamic visualization can make abstract content tractable as first exposure.

**Flipped STEM courses (e.g., University of Washington's flipped introductory chemistry)** — Published implementations pairing short pre-class videos with in-class problem solving; studies report moderate learning gains over lecture-only formats [Investigating the effects of a flipped classroom on student learning.](https://doi.org/10.1187/cbe.14-08-0129) [+M]

## Key Sources
- Guo, P. J., Kim, J., & Rubin, R. (2014). How video production affects student engagement in MOOCs. *Proceedings of the First ACM Conference on Learning @ Scale*, 41–50. [doi:10.1145/2556325.2566239](https://doi.org/10.1145/2556325.2566239)
- Brame, C. J. (2016). Effective educational videos: Principles and guidelines for maximizing student learning from video content. *CBE—Life Sciences Education, 15*(4), es6. [doi:10.1187/cbe.16-03-0125](https://doi.org/10.1187/cbe.16-03-0125)
- Jensen, J. L., Kummer, T. A., & Godoy, P. D. d. M. (2015). Improvements from a flipped classroom may simply be the fruits of active learning. *CBE—Life Sciences Education, 14*(1), ar5. [doi:10.1187/cbe.14-08-0129](https://doi.org/10.1187/cbe.14-08-0129)
- Mayer, R. E. (2009). *Multimedia learning* (2nd ed.). Cambridge University Press. [doi:10.1017/CBO9780511811678](https://doi.org/10.1017/CBO9780511811678)
- Bergmann, J., & Sams, A. (2012). *Flip your classroom: Reach every student in every class every day*. ISTE/ASCD.

---