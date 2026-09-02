---
type: strategy
id: define_and_apply_ethical_responsibility
title: Define and Apply Ethical Responsibility
description: Making the ethical obligations of a domain explicit, then having learners apply them to concrete, contested cases rather than affirm them in the abstract.
status: review
generated:
  by: claude/unspecified
  at: 2026-08-30
sources:
  - id: bebeau-1999
    resource: "https://doi.org/10.3102/0013189X028004018"
    title: "Bebeau, M. J., Rest, J. R., & Narvaez, D. (1999). Beyond the promise: A perspective on research in moral education. *Educational Researcher, 28*(4), 18–26"
    author: "Bebeau, M. J., Rest, J. R., & Narvaez, D"
  - id: rest-1986
    title: "Rest, J. R. (1986). *Moral development: Advances in research and theory*. Praeger"
    author: "Rest, J. R"
  - id: jagers-2019
    resource: "https://doi.org/10.1080/00461520.2019.1623032"
    title: "Jagers, R. J., Rivas-Drake, D., & Williams, B. (2019). Transformative social and emotional learning (SEL): Toward SEL in service of educational equity and excellence. *Educational Psychologist, 54*(3), 162–184"
    author: "Jagers, R. J., Rivas-Drake, D., & Williams, B"
---

# Define and Apply Ethical Responsibility

> **Strategy** · [All strategies](index.md)

## Description
This strategy has two halves that must both be present. **Defining**: making explicit what obligations a domain places on someone acting within it — what a researcher owes participants, a developer owes users, a clinician owes patients, a student owes the people whose work they cite. **Applying**: putting learners into concrete cases where those obligations conflict with each other or with self-interest, and requiring a decision with reasons. The definition alone produces learners who can recite a code; the application is where the learning is, because the difficulty in practice is almost never ignorance of the principle but failure to notice that it applies.

## Design Implications

Rest's four-component model is the most useful frame for design, because it separates what an ethics activity can actually target. Acting ethically requires *sensitivity* (noticing that a situation has an ethical dimension), *judgement* (deciding which action is right), *motivation* (prioritizing the ethical over competing values), and *implementation* (carrying it through). Most classroom ethics instruction targets judgement, which is the component least often responsible for failure — professionals who behave badly usually did not deliberate wrongly, they did not notice, or noticed and were outweighed. Cases designed so the ethical dimension is announced train judgement; cases where the ethical issue is embedded in an ordinary technical problem train sensitivity, which is the harder and more transferable target.

The applying half works largely through argument. Requiring learners to construct and defend a position, and to engage with a genuinely opposed one, improves reasoning quality [Argumentation Improves Reasoning](../claims/argumentation-improves-reasoning.md) [+M], and structured disagreement formats outperform open discussion for this [Structured Discussion Approaches Improve Comprehension](../claims/structured-discussion-approaches-improve-comprehension.md) [+M]. Perspective-taking on the affected party is the other active ingredient [Building Empathy Improves Intergroup Attitudes](../claims/building-empathy-improves-intergroup-attitudes.md) [+M].

### Context
#### Requirements
- A domain-specific statement of obligations — a professional code, a disciplinary norm, a course integrity policy — concrete enough to be applied, not a list of virtues
- Cases with genuine tension: if the right answer is obvious, learners practise recognizing obvious answers ([Case-Based Learning](case-based_learning.md))
- A discussion climate where a learner can voice an unpopular position without social penalty, or the exercise produces performance rather than reasoning ([Norm Setting](norm_setting.md))
- A requirement to decide and justify, not merely to explore the considerations
- An instructor willing to hold the tension rather than resolve it, and to make their own reasoning visible when they do take a position ([Think-Aloud](../elements/think-aloud.md))

#### Constraints
- Abstract ethics instruction produces learners who reason well on paper and behave unchanged in practice; the transfer gap between judgement and conduct is the central finding of this literature [-M]
- Cases where the ethical dimension is pre-announced train judgement but not sensitivity — and sensitivity is the component that fails in real settings [-M]
- Discussion of contested moral questions can consolidate rather than shift positions if learners argue only from their existing stance; the structure must require engaging with the opposing case [-M]
- Codes and case sets carry the assumptions of who wrote them, and treating a professional code as a neutral standard can teach learners to reproduce inequities encoded in it [Transformative social and emotional learning (SEL): Toward SEL in service of educational equity and excellence](../claims/social-emotional-learning-improves-achievement.md) [~M]
- Assessing ethical reasoning invites learners to produce the answer they think is wanted, which measures compliance rather than judgement [-M]
- The classroom setting removes the pressures — time, hierarchy, money, fatigue — that cause most real ethical failures [~M]

#### Implementation Variability
- **Professional code analysis** — learners work from the actual code governing their field and apply specific clauses to cases
- **Embedded-dilemma cases** — the ethical issue is buried inside an ordinary technical task, so noticing it is the assessed skill
- **Structured academic controversy** — learners argue an assigned side, then swap, then seek consensus ([Structured Academic Controversy](structured-academic-controversy.md))
- **Take-a-stand continuum** — learners physically position themselves on a spectrum and must justify moving ([Barometer: Taking a Stand on Controversial Issues](barometer-taking_a_stand_on_controversial_issues.md))
- **Dilemma discussion** — the classic Kohlbergian format, with a moderator pressing for reasons ([SEL Discussions on Ethical Dilemmas](sel_discussions_on_ethical_dilemmas.md))
- **Live stakes** — applying the framework to an actual decision facing the class, group, or institution rather than to a hypothetical

### Target Learners
- Learners entering a profession with a formal code and real consequences — health, law, engineering, computing, teaching, research
- Post-secondary and upper-secondary learners with enough domain knowledge to see why a case is hard; the tension is invisible without it
- Learners in courses where academic integrity is the live ethical question, where the domain is one they are already inside
- Weaker fit for young learners on abstract dilemmas, where the reasoning demands exceed what the case can support — concrete, immediate, personally relevant cases work better
- Any group where the ethical questions of the discipline are currently taught as a compliance module divorced from the technical content

### Target Learning Goals
- Ethical sensitivity: noticing that an ordinary situation has a moral dimension — the primary target
- Reasoned judgement: reaching and defending a position with reference to stated obligations [Argumentation Improves Reasoning](../claims/argumentation-improves-reasoning.md) [+M]
- Perspective-taking on those affected by a decision [Building Empathy Improves Intergroup Attitudes](../claims/building-empathy-improves-intergroup-attitudes.md) [+M]
- Practical implementation: knowing what one would actually say and to whom
- Familiarity with the specific obligations of the domain, as content rather than as sentiment

### Instructions
1. **Establish the obligations concretely.** Work from the actual code, policy, or disciplinary norm, and identify the specific duties it names and to whom they are owed.
2. **Set discussion norms first.** Agree how disagreement will work before opening a contested question ([Norm Setting](norm_setting.md), [Class Discussion Norms](class-discussion-norms.md)).
3. **Start with an embedded case.** Give a task that looks technical and contains an unflagged ethical issue; see who notices, and make noticing the first discussion point.
4. **Require a decision, then the reasons.** Have learners commit to an action individually and in writing before any discussion, so the discussion revises a position rather than forms one ([Individual Reflection](../elements/individual-reflection.md)).
5. **Assign opposing positions.** Structure the argument so each learner must construct the strongest version of a case they did not choose ([Structured Academic Controversy](structured-academic-controversy.md)).
6. **Foreground the affected party.** Ask explicitly what the person on the other end of the decision experiences ([Acting / Role Play](acting-role-play.md)).
7. **Move from judgement to implementation.** Ask what they would actually say, to whom, and what it would cost them — this is where classroom ethics usually stops and where practice begins.
8. **Return to the code.** Close by mapping the decision back onto the stated obligations, including where the code was silent or unhelpful.

## Related Strategies
- [Ethical Responsibility Tools](ethical_responsibility_tools.md) — the frameworks and decision aids learners apply within this strategy
- [SEL Discussions on Ethical Dilemmas](sel_discussions_on_ethical_dilemmas.md) — the dilemma-discussion format in a social-emotional frame
- [Structured Academic Controversy](structured-academic-controversy.md) — the argument structure that makes contested discussion productive
- [Barometer: Taking a Stand on Controversial Issues](barometer-taking_a_stand_on_controversial_issues.md) — a fast, physical commitment device for opening a contested question
- [Case-Based Learning](case-based_learning.md) — the vehicle for the applying half of the strategy
- [Civic Online Reasoning](civic-online-reasoning.md) — the same define-and-apply pattern for the ethics of information

## Examples

**Embedded-dilemma cases in software engineering:** Students are given a feature specification to implement; the requirements quietly include collecting data the described use case does not need. Whether anyone raises it before writing the code is the assessed outcome.

**Professional code application in clinical education:** Trainees take a specific clause from their regulator's code and apply it to three cases where it conflicts with another clause, producing a decision and a justification for each.

**Academic integrity as a live ethical question:** Rather than a policy briefing, the class works through cases about collaboration boundaries and AI use in their own current assignments, and drafts the class's own working agreement.

**Structured controversy on a disciplinary question:** Pairs argue an assigned side of a contested question in the field, exchange sides, then attempt a joint statement — the swap being what forces engagement with the opposing case rather than rehearsal of one's own.

## Key Sources
- Bebeau, M. J., Rest, J. R., & Narvaez, D. (1999). Beyond the promise: A perspective on research in moral education. *Educational Researcher, 28*(4), 18–26. [doi:10.3102/0013189X028004018](https://doi.org/10.3102/0013189X028004018)
- Rest, J. R. (1986). *Moral development: Advances in research and theory*. Praeger.
- Jagers, R. J., Rivas-Drake, D., & Williams, B. (2019). Transformative social and emotional learning (SEL): Toward SEL in service of educational equity and excellence. *Educational Psychologist, 54*(3), 162–184. [doi:10.1080/00461520.2019.1623032](https://doi.org/10.1080/00461520.2019.1623032)
