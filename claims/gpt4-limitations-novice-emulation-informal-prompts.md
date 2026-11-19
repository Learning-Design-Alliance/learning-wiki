---
type: claim
title: GPT-4 could not reproduce novice reasoning when prompted, and failed on physics questions not phrased in canonical physics tone and nomenclature
description: GPT-4 could not reproduce novice reasoning when prompted, and failed on physics questions not phrased in canonical physics tone and nomenclature
id: gpt4-limitations-novice-emulation-informal-prompts
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: colin-g-west-2023
    resource: "https://doi.org/10.48550/arXiv.2303.17012"
    title: "Colin G. West. (2023). Advances in apparent conceptual physics reasoning in GPT-4. arXiv preprint. [doi:10.48550/arXiv.2303.17012](https://doi.org/10.48550/arXiv.2303.17012)"
    author: Colin G. West
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: colin-g-west-2023-2
    resource: "https://doi.org/10.48550/arXiv.2303.17012"
    title: "Colin G. West. (2023). Advances in apparent conceptual physics reasoning in GPT-4. arXiv preprint. [doi:10.48550/arXiv.2303.17012](https://doi.org/10.48550/arXiv.2303.17012)"
    author: Colin G. West
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4 could not reproduce novice reasoning when prompted, and failed on physics questions not phrased in canonical physics tone and nomenclature

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-4 resisted changing correct answers even when prompted to pretend it did not know Newton's Laws, appearing incapable of reproducing novice reasoning. [→ Colin G. West 2023](#colin-g-west-2023)
`q2 i?` In three brief tests, GPT-4 failed on informally phrased physics questions about content it had handled on the FCI, e.g. misapplying momentum in a toy-truck scenario. [→ Colin G. West 2023 (2)](#colin-g-west-2023-2)

## Evidence

### Colin G. West 2023

Colin G. West. (2023). Advances in apparent conceptual physics reasoning in GPT-4. arXiv preprint. [doi:10.48550/arXiv.2303.17012](https://doi.org/10.48550/arXiv.2303.17012)

`q2 · i?` · `design · r2`

Prompt-based tests, described in more detail in the author's prior work, in which GPT-4 was asked to emulate a novice and resisted changing any answers it initially got correct. The author likens the result to a professor who cannot recall not knowing the concepts.

> "it seems completely incapable of reproducing the reasoning of a novice, even in the face of various prompts asking it to pretend it does not know things like Newton’s Laws."

### Colin G. West 2023 (2)

Colin G. West. (2023). Advances in apparent conceptual physics reasoning in GPT-4. arXiv preprint. [doi:10.48550/arXiv.2303.17012](https://doi.org/10.48550/arXiv.2303.17012)

`q2 · i?` · `design · r2`

Three brief informal-prompt tests, e.g. a toddler's toy trucks pushed off a table, where GPT-4 misapplied momentum. The author stipulates the informal question is harder than the corresponding FCI item and notes others found more reasonable answers with different prompt wording.

> "in three brief tests we performed, GPT-4 failed spectacularly at responding to questions which did not adopt the canonical tone and nomenclature of a physics problem"

## Discussion


## Related Claims
- [GPT-4o sometimes selects correct answers with flawed reasoning and answers inaccuracies in an authoritative tone, risking user overconfidence](llm-flawed-reasoning-authoritative-tone.md) — related
- [Student explanations of projectile motion questions can reflect valid causal pathways in the canonical network even when the reasoning is not generally correct](lower-angle-less-time-valid-causal-pathway.md) — related
- [Introductory students overlooked the similarity between isomorphic friction and tension problems: 28% correct on the friction problem versus 72% on the tension problem](isomorphic-friction-tension-overlooked-similarity.md) — related
- [Question keywords correlate with GPT-4 scores: mathematical terms with lower scores, 'explain' with higher, and 'sketch' showing the strongest negative correlation](keyword-correlations-gpt4-physics-scores.md) — related
