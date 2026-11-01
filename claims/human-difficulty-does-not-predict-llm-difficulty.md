---
type: claim
title: Human-perceived item difficulty (human-human QWK) does not reliably predict LLM scoring difficulty on the same items
description: Human-perceived item difficulty (human-human QWK) does not reliably predict LLM scoring difficulty on the same items
id: human-difficulty-does-not-predict-llm-difficulty
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-01
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: michael-hardy-2026
    resource: "https://arxiv.org/abs/2603.04820"
    title: "Michael Hardy. (2026). Autoscoring Anticlimax: A Meta-analytic Understanding of AI's Short-answer Shortcomings and Wording Weaknesses. https://arxiv.org/abs/2603.04820"
    author: Michael Hardy
    q: 2
    i: "?"
    kind: quant-synthesis
    rigour: 2
---

# Human-perceived item difficulty (human-human QWK) does not reliably predict LLM scoring difficulty on the same items

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · quant-synthesis `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` QWKhum is not reliably associated with LLM QWK in any parameterization, including the Bayesian model (posterior mean near 0 with wide uncertainty). [→ Michael Hardy 2026](#michael-hardy-2026)

## Evidence

### Michael Hardy 2026

Michael Hardy. (2026). Autoscoring Anticlimax: A Meta-analytic Understanding of AI's Short-answer Shortcomings and Wording Weaknesses. https://arxiv.org/abs/2603.04820

`q2 · i?` · `quant-synthesis · r2`

Meta-regression null finding across 890 QWK observations and multiple specifications. The article reports that "QWKhum (humqwk) is not reliably associated with LLM QWK in any parameterization, including the Bayesian model (posterior mean near 0 with wide uncertainty)". No effect size is printed; equivalence was not tested.

> "A central and practically important null result is that QWKhum (humqwk) is not reliably associated with LLM QWK in any parameterization, including the Bayesian model (posterior mean near 0 with wide uncertainty)."

## Discussion


## Related Claims
- [Meaning-dependent (reading) short-answer items reliably lower LLM agreement with human raters compared with more fact-based science items](meaning-dependence-lowers-llm-scoring-agreement.md) — related
- [Decoder-only (GPT-style) architectures underperform encoder-based architectures in short-answer scoring agreement with humans by a substantial margin](decoder-only-underperforms-encoders-scoring.md) — related
- [Fine-tuning several pre-trained LLMs with class balancing, data augmentation, and tailored input modification reaches near human-level automated scoring accuracy on most extended-response mathematics assessment items](fine-tuned-llms-near-human-math-scoring.md) — related
- [LLM Short-Answer Graders Agree With One Human Rater More, and the Other Less, Than the Two Raters Agree With Each Other](llm-short-answer-graders-can-reach-human-rater-agreement.md) — related
