---
type: claim
title: Re-sampling the same question against a fixed interaction history produces diverging LLM answers, revealing stochastic flips and trajectory bifurcation
description: Re-sampling the same question against a fixed interaction history produces diverging LLM answers, revealing stochastic flips and trajectory bifurcation
id: llm-resampling-reveals-stochastic-flips
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: tufino-2026
    resource: "https://doi.org/10.48550/arXiv.2602.01254"
    title: "Tufino, E. (2026). Demystifying the oracle: A \"20 Questions\" game to promote AI ethics and literacy. [doi:10.48550/arXiv.2602.01254](https://doi.org/10.48550/arXiv.2602.01254)"
    author: Tufino, E.
    q: 1
    i: "?"
    kind: design
    rigour: 1
  - id: tufino-2026-2
    resource: "https://doi.org/10.48550/arXiv.2602.01254"
    title: "Tufino, E. (2026). Demystifying the oracle: A \"20 Questions\" game to promote AI ethics and literacy. [doi:10.48550/arXiv.2602.01254](https://doi.org/10.48550/arXiv.2602.01254)"
    author: Tufino, E.
    q: 1
    i: "?"
    kind: design
    rigour: 1
---

# Re-sampling the same question against a fixed interaction history produces diverging LLM answers, revealing stochastic flips and trajectory bifurcation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r1` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Repeating the same question against the same antecedent history yielded fluctuating answers (a dominant "Yes" trajectory with 14 samples and a rare "No" trajectory with 2 samples), demonstrating the model samples from a probability distribution rather than retrieving a fixed fact. [→ Tufino 2026](#tufino-2026)
`q1 i?` A single stochastic flip redirected the conversation from the guess "Lamp" (Line A) to the guess "Car" (Line B), a macroscopic bifurcation from identical history. [→ Tufino 2026 (2)](#tufino-2026-2)

## Evidence

### Tufino 2026

Tufino, E. (2026). Demystifying the oracle: A "20 Questions" game to promote AI ethics and literacy. [doi:10.48550/arXiv.2602.01254](https://doi.org/10.48550/arXiv.2602.01254)

`q1 · i?` · `design · r1`

Case study using Google's Gemini 2.5 Flash in the authors' app: resampling Q2 ("Is it relatively small?") against fixed history H1 gave 14 "Yes" and 2 "No" samples. This "observed variance confirms that the model does not hold a fixed internal truth" but samples from a distribution.

> "As reported in Supplementary material, the resampling process yielded a dominant "Yes" trajectory (14 samples) and a rare "No" trajectory (2 samples)."

### Tufino 2026 (2)

Tufino, E. (2026). Demystifying the oracle: A "20 Questions" game to promote AI ethics and literacy. [doi:10.48550/arXiv.2602.01254](https://doi.org/10.48550/arXiv.2602.01254)

`q1 · i?` · `design · r1`

In the same case study, the user adopted the rare "No" outcome as the new branch's history and continued questioning, ending at "Car". The demonstration shows the flip "redirects the space of compatible continuations".

> "The application displays an explicit bifurcation summary: Line A ends at "Lamp"; Line B ends at "Car"."

## Discussion


## Related Claims
- [Preliminary workshops with in-service teachers reveal a persistent \"Hidden Variable\" misconception that the activity is designed to challenge](hidden-variable-misconception-llm-game.md) — related
- [GPT-2 generates different text for the same prompt across repeated runs, demonstrating its stochastic output](gpt2-stochastic-output-varies-across-runs.md) — a broader claim this one bears on
- [Smaller local LLMs show a minor position bias toward option ordering and partially guessing-like error variation, but accuracy remains relatively stable across permutations and repeated sampling runs](minor-position-bias-and-partial-guessing-in-small-llms.md) — related
- [The benchmark procedure is stable under stochastic decoding, with a maximum accuracy standard deviation of 0.43% over 20 repeated runs](cdpk-benchmark-stability-0-43-percent-sd.md) — related
