---
type: claim
title: LLM failures on the CRCI stem predominantly from visual misinterpretation rather than deficits in physics knowledge
description: LLM failures on the CRCI stem predominantly from visual misinterpretation rather than deficits in physics knowledge
id: llm-crcl-errors-predominantly-visual
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: eugenio-tufino-2026
    resource: "https://doi.org/10.1088/1361-6404/ae8c90"
    title: "Eugenio Tufino, Caterina Giovanzana, Andrea Zamboni, Pasquale Onorato and Stefano Oss. (2026). Performance and failure modes of AI chatbots on a novel concept inventory on relativity in classical mechanics. [doi:10.1088/1361-6404/ae8c90](https://doi.org/10.1088/1361-6404/ae8c90)"
    author: Eugenio Tufino, Caterina Giovanzana, Andrea Zamboni, Pasquale Onorato and Stefano Oss
    q: 2
    i: "?"
    kind: qualitative
    rigour: 2
---

# LLM failures on the CRCI stem predominantly from visual misinterpretation rather than deficits in physics knowledge

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · qualitative `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Qualitative coding of all 1890 responses on three dimensions (visual, physics reasoning, coordination) shows errors are mostly visual; when models extract visual features correctly they almost always generate a correct physical derivation. [→ Eugenio Tufino 2026](#eugenio-tufino-2026)

## Evidence

### Eugenio Tufino 2026

Eugenio Tufino, Caterina Giovanzana, Andrea Zamboni, Pasquale Onorato and Stefano Oss. (2026). Performance and failure modes of AI chatbots on a novel concept inventory on relativity in classical mechanics. [doi:10.1088/1361-6404/ae8c90](https://doi.org/10.1088/1361-6404/ae8c90)

`q2 · i?` · `qualitative · r2`

Qualitative coding of all responses (not only incorrect ones) on binary visual, reasoning and coordination dimensions, adapted from the Polverini and Gregorcic BEMA framework. Gemini 3 Flash errors were almost entirely visual; reasoning errors were concentrated on few items and often entangled with visual difficulties.

> "The overall picture supports the conclusion that, on the CRCI, multimodal failures stem primarily from visual misinterpretations rather than from deficits in physics knowledge."

## Discussion


## Related Claims
- [LLM errors on multimodal physics problems fall into four categories, with visual processing errors most prevalent, and error type distribution does not differ significantly across models](four-category-llm-multimodal-error-taxonomy.md) — possibly the same claim (merge candidate)
- [ChatGPT-4o's BEMA errors fall into three difficulty types, with spatial coordination of representations and rules the most prevalent](three-chatbot-difficulty-types-bema.md) — related
- [A three-step structured multimodal dialogue intervention corrected 82% of baseline errors and raised multimodal accuracy to 95%, with visual processing errors corrected at 100% but context misinterpretation errors resistant](structured-dialogue-corrects-82-percent-llm-errors.md) — related
- [When GPT-4V answered incorrectly, its explanations frequently contained image misunderstandings, reasoning errors, and hallucinations](gpt4v-poor-explanations-incorrect-answers.md) — related
