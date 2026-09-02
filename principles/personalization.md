---
type: principle
id: personalization
title: Personalization
description: Personalization adapts content, pacing, difficulty, or context to individual learners' prior knowledge, needs, or interests rather than delivering a uniform experience to all.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Personalization

> **Principle** · [All principles](index.md)

## Description
Personalization tailors instruction to individual learners — adjusting pacing, task difficulty, content sequencing, or the context of problems to match prior knowledge, skill level, or interests. It ranges from learner-directed choice (topics, pathways) to system-directed adaptation (intelligent tutoring, adaptive difficulty). The core recommendation: replace one-size-fits-all instruction with experiences calibrated to where each learner actually is.

## Implications

Personalization works primarily by keeping instruction within each learner's zone of productive difficulty — reducing overload for struggling learners and redundancy for advanced ones [Adaptive guidance improves learning relative to fixed instruction.](../claims/expertise-reversal-effect.md) [~M]. Adaptive tutoring systems that individualize step-level support approach the effectiveness of human tutoring [Adaptive tutoring approaches human tutoring effectiveness.](../claims/example-problem-sequences-reduce-cognitive-load.md) [~W], and embedding personal interests into problem contexts can raise performance in mathematics [Personalizing problem contexts to learner interests improves performance.](../claims/contingent-scaffolding-improves-learning.md) [+M]. Offering meaningful choice also boosts intrinsic motivation and effort [Autonomy supports intrinsic motivation.](../claims/autonomy-supports-intrinsic-motivation.md) [+S]. However, personalization is not uniformly beneficial: adapting to purported "learning styles" has no empirical support [Teaching to learning styles does not improve outcomes.](../claims/intuitive-learners-outperform-sensing-learners.md) [X], and excessive choice can overwhelm novices who lack the knowledge to select productively [~M].

### Context
#### Requirements
- Reliable information about learner state — prior knowledge, current performance, or interests ([Assessment](../elements/assessment.md), [Check-in](../elements/check-in.md), or diagnostic tasks); adaptation without accurate diagnosis is guesswork
- A mechanism for adjustment ([Adaptive Difficulty](../elements/adaptive-difficulty.md), [Adaptive Mastery Learning](../elements/adaptive-mastery-learning.md), or [Choice Boards](../elements/choice-boards.md)) — the system or teacher must be able to act on the diagnostic information
- Shared learning goals across personalized paths — personalization of *how* and *when*, not of *what* counts as mastery, keeps outcomes comparable
- Progress monitoring ([Assessment for Learning](assessment-for-learning.md)) so adaptation responds to evidence rather than self-report alone

#### Constraints
- Adapting to self-reported learning styles is ineffective and wastes design effort [Teaching to learning styles does not improve outcomes.](../claims/intuitive-learners-outperform-sensing-learners.md) [X]
- Unstructured learner choice can reduce learning when novices choose tasks beyond their competence or avoid challenge [~M]
- Personalization that fragments a cohort can undermine [Collaborative Learning](collaborative-learning.md) and shared discussion
- Over-adapted scaffolds can trigger expertise reversal — support that helped novices becomes redundant and harmful as competence grows [Adaptive guidance improves learning relative to fixed instruction.](../claims/expertise-reversal-effect.md) [~M]
- Adaptive systems risk narrowing exposure: learners are routed around content they need but did not request

### Target Learners
- Heterogeneous groups with wide prior-knowledge variance, where a single fixed pace fits almost no one
- Struggling learners who need [Accommodations](../elements/accommodations.md) and additional scaffolding to access the same goals
- Advanced learners who disengage when instruction repeats what they already know
- Young or novice learners benefit less from open choice; older learners with metacognitive skill benefit more [Autonomy supports intrinsic motivation.](../claims/autonomy-supports-intrinsic-motivation.md) [~M]

### Target Learning Objectives
- Mastery of procedural and conceptual skills with clear proficiency criteria
- Closing prerequisite gaps before new material ([Activation](activation.md) of prior knowledge)
- Sustained engagement and persistence in extended learning sequences
- Self-regulated learning, when learners co-direct their pathways ([Self-Regulated Learning](../theories/self-regulated-learning.md))

### Theory
#### Supporting
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) — adapting difficulty to expertise keeps intrinsic load manageable and avoids the expertise reversal effect
- [Self-Determination Theory](../theories/self-determination-theory.md) — choice and autonomy-supportive personalization raise intrinsic motivation and persistence
- [Information Processing Theory](../theories/information-processing-theory.md) — matching instruction to prior knowledge ensures new information connects to existing schemas
- [Self-Regulated Learning](../theories/self-regulated-learning.md) — personalized pathways with monitoring support adaptive control of effort and strategy

#### Contradicting / Qualifying
- [Constructivism](../theories/constructivism.md) — qualifies rather than contradicts: personalization of *path* must not become personalization of *standards*; learners still need generative, effortful processing that adaptive easing can inadvertently remove

### Claims
- [Autonomy supports intrinsic motivation.](../claims/autonomy-supports-intrinsic-motivation.md) [+S] — meaningful choice raises motivation and effort
- [Adaptive guidance improves learning relative to fixed instruction.](../claims/expertise-reversal-effect.md) [~M] — adaptation must track growing expertise or it backfires
- [Personalizing problem contexts to learner interests improves performance.](../claims/contingent-scaffolding-improves-learning.md) [+M] — interest-based personalization of problem contexts improves math performance
- [Teaching to learning styles does not improve outcomes.](../claims/intuitive-learners-outperform-sensing-learners.md) [X] — style-matched instruction is a discredited form of personalization
- [Contingent scaffolding improves learning.](../claims/contingent-scaffolding-improves-learning.md) [+M] — support calibrated to learner state outperforms fixed support

## Related Principles
- [Adaptive Learning](adaptive-learning.md) — the system-driven end of the personalization spectrum, where algorithms adjust difficulty and sequencing
- [Cognitive Load Management](cognitive-load-management.md) — personalization is one of the main levers for keeping load within each learner's capacity
- [Assessment for Learning](assessment-for-learning.md) — supplies the diagnostic evidence on which any personalization depends
- [Activation](activation.md) — diagnosing and engaging prior knowledge is the first step in deciding what to personalize

## Examples

### Validated
- [Contingent scaffolding improves learning.](../claims/contingent-scaffolding-improves-learning.md) [+M] — Walkington (2013) personalized algebra word problems to individual learners' out-of-school interests (sports, music, gaming) and found improved performance relative to standard contexts, with the largest gains for struggling learners.

### Illustrative

**[Adaptive Learning](../patterns/adaptive-learning.md)** — Platform-driven personalization in which item difficulty and sequencing adjust continuously to response accuracy and latency. Used at scale in mathematics and language learning; effectiveness depends on mastery gating rather than mere content variety.

**[ASSISTments](https://www.assistments.org)** — Free web-based math platform (grades 6–12) that routes students through problem sets with step-level hints and immediate feedback, effectively personalizing the support each student receives during [practice](../elements/practice.md).

**[Khan Academy](https://www.khanacademy.org)** — Mastery-based personalization: learners progress through skill maps at their own pace, with the system recommending review of prerequisite skills when gaps are detected. Widely used in flipped and blended classrooms.

**[Choice Boards](../elements/choice-boards.md)** — A teacher-designed personalization pattern: learners select from a curated set of tasks aligned to the same objective, allowing choice of modality or topic while preserving common outcomes. Works best when all options are genuinely equivalent in rigor.

**[Carnegie Learning MATHia](https://www.carnegielearning.com/solutions/math/mathia/)** — Intelligent tutoring system that models each learner's knowledge at the skill level and personalizes problem selection and hint delivery, gating advancement on demonstrated mastery.

**[Duolingo](https://www.duolingo.com)** — Language-learning app that personalizes review scheduling (spaced repetition of items the individual learner has struggled with) and adapts session difficulty; a consumer-scale example of adaptive item selection.

## Key Sources
- VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist, 46*(4), 197–221. [doi:10.1080/00461520.2011.611369](https://doi.org/10.1080/00461520.2011.611369)
- Walkington, C. (2013). Using adaptive learning technologies to personalize instruction to student interests: The impact of relevant contexts on performance and learning outcomes. *Journal of Educational Psychology, 105*(4), 932–945. [doi:10.1037/a0031882](https://doi.org/10.1037/a0031882)
- Patall, E. A., Cooper, H., & Robinson, J. C. (2008). The effects of choice on intrinsic motivation and related outcomes: A meta-analysis of research findings. *Psychological Bulletin, 134*(2), 270–300. [doi:10.1037/0033-2909.134.2.270](https://doi.org/10.1037/0033-2909.134.2.270)
- Pashler, H., McDaniel, M., Rohrer, D., & Bjork, R. (2008). Learning styles: Concepts and evidence. *Psychological Science in the Public Interest, 9*(3), 105–119. [doi:10.1111/j.1539-6053.2009.01038.x](https://doi.org/10.1111/j.1539-6053.2009.01038.x)
- Pane, J. F., Steiner, E. D., Baird, M. D., & Hamilton, L. S. (2015). Continued progress: Promising evidence on personalized learning. *RAND Corporation*. [https://www.rand.org/pubs/research_reports/RR1365.html](https://www.rand.org/pubs/research_reports/RR1365.html) [doi:10.7249/rr1365](https://doi.org/10.7249/rr1365)
