---
type: strategy
title: Screencast Feedback
description: Audiovisual feedback in which the instructor records their screen while narrating comments on a learner's work, combining spoken commentary with a visual walkthrough of the artifact.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Screencast Feedback

> **Strategy** · [All strategies](index.md)

## Description
Screencast feedback is a form of technology-mediated formative feedback in which the instructor records the learner's assignment on screen (a document, code, design, or dataset) while providing spoken commentary, often pointing to, highlighting, or annotating specific passages as they talk. It replaces or supplements written margin comments with a richer, dialogic-feeling audiovisual message that conveys tone, emphasis, and reasoning alongside the content of the critique.

## Design Implications

Screencast feedback leverages the redundancy and signaling affordances of combined audio and visual channels: learners see exactly which text or artifact feature the instructor is discussing while hearing the explanation, reducing the ambiguity that written comments often create [~M]. Because voice carries paralinguistic cues, screencast feedback is consistently perceived by students as more personal, detailed, and caring than written feedback, which can strengthen the learner's willingness to engage with critique [~M]. Feedback of any kind improves achievement when learners act on it, so screencasts should be tied to revision opportunities rather than delivered as terminal evaluation [Assessment for learning improves achievement.](../claims/assessment-for-learning-improves-achievement.md) [+S].

### Context
#### Requirements
- Screen-recording tooling (e.g., Zoom, Loom, Screencast-O-Matic, Kaltura) and a workflow for returning videos securely to learners
- A visible artifact to comment on — screencasts work best when the instructor can point at the exact element under discussion
- A time budget: recording is faster than typing long comments, but videos cannot be skimmed, so instructors must keep them focused (typically 3–7 minutes)
- A follow-on task requiring learners to act on the feedback ([Practice](../elements/practice.md), revision, or resubmission)

#### Constraints
- Video cannot be scanned or skimmed the way written comments can; learners must watch linearly, which raises time cost and can bury key points mid-video [~M]
- Long or unstructured screencasts risk cognitive overload — split attention between listening, watching cursor movement, and reading the artifact degrades learning [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [-M]
- Students with hearing impairments, or those studying in a second language, may be disadvantaged unless transcripts or captions are provided [-M]
- Learners who prefer private, re-readable written comments sometimes report discomfort with the intimacy of hearing an instructor's voice [~W]
- Storage, bandwidth, and privacy constraints (student work visible on screen) complicate deployment at scale

#### Implementation Variability
- **Document walkthrough**: cursor highlighting and verbal margin comments on essays or reports
- **Code review**: narrated line-by-line critique in an IDE, common in computing education
- **Comparative modeling**: instructor rewrites or fixes a portion live, turning feedback into a brief [demonstration](../elements/demonstration.md)
- **Hybrid**: short screencast summarizing priorities plus written comments for detail, preserving scannability
- **Peer screencasting**: students record feedback for each other, deepening their own evaluation skills

### Target Learners
- Online and distance learners, for whom feedback is often the main instructor "touchpoint" and social presence is scarce [~M]
- Novices, who benefit from the instructor pointing at exactly what to look at rather than interpreting written references to "paragraph 3" [~M]
- Less beneficial for advanced learners who need only terse, scannable corrections and can self-locate issues [~W]

### Target Learning Goals
- Revision and iterative improvement of complex artifacts (writing, code, designs)
- Making evaluation criteria transparent — learners hear *why* something is a problem, not just that it is
- Instructor social presence and relationship-building in mediated courses

### Instructions
1. Skim the work first and decide on 2–3 priority points; do not narrate a cold read.
2. Open the learner's artifact on screen and start recording; greet the learner by name to establish rapport.
3. Point to or highlight each element as you discuss it, pairing visual signaling with verbal explanation to avoid split attention [Cognitive Load Management](../principles/cognitive-load-management.md).
4. Lead with strengths briefly, then spend most of the time on the highest-leverage improvements, explaining the reasoning against the task criteria.
5. End with a concrete next action — a revision task or [practice](../elements/practice.md) opportunity the learner completes before the next attempt.
6. Keep recordings under ~7 minutes; provide captions or a transcript for accessibility.

## Related Strategies
- [Written margin comments](../strategies/written-feedback.md) — the default alternative; scannable but lower in tone and specificity
- [Audio feedback](../strategies/audio-feedback.md) — the voice-only variant; retains tone but loses visual pointing
- [Rubric-based feedback](../strategies/rubric-feedback.md) — provides the criteria structure a screencast can reference

## Examples
- **Writing-intensive online courses**: instructors at many universities use Zoom or Kaltura to record 5-minute document walkthroughs of essay drafts before revision; research on such implementations (e.g., in Distance Education studies of screencast feedback) reports students rating screencasts as more useful and personal than written comments.
- **Computing education**: CS instructors record narrated code reviews of student submissions in an IDE, showing the running program failing and explaining the fix — combining feedback with live [demonstration](../elements/demonstration.md).
- **Loom for Education** (https://www.loom.com/education) — a widely used tool for asynchronous video feedback with cursor highlighting and easy LMS sharing.

## Key Sources
- Henderson, M., & Phillips, M. (2015). Video-based feedback on student assessment: Scarily personal. *Distance Education, 36*(1), 51–66. [doi:10.14742/ajet.1878](https://doi.org/10.14742/ajet.1878)
- Borup, J., West, R. E., Thomas, R., & Graham, C. R. (2015). The influence of asynchronous video communication on learner social presence: A narrative analysis of four cases. *Distance Education, 36*(1), 67–85. [doi:10.1080/01587919.2013.770427](https://doi.org/10.1080/01587919.2013.770427)
- Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81–112. [doi:10.3102/003465430298487](https://doi.org/10.3102/003465430298487)
- Mayer, R. E. (2021). *Multimedia learning* (3rd ed.). Cambridge University Press. [doi:10.1017/9781316941355](https://doi.org/10.1017/9781316941355)