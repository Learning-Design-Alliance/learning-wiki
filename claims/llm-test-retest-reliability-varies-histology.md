---
type: claim
title: Test-retest reliability of LLM answers to histology MCQs ranged from moderate (Gemini, DeepSeek) to excellent (Claude)
description: Test-retest reliability of LLM answers to histology MCQs ranged from moderate (Gemini, DeepSeek) to excellent (Claude)
id: llm-test-retest-reliability-varies-histology
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: mavrych-volodymyr-2025
    resource: "https://doi.org/10.1080/10872981.2025.2534065"
    title: "Mavrych Volodymyr, Yousef Einas M., Yaqinuddin Ahmed, Bolgova Olena. (2025). Large language models in medical education: a comparative cross-platform evaluation in answering histological questions. Medical Education Online. https://doi.org/10.1080/10872981.2025.2534065"
    author: Mavrych Volodymyr, Yousef Einas M., Yaqinuddin Ahmed, Bolgova Olena
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: mavrych-volodymyr-2025-2
    resource: "https://doi.org/10.1080/10872981.2025.2534065"
    title: "Mavrych Volodymyr, Yousef Einas M., Yaqinuddin Ahmed, Bolgova Olena. (2025). Large language models in medical education: a comparative cross-platform evaluation in answering histological questions. Medical Education Online. https://doi.org/10.1080/10872981.2025.2534065"
    author: Mavrych Volodymyr, Yousef Einas M., Yaqinuddin Ahmed, Bolgova Olena
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: mavrych-volodymyr-2025-3
    resource: "https://doi.org/10.1080/10872981.2025.2534065"
    title: "Mavrych Volodymyr, Yousef Einas M., Yaqinuddin Ahmed, Bolgova Olena. (2025). Large language models in medical education: a comparative cross-platform evaluation in answering histological questions. Medical Education Online. https://doi.org/10.1080/10872981.2025.2534065"
    author: Mavrych Volodymyr, Yousef Einas M., Yaqinuddin Ahmed, Bolgova Olena
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Test-retest reliability of LLM answers to histology MCQs ranged from moderate (Gemini, DeepSeek) to excellent (Claude)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Claude showed the highest test-retest reliability (ICC = 0.931, excellent), while Gemini (ICC = 0.562) and DeepSeek (ICC = 0.633) showed only moderate reliability. [→ Mavrych Volodymyr 2025](#mavrych-volodymyr-2025)
`q2 i?` ICC differences were statistically significant between Claude and both DeepSeek and Gemini, but not between Claude and GPT-4 or Copilot. [→ Mavrych Volodymyr 2025 (2)](#mavrych-volodymyr-2025-2)
`q2 i?` Hierarchical cluster analysis identified a high-reliability cluster (Claude, GPT-4, Copilot; mean ICC = 0.881) and a moderate-reliability cluster (DeepSeek, Gemini; mean ICC = 0.598). [→ Mavrych Volodymyr 2025 (3)](#mavrych-volodymyr-2025-3)

## Evidence

### Mavrych Volodymyr 2025

Mavrych Volodymyr, Yousef Einas M., Yaqinuddin Ahmed, Bolgova Olena. (2025). Large language models in medical education: a comparative cross-platform evaluation in answering histological questions. Medical Education Online. https://doi.org/10.1080/10872981.2025.2534065

`q2 · i?` · `design · r2`

Test-retest reliability analysis using intraclass correlation coefficients (two-way mixed effects model, absolute agreement) across three independent testing sessions. The article reports "Claude demonstrated the highest test-retest reliability (ICC = 0.931, 95% CI [0.831–0.973])", interpreted as excellent, with Gemini at 0.562 and DeepSeek at 0.633 (moderate); no standardised effect size is printed, so no magnitude is coded.

> "Claude demonstrated the highest test-retest reliability (ICC = 0.931, 95% CI [0.831–0.973]), followed by GPT-4 (ICC = 0.882, 95% CI [0.722–0.953]) and Copilot (ICC = 0.830, 95% CI [0.613–0.931])."

### Mavrych Volodymyr 2025 (2)

Mavrych Volodymyr, Yousef Einas M., Yaqinuddin Ahmed, Bolgova Olena. (2025). Large language models in medical education: a comparative cross-platform evaluation in answering histological questions. Medical Education Online. https://doi.org/10.1080/10872981.2025.2534065

`q2 · i?` · `design · r2`

Fisher's r-to-z transformation compared ICC values between systems. The article reports "significant differences between Claude and both DeepSeek (Fisher's z = 3.42, p < 0.001) and Gemini (Fisher's z = 3.84, p < 0.001)", but not versus GPT-4 (p = 0.144) or Copilot (p = 0.059).

> "These comparisons revealed significant differences between Claude and both DeepSeek (Fisher's z = 3.42, p < 0.001) and Gemini (Fisher's z = 3.84, p < 0.001)"

### Mavrych Volodymyr 2025 (3)

Mavrych Volodymyr, Yousef Einas M., Yaqinuddin Ahmed, Bolgova Olena. (2025). Large language models in medical education: a comparative cross-platform evaluation in answering histological questions. Medical Education Online. https://doi.org/10.1080/10872981.2025.2534065

`q2 · i?` · `associational · r2`

Hierarchical cluster analysis of the reliability patterns separated the five systems into two clusters with "significant between-cluster differences (t(3) = 7.92, p = 0.004)"; only the test statistic is printed, so no effect size is reported.

> "A hierarchical cluster analysis of reliability patterns identified two distinct clusters: high-reliability systems (Claude, GPT-4, Copilot; mean ICC = 0.881) and moderate-reliability systems (DeepSeek, Gemini; mean ICC = 0.598), with significant between-cluster differences (t(3) = 7.92, p = 0.004)."

## Discussion


## Related Claims
- [Five LLMs showed comparable, exceptionally high accuracy (collective mean 91.1%) on text-based medical histology MCQs](llm-mean-accuracy-91-1-histology-mcqs.md) — related
- [Reliability patterns were discipline-specific: Gemini ranked highest in reliability in embryology but only moderate in histology](llm-reliability-discipline-specific-patterns.md) — related
- [Large closed-weights LLMs show high test-retest reliability when scoring clinical summary statements across repeated runs](llm-high-test-retest-reliability-summary-statement-scoring.md) — related
- [In one study of repeated LLM scoring of 60 IELTS essays, Gemini 2.5 Flash was moderately reliable (ICC 0.63-0.75) while Claude Sonnet 4 and DeepSeek R1 stayed below 0.70 in most dimensions](llm-essay-scoring-reliability-stratification.md) — related
- [All five LLMs answered every MCQ and showed high short-term test–retest agreement (AC1 0.79–1.00), indicating reproducible performance without selective abstention](llms-answered-every-mcq-high-test-retest-agreement.md) — related
