---
type: strategy
title: Needs Analysis
description: A systematic process for identifying the gap between current and desired performance and determining whether instruction is the right remedy.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Needs Analysis

> **Strategy** · [All strategies](index.md)

## Description
Needs analysis (often called needs assessment) is the front-end process of determining whether a performance gap exists, what causes it, and whether — and what kind of — instruction will close it. It gathers data from learners, performers, and stakeholders through interviews, surveys, observation, and document review, then maps findings to instructional or non-instructional interventions. It is carried out before design begins, so that subsequent decisions about objectives, [Practice](../elements/practice.md), and assessment are grounded in evidence rather than assumption.

## Design Implications

Needs analysis protects against the most common instructional design failure: building training for a problem that is not instructional in origin. Performance gaps can stem from missing tools, unclear expectations, inadequate incentives, or environmental obstacles; instruction aimed at these causes is wasted effort [Training interventions matched to diagnosed causes outperform generic solutions.](../claims/claim-slug.md) [+W]. Analysis should distinguish *can't* (knowledge/skill deficit — trainable) from *won't* (motivation or consequence problem — usually not) before committing to a design.

### Context
#### Requirements
- Access to multiple data sources: performers, supervisors, and ideally the work products or performance records themselves
- A clear statement of the desired state (standard, competency, or organizational goal) against which current performance is compared
- Willingness to conclude that instruction is *not* the answer when the data say so
- Triangulation across methods — surveys alone systematically misidentify causes [Self-report data about performance causes diverge from observed performance data.](../claims/claim-slug.md) [+W]

#### Constraints
- Analysis conducted only with managers or sponsors (not performers) produces solutions that miss the actual workflow [~W]
- Time pressure routinely truncates analysis; designs built on unexamined assumptions about the audience require costly rework after pilot [~M]
- Stakeholders often request a delivery format ("we need a course") rather than a performance outcome; accepting the request as the need invalidates the analysis [-M]
- In fast-changing domains, a lengthy analysis can be obsolete before design begins; rapid, iterative analysis is required instead [~W]

#### Implementation Variability
- **Performance analysis** (Dick & Carey tradition): compares actual vs. desired performance to derive instructional goals
- **Discrepancy model** (Kaufman): organizational, process, and individual levels of gap analysis
- **Learning-centered analysis** (Foshay, Silber & Stelnicki): focuses on what learners must know and do, deferring organizational framing
- **Rapid/front-end analysis** (Rossett): short-cycle interviews and observation embedded in project kickoff, suited to agile development

### Target Learners
- Not applied to learners directly, but defines them: prior knowledge, motivation, constraints, and context identified during analysis drive audience segmentation [Activation of prior knowledge improves learning outcomes.](../claims/activation-improves-learning.md) [+S]
- Analysis of learner characteristics determines whether supports like [Advance Organizers](../elements/advance-organizers.md) or [Worked Examples](../elements/worked-examples.md) are appropriate for the audience's expertise level

### Target Learning Goals
- Not a learning goal in itself; it determines which goals are worth pursuing
- Outputs feed goal statements, terminal objectives, and the criteria later used in [Assessment](../elements/assessment.md) and [Assess Performance](../elements/assess-performance.md)

### Instructions
1. Identify the performance gap: gather data on what is happening and what should be happening (records, observation, interviews).
2. Diagnose causes: sort deficits into skills/knowledge, motivation, environment, and resources; only skill/knowledge deficits warrant instruction.
3. Prioritize: rank gaps by impact on organizational or learner goals and by feasibility of closing them.
4. Characterize the audience: prior knowledge, [Accommodations](../elements/accommodations.md) needs, technology access, and context of use.
5. Write an instructional goal statement and validate it with stakeholders before moving to design ([Clear Structure](../principles/clear-structure.md) begins here — the goal statement becomes the spine of the design).
6. Revisit the analysis after pilot testing; treat it as a hypothesis, not a verdict.

## Related Strategies
- [Learner Personas](../strategies/learner-personas.md) — a synthesis format for the audience data gathered during analysis
- [Task Analysis](task-analysis.md) — the follow-on decomposition of the goal into component knowledge and skills
- [Formative Evaluation](../strategies/formative-evaluation.md) — continues the evidence-gathering stance after design begins

## Examples
- **Dick & Carey model** — the first step, "Identify Instructional Goals," is a needs analysis that derives goals from performance discrepancies rather than from content inventories.
- **[CDC's training evaluation framework](https://www.cdc.gov/training-publichealth/php/about/index.html)** — public health training programs conduct needs assessments across organizational and individual levels before commissioning courses.
- **Corporate onboarding redesign** — analysis revealing that new-hire errors stemmed from undocumented tool settings (environmental cause) leads to a job aid rather than a training course, saving development cost.

## Key Sources
- Rossett, A. (1987). *Training needs assessment*. Educational Technology Publications.
- Witkin, B. R., & Altschuld, J. W. (1995). *Planning and conducting needs assessments: A practical guide*. Sage.
- Kaufman, R., & English, F. W. (1979). *Needs assessment: Concept and application*. Educational Technology Publications.
- Dick, W., Carey, L., & Carey, J. O. (2015). *The systematic design of instruction* (8th ed.). Pearson.
- Clark, R. E., & Estes, F. (2008). *Turning research into results: A guide to selecting the right performance solutions*. IAP. [doi:10.1002/pfi.4140430110](https://doi.org/10.1002/pfi.4140430110)