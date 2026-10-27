---
type: claim
title: "The star-to-sentiment labeling rule agrees with human review-level labels at Cohen's kappa 0.66 with 82% accuracy on 3,000 RateMyProfessor teacher reviews"
description: "The star-to-sentiment labeling rule agrees with human review-level labels at Cohen's kappa 0.66 with 82% accuracy on 3,000 RateMyProfessor teacher reviews"
id: star-label-rule-kappa-066-82-percent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: esteban-u-vega-barajas-2026
    resource: "https://doi.org/10.48550/arxiv.2607.11873"
    title: "Esteban U. Vega Barajas. (2026). A Durability and Cross-Language Transfer Benchmark for a Validated Teaching-Feedback Classification Protocol. https://arxiv.org/abs/2607.11873 [doi:10.48550/arxiv.2607.11873](https://doi.org/10.48550/arxiv.2607.11873)"
    author: Esteban U. Vega Barajas
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The star-to-sentiment labeling rule agrees with human review-level labels at Cohen's kappa 0.66 with 82% accuracy on 3,000 RateMyProfessor teacher reviews

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Star-derived English sentiment labels are a reasonable but imperfect proxy, agreeing with EduRABSA human labels at kappa 0.66 and 82% accuracy, with the neutral class weakest. [→ Esteban U. Vega Barajas 2026](#esteban-u-vega-barajas-2026)

## Evidence

### Esteban U. Vega Barajas 2026

Esteban U. Vega Barajas. (2026). A Durability and Cross-Language Transfer Benchmark for a Validated Teaching-Feedback Classification Protocol. https://arxiv.org/abs/2607.11873 [doi:10.48550/arxiv.2607.11873](https://doi.org/10.48550/arxiv.2607.11873)

`q2 · i?` · `design · r2`

Validation of the star-to-sentiment labeling rule against EduRABSA's independently annotated review-level human sentiment labels, on the 3,000 RateMyProfessor teacher reviews within EduRABSA that share the star-rating scale of the assembled corpus. The article reports "Cohen’s kappa 0.66, with 82% accuracy" and notes "The neutral class is the weakest, because human-neutral reviews scatter across star levels".

> "review-level sentiment at Cohen’s kappa 0.66, with 82% accuracy. The neutral class is the weakest, because human-neutral reviews scatter across star levels."

## Discussion


## Related Claims

- An open-source Llama3 model reached substantial agreement with a human coder when sentiment-labeling pre-extracted student reflection quotes — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [An LLM-based AI Evaluator agrees with expert human raters on collaboration transcripts at a level similar to inter-expert agreement](llm-evaluator-agreement-matches-expert-raters.md) — related
- [Sentiment classification transfers to English under the unchanged protocol, with a frozen multilingual encoder the strongest arm at wF1 0.73 and LLMs matching it only with few-shot prompting](english-sentiment-transfer-encoder-strongest.md)
- [The rule-based recipe annotation system reaches near-perfect inter-annotator agreement (Cohen's Kappa 0.85) and average accuracy 0.95 in a validation on sampled recipe segments.](relex-annotation-validation-kappa-accuracy.md) — related
