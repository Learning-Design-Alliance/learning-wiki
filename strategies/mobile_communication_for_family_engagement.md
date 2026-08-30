---
type: strategy
title: Mobile Communication for Family Engagement
description: Utilizing text messages to inform families about their student's progress, as well as general tips for supporting children's learning.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Mobile Communication for Family Engagement

## Description
Mobile communication for family engagement uses SMS text messaging (and similar low-friction channels) to send families timely information about their student's progress, attendance, and behavior, along with concrete tips for supporting learning at home. Because texts require no app, login, or broadband connection, they reach families that newsletters, portals, and conferences often miss. Effectiveness depends on message design: personalized, actionable, and translated messages outperform generic broadcasts.

## Design Implications

Texting works because it lowers the cost of the school-to-family information flow, reducing the "information frictions" that keep parents from acting on their child's needs [Bergman & Chan's texting intervention raised ELA achievement by reducing parent information gaps.](https://doi.org/10.3368/jhr.58.1.0918-9761R1) [+M]. Messages function as a form of [Feedback](../elements/feedback.md) delivered to the family rather than the student, and are most useful when they specify what to do next, not just how the child is doing [Feedback most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S].

### Context
#### Requirements
- A messaging platform (e.g., Remind, TalkingPoints, ClassDojo) with current, verified family contact information
- Translation and, where possible, two-way messaging in families' home languages; TalkingPoints and similar tools provide automated translation
- Message content that is specific (named student, named behavior or assignment) and actionable (one concrete step families can take)
- Consent and clear opt-in/opt-out handling; awareness of text costs for prepaid plans

#### Constraints
- Generic, one-size-fits-all broadcasts show weak or null effects; personalization and actionability drive outcomes [Kraft & Rogers found personalized, student-specific texts increased parent response rates far more than generic ones.](https://doi.org/10.3102/0013189X15589581) [+M]
- Families without reliable phone access, with shared phones, or with distrust of school contact may be unreachable or opt out; texting cannot substitute for relationship-building
- Over-messaging causes fatigue and opt-outs; effects attenuate when frequency is high and content is redundant [~M]
- Messages that place heavy literacy or time demands on families (e.g., "tutor your child in fractions") are less feasible than low-effort prompts (attendance reminders, "ask what she read today")

#### Implementation Variability
- **Progress/attendance alerts:** automated, triggered by data (missing work, absences); scalable but least personal
- **Teacher-sent personalized texts:** higher impact per message on engagement and trust [Kraft & Dougherty found teacher-frequent texting increased student engagement and homework completion.](https://doi.org/10.1080/19345747.2013.794840) [+M] but costs teacher time
- **Learning tips ("text nudges"):** short, curriculum-aligned suggestions for home activities, as in York & Loeb's kindergarten literacy texting program [+M]
- **Two-way messaging:** families can reply, ask questions, and flag problems, converting broadcast into [Coaching](../elements/coaching.md) and enabling [Check-ins](../principles/check-ins.md)

### Target Learners
- Families of K–12 students, with the strongest documented effects for early-grades literacy and middle-grades engagement
- Low-income families and families of color, who are disproportionately reached by text where portals and conferences underperform [Bergman & Chan's texting intervention raised ELA achievement by reducing parent information gaps.](https://doi.org/10.3368/jhr.58.1.0918-9761R1) [+M]
- Multilingual families, when messages are translated into home languages
- Families of students with low [Self-efficacy](../claims/self-efficacy-predicts-academic-persistence.md) — regular progress messages can build a sense of efficacy and persistence for both parent and child [+W]

### Target Learning Goals
- Attendance, homework completion, and engagement behaviors
- Home literacy and numeracy practice in early grades
- Family awareness of progress and of concrete support actions — a form of [Assessment for Learning](../principles/assessment-for-learning.md) aimed at the family unit

### Instructions
1. **Collect and verify contacts** at enrollment; record preferred language and confirm consent for SMS.
2. **Choose a platform** with translation and two-way capability (e.g., TalkingPoints, Remind).
3. **Segment audiences** — grade level, language, current student needs — rather than sending school-wide blasts.
4. **Draft message templates** that pair one piece of student-specific information with one actionable step ([Provide guidance](../elements/provide-guidance.md)).
5. **Personalize before automating:** merge student names, specific assignments, or specific behaviors into every message [Kraft & Rogers found personalized, student-specific texts increased parent response rates far more than generic ones.](https://doi.org/10.3102/0013189X15589581) [+M]
6. **Set a sustainable cadence** (e.g., weekly progress plus event-triggered alerts) and monitor opt-out rates.
7. **Enable and respond to replies**, using two-way exchange for [Check-ins](../principles/check-ins.md) and relationship-building ([Provide feedback](../elements/feedback.md)).
8. **Evaluate:** track attendance, homework completion, and achievement alongside family survey feedback; A/B test message formats where feasible.

## Related Strategies
- Positive phone calls and personalized teacher outreach — the high-touch sibling of texting; combining both channels leverages text's reach with voice's relational depth
- Home literacy activity programs — texting is a delivery mechanism for these; York & Loeb's kindergarten program embedded weekly literacy tips in texts

## Examples
- **[TalkingPoints](https://www.talkingpts.org)** — two-way translated family messaging used widely in U.S. districts; families and teachers exchange texts in their own languages.
- **[Remind](https://www.remind.com)** — mass texting platform for class announcements and progress updates.
- **York & Loeb kindergarten texting program (San Francisco)** — weekly texts with literacy activities for parents produced measurable gains in early literacy outcomes [+M].
- **Bergman & Chan's ELA texting intervention (West Sacramento)** — high-frequency, personalized texts about missing work and progress raised ELA achievement, with the largest gains for previously low-achieving students [+M].

## Key Sources
- Kraft, M. A., & Dougherty, S. M. (2013). The effect of teacher–family communication on student engagement: Evidence from a randomized field experiment. *Journal of Research on Educational Effectiveness, 6*(3), 199–222. [doi:10.1080/19345747.2012.743636](https://doi.org/10.1080/19345747.2012.743636)
- Kraft, M. A., & Rogers, T. (2015). The underutilized potential of teacher-to-parent communication: Evidence from a field experiment. *Educational Researcher, 44*(5), 263–274. [doi:10.2139/ssrn.2528688](https://doi.org/10.2139/ssrn.2528688)
- Bergman, P., & Chan, E. W. (2021). Leveraging parents through low-cost technology: The impact of high-frequency information on student achievement. *Journal of Human Resources, 58*(1), 180–215. [doi:10.3368/jhr.56.1.1118-9837r1](https://doi.org/10.3368/jhr.56.1.1118-9837r1)
- York, B. N., & Loeb, S. (2014). One step at a time: The effects of an early literacy text messaging program for parents of preschoolers. *NBER Working Paper No. 20659.* [doi:10.3386/w20659](https://doi.org/10.3386/w20659)
