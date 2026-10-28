---
type: claim
title: On new crowd-sourced Prolific summaries, the Content model generalized well (r = 0.70) but the Wording model predicted human scores poorly (r = 0.29)
description: On new crowd-sourced Prolific summaries, the Content model generalized well (r = 0.70) but the Wording model predicted human scores poorly (r = 0.29)
id: prolific-generalizability-content-strong-wording-weak
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: mixed
newest_evidence: 2025
sources:
  - id: morris-2025
    resource: "https://doi.org/10.1007/s40593-024-00395-0"
    title: "Morris, W., Crossley, S., Holmes, L., Ou, C., Dascalu, M., & McNamara, D. (2025). Formative Feedback on Student-Authored Summaries in Intelligent Textbooks Using Large Language Models. International Journal of Artificial Intelligence in Education, 35, 1022–1043. https://doi.org/10.1007/s40593-024-00395-0"
    author: "Morris, W., Crossley, S., Holmes, L., Ou, C., Dascalu, M., & McNamara, D."
    q: 2
    i: 3
    kind: design
    rigour: 2
  - id: morris-2025-2
    resource: "https://doi.org/10.1007/s40593-024-00395-0"
    title: "Morris, W., Crossley, S., Holmes, L., Ou, C., Dascalu, M., & McNamara, D. (2025). Formative Feedback on Student-Authored Summaries in Intelligent Textbooks Using Large Language Models. International Journal of Artificial Intelligence in Education, 35, 1022–1043. https://doi.org/10.1007/s40593-024-00395-0"
    author: "Morris, W., Crossley, S., Holmes, L., Ou, C., Dascalu, M., & McNamara, D."
    q: 2
    i: 2
    kind: design
    rigour: 2
---

# On new crowd-sourced Prolific summaries, the Content model generalized well (r = 0.70) but the Wording model predicted human scores poorly (r = 0.29)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2` · `i2`–`i3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i3` The Content model showed a strong correlation with human scores on the Prolific dataset, r(123) = 0.70, p <.001. [→ Morris 2025](#morris-2025)
`q2 i2` The Wording model did a poorer job predicting human scores on the Prolific dataset, r(123) = 0.29, p =.001. [→ Morris 2025 (2)](#morris-2025-2)

## Evidence

### Morris 2025

Morris, W., Crossley, S., Holmes, L., Ou, C., Dascalu, M., & McNamara, D. (2025). Formative Feedback on Student-Authored Summaries in Intelligent Textbooks Using Large Language Models. International Journal of Artificial Intelligence in Education, 35, 1022–1043. https://doi.org/10.1007/s40593-024-00395-0

`q2 · i3` · `design · r2`

Post-hoc generalizability test on 113 summaries of OpenStax Macroeconomics sections written by 60 Prolific participants, scored by two expert raters with the original rubric. The Content model's accuracy was lower than on the original dataset but remained strong, with printed correlation r = 0.70 (r(123) = 0.70, p <.001).

> "Pearson's product-moment correlations showed a strong correlation between predictions and human scores for Content r(123) = 0.70, p <.001."

### Morris 2025 (2)

Morris, W., Crossley, S., Holmes, L., Ou, C., Dascalu, M., & McNamara, D. (2025). Formative Feedback on Student-Authored Summaries in Intelligent Textbooks Using Large Language Models. International Journal of Artificial Intelligence in Education, 35, 1022–1043. https://doi.org/10.1007/s40593-024-00395-0

`q2 · i2` · `design · r2`

Same Prolific evaluation: the Wording model's predictions, though better than chance, correlated only r = 0.29 with human PCA scores (r(123) = 0.29, p =.001), showing reduced accuracy compared to the training set.

> "However, the Wording model did a poorer job at predicting human scores r(123) = 0.29, p =.001."

## Discussion


## Related Claims
- [On professional OpenStax textbook summaries, matched summaries scored significantly higher than unmatched ones, with a larger effect for Content (d = 1.56) than Wording (d = 0.938)](matched-unmatched-summary-validity-large-effects.md) — related
- [Rubric-aligned NLP features for evidence and organization outperform proxy-feature and coherence baselines and generalize across datasets](rubric-aligned-nlp-features-outperform-proxies.md) — a broader claim this one bears on
- [Wise-crowd content models for summary assessment correlate well with an educational rubric, manually and via two automated NLP methods](wise-crowd-content-model-summary-assessment.md) — related
