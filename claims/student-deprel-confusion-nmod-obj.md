---
type: claim
title: Student annotation errors concentrate in specific dependency relations, most mislabeling nmod and most misapplying obj
description: Student annotation errors concentrate in specific dependency relations, most mislabeling nmod and most misapplying obj
id: student-deprel-confusion-nmod-obj
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: lauren-levine-2025
    resource: "https://doi.org/10.48550/arXiv.2504.18718"
    title: "Lauren Levine, Junghyun Min, and Amir Zeldes. (2025). Building UD Cairo for Old English in the Classroom. [doi:10.48550/arXiv.2504.18718](https://doi.org/10.48550/arXiv.2504.18718)"
    author: Lauren Levine, Junghyun Min, and Amir Zeldes
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Student annotation errors concentrate in specific dependency relations, most mislabeling nmod and most misapplying obj

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In the confusion matrix of gold vs student labels, nmod was the relation mislabeled by students the most (6 times) and obj was the label most misapplied by students (9 times), with confusions stemming largely from misunderstanding nmod:poss with possessive case. [→ Lauren Levine 2025](#lauren-levine-2025)

## Evidence

### Lauren Levine 2025

Lauren Levine, Junghyun Min, and Amir Zeldes. (2025). Building UD Cairo for Old English in the Classroom. [doi:10.48550/arXiv.2504.18718](https://doi.org/10.48550/arXiv.2504.18718)

`q2 · i?` · `design · r2`

Disagreement analysis comparing final gold dependency labels with student annotations via a confusion matrix (Figure 2), with deprel subtypes collapsed and punct excluded. The authors also report obj was misapplied a total of 9 times across nmod, obl, orphan, conj, det, and xcomp.

> "The dependency relation that was mislabeled by students the most was nmod, which was mislabeled 6 times (3 times as det, 2 times as obj, and 1 time as nsubj). These confusions primarily stemmed from students not understanding when to apply the nmod:poss subtype when possessive case was involved in the sentence."

## Discussion


## Related Claims
- [Novice student annotators with minimal UD instruction achieve attachment scores comparable to experienced annotators on an Old English treebanking assignment](novice-annotators-comparable-ud-accuracy.md) — related
- [Provide-Info, Request-Info, and Other are the dialogue act labels most commonly confused by both GPT-4 and T5 classifiers.](provide-info-request-info-other-most-confused-labels.md) — related
