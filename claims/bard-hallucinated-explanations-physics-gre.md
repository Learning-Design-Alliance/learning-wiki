---
type: claim
title: Among questions Bard answered correctly, some correct options were chosen by chance with fabricated explanations, and Bard hallucinated numerical values for variables
description: Among questions Bard answered correctly, some correct options were chosen by chance with fabricated explanations, and Bard hallucinated numerical values for variables
id: bard-hallucinated-explanations-physics-gre
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: pranav-gupta-2023
    resource: "https://doi.org/10.48550/arXiv.2312.04613"
    title: "Pranav Gupta. (2023). Testing an LLM's performance on the Physics GRE: some observations. [doi:10.48550/arXiv.2312.04613](https://doi.org/10.48550/arXiv.2312.04613)"
    author: Pranav Gupta
    q: 1
    i: "?"
    kind: qualitative
    rigour: 1
---

# Among questions Bard answered correctly, some correct options were chosen by chance with fabricated explanations, and Bard hallucinated numerical values for variables

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · qualitative `r1` · `q1`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q1 i?` On some correctly answered questions Bard fabricated explanations and chose the correct option only by chance; in some questions it hallucinated numerical values for variables where no option was numerical. [→ Pranav Gupta 2023](#pranav-gupta-2023)

## Evidence

### Pranav Gupta 2023

Pranav Gupta. (2023). Testing an LLM's performance on the Physics GRE: some observations. [doi:10.48550/arXiv.2312.04613](https://doi.org/10.48550/arXiv.2312.04613)

`q1 · i?` · `qualitative · r1`

Author's qualitative observation from the same single-session Bard evaluation of the Physics GRE. The article reports that among correct answers, Bard "made up incorrect explanations" and chose correctly "solely due to chance", and separately hallucinated numerical values for variables in questions with no numerical options.

> "Among the questions answered correctly, Bard made up incorrect explanations, albeit ending choosing the correct option solely due to chance."

## Discussion


## Related Claims
- [Bard answered 26 of 98 Physics GRE questions correctly, earning a raw score of 8 out of 100 and placing in the bottom 2% of test-takers](bard-bottom-2-percent-physics-gre.md) — related
- [Agreement between GPT-4's answers and human-curated answers based on its explanations was low (κ=0.504), with frequent answer-explanation mismatches](gpt4-answer-explanation-consistency-low-kappa.md) — related
- [A relatively high percentage of correct-choice-incorrect-explanation (CI) answers appeared across many problems, revealing false positives invisible to answer-only scoring](high-percentage-ci-answers-free-response.md) — related
- [Bard's safety guardrails blocked image upload for 2 of the 100 Physics GRE questions](bard-image-upload-failures-two-of-100.md) — related
