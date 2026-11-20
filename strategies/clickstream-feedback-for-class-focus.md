---
type: strategy
id: clickstream-feedback-for-class-focus
title: Use clickstream data from online video players to inform what to focus on during class
description: The article recommends analyzing time-stamped video-player interaction logs (plays, pauses, seeks) as feedback for instructors of flipped courses.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
sources:
  - id: john-m-aiken-2013
    resource: "http://youtu.be/DcjIgJY5ets"
    title: "John M. Aiken, Shih-Yin Lin, Scott S. Douglas, Edwin F. Greco, Brian D. Thoms, Marcos D. Caballero and Michael F. Schatz. (2013). Student Use of a Single Lecture Video in a Flipped Introductory Mechanics Course. http://youtu.be/DcjIgJY5ets"
    author: John M. Aiken, Shih-Yin Lin, Scott S. Douglas, Edwin F. Greco, Brian D. Thoms, Marcos D. Caballero and Michael F. Schatz
---

# Use clickstream data from online video players to inform what to focus on during class

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (4 for, 1 mixed) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
The article recommends analyzing time-stamped video-player interaction logs (plays, pauses, seeks) as feedback for instructors of flipped courses. According to the authors, "Clickstream data can provide valuable feedback about time on task, where students focus their attention, and what should be focused on during class." By mapping pause and seek distributions onto coded video-timeline categories, instructors can see which content segments students attend to and adjust in-class emphasis accordingly.

## Design Implications

### Context
#### Requirements
- Access to time-stamped clickstream logs from the video player
- Removal of auto-generated pauses (e.g., at interaction points) and noise correction, which the authors implemented using the median absolute deviation because the pause distribution is not normal
#### Constraints
- Findings here represent analysis of only one of the seventy-eight videos students watched that semester, and interaction with this video could be unique to this type (lab) of video

### Target Learners
- undergraduate students in flipped large-enrollment courses

### Target Learning Goals
- informing instructors about student pre-class video engagement and what to highlight during class

### Affordances
- [Video Timeline Six Categories](../research-methods/six-category-video-timeline-coding-scheme-for-characterizing-lecture-video-content.md)

## Claims

- [Students' focus on solution-finding segments suggests they may not attend to conceptual video elements any more than in a passive lecture](../claims/conceptual-attention-like-passive-lecture.md) [~W]
- [Students' initial viewing behavior of the lecture video differed from their subsequent viewing behavior, consistent with downloading the starter script at the second interaction point](../claims/initial-vs-subsequent-viewing-differ.md) [+W]
- [A pause peak immediately after the third interaction point suggests some students paused to copy down the correct Newton's 2nd law code after the answer was given](../claims/pause-peak-after-answer-copying.md) [+W]
- [Students' deliberate pauses in a flipped-course lecture video cluster on segments presenting specific parameter values and code needed for the assignment](../claims/pauses-cluster-on-parameter-values.md) [+W]
- [A single student's watching trajectory showed seeking and pausing mid-video to find values needed for the assignment, with only 46.8 s spent on the conceptual interaction-point questions](../claims/single-student-trajectory-value-seeking.md) [+W]

## Related Strategies

- [Model student performance on complex activities starting from in-class engagement measures rather than video clickstream features](model-complex-performance-from-in-class-engagement.md)
- [Use learning analytics from VLE logs rather than student feedback alone to detect low engagement with pre-class work](learning-analytics-detect-hidden-disengagement.md)

## Examples
-

## Key Sources
- John M. Aiken, Shih-Yin Lin, Scott S. Douglas, Edwin F. Greco, Brian D. Thoms, Marcos D. Caballero and Michael F. Schatz. (2013). Student Use of a Single Lecture Video in a Flipped Introductory Mechanics Course. http://youtu.be/DcjIgJY5ets
