---
type: strategy
title: Text Chats in Instruction
description: Using real-time text messaging platforms to support communication, questioning, and collaboration during instruction.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Text Chats in Instruction

## Description
Text chats in instruction use synchronous or near-synchronous text messaging — SMS, chat tools (Slack, Discord, Remind), or in-platform chat — as a channel for questions, discussion, feedback, and coordination during learning. The strategy lowers the social and logistical barriers to participation: learners can contribute without speaking publicly, and instructors can reach students in the channel they already use daily.

## Design Implications

Text chat functions as a low-threshold participation and feedback channel, which is most valuable when it feeds into structured instructional activities rather than replacing them. Because chat is informal and fragmented, its learning value depends on how messages are connected to tasks, [Assessment](../elements/assessment.md), and [Class Discussion](../elements/class-discussion.md) — unstructured chat streams tend to produce social presence without cognitive depth [~M]. Chat also competes for attention: notifications and off-task messaging during focused work measurably reduce learning performance [Kuznekoff & Titsworth found phone-related distraction reduces note-taking and recall.](https://doi.org/10.1080/03634523.2013.767917) [-S], so chat must be bounded by clear norms and task windows.

### Context
#### Requirements
- A platform accessible to all learners, with equitable device and connectivity assumptions stated up front
- Clear norms for when chat is on-task (e.g., backchannel during a lecture, Q&A windows, group coordination) and when it is off
- An instructor or facilitator presence that responds quickly enough to sustain the channel — an unanswered chat channel dies within days
- A purpose tied to instruction: questions, [Check-In](../elements/check-in.md) prompts, peer help, or [Coaching](../elements/coaching.md) follow-up

#### Constraints
- Multitasking with chat during lectures or reading reduces note-taking quality and recall [Kuznekoff & Titsworth found phone-related distraction reduces note-taking and recall.](https://doi.org/10.1080/03634523.2013.767917) [-S]
- Chat's brevity and informality constrain elaborated reasoning; complex conceptual discussion usually degrades into fragments unless an instructor synthesizes and re-anchors the thread [~M]
- Always-on channels blur boundaries and can create response-time pressure for instructors and anxiety for students; without norms, the channel becomes a liability rather than a support [-W]
- Learners with limited literacy in the language of instruction or with certain processing-speed challenges may be disadvantaged in fast-moving synchronous chat [~W]

#### Implementation Variability
- **Backchannel chat** during a live lecture or video, letting learners pose questions without interrupting flow
- **Q&A and help channels** for homework support, often with peer answering encouraged before instructor response
- **SMS nudges and spaced prompts** — short text messages delivering retrieval prompts, reminders, or micro-questions; text-message prompts have improved study behaviors and course outcomes in several field experiments [~M]
- **Small-group chat** for project coordination, paired with [Collaborative Learning](../principles/collaborative-learning.md) structures and defined roles
- **Asynchronous-first variants** (e.g., threaded channels in Slack/Discord) that preserve the low barrier while allowing longer-form contributions

### Target Learners
- Anxious or quiet students who rarely speak in whole-class settings; chat measurably widens the participation base compared with verbal discussion [~M]
- Adolescents and adults already fluent in texting; younger learners need more scaffolding for on-task norms
- Distance and hybrid learners, where chat substitutes for the informal corridor questions lost online [~W]
- Less suitable as a primary channel for learners needing extended, structured explanation — see [Cognitive Load Management](../principles/cognitive-load-management.md); fragmented chat adds extraneous load when content is complex

### Target Learning Goals
- Procedural and logistical clarity: unblocking learners quickly during tasks
- Social presence and community building, supporting persistence in online courses [~W]
- Formative checking: rapid pulse questions and [Check-In](../elements/check-in.md) responses that inform immediate instructional adjustment
- Not well suited as the sole medium for deep conceptual learning or [Application](../elements/application.md) of complex skills

### Instructions
1. Choose a platform all learners can access and set participation norms (response windows, on-task expectations, privacy).
2. Open the channel with a structured prompt — a question, a [Check-In](../elements/check-in.md), or a prediction — rather than an open "any questions?"
3. During instruction, use chat as a backchannel: monitor, cluster questions, and address them at planned pauses instead of continuously.
4. Route substantive questions into [Class Discussion](../elements/class-discussion.md) or [Assessment](../elements/assessment.md) activities; synthesize chat threads into summaries so fragments become shared artifacts.
5. Use the channel for spaced retrieval prompts and feedback between sessions, keeping messages short and task-focused.
6. Periodically audit the channel: participation breadth, response latency, and off-task ratio — adjust norms accordingly.

## Related Strategies
- [Class Discussion](../elements/class-discussion.md) — chat widens entry points but discussion structures deepen reasoning
- [Check-In](../elements/check-in.md) — chat is a natural delivery channel for rapid formative check-ins
- [Coaching](../elements/coaching.md) — chat sustains coaching contact between sessions

## Examples
- **Remind (https://www.remind.com)** — school-safe SMS/announcement platforms used for assignment reminders, quick pulse questions, and parent communication.
- **Backchannel with Slack or Discord in university courses** — instructors run course Q&A channels where peers answer first and instructors endorse or correct, building a searchable archive of explanations.
- **SMS retrieval practice in field settings** — studies sending spaced text-message questions to students between classes report improved study engagement and retention [~M].

## Key Sources
- Markett, C., Sánchez, L. A. I., Weber, S., & Tangney, B. (2006). Using short message service to encourage interactivity in the classroom. *Computers & Education, 46*(3), 280–293. [doi:10.1016/j.compedu.2005.11.014](https://doi.org/10.1016/j.compedu.2005.11.014)
- Kuznekoff, J. H., & Titsworth, S. (2013). The impact of mobile phone usage on student learning. *Communication Education, 62*(3), 233–252. [doi:10.1080/03634523.2013.767917](https://doi.org/10.1080/03634523.2013.767917)
- Tindell, D. R., & Bohlander, R. W. (2012). The use and abuse of cell phones and text messaging in the classroom: A survey of college students. *Computers in Human Behavior, 28*(1), 233–239. [doi:10.1016/j.chb.2012.05.001](https://doi.org/10.1016/j.chb.2012.05.001)
- Garrison, D. R., Anderson, T., & Archer, W. (2000). Critical inquiry in a text-based environment: Computer conferencing in higher education. *The Internet and Higher Education, 2*(2–3), 87–105. [doi:10.1016/S1096-7516(00)00016-6](https://doi.org/10.1016/S1096-7516(00)00016-6)