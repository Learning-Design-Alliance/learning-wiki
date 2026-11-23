---
type: claim
title: "Generative AI (Midjourney v 6.1) produces stereotypical images of scientists, with lab coat in 97%, eyeglasses in 97%, male gender in 81% and Caucasian in 85% of the 100 human-scored images"
description: "Generative AI (Midjourney v 6.1) produces stereotypical images of scientists, with lab coat in 97%, eyeglasses in 97%, male gender in 81% and Caucasian in 85% of the 100 human-scored images"
id: midjourney-scientist-images-stereotyped-dast
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
newest_evidence: 2025
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

# Generative AI (Midjourney v 6.1) produces stereotypical images of scientists, with lab coat in 97%, eyeglasses in 97%, male gender in 81% and Caucasian in 85% of the 100 human-scored images

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Images generated from the prompt "draw a scientist" predominantly show stereotypical features such as lab coat, eyeglasses, male gender and Caucasian appearance. [→ Gyeonggeon Lee 2025](#gyeonggeon-lee-2025)

## Evidence

### Gyeonggeon Lee 2025

Gyeonggeon Lee. (2025). Artificial Intelligence Generates Stereotypical Images of Scientists but Can Also Detect Them: A Pilot Study Using the Draw-A-Scientist Test. Version 1 - Last modified: Apr 27, 2025. [doi:10.48550/arXiv.2504.19005](https://doi.org/10.48550/arXiv.2504.19005)

`q2 · i?` · `design · r2`

Human scoring by the researcher, a PhD in science education, of 100 Midjourney-generated images coded for the 15 DAST-C features. The results report "stereotypical features in the image of scientist" at the listed percentages; the pilot study involved a single scorer and no inter-rater validation.

> "According to human scoring, there were stereotypical features in the image of scientist, such as '1. Lab Coat' (97%), '2. Eyeglasses' (97%), '8. Male Gender' (81%), '9. Caucasian' (85%), and '5. Symbols of Research' (72%)."

## Discussion


## Related Claims
- [gpt-4.1-mini can detect stereotypical features in AI-generated scientist images with 79% average human-machine agreement on the same 100 images](gpt-mini-detects-dast-stereotypes-79-mha.md) — related
- Machine scoring of an additional 1,000 Midjourney images replicates the stereotype pattern (lab coat 97%, eyeglasses 95%, male gender 82%, Caucasian 67%) — related
- [Machine-human agreement on DAST-C features varies widely, from 49-100%, being high for concrete features and low for uncertain ones such as scientist working indoors and middle-aged/elderly appearance](mha-varies-concrete-vs-uncertain-features.md) — related
- [Commercial text-to-image models produce accurate images for broad nuclear concepts but fail on specialized engineering prompts](commercial-models-fail-specialized-nuclear-prompts.md) — related
- [A gender-biased system prompt induces large gender-differentiated language in LLM-generated career essays, while a neutral prompt does not](biased-prompt-induces-gender-differentiated-llm-essays.md) — related
- [A neutrally configured LLM assistant produced the lowest rate of gender-stereotypic occupation suggestions, below even the no-AI control condition](neutral-llm-assistant-attenuates-baseline-stereotyping.md) — related
