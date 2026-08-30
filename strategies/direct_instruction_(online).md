---
type: strategy
title: Direct Instruction (Online)
description: Direct instruction in online learning delivers pre-developed, explicitly structured presentations and targeted feedback, with the instructor diagnosing misconceptions, clarifying concepts, and directing learners to further practice.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Direct Instruction (Online)

## Description
Direct instruction in online learning involves pre-developed presentations, assessing student work and providing instructive feedback, diagnosing misconceptions, clarifying concepts, and referring students to additional resources or practice opportunities. It is a key component of teaching presence in the [Community of Inquiry](../principles/community-of-inquiry.md) framework, ensuring students receive guidance and support to achieve learning outcomes. Online, the instruction is typically asynchronous and must therefore be fully self-contained: the explanation, modeling, and checks for understanding that a face-to-face teacher improvises must be designed into the materials in advance.

## Design Implications

Explicit, well-structured online instruction reduces unguided search and working-memory burden for novices, particularly when explanations are segmented and paired with visuals [Kirschner, Sweller, and Clark argue minimal-guidance approaches overload novice working memory.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+M]. Effectiveness depends on instructional design quality: segmenting content, aligning narration with visuals rather than redundant on-screen text, and building in frequent checks for understanding [Multimedia design principles such as segmenting and signaling improve learning from narrated presentations.](../claims/chunking-reduces-working-memory-load.md) [+M]. Feedback should target the task and the process, not just a right/wrong verdict [Feedback most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S].

### Context
#### Requirements
- Pre-developed, well-structured presentations or materials with clear objectives and advance organizers ([Advance Organizers](../elements/advance-organizers.md))
- Assessment tools and timely feedback mechanisms (e.g., SpeedGrader in Canvas, embedded quiz checks)
- A mechanism for diagnosing misconceptions — embedded questions, [Self-Explanation](../elements/self-explanation.md) prompts, or low-stakes checks — so clarification is targeted rather than generic
- Curated pointers to additional resources and [Practice](../elements/practice.md) opportunities

#### Constraints
- One-way presentation without embedded checks or feedback loops leaves misconceptions undetected; direct instruction online loses its diagnostic function when delivery is purely broadcast [-M]
- Less effective for learners with strong prior knowledge, for whom highly guided instruction becomes redundant and can depress engagement [Guidance that helps novices can hinder more expert learners.](../claims/expertise-reversal-effect.md) [~S]
- Purely passive video or slide delivery without application tasks produces shallow encoding; instruction must be interleaved with [Practice](../elements/practice.md) and [Application](../elements/application.md) [-S]
- Long, unsegmented presentations exceed effective video length; attention and retention drop sharply beyond roughly 6–9 minutes [-M]

#### Implementation Variability
- Synchronous (live lecture with chat/polling checks) vs. asynchronous (recorded segments with embedded questions)
- Fully instructor-produced vs. curated (instructor selects and sequences existing materials, then adds framing and feedback)
- Degree of guidance can be faded across a course, shifting toward inquiry as expertise grows [Fading support promotes transfer of responsibility.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M]

### Target Learners
- Novices and online learners who need structured guidance and clear explanations, especially in high-content domains [Unguided methods disadvantage novices relative to explicit instruction.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+M]
- Learners with limited self-regulation skills who benefit from externally imposed structure and pacing
- Less beneficial for advanced learners, who profit more from open problems and reduced guidance [Guidance that helps novices can hinder more expert learners.](../claims/expertise-reversal-effect.md) [~S]

### Target Learning Goals
- Concept clarification and correction of misconceptions
- Procedural skill acquisition with clear step-by-step structure
- Foundational knowledge that later supports [Active Learning](../principles/active-learning.md) and transfer tasks

### Instructions
1. Define explicit learning outcomes and sequence content into short, segmented units ([Chunking](../principles/chunking.md), [Clear Structure](../principles/clear-structure.md))
2. Develop or curate presentations that model the skill or explain the concept, making reasoning visible ([Direct Instruction](../elements/direct-instruction.md), [Demonstration](../elements/demonstration.md))
3. Embed checks for understanding — low-stakes quizzes, [Self-Explanation](../elements/self-explanation.md) prompts, or discussion triggers — to surface misconceptions
4. Assess student work and provide instructive, process-focused feedback ([Assess Performance](../elements/assess-performance.md), [Provide Feedback](../elements/provide-feedback.md)) [Feedback most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]
5. Diagnose common misconceptions from the checks and deliver targeted clarification (announcement, short video, or annotated exemplar)
6. Refer students to additional resources or practice matched to diagnosed needs ([Practice](../elements/practice.md), [Coaching](../elements/coaching.md))

## Related Strategies
- [Flipped Classroom](../patterns/flipped-classroom.md) — direct instruction is delivered before class, freeing live time for application
- [Explicit Teaching](../patterns/explicit-teaching.md) — the face-to-face counterpart; same instructional logic
- [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md) — extends direct instruction with modeling, coaching, and fading

## Related Elements
- [Direct Instruction](../elements/direct-instruction.md) — the core element this strategy operationalizes online
- [Assess Performance](../elements/assess-performance.md) — the diagnostic loop that makes online instruction responsive
- [Coaching](../elements/coaching.md) — individualized follow-up once misconceptions are diagnosed
- [Advance Organizers](../elements/advance-organizers.md) — structure that orients learners before presentation

## Tools
- **Canvas SpeedGrader** — inline annotation and feedback on submitted work
- **Panopto / Kaltura** — recorded, segmented lecture capture with in-video quiz checks
- **H5P** — embedded interactive questions within instructional video

## Examples
- **ASU Online gateway courses** — short segmented concept videos with embedded comprehension checks, followed by adaptive practice sets and instructor feedback on common error patterns
- **[Khan Academy](https://www.khanacademy.org)** — narrated step-by-step demonstrations followed by practice exercises with hint scaffolds; a fully asynchronous direct-instruction model
- **Community of Inquiry teaching presence** — Anderson et al.'s framework treats direct instruction (diagnosing, clarifying, feeding back) as one of three teaching-presence responsibilities in online courses

## Key Sources
- Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why minimal guidance during instruction does not work: An analysis of the failure of constructivist, discovery, problem-based, experiential, and inquiry-based teaching. *Educational Psychologist, 41*(2), 75–86. [doi:10.1207/s15326985ep4102_1](https://doi.org/10.1207/s15326985ep4102_1)
- Anderson, T., Rourke, L., Garrison, D. R., & Archer, W. (2001). Assessing teaching presence in a computer conferencing context. *Journal of Asynchronous Learning Networks, 5*(2), 1–17. [doi:10.24059/olj.v5i2.1875](https://doi.org/10.24059/olj.v5i2.1875)
- Hattie, J. (2009). *Visible learning: A synthesis of over 800 meta-analyses relating to achievement.* Routledge. [doi:10.4324/9780203887330](https://doi.org/10.4324/9780203887330)
- Mayer, R. E. (2020). *Multimedia learning* (3rd ed.). Cambridge University Press. [doi:10.1017/9781316941355](https://doi.org/10.1017/9781316941355)
- Guo, P. J., Kim, J., & Rubin, R. (2014). How video production affects student engagement: An empirical study of MOOC videos. *Proceedings of the First ACM Conference on Learning @ Scale (L@S '14)*, 41–50. [doi:10.1145/2556325.2566239](https://doi.org/10.1145/2556325.2566239)