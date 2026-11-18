---
type: design
id: percs-sequential-email-trial
title: "PERCS: a sequentially randomized factorial email-reminder trial in the Applied Data Science with Python MOOC"
description: PERCS (Problem-based Email Reminder Coursera Study) was an SRT in the Applied Data Science with Python Coursera MOOC in which, at the end of weeks one, two, and three of the four-week course, learners were randomly as...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
sources:
  - id: timothy-necamp-2019
    resource: "https://arxiv.org/abs/1810.11185"
    title: "Timothy NeCamp, Josh Gardner, Christopher Brooks. (2019). Beyond A/B Testing: Sequential Randomization for Developing Interventions in Scaled Digital Learning Environments. arXiv. https://arxiv.org/abs/1810.11185"
    author: Timothy NeCamp, Josh Gardner, Christopher Brooks
---

# PERCS: a sequentially randomized factorial email-reminder trial in the Applied Data Science with Python MOOC

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
PERCS (Problem-based Email Reminder Coursera Study) was an SRT in the Applied Data Science with Python Coursera MOOC in which, at the end of weeks one, two, and three of the four-week course, learners were randomly assigned to a cultural problem email, a global problem email, no-problem email, or no email, with emailed conditions crossed with growth mindset framing — a 2 × 3 factorial design plus control each week. "A total of 8,681 unique learners (3,455 Indian, 5,226 US) were sent 22,073 emails", and because randomizations across weeks are independent, "there are 73 different possible email sequences students may receive". Emails used a cut-and-paste template so effects could be attributed to the added condition.

## Design Implications

### Context
#### Requirements
- Email delivery via the Coursera platform's instructor email capabilities, which the article notes does not support fully-automated scheduled delivery
#### Constraints
- Focused on Indian and US-based learners determined by IP address; about 10% of users retook the course and were repeated in multiple trial iterations; exploratory, not confirmatory

### Target Learners
- Indian and US-based learners in a data science MOOC

### Learning Goals
- course engagement and retention via weekly reminder emails

### Claims
- [Percs Sequence Effects Suggestive Us Week1 Email Benefit](../claims/percs-sequence-effects-suggestive-us-week1-email-benefit.md) [+M]
- [Percs Timing Email Effects Country Week](../claims/percs-timing-email-effects-country-week.md) [+M]
- [Percs Activity Moderation Sign Switch](../claims/percs-activity-moderation-sign-switch.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Timothy NeCamp, Josh Gardner, Christopher Brooks. (2019). Beyond A/B Testing: Sequential Randomization for Developing Interventions in Scaled Digital Learning Environments. arXiv. https://arxiv.org/abs/1810.11185
