---
type: strategy
id: weeding
title: Weeding
description: Systematically removing extraneous words, images, audio, and features from learning materials so that working-memory resources are devoted to essential content.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Weeding

> **Strategy** · [All strategies](index.md)

## Description
Weeding is the deliberate removal of non-essential material — decorative graphics, tangential anecdotes, redundant on-screen text, background music, and unused interface features — from learning materials before delivery. It is carried out by auditing each element of a lesson or screen against the learning objective and deleting anything that does not support it, rather than adding cues or simplifying wording.

## Design Implications

Weeding enacts the coherence principle: extraneous material competes for limited working-memory capacity and measurably depresses learning outcomes [Irrelevant material hurts learning by diverting attention and working memory.](../claims/coherence-principle-irrelevant-material-hurts-learning.md) [+S]. Learners do not reliably ignore seductive details; interesting-but-irrelevant content captures attention and is often encoded at the expense of core content [Cognitive overload degrades learning outcomes.](../claims/cognitive-overload-degrades-learning.md) [+S]. Weeding is a subtraction-first alternative to [Cognitive Load Management](../principles/cognitive-load-management.md): rather than restructuring content, it reduces the total load by cutting it.

### Context
#### Requirements
- An explicit statement of the learning objective, so "essential" is decidable rather than a matter of taste
- Authority to remove or defer content (designers and instructors often resist deleting material they produced)
- A review pass late in development, since extraneous material tends to accumulate during drafting

#### Constraints
- Over-weeding can strip out [Advance Organizers](../elements/advance-organizers.md), analogies, or examples that aid schema building for novices; what is extraneous for an expert may be supportive for a beginner [Guidance effectiveness reverses as learner expertise increases.](../claims/expertise-reversal-effect.md) [~S]
- Removing all narrative or humanizing content can reduce engagement and interest without improving outcomes [Mixed evidence on whether interest-generating details affect retention.](../claims/seductive-details-effect.md) [~M]
- In exploratory or motivational contexts (museums, games), some "extraneous" content serves affective goals that weeding would eliminate [~W]

#### Implementation Variability
- **Pre-delivery weeding**: editing slides, texts, and videos before release (the standard case)
- **Progressive disclosure**: keeping content but hiding it behind links or layers, so it is available on demand rather than deleted
- **Learner-controlled weeding**: teaching students to skim and prioritize — a study-skills variant rather than a design variant
- **Interface weeding**: removing unused menu items, toolbars, and notifications from digital learning environments

### Target Learners
- Novices, who lack the prior knowledge to filter irrelevant from essential material and are most harmed by extraneous load [Irrelevant material hurts learning by diverting attention and working memory.](../claims/coherence-principle-irrelevant-material-hurts-learning.md) [+S]
- Learners with limited working-memory capacity or reading proficiency, for whom every competing element carries a higher cost
- Less critical for experts, who can filter efficiently and may find stripped-down materials under-informative [Guidance effectiveness reverses as learner expertise increases.](../claims/expertise-reversal-effect.md) [~M]

### Target Learning Goals
- Retention and comprehension of core concepts and procedures
- Efficient procedural learning where steps must be held in working memory
- Less suited to goals where breadth, exploration, or motivation are primary outcomes

### Instructions
1. Write the learning objective in observable terms; list every element currently in the material ([Clear Structure](../principles/clear-structure.md)).
2. For each element, ask: does it support the objective, or only interest, decoration, or completeness? Delete or move anything in the latter category.
3. Remove redundant channels — e.g., narrating text that is also displayed verbatim [Redundant on-screen text with narration impairs learning.](../claims/redundancy-principle.md) [+S].
4. Strip decorative graphics and background audio that do not explain content [Irrelevant material hurts learning by diverting attention and working memory.](../claims/coherence-principle-irrelevant-material-hurts-learning.md) [+S].
5. Check the result against learner prior knowledge: restore supportive elements ([Analogies](analogies.md), advance organizers) that novices need but experts would not.
6. Pilot with target learners and verify that comprehension of essential content is intact before full release.

## Related Strategies
- [Signaling](signaling.md) — the additive complement: when content cannot be cut, cue attention to essentials instead
- [Segmenting](segmenting.md) — breaks remaining essential content into learner-paced pieces
- [Simplifying Language](simplifying-language.md) — weeding applied at the sentence level rather than the material level
- [Chunking](../principles/chunking.md) — organizes what remains after weeding into digestible units

## Examples
- **Mayer's coherence experiments** — removing interesting-but-irrelevant video clips about lightning formation from a multimedia lesson improved retention and transfer; the same pattern held across dozens of replications (see Clark & Mayer, 2016).
- **[Khan Academy](https://www.khanacademy.org)** videos — deliberately spare visuals: a single problem, a writing surface, and narration, with no decorative imagery.
- **Slide redesign in corporate e-learning** — replacing text-heavy, clip-art-decorated slides with one visual and minimal text per screen, per the [coherence and redundancy principles](../claims/coherence-principle-irrelevant-material-hurts-learning.md).

## Key Sources
- Mayer, R. E. (2021). *Multimedia learning* (3rd ed.). Cambridge University Press. [doi:10.1017/9781316941355](https://doi.org/10.1017/9781316941355)
- Clark, R. C., & Mayer, R. E. (2016). *E-Learning and the Science of Instruction* (4th ed.). Wiley. [doi:10.1002/9781119239086](https://doi.org/10.1002/9781119239086)
- Mayer, R. E., Heiser, J., & Lonn, S. (2001). Cognitive constraints on multimedia learning: When presenting more material results in less understanding. *Journal of Educational Psychology, 93*(1), 187–198. [doi:10.1037/0022-0663.93.1.187](https://doi.org/10.1037/0022-0663.93.1.187)
- Harp, S. F., & Mayer, R. E. (1998). How seductive details do their damage: A theory of cognitive interest in science learning. *Journal of Educational Psychology, 90*(3), 414–434. [doi:10.1037/0022-0663.90.3.414](https://doi.org/10.1037/0022-0663.90.3.414)
- Sweller, J., Ayres, P., & Kalyuga, S. (2011). *Cognitive load theory*. Springer. [doi:10.1007/978-1-4419-8126-4](https://doi.org/10.1007/978-1-4419-8126-4)