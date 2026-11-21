---
type: claim
title: LLM handwriting recognition of scanned physics solutions is decent but not sufficiently reliable for grading real exam papers
description: LLM handwriting recognition of scanned physics solutions is decent but not sufficiently reliable for grading real exam papers
id: llm-handwriting-recognition-unreliable-for-grading
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: mok-2025
    resource: "https://doi.org/10.1088/1361-6552/adb92b"
    title: "Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli. (2025). Using AI Large Language Models for Grading in Education: A Hands-On Test for Physics. arXiv. Originally published 2024. [doi:10.1088/1361-6552/adb92b](https://doi.org/10.1088/1361-6552/adb92b)"
    author: Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM handwriting recognition of scanned physics solutions is decent but not sufficiently reliable for grading real exam papers

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Of ChatGPT 3.5, ChatGPT 4 and Gemini 1.0, only ChatGPT 4 converted scanned handwritten exam text well, exceeding 80% correct conversion above 200 dpi, but formula elements such as vector arrows and differentiation dots were often misread. [→ Mok 2025](#mok-2025)

## Evidence

### Mok 2025

Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli. (2025). Using AI Large Language Models for Grading in Education: A Hands-On Test for Physics. arXiv. Originally published 2024. [doi:10.1088/1361-6552/adb92b](https://doi.org/10.1088/1361-6552/adb92b)

`q2 · i?` · `design · r2`

Preliminary independent test using several handwritten old exam papers and assignments presented to ChatGPT 3.5, ChatGPT 4 and Gemini 1.0, with conversion evaluated by a human reader; only ChatGPT 4 gave good results.

> "As long as the quality of the scanning was better than 200 dpi, more than 80% of the text was correctly converted, with the written words almost always correctly understood, but some problems in understanding formulae: sometimes extra text (like ”let x be”, correct but not present in the written text) was added, and often superscripts like the arrow sign indicating vectors, or the double dots indicating double differentiation with respect to time, were confused or misinterpreted."

## Discussion


## Related Claims
- [Students rated Ethel's handwritten-homework feedback helpful and correct in 3/4th of cases, but the system tended to underestimate solution correctness, mostly due to handwriting recognition](ethel-homework-feedback-ratings.md) — related
- [MathPix with GPT-4V support produces more reliable and reproducible OCR than using GPT-4V alone for handwritten exam solutions](mathpix-gpt4v-ocr-more-reliable-than-gpt4v-alone.md) — related
- [In the authors' practical test, vision-capable LLMs recognized handwritten examination letters with high accuracy, with Gemini 3 Flash best at about 98.84% (35 errors in 3009 letters)](vision-llm-letter-recognition-98-84-percent.md) — related
- [An earlier YOLO-5-based handwriting recognition method reached only 88.28% accuracy on examination table fields, which the authors judge insufficient for summative assessment](yolo5-handwriting-recognition-88-percent-insufficient.md) — related
- [AI-assigned total scores on a handwritten chemistry exam align strongly with TA-assigned totals (R2 = 0.91), while per-problem agreement is lower (R2 = 0.61–0.85)](ai-total-scores-align-with-ta-grades-chemistry-exam.md) — related
- [Automated grading was substantially less reliable for graphical solutions than mathematical derivations, and showed high precision but low recall in identifying passing exam solutions](ethel-grading-reliability-format-precision-recall.md) — related
- [In API-based evaluation, ChatGPT's assessment of technical and conceptual content is irregular and often inaccurate](chatgpt-api-unreliable-technical-assessment.md) — related
