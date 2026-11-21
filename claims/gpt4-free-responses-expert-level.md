---
type: claim
title: "The author judges 26 of GPT-4's free-response explanations entirely correct at the expert level, while GPT-3.5's wrong-answer explanations erred randomly or self-inconsistently"
description: "The author judges 26 of GPT-4's free-response explanations entirely correct at the expert level, while GPT-3.5's wrong-answer explanations erred randomly or self-inconsistently"
id: gpt4-free-responses-expert-level
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: colin-g-west-2023
    resource: "https://doi.org/10.48550/arXiv.2303.17012"
    title: "Colin G. West. (2023). Advances in apparent conceptual physics reasoning in GPT-4. arXiv preprint. [doi:10.48550/arXiv.2303.17012](https://doi.org/10.48550/arXiv.2303.17012)"
    author: Colin G. West
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: colin-g-west-2023-2
    resource: "https://doi.org/10.48550/arXiv.2303.17012"
    title: "Colin G. West. (2023). Advances in apparent conceptual physics reasoning in GPT-4. arXiv preprint. [doi:10.48550/arXiv.2303.17012](https://doi.org/10.48550/arXiv.2303.17012)"
    author: Colin G. West
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The author judges 26 of GPT-4's free-response explanations entirely correct at the expert level, while GPT-3.5's wrong-answer explanations erred randomly or self-inconsistently

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` 26 of GPT-4's free responses are assessed as entirely correct at the expert level; three contain small unforced errors and one a baffling failure of internal logic. [→ Colin G. West 2023](#colin-g-west-2023)
`q2 i?` GPT-3.5's incorrect explanations were strikingly incorrect, mostly in a random or self-inconsistent manner unlike human errors. [→ Colin G. West 2023 (2)](#colin-g-west-2023-2)

## Evidence

### Colin G. West 2023

Colin G. West. (2023). Advances in apparent conceptual physics reasoning in GPT-4. arXiv preprint. [doi:10.48550/arXiv.2303.17012](https://doi.org/10.48550/arXiv.2303.17012)

`q2 · i?` · `design · r2`

The author's qualitative judgement of GPT-4's free-response explanations on the modified FCI. One response (item 19) contained a mathematical and logic error; item 26's chosen answer was correct only if air resistance were non-negligible, and the model then gave the correct answer when told to assume negligible air resistance.

> "On the whole, we assess that 26 of GPT-4’s responses are entirely correct at the expert level. Three contain small, “unforced” errors–for example, in item 22, it casually calls the motion of the rocket “diagonal,”"

### Colin G. West 2023 (2)

Colin G. West. (2023). Advances in apparent conceptual physics reasoning in GPT-4. arXiv preprint. [doi:10.48550/arXiv.2303.17012](https://doi.org/10.48550/arXiv.2303.17012)

`q2 · i?` · `design · r2`

Qualitative judgement of GPT-3.5's explanations: ten were exactly correct, five had unforced errors, and its 15 wrong-answer explanations erred randomly or self-inconsistently rather than with internal logic from unsound premises.

> "For GPT-3.5’s 15 wrong answers, the short answer explanations were all strikingly incorrect. Almost all erred in a manner which seemed random or self-inconsistent, unlike the incorrect responses of a human"

## Discussion


## Related Claims
- [ChatGPT3.5's FCI free responses split between expert-level accuracy and complete incoherence](chatgpt35-fci-free-response-expert-test.md) — related
- [ChatGPT4 gives no completely confused FCI free responses, with 20 of 23 assessed exactly correct](chatgpt4-fci-free-responses-exactly-correct.md) — related
- [When GPT-4V answered incorrectly, its explanations frequently contained image misunderstandings, reasoning errors, and hallucinations](gpt4v-poor-explanations-incorrect-answers.md) — related
- [An exploratory LLM-judge audit labels knowledge gaps (39.1%) and reasoning errors (26.9%) as the most frequent failure modes among incorrect frontier-model responses](llm-judge-audit-failure-modes.md) — related
- [Health care professionals rated GPT-4V's explanations nearly on par with expert explanations when answers were correct, but overwhelmingly preferred expert explanations when answers were incorrect](explanation-preference-correct-versus-incorrect.md) — related
- [Requiring explanations before answers increases the randomness of LLM incorrect answers and the confidence of correct ones](explanations-randomize-incorrect-boost-confidence.md) — related
- [Humans and GPT-3.5 show guessing preferences among options while GPT-4 shows no discernible preference](guessing-preference-humans-gpt35-gpt4-no-bias.md) — related
- [Expert annotation found nearly 20% of AI interactions contained a definitively incorrect statement, yet 86% of students accepted the AI explanation](ai-peer-interaction-quality-annotations.md) — related
- [Five independent CLASS runs by GPT-5 Thinking yield 100% favorable responses, an entirely expert-like simulated stance](gpt5-class-100-percent-favorable.md) — related
