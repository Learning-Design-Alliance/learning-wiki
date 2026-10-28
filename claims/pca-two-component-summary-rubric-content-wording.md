---
type: claim
title: "A principal component analysis distills the seven-criterion summary rubric into two components, Content and Wording, explaining approximately 73% of shared variance"
description: "A principal component analysis distills the seven-criterion summary rubric into two components, Content and Wording, explaining approximately 73% of shared variance"
id: pca-two-component-summary-rubric-content-wording
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: morris-2025
    resource: "https://doi.org/10.1007/s40593-024-00395-0"
    title: "Morris, W., Crossley, S., Holmes, L., Ou, C., Dascalu, M., & McNamara, D. (2025). Formative Feedback on Student-Authored Summaries in Intelligent Textbooks Using Large Language Models. International Journal of Artificial Intelligence in Education, 35, 1022–1043. https://doi.org/10.1007/s40593-024-00395-0"
    author: "Morris, W., Crossley, S., Holmes, L., Ou, C., Dascalu, M., & McNamara, D."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: morris-2025-2
    resource: "https://doi.org/10.1007/s40593-024-00395-0"
    title: "Morris, W., Crossley, S., Holmes, L., Ou, C., Dascalu, M., & McNamara, D. (2025). Formative Feedback on Student-Authored Summaries in Intelligent Textbooks Using Large Language Models. International Journal of Artificial Intelligence in Education, 35, 1022–1043. https://doi.org/10.1007/s40593-024-00395-0"
    author: "Morris, W., Crossley, S., Holmes, L., Ou, C., Dascalu, M., & McNamara, D."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A principal component analysis distills the seven-criterion summary rubric into two components, Content and Wording, explaining approximately 73% of shared variance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The seven analytic rubric scores reduce to two principal components, Content (details, main point, objective language, cohesion) and Wording (paraphrasing, language beyond the source), explaining about 73% of shared variance. [→ Morris 2025](#morris-2025)
`q2 i?` Text length did not load into the first components and was removed. [→ Morris 2025 (2)](#morris-2025-2)

## Evidence

### Morris 2025

Morris, W., Crossley, S., Holmes, L., Ou, C., Dascalu, M., & McNamara, D. (2025). Formative Feedback on Student-Authored Summaries in Intelligent Textbooks Using Large Language Models. International Journal of Artificial Intelligence in Education, 35, 1022–1043. https://doi.org/10.1007/s40593-024-00395-0

`q2 · i?` · `design · r2`

PCA on z-score normalized human rubric scores for 4,690 summaries; Bartlett's test was significant (χ2(4690) = 11,513.99, p <.001) and overall KMO = 0.87. The authors report the solution "explained approximately 73% of the shared variance in the data from the initial PCA."

> "Considering this break, we decided on a 2-component solution when developing the PCA. These 2 components explained approximately 73% of the shared variance in the data from the initial PCA."

### Morris 2025 (2)

Morris, W., Crossley, S., Holmes, L., Ou, C., Dascalu, M., & McNamara, D. (2025). Formative Feedback on Student-Authored Summaries in Intelligent Textbooks Using Large Language Models. International Journal of Artificial Intelligence in Education, 35, 1022–1043. https://doi.org/10.1007/s40593-024-00395-0

`q2 · i?` · `design · r2`

Component interpretation from the Methods dimensionality-reduction section: Content combines details, main point, objective language use, and cohesion; Wording combines paraphrasing and language beyond the source. Per the article, "Text length did not load into the first components and was removed."

> "The first component was related to Content (i.e., Component 1), and the analytic scales of details, main point, objective language use, and cohesion were combined into a weighted score. The analytic scales for paraphrasing and language beyond the source were combined into a weighted score designated as Wording (i.e., Component 2). Text length did not load into the first components and was removed."

## Discussion


## Related Claims
- [On professional OpenStax textbook summaries, matched summaries scored significantly higher than unmatched ones, with a larger effect for Content (d = 1.56) than Wording (d = 0.938)](matched-unmatched-summary-validity-large-effects.md) — related
- [Including the textbook source text in the model input improves automated summary scoring accuracy, with Longformer explaining 82% of Content and 70% of Wording score variance versus 67% and 41% for summary-only RoBERTa](longformer-source-text-outperforms-roberta-summary-scoring.md) — related
