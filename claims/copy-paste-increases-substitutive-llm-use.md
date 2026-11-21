---
type: claim
title: Enabling copy and paste increases LLM use during learning, and specifically increases substitutive solution requests but not explanation requests
description: Enabling copy and paste increases LLM use during learning, and specifically increases substitutive solution requests but not explanation requests
id: copy-paste-increases-substitutive-llm-use
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: matthias-lehmann-2024
    resource: "https://doi.org/10.48550/arXiv.2409.09047"
    title: "Matthias Lehmann, Philipp B. Cornelius, and Fabian J. Sting. (2024). AI Meets the Classroom: When Do Large Language Models Harm Learning? arXiv preprint. [doi:10.48550/arXiv.2409.09047](https://doi.org/10.48550/arXiv.2409.09047)"
    author: Matthias Lehmann, Philipp B. Cornelius, and Fabian J. Sting
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: matthias-lehmann-2024-2
    resource: "https://doi.org/10.48550/arXiv.2409.09047"
    title: "Matthias Lehmann, Philipp B. Cornelius, and Fabian J. Sting. (2024). AI Meets the Classroom: When Do Large Language Models Harm Learning? arXiv preprint. [doi:10.48550/arXiv.2409.09047](https://doi.org/10.48550/arXiv.2409.09047)"
    author: Matthias Lehmann, Philipp B. Cornelius, and Fabian J. Sting
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Enabling copy and paste increases LLM use during learning, and specifically increases substitutive solution requests but not explanation requests

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1`–`r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Treated subjects with copy and paste sent significantly more messages to the LLM than treated subjects without it. [→ Matthias Lehmann 2024](#matthias-lehmann-2024)
`q2 i?` Copy and paste significantly increased requests for solutions but not requests for explanations, suggesting an intrinsic preference for substitutive use. [→ Matthias Lehmann 2024 (2)](#matthias-lehmann-2024-2)

## Evidence

### Matthias Lehmann 2024

Matthias Lehmann, Philipp B. Cornelius, and Fabian J. Sting. (2024). AI Meets the Classroom: When Do Large Language Models Harm Learning? arXiv preprint. [doi:10.48550/arXiv.2409.09047](https://doi.org/10.48550/arXiv.2409.09047)

`q2 · i?` · `causal · r1`

Exploratory comparison of treated subjects across Studies 2 and 3, which differed only in copy-and-paste availability. Copy and paste increased LLM use: "treated subjects in Study 3 sent 7.71 (S.D. = 5.50) messages to the LLM, which is significantly more than the 4.45 messages sent in Study 2".

> "On average, treated subjects in Study 3 sent 7.71 (S.D. = 5.50) messages to the LLM, which is significantly more than the 4.45 messages sent in Study 2 (𝑝 = 0.002; Table 9, column 3:𝑝 = 0.001)."

### Matthias Lehmann 2024 (2)

Matthias Lehmann, Philipp B. Cornelius, and Fabian J. Sting. (2024). AI Meets the Classroom: When Do Large Language Models Harm Learning? arXiv preprint. [doi:10.48550/arXiv.2409.09047](https://doi.org/10.48550/arXiv.2409.09047)

`q2 · i?` · `causal · r2`

Regressions on treated subjects from Studies 2 and 3 (n = 94) show copy and paste raised substitutive Solutions requests (p < 0.001) while Explanations requests were unchanged (p = 0.936): "copy and paste increased substitutive but not complementary use, suggesting that subjects intrinsically preferred the former".

> "treated subjects in Study 3 asked for significantly moreSolutions(𝑝 < 0.001) but not for moreExplanations(𝑝 = 0.936) than treated subjects in Study 2."

## Discussion


## Related Claims
- [Copy-and-paste-enabled substitutive LLM use trades topic volume for understanding: volume rises while understanding falls, leaving overall outcomes unchanged](substitution-volume-understanding-tradeoff.md) — related
- [Most unrestricted-mode interactions were direct answer retrieval: 52.9% of exercise interactions were copy-paste of the question, and participant answers were linguistically near-identical to chatbot text in 25.3% of cases](unrestricted-mode-answer-retrieval-copy-paste.md) — related
- [Guidance strategies G1, G2 and G4 reduce verbatim copy-pasting of assignment questions to the LLM, while G3 increases rephrasing](guidance-reduces-verbatim-question-copying.md) — related
- [Some students given complete LLM-generated solutions copied and submitted answers within minutes without engaging with the practice](complete-solution-students-copy-submit-quickly.md) — related
