---
type: claim
title: Outcome measures validated via learning curves and correlations with expert ratings and end-user satisfaction
description: Outcome measures validated via learning curves and correlations with expert ratings and end-user satisfaction
id: intent-quality-measures-validated
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: conrad-borchers-2025
    resource: "https://doi.org/10.48550/arXiv.2506.11326"
    title: "Conrad Borchers, Xiaoyi Tian, Kristy Elizabeth Boyer, Maya Israel. (2025). Combining Log Data and Collaborative Dialogue Features to Predict Project Quality in Middle School AI Education. CSEDM'25: 9th Educational Data Mining in Computer Science Education (CSEDM) Workshop. [doi:10.48550/arXiv.2506.11326](https://doi.org/10.48550/arXiv.2506.11326)"
    author: Conrad Borchers, Xiaoyi Tian, Kristy Elizabeth Boyer, Maya Israel
    q: 2
    i: 3
    kind: associational
    rigour: 1
  - id: conrad-borchers-2025-2
    resource: "https://doi.org/10.48550/arXiv.2506.11326"
    title: "Conrad Borchers, Xiaoyi Tian, Kristy Elizabeth Boyer, Maya Israel. (2025). Combining Log Data and Collaborative Dialogue Features to Predict Project Quality in Middle School AI Education. CSEDM'25: 9th Educational Data Mining in Computer Science Education (CSEDM) Workshop. [doi:10.48550/arXiv.2506.11326](https://doi.org/10.48550/arXiv.2506.11326)"
    author: Conrad Borchers, Xiaoyi Tian, Kristy Elizabeth Boyer, Maya Israel
    q: 2
    i: 2
    kind: associational
    rigour: 1
  - id: conrad-borchers-2025-3
    resource: "https://doi.org/10.48550/arXiv.2506.11326"
    title: "Conrad Borchers, Xiaoyi Tian, Kristy Elizabeth Boyer, Maya Israel. (2025). Combining Log Data and Collaborative Dialogue Features to Predict Project Quality in Middle School AI Education. CSEDM'25: 9th Educational Data Mining in Computer Science Education (CSEDM) Workshop. [doi:10.48550/arXiv.2506.11326](https://doi.org/10.48550/arXiv.2506.11326)"
    author: Conrad Borchers, Xiaoyi Tian, Kristy Elizabeth Boyer, Maya Israel
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Outcome measures validated via learning curves and correlations with expert ratings and end-user satisfaction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · associational `r1` · `q2` · `i2`–`i3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i3` Training phrase count significantly correlated with expert-rated training phrase scores (r(45) = 0.5, p < .001). [→ Conrad Borchers 2025](#conrad-borchers-2025)
`q2 i2` Lexical density correlated with end-user satisfaction score (r(45) = 0.36, p = .013). [→ Conrad Borchers 2025 (2)](#conrad-borchers-2025-2)
`q2 i?` Learning curves showed improvements across all three metrics over time, clearest for lexical variation. [→ Conrad Borchers 2025 (3)](#conrad-borchers-2025-3)

## Evidence

### Conrad Borchers 2025

Conrad Borchers, Xiaoyi Tian, Kristy Elizabeth Boyer, Maya Israel. (2025). Combining Log Data and Collaborative Dialogue Features to Predict Project Quality in Middle School AI Education. CSEDM'25: 9th Educational Data Mining in Computer Science Education (CSEDM) Workshop. [doi:10.48550/arXiv.2506.11326](https://doi.org/10.48550/arXiv.2506.11326)

`q2 · i3` · `associational · r1`

Validation analysis correlating intent-level outcome measures with three final project grades (expert rubric score, expert-rated training phrase score, end-user satisfaction from three annotators); none significantly correlated with overall expert ratings. The printed effect size is r = 0.5 (r(45) = 0.5, p < .001) for training phrase count with expert-rated training phrase scores.

> "training phrase count significantly correlated with expert-rated training phrase scores (r(45) = 0.5, p < .001)"

### Conrad Borchers 2025 (2)

Conrad Borchers, Xiaoyi Tian, Kristy Elizabeth Boyer, Maya Israel. (2025). Combining Log Data and Collaborative Dialogue Features to Predict Project Quality in Middle School AI Education. CSEDM'25: 9th Educational Data Mining in Computer Science Education (CSEDM) Workshop. [doi:10.48550/arXiv.2506.11326](https://doi.org/10.48550/arXiv.2506.11326)

`q2 · i2` · `associational · r1`

Same validation analysis for lexical density against end-user satisfaction rated by three independent annotators; the printed effect size is r = 0.36 (r(45) = 0.36, p = .013), which the authors read as richer linguistic content improving end-user experience.

> "lexical density correlated with end-user satisfaction score (r(45) = 0.36, p = .013), indicating richer linguistic content improves end-user experience."

### Conrad Borchers 2025 (3)

Conrad Borchers, Xiaoyi Tian, Kristy Elizabeth Boyer, Maya Israel. (2025). Combining Log Data and Collaborative Dialogue Features to Predict Project Quality in Middle School AI Education. CSEDM'25: 9th Educational Data Mining in Computer Science Education (CSEDM) Workshop. [doi:10.48550/arXiv.2506.11326](https://doi.org/10.48550/arXiv.2506.11326)

`q2 · i?` · `associational · r1`

Learning curve analysis with smoothed running averages across sessions, reported as Figure 3; trends were less consistent for students with high submission counts (>30 intents vs. average 17), described as likely outliers.

> "Figure 3 shows improvements across all metrics over time as students learned to add more phrases and improve lexical choices in the training data for better intent recognition (with the clearest improvement in lexical variation)."

## Discussion


## Related Claims
- [Removing phrase-count-dependent log features substantially lowers predictive accuracy for training phrase count](ablation-without-phrase-count-features.md) — related
- [Domain correlations suggest coherent construct validity, with realism–skill-replication r = 0.85 and effectiveness–engagement r = 0.79](vr-simulator-domain-correlations-construct-validity.md) — related
- [Global rating scores correlate strongly positively with checklist scores (r = 0.78)](global-rating-checklist-correlation-cvc.md) — related
- [Ratings of user-friendliness, input identification, and interaction correlate strongly and positively with overall learning efficacy and experience ratings](usability-aspects-correlate-with-efficacy-experience.md) — related
- [System interaction logs predict training phrase count (productivity) better than dialogue features in collaborative middle school chatbot development](logs-better-predict-training-phrase-count.md) — related
