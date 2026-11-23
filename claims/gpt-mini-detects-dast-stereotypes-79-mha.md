---
type: claim
title: "gpt-4.1-mini can detect stereotypical features in AI-generated scientist images with 79% average human-machine agreement on the same 100 images"
description: "gpt-4.1-mini can detect stereotypical features in AI-generated scientist images with 79% average human-machine agreement on the same 100 images"
id: gpt-mini-detects-dast-stereotypes-79-mha
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
newest_evidence: 2025
source_checked: 2026-11-23
recheck_by: 2028
sources:
  - id: gyeonggeon-lee-2025
    resource: "https://doi.org/10.48550/arXiv.2504.19005"
    title: "Gyeonggeon Lee. (2025). Artificial Intelligence Generates Stereotypical Images of Scientists but Can Also Detect Them: A Pilot Study Using the Draw-A-Scientist Test. Version 1 - Last modified: Apr 27, 2025. [doi:10.48550/arXiv.2504.19005](https://doi.org/10.48550/arXiv.2504.19005)"
    author: Gyeonggeon Lee
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# gpt-4.1-mini can detect stereotypical features in AI-generated scientist images with 79% average human-machine agreement on the same 100 images

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · checked against its sources 2026-11-23 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A VLM prompted with the DAST-C rubric scored the 15 stereotype features with an average machine-human agreement of 79%, which the author calls fair. [→ Gyeonggeon Lee 2025](#gyeonggeon-lee-2025)

## Evidence

### Gyeonggeon Lee 2025

Gyeonggeon Lee. (2025). Artificial Intelligence Generates Stereotypical Images of Scientists but Can Also Detect Them: A Pilot Study Using the Draw-A-Scientist Test. Version 1 - Last modified: Apr 27, 2025. [doi:10.48550/arXiv.2504.19005](https://doi.org/10.48550/arXiv.2504.19005)

`q2 · i?` · `design · r2`

Machine scoring of the same 100 sampled images using gpt-4.1-mini, iteratively called via API with the image and a rubric-based prompt. The author reports "The average MHA was 79%" and treats this agreement as evidence of the scoring machine's validity; no statistical test or effect size is printed.

> "The average MHA was 79%, which is fair. This shows that VLMs' scoring of image of scientist shows considerable MHA, which can be thought as a validity of the scoring machine."

## Discussion


## Related Claims
- [Generative AI (Midjourney v 6.1) produces stereotypical images of scientists, with lab coat in 97%, eyeglasses in 97%, male gender in 81% and Caucasian in 85% of the 100 human-scored images](midjourney-scientist-images-stereotyped-dast.md) — related
- [Machine-human agreement on DAST-C features varies widely, from 49-100%, being high for concrete features and low for uncertain ones such as scientist working indoors and middle-aged/elderly appearance](mha-varies-concrete-vs-uncertain-features.md) — related
- Machine scoring of an additional 1,000 Midjourney images replicates the stereotype pattern (lab coat 97%, eyeglasses 95%, male gender 82%, Caucasian 67%) — related
