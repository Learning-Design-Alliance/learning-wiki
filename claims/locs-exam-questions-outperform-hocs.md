---
type: claim
title: Students perform better overall on LOCS exam questions than on HOCS exam questions
description: Students perform better overall on LOCS exam questions than on HOCS exam questions
id: locs-exam-questions-outperform-hocs
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-02
evidence_strength: moderate
newest_evidence: 2023
source_checked: 2026-10-20
recheck_by: 2028
sources:
  - id: deborah-k-anderson-2023
    resource: "https://doi.org/10.1128/jmbe.00151-22"
    title: "Deborah K. Anderson, Michelle Schoenleber, and Stuart Korshavn. (2023). Higher-Order Clicker Questions Engage Students and Prepare Them for Higher-Order Thinking Activities. Journal of Microbiology and Biology Education. https://doi.org/10.1128/jmbe.00151-22"
    author: Deborah K. Anderson, Michelle Schoenleber, and Stuart Korshavn
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Students perform better overall on LOCS exam questions than on HOCS exam questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`
> **Currency** · newest study 2023 · checked against its sources 2026-10-20 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2028: baselines and conditions change

## Subclaims
`q3 i?` Across the mixed ANOVA, the main effect of exam question type was significant, with LOCS exam questions answered better than HOCS exam questions. [→ Deborah K. Anderson 2023](#deborah-k-anderson-2023)

## Evidence

### Deborah K. Anderson 2023

Deborah K. Anderson, Michelle Schoenleber, and Stuart Korshavn. (2023). Higher-Order Clicker Questions Engage Students and Prepare Them for Higher-Order Thinking Activities. Journal of Microbiology and Biology Education. https://doi.org/10.1128/jmbe.00151-22

`q3 · i?` · `causal · r2`

Main effect from the 2 (clicker type) × 2 (exam question type) × 2 (semester) mixed ANOVA on exam performance; the article reports "performance on LOCS exam questions was overall significantly better than performance on HOCS exam questions" with a large effect size (Table 2 prints partial η² = 0.90). Coded `i?` because a partial η² from a mixed ANOVA is not a d-family effect size and is not converted here.

> "performance on LOCS exam questions was overall significantly better than performance on HOCS exam questions, as indicated by a large effect size"

## Studies bearing on this claim

<!-- synthesis:start -->
*Are questions at higher Bloom levels harder for learners, as the taxonomy's hierarchy assumes?* This table gathers the studies behind this claim and the 4 narrower claims that bear on it: **5 distinct studies** (3 associational, 2 causal), `q2`–`q3`, 0 of 5 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Deborah K. Anderson 2023](https://doi.org/10.1128/jmbe.00151-22) | q3 · causal · r2 | i? | this claim |
| [Nero 2021](https://doi.org/10.24191/ajue.v17i4.16222) | q3 · causal · r2 | i? | [After retrieval practice, undergraduates score significantly higher on lower-order thinkin](retrieval-practice-lower-order-questions-outscore-higher-order-questions.md) (supports) |
| [Bates 2013](https://doi.org/10.48550/arxiv.1308.2202) | q2 · associational · r1 | i? | [Students answer lower-taxonomy-category questions more frequently, but only by a factor of](lower-taxonomy-questions-answered-more.md) (qualifies) |
| Madaus 1971 | q2 · associational · r2 | i? | [Proportions of variance explained follow a curvilinear pattern across the six taxonomy lev](curvilinear-variance-pattern-across-taxonomy-levels.md) (qualifies) |
| [Yuan An 2026](https://doi.org/10.48550/arxiv.2609.27063) | q2 · associational · r2 | i? | [LLM-assigned difficulty labels fail to predict empirical item difficulty in classroom retr](llm-difficulty-labels-fail-to-predict-empirical-item-difficulty.md) (counts against) |
<!-- synthesis:end -->

## Discussion

## Related Claims

- [University examination questions concentrate at the lower cognitive levels of Bloom's Taxonomy, dominated by comprehension and knowledge](exam-questions-concentrate-lower-bloom-levels.md) — the general claim this finding bears on, with the studies behind it
- [Semester 2 students outperformed semester 1 students on HOCS exam questions regardless of clicker question type](semester-cohort-difference-hocs-exams.md) — related
- [HOCS clicker questions during learning improve performance on LOCS exam questions more than LOCS clicker questions do](hocs-clickers-improve-locs-exam-performance.md) — related
- [Students perceive LOCS and HOCS clicker questions as equally helpful, despite exam performance differences](students-perceive-clicker-levels-equally-helpful.md) — related
- [After retrieval practice, undergraduates score significantly higher on lower-order thinking questions than on higher-order thinking questions about a studied passage](retrieval-practice-lower-order-questions-outscore-higher-order-questions.md) — possibly the same claim (merge candidate)
