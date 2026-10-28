---
type: claim
title: Rank-averaged ensembling stabilized predictions but did not outperform the single base model
description: Rank-averaged ensembling stabilized predictions but did not outperform the single base model
id: ensemble-stabilizes-but-not-better-than-model1
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: lu-2024
    resource: "https://doi.org/10.31219/osf.io/3k7z2"
    title: "Lu, Y., Tong, L., & Cheng, Y. (2024). Advanced Knowledge Tracing: Incorporating Process Data and Curricula Information via an Attention-Based Framework for Accuracy and Interpretability. Journal of Educational Data Mining, 16(2). https://osf.io/mdpzc/ [doi:10.31219/osf.io/3k7z2](https://doi.org/10.31219/osf.io/3k7z2)"
    author: "Lu, Y., Tong, L., & Cheng, Y."
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# Rank-averaged ensembling stabilized predictions but did not outperform the single base model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q3 i?` The ensemble achieved the best public evaluation AUC and second-best private AUC, but did not perform better than Model 1. [→ Lu 2024](#lu-2024)

## Evidence

### Lu 2024

Lu, Y., Tong, L., & Cheng, Y. (2024). Advanced Knowledge Tracing: Incorporating Process Data and Curricula Information via an Attention-Based Framework for Accuracy and Interpretability. Journal of Educational Data Mining, 16(2). https://osf.io/mdpzc/ [doi:10.31219/osf.io/3k7z2](https://doi.org/10.31219/osf.io/3k7z2)

`q3 · i? · the article prints no effect size for this finding` · `design · r2`

Results section, Table 4: the rank-averaging ensemble of five trained models reached public AUC 0.79038 and private 0.78969. The authors report "the ensemble model does not perform better than Model 1, suggesting that we can just use Model 1 in practice".

> "However, note that the ensemble model does not perform better than Model 1, suggesting that we can just use Model 1 in practice."

## Discussion


## Related Claims
- [Ablation study: removing any component lowers evaluation AUC, and removing all additional features yields the lowest public and private AUCs](ablation-all-features-maximize-auc.md) — related
- [The single-head base model (Model 1) outperformed the more complex Model 2, suggesting overfitting in the larger architecture](model1-outperforms-complex-model2.md) — related
- [The proposed Transformer-based framework achieved first place in the EDM Cup 2023 with an AUC of 78.969% on the private evaluation dataset](transformer-kt-first-place-edm-cup-2023.md) — related
- [Both pedagogy-expertise-weighted and unanimous-vote ensembles frequently worsen LLM alignment with student learning](ensembling-worsens-llm-alignment-with-learning.md) — related
- [Ensemble modeling of multiple LLM scorers yields performance gains in automated divergent thinking scoring](ensemble-models-performance-gains-llm-scoring.md) — reports the opposite
- Majority-vote ensembling across three runs produced only modest accuracy gains (1% to 5%) with no model showing degradation — related
- [A stacking ensemble of LG, SVM, NB, KNN and XGB achieved the best fine-tuning F1-score (0.88), outperforming individual models such as SVM (0.86)](stacking-ensemble-best-finetuning-f1.md) — related
- [A Soft-Voting Ensemble achieves the best behavioral-dataset attrition prediction (CV F1 = 0.737, test recall = 0.769)](soft-voting-ensemble-behavioral-attrition-f1.md) — related
- [Ensembles of operational raters outperform the LLMs: two raters suffice on average across aspects, but larger ensembles are needed for individual aspects](rater-ensembles-outperform-llms-feedback.md) — related
- [Model self-confidence, weighted probabilistic scoring, and ensemble modeling each significantly improve LLM-based divergent thinking scoring, raising correlation with human judges from r = 0.781 to r = 0.823](llm-scoring-three-techniques-raise-human-judge-correlation.md) — related
- [A multi-polygenic-score GPAΔ predicted achievement no better than the EA4 GPS alone](multi-gps-gpad-no-better-than-ea4-alone.md) — related
- [An ensemble learner outperforms every individual base learner for predicting final exam score and course grade in a large introductory statistics course](ensemble-outperforms-base-learners-exam-grade.md) — related
- [Each generalised plait ensemble (SVM, KNN, DCT) beats the single classifier, majority-vote and stacking ensemble of the same type in perceived task-difficulty classification (e.g., SVM plait error 14.54%, KNN plait 12.84%), though the DCT plait does not beat SVM stacking](plait-ensemble-outperforms-single-and-standard-ensembles.md) — related
