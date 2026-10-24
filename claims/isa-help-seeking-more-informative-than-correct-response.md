---
type: claim
title: Single instances of help-seeking actions (answer requested, explanation requested) carry more predictive information than single correct or open responses (ISA)
description: Single instances of help-seeking actions (answer requested, explanation requested) carry more predictive information than single correct or open responses (ISA)
id: isa-help-seeking-more-informative-than-correct-response
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
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Single instances of help-seeking actions (answer requested, explanation requested) carry more predictive information than single correct or open responses (ISA)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` By the importance-of-a-single-action measure, single instances of "answer requested" (ISA 1.1293) and "explanation requested" (ISA 1.0983) have higher relative importance than "correct response" (0.9456) and "open response" (0.9933). [→ Lu 2024](#lu-2024)

## Evidence

### Lu 2024

Lu, Y., Tong, L., & Cheng, Y. (2024). Advanced Knowledge Tracing: Incorporating Process Data and Curricula Information via an Attention-Based Framework for Accuracy and Interpretability. Journal of Educational Data Mining, 16(2). https://osf.io/mdpzc/ [doi:10.31219/osf.io/3k7z2](https://doi.org/10.31219/osf.io/3k7z2)

`q2 · i? · the article prints no effect size for this finding` · `design · r2`

Interpretation analysis of attention weights from the single-head Transformer Encoder on ASSISTments action logs (Table 6). The authors report "the ISA of “answer requested” and “explanation requested” are 1.1293 and 1.0983 respectively", exceeding correct and open responses.

> "the ISA of “answer requested” and “explanation requested” are 1.1293 and 1.0983 respectively, and higher than both “correct response” and “open response.”"

## Discussion


## Related Claims
- [In artificial action logs, \"answer requested\" yields the lowest average predicted probability of a correct end-of-unit response, below even \"wrong response\"](answer-requested-lowest-main-effect.md) — related
- [A wrong response preceding a help request is associated with a higher predicted probability of a correct end-of-unit response than the request alone](wrong-then-request-joint-effect-higher.md) — related
- [NCA scores of IIU input vectors order action types identically to the main-effects ordering (Spearman's ρ = 1)](nca-scores-align-with-main-effects.md) — related
- [The Help Tutor improved students' in-tutor help-seeking behavior, but only for a subset of help-seeking action types](help-tutor-improved-in-tutor-help-seeking.md) — related
