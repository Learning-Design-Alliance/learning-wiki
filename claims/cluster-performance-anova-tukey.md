---
type: claim
title: "The six clusters differ substantially in academic performance: Final Grade ANOVA η² = 0.770, with C0 exceeding C1 by 40.17 exam-score points"
description: "The six clusters differ substantially in academic performance: Final Grade ANOVA η² = 0.770, with C0 exceeding C1 by 40.17 exam-score points"
id: cluster-performance-anova-tukey
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: najem-2026
    resource: "https://doi.org/10.1007/s44217-026-02181-7"
    title: "Najem, K., Zaoui Seghroucheni, Y., & Ziti, S. (2026). Behavioral clustering for adaptive learning object recommendation in higher education using learning analytics for personalized student success. Discover Education. https://doi.org/10.1007/s44217-026-02181-7"
    author: "Najem, K., Zaoui Seghroucheni, Y., & Ziti, S."
    q: 2
    i: 3
    kind: associational
    rigour: 1
  - id: najem-2026-2
    resource: "https://doi.org/10.1007/s44217-026-02181-7"
    title: "Najem, K., Zaoui Seghroucheni, Y., & Ziti, S. (2026). Behavioral clustering for adaptive learning object recommendation in higher education using learning analytics for personalized student success. Discover Education. https://doi.org/10.1007/s44217-026-02181-7"
    author: "Najem, K., Zaoui Seghroucheni, Y., & Ziti, S."
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# The six clusters differ substantially in academic performance: Final Grade ANOVA η² = 0.770, with C0 exceeding C1 by 40.17 exam-score points

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2` · `i3` large

## Subclaims
`q2 i3` Cluster membership is strongly associated with Final Grade (F(5, 13,997) = 9365.49, p < 0.001, η² = 0.770), with Exam Score as a sensitivity analysis (η² = 0.709). [→ Najem 2026](#najem-2026)
`q2 i?` Tukey HSD tests show the highest-performing cluster C0 exceeded the lowest-performing cluster C1 by a mean of 40.17 points (95% CI [39.55, 40.78], p < 0.001), and C5 exceeded C1 by 32.82 points. [→ Najem 2026 (2)](#najem-2026-2)

## Evidence

### Najem 2026

Najem, K., Zaoui Seghroucheni, Y., & Ziti, S. (2026). Behavioral clustering for adaptive learning object recommendation in higher education using learning analytics for personalized student success. Discover Education. https://doi.org/10.1007/s44217-026-02181-7

`q2 · i3` · `associational · r1`

One-way ANOVA on the 14,003-record dataset comparing the six clusters on Final Grade, with Exam Score as a sensitivity analysis because the two outcomes are not statistically independent; the article reports η² = 0.770 and η² = 0.709 respectively.

> "Therefore, the primary validation relies on Final Grade, F(5, 13,997) = 9365.49, p < 0.001, η2 = 0.770. Exam Score is reported as a sensitivity analysis (F(5, 13,997) = 6822.77, p < 0.001, η2 = 0.709)"

### Najem 2026 (2)

Najem, K., Zaoui Seghroucheni, Y., & Ziti, S. (2026). Behavioral clustering for adaptive learning object recommendation in higher education using learning analytics for personalized student success. Discover Education. https://doi.org/10.1007/s44217-026-02181-7

`q2 · i?` · `associational · r1`

Post hoc Tukey HSD pairwise comparisons across the six clusters; C0 exceeded C1 by 40.17 points and C5 exceeded C1 by 32.82 points, with all top-versus-bottom pairwise comparisons significant at p < 0.001.

> "Post hoc Tukey HSD comparisons revealed that the highest-performing cluster, C0 (Highly Engaged Achievers), differed significantly from the lowest-performing cluster, C1 (At-Risk Learners), by a mean of 40.17 points (95% CI [39.55, 40.78], p < 0.001)."

## Discussion


## Related Claims
- [K-means clustering of standardized prior knowledge and final grades yields four performance profiles: Consistent Achievers, Growing Achievers, Declining Performers, and Struggling Performers](four-kmeans-achievement-trajectory-profiles.md) — related
- [Profiles differ in self-perceived academic skills: Engaged and Literate users report the highest problem-solving and cognitive endurance gains, while Uncritical Reliant users report the highest independent thinking](profile-differences-academic-skills.md) — related
- [Growing Achievers used StatBot significantly more than Declining Performers, driven mainly by initiating new inquiries](growing-achievers-out-use-declining-performers.md) — related
- [Student academic ability varied across quarters but not systematically with changes in course structure](student-ability-varied-not-with-structure.md) — related
- [The four exam-performance quartile groups differed significantly on first-unit exam scores, validating the grouping used for behavioral comparisons](quartile-groups-differ-on-exam-scores.md) — related
