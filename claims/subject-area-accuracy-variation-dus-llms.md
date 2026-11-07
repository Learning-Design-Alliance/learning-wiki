---
type: claim
title: "LLM accuracy varied by subject area, with oral pathology (94%) and salivary gland diseases (91.8%) highest and radiological anatomy (67.3%) lowest; only Copilot showed a statistically significant across-subject difference"
description: "LLM accuracy varied by subject area, with oral pathology (94%) and salivary gland diseases (91.8%) highest and radiological anatomy (67.3%) lowest; only Copilot showed a statistically significant across-subject differ..."
id: subject-area-accuracy-variation-dus-llms
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: geduk-gediz-2026
    resource: "https://doi.org/10.1038/s41598-026-37800-8"
    title: "Geduk Gediz, Hasırcı Utku Cem, Kusay Didem Dumanlı, Aras Rabia Çayır, Çapar İsmail, Altın Edanur, Şeker Çiğdem. (2026). A comparative analysis of the performance of large Language models in the dentistry specialty examination. Scientific Reports. https://doi.org/10.1038/s41598-026-37800-8"
    author: Geduk Gediz, Hasırcı Utku Cem, Kusay Didem Dumanlı, Aras Rabia Çayır, Çapar İsmail, Altın Edanur, Şeker Çiğdem
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: geduk-gediz-2026-2
    resource: "https://doi.org/10.1038/s41598-026-37800-8"
    title: "Geduk Gediz, Hasırcı Utku Cem, Kusay Didem Dumanlı, Aras Rabia Çayır, Çapar İsmail, Altın Edanur, Şeker Çiğdem. (2026). A comparative analysis of the performance of large Language models in the dentistry specialty examination. Scientific Reports. https://doi.org/10.1038/s41598-026-37800-8"
    author: Geduk Gediz, Hasırcı Utku Cem, Kusay Didem Dumanlı, Aras Rabia Çayır, Çapar İsmail, Altın Edanur, Şeker Çiğdem
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# LLM accuracy varied by subject area, with oral pathology (94%) and salivary gland diseases (91.8%) highest and radiological anatomy (67.3%) lowest; only Copilot showed a statistically significant across-subject difference

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across 14 subject areas, the highest-performing topics were oral pathology (94%) and salivary gland diseases (91.8%), while radiological anatomy (67.3%) and soft tissue calcifications were lowest. [→ Geduk Gediz 2026](#geduk-gediz-2026)
`q2 i?` In an ANOVA across subjects per model, only Copilot showed a statistically significant difference, with soft tissue calcifications (50%) significantly lower than radiation physics, systemic diseases, cysts and tumors, and oral pathology. [→ Geduk Gediz 2026 (2)](#geduk-gediz-2026-2)

## Evidence

### Geduk Gediz 2026

Geduk Gediz, Hasırcı Utku Cem, Kusay Didem Dumanlı, Aras Rabia Çayır, Çapar İsmail, Altın Edanur, Şeker Çiğdem. (2026). A comparative analysis of the performance of large Language models in the dentistry specialty examination. Scientific Reports. https://doi.org/10.1038/s41598-026-37800-8

`q2 · i?` · `design · r2`

Descriptive analysis of accuracy by 14 subject headings across the seven models (Table 4). The article reports oral pathology (94%) and salivary gland diseases (91.8%) as highest and radiological anatomy (67.3%) among the lowest.

> "When the models responses were analyzed based on subject area, the highest-performing topics were oral pathology (94%) and salivary gland diseases (91.8%). In contrast, radiological anatomy (67.3%) and soft tissue calcifications were identified as the subjects with the lowest accuracy rates (Table 4)."

### Geduk Gediz 2026 (2)

Geduk Gediz, Hasırcı Utku Cem, Kusay Didem Dumanlı, Aras Rabia Çayır, Çapar İsmail, Altın Edanur, Şeker Çiğdem. (2026). A comparative analysis of the performance of large Language models in the dentistry specialty examination. Scientific Reports. https://doi.org/10.1038/s41598-026-37800-8

`q2 · i?` · `causal · r1`

ANOVA comparing accuracy distributions across subjects for each model, with post hoc Tukey tests. Only Copilot was significant (p < 0.05); its soft tissue calcifications accuracy (50%) was significantly lower than four other subject areas.

> "The test results revealed that only the copilot model exhibited a statistically significant difference (p < 0.05), and a post hoc Tukey test was subsequently performed. Within the copilot chatbot, the accuracy rate for soft tissue calcifications (50%) was found to be significantly lower compared to its performance in other subject areas such as radiation physics (p: 0,030), systemic diseases (p: 0,034), cysts and tumors (p: 0,032), and oral pathology (p: 0,021)."

## Discussion


## Related Claims
- [Non-dentistry undergraduates prioritize learning oral pathologies and diagnostic thinking over basic oral procedural skills in their stomatology clerkship](non-dental-students-prioritize-diagnostic-over-procedural-skills.md) — related
- [ChatGPT-4o's subtopic-level accuracy on Chinese questions ranged from 90% (Nerve Disorders) down to 38% (Dentofacial Deformities)](chatgpt-4o-chinese-subtopic-accuracy-range.md) — related
- [LLM accuracy on the EUS varies by subject area, with pharmacy legislation/ethics lowest (DeepSeek-R1 at 20%)](eus-subject-area-accuracy-variation.md) — related
- [ChatGPT 4.0 achieved the highest accuracy (91.3%) on DUS oral and maxillofacial radiology questions and significantly outperformed all other evaluated LLMs](chatgpt-4-highest-accuracy-dus-radiology.md) — related
- [Diagnostic accuracy is higher for oral conditions with recognizable clinical features and lower for conditions with non-specific presentations](recognizable-features-higher-oral-diagnostic-accuracy.md) — related
- [All seven LLMs showed markedly lower accuracy on image-based than text-based DUS questions, with significant text-image gaps for five models but not Gemini or Claude](llms-lower-accuracy-image-based-dus-questions.md) — related
- [Gemini 2.5 Pro achieved the highest accuracy (90%) on 100 radiology multiple-choice questions, and all LLMs and 3rd-year residents significantly outperformed 1st- and 2nd-year residents](llms-gemini-highest-radiology-mcq-accuracy-outperform-junior-residents.md) — related
- [Large language models achieve a pooled accuracy of 63.69% (95% CI 60.26%-67.06%) in answering dental examination questions](llm-pooled-accuracy-dental-exam-63-69.md) — related
- [LLM accuracy is uniformly high in OT basic sciences but lower on OT-specific content, widening further on visuals](basic-sciences-high-ot-specific-lower.md) — related
- [Diagnostic accuracy and confidence vary widely across lesion types, with stafne bone cavity easiest and adenomatoid odontogenic tumor and odontogenic keratocyst hardest](case-difficulty-varies-across-radiographic-lesions.md) — related
- [LLM performance on anatomy MCQs varies significantly across anatomical topics, with Head & Neck and Abdomen highest and Upper Limb lowest](llm-anatomy-topic-performance-variation.md) — a narrower finding that bears on this claim
- [LLM accuracy varied sharply by histology topic: perfect in foundational areas and lowest in Muscle (76.0%)](histology-topic-difficulty-llm-performance.md) — related
- [Residents' correct answers vary widely across nutrition topics, lowest for macronutrient distribution and highest for fish portions](topic-level-nutrition-knowledge-gaps-residents.md) — related
- [ChatGPT-4o outperformed both third-year and fifth-year dental students in diagnostic accuracy on endodontic multiple-choice questions with radiographic and clinical images](chatgpt-4o-outperforms-dental-students-endodontic-diagnosis.md) — related
- [Prior studies report widely varying ChatGPT diagnostic accuracy in dentistry (11% to 99%), likely due to differences in question types and content](prior-chatgpt-dental-accuracy-studies-vary-11-to-99-percent.md) — a narrower finding that bears on this claim
- [Chatbot accuracy varied substantially across biochemistry topics: highest for eicosanoids (100%), bioenergetics and electron transport chain (96.4%), ketone bodies (93.8%), and the hexose monophosphate pathway (91.7%), lowest for globular proteins and hemoglobin (58.4%)](topic-level-chatbot-accuracy-variation-biochemistry.md) — a narrower finding that bears on this claim
- [GPT-4V's accuracy was inconsistent across medical subdomains, high in some (e.g. immunology 100%) and low in others (e.g. anatomy 25%)](gpt4v-subdomain-performance-inconsistent.md) — a narrower finding that bears on this claim
- [LLM accuracy varied significantly across oncology topics, with the lowest performance in colorectal tumors (mean 48.3%) and genitourinary tumors (mean 50.8%)](llm-accuracy-varies-across-oncology-topics.md) — related
