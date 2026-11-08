---
type: claim
title: "Proportional bias: AI assigned relatively higher scores at the lower end of the performance distribution"
description: "Proportional bias: AI assigned relatively higher scores at the lower end of the performance distribution"
id: proportional-bias-ai-higher-scores-lower-end
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: gao-xiaoxing-2026
    resource: "https://doi.org/10.2196/95578"
    title: "Gao Xiaoxing, Huang Xiaoming, Hu Rongrong, Zhang Li, Liu Huiting, Zhang Bingqing, Wei Chong, Qiu Wei, Zhang Mengyu, Sun Xuefeng. (2026). Evaluating Large Language Model–Based Automated Scoring in a Voice-Based Virtual Standardized Patient Platform for Medical Students: Cross-Sectional Agreement Study. JMIR Medical Education. https://doi.org/10.2196/95578"
    author: Gao Xiaoxing, Huang Xiaoming, Hu Rongrong, Zhang Li, Liu Huiting, Zhang Bingqing, Wei Chong, Qiu Wei, Zhang Mengyu, Sun Xuefeng
    q: 3
    i: "?"
    kind: associational
    rigour: 2
---

# Proportional bias: AI assigned relatively higher scores at the lower end of the performance distribution

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Mixed-effects Bland-Altman analysis showed a non-significant mean bias of 1.26 points but significant proportional bias (β_proportional bias=−0.55; P<.001). [→ Gao Xiaoxing 2026](#gao-xiaoxing-2026)

## Evidence

### Gao Xiaoxing 2026

Gao Xiaoxing, Huang Xiaoming, Hu Rongrong, Zhang Li, Liu Huiting, Zhang Bingqing, Wei Chong, Qiu Wei, Zhang Mengyu, Sun Xuefeng. (2026). Evaluating Large Language Model–Based Automated Scoring in a Voice-Based Virtual Standardized Patient Platform for Medical Students: Cross-Sectional Agreement Study. JMIR Medical Education. https://doi.org/10.2196/95578

`q3 · i?` · `associational · r2`

Mixed-effects Bland-Altman analysis of the 92 paired AI-faculty score sets. Mean bias (1.26 points, 95% CI −0.48 to 3.01; P=.16) did not reach significance, but "Proportional bias was present," with 95% limits of agreement from −4.95 to 7.48 (width=12.43 points).

> "Proportional bias was present (β_proportional bias=−0.55; P<.001), with AI assigning relatively higher scores at the lower end of the performance distribution (Figure 3)."

## Discussion


## Related Claims
- [ChatGPT 3.5 grading with the best prompt was significantly lower than official IELTS examiner grades, indicating systematic bias in absolute grading](llm-grades-significantly-lower-than-examiners.md) — reports the opposite
- [In one study of five LLMs scoring 60 undergraduate essays on IELTS rubric dimensions, systematic underestimation of human scores was the dominant bias trend, with some models also compressing scores into a narrow range](llm-essay-scoring-systematic-underestimation.md) — related
- [Automated judging aligns strongly with three domain experts (r = 0.82 for role fidelity) but exhibits a conservative bias, scoring ethical deviation 0.08 points lower than humans](automated-judge-human-alignment-conservative-bias.md) — related
- [Bland–Altman analysis shows systematic bias and wide limits of agreement, with AI tending to assign slightly higher scores than the expert across most criteria](bland-altman-ai-higher-scores-poor-interchangeability.md) — related
- [Bland–Altman analysis shows peer and instructor scores agree closely, with limits of agreement from -1.17 to +1.16](bland-altman-agreement-peer-instructor.md) — related
