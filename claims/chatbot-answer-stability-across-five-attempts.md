---
type: claim
title: "Chatbot answers were largely stable across 5 successive attempts, with all chatbots answering 104 (52%) of the 200 questions correctly in every attempt"
description: "Chatbot answers were largely stable across 5 successive attempts, with all chatbots answering 104 (52%) of the 200 questions correctly in every attempt"
id: chatbot-answer-stability-across-five-attempts
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: bolgova-o-2025
    resource: "https://doi.org/10.2196/67244"
    title: "Bolgova O, Shypilova I, Mavrych V. (2025). Large Language Models in Biochemistry Education: Comparative Evaluation of Performance. JMIR Medical Education. https://doi.org/10.2196/67244"
    author: Bolgova O, Shypilova I, Mavrych V.
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Chatbot answers were largely stable across 5 successive attempts, with all chatbots answering 104 (52%) of the 200 questions correctly in every attempt

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Responses were highly repeatable: Claude's and Gemini's answers in subsequent attempts were identical to the first, and all chatbots answered 104 of the 200 questions correctly in all attempts. [→ Bolgova O 2025](#bolgova-o-2025)

## Evidence

### Bolgova O 2025

Bolgova O, Shypilova I, Mavrych V. (2025). Large Language Models in Biochemistry Education: Comparative Evaluation of Performance. JMIR Medical Education. https://doi.org/10.2196/67244

`q2 · i?` · `associational · r2`

Consistency analysis of the 5 successive attempts per chatbot (4000 LLM answers analyzed), with attempts matched against previous ones for repeated and correct answers. The article reports "all chatbots answered 104 (52%) of the 200 questions correctly in all attempts"; GPT-4 showed some variation, with 91.5%-94.5% coincidence with previous attempts.

> "Interestingly, all chatbots answered 104 (52%) of the 200 questions correctly in all attempts."

## Discussion


## Related Claims
- [Only 29.5% of questions were answered correctly by all four current LLMs across all attempts](only-29-5-percent-answered-correctly-by-all-llms.md) — related
- [All three LLMs show near-perfect answer reproducibility under repeated API testing at zero temperature, highest for Claude 3.5 Sonnet (99.9%)](llm-kmle-reproducibility-near-perfect.md) — related
- [Chatbot responses show near-perfect repeatability across no-feedback attempts (κ 0.967-1.000)](chatbot-response-consistency-kappa-near-perfect.md) — a broader claim this one bears on
- [Claude, Copilot, and Gemini showed model-specific topic strengths and weaknesses and lower cross-attempt reliability than GPT-4o](claude-copilot-gemini-topic-strengths-reliability.md) — related
