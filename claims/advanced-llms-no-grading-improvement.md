---
type: claim
title: More advanced LLMs (ChatGPT 4.0, Claude 3.0 Haiku) did not improve criterion-based grading over ChatGPT 3.5 with the same prompt
description: More advanced LLMs (ChatGPT 4.0, Claude 3.0 Haiku) did not improve criterion-based grading over ChatGPT 3.5 with the same prompt
id: advanced-llms-no-grading-improvement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: da-wei-zhang-2024
    resource: "https://doi.org/10.1038/s41539-024-00291-1"
    title: "Da-Wei Zhang, Melissa Boey, Yan Yu Tan & Alexis Hoh Sheng Jia. (2024). Evaluating large language models for criterion-based grading from agreement to consistency. npj Science of Learning 9:79. https://doi.org/10.1038/s41539-024-00291-1"
    author: "Da-Wei Zhang, Melissa Boey, Yan Yu Tan & Alexis Hoh Sheng Jia"
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# More advanced LLMs (ChatGPT 4.0, Claude 3.0 Haiku) did not improve criterion-based grading over ChatGPT 3.5 with the same prompt

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` ChatGPT 4.0 achieved moderate agreement (ICC = 0.74) and good consistency (ICC = 0.84), qualitatively comparable to ChatGPT 3.5 with no significant Fisher's Z difference (p > 0.05); Claude 3.0 Haiku yielded ICC = 0.68 agreement and 0.72 consistency. [→ Da-Wei Zhang 2024](#da-wei-zhang-2024)

## Evidence

### Da-Wei Zhang 2024

Da-Wei Zhang, Melissa Boey, Yan Yu Tan & Alexis Hoh Sheng Jia. (2024). Evaluating large language models for criterion-based grading from agreement to consistency. npj Science of Learning 9:79. https://doi.org/10.1038/s41539-024-00291-1

`q2 · i?` · `causal · r1`

Follow-up ICC analyses rerunning Prompt 3 with ChatGPT 4.0 (agreement ICC = 0.74, consistency ICC = 0.84) and Claude 3.0 Haiku, compared to ChatGPT 3.5 via Fisher's Z. The article reports "no sig-niﬁcant difference from ChatGPT 3.5, as indicated by nonsigniﬁcant Fisher’s Z scores (p > 0.05)".

> "Quantitatively, there was no sig-niﬁcant difference from ChatGPT 3.5, as indicated by nonsigniﬁcant Fisher’s Z scores (p > 0.05). Applying the same prompt to Claude 3.0 Haiku yielded comparable interrater agreement of ICC = 0.68 (95% CI [0.44, 0.83]) and interrater consistency of ICC = 0.72 (95% CI [0.50, 0.86])."

## Discussion


## Related Claims
- [Domain-specific knowledge, rather than model complexity or general abilities, limits the precision of LLM criterion-based grading](domain-specific-knowledge-limits-llm-grading-precision.md) — a broader claim this one bears on
- [Prompting ChatGPT 3.5 with detailed IELTS band descriptors achieves moderate interrater agreement and good interrater consistency with official examiner grades](llm-detailed-criteria-prompt-moderate-agreement-good-consistency.md) — related
- [The best prompt showed excellent test-retest reliability (intrarater consistency ICC = 0.89) when rerun in ChatGPT 3.5](llm-grading-excellent-intrarater-consistency.md) — related
- [A teacher without IELTS-specific training showed poorer grading consistency than the best LLM prompt condition](teacher-grading-poorer-consistency-than-llm.md) — related
- [Automated grading achieves excellent agreement with human grading (ICC = 0.893)](automated-grading-excellent-agreement-icc-0893.md) — related
