---
type: claim
title: "Excluding zero-scoring answers, AI averages rise to 65.6% (GPT-4) and 56.7% (GPT-3.5), suggesting a use case for AI-provided hints"
description: "Excluding zero-scoring answers, AI averages rise to 65.6% (GPT-4) and 56.7% (GPT-3.5), suggesting a use case for AI-provided hints"
id: ai-hint-use-case-excluding-zero-scores
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: will-yeadon-2023
    resource: "https://doi.org/10.48550/arXiv.2306.15609"
    title: "Will Yeadon, Douglas P. Halliday. (2023). Exploring Durham University Physics Exams with Large Language Models. [doi:10.48550/arXiv.2306.15609](https://doi.org/10.48550/arXiv.2306.15609)"
    author: Will Yeadon, Douglas P. Halliday
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: will-yeadon-2023-2
    resource: "https://doi.org/10.48550/arXiv.2306.15609"
    title: "Will Yeadon, Douglas P. Halliday. (2023). Exploring Durham University Physics Exams with Large Language Models. [doi:10.48550/arXiv.2306.15609](https://doi.org/10.48550/arXiv.2306.15609)"
    author: Will Yeadon, Douglas P. Halliday
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Excluding zero-scoring answers, AI averages rise to 65.6% (GPT-4) and 56.7% (GPT-3.5), suggesting a use case for AI-provided hints

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` When answers scoring zero are excluded, overall averages stand at 56.7% for GPT-3.5 and 65.6% for GPT-4, indicating potential for AI as a provider of useful hints. [→ Will Yeadon 2023](#will-yeadon-2023)
`q2 i?` On Mathematical Methods in Physics, GPT-3.5 outperformed GPT-4 when zero-scoring answers were excluded, the only instance of such a result. [→ Will Yeadon 2023 (2)](#will-yeadon-2023-2)

## Evidence

### Will Yeadon 2023

Will Yeadon, Douglas P. Halliday. (2023). Exploring Durham University Physics Exams with Large Language Models. [doi:10.48550/arXiv.2306.15609](https://doi.org/10.48550/arXiv.2306.15609)

`q2 · i?` · `design · r2`

Re-analysis of the marked exam answers excluding zero-scoring responses, which occurred 30.0% of the time for GPT-4 and 40.1% for GPT-3.5. The article reports the printed averages of 56.7% and 65.6%; no effect size is given.

> "The overall averages notably stand at 56.7% for GPT-3.5 and 65.6% for GPT-4, indicating a potential use case for AI as a provider of useful ’hints’ that students could expand upon."

### Will Yeadon 2023 (2)

Will Yeadon, Douglas P. Halliday. (2023). Exploring Durham University Physics Exams with Large Language Models. [doi:10.48550/arXiv.2306.15609](https://doi.org/10.48550/arXiv.2306.15609)

`q2 · i?` · `design · r2`

Within the zero-excluded analysis (Figure 6), the article reports the single exam where GPT-3.5 scored higher than GPT-4, on Mathematical Methods in Physics.

> "Interestingly, when it came to Mathematical Methods in Physics, GPT-3.5 outperformed GPT-4, marking the only instance of such a result."

## Discussion


## Related Claims
- [Bootstrapped self-consistency at temperature 1.0 flags potentially incorrect GPT-4 answers: about half of inconsistent responses were incorrect versus about 5% of consistent ones](bootstrapping-self-consistency-flags-incorrect-answers.md) — related
- [A sensitivity analysis excluding not-applicable answers (e.g., image-based items) yielded results similar to the main accuracy comparison](cineca-accuracy-sensitivity-analysis-similar-results.md) — related
- [Hint-not-solution is the most challenging rubric dimension, with scores ranging from 6% to 81% across models](hint-not-solution-most-challenging-dimension.md) — related
- [GPT-4 outperforms GPT-3.5 on real university physics exams, averaging 49.4% versus 38.6%](gpt4-outperforms-gpt35-physics-exams.md) — related
