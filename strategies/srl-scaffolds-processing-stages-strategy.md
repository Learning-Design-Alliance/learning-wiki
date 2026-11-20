---
type: strategy
id: srl-scaffolds-processing-stages-strategy
title: "Provide SRL scaffolds during processing stages and after errors, informed by students' SRL cycle state"
description: "The authors recommend that tutoring software provide additional scaffolds guiding students to process instruction and error feedback rather than continuing to act, and that adaptive scaffolds \"should not only jump in..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: conrad-borchers-2024
    resource: "https://doi.org/10.1145/3636555.3636911"
    title: "Conrad Borchers, Jiayi Zhang, Ryan S. Baker, and Vincent Aleven. 2024. Using Think-Aloud Data to Understand Relations between Self-Regulation Cycle Characteristics and Student Performance in Intelligent Tutoring Systems. In The 14th Learning Analytics and Knowledge Conference (LAK '24). ACM. https://doi.org/10.1145/3636555.3636911"
    author: Conrad Borchers, Jiayi Zhang, Ryan S. Baker, and Vincent Aleven
---

# Provide SRL scaffolds during processing stages and after errors, informed by students' SRL cycle state

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The authors recommend that tutoring software provide additional scaffolds guiding students to process instruction and error feedback rather than continuing to act, and that adaptive scaffolds "should not only jump in when a stage of processing is detected but should explicitly consider students' SRL cycle characteristics". Scaffolds could signal the next expected cycle stage, display the current subgoal, or prompt subgoal setting, with fading as students self-regulate more effectively.

## Design Implications

### Context
#### Requirements
- Detection of processing stages, potentially via live think-aloud transcription and machine learning
- A fading mechanism so scaffolding decreases as students gain self-regulation ability
#### Constraints
- Having multiple students think aloud concurrently in larger classrooms is not feasible; the authors suggest teacher visits or at-home practice as collection opportunities
- Practicality of adaptivity pipelines from live transcriptions remains an open question

### Target Learners
- higher-education students practicing stoichiometry in ITS

### Target Learning Goals
- effective self-regulated learning during tutored problem-solving
- reducing premature acting during processing stages

## Claims

- [In-tutor correctness is lower after processing and error-realization utterances and higher after enacting utterances in stoichiometry ITS](../claims/srl-codes-moment-correctness-its.md) [+W]
- [A model including SRL cycle characteristics fits next-attempt correctness better than a model using only in-the-moment SRL codes](../claims/srl-cycle-features-outperform-in-the-moment.md) [+W]
- [Correctness rises the farther students are into an ongoing SRL cycle, and longer average cycles relate to higher correctness](../claims/srl-cycle-position-correctness.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Conrad Borchers, Jiayi Zhang, Ryan S. Baker, and Vincent Aleven. 2024. Using Think-Aloud Data to Understand Relations between Self-Regulation Cycle Characteristics and Student Performance in Intelligent Tutoring Systems. In The 14th Learning Analytics and Knowledge Conference (LAK '24). ACM. https://doi.org/10.1145/3636555.3636911
