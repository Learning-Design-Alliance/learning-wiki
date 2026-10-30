---
type: claim
title: "Four of eight sentence embedding models (USE-T, USE-DAN, all-MiniLM-L6, all-mpnet-base) correlate significantly highly with experts' evaluations while the remaining four correlate weakly"
description: "Four of eight sentence embedding models (USE-T, USE-DAN, all-MiniLM-L6, all-mpnet-base) correlate significantly highly with experts' evaluations while the remaining four correlate weakly"
id: four-embedding-models-high-expert-correlation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: ijaz-ul-haq-2024
    resource: "https://doi.org/10.1007/s40593-024-00392-3"
    title: "Ijaz Ul Haq, Manoli Pifarré, Estibaliz Fraca. (2024). Novelty Evaluation using Sentence Embedding Models in Open-ended Cocreative Problem-solving. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00392-3"
    author: Ijaz Ul Haq, Manoli Pifarré, Estibaliz Fraca
    q: 3
    i: "?"
    kind: associational
    rigour: 1
---

# Four of eight sentence embedding models (USE-T, USE-DAN, all-MiniLM-L6, all-mpnet-base) correlate significantly highly with experts' evaluations while the remaining four correlate weakly

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q3`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q3 i?` USE-T, USE-DAN, all-MiniLM-L6, and all-mpnet-base had significantly high correlation with experts' evaluations; SRoBERTa-NLI Large, ELMo, InferSent_Glove, and InferSent-FastText showed low correlations. [→ Ijaz Ul Haq 2024](#ijaz-ul-haq-2024)

## Evidence

### Ijaz Ul Haq 2024

Ijaz Ul Haq, Manoli Pifarré, Estibaliz Fraca. (2024). Novelty Evaluation using Sentence Embedding Models in Open-ended Cocreative Problem-solving. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00392-3

`q3 · i?` · `associational · r1`

Correlation analysis in the Findings section over the 588 comparisons; the Discussion reports the remaining four models — SRoBERTa-NLI Large, ELMo, InferSent_Glove, and InferSent-FastText — had low R2 and RMSE values.

> "Our analysis shows that four of the eight embedding models had a significantly high correlation with experts' evaluations. These models include USE-T, USE-DAN, all-MiniLM-L6, and all-mpnet-base."

## Discussion


## Related Claims
- [The eight sentence embedding models produce discrepant similarity scores for the same pairs of cocreative ideas, motivating validation against expert novelty scores](embedding-models-discrepant-similarity-scores.md) — related
- [Probability distribution analysis across low, medium, and high novelty categories confirms that USE-T, USE-DAN, all-MiniLM-L6, and all-mpnet-base align closest with experts' category distributions](probability-distribution-confirms-four-models.md) — related
- [Pre-trained sentence embedding models can evaluate the novelty of open-ended, generic, small datasets of ideas co-generated during classroom PBL cocreation without fine-tuning](sentence-embedding-novelty-evaluation-pbl-cocreation.md) — a broader claim this one bears on
- [USE-T shows the highest correlation with experts' agreed novelty scores, followed by USE-DAN, among sentence embedding models tested on classroom cocreative ideas](use-t-use-dan-highest-expert-correlation.md) — a narrower finding that bears on this claim
