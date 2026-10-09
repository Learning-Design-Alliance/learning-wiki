---
type: claim
title: Adding think-aloud data to theory prompts improves GPT-4o codebook completeness and alignment with the data
description: Adding think-aloud data to theory prompts improves GPT-4o codebook completeness and alignment with the data
id: theory-plus-data-prompting-improves-codebook
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: zambrano-2026
    resource: "https://osf.io/g3z4x"
    title: "Zambrano, A.F., Wei, Z., Zhang, J., Baker, R.S., Ocumpaugh, J., Barany, A., Liu, X., Ginger, J., Paquette, L., Zhou, Y., & Borchers, C. (2026). Data Plus Theory Equals Codebook: Leveraging LLMs for Human-AI Codebook Development. Journal of Educational Data Mining, Volume 18, No 1. https://osf.io/g3z4x"
    author: "Zambrano, A.F., Wei, Z., Zhang, J., Baker, R.S., Ocumpaugh, J., Barany, A., Liu, X., Ginger, J., Paquette, L., Zhou, Y., & Borchers, C."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: zambrano-2026-2
    resource: "https://osf.io/g3z4x"
    title: "Zambrano, A.F., Wei, Z., Zhang, J., Baker, R.S., Ocumpaugh, J., Barany, A., Liu, X., Ginger, J., Paquette, L., Zhou, Y., & Borchers, C. (2026). Data Plus Theory Equals Codebook: Leveraging LLMs for Human-AI Codebook Development. Journal of Educational Data Mining, Volume 18, No 1. https://osf.io/g3z4x"
    author: "Zambrano, A.F., Wei, Z., Zhang, J., Baker, R.S., Ocumpaugh, J., Barany, A., Liu, X., Ginger, J., Paquette, L., Zhou, Y., & Borchers, C."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Adding think-aloud data to theory prompts improves GPT-4o codebook completeness and alignment with the data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` The Theory+Data codebook captured elements from all phases of both SRL models, including the task-definition phase missing from the theory-only codebook, and produced fewer overlapping constructs. [→ Zambrano 2026](#zambrano-2026)
`q2 i?` When data was available, GPT filtered out theory-relevant constructs absent from the data, such as Imitation and Social Environment. [→ Zambrano 2026 (2)](#zambrano-2026-2)

## Evidence

### Zambrano 2026

Zambrano, A.F., Wei, Z., Zhang, J., Baker, R.S., Ocumpaugh, J., Barany, A., Liu, X., Ginger, J., Paquette, L., Zhou, Y., & Borchers, C. (2026). Data Plus Theory Equals Codebook: Leveraging LLMs for Human-AI Codebook Development. Journal of Educational Data Mining, Volume 18, No 1. https://osf.io/g3z4x

`q2 · i?` · `design · r2`

Step 2 (Theory+Data) prompting on 955 segmented think-aloud utterances from fifteen students in three intelligent tutoring systems. The authors report the codebook "capturing elements from all phases of both theoretical models", with fewer overlapping constructs and a new Error Identification construct.

> "When provided with the data, GPT produced a codebook that was more complete (see Table 1), capturing elements from all phases of both theoretical models."

### Zambrano 2026 (2)

Zambrano, A.F., Wei, Z., Zhang, J., Baker, R.S., Ocumpaugh, J., Barany, A., Liu, X., Ginger, J., Paquette, L., Zhou, Y., & Borchers, C. (2026). Data Plus Theory Equals Codebook: Leveraging LLMs for Human-AI Codebook Development. Journal of Educational Data Mining, Volume 18, No 1. https://osf.io/g3z4x

`q2 · i?` · `design · r2`

In the same Step 2 analysis, constructs like Imitation and Social Environment that emerged in Step 1 "did not appear in Step Two", and motivational constructs were replaced with data-grounded ones like Frustration, yielding "better alignment with the students' think-aloud data".

> "Finally, constructs that were relevant to the theory but absent from the data  (see discussion in Section 3.4.1), were appropriately filtered out by GPT  once the data was available ."

## Discussion


## Related Claims
- [GPT-4o prompted only with SRL theory references generates a codebook accurately representing most key elements of both foundational SRL theories](gpt4o-theory-references-codebook-covers-srl-theories.md) — related
- [Human review remains essential after GPT-based codebook generation, producing a final refined SRL codebook of eleven constructs](human-refinement-essential-gpt-codebooks.md) — related
- [Fully inductive LLM codebook development risks importing unexamined sensitizing concepts, such as folk theories and scientific misconceptions, from the model's training data](llm-inductive-coding-sensitizing-concept-risk.md) — related
- [In the interest-development context, naming the theory without full references produced the most practical and usable codebook, while supplying full papers enhanced theoretical alignment but reduced applicability](naming-theory-most-practical-prompting-strategy.md) — related
