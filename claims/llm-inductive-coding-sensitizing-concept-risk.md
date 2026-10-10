---
type: claim
title: "Fully inductive LLM codebook development risks importing unexamined sensitizing concepts, such as folk theories and scientific misconceptions, from the model's training data"
description: "Fully inductive LLM codebook development risks importing unexamined sensitizing concepts, such as folk theories and scientific misconceptions, from the model's training data"
id: llm-inductive-coding-sensitizing-concept-risk
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: weak
sources:
  - id: zambrano-2026
    resource: "https://osf.io/g3z4x"
    title: "Zambrano, A.F., Wei, Z., Zhang, J., Baker, R.S., Ocumpaugh, J., Barany, A., Liu, X., Ginger, J., Paquette, L., Zhou, Y., & Borchers, C. (2026). Data Plus Theory Equals Codebook: Leveraging LLMs for Human-AI Codebook Development. Journal of Educational Data Mining, Volume 18, No 1. https://osf.io/g3z4x"
    author: "Zambrano, A.F., Wei, Z., Zhang, J., Baker, R.S., Ocumpaugh, J., Barany, A., Liu, X., Ginger, J., Paquette, L., Zhou, Y., & Borchers, C."
    q: 1
    i: "?"
    kind: design
    rigour: 3
---

# Fully inductive LLM codebook development risks importing unexamined sensitizing concepts, such as folk theories and scientific misconceptions, from the model's training data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q1`

## Subclaims
`q1 i?` If not prompted toward specific theory, GPT may implicitly apply sensitizing concepts drawn from non-neutral training data, and such implicit theoretical choices may go unnoticed by researchers. [→ Zambrano 2026](#zambrano-2026)

## Evidence

### Zambrano 2026

Zambrano, A.F., Wei, Z., Zhang, J., Baker, R.S., Ocumpaugh, J., Barany, A., Liu, X., Ginger, J., Paquette, L., Zhou, Y., & Borchers, C. (2026). Data Plus Theory Equals Codebook: Leveraging LLMs for Human-AI Codebook Development. Journal of Educational Data Mining, Volume 18, No 1. https://osf.io/g3z4x

`q1 · i?` · `design · r3`

Theoretical argument, not a tested result: the authors reason from prior work that LLM training data "is not neutral or atheoretical", so fully inductive prompting risks unnoticed biases that expert oversight may miss, such as missing codes or blends of related theories.

> "If not prompted to consider specific theory, GPT might draw its sensitizing concepts from, for example, the folk theories or widely believed scientific misconceptions present in its training data"

## Discussion


## Related Claims
- [GPT-4o prompted only with SRL theory references generates a codebook accurately representing most key elements of both foundational SRL theories](gpt4o-theory-references-codebook-covers-srl-theories.md) — related
- [LLM-assisted inductive qualitative coding carries risks of superficial themes, broad or redundant codes, and hallucinated interpretations, so LLMs should augment rather than replace human researchers](llm-inductive-coding-risks-require-human-oversight.md) — a broader claim this one bears on
- [A hybrid human-AI workflow using GPT-4o with retrieval-augmented generation supported efficient inductive thematic analysis while preserving researcher judgment](hybrid-gpt4o-human-inductive-thematic-analysis-workflow.md) — related
- [In the interest-development context, naming the theory without full references produced the most practical and usable codebook, while supplying full papers enhanced theoretical alignment but reduced applicability](naming-theory-most-practical-prompting-strategy.md) — related
- [Adding think-aloud data to theory prompts improves GPT-4o codebook completeness and alignment with the data](theory-plus-data-prompting-improves-codebook.md) — related
- [Five common AI misconceptions debunked: AI does not think like humans, create original ideas, replace teachers, or guarantee accuracy, and well-designed AI use need not lower rigor](five-ai-misconceptions-for-educators.md) — related
- [Attachment to LLMs exhibits cruel optimism: desired efficiency collides with the vigilance and expertise students do not yet possess](cruel-optimism-of-llms-in-education.md) — related
- [A general-purpose LLM assessing team emails' emotional tone was biased toward interpreting messages as anxiety-related only](llm-emotional-tone-bias-incident-words.md) — a narrower finding that bears on this claim
