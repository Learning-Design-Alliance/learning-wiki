---
type: claim
title: "A trivial baseline generating \"Hello\" for every prompt achieved the best BERTScore precision and DialogRPT updown scores, exposing construct-irrelevant sensitivity in the automated metrics."
description: "A trivial baseline generating \"Hello\" for every prompt achieved the best BERTScore precision and DialogRPT updown scores, exposing construct-irrelevant sensitivity in the automated metrics."
id: hello-baseline-best-automated-metrics
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: anaïs-tack-2023
    resource: "https://doi.org/10.18653/v1/2023.bea-1.64"
    title: "Anaïs Tack, Ekaterina Kochmar, Zheng Yuan, Serge Bibauw, Chris Piech. (2023). The BEA 2023 Shared Task on Generating AI Teacher Responses in Educational Dialogues. [doi:10.18653/v1/2023.bea-1.64](https://doi.org/10.18653/v1/2023.bea-1.64)"
    author: Anaïs Tack, Ekaterina Kochmar, Zheng Yuan, Serge Bibauw, Chris Piech
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A trivial baseline generating "Hello" for every prompt achieved the best BERTScore precision and DialogRPT updown scores, exposing construct-irrelevant sensitivity in the automated metrics.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The RETUYT-InCo team observed that a baseline replying "Hello" to every prompt topped BERTScore precision and DialogRPT updown, demonstrating that these metrics can be gamed without pedagogically valid responses. [→ Anaïs Tack 2023](#anais-tack-2023)

## Evidence

### Anaïs Tack 2023

Anaïs Tack, Ekaterina Kochmar, Zheng Yuan, Serge Bibauw, Chris Piech. (2023). The BEA 2023 Shared Task on Generating AI Teacher Responses in Educational Dialogues. [doi:10.18653/v1/2023.bea-1.64](https://doi.org/10.18653/v1/2023.bea-1.64)

`q2 · i?` · `design · r2`

Reported observation by the RETUYT-InCo team (Baladón et al.) in their system paper, cited in the shared task's results discussion. The authors use it, with the teacher-prefix result, as evidence that BERTScore and DialogRPT "show considerable sensitivity to construct-irrelevant variations."

> "they found that a baseline generating "Hello" in response to every prompt achieved the best result for BERTScore precision and DialogRPT updown."

## Discussion


## Related Claims
- [DialogRPT scores were highly sensitive to the presence of a teacher prefix: identical GPT-4 responses scored 0.52 on updown with the prefix but 0.40 without it.](dialogrpt-teacher-prefix-sensitivity.md) — a narrower finding that bears on this claim
- [Participating teams found that smaller fine-tuned models can be competitive and that DialogRPT tends to prefer complete answers over pedagogically scaffolded ones.](team-observations-model-size-and-metric-bias.md) — related
