---
type: claim
title: Blind LLM grading of undergraduate physics solutions is substantially more lenient than human grading, driven by mathematical hallucinations
description: Blind LLM grading of undergraduate physics solutions is substantially more lenient than human grading, driven by mathematical hallucinations
id: llm-blind-grading-lenient-hallucinations
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
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
  - id: mok-2025-2
    resource: "https://doi.org/10.1088/1361-6552/adb92b"
    title: "Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli. (2025). Using AI Large Language Models for Grading in Education: A Hands-On Test for Physics. arXiv. Originally published 2024. [doi:10.1088/1361-6552/adb92b](https://doi.org/10.1088/1361-6552/adb92b)"
    author: Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Blind LLM grading of undergraduate physics solutions is substantially more lenient than human grading, driven by mathematical hallucinations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Without a mark scheme, all four tested LLM chatbots grade physics solutions more leniently than averaged human graders, with best-fit slopes well below 1 and positive intercepts. [→ Mok 2025](#mok-2025)
`q2 i?` The leniency is typically caused by hallucinations involving algebraic steps or mathematical expressions, where chatbots assert incorrect expressions are correct. [→ Mok 2025 (2)](#mok-2025-2)

## Evidence

### Mok 2025

Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli. (2025). Using AI Large Language Models for Grading in Education: A Hands-On Test for Physics. arXiv. Originally published 2024. [doi:10.1088/1361-6552/adb92b](https://doi.org/10.1088/1361-6552/adb92b)

`q2 · i?` · `design · r2`

Regression analysis of AI grades against averaged human grades (four UCL graduate graders) for 90 LLM-generated solutions, plotted in Figs. 10-13. The article reports "all LLM models appear to be much more lenient than human graders", ordered Claude 3.5 Sonnet, Gemini 1.5 Pro, GPT-4o, GPT-4.

> "In general, one can see that for blind grading, all LLM models appear to be much more lenient than human graders. In order of most to least, this seems to be Claude 3.5 Sonnet, Gemini 1.5 Pro, GPT-4o and GPT-4."

### Mok 2025 (2)

Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli. (2025). Using AI Large Language Models for Grading in Education: A Hands-On Test for Physics. arXiv. Originally published 2024. [doi:10.1088/1361-6552/adb92b](https://doi.org/10.1088/1361-6552/adb92b)

`q2 · i?` · `design · r2`

Qualitative examination of chatbot grading responses in the Results section; the article illustrates this with an EM problem where GPT-4, GPT-4o and Claude praised an incorrect electric-field expression, awarding 14, 13 and 11 marks respectively.

> "A closer examination of chatbots’ grading responses and feedback demonstrates that leniency in grading is typically a result of hallucinations, most often involving algebraic steps or mathematical expressions."

## Discussion


## Related Claims
- [GPT-4's grading accuracy correlates with its problem-solving ability, and a mark scheme removes this dependence](gpt4-solving-grading-correlation.md) — related
- [Providing a mark scheme substantially improves LLM grading accuracy and consistency, with GPT-4 shifting closest to human grades](mark-scheme-improves-llm-grading.md) — related
- [AI grades more leniently than teaching assistants and clusters rubric item grades more strongly, indicating holistic rather than differentiated grading](ai-grades-leniently-and-holistically.md) — possibly the same claim (merge candidate)
- [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](llm-grading-mixed-against-human-raters.md) — related
- [GenAI models' grades differ significantly across models, with GPTo1 grading more leniently than Llama2, Mistral7B and Cohere](genai-grade-differences-wilcoxon.md) — related
- [Claude3 and PaLM2 show substantial agreement but fall short on identifying failing grades](claude3-palm2-substantial-agreement-failing-grades.md) — related
- [Peer graders in these MOOCs score more leniently and with greater dispersion than the instructor](peer-grading-lenient-high-dispersion-moocs.md) — related
- [Students grading practice exams award significantly more points than a professional grader, about 25% more overall](peer-graders-more-lenient-than-professional.md) — related
