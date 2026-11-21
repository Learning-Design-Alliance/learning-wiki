---
type: claim
title: AAG system scores align closely with human TA scores on open-ended statistics questions, with Pearson correlations of 0.75 and 0.82
description: AAG system scores align closely with human TA scores on open-ended statistics questions, with Pearson correlations of 0.75 and 0.82
id: aag-ta-score-correlation-open-ended
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: calvin-yeung-2025
    resource: "https://doi.org/10.1007/978-3-031-99264-3_3"
    title: "Calvin Yeung, Jeff Yu, King Chau Cheung, Tat Wing Wong, Chun Man Chan, Kin Chi Wong, and Keisuke Fujii. (2025). A Zero-Shot LLM Framework for Automatic Assignment Grading in Higher Education. arXiv preprint. [doi:10.1007/978-3-031-99264-3_3](https://doi.org/10.1007/978-3-031-99264-3_3)"
    author: Calvin Yeung, Jeff Yu, King Chau Cheung, Tat Wing Wong, Chun Man Chan, Kin Chi Wong, and Keisuke Fujii
    q: 2
    i: 3
    kind: design
    rigour: 2
---

# AAG system scores align closely with human TA scores on open-ended statistics questions, with Pearson correlations of 0.75 and 0.82

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · `i3` large
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i3` Pearson correlations between human TA and AAG scores were 0.75 (Question 1) and 0.82 (Question 2) on 150 independently graded assignments. [→ Calvin Yeung 2025](#calvin-yeung-2025)

## Evidence

### Calvin Yeung 2025

Calvin Yeung, Jeff Yu, King Chau Cheung, Tat Wing Wong, Chun Man Chan, Kin Chi Wong, and Keisuke Fujii. (2025). A Zero-Shot LLM Framework for Automatic Assignment Grading in Higher Education. arXiv preprint. [doi:10.1007/978-3-031-99264-3_3](https://doi.org/10.1007/978-3-031-99264-3_3)

`q2 · i3` · `design · r2`

Comparison of grading on two open-ended STAT1011 questions: both the TA and the AAG system independently graded 150 student assignments. The article reports Pearson correlations of r = 0.75 and r = 0.82, noting direct validation against ground truth was not possible due to the absence of reference grading data.

> "The Pearson correlation coefficients between human and AAG scores for Questions 1 and 2 were 0.75 and 0.82, respectively. These strong correlations indicate that the AAG system produced grading results closely aligned with human evaluations"

## Discussion


## Related Claims
- [LLM marking agrees with human markers on only about half of graded Physics answers, and assigns higher, less variable normalized scores than humans](llm-marking-concordance-with-humans-about-half.md) — related
- [The automated scoring system's agreement with human raters varied widely by dimension, with information fidelity showing a weak, non-significant correlation](yunyi-human-agreement-varies-by-dimension.md) — related
- [GPT-4-based grading of open answers aligns moderately with expert human graders, with an average grade difference of 2.75%](gpt4-grading-aligns-with-human-graders.md) — related
- [Qualitative analysis attributes some human–AAG scoring discrepancies to human grading errors such as overlooking a missing zero or incorrect calculation processes](ta-grading-errors-discrepancy-analysis.md) — related
- [Both LLMs correlate only weakly with human ground-truth scores overall, with agreement strongest for Programming and near-zero for Mathematics](weak-human-llm-grading-agreement.md) — related
