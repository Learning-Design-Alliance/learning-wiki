---
type: claim
title: "The strict-persona collapse is attributed to the preamble's two credit-withholding policy sentences, not its harsh tone, with S2 alone causing refusal in two models"
description: "The strict-persona collapse is attributed to the preamble's two credit-withholding policy sentences, not its harsh tone, with S2 alone causing refusal in two models"
id: strict-preamble-policy-sentence-attribution
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: habibullah-2026
    resource: "https://doi.org/10.48550/arxiv.2609.29333"
    title: "Habibullah, A., Alshoibi, Y., Alshiekh, M., Khan, S., & Khan, N. (2026). Where LLM graders succeed and break: Evidence from two computer-science exams. arXiv. https://arxiv.org/abs/2609.29333 [doi:10.48550/arxiv.2609.29333](https://doi.org/10.48550/arxiv.2609.29333)"
    author: "Habibullah, A., Alshoibi, Y., Alshiekh, M., Khan, S., & Khan, N."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# The strict-persona collapse is attributed to the preamble's two credit-withholding policy sentences, not its harsh tone, with S2 alone causing refusal in two models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Varying the adjective alone over verbatim policy sentences moves MAE by only 0.94–2.15, while a 2×2 crossing of sentences S1 and S2 takes three models to 20.26–26.04, with S2 alone producing outright refusal on Llama-3.1-8B and Mistral-Small-24B. [→ Habibullah 2026](#habibullah-2026)

## Evidence

### Habibullah 2026

Habibullah, A., Alshoibi, Y., Alshiekh, M., Khan, S., & Khan, N. (2026). Where LLM graders succeed and break: Evidence from two computer-science exams. arXiv. https://arxiv.org/abs/2609.29333 [doi:10.48550/arxiv.2609.29333](https://doi.org/10.48550/arxiv.2609.29333)

`q2 · i?` · `causal · r2`

Mechanism-probe runs on the CV exam isolating the persona's frame sentence from its two policy sentences. The article concludes "S2 contradicts the partial-credit scale the rubric scaffold mandates — hence the safer wordings, and advice about one instruction, not a tone."

> "A 2×2 crosses S1 with S2 on three models, frame fixed: the frame alone moves each less than two points off neutral, both sentences take them to 20.26–26.04, S2 alone to outright refusal on Llama-3.1-8B and Mistral-Small-24B."

## Discussion


## Related Claims
- [A short strict-grader preamble knocks 14 of 17 open-weights LLM graders out of the graded band on a computer-vision exam, with three stopping grading outright](llm-grader-strict-persona-collapse.md) — related
- [The strict-persona vulnerability replicates on an independent machine-learning exam, but its direction is exam-specific: seven of 17 models improve because the persona cancels their over-marking](strict-persona-effect-exam-specific.md) — related
- [One LoRA adapter fine-tuned on the two exams' pooled ~3,900 dual-graded examples brings five small open models to parity or better with a human grader and makes them insensitive to harsh personas](lora-finetuning-llm-grader-parity.md) — related
- [Chinese-developed models lead the safety module, with the refusal gap concentrated on region-specific normative content (difference-in-differences of 28.9 points)](chinese-models-safety-refusal-gap.md) — related
