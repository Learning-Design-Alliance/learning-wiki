---
type: strategy
title: Leaderboards
description: Leaderboards showcase the distribution of point totals that learners have accumulated through various learning activities, leveraging competition to drive engagement.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Leaderboards

## Description
Leaderboards rank learners by points accumulated through learning activities such as quizzes, discussions, or practice sets, providing a visible representation of relative progress. They are a core gamification mechanic: competition can motivate some learners, but full public ranking can demoralize those at the bottom. A common mitigation is a "relative" leaderboard in which each learner sees only the participants directly above and below them, reframing the display as actionable next steps rather than a verdict on ability.

## Design Implications

Leaderboards operate on competitive and achievement-based motivation, which reliably increases engagement with the *activity* but does not automatically increase learning of the *content* [~M]. Meta-analytic evidence on gamification shows significant positive cognitive, motivational, and behavioral effects on average, but with substantial heterogeneity driven by design and context [Sailer & Homner meta-analysis](https://doi.org/10.1007/s10648-019-09498-w) [+M]. Because points are outcome-oriented, leaderboards can pull attention away from mastery; for novices, process goals tend to outperform outcome goals [Process goals outperform outcome goals for novices.](../claims/process-goals-outperform-outcome-goals-for-novices.md) [+M]. Design should therefore reward controllable behaviors (attempts, revisions, streaks of practice) rather than raw rank alone.

### Context
#### Requirements
- Digital tools to track and display scores transparently and accurately
- Clear, published criteria for how points are earned, so the leaderboard reflects valued learning behaviors rather than gaming the metric
- Careful monitoring to ensure fair competition and to catch disengagement among low-ranked learners
- A feedback channel so rankings connect to [Feedback](../elements/provide-feedback.md) about *what to improve*, not just where one stands

#### Constraints
- Full public ranking is a disincentive for learners at the bottom; visible low rank can depress self-efficacy, which predicts persistence [Self-efficacy predicts academic persistence.](../claims/self-efficacy-predicts-academic-persistence.md) [-M]
- Competition can crowd out intrinsic motivation when learners perceive the reward as the point [Autonomy supports intrinsic motivation.](../claims/autonomy-supports-intrinsic-motivation.md) [-M] — a field study found a leaderboard course section produced lower intrinsic motivation, satisfaction, and exam performance than a non-gamified section [Hanus & Fox (2015)](https://doi.org/10.1016/j.compedu.2014.08.019) [-M]
- Points for volume (posts, logins) can shift focus from learning to point accumulation [-M]
- Effects fade over time; novelty-driven engagement gains often decay after a few weeks [~W]

#### Implementation Variability
- **Relative leaderboards**: each learner sees only the two adjacent ranks, converting the display into an attainable next target
- **Team leaderboards**: aggregate scores across small groups, adding accountability while shielding individuals from public bottom-rank exposure
- **Multiple boards**: separate rankings for effort, improvement, and accuracy so different learners can appear at the top
- **Opt-in or private ranking**: learners see their own percentile without a public list, preserving progress visibility without social comparison
- **Resetting periods**: weekly or unit-level resets keep entry points attainable for late starters

### Target Learners
- Learners motivated by competition and social comparison, typically those with moderate-to-high self-efficacy [+W]
- Learners who benefit from a concrete visual representation of progress toward goals [Task value increases motivation and engagement.](../claims/task-value-increases-motivation-and-engagement.md) [+M]
- Use caution with learners sensitive to competition, low-performing students, and those with low self-efficacy, for whom visible bottom ranks can be actively harmful [-M]

### Target Learning Goals
- Engagement and participation in routine practice activities (drills, quizzes, discussion)
- Behavioral persistence: sustaining regular engagement over a course or term
- Not well suited to deep conceptual learning or creative work, where quality resists point quantification [~M]

### Instructions
1. Define the behaviors worth rewarding and publish transparent point criteria, tied to [Assess Performance](../elements/assess-performance.md)
2. Award points for controllable, learning-relevant actions (completing practice, revising after [Feedback](../elements/provide-feedback.md)) rather than raw speed or volume
3. Choose a display mode — full, relative, team, or private — based on your learners' sensitivity to social comparison
4. Pair every ranking with actionable feedback so learners know *what to do next*, not just where they stand
5. Monitor participation and outcomes, and gather learner feedback on the leaderboard's motivational impact; retire or restructure it if it demotivates a segment of the class

## Related Strategies
- Badges and achievements — complementary gamification mechanics that reward milestones without public ranking
- Streaks and daily goals — reward consistency rather than relative standing
- Team-based competition — shifts comparison from individual to group level

## Related Elements
- [Assess Performance](../elements/assess-performance.md) — the scoring mechanism that feeds the leaderboard
- [Provide Feedback](../elements/provide-feedback.md) — rankings must connect to improvement information to support learning rather than mere competition

## Examples
- **[Khan Academy](https://www.khanacademy.org)** — energy-point totals and avatar badges reward practice volume; points accrue from exercises and videos rather than public rank alone
- **[Duolingo](https://www.duolingo.com)** — weekly leagues place each learner in a small cohort of ~30, an implementation of the relative-leaderboard design that limits visible comparison range
- **[Kahoot!](https://kahoot.com)** — post-quiz leaderboards display top five scorers after each question, using short-lived, low-stakes competition within a single session
- A discussion forum leaderboard showing most active participants — effective only if activity criteria reward substantive contribution rather than post count

## Key Sources
- Sailer, M., & Homner, L. (2020). The gamification of learning: A meta-analysis. *Educational Psychology Review, 32*(1), 77–112. [doi:10.1007/s10648-019-09498-w](https://doi.org/10.1007/s10648-019-09498-w)
- Hanus, M. D., & Fox, J. (2015). Assessing the effects of gamification in the classroom: A longitudinal study on intrinsic motivation, social comparison, satisfaction, effort, and academic performance. *Computers & Education, 80*, 152–161. [doi:10.1016/j.compedu.2014.08.019](https://doi.org/10.1016/j.compedu.2014.08.019)
- Domínguez, A., Saenz-de-Navarrete, J., de-Marcos, L., Fernández-Sanz, L., Pagés, C., & Martínez-Herráiz, J.-J. (2013). Gamifying learning experiences: Practical implications and outcomes. *Computers & Education, 63*, 380–392. [doi:10.1016/j.compedu.2012.12.034](https://doi.org/10.1016/j.compedu.2012.12.034)
- Deterding, S., Dixon, D., Khaled, R., & Nacke, L. (2011). From game design elements to gamefulness: Defining "gamification." *Proceedings of the 15th International Academic MindTrek Conference*, 9–15. [doi:10.1145/2181037.2181040](https://doi.org/10.1145/2181037.2181040)
- Hamari, J., Koivisto, J., & Sarsa, H. (2014). Does gamification work? A literature review of empirical studies on gamification. *Proceedings of the 47th Hawaii International Conference on System Sciences*, 3025–3034. [doi:10.1109/HICSS.2014.377](https://doi.org/10.1109/HICSS.2014.377)