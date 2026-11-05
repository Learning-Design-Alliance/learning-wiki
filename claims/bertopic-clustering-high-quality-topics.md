---
type: claim
title: BERTopic clustering of medical documents produced highly distinct topics rated highly by medical experts
description: BERTopic clustering of medical documents produced highly distinct topics rated highly by medical experts
id: bertopic-clustering-high-quality-topics
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: pang-xiao-2026
    resource: "https://doi.org/10.2196/83785"
    title: "Pang Xiao, Liu Chang, Huang Yan, Liu MingYou, Liu Jiyuan. (2026). An Entity-Based Visual Analytics System Enhancing Medical Expertise Acquisition: Development and Verification Study. JMIR Medical Informatics. https://doi.org/10.2196/83785"
    author: Pang Xiao, Liu Chang, Huang Yan, Liu MingYou, Liu Jiyuan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# BERTopic clustering of medical documents produced highly distinct topics rated highly by medical experts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Topic clustering of document embeddings yielded a topic diversity score of 0.975, and expert Likert ratings averaged 4.3 (interpretability), 4.4 (distinctiveness), and 4.6 (relevance). [→ Pang Xiao 2026](#pang-xiao-2026)

## Evidence

### Pang Xiao 2026

Pang Xiao, Liu Chang, Huang Yan, Liu MingYou, Liu Jiyuan. (2026). An Entity-Based Visual Analytics System Enhancing Medical Expertise Acquisition: Development and Verification Study. JMIR Medical Informatics. https://doi.org/10.2196/83785

`q2 · i?` · `design · r2`

Topic clustering step of the data pipeline using BERTopic over ESimCSE-BERT embeddings; a 5-point Likert assessment by five medical experts (E3, E4, E6, E7, E8) rated interpretability 4.3 (0.57), distinctiveness 4.4 (0.41), and relevance 4.6 (0.22), with a "topic diversity score [53] of 0.975".

> "The results yielded a topic diversity score [53] of 0.975, indicating a high degree of distinctness among the generated categories."

## Discussion


## Related Claims
- [LDA topic modeling of HI/HIM AI policy documents identifies four dominant themes: academic integrity, generative AI use, AI in research, and ChatGPT engagement](lda-four-themes-hi-him-ai-policies.md) — related
- [Topic modelling yielded 16 topics dominated by four: AI in Education & Pedagogy (39.43%), Applied ML & Data Science (21.33%), AI Ethics Risk & Governance (20.83%), and ChatGPT for Teaching, Writing & Coding (7.13%)](four-dominant-bertopic-topics-aied-twitter.md) — related
- [GenAI guidelines at top U.S. universities cluster into four topics: learning and assessment integration, visual/multimodal media, security and ethics, and academic integrity](four-topics-genai-guidelines-heis.md) — related
- [Domain experts rated MExplore positively and recommended it for medical expertise acquisition](expert-interviews-positive-mexplore-acceptance.md) — related
