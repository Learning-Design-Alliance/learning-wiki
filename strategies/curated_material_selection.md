---
type: strategy
title: Curated Material Selection
description: Regularly assessing instructional materials for relevance and currency, discarding broken or obsolete items, and selecting new resources against explicit learning criteria.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Curated Material Selection

## Description
Curated material selection is the ongoing practice of reviewing an instructional resource collection — readings, videos, examples, datasets, tools — against explicit criteria tied to learning goals, and pruning what no longer serves. It treats materials as a maintained portfolio rather than an accumulating archive: items are added because they meet a defined instructional need, and retired when they are outdated, redundant, or misaligned.

## Design Implications

Selection quality directly shapes cognitive load: poorly chosen or redundant materials force learners to discriminate relevant from irrelevant content on their own, imposing extraneous load [Cognitive load management](../principles/cognitive-load-management.md). Curators act as a filter, so learners' attention is directed to what matters [Relevancy of emphasis directs attention.](../claims/relevancy-of-emphasis-directs-attention.md) [+M]. Selection should also match material difficulty to learner expertise, since guidance-rich materials help novices but can become redundant for experts [Guidance effectiveness reverses as learner expertise grows.](../claims/expertise-reversal-effect.md) [~M].

### Context
#### Requirements
- Explicit selection criteria derived from learning goals (alignment, currency, accuracy, cognitive load, accessibility, representation)
- A defined review cycle (e.g., annual audit) with ownership assigned
- Metadata for each item: purpose, prerequisite knowledge, last-verified date
- A retirement process, not just an acquisition process — broken links, obsolete software, and superseded content must be actively removed

#### Constraints
- Over-curation removes productive difficulty: pre-digesting all materials deprives learners of practice in evaluating sources [~M]
- Curator bias narrows the material pool; homogeneous selection reduces the multiple perspectives needed for abstraction from [Case Studies](../elements/case-studies.md) [-M]
- Static curation decays quickly — links break, tools change, and unreviewed collections accumulate obsolete items [-S]
- Highly polished, seductive materials can depress learning when their interesting-but-irrelevant details divert attention from the target content [~S]

#### Implementation Variability
- **Instructor-curated**: a small, tightly aligned set of [Assigned Readings](../elements/assigned-readings.md) chosen each term
- **Co-curated with students**: learners nominate and evaluate candidate materials against shared criteria, building source-evaluation skill
- **Repository-based**: departments maintain shared collections with metadata and review stamps (e.g., OER repositories such as [OER Commons](https://www.oercommons.org) and [MERLOT](https://www.merlot.org))
- **Adaptive**: a larger curated pool from which an [Adaptive Learning](../principles/adaptive-learning.md) system selects per learner

### Target Learners
- Novices, who cannot yet cheaply discriminate relevant from irrelevant material and benefit most from a pre-filtered set [Relevancy of emphasis directs attention.](../claims/relevancy-of-emphasis-directs-attention.md) [+M]
- Learners with high working-memory demands in the domain, for whom redundant or poorly structured materials impose disproportionate load [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+M]
- Advanced learners need less filtering; over-selection of scaffolded material wastes their capacity [Guidance effectiveness reverses as learner expertise grows.](../claims/expertise-reversal-effect.md) [~M]

### Target Learning Goals
- Efficient acquisition of well-structured knowledge (concepts, procedures with canonical treatments)
- Media-complementary goals where text and visuals must work together [Media combinations affect recall and retention.](../claims/media-combinations-affect-recall-and-retention.md) [+M]
- Less suited to open-ended inquiry goals, where a deliberately broad, unfiltered material pool is part of the learning

### Instructions
1. Define selection criteria from the learning goals: alignment, accuracy, currency, load profile, accessibility, and cost.
2. Audit the existing collection against those criteria; retire or flag broken, obsolete, and redundant items.
3. Select or commission replacements, favoring materials that segment content and integrate text with supporting visuals rather than duplicating it [Media combinations affect recall and retention.](../claims/media-combinations-affect-recall-and-retention.md) [+M].
4. Sequence the selected set — order materials from lower to higher complexity and attach [Advance Organizers](../elements/advance-organizers.md) to show how items relate.
5. Record metadata (purpose, prerequisites, verification date) so the next review cycle is fast.
6. Schedule recurring review and gather learner feedback on which materials actually supported learning.

## Related Strategies
- [Chunking](../principles/chunking.md) — selection decisions determine the size and boundaries of the chunks learners encounter
- [Scaffolded Questioning](scaffolded-questioning.md) — curated materials give the questioning sequence something reliable to build on
- [Text Set Construction](text-set-construction.md) — a specific form of curation focused on multiple perspectives on one topic

## Examples
- **[MERLOT](https://www.merlot.org)** — peer-reviewed repository of online teaching materials with user ratings and review metadata, institutionalizing curation criteria.
- **[OER Commons](https://www.oercommons.org)** — open educational resources with alignment metadata and rubric-based evaluation, supporting department-level curation cycles.
- **Newsela** — curates news articles at multiple reading levels, allowing teachers to select the same content calibrated to learner expertise.

## Key Sources
- Mayer, R. E., & Moreno, R. (2003). Nine ways to reduce cognitive load in multimedia learning. *Educational Psychologist, 38*(1), 43–52. [doi:10.1207/s15326985ep3801_6](https://doi.org/10.1207/s15326985ep3801_6)
- Clark, R. C., & Mayer, R. E. (2016). *E-Learning and the Science of Instruction* (4th ed.). Wiley. [doi:10.1002/9781119239086](https://doi.org/10.1002/9781119239086)
- Mayer, R. E. (2009). *Multimedia learning* (2nd ed.). Cambridge University Press.
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (1998). Cognitive architecture and instructional design. *Educational Psychology Review, 10*(3), 251–296. [doi:10.1023/A:1022193728205](https://doi.org/10.1023/A:1022193728205)