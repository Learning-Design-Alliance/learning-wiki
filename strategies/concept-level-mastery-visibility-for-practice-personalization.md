---
type: strategy
id: concept-level-mastery-visibility-for-practice-personalization
title: Deploy knowledge-tracing models that expose per-concept mastery levels so platforms can tailor practice and students can target their own gaps
description: The article recommends implementing DKVMN on online learning platforms so tutors can tailor exercise sequences to individual strengths and weaknesses and students can see their own progress.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-26
sources:
  - id: jiani-zhang-2017
    resource: "https://doi.org/10.1145/3038912.3052580"
    title: "Jiani Zhang, Xingjian Shi, Irwin King, Dit-Yan Yeung. (2017). Dynamic Key-Value Memory Networks for Knowledge Tracing. WWW 2017, Perth, Australia. https://doi.org/10.1145/3038912.3052580"
    author: Jiani Zhang, Xingjian Shi, Irwin King, Dit-Yan Yeung
---

# Deploy knowledge-tracing models that expose per-concept mastery levels so platforms can tailor practice and students can target their own gaps

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (4 for, 1 mixed) · 2 studies (1 associational, 1 design), `q2`–`q3` · 0 of 2 report an effect size · 5 claims rest on one study

## Description
The article recommends implementing DKVMN on online learning platforms so tutors can tailor exercise sequences to individual strengths and weaknesses and students can see their own progress. It states the model "can be implemented in online learning platforms to improve the study efficiency of students", and that if students possess concept states pinpointing strengths and weaknesses, "they will be more motivated to fill in the learning gaps independently". The strategy rests on DKVMN's ability to trace each concept state separately rather than summarizing knowledge in one hidden vector.

## Design Implications

### Context
#### Requirements
- A knowledge-tracing model that outputs per-concept mastery levels (DKVMN's value matrix read process), plus a stream of tagged exercise responses per student
#### Constraints
- The motivational and efficiency benefits are the authors' stated expectations, not experimentally tested in this paper

### Target Learners
- students in massive open online courses and intelligent tutoring systems

### Target Learning Goals
- efficient personalized practice and self-directed remediation of weak concepts

### Affordances
- [Dkvmn Key Value Memory Architecture](../theories/deep-learning-knowledge-tracing-models.md)

## Claims

- [DKVMN's correlation weights automatically discover underlying concepts of exercises without expert annotation](../claims/dkvmn-automatic-concept-discovery.md) [+W]
- [DKVMN reaches higher prediction accuracy than DKT with substantially fewer parameters, especially at low state dimensions](../claims/dkvmn-better-accuracy-fewer-parameters.md) [+W]
- [DKVMN can depict a student's changing mastery state of individual concepts over a practice sequence](../claims/dkvmn-knowledge-state-depiction.md) [+W]
- [DKVMN consistently outperforms BKT, DKT and a MANN baseline in knowledge-tracing prediction AUC across four datasets](../claims/dkvmn-outperforms-dkt-mann-bkt-auc.md) [+W]
- [Posttest predictability of all algorithms varies by skill, with all algorithms struggling on Complete the Sequence and mean-DKVMN best on Decimal Addition](../claims/skill-specific-posttest-correlations-vary.md) [~W]

## Related Strategies

- [Knowledge-Tracing-Driven Exercise Recommendation](knowledge-tracing-driven-exercise-recommendation.md)
- [Use traced error causes as personalized intervention recommendations in online learning systems](error-cause-tracing-for-personalized-recommendations.md)

## Examples
-

## Key Sources
- Jiani Zhang, Xingjian Shi, Irwin King, Dit-Yan Yeung. (2017). Dynamic Key-Value Memory Networks for Knowledge Tracing. WWW 2017, Perth, Australia. https://doi.org/10.1145/3038912.3052580
