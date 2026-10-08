---
type: element
id: uc-berkeley-course-transaction-dataset
title: UC Berkeley course transaction dataset and publicly released analysis code
description: "The study analyzes timestamped student course transactions (waitlists, adds, swaps, drops) from Fall 2016 to Spring 2022 at UC Berkeley, described as \"over 10 million fine-grain, timestamped records of student course..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: borchers-2025
    resource: "https://github.com/CAHLR/enrollment-procrastination-edm"
    title: "Borchers, C., Xu, Y., & Pardos, Z. A. (2025). Workload Overload? Late Enrollment Leads to Course Dropout. Journal of Educational Data Mining, Volume 17, No 1. https://github.com/CAHLR/enrollment-procrastination-edm"
    author: "Borchers, C., Xu, Y., & Pardos, Z. A"
---

# UC Berkeley course transaction dataset and publicly released analysis code

> **Element** · [All elements](index.md)
> **Evidence** · 6 claims (6 for) · 1 study (1 associational), `q2` · 1 of 1 report an effect size · 6 claims rest on one study

## Description
The study analyzes timestamped student course transactions (waitlists, adds, swaps, drops) from Fall 2016 to Spring 2022 at UC Berkeley, described as "over 10 million fine-grain, timestamped records of student course transactions" covering "over N = 150,887 student semesters". The dataset includes 11,136,719 transactions, of which 9,141,091 (82.1%) were initiated by students and affect enrollment status. All data analysis code is publicly available in a GitHub repository linked in the article.

## Design Implications

### Context
#### Requirements
- Data was provided in anonymized format by an institutional data provider; analysis was conducted on servers within the UC Berkeley data center.
#### Constraints
- The data is anonymized and privately held; the article states an IRB approval was not necessary due to this nature.

### Target Learners
- undergraduate students at a large public US university

### Target Learning Goals
- understanding academic planning behavior and late course dropping in higher education

## Claims

- [Course add and drop activity concentrates early in enrollment phases, with drops outnumbering adds from mid-to-late Phase 2 onward and basket size never substantially decreasing](../claims/course-transaction-trends-across-semester.md) [+W]
- [Drop delay and enrollment delay correlate strongly (r = 0.52), while semester workload correlates weakly and negatively with enrollment delay and activity regularity](../claims/delay-regularity-workload-correlations.md) [+W]
- [Cross-lagged panel models support a causal hypothesis that delayed enrollment leads to subsequent late drops, with no reverse reinforcement](../claims/delayed-enrollment-causally-leads-to-late-drops.md) [+W]
- [Later enrollment is associated with more late dropped course units, while later dropping and more regular planning activity are associated with fewer late dropped units](../claims/enrollment-delay-increases-late-drops-regularity-decreases.md) [+W]
- [High-enrollment-delay students and late droppers enroll in more courses and carry higher predicted semester workload, out of their own volition rather than being forced into leftover high-workload courses](../claims/late-enrollment-voluntary-higher-workload.md) [+W]
- [Students preferentially late-drop courses with higher predicted workload than retained courses, regardless of enrollment delay group](../claims/preferential-late-drop-high-workload-courses.md) [+W]

## Related Elements
- 

## Examples
-

## Key Sources
- Borchers, C., Xu, Y., & Pardos, Z. A. (2025). Workload Overload? Late Enrollment Leads to Course Dropout. Journal of Educational Data Mining, Volume 17, No 1. https://github.com/CAHLR/enrollment-procrastination-edm
