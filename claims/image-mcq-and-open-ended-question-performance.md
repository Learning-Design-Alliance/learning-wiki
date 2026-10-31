---
type: claim
title: "ChatGPT's accuracy on image-based MCQs ranged from 13.1% to 100% across studies, and it performed significantly worse on open-ended questions than on MCQs"
description: "ChatGPT's accuracy on image-based MCQs ranged from 13.1% to 100% across studies, and it performed significantly worse on open-ended questions than on MCQs"
id: image-mcq-and-open-ended-question-performance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-31
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: mingxin-liu-2024
    resource: "https://doi.org/10.2196/60807"
    title: "Mingxin Liu, Tsuyoshi Okuhara, XinYi Chang, Ritsuko Shirabe, Yuriko Nishiie, Hiroko Okada, Takahiro Kiuchi. (2024). Performance of ChatGPT Across Different Versions in Medical Licensing Examinations Worldwide: Systematic Review and Meta-Analysis. Journal of Medical Internet Research. https://doi.org/10.2196/60807"
    author: Mingxin Liu, Tsuyoshi Okuhara, XinYi Chang, Ritsuko Shirabe, Yuriko Nishiie, Hiroko Okada, Takahiro Kiuchi
    q: 2
    i: "?"
    kind: quant-synthesis
    rigour: 3
  - id: mingxin-liu-2024-2
    resource: "https://doi.org/10.2196/60807"
    title: "Mingxin Liu, Tsuyoshi Okuhara, XinYi Chang, Ritsuko Shirabe, Yuriko Nishiie, Hiroko Okada, Takahiro Kiuchi. (2024). Performance of ChatGPT Across Different Versions in Medical Licensing Examinations Worldwide: Systematic Review and Meta-Analysis. Journal of Medical Internet Research. https://doi.org/10.2196/60807"
    author: Mingxin Liu, Tsuyoshi Okuhara, XinYi Chang, Ritsuko Shirabe, Yuriko Nishiie, Hiroko Okada, Takahiro Kiuchi
    q: 2
    i: "?"
    kind: quant-synthesis
    rigour: 3
---

# ChatGPT's accuracy on image-based MCQs ranged from 13.1% to 100% across studies, and it performed significantly worse on open-ended questions than on MCQs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · quant-synthesis `r3` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In 4 studies of image-based MCQs, accuracy ranged from 13% (Spanish) to 100% (a 3-question UK set); a Japanese study found 68% accuracy with images and text versus 72% with text only. [→ Mingxin Liu 2024](#mingxin-liu-2024)
`q2 i?` Of 4 studies comparing open-ended questions with MCQs, 2 showed ChatGPT performed significantly worse on open-ended questions; calculation questions also showed significantly worse performance than MCQs in one Japanese study. [→ Mingxin Liu 2024 (2)](#mingxin-liu-2024-2)

## Evidence

### Mingxin Liu 2024

Mingxin Liu, Tsuyoshi Okuhara, XinYi Chang, Ritsuko Shirabe, Yuriko Nishiie, Hiroko Okada, Takahiro Kiuchi. (2024). Performance of ChatGPT Across Different Versions in Medical Licensing Examinations Worldwide: Systematic Review and Meta-Analysis. Journal of Medical Internet Research. https://doi.org/10.2196/60807

`q2 · i?` · `quant-synthesis · r3`

Narrative synthesis of 4 studies on image-based MCQs. The review reports the Spanish study's 13% versus 26% rates, 100% accuracy on only 3 UK questions, 68% (73/108) with images and text versus 72% (78/108) with text only in Japan, and GPT-4V (70%) performing worse than GPT-4 (76.7%) in Chile.

> "In a Spanish study, the accuracy rate of GPT-4 for image-based MCQs in Spanish was 13%, and the accuracy rate was 26% after translating the image-based MCQs into English, twice as high as in Spanish"

### Mingxin Liu 2024 (2)

Mingxin Liu, Tsuyoshi Okuhara, XinYi Chang, Ritsuko Shirabe, Yuriko Nishiie, Hiroko Okada, Takahiro Kiuchi. (2024). Performance of ChatGPT Across Different Versions in Medical Licensing Examinations Worldwide: Systematic Review and Meta-Analysis. Journal of Medical Internet Research. https://doi.org/10.2196/60807

`q2 · i?` · `quant-synthesis · r3`

Narrative synthesis of 4 studies comparing open-ended questions with MCQs: "2 showed that ChatGPT performed significantly worse on open-ended questions than on MCQs"; one Japanese study found calculation questions significantly worse than MCQs; one Chinese patient-history study was passed above average student level.

> "Among them, 2 showed that ChatGPT performed significantly worse on open-ended questions than on MCQs [3,19], 1 showed slightly better performance on open-ended questions, and another asked ChatGPT 10 short questions, all of which received an “A” grade"

## Discussion


## Related Claims
- [GPT-4 passed medical licensing examinations in 26 of 29 cases and outperformed average medical students in 13 of 17 cases, while GPT-3.5 passed in only 10 of 26 and surpassed students in 4 of 14](gpt4-pass-and-student-comparison-rates.md) — related
- [Newer OpenAI LLM versions achieve significantly higher pooled accuracy on biomedical MCQs than earlier versions (GPT‐4o–o1: 90%; GPT‐4: 82%; GPT‐3/3.5: 59%)](openai-llm-accuracy-improves-across-versions-biomedical-mcq.md) — related
- [LLM accuracy does not differ significantly across question languages, ranging from 62% in Polish to 77% in German](llm-accuracy-language-differences-nonsignificant.md) — related
