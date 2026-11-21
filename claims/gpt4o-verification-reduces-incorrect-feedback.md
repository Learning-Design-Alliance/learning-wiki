---
type: claim
title: "A GPT-4o verification layer reduced the rate of incorrect feedback from 23% to 1.2% in the feedback-matching pipeline"
description: "A GPT-4o verification layer reduced the rate of incorrect feedback from 23% to 1.2% in the feedback-matching pipeline"
id: gpt4o-verification-reduces-incorrect-feedback
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
---

# A GPT-4o verification layer reduced the rate of incorrect feedback from 23% to 1.2% in the feedback-matching pipeline

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In the human evaluation of feedback matching, 63% of errors received correctly matched feedback, 23% incorrect feedback, and 14% no feedback; adding a GPT-4o judge verification step reduced incorrect feedback from 23% to 1.2%. [→ Muntasir Hoq 2026](#muntasir-hoq-2026)

## Evidence

### Muntasir Hoq 2026

Muntasir Hoq, Griffin Pitts, Bradford Mott, Seung Lee, Jessica Vandenberg, Shuyin Jiao, Narges Norouzi, James Lester, and Bita Akram. (2026). An Explainable AI Assistant for Introductory Programming Education: Improving Feedback Reliability with Instructor-AI Collaboration. arXiv. [doi:10.1007/978-3-032-29744-0_13](https://doi.org/10.1007/978-3-032-29744-0_13)

`q2 · i?` · `design · r2`

Human evaluation by two expert evaluators (inter-rater agreement Cohen's κ = 0.89) of feedback matching on 169 incorrect programs from the fine-tuned problem, after excluding syntax/runtime errors. The paper reports the verification layer "reduced the rate of incorrect feedback from23% to1.2%".

> "Quantitative analysis showed that among all errors from incorrect submissions,63% received correctly matched feedback,23% received incorrect feedback,and14% received no feedback due to low similarity or unmatched patterns."

## Discussion


## Related Claims
- [GPT-4 grading feedback sounds plausible but frequently contains incorrect or misleading statements](gpt4-feedback-plausible-but-misleading.md) — related
- [Bootstrapped self-consistency at temperature 1.0 flags potentially incorrect GPT-4 answers: about half of inconsistent responses were incorrect versus about 5% of consistent ones](bootstrapping-self-consistency-flags-incorrect-answers.md) — related
- [GPT-4-Turbo as an LLM Judge reliably selects better scaffolds and mitigates hallucination errors, while weaker LLM Judges do not](gpt4-turbo-judge-mitigates-hallucinations-weaker-judges-do-not.md) — a broader claim this one bears on
