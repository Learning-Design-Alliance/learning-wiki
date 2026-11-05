---
type: claim
title: LLM accuracy is uniformly high in OT basic sciences but lower on OT-specific content, widening further on visuals
description: LLM accuracy is uniformly high in OT basic sciences but lower on OT-specific content, widening further on visuals
id: basic-sciences-high-ot-specific-lower
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: saita-kazuya-2026
    resource: "https://doi.org/10.1186/s12909-025-08542-4"
    title: "Saita Kazuya, Mine Yuichi, Amano Satoru. (2026). What the performance of multimodal LLMs on a national licensing exam teaches us about occupational therapy education. BMC Medical Education. https://doi.org/10.1186/s12909-025-08542-4"
    author: Saita Kazuya, Mine Yuichi, Amano Satoru
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: saita-kazuya-2026-2
    resource: "https://doi.org/10.1186/s12909-025-08542-4"
    title: "Saita Kazuya, Mine Yuichi, Amano Satoru. (2026). What the performance of multimodal LLMs on a national licensing exam teaches us about occupational therapy education. BMC Medical Education. https://doi.org/10.1186/s12909-025-08542-4"
    author: Saita Kazuya, Mine Yuichi, Amano Satoru
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM accuracy is uniformly high in OT basic sciences but lower on OT-specific content, widening further on visuals

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` All models exceeded 94% in anatomy, physiology, kinesiology, pathology, clinical psychology and clinical medicine, while on 81 text-based OT questions Gemini 2.5 scored 87.7% and models fell below 80%; on OT visuals rates ranged from 63.2% to 47.4%. [→ Saita Kazuya 2026](#saita-kazuya-2026)

## Evidence

### Saita Kazuya 2026

Saita Kazuya, Mine Yuichi, Amano Satoru. (2026). What the performance of multimodal LLMs on a national licensing exam teaches us about occupational therapy education. BMC Medical Education. https://doi.org/10.1186/s12909-025-08542-4

`q2 · i?` · `design · r2`

Specialty-level analysis across the nine national-curriculum specialties (Table 4): "All models exceeded 94% in anatomy, physiology, kinesiology, pathology, clinical psychology and clinical medicine" while OT-specific content was harder.

> "All models exceeded 94% in anatomy, physiology, kinesiology, pathology, clinical psychology and clinical medicine, with both Gemini 2.5 and OpenAI o3 achieving perfect scores in several categories. OT specific content, on the other hand, was more difficult: across the 81 text-based OT questions, Gemini 2.5 scored 87.7% and OpenAI o3 scored 85.2%, while GPT-4.5 and Claude 3.7 fell below 80%."

### Saita Kazuya 2026 (2)

Saita Kazuya, Mine Yuichi, Amano Satoru. (2026). What the performance of multimodal LLMs on a national licensing exam teaches us about occupational therapy education. BMC Medical Education. https://doi.org/10.1186/s12909-025-08542-4

`q2 · i?` · `design · r2`

OT-specific visual subscores: "correct response rates for OT visuals ranging from 63.2% (Gemini 2.5) to 47.4% (Claude 3.7)". The authors attribute limited OT-specific literature in global databases as a possible cause of these knowledge gaps.

> "The gap widened when images were added, with correct response rates for OT visuals ranging from 63.2% (Gemini 2.5) to 47.4% (Claude 3.7)."

## Discussion


## Related Claims
- [LLM accuracy varied by subject area, with oral pathology (94%) and salivary gland diseases (91.8%) highest and radiological anatomy (67.3%) lowest; only Copilot showed a statistically significant across-subject difference](subject-area-accuracy-variation-dus-llms.md) — related
- [Both chatbots achieve above-90% accuracy on fundamental medical sciences questions with no significant difference between models or sub-disciplines](llms-fundamental-medical-sciences-dus-high-accuracy.md) — related
- [LLM accuracy on the EUS varies by subject area, with pharmacy legislation/ethics lowest (DeepSeek-R1 at 20%)](eus-subject-area-accuracy-variation.md) — related
- [All seven LLMs showed markedly lower accuracy on image-based than text-based DUS questions, with significant text-image gaps for five models but not Gemini or Claude](llms-lower-accuracy-image-based-dus-questions.md) — related
