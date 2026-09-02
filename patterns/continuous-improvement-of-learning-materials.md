---
type: pattern
id: continuous-improvement-of-learning-materials
title: Continuous Improvement of Learning Materials
description: A post-release design process that treats a shipped course as a hypothesis under test — instrumenting materials so that use and outcome data are collected together, running short build–measure–learn cycles, and using RISE analysis to decide which resource to revise next.
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-02
author: David Wiley, Strader and Bodily lineage
grain_size: course
---

# Continuous Improvement of Learning Materials

> **Pattern** · [All patterns](index.md)

## Description
Most design processes end at release. Continuous improvement begins there: the shipped course is treated as the current best hypothesis, instrumented so that every subsequent cohort produces evidence about which of its parts are working, and revised in small, targeted increments rather than in periodic wholesale rewrites.

The process borrows the **build–measure–learn** loop from lean product development and applies it to instructional materials. *Build* is a specific, small change to a specific resource. *Measure* is the pairing of two data the course already generates — which resources learners actually used, and how they then performed on the assessment aligned to the same outcome. *Learn* is the decision about what to change next, which the pairing makes far better posed than either signal alone.

**RISE analysis** — Resource Inspection, Selection, and Enhancement — is the selection instrument. For each learning outcome it plots resource use against assessment performance, both relative to the course average, giving four quadrants:

| | Below-average grade | Above-average grade |
|---|---|---|
| **Above-average use** | Learners used it and still did badly — **the improvement queue** | Working; leave alone |
| **Below-average use** | Learners skipped it and did badly — check discoverability and alignment | Learners skipped it and did fine — the resource may be redundant |

The high-use, low-grade quadrant is the point of the method: it names the resources that are being read and are failing, which is neither what a usage report alone nor a gradebook alone would surface. The other quadrants are diagnostic rather than directive — low use with low grades is as likely to mean a broken link or a bad outcome-to-item alignment as a bad resource.

This is a *design* process, not an analytics dashboard. Its precondition is a licence and a workflow that let the materials actually be changed, which is why it developed in open educational resources: a textbook you cannot revise cannot be continuously improved, however well instrumented.

## Implications

### Context
#### Requirements
- **Materials you are permitted and able to revise** — an open licence, or ownership of the content
- **Outcome-tagged resources and assessment items.** RISE pairs use with performance *per outcome*; without the alignment mapping there is nothing to cross-tabulate
- **Enough learners for the averages to mean something.** The method is comparative, so a small cohort produces noise with a quadrant label on it
- **A release cadence** — a real path from "this resource is in the improvement queue" to a revised resource in front of the next cohort
- **Consent and data governance** appropriate to using learner behaviour and grades as design evidence

#### Constraints
- **Correlational, not causal.** A high-use low-grade resource may be the hardest topic rather than the worst resource; the analysis ranks candidates for inspection, and the inspection is human
- **Optimises what is measured.** Outcomes that carry no aligned items are invisible to the loop and decay quietly while the measured ones improve
- **Assessment quality caps the whole method.** A poorly written item makes its aligned resource look broken, and the loop will then "improve" a resource that was fine
- **Local minima.** Continuous small revision improves the design you have; it will not tell you the course should have been structured differently. Periodic redesign — [Design Thinking](design-thinking.md), or a fresh [systematic analysis](systematic-instructional-design.md) — is a separate obligation
- **Survivorship in the use data.** Learners who dropped out are the ones whose evidence you most need and least have

#### Grain Size
- Course (the natural unit, because the averages are within-course)
- Programme, where the same outcome framework spans courses
- Resource (the unit of the revision itself)

### Target Goals
- Courses that will run repeatedly, where each cohort can leave the next one better off
- Large-enrolment or self-paced materials, where usage data is plentiful and direct observation of learners is not
- Open textbooks and OER collections, where revision rights exist and revision effort must be prioritised

### Target Learners
- Cohorts large enough to be described by averages; the method reasons about a population, and says nothing about an individual learner
- Later cohorts are the beneficiaries — a design cost borne by earlier ones, which is worth stating openly

### Theory
#### Supporting
- [Information Processing Theory](../theories/information-processing-theory.md) — the assumption that a resource's contribution to an outcome is separable enough to be measured
- [Design Layers Theory](../theories/design-layers-theory.md) — revising resources without redesigning structure is a layered change

#### Contradicting / Qualifying
- [Situated Learning](../theories/situated-learning.md) — outcome-tagged resource use is a thin proxy for participation in a practice, and improving the proxy is not the same as improving the learning

### Claims
#### Supporting
- [Feedback is most effective when directed at the task and process rather than the self.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S] — the loop is feedback to the *design*, and the same conditions apply: task-level and specific beats global and evaluative
- [Assessment for learning improves achievement](../claims/assessment-for-learning-improves-achievement.md) [+S] — the assessment data the loop runs on has to be worth acting on for learners first, or the design signal is built on an instrument nobody should trust

#### Contradicting
- [Fluent Illusions Mislead Self Assessment](../claims/fluent-illusions-mislead-self-assessment.md) [~M] — resource *use* is a fluency signal, and fluency is exactly the cue that misleads; a heavily-used resource can be popular because it feels easy

## Design

### Sequence
1. **Align** — map every resource and every assessment item to a learning outcome. This is the step that makes the rest possible and the step most often absent
2. **Instrument** — capture resource use and item-level performance in a form that can be joined on outcome
3. **Run a cohort** and let the data accumulate; resist revising mid-run, which destroys the comparison
4. **Analyse (RISE)** — cross-tabulate use against performance per outcome; rank the above-use/below-grade resources
5. **Inspect** — read the flagged resources and their items. Decide whether the resource, the item, the alignment, or the topic's difficulty is the finding
6. **Enhance** — make one specific change per flagged resource, small enough that the next cohort's data can be attributed to it
7. **Release and repeat** — and record what was changed, so an improvement that made things worse can be identified and reverted

### Elements Used
- [Learning Outcomes](../elements/learning-outcomes.md)
- [Assessment](../elements/assessment.md)
- [Learning Analytics Feedback](../elements/learning-analytics-feedback.md)

### Affordances
- [Formative Assessment](../principles/formative-assessment.md)

### Personalization
- **Without analytics**, run the same loop on cheaper evidence: item analysis from the gradebook, a two-question exit survey per module, or instructor notes. The loop's value is the discipline of one change per cycle, not the telemetry
- **Small cohorts** should aggregate across several runs before analysing, and treat quadrant membership as a prompt to look rather than a finding
- **Where the licence does not permit revision**, the loop still works as a *selection* process: swap the failing resource for another rather than improving it

## Related Patterns
- [Data Wise Improvement Process](data-wise-improvement-process.md) — the same evidence-to-action discipline run by a school team on its own instruction
- [Successive Approximation Model](successive-approximation-model.md) — iterative before release; this is iterative after it
- [Formative Assessment](formative-assessment.md) — the learner-facing counterpart of the same loop
- [Learner Experience Design](learner-experience-design.md) — supplies the qualitative methods that explain *why* a flagged resource is failing
- [Online Course Design](online-course-design.md)

## Examples
- **Open textbook revision programmes** — usage and outcome data from one term prioritising which chapters are rewritten for the next
- **Self-paced courseware** — where per-resource telemetry is abundant and no instructor is present to notice a resource failing

## Key Sources
- Wiley, Strader, & Bodily. Ch. 15 in *Design for Learning*. EdTech Books. [https://edtechbooks.org/id/continuous_improvement](https://edtechbooks.org/id/continuous_improvement)
