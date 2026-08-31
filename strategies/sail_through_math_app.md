---
type: strategy
title: Sail through Math App
description: A pirate-themed iOS app that builds arithmetic fluency in young learners through story-framed, leveled practice with immediate feedback.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Sail through Math App

> **Strategy** · [All strategies](index.md)

## Description
Sail through Math is an iOS app from McGraw-Hill Education that develops arithmetic fluency — addition, subtraction, multiplication, and division, including equations and two-step problems — through a pirate-themed narrative. Learners progress through three difficulty levels, solving math facts and equations embedded in story contexts (firing cannonballs, earning treasure), with the game providing immediate correctness feedback and level progression as performance improves.

## Design Implications

The app exemplifies game-framed [Practice](../elements/practice.md) for math facts: fluency with basic combinations frees working memory for higher-order reasoning, and retrieval practice with feedback is the most reliable route to that automaticity [Spaced, repeated retrieval practice improves retention.](../claims/spaced-repetition-improves-retention.md) [+S]. Immediate feedback on each answer supports error correction at the task level [Feedback is most effective at the task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]. The three-level structure functions as coarse [Adaptive Difficulty](../elements/adaptive-difficulty.md), keeping problems within a manageable band of challenge [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+M].

### Context
#### Requirements
- Access to the Sail through Math app on an iOS device (iPad or iPhone)
- Learners with sufficient decoding ability or adult support to read story prompts
- Periodic adult monitoring of which level a learner is working at, since self-pacing can stall at easy levels

#### Constraints
- Limited to iOS devices; no web or Android version, restricting classroom deployment
- The narrative theme is decorative rather than integral — the stories frame problems but do not change the underlying mathematics, so engagement gains may fade once novelty wears off [~W]
- Drill-based fact practice alone does not build conceptual understanding of operations; it must be paired with instruction on number relationships [-S] — overreliance on timed fact apps can produce math anxiety in some young learners [~M]
- Three fixed levels provide limited adaptation compared with fully adaptive systems; learners far above or below a level band get little benefit

#### Implementation Variability
- Use as a station-rotation activity (10–15 min sessions) rather than whole-class instruction
- Pair with concrete manipulatives or number talks so fact retrieval is connected to conceptual models
- Use level completion data as a formative checkpoint in [Assess Performance](../elements/assess-performance.md) routines

### Target Learners
- Early elementary learners (roughly ages 6–10) building initial fluency with the four operations
- Learners who benefit from low-stakes, high-repetition practice with immediate feedback [Feedback is most effective at the task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]
- Less suitable for learners who already have fluent fact retrieval (redundant practice) or who need conceptual reteaching rather than drill

### Target Learning Goals
- Automatic recall of basic math facts across the four operations
- Solving one- and two-step equations
- Fluency as a prerequisite for later problem solving — automaticity reduces cognitive load during complex tasks [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+M]

### Instructions
1. Set the learner at the appropriate level (addition/subtraction for early grades; multiplication/division later) and model one session so learners understand the story framing and feedback signals.
2. Schedule short, regular practice sessions — distributed practice outperforms massed sessions for fact retention [Spaced, repeated retrieval practice improves retention.](../claims/spaced-repetition-improves-retention.md) [+S].
3. Have learners [Practice](../elements/practice.md) within the app while the system delivers immediate correctness [Provide Feedback](../elements/provide-feedback.md) on each response.
4. Review level-completion data with the learner to [Assess Performance](../elements/assess-performance.md) and adjust level placement or provide targeted offline support for persistent error patterns.
5. Connect app practice to classroom instruction — discuss strategies (doubles, make-ten) so retrieval is anchored in understanding.

## Related Strategies
- [Timed math fact drills](timed_math_fact_drills.md) — the non-digital counterpart; the app gamifies the same retrieval-practice mechanism
- [Station rotation](station_rotation.md) — a common classroom structure for scheduling short app-based practice blocks

## Related Elements
- [Practice](../elements/practice.md) — the core mechanism; the app is a delivery vehicle for distributed retrieval practice
- [Provide Feedback](../elements/provide-feedback.md) — immediate per-item feedback is the app's primary instructional lever
- [Assess Performance](../elements/assess-performance.md) — level progression provides built-in performance data
- [Adaptive Difficulty](../elements/adaptive-difficulty.md) — the three-level structure approximates difficulty calibration

## Tools
- [Sail through Math (McGraw-Hill, iOS App Store)](https://apps.apple.com/us/app/everyday-mathematics-sail-through-math/id465271965)

## Examples
- A second-grade classroom uses Sail through Math as a 10-minute morning station three times per week; the teacher reviews level-completion data weekly to identify students needing small-group support with subtraction regrouping.
- A parent uses the app at home over summer break to maintain multiplication fluency, with the pirate narrative sustaining engagement across sessions.

## Key Sources
- National Mathematics Advisory Panel. (2008). *Foundations for success: The final report of the National Mathematics Advisory Panel*. U.S. Department of Education.
- Shin, N., Sutherland, L. M., Norris, C. A., & Soloway, E. (2012). Effects of game technology on elementary student learning in mathematics. *British Journal of Educational Technology, 43*(4), 540–560. [doi:10.1111/j.1467-8535.2011.01197.x](https://doi.org/10.1111/j.1467-8535.2011.01197.x)
- Outhwaite, L. A., Faulder, M., Gulliford, A., & Pitchford, N. J. (2019). Raising early achievement in math with interactive apps: A randomized control trial. *Journal of Educational Psychology, 111*(2), 284–298. [doi:10.1037/edu0000286](https://doi.org/10.1037/edu0000286)
- Baroody, A. J., Bajwa, N. P., & Eiland, M. (2009). Why can't Johnny remember the basic facts? *Developmental Disabilities Research Reviews, 15*(1), 69–79. [doi:10.1002/ddrr.45](https://doi.org/10.1002/ddrr.45)