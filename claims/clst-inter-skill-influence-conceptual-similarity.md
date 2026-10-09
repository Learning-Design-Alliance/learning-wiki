---
type: claim
title: Quantitative inter-skill influence analysis shows conceptually similar skills exert the strongest mutual influence in CLST predictions
description: Quantitative inter-skill influence analysis shows conceptually similar skills exert the strongest mutual influence in CLST predictions
id: clst-inter-skill-influence-conceptual-similarity
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: weak
sources:
  - id: heeseok-jung-2025
    resource: "https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2"
    title: "Heeseok Jung, Yohaan Yoon, Jaesang Yoo, Yeonju Jang. (2025). CLST: Cold-Start Mitigation in Knowledge Tracing by Aligning a Generative Language Model as a Students' Knowledge Tracer. Journal of Educational Data Mining, Volume 17, No 2. https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2"
    author: Heeseok Jung, Yohaan Yoon, Jaesang Yoo, Yeonju Jang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Quantitative inter-skill influence analysis shows conceptually similar skills exert the strongest mutual influence in CLST predictions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Using Piech et al.'s influence metric over skill pairs, the top influencing skills for a given skill were conceptually related ones, e.g., Area Rectangle and Area Triangle for Area Circle in mathematics. [→ Heeseok Jung 2025](#heeseok-jung-2025)

## Evidence

### Heeseok Jung 2025

Heeseok Jung, Yohaan Yoon, Jaesang Yoo, Yeonju Jang. (2025). CLST: Cold-Start Mitigation in Knowledge Tracing by Aligning a Generative Language Model as a Students' Knowledge Tracer. Journal of Educational Data Mining, Volume 17, No 2. https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2

`q2 · i?` · `design · r2`

Quantitative inter-skill influence analysis (Tables 9-11) computing Jij for every skill pair per the methodology of Piech et al. (2015), reporting the top two influencing skills for five skills per dataset. The article found "skills sharing conceptual similarities tend to exert strong mutual influence" across math, social studies, and science.

> "The analysis indicates that skills sharing conceptual similarities tend to exert strong mutual influence."

## Discussion


## Related Claims
- [CLST's predicted mastery levels track response correctness and move similarly for related knowledge components](clst-mastery-tracks-correctness-and-related-kcs.md) — related
- [The rank ordering of math and reading skills is highly stable over time, while four SEL domains are more strongly influenced by contextual factors](sel-domains-less-stable-than-achievement.md) — related
