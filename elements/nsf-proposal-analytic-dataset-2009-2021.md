---
type: element
id: nsf-proposal-analytic-dataset-2009-2021
title: NSF proposal analytic dataset of 648,748 proposals across 836 programs, FY 2009–FY 2021
description: "An administrative dataset assembled from NSF's Solr API, Fastlane database, Report Server, and NSF program announcement publications."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: fesler-2022
    resource: "https://www.mathematica.org/publications/no-deadlines-synthetic-control-and-exploratory-outcomes-analysis-and-recommendations-for-a-future"
    title: "Fesler, Lily and Lindsay Fox. (2022). No-deadlines Synthetic Control and Exploratory Outcomes Analysis and Recommendations for a Future Rigorous Evaluation [Memorandum]. Alexandria, VA: National Science Foundation. https://www.mathematica.org/publications/no-deadlines-synthetic-control-and-exploratory-outcomes-analysis-and-recommendations-for-a-future"
    author: Fesler, Lily and Lindsay Fox
---

# NSF proposal analytic dataset of 648,748 proposals across 836 programs, FY 2009–FY 2021

> **Element** · [All elements](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
An administrative dataset assembled from NSF's Solr API, Fastlane database, Report Server, and NSF program announcement publications. After excluding supplements, forward funds, renewals, PI transfers, PAPPG responses, and mis-year proposals, the sample includes "648,748 proposals for 836 programs" out of 781,835 proposals for 921 programs. The synthetic control analytic set further restricted to 468,561 proposals across 194 programs with at least six consecutive years of data. Five outcome variables were constructed: proposal counts, average requested amount, collaborative proposals per project, reviewer counts, and quality rating categories.

## Design Implications

### Context
#### Requirements
- Program linkages across time, since program numbers change over time
- Close-date information in the proposal data to identify NDL status
#### Constraints
- The memo reports close-date information does not always match NSF program announcement publications, and not all funding opportunities have associated program names
- Fewer proposals appear in the data before FY 2009

### Target Learners
- NSF evaluation staff and researchers studying agency award processes

### Target Learning Goals
- Measuring proposal volume, requested funding, collaboration, reviewer burden, and proposal quality over time

### Affordances
- [Augmented Synthetic Control Ndl Approach](../theories/augmented-synthetic-control-ndl-approach.md)

## Claims

- [Exploratory analyses suggest NDL increased requested funding, reduced reviewer burden, and shifted proposal quality ratings for two GEO programs](../claims/ndl-funding-reviewer-quality-exploratory.md) [+W]
- [In exploratory synthetic control analyses, two GEO no-deadlines programs received 120 to 130 fewer proposals relative to their synthetic counterfactuals](../claims/ndl-reduced-proposal-volume-geo-exploratory.md) [+W]
- [Synthetic control counterfactuals performed poorly for BIO NDL programs because few comparison programs were available](../claims/synthetic-control-poor-fit-bio-few-comparisons.md) [+W]

## Related Elements
- 

## Examples

- [Design considerations for a future rigorous evaluation of no-deadlines approaches](../strategies/future-rigorous-ndl-evaluation-considerations.md)

## Key Sources
- Fesler, Lily and Lindsay Fox. (2022). No-deadlines Synthetic Control and Exploratory Outcomes Analysis and Recommendations for a Future Rigorous Evaluation [Memorandum]. Alexandria, VA: National Science Foundation. https://www.mathematica.org/publications/no-deadlines-synthetic-control-and-exploratory-outcomes-analysis-and-recommendations-for-a-future
