---
type: claim
title: The GPT-4o question generator repeatedly asked the same questions, an issue the authors attribute to zero temperature and prompts that did not emphasize adapting to learner responses
description: The GPT-4o question generator repeatedly asked the same questions, an issue the authors attribute to zero temperature and prompts that did not emphasize adapting to learner responses
id: cl-gpt4o-repeated-questions-limitation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
sources:
  - id: tokio-uchida-2026
    title: Tokio Uchida 2026
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# The GPT-4o question generator repeatedly asked the same questions, an issue the authors attribute to zero temperature and prompts that did not emphasize adapting to learner responses

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Several participants reported being repeatedly asked the same questions and being able to predict the next question, and the authors found cases of repeated questions, attributing the issue to the model's deterministic output and insufficiently adaptive prompts. [→ Tokio Uchida 2026](#tokio-uchida-2026)

## Evidence

### Tokio Uchida 2026

Tokio Uchida, Ko Watanabe, Andrew Vargo, Shoya Ishimaru, Ralph L. Rose, Ayaka Sugawara, Andreas Dengel, and Koichi Kise. 2026. Empowering Vocabulary Learning Through Teaching AI: Using LLMs as a Student to Perform Learning by Teaching in Vocabulary Acquisition. In The Augmented Humans International Conference 2026 (AHs 2026). https://doi.org/10.1145/3795011.3797361

`q2 · i?` · `causal · r1`

Qualitative inspection of dialogue logs (Appendix C) in the ten-student experiment found 'cases where the same questions were asked repeatedly'; the authors attribute this to the model's deterministic output rather than reporting a learning outcome test.

> "This issue may stem from the model's deterministic, repetitive output, as the temperature hyperparameter of GPT-4o was set to zero, and the prompts did not strongly emphasize adapting to the learner's responses."

## Discussion


## Related Claims
- [All three LLMs show near-perfect answer reproducibility under repeated API testing at zero temperature, highest for Claude 3.5 Sonnet (99.9%)](llm-kmle-reproducibility-near-perfect.md) — related
