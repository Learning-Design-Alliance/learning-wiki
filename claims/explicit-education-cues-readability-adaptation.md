---
type: claim
title: Explicitly mentioned education and SES cues lead most models to produce less readable responses for higher-education users, showing partial readability adaptation
description: Explicitly mentioned education and SES cues lead most models to produce less readable responses for higher-education users, showing partial readability adaptation
id: explicit-education-cues-readability-adaptation
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: donya-rooein-2026
    resource: "https://arxiv.org/abs/2609.16993"
    title: "Donya Rooein, Luca Benedetto, Dirk Hovy. (2026). The Role of Implicit and Explicit Demographic Signals in Large Language Model-based Student Assessment. https://arxiv.org/abs/2609.16993"
    author: Donya Rooein, Luca Benedetto, Dirk Hovy
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: donya-rooein-2026-2
    resource: "https://arxiv.org/abs/2609.16993"
    title: "Donya Rooein, Luca Benedetto, Dirk Hovy. (2026). The Role of Implicit and Explicit Demographic Signals in Large Language Model-based Student Assessment. https://arxiv.org/abs/2609.16993"
    author: Donya Rooein, Luca Benedetto, Dirk Hovy
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Explicitly mentioned education and SES cues lead most models to produce less readable responses for higher-education users, showing partial readability adaptation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` When education levels are explicitly mentioned, users with higher educational level receive less readable responses, indicating models can partially adapt readability. [→ Donya Rooein 2026](#donya-rooein-2026)
`q2 i?` This readability adaptation does not occur under implicit conditioning, which instead produces surface mimicry such as longer responses for longer prompt histories. [→ Donya Rooein 2026 (2)](#donya-rooein-2026-2)

## Evidence

### Donya Rooein 2026

Donya Rooein, Luca Benedetto, Dirk Hovy. (2026). The Role of Implicit and Explicit Demographic Signals in Large Language Model-based Student Assessment. https://arxiv.org/abs/2609.16993

`q2 · i?` · `causal · r2`

Regression analysis of Automated Readability Index (ARI) and Flesch Reading Ease (FRE) of responses in the QA task. The Education attribute produced significant positive ARI coefficients under explicit conditioning for Llama-70B, Llama-3B, Qwen-30B, and GPT-mini; similar effects appeared for mum_education, ses, and dad_education (Llama-70B).

> "users with higher educational level receive less readable responses: this suggests that if the models have access to an explicit reference to the educational level of the user they can partially adapt the readability of their responses."

### Donya Rooein 2026 (2)

Donya Rooein, Luca Benedetto, Dirk Hovy. (2026). The Role of Implicit and Explicit Demographic Signals in Large Language Model-based Student Assessment. https://arxiv.org/abs/2609.16993

`q2 · i?` · `causal · r2`

Cross-condition comparison of the QA readability results: under implicit conditioning the education-based readability adaptation is absent, and the article states the models "often mimic surface characteristics of previous prompt histories (e.g., longer responses for users with longer prompts in their history)". Implicit coefficients were smaller (µb = 0.56 for ARI, 0.51 for FRE).

> "Overall, our readability analysis suggests that when Exp references to the user’s (or their parents’) education level or Socio-Economic Status are avail- able, most models partially adapt their responses"

## Discussion


## Related Claims
- [Higher stated education and SES levels receive responses with more positive sentiment, an implicit bias that can disadvantage lower-education users](education-ses-sentiment-bias-qa.md) — related
- [Implicit demographic conditioning inflates AES scores in some models, with Llama-70B scores rising 1.57 points over its own default, while GPT models remain stable](implicit-conditioning-inflates-aes-scores-llama-70b.md) — related
