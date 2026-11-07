---
type: design
id: meya-session-selector-planner-algorithm
title: MEYA Session Selector/Planner algorithm recommending modules from caregiver-rated Youth Top Problems
description: "The Session Selector/Planner sits on the practitioner's homepage and \"provides module recommendations for each session for each child based on an underlying algorithm\"."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-07
sources:
  - id: wood-jeffrey-j-2024
    resource: "https://doi.org/10.1007/s10803-023-06226-w"
    title: "Wood Jeffrey J., Wood Karen S., Rosenau Kashia A., Cho An Chuen, Johnson Amanda R., Muscatello Virginia S., Tien Ingrid S., Straus Jolie, Wolpe Samara, Zeldin Ari, Kazlauskas Kristofer, McLeod Bryce D. (2024). Practitioner Adherence and Competence in MEYA, a Free Online Self-Instruction Program in Modular Psychotherapy and Counseling for Children's Autism-Related Clinical Needs. Journal of Autism and Developmental Disorders. https://doi.org/10.1007/s10803-023-06226-w"
    author: Wood Jeffrey J., Wood Karen S., Rosenau Kashia A., Cho An Chuen, Johnson Amanda R., Muscatello Virginia S., Tien Ingrid S., Straus Jolie, Wolpe Samara, Zeldin Ari, Kazlauskas Kristofer, McLeod Bryce D
---

# MEYA Session Selector/Planner algorithm recommending modules from caregiver-rated Youth Top Problems

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The Session Selector/Planner sits on the practitioner's homepage and "provides module recommendations for each session for each child based on an underlying algorithm". It uses weekly caregiver severity ratings (0-10) of up to 12 Youth Top Problems across six clinical areas, first recommending two core modules, then modules for clinical areas with a current YTP score of at least 5, in a fixed priority order, until no YTP exceeds 4 or maximum sessions are reached. Practitioners remain free to select any module regardless of the recommendation.

## Design Implications

### Context
#### Requirements
- An initial semi-structured caregiver interview (derived from the Youth Top Problems measure) eliciting up to two high-priority goals or problems per clinical area
- Weekly caregiver ratings of the child's YTPs as ongoing input data
#### Constraints
- The cutpoint of 5 (out of 10) as an indicator of clinical need was a rationally selected parameter based on clinical experience, and the article states it is an empirical question whether a different threshold would be more effective
- The article notes limitations to an intervention primarily driven by caregivers' ratings of problems and goals

### Target Learners
- Practitioners delivering once-weekly outpatient psychotherapy or counseling to autistic children and youth

### Learning Goals
- Personalized selection of intervention modules matched to each child's highest-priority clinical needs

### Claims
- 

## Related Designs
- Meya Online Self Instruction Platform

## Examples
-

## Key Sources
- Wood Jeffrey J., Wood Karen S., Rosenau Kashia A., Cho An Chuen, Johnson Amanda R., Muscatello Virginia S., Tien Ingrid S., Straus Jolie, Wolpe Samara, Zeldin Ari, Kazlauskas Kristofer, McLeod Bryce D. (2024). Practitioner Adherence and Competence in MEYA, a Free Online Self-Instruction Program in Modular Psychotherapy and Counseling for Children's Autism-Related Clinical Needs. Journal of Autism and Developmental Disorders. https://doi.org/10.1007/s10803-023-06226-w
