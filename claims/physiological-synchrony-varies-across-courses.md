---
type: claim
title: "Students' physiological synchrony differs statistically significantly across academic courses, with all significant pairwise differences involving PE"
description: "Students' physiological synchrony differs statistically significantly across academic courses, with all significant pairwise differences involving PE"
id: physiological-synchrony-varies-across-courses
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
sources:
  - id: soundariya-ananthan-2024
    title: Soundariya Ananthan 2024
    q: 2
    i: "?"
    kind: associational
    rigour: 1
  - id: soundariya-ananthan-2024-2
    title: Soundariya Ananthan 2024 (2)
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Students' physiological synchrony differs statistically significantly across academic courses, with all significant pairwise differences involving PE

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 associational `r1` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` ANOVA on physiological synchrony scores across courses was significant (statistic 3.711, P = 3.163e-07), rejecting the null hypothesis of no difference across course types. [→ Soundariya Ananthan 2024](#soundariya-ananthan-2024)
`q2 i?` Tukey HSD post-hoc tests found 6 of 45 course pairs significantly different, and all six pairs involved the course PE. [→ Soundariya Ananthan 2024 (2)](#soundariya-ananthan-2024-2)

## Evidence

### Soundariya Ananthan 2024

Soundariya Ananthan, Nan Gao, and Flora D. Salim. 2024. Understanding Physiological Responses of Students Over Different Courses. In Proceedings of the 2024 ACM International Symposium on Wearable Computers (ISWC '24). https://doi.org/10.1145/3675095.3676620

`q2 · i?` · `associational · r1`

Analysis of FastDTW-computed physiological synchrony scores from 23 students across 10 courses using ANOVA. The article reports "a statistical value of 3.711 and a P-value of 3.163e-07", so the null hypothesis of no difference across courses was rejected.

> "we employed the analysis of variance (ANOVA) method on calculated physiological synchrony. The results showed a statistical value of 3.711 and a P-value of 3.163e-07, which is less than 0.05."

### Soundariya Ananthan 2024 (2)

Soundariya Ananthan, Nan Gao, and Flora D. Salim. 2024. Understanding Physiological Responses of Students Over Different Courses. In Proceedings of the 2024 ACM International Symposium on Wearable Computers (ISWC '24). https://doi.org/10.1145/3675095.3676620

`q2 · i?` · `associational · r1`

Tukey's HSD with FWER set to 0.05 on the same synchrony scores. The article reports "45 pairs of courses, out of which 6 have significant differences", and notes "all the six pairs involved the course PE"; adjusted p-values ranged from 0.003 to 0.044.

> "In total, we had 45 pairs of courses, out of which 6 have significant differences."

## Discussion


## Related Claims
- [PE shows the highest physiological synchrony score (195.3) and Assembly the lowest (3.3), with other courses scoring similarly](pe-highest-assembly-lowest-synchrony.md) — related
- [Frequency-domain HRV features differ by course: Assembly shows high VLF and HF activation while PE has the lowest HF value](frequency-domain-hrv-course-differences.md) — related
- [EDA changepoint and autocorrelation values are high for PE and low for Assembly, with Assembly showing fewer SCR peaks](eda-changepoint-autocorrelation-course-differences.md) — related
- [Mean heart rate is higher in Assembly (109.4 bpm) than in PE (101.3 bpm), with both courses showing shorter NNI intervals than other courses](assembly-heart-rate-exceeds-pe.md) — related
