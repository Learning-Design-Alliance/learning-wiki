---
type: claim
title: "Insight's instructor-verified feedback showed higher selectivity and pedagogical suitability than GPT-4o-generated feedback, while GPT-4o showed higher completeness"
description: "Insight's instructor-verified feedback showed higher selectivity and pedagogical suitability than GPT-4o-generated feedback, while GPT-4o showed higher completeness"
id: insight-feedback-beats-gpt4o-selectivity-suitability
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: muntasir-hoq-2026
    resource: "https://doi.org/10.1007/978-3-032-29744-0_13"
    title: "Muntasir Hoq, Griffin Pitts, Bradford Mott, Seung Lee, Jessica Vandenberg, Shuyin Jiao, Narges Norouzi, James Lester, and Bita Akram. (2026). An Explainable AI Assistant for Introductory Programming Education: Improving Feedback Reliability with Instructor-AI Collaboration. arXiv. [doi:10.1007/978-3-032-29744-0_13](https://doi.org/10.1007/978-3-032-29744-0_13)"
    author: Muntasir Hoq, Griffin Pitts, Bradford Mott, Seung Lee, Jessica Vandenberg, Shuyin Jiao, Narges Norouzi, James Lester, and Bita Akram
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: muntasir-hoq-2026-2
    resource: "https://doi.org/10.1007/978-3-032-29744-0_13"
    title: "Muntasir Hoq, Griffin Pitts, Bradford Mott, Seung Lee, Jessica Vandenberg, Shuyin Jiao, Narges Norouzi, James Lester, and Bita Akram. (2026). An Explainable AI Assistant for Introductory Programming Education: Improving Feedback Reliability with Instructor-AI Collaboration. arXiv. [doi:10.1007/978-3-032-29744-0_13](https://doi.org/10.1007/978-3-032-29744-0_13)"
    author: Muntasir Hoq, Griffin Pitts, Bradford Mott, Seung Lee, Jessica Vandenberg, Shuyin Jiao, Narges Norouzi, James Lester, and Bita Akram
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Insight's instructor-verified feedback showed higher selectivity and pedagogical suitability than GPT-4o-generated feedback, while GPT-4o showed higher completeness

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In a two-rater human evaluation (κ = 0.84), Insight exhibited higher selectivity (95% vs. 53%) and pedagogical suitability (100% vs. 47%) than GPT-4o. [→ Muntasir Hoq 2026](#muntasir-hoq-2026)
`q2 i?` GPT-4o achieved higher completeness (87% vs. 80%) than Insight, while both approaches reached 100% perceptivity, almost always identifying at least one instructor-defined error. [→ Muntasir Hoq 2026 (2)](#muntasir-hoq-2026-2)

## Evidence

### Muntasir Hoq 2026

Muntasir Hoq, Griffin Pitts, Bradford Mott, Seung Lee, Jessica Vandenberg, Shuyin Jiao, Narges Norouzi, James Lester, and Bita Akram. (2026). An Explainable AI Assistant for Introductory Programming Education: Improving Feedback Reliability with Instructor-AI Collaboration. arXiv. [doi:10.1007/978-3-032-29744-0_13](https://doi.org/10.1007/978-3-032-29744-0_13)

`q2 · i?` · `design · r2`

Human evaluation comparing Insight and GPT-4o feedback on all incorrect submissions from the week-3 exercise, with two raters (κ = 0.84) using a codebook covering completeness, perceptivity, selectivity, and pedagogical suitability. Insight showed "higher selectivity (95% vs.53%)" and better pedagogical suitability; Figure 8 summarizes the results.

> "However,Insightexhibited higher selectivity (95% vs.53%) and substantially better pedagogical suitability (100% vs.47%), suggesting that GPT-4o was far more prone to introducing extra or misleading issues"

### Muntasir Hoq 2026 (2)

Muntasir Hoq, Griffin Pitts, Bradford Mott, Seung Lee, Jessica Vandenberg, Shuyin Jiao, Narges Norouzi, James Lester, and Bita Akram. (2026). An Explainable AI Assistant for Introductory Programming Education: Improving Feedback Reliability with Instructor-AI Collaboration. arXiv. [doi:10.1007/978-3-032-29744-0_13](https://doi.org/10.1007/978-3-032-29744-0_13)

`q2 · i?` · `design · r2`

Same two-rater human evaluation (κ = 0.84) of week-3 incorrect submissions. The paper reports "GPT-4o achieved higher completeness (87% vs.80%)" and that both approaches reached 100% perceptivity, identifying at least one instructor-defined error.

> "Results show that GPT-4o achieved higher completeness (87% vs.80%), and both approaches reached 100% perceptivity, indicating that they almost always identified at least one instructor-defined error."

## Discussion


## Related Claims
- [GPT-4o-generated student-facing feedback was rated 3 or above on a 5-point scale by two experienced instructors for almost all messages](llm-generated-student-facing-feedback-quality.md) — related
- [Expert raters rate TeachingCoach higher than a GPT-4o baseline on clarity, tone, reflection, and acknowledgment of user input](teachingcoach-outperforms-gpt4o-expert-ratings.md) — related
- [In a human evaluation, the DPO-trained tutor outperforms both human tutors and GPT-4o on perceived student correctness and rubric score, with statistically significant differences](human-evaluation-dpo-beats-human-tutors-and-gpt4o.md) — related
