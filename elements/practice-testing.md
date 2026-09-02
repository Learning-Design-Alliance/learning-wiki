---
type: element
id: practice-testing
title: Practice Testing
description: Learners actively retrieve information from memory as a learning activity, rather than rereading or reviewing material.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Practice Testing

> **Element** · [All elements](index.md)

## Description
Practice testing (retrieval practice) asks learners to recall or apply information from memory — via low- or no-stakes quizzes, flashcards, free recall, or problem-solving — before or instead of restudying. The act of successful retrieval itself strengthens memory and reveals gaps, making testing a learning event rather than merely an assessment event.

## Design Implications

Retrieval practice produces substantially larger and more durable learning gains than restudying or elaborative review at equivalent time on task [Dunlosky et al. rated practice testing among the highest-utility learning techniques.](https://doi.org/10.1177/1529100612453266) [+S]. Its benefits depend on retrieval actually occurring: feedback after incorrect retrieval is essential, and tests that learners cannot answer at all yield little benefit. Spacing repeated tests over time multiplies the effect relative to massed testing.

### Context
#### Requirements
- Questions that require genuine retrieval (recall, application), not recognition of recently seen text
- Feedback or answer-checking so errors are corrected rather than consolidated
- Sufficient delay between study and test that retrieval is effortful but achievable — "desirable difficulty"
- Repeated retrieval opportunities distributed over time ([Spaced Practice](../principles/spaced-practice.md) where available)

#### Constraints
- Testing before any instruction produces weak or negative effects when retrieval failure rates are high [~M] — pretesting helps mainly when learners can make plausible partial attempts
- Repeated immediate testing of the same item in one session (massed retrieval) adds little beyond the first successful recall [~S]
- Simple recognition formats (multiple choice with short exposure) can encourage cue-based guessing rather than retrieval [-W]
- High-stakes use shifts the function from learning to evaluation and can induce anxiety that offsets gains [~M]

### Target Learners
- Benefits are remarkably broad across ages and subject domains, including young children and learners with low prior knowledge [Rowland's meta-analysis found robust effects across ability levels.](https://doi.org/10.1037/a0035056) [+S]
- Learners prone to illusions of fluency from rereading benefit most, because testing corrects metacognitive miscalibration [~S]
- Learners with high test anxiety need low-stakes framing to capture the benefit without the cost

### Target Learning Goals
- Retention of factual and conceptual knowledge over delays of weeks to months
- Transfer and inference: retrieval practice improves application to new questions better than restudying [Karpicke & Blunt found retrieval outperformed concept mapping for meaningful learning.](https://doi.org/10.1126/science.1199327) [+S]
- Metacognitive accuracy: calibrating judgments of what is and is not yet known

### Affordances
- [Assessment for Learning](../principles/assessment-for-learning.md) — low-stakes testing is the core mechanism: it generates evidence about learning while simultaneously producing learning
- [Cognitive Load Management](../principles/cognitive-load-management.md) — successful retrieval consolidates information so it no longer competes for working memory, freeing capacity for harder material
- [Spacing and Distributed Practice](../principles/spaced-practice.md) — tests are natural spacing events; scheduling retrieval at expanding intervals compounds the testing effect
- [Self-Regulated Learning](../theories/self-regulated-learning.md) — self-testing gives learners accurate feedback on their own state of knowledge, driving better study decisions

## Related Elements
- [Practice](practice.md) — practice testing is the memory-focused subset of practice; both depend on active production rather than review
- [Feedback](feedback.md) — corrects errors surfaced by retrieval; testing without feedback risks consolidating mistakes
- [Spaced Repetition](spaced-repetition.md) — schedules the retrieval events that maximize retention
- [Formative Assessment](formative-assessment.md) — the instructional pattern built on low-stakes checking

## Patterns That Use This Element
- [Direct Instruction](../patterns/direct-instruction.md) — frequent checks for understanding function as embedded retrieval practice
- [Mastery Learning](../patterns/mastery-learning.md) — repeated testing with feedback until criterion is met
- [Gagné's 9 Events](../patterns/gagnés-9-events-of-instruction.md) — "eliciting performance" and "assessing performance" events

## Examples

**[Anki](https://apps.ankiweb.net)** — Spaced-repetition flashcard software that schedules retrieval at expanding intervals; the canonical implementation of combined testing and spacing.

**[Khan Academy](https://www.khanacademy.org)** — Mastery-tracking exercise sets that require repeated successful retrieval across sessions before a skill is marked complete.

**[Retrieval Practice Guide](https://www.retrievalpractice.org)** — Agarwal and Bain's practitioner resource with classroom routines (brain dumps, two-things exit tickets) implementing free-recall testing.

**[Quizlet](https://quizlet.com)** — Self-testing tools (Learn and Test modes) that convert study sets into retrieval trials with feedback.

## Key Sources
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. [doi:10.1111/medu.12141](https://doi.org/10.1111/medu.12141)
- Karpicke, J. D., & Blunt, J. R. (2011). Retrieval practice produces more learning than elaborative studying with concept mapping. *Science, 331*(6018), 772–775. [doi:10.1126/science.1199327](https://doi.org/10.1126/science.1199327)
- Rowland, C. A. (2014). The effect of testing versus restudy on retention: A meta-analytic review of the testing effect. *Psychological Bulletin, 140*(6), 1432–1463. [doi:10.1037/a0037559](https://doi.org/10.1037/a0037559)
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest, 14*(1), 4–58. [doi:10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)