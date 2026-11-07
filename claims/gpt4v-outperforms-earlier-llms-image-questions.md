---
type: claim
title: GPT-4V outperformed GPT-3.5 Turbo and GPT-4 on multiple-choice medical exam questions with images
description: GPT-4V outperformed GPT-3.5 Turbo and GPT-4 on multiple-choice medical exam questions with images
id: gpt4v-outperforms-earlier-llms-image-questions
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: yang-z-2025
    resource: "https://doi.org/10.2196/65146"
    title: "Yang Z, Yao Z, Tasmin M, Vashisht P, Jang WS, Ouyang F, Wang B, McManus D, Berlowitz D, Yu H. (2025). Unveiling GPT-4V's hidden challenges behind high accuracy on USMLE questions: Observational Study. Journal of Medical Internet Research. https://doi.org/10.2196/65146"
    author: Yang Z, Yao Z, Tasmin M, Vashisht P, Jang WS, Ouyang F, Wang B, McManus D, Berlowitz D, Yu H.
    q: 3
    i: "?"
    kind: associational
    rigour: 1
---

# GPT-4V outperformed GPT-3.5 Turbo and GPT-4 on multiple-choice medical exam questions with images

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q3 i?` On questions with images, GPT-4V achieved accuracies of 84.2% (Step 1), 85.7% (Step 2 CK), 88.9% (Step 3), and 73.1% (DRQCE), exceeding both GPT-3.5 Turbo and GPT-4 on each exam. [→ Yang Z 2025](#yang-z-2025)

## Evidence

### Yang Z 2025

Yang Z, Yao Z, Tasmin M, Vashisht P, Jang WS, Ouyang F, Wang B, McManus D, Berlowitz D, Yu H. (2025). Unveiling GPT-4V's hidden challenges behind high accuracy on USMLE questions: Observational Study. Journal of Medical Internet Research. https://doi.org/10.2196/65146

`q3 · i?` · `associational · r1`

Cross-sectional observational comparison of three models on 227 image-containing exam questions; the Results section reports pairwise chi-square comparisons with Bonferroni corrections, e.g. GPT-4V "outperformed GPT-3.5 Turbo and GPT-4 by 42.1%" in Step 1 (P<.001 and P=0.01).

> "For questions with images, GPT-4V achieved an accuracy of 84.2%, 85.7%, and 88.9% in Step 1, Step 2 CK, and Step 3 of USMLE questions, respectively. It outperformed GPT-3.5 Turbo and GPT-4 by 42.1% (8/19; 95% CI 36.8%-47.4%; P<.001) and 21.1% (4/19; 95% CI 7.8-34.2%; P=0.01) in Step 1"

## Discussion


## Related Claims
- [GPT-4o answered image-based USMLE sample items with 89.5% accuracy versus GPT-4's 73.4%, a numerically higher but not statistically significant difference](gpt4o-89-5-percent-image-usmle-accuracy.md) — related
- [GPT-4 examination accuracy is moderated by item type: multi-step vignettes (61–71%) and image-dependent items (48–63%) fall well below single-fact recall (83–88%)](gpt4-accuracy-item-type-moderators.md) — related
- [GPT-4V's accuracy was inconsistent across medical subdomains, high in some (e.g. immunology 100%) and low in others (e.g. anatomy 25%)](gpt4v-subdomain-performance-inconsistent.md) — related
- [GPT-4 achieves passing accuracy on USMLE Steps 1–3 (mean 86%), significantly exceeding GPT-3.5 (mean 56%)](gpt4-usme-passing-accuracy-exceeds-gpt35.md) — related
- [Newer OpenAI LLM versions achieve significantly higher pooled accuracy on biomedical MCQs than earlier versions (GPT‐4o–o1: 90%; GPT‐4: 82%; GPT‐3/3.5: 59%)](openai-llm-accuracy-improves-across-versions-biomedical-mcq.md) — related
