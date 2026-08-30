---
type: strategy
title: Feedback Through Different Media
description: Delivering feedback through varied media (video, audio, screencast, text) changes its tone, richness, and impact, with video and audio often conveying more personal, encouraging feedback than written text.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Feedback Through Different Media

## Description
Feedback can be delivered through text, audio, video, screencast, or face-to-face channels, and the choice of medium shapes how learners perceive and use it. Video and audio feedback carry paralinguistic cues — tone of voice, pacing, facial expression — that soften critique and convey instructor presence, whereas text is faster to scan, easier to reference, and better suited to precise, itemized corrections.

## Design Implications

The medium is not neutral: richer media increase perceived instructor presence and student satisfaction, but media that combine redundant visual and verbal channels can overload working memory if poorly designed [Media combinations affect recall and retention.](../claims/media-combinations-affect-recall-and-retention.md) [~M]. Whatever the channel, feedback content matters more than delivery format — feedback targeting the task and the process outperforms feedback about the self [Feedback is most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]. Video and audio feedback are typically faster for instructors to produce than equivalent written comments, though harder for students to skim or search.

### Context
#### Requirements
- A clear purpose for each feedback episode (correction, elaboration, encouragement) matched to an appropriate medium
- For video/screencast: a way to display the learner's work while commenting (e.g., screen annotation tools)
- Consistency of delivery so learners know where and how to find feedback
- Attention to multimedia design principles — narration aligned with relevant visuals, no redundant on-screen text duplicating narration ([Clark & Mayer, 2016](https://doi.org/10.1002/9781119239086)) [+M]

#### Constraints
- Video and audio feedback cannot be skimmed or searched the way text can; learners seeking a specific correction must scrub through recordings [-M]
- Rich media can create a *social presence illusion* — students report liking video feedback more, but learning gains are often equivalent to well-written text [~M]
- Poorly designed multimedia (narration reading verbatim on-screen text) actively harms learning [Media combinations affect recall and retention.](../claims/media-combinations-affect-recall-and-retention.md) [-M]
- Audio/video feedback raises accessibility issues for learners with hearing impairments or those in noise-constrained environments; transcripts or captions are needed

#### Implementation Variability
- **Screencast feedback**: instructor annotates the learner's document or code on screen while narrating — strongest for procedural and written work
- **Audio-over-document**: voice comments embedded at specific points, combining text's precision with speech's tone
- **Video talking-head**: best for relational, motivational feedback or whole-assignment summaries
- **Structured text**: remains the medium of choice for itemized, criterion-referenced corrections learners need to revisit

### Target Learners
- Distance and online learners, for whom media richness compensates for reduced instructor presence [~M]
- Anxious or low-efficacy students, who may read harsh intent into terse written comments; spoken tone mitigates this [~W]
- Students revising written work benefit from screencast feedback pointing at specific passages [~M]

### Target Learning Goals
- Revision and improvement of written, code, or design artifacts
- Self-regulated learning: process-level feedback delivered conversationally can prompt reflection [Feedback is most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]
- Affective goals: persistence and motivation in online courses

### Instructions
1. Decide the feedback's primary function — correction, elaboration, or motivation — and let that drive the medium choice; keep content aligned to task and process levels [Feedback is most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]
2. For work requiring precise revision, use screencast or audio-over-document so comments anchor to specific locations
3. Apply multimedia design principles: narrate over the learner's actual work rather than reading slides or duplicating text on screen ([Clark & Mayer, 2016](https://doi.org/10.1002/9781119239086))
4. Keep video/audio feedback short (3–7 minutes); long recordings are rarely re-watched
5. Pair rich-media feedback with a written summary of required actions so learners have a skimmable record; make feedback actionable ([Action-Oriented Feedback](action-oriented-feedback.md))
6. Provide captions or transcripts to maintain accessibility

## Related Strategies
- [Action-Oriented Feedback](action-oriented-feedback.md) — the content standard any feedback medium should meet
- [Check-Ins](../principles/check-ins.md) — brief media-rich touchpoints that sustain instructor presence between major feedback episodes

## Examples
- **Screencast feedback in writing courses**: instructors at many universities use tools such as [Turnitin Feedback Studio](https://www.turnitin.com) or [ScreenPal](https://screenpal.com) to record narrated, annotated walkthroughs of student essays, pointing at specific sentences while explaining revisions.
- **Audio comments in LMS grading**: Canvas and SpeedGrader support embedded audio comments, letting instructors deliver tone-rich feedback faster than typing.
- **Video feedback in MOOCs**: [Coursera](https://www.coursera.org) peer-review workflows pair rubric scores with short instructor videos explaining common errors across the cohort.

## Key Sources
- Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81–112. [doi:10.3102/003465430298487](https://doi.org/10.3102/003465430298487)
- van der Kleij, F. M., Feskens, R. C. W., & Eggen, T. J. H. M. (2015). Effects of feedback in a computer-based learning environment on students' learning outcomes: A meta-analysis. *Review of Educational Research, 85*(4), 475–511. [doi:10.3102/0034654314564881](https://doi.org/10.3102/0034654314564881)
- Clark, R. C., & Mayer, R. E. (2016). *E-Learning and the Science of Instruction* (4th ed.). Wiley. [doi:10.1002/9781119239086](https://doi.org/10.1002/9781119239086)
- Henderson, M., Ryan, T., & Boud, D. (2019). Learning to listen: Exploring students' engagement with audio feedback. *Assessment & Evaluation in Higher Education, 44*(8), 1259–1271. [doi:10.1080/02602938.2019.1586648](https://doi.org/10.1080/02602938.2019.1586648)