---
type: claim
title: Most students submitted JoLs out of curiosity about the system rating, often without attending to the LA graphs, and reported behaviour change more from JoL than from the agent
description: Most students submitted JoLs out of curiosity about the system rating, often without attending to the LA graphs, and reported behaviour change more from JoL than from the agent
id: self-reported-jol-motivation-and-behaviour-change
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
newest_evidence: 2026
sources:
  - id: graf-2026
    resource: "https://doi.org/10.1007/s10639-026-14082-1"
    title: "Graf, L., Bassner, P., Anzinger, M., Dietrich, F., Krusche, S., & Poquet, O. (2026). Interactive learning dashboards: rethinking learning visualisations as engagement tools. Education and Information Technologies. https://doi.org/10.1007/s10639-026-14082-1"
    author: "Graf, L., Bassner, P., Anzinger, M., Dietrich, F., Krusche, S., & Poquet, O."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: graf-2026-2
    resource: "https://doi.org/10.1007/s10639-026-14082-1"
    title: "Graf, L., Bassner, P., Anzinger, M., Dietrich, F., Krusche, S., & Poquet, O. (2026). Interactive learning dashboards: rethinking learning visualisations as engagement tools. Education and Information Technologies. https://doi.org/10.1007/s10639-026-14082-1"
    author: "Graf, L., Bassner, P., Anzinger, M., Dietrich, F., Krusche, S., & Poquet, O."
    q: 2
    i: 3
    kind: causal
    rigour: 1
---

# Most students submitted JoLs out of curiosity about the system rating, often without attending to the LA graphs, and reported behaviour change more from JoL than from the agent

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1`–`r2` · `q2` · `i3` large
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person
> **Design limits** · Graf 2026: no comparison group · Graf 2026 (2): no comparison group (read from the study by two models, 2026-10-25)

## Subclaims
`q2 i?` 83% of participants reported submitting their JoL out of curiosity to see the system's rating, and 70% did not actively attend to the LA metrics when judging. [→ Graf 2026](#graf-2026)
`q2 i3` The number of messages students wrote was positively correlated with their mean mastery score (r = 0.47, p = 0.04) and negatively correlated with self-reported tendencies to work on non-graded exercises (r = −0.59, p = 0.008). [→ Graf 2026 (2)](#graf-2026-2)

## Evidence

### Graf 2026

Graf, L., Bassner, P., Anzinger, M., Dietrich, F., Krusche, S., & Poquet, O. (2026). Interactive learning dashboards: rethinking learning visualisations as engagement tools. Education and Information Technologies. https://doi.org/10.1007/s10639-026-14082-1

`q2 · i?` · `causal · r2`

Post-deployment self-report survey of the thirty participants validated the design choice of hiding analytics before JoL submission; "70% of participants did not actively pay attention to the LA metrics on the dashboard when judging their learning". Students reported more reflection from the LLM feature (78%) than the JoL feature (68%), and 79% reported behaviour change after judging versus 47% due to agent interactions.

> "Indeed, 83% of the participants reported they were curious to learn how the system rated them and submitted their JoL to see the system's rating."

### Graf 2026 (2)

Graf, L., Bassner, P., Anzinger, M., Dietrich, F., Krusche, S., & Poquet, O. (2026). Interactive learning dashboards: rethinking learning visualisations as engagement tools. Education and Information Technologies. https://doi.org/10.1007/s10639-026-14082-1

`q2 · i3` · `causal · r1`

Correlational analysis of pre-study survey items against usage counts (nStudents = 24) found message counts "positively correlated with their mean mastery score ( nStudents = 24, r = 0.47, p = 0.04)" and negatively correlated with working on non-graded exercises.

> "The number of messages students wrote was positively correlated with their mean mastery score ( nStudents = 24, r = 0.47, p = 0.04) and negatively correlated to students' self-reported tendencies to work on non-graded exercises ( r=-0.59, p = 0.008)."

## Discussion


## Related Claims
- [In a real programming course, students with an eliciting LLM agent on a learning dashboard wrote more reflection messages than students with a telling agent](elicit-agent-more-reflection-messages-lad.md) — related
- [Students using the eliciting agent showed JoL ratings correlated with system learning metrics, strongest for mastery](elicit-condition-jol-accuracy-correlations.md) — related
- [Students' JoL ratings became more consistent over time and evolved from under-rating to over-rating to accurate judgement](jol-consistency-and-rating-evolution.md) — related
- [Tell and no-agent conditions showed no significant JoL–confidence correlations, with mixed results for progress and mastery](tell-none-conditions-mixed-jol-correlations.md) — related
- [Fluent Illusions Mislead Self Assessment](fluent-illusions-mislead-self-assessment.md) — related
- [JoL–mastery accuracy trajectories over the five weeks rose in the elicit condition, declined in the none condition, and were mixed in the tell condition](jol-accuracy-trajectories-by-condition.md) — related
- [Engineering physics undergraduates are more curious than they appear in lecture when given the chance to submit questions about interactive simulations](students-more-curious-than-lecture-appears.md) — related
- [Every student present submitted at least one question response for each simulation, without external incentives](full-participation-question-submission.md) — related
