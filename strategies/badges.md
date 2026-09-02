---
type: strategy
id: badges
title: Badges
description: Badges are digital credentials that acknowledge learner work, awarded for achievement levels or additional contributions such as submitting drafts or sharing notes.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Badges

> **Strategy** · [All strategies](index.md)

## Description
Badges are a digital way to acknowledge learner work. Learners can receive a badge if they achieve certain levels of success on assignments, or if they do additional work, such as submitting a draft or sharing notes with another learner. Badges may be displayed to other learners in the class as a means to encourage competition or to demonstrate the variety of badges which can be earned. Well-designed badges function as micro-credentials: they carry explicit criteria and evidence, making them closer to [Competency-Based Assessment](../principles/competency-based-assessment.md) than to simple participation rewards.

## Design Implications

Badges operate as extrinsic motivators, and their effect on learning depends almost entirely on what they signal and how they are framed. Badges tied to meaningful performance criteria can support engagement and goal-directed effort [task value increases motivation and engagement](../claims/task-value-increases-motivation-and-engagement.md) [+M], but rewards for activities learners already find interesting can undermine intrinsic motivation [autonomy supports intrinsic motivation](../claims/autonomy-supports-intrinsic-motivation.md) [~M]. Badges that mark progress toward mastery (e.g., "revised and resubmitted") align better with learning than badges that mark rank or comparison.

### Context
#### Requirements
- Badge-issuing infrastructure (e.g., [Credly](https://info.credly.com), [Open Badges](https://1edtech.org/standards/open-badges) from 1EdTech) or LMS integration (Canvas, Moodle badges)
- Clear, transparent criteria for earning each badge, so the badge represents a verifiable achievement rather than a token
- Alignment between badge criteria and valued learning behaviors, not just completion counts
- A display or portfolio mechanism so badges have social or personal meaning

#### Constraints
- Badges can shift attention from learning to token accumulation — learners optimize for the reward rather than the underlying goal [~M]
- Expected, contingent rewards for tasks learners already enjoy can reduce intrinsic motivation once rewards stop [~S]
- Public badge displays framed as competition can demotivate lower-performing learners and reduce [self-efficacy](../claims/self-efficacy-predicts-academic-persistence.md) [-M]
- Badges awarded for mere participation carry little evidential value and quickly lose motivational force [-W]
- Badge systems require ongoing maintenance; stale or trivially easy badges erode credibility of the whole system [-W]

#### Implementation Variability
- **Achievement badges** — tied to performance levels on assessments; strongest link to learning
- **Process badges** — reward productive behaviors (submitting a draft, peer feedback, sharing notes); support self-regulation and process goals [process goals outperform outcome goals for novices](../claims/process-goals-outperform-outcome-goals-for-novices.md) [+M]
- **Progression badges** — sequenced levels that visualize a learning pathway, similar to leveling in games
- **Private vs. public display** — private badges function as progress markers; public badges add social recognition but introduce comparison effects
- **Learner-selected display** — letting learners choose which badges to showcase supports autonomy and identity-building

### Target Learners
- All learner levels; particularly useful in online and large-enrollment settings where individual recognition is otherwise scarce
- Younger learners and gamification-responsive audiences, though effects vary widely by individual [~W]
- Less effective for learners who find game mechanics juvenile or who are already highly self-regulated [-W]

### Target Learning Goals
- Motivation and engagement: encouraging participation and persistence
- Self-regulation: rewarding productive process behaviors such as drafting and revision
- Competency signaling: making achievement levels visible to learners, peers, and (with Open Badges) external audiences

### Instructions
1. Define the learning behaviors or achievements worth recognizing, aligned to course goals — not every activity needs a badge.
2. Write explicit, verifiable criteria for each badge and publish them in advance.
3. Configure badge issuance in your platform ([Credly](https://info.credly.com), Open Badges, or LMS-native badges).
4. [Assess performance](../elements/assessment.md) against the published criteria and issue badges promptly so recognition follows the achievement.
5. [Provide feedback](../elements/provide-feedback.md) alongside badges — a badge should accompany, not replace, substantive feedback on the work.
6. Decide on display policy: private progress tracking, learner-curated portfolios, or class-visible boards; prefer learner choice over imposed competition.

## Related Strategies
- [Gamification](gamification.md) — badges are one of the most common gamification elements; the same motivation caveats apply
- [Micro-credentials](micro-credentials.md) — badges at institutional scale with external recognition
- [Leaderboards](leaderboards.md) — a competitive display mechanism often paired with badges, with stronger demotivation risks

## Related Elements
- [Assessment](../elements/assessment.md) — badge criteria must be grounded in real assessment of the work
- [Provide Feedback](../elements/provide-feedback.md) — badges should accompany feedback, not substitute for it

## Examples
- **[Khan Academy](https://www.khanacademy.org)** — energy-point and badge system rewarding practice volume and mastery levels; an early large-scale implementation of badge progression.
- **[Mozilla Open Badges](https://1edtech.org/standards/open-badges)** (now 1EdTech standard) — open specification for portable, evidence-linked badges used in professional and higher education credentialing.
- **[Credly](https://info.credly.com)** — enterprise badging platform used by universities and professional bodies for stackable micro-credentials.
- **Course-level example** — awarding a "Reviser" badge for submitting a revised draft after feedback, rewarding process rather than outcome.

## Key Sources
- Deci, E. L., Koestner, R., & Ryan, R. M. (1999). A meta-analytic review of experiments examining the effects of extrinsic rewards on intrinsic motivation. *Psychological Bulletin, 125*(6), 627–668. [doi:10.1037/0033-2909.125.6.627](https://doi.org/10.1037/0033-2909.125.6.627)
- Abramovich, S., Schunn, C., & Higashi, R. M. (2013). Are badges useful in education? It depends upon the type of badge and expertise of learner. *Educational Technology Research and Development, 61*(2), 217–232. [doi:10.1007/s11423-013-9289-2](https://doi.org/10.1007/s11423-013-9289-2)
- Gibson, D., Ostashewski, N., Flintoff, K., Grant, S., & Knight, E. (2015). Digital badges in education. *Education and Information Technologies, 20*(2), 403–410. [doi:10.1007/s10639-013-9291-7](https://doi.org/10.1007/s10639-013-9291-7)
- Filsecker, M., & Kerres, M. (2014). Engagement as a volitional construct: A framework for evidence-based design of motivational gamification. *On the Horizon, 22*(3), 171–178. [doi:10.1108/OTH-04-2014-0013](https://doi.org/10.1108/OTH-04-2014-0013)
