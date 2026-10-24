---
type: claim
title: Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested
description: Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested
id: within-judge-stability-llm-rubric
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
newest_evidence: 2026
source_checked: 2026-10-20
recheck_by: 2029
sources:
  - id: md-zabirul-islam-2026
    resource: "https://doi.org/10.48550/arxiv.2606.20608"
    title: "Md Zabirul Islam, Md Motaleb Hossen Manik, and Ge Wang. (2026). CourseBlueprint: A Structured Pipeline for Adaptive Pedagogical Video Generation Grounded in Course Corpora. arXiv preprint. https://arxiv.org/abs/2606.20608 [doi:10.48550/arxiv.2606.20608](https://doi.org/10.48550/arxiv.2606.20608)"
    author: Md Zabirul Islam, Md Motaleb Hossen Manik, and Ge Wang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-20 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across thirty ablation cells, twenty-six had identical scores across three judge repetitions, with mean per-cell standard deviation 0.063 and Krippendorff's alpha approximately 0.97; cross-judge-family agreement is treated as a separate limitation. [→ Md Zabirul Islam 2026](#md-zabirul-islam-2026)

## Evidence

### Md Zabirul Islam 2026

Md Zabirul Islam, Md Motaleb Hossen Manik, and Ge Wang. (2026). CourseBlueprint: A Structured Pipeline for Adaptive Pedagogical Video Generation Grounded in Course Corpora. arXiv preprint. https://arxiv.org/abs/2606.20608 [doi:10.48550/arxiv.2606.20608](https://doi.org/10.48550/arxiv.2606.20608)

`q2 · i?` · `design · r2`

Reliability analysis of a single Gemini-Flash judge scored n=3 times across thirty cells (five topics, three PCK dimensions, two variants). The article reports mean per-cell standard deviation 0.063 and alpha approximately 0.97; these are reliability statistics, not effect sizes.

> "The mean per-cell standard deviation is 0.063, and Krippendorff’s α [44], treating repetitions as raters, is approximately 0.97. Thus, within-judge variance is negligible at this rubric resolution, while cross-judge-family agreement remains the next required check."

## Discussion


## Related Claims

- [Removing the engagement contract reduces judged engagement, adaptive scores, readability, and engagement-move counts in pedagogical video generation](engagement-contract-ablation-reduces-pck-scores.md) — related
- [LLM-as-judge automated evaluation can achieve human-level agreement when carefully validated](llm-as-judge-human-level-agreement-with-validation.md) — a broader claim this one bears on
- Multimodal LLMs show moderate cross-model agreement on which image-Required items are solvable, with within-family agreement exceeding cross-family agreement — related
- [Same-model LLM configuration pairs agree more than cross-model pairs, and agreement decreases monotonically as temperature difference increases](llm-pairwise-agreement-model-type-temperature.md) — related
- [AI grading of the exam is highly stable across five independent runs at the total-score level (ICC(A,1) = 0.967), with lower but still strong cell-level stability (ICC(A,1) = 0.836)](ai-grading-run-to-run-reliability-icc.md) — related
- [Cross-model agreement on assertions is moderate (median 0.401) and higher among construct-derived than corpus-derived assertions](assertion-cross-model-agreement-moderate-median-0401.md) — related
- [Adding a cross-model agreement filter improves performance for the top three LLM annotators](cross-model-agreement-filter-improves-top-annotators.md) — related
- [Gemini 2.0 Flash validated as a reliable LLM annotator of feedback focus types](gemini-flash-reliable-feedback-focus-annotator.md) — related
- [Gemini and Gemini Pro show the highest internal grading consistency across file upload volumes, with no clear monotonic lost-in-the-middle effect](gemini-highest-consistency-across-file-volumes.md) — related
- [LLM difficulty predictions for fraction items are less stable across repeated runs than for the overall item set](llm-fraction-predictions-run-to-run-instability.md) — related
- [LLM-based essay grading is not fully reproducible: repeated ChatGPT sessions on the same submissions show only moderate consistency (Krippendorff's alpha 0.625)](llm-grading-session-variability-limited-reproducibility.md) — related
- [Unanimous-fail panels alone reduced benchmark activation by approximately 40% on average for three Critical evaluators, but were insufficient on their own](unanimous-panels-40-percent-activation-reduction.md) — related
- [In the public TutorBench sample, agency-oriented rubric criteria are most concentrated in the active-learning use case (agency-dimension density 0.720, agency-skill density 0.411)](tutorbench-rubrics-encode-agency-active-learning-highest.md) — related
- [Judge and crowd broadly agree on which criteria matter, but the judge's near-identical top scores make its ranking of strong systems essentially random](judge-crowd-agree-on-criteria-but-scores-separate-nothing.md) — related
- [LLM-as-a-judge ratings found only small, incremental differences between systems, with ceiling effects on several criteria](llm-judge-small-incremental-differences-ceiling.md) — related
- [LLM grading patterns cluster into six groups aligned with vendor families, with highest correlations within same-vendor model families](llm-grading-vendor-specific-six-clusters.md) — related
- [The LLM judge agrees with human annotators at 87.7% (κ = 0.842) on consensus pairs, but severity-rating agreement is uneven and medium-tier boundaries are uncertain](judge-calibration-labels-strong-severity-uneven.md)
- [The LLM-judge separates weak submissions but its ranking of the strongest systems has almost no agreement with crowd ranking (Spearman ρ = −0.17)](llm-judge-ranks-strongest-systems-poorly.md) — related
- [LLM configurations show high within-configuration reliability when re-coding the same chat log dataset, with ChatGPT4o/temperature=0 highest](llm-within-configuration-reliability-high.md) — related
- [Lowering an LLM's temperature setting is one lever for improving output consistency](lowering-temperature-improves-llm-consistency.md) — related
- [Human-shadow prompting generates broad psychometric variance while AI-assistant responses are uniform](human-shadow-prompting-generates-psychometric-variance.md) — related
- [Cognitive artifact scoring in the digital workbook achieved high intercoder reliability, with average Spearman's rho of 0.97 overall](high-intercoder-reliability-workbook-scoring.md) — related
