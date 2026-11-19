---
type: claim
title: "Participants using an external RTK module were exposed to less accurate and less continuous geolocation data than participants using the device's embedded GNSS sensor"
description: "Participants using an external RTK module were exposed to less accurate and less continuous geolocation data than participants using the device's embedded GNSS sensor"
id: rtk-less-accurate-than-embedded-gnss-location-ar
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
sources:
  - id: j-mercier-2023
    resource: "https://doi.org/10.5194/isprs-archives-xlviii-4-w7-2023-133-2023"
    title: "J. Mercier, N. Chabloz, G. Dozot, C. Audrin, O. Ertz, E. Bocher, D. Rappo. (2023). Impact of Geolocation Data on Augmented Reality Usability: A Comparative User Test. [doi:10.5194/isprs-archives-xlviii-4-w7-2023-133-2023](https://doi.org/10.5194/isprs-archives-xlviii-4-w7-2023-133-2023)"
    author: J. Mercier, N. Chabloz, G. Dozot, C. Audrin, O. Ertz, E. Bocher, D. Rappo
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Participants using an external RTK module were exposed to less accurate and less continuous geolocation data than participants using the device's embedded GNSS sensor

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` RTK trajectories contained significantly more outliers (M = 46.8) than GNSS trajectories (M = 7.2). [→ J. Mercier 2023](#j-mercier-2023)

## Evidence

### J. Mercier 2023

J. Mercier, N. Chabloz, G. Dozot, C. Audrin, O. Ertz, E. Bocher, D. Rappo. (2023). Impact of Geolocation Data on Augmented Reality Usability: A Comparative User Test. [doi:10.5194/isprs-archives-xlviii-4-w7-2023-133-2023](https://doi.org/10.5194/isprs-archives-xlviii-4-w7-2023-133-2023)

`q2 · i?` · `causal · r2`

Outlier counts in logged 1 Hz trajectories, an indicator of data continuity. RTK trajectories contained far more outliers than GNSS trajectories, with a significant Welch t-test; the authors attribute this to embedded GNSS filters removing outliers.

> "the GNSS group trajectories contained M = 7.2 (SD = 7.55) outliers, and these of the RTK group M = 46.8 (SD = 40.1). A Welch t-test was used. The results show a significant difference between the two groups (t(27.9) = -5.04, p = <.001)."

## Discussion


## Related Claims
- [The group exposed to less accurate geolocation data reported lower usability on all nine scales, of which five were statistically significant](geolocation-accuracy-predicts-ar-usability.md) — related
- [No significant group differences in exploration diversity or ease: POIs visited and 2D map openings did not differ between GNSS and RTK groups](no-group-difference-pois-visited-map-openings.md) — related
- [Geolocation data accuracy showed no significant relation to focus: screen-gaze time ratios did not differ between groups](no-relation-geolocation-accuracy-focus-screen-gaze.md) — related
