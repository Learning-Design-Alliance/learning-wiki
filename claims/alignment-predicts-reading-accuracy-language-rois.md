---
type: claim
title: Reading accuracy correlates positively with model-brain alignment in language ROIs, and alignment in left PTG and AG predicts out-of-sample reading accuracy
description: Reading accuracy correlates positively with model-brain alignment in language ROIs, and alignment in left PTG and AG predicts out-of-sample reading accuracy
id: alignment-predicts-reading-accuracy-language-rois
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: gu-2025
    resource: "https://doi.org/10.1038/s41539-025-00337-y"
    title: "Gu, C., Nastase, S. A., Zada, Z., & Li, P. (2025). Reading comprehension in L1 and L2 readers: neurocomputational mechanisms revealed through large language models. npj Science of Learning, 10:46. https://doi.org/10.1038/s41539-025-00337-y"
    author: "Gu, C., Nastase, S. A., Zada, Z., & Li, P."
    q: 3
    i: 2
    kind: associational
    rigour: 2
  - id: gu-2025-2
    resource: "https://doi.org/10.1038/s41539-025-00337-y"
    title: "Gu, C., Nastase, S. A., Zada, Z., & Li, P. (2025). Reading comprehension in L1 and L2 readers: neurocomputational mechanisms revealed through large language models. npj Science of Learning, 10:46. https://doi.org/10.1038/s41539-025-00337-y"
    author: "Gu, C., Nastase, S. A., Zada, Z., & Li, P."
    q: 2
    i: 2
    kind: associational
    rigour: 2
---

# Reading accuracy correlates positively with model-brain alignment in language ROIs, and alignment in left PTG and AG predicts out-of-sample reading accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`–`q3` · `i2` medium
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i2` Reading accuracy correlates positively with alignment in bilateral language ROIs (e.g., left AG r = 0.33, left PTG r = 0.36), but not in visual ROIs (ps > 0.1). [→ Gu 2025](#gu-2025)
`q2 i2` Cross-validated regression models predict reading accuracy in left-out subjects from alignment in left PTG (r = 0.30, p = 0.02) and AG (r = 0.27, p = 0.03). [→ Gu 2025 (2)](#gu-2025-2)

## Evidence

### Gu 2025

Gu, C., Nastase, S. A., Zada, Z., & Li, P. (2025). Reading comprehension in L1 and L2 readers: neurocomputational mechanisms revealed through large language models. npj Science of Learning, 10:46. https://doi.org/10.1038/s41539-025-00337-y

`q3 · i2` · `associational · r2`

Correlation analysis of concatenated accuracy and alignment across 51 L1 and 55 L2 readers (groups combined due to no group differences), with FDR correction (q < 0.05). Significant positive correlations appeared in language ROIs (r = 0.21–0.36); "none of the visual ROIs" showed significant correlations.

> "We found positive correlations between reading accuracy and alignment in bilateral language ROIs (Fig.4a), including the left inferior frontal gyrus (IFG; r = 0.23, p = 0.03), left angular gyrus (AG; r = 0.33, p =0 . 0 0 3 )"

### Gu 2025 (2)

Gu, C., Nastase, S. A., Zada, Z., & Li, P. (2025). Reading comprehension in L1 and L2 readers: neurocomputational mechanisms revealed through large language models. npj Science of Learning, 10:46. https://doi.org/10.1038/s41539-025-00337-y

`q2 · i2` · `associational · r2`

Linear regression models with leave-one-run-out cross-validation predicted reading accuracy from model-brain alignment; predicted and actual scores correlated significantly in left PTG (r = 0.30) and left AG (r = 0.27), FDR-corrected at q < 0.05.

> "This model predicted reading score in left-out subjects in the left PTG ( r = 0.30, p =0 . 0 2 ) a n d A G (r =0 . 2 7 , p =0 . 0 3)"

## Discussion


## Learner Variables
- [Reading and Language](../learner-variables/reading-and-language.md) — predictor: learners who differ on it differ in outcomes

## Related Claims
- [Linguistic abilities shape model-brain alignment in both groups, whereas attentional abilities predict alignment only for L2 readers](expertise-attention-divergent-effects-alignment.md) — related
- [Language dominance interacts with vocabulary size and alerting ability in predicting model-brain alignment in L2 readers](language-dominance-interacts-expertise-l2-alignment.md) — related
- [GPT-2 contextual embeddings predict brain responses comparably in L1 and L2 readers across widespread brain regions](comparable-model-brain-alignment-l1-l2.md) — related
- [Contextual embeddings uniquely contribute to model-brain alignment in frontoparietal and frontotemporal regions for both L1 and L2 readers](unique-contextual-embedding-contribution-both-groups.md) — related
