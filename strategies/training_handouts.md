---
type: strategy
title: Training Handouts
description: Training handouts are supplementary materials distributed during training sessions to enhance learner engagement, structure interactions, and provide a reference for key content.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Training Handouts

## Description
Training handouts are supplementary materials distributed during training sessions to structure attention, support note-taking, and provide a durable reference after the session ends. Effective handouts do not duplicate slides verbatim; they are designed as participation tools — outlines with gaps to complete, worksheets, feedback forms, and action plans — that require learners to actively process content during the session.

## Design Implications

Handouts work when they function as an external memory aid plus an engagement device: providing a partial outline frees working memory for processing rather than transcription [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+M], and structured note-taking prompts produce better recall than verbatim transcription or passive listening [~M]. The critical design decision is what to leave out — handouts containing all the content invite passive reading instead of active listening.

### Context
#### Requirements
- Alignment with session learning objectives; each handout section should map to a goal or activity
- Deliberate gaps: fill-in sections, response prompts, or checklists that require learner generation ([Annotating](../principles/annotating.md))
- Guidance on *when* to use the handout during the session, not just distribution at the start ([Provide guidance](../elements/provide-guidance.md))
- A post-session role — action plans and reference summaries — so the handout supports later retrieval ([Spaced repetition improves retention.](../claims/spaced-repetition-improves-retention.md) [+S])

#### Constraints
- Handouts that reproduce the full presentation reduce attention to the presenter and encourage passive reading [-M]
- Distributing dense reference material *during* a presentation splits visual attention between slides and page, harming both [~S] — reference handouts are better distributed after the session
- Verbatim note-taking prompts (handouts that encourage transcription) yield poorer conceptual learning than generative prompts [~M]
- Handouts no one revisits after the session add cost without retention benefit; without a follow-up task, post-session value approaches zero [-W]

#### Implementation Variability
- **Partial outlines** — key structure provided, details left for learners to complete during the session
- **Activity worksheets** — structured templates for pair work, case analysis, or peer feedback forms
- **Action plans** — end-of-session commitment sheets that convert content into intended workplace behavior
- **Post-session references** — summaries, job aids, and checklists distributed afterward for on-the-job support
- **Digital interactive handouts** — live documents (shared docs, LMS pages) that learners annotate collaboratively

### Target Learners
- Novice trainees who cannot yet distinguish central from peripheral content and benefit from an expert-prepared structure signaling what matters [Relevancy of emphasis directs attention.](../claims/relevancy-of-emphasis-directs-attention.md) [+M]
- Learners with limited note-taking skill, for whom a partial outline compensates for poor self-generated notes [~M]
- Less necessary for expert audiences, who can structure their own notes and may find guided outlines constraining [~W]

### Target Learning Goals
- Retention of key facts and procedures via a structured reference for later review
- Active engagement during sessions: prompts that trigger [Self-explanation](../elements/self-explanation.md) and application rather than transcription
- Transfer to practice: action plans and job aids that bridge training content and workplace performance

### Instructions
1. Identify the 3–5 session objectives and design one handout section per objective; cut anything that merely restates slides ([Clear structure presentation](../principles/clear-structure-presentation.md))
2. Build in generative gaps — blanks, prediction prompts, rating scales — so learners produce content rather than receive it ([Annotating](../principles/annotating.md))
3. Embed the handout in session activities: worksheets structure pair discussion, case analysis, and peer feedback rounds ([Practice](../elements/practice.md), [Class discussion](../elements/class-discussion.md))
4. Close with an action-planning section where each learner commits to specific applications ([Application of knowledge](../elements/application-of-knowledge.md))
5. Distribute reference material after the session and attach it to a follow-up task or reminder so it is actually revisited

## Related Strategies
- [Advance organizers](../elements/advance-organizers.md) — a partial-outline handout is an advance organizer delivered on paper
- [Active learning](../principles/active-learning.md) — handouts are a low-cost vehicle for embedding activity into lecture-based training
- [Check-ins](../principles/check-ins.md) — handout rating scales and response prompts can double as structured check-in tools

## Related Elements
- [Annotating](../principles/annotating.md) — the core learner behavior a well-designed handout elicits
- [Practice](../elements/practice.md) — worksheets structure in-session practice
- [Chunking](../principles/chunking.md) — handout sections should present content in digestible units
- [Assessment](../elements/assessment.md) — feedback forms and exit prompts make handouts a light formative-assessment channel

## Tools
- **Soapbox** (https://www.soapboxhq.com) — generates participant handouts automatically from a lesson plan outline
- **Google Docs / Microsoft 365** — shared live handouts for collaborative annotation
- **LMS handout repositories** (Canvas, Moodle) — post-session reference distribution with follow-up reminders

## Examples
- **Corporate onboarding (e.g., Dale Carnegie training programs)** — participant manuals with fill-in frameworks, practice exercises, and commitment pages that structure each module rather than duplicating slides
- **Peer feedback forms in workshop training** — structured observation sheets that guide specific, criterion-referenced peer comments during practice rounds
- **Action planning worksheets in teacher professional development** — end-of-session plans naming one technique, one context, and one success indicator, revisited at the next session

## Key Sources
- Clark, R. C., & Mayer, R. E. (2016). *E-Learning and the Science of Instruction* (4th ed.). Wiley. [doi:10.1002/9781119239086](https://doi.org/10.1002/9781119239086)
- Kiewra, K. A. (1989). A review of note-taking: The encoding-storage paradigm and beyond. *Educational Psychology Review, 1*(2), 147–172. [doi:10.1007/bf01326640](https://doi.org/10.1007/bf01326640)
- Mueller, P. A., & Oppenheimer, D. M. (2014). The pen is mightier than the keyboard: Advantages of longhand over laptop note taking. *Psychological Science, 25*(6), 1159–1168. [doi:10.1177/0956797614524581](https://doi.org/10.1177/0956797614524581)
- Bligh, D. A. (2001). *What's the Use of Lectures?* (6th ed.). Jossey-Bass.
- Hartley, J., & Davies, I. K. (1978). Note-taking: A critical review. *Programmed Learning and Educational Technology, 15*(3), 207–224.