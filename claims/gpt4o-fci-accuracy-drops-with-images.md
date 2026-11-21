---
type: claim
title: "GPT-4o answered only 59% of pre-test questions correctly, with accuracy dropping sharply as the number of images per question increased"
description: "GPT-4o answered only 59% of pre-test questions correctly, with accuracy dropping sharply as the number of images per question increased"
id: gpt4o-fci-accuracy-drops-with-images
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: weijers-2025
    resource: "https://doi.org/10.48550/arXiv.2504.00408"
    title: "Weijers, R., Wu, D., Betts, H., Jacod, T., Guan, L. Y., Sujaya, V., Dev, K., Goel, T., Delooze, W., Rabbany, R., Wu, Y., Godbout, J.-F., & Pelrine, K. (2025). From Intuition to Understanding: Using AI Peers to Overcome Physics Misconceptions. [doi:10.48550/arXiv.2504.00408](https://doi.org/10.48550/arXiv.2504.00408)"
    author: "Weijers, R., Wu, D., Betts, H., Jacod, T., Guan, L. Y., Sujaya, V., Dev, K., Goel, T., Delooze, W., Rabbany, R., Wu, Y., Godbout, J.-F., & Pelrine, K."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# GPT-4o answered only 59% of pre-test questions correctly, with accuracy dropping sharply as the number of images per question increased

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-4o averaged 59% correct on the modified FCI pre-test over 5 iterations, and performed worse on questions with more image descriptions (26.67% correct for questions with more than 2 images). [→ Weijers 2025](#weijers-2025)

## Evidence

### Weijers 2025

Weijers, R., Wu, D., Betts, H., Jacod, T., Guan, L. Y., Sujaya, V., Dev, K., Goel, T., Delooze, W., Rabbany, R., Wu, Y., Godbout, J.-F., & Pelrine, K. (2025). From Intuition to Understanding: Using AI Peers to Overcome Physics Misconceptions. [doi:10.48550/arXiv.2504.00408](https://doi.org/10.48550/arXiv.2504.00408)

`q2 · i?` · `causal · r2`

Model evaluation feeding written image descriptions to GPT-4o-2024-08-06 at temperature 0.7 over 5 iterations; Table 1 shows 67.69% correct with 0 images, 62.22% with 1, and 26.67% with more than 2. "GPT-4o got 59% of pre-test questions correct over 5 iterations".

> "On average, GPT-4o got 59% of pre-test questions correct over 5 iterations when using written image descriptions"

## Discussion


## Related Claims
- [GPT-4o answered image-based USMLE sample items with 89.5% accuracy versus GPT-4's 73.4%, a numerically higher but not statistically significant difference](gpt4o-89-5-percent-image-usmle-accuracy.md) — related
- [GPT-4o answered both image-based PNA questions correctly](gpt-4o-answered-image-questions-correctly.md) — related
- [ChatGPT3.5 answers 15 of 23 modified FCI questions correctly, scoring near or above the median end-of-semester student](chatgpt35-fci-15-of-23-near-median-student.md) — related
- [Model strengths differ by question type: Gemini 1.5 Pro leads on A1 recall and image-based questions, Claude 3.5 Sonnet on A2 application, and Gemini and GPT-4o on case analysis](llm-strengths-vary-by-srtp-question-type.md) — related
- [GPT-4o accuracy on image-required FCI questions (36–38%) is substantially weaker than on text-only and image-optional questions (97–100%)](image-required-questions-low-llm-accuracy.md) — related
