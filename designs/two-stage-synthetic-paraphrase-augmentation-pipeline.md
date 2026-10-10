---
type: design
id: two-stage-synthetic-paraphrase-augmentation-pipeline
title: "Two-stage data preparation pipeline: rule-based synthetic generation plus LLM paraphrase augmentation without data leakage"
description: "The pipeline first generates synthetic score-level-1 samples in the training partition only, using \"template-based generation (40%), quality degradation (35%), and a combined approach (25%)\", including truncation to 2..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: firdausi-2026
    resource: "https://doi.org/10.22266/ijies2026.0831.09"
    title: "Firdausi, H.; Wasis; Sholikah, R. W.; Lemantara, J.; Rosyadi, F. D.; Ginardi, R. V. H.; Pradityo, M. H. A.; Hakim, A. R. (2026). Educational Innovation through Automated Essay Scoring: A Multidimensional Framework for Evaluating Critical Thinking in High School Physics Essays. International Journal of Intelligent Engineering and Systems, Vol.19, No.8. https://doi.org/10.22266/ijies2026.0831.09"
    author: Firdausi, H.; Wasis; Sholikah, R. W.; Lemantara, J.; Rosyadi, F. D.; Ginardi, R. V. H.; Pradityo, M. H. A.; Hakim, A. R
---

# Two-stage data preparation pipeline: rule-based synthetic generation plus LLM paraphrase augmentation without data leakage

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The pipeline first generates synthetic score-level-1 samples in the training partition only, using "template-based generation (40%), quality degradation (35%), and a combined approach (25%)", including truncation to 20–40% of original length and removal of domain-critical keywords. Second, paraphrase-based augmentation via the Gemini API balances minority classes at scores 2–4 to a uniform 25% per level. Splitting was done once at the student level so each student's responses appear in a single partition, "thereby preventing cross -dimensional data leakage," and the test set stayed locked and unmodified.

## Design Implications

### Context
#### Requirements
- Augmentation and generation confined strictly to the training partition; fixed random seed; target counts set to the majority class size per dimension
#### Constraints
- Alternative techniques (back-translation, synonym substitution, EDA) were excluded after preliminary experiments showed lower output quality and inconsistent meaning preservation in the Indonesian physics essay domain; in Overview, augmentation marginally decreased QWK

### Target Learners
- Indonesian high school physics students whose essays form the scored dataset

### Learning Goals
- Reliable ordinal automated scoring of critical thinking dimensions despite severe class imbalance

### Claims
- [Augmentation Critical Ordinal Qwk Gains](../claims/augmentation-critical-ordinal-qwk-gains.md) [+M]
- [Overview Augmentation Qwk Tradeoff](../claims/overview-augmentation-qwk-tradeoff.md) [~M]

## Related Designs
- 

## Examples
-

## Key Sources
- Firdausi, H.; Wasis; Sholikah, R. W.; Lemantara, J.; Rosyadi, F. D.; Ginardi, R. V. H.; Pradityo, M. H. A.; Hakim, A. R. (2026). Educational Innovation through Automated Essay Scoring: A Multidimensional Framework for Evaluating Critical Thinking in High School Physics Essays. International Journal of Intelligent Engineering and Systems, Vol.19, No.8. https://doi.org/10.22266/ijies2026.0831.09
