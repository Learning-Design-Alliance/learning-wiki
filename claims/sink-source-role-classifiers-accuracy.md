---
type: claim
title: Machine-learned Sink/Source classifiers classify information roles with F-scores of 0.914 and 0.908 on noisy student discussion text
description: Machine-learned Sink/Source classifiers classify information roles with F-scores of 0.914 and 0.908 on noisy student discussion text
id: sink-source-role-classifiers-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2014
recheck_by: 2017
sources:
  - id: jaebong-yoo-jihie-kim-2014
    resource: "https://doi.org/10.1007/s40593-013-0010-8"
    title: "Jaebong Yoo & Jihie Kim. (2014). Can Online Discussion Participation Predict Group Project Performance? Investigating the Roles of Linguistic Features and Participation Patterns. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-013-0010-8"
    author: "Jaebong Yoo & Jihie Kim"
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Machine-learned Sink/Source classifiers classify information roles with F-scores of 0.914 and 0.908 on noisy student discussion text

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2014 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2017**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` SVM-based Sink/Source classifiers, trained on human-annotated messages with feature optimization, reached F-scores of 0.914 (sink) and 0.908 (source) on a held-out test set. [→ Jaebong Yoo & Jihie Kim 2014](#jaebong-yoo-jihie-kim-2014)

## Evidence

### Jaebong Yoo & Jihie Kim 2014

Jaebong Yoo & Jihie Kim. (2014). Can Online Discussion Participation Predict Group Project Performance? Investigating the Roles of Linguistic Features and Participation Patterns. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-013-0010-8

`q2 · i?` · `associational · r2`

Classifiers trained on 898 annotated messages (628 training / 270 test) from two semesters; Kappa scores of 92.92% (sink) and 95.95% (source); SVM outperformed J48 and Naïve Bayes, with 10-fold cross-validation F-scores of 0.929 (sink) and 0.921 (source).

> "The F-score of the role classifiers for sink and source on test dataset have improved from 0.871 to 0.914 and from 0.861 to 0.908 respectively by optimizing the features as summarized in Table 6."

## Discussion


## Related Claims
- [A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts](svm-outperforms-dt-rf-cognitive-engagement-prediction.md) — related
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — related
- [SVM and random forest classifiers showed consistent performance in classifying ethnic bias, with F1-scores of 0.71 and 0.70 on the test set](svm-rf-consistent-bias-classification.md) — related
- [SVM classifier on sentence embeddings classifies comment correctness with F1 = 0.914 and Cohen's K = 0.764](svm-embeddings-classify-comments-f1-0914.md) — related
