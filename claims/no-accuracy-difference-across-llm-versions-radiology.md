---
type: claim
title: Successive versions of ChatGPT and Gemini showed no statistically significant difference in overall accuracy on the radiology questions, with only moderate response consistency across versions
description: Successive versions of ChatGPT and Gemini showed no statistically significant difference in overall accuracy on the radiology questions, with only moderate response consistency across versions
id: no-accuracy-difference-across-llm-versions-radiology
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: atlanoğlu-ş-2026
    resource: "https://doi.org/10.1097/MD.0000000000049517"
    title: "Atlanoğlu Ş, Gedik MA. (2026). Large language models in radiology exams: A cross-sectional comparative analysis of performance in Turkish and English. Medicine 2026;105:26(e49517). https://doi.org/10.1097/MD.0000000000049517"
    author: Atlanoğlu Ş, Gedik MA
    q: 3
    i: "?"
    kind: causal
    rigour: 1
  - id: atlanoğlu-ş-2026-2
    resource: "https://doi.org/10.1097/MD.0000000000049517"
    title: "Atlanoğlu Ş, Gedik MA. (2026). Large language models in radiology exams: A cross-sectional comparative analysis of performance in Turkish and English. Medicine 2026;105:26(e49517). https://doi.org/10.1097/MD.0000000000049517"
    author: Atlanoğlu Ş, Gedik MA
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Successive versions of ChatGPT and Gemini showed no statistically significant difference in overall accuracy on the radiology questions, with only moderate response consistency across versions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1`–`r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Across ChatGPT versions (v5.1, v5.0, v4.0), no statistically significant difference was observed in overall accuracy rates (P = .282), with moderate Fleiss kappa agreement (0.600). [→ Atlanoğlu Ş 2026](#atlanoglu-s-2026)
`q3 i?` Gemini 2.5 Pro and Gemini 2.5 Flash showed statistically similar correct-response rates (P = .508) with moderate agreement (kappa = 0.589). [→ Atlanoğlu Ş 2026 (2)](#atlanoglu-s-2026-2)

## Evidence

### Atlanoğlu Ş 2026

Atlanoğlu Ş, Gedik MA. (2026). Large language models in radiology exams: A cross-sectional comparative analysis of performance in Turkish and English. Medicine 2026;105:26(e49517). https://doi.org/10.1097/MD.0000000000049517

`q3 · i?` · `causal · r1`

Version comparison in which questions were posed in English to successive ChatGPT releases (v5.1, v5.0, v4.0). Cochran Q testing found no significant accuracy difference (P = .282); Fleiss kappa indicated moderate cross-version response consistency.

> "In the comparative analysis across different versions of ChatGPT, no statistically significant difference was observed in the overall accuracy rates (P = .282). Fleiss Kappa analysis, conducted to assess response consistency among the versions, revealed a "moderate" level of agreement (kappa = 0.600; P < .001; Table 4)."

### Atlanoğlu Ş 2026 (2)

Atlanoğlu Ş, Gedik MA. (2026). Large language models in radiology exams: A cross-sectional comparative analysis of performance in Turkish and English. Medicine 2026;105:26(e49517). https://doi.org/10.1097/MD.0000000000049517

`q3 · i?` · `causal · r2`

Version comparison between Gemini 2.5 Pro and Gemini 2.5 Flash on the same English question set. McNemar testing found no significant performance difference (P = .508); kappa indicated moderate response-based consistency between versions.

> "In the comparison between different versions of the Gemini model, the rates of correct responses were statistically similar, with no significant performance difference observed (P = .508). Response-based consistency analysis revealed a "moderate" level of agreement between versions (kappa = 0.589; P < .001; Table 5)."

## Discussion


## Related Claims
- [Gemini 2.5 Pro achieved the highest accuracy (90%) on 100 radiology multiple-choice questions, and all LLMs and 3rd-year residents significantly outperformed 1st- and 2nd-year residents](llms-gemini-highest-radiology-mcq-accuracy-outperform-junior-residents.md) — related
- [Inter-model agreement is moderate, indicating models do not consistently identify the same questions correctly](moderate-inter-model-agreement-endodontic-questions.md) — related
- [Temporal reliability over a 1-week interval varied across LLMs: Claude 4.5 Sonnet showed very good consistency (kappa = 0.872) while Grok-4 and ChatGPT-5 showed moderate agreement](claude-sonnet-superior-temporal-reliability-radiology-questions.md) — related
- [ChatGPT-5, Gemini 3.0 Pro, and Claude Sonnet 4.5 achieved significantly higher overall scores than mean ophthalmology trainee performance, while ChatGPT-4o did not](three-llms-outperform-mean-trainee-overall.md) — related
