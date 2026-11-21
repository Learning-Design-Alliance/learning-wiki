---
type: claim
title: NTKT maintains stable performance on unseen cold-start questions while baselines show a significant drop between seen and unseen questions
description: NTKT maintains stable performance on unseen cold-start questions while baselines show a significant drop between seen and unseen questions
id: ntkt-question-cold-start-stability
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: max-norris-2025
    resource: "https://doi.org/10.48550/arXiv.2511.02599"
    title: "Max Norris, Kobi Gal and Sahan Bulathwela. (2025). Next Token Knowledge Tracing: Exploiting Pretrained LLM Representations to Decode Student Behaviour. arXiv. [doi:10.48550/arXiv.2511.02599](https://doi.org/10.48550/arXiv.2511.02599)"
    author: Max Norris, Kobi Gal and Sahan Bulathwela
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# NTKT maintains stable performance on unseen cold-start questions while baselines show a significant drop between seen and unseen questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Baseline models drop from 0.777 to 0.732 on unseen questions (p < 0.001), whereas NTKT maintains stable performance at 0.843 on both seen and unseen questions (p > 0.5). [→ Max Norris 2025](#max-norris-2025)

## Evidence

### Max Norris 2025

Max Norris, Kobi Gal and Sahan Bulathwela. (2025). Next Token Knowledge Tracing: Exploiting Pretrained LLM Representations to Decode Student Behaviour. arXiv. [doi:10.48550/arXiv.2511.02599](https://doi.org/10.48550/arXiv.2511.02599)

`q2 · i?` · `design · r2`

Question cold-start experiment (RQ3, Figure 3) evaluating on ten unseen questions spanning difficulty and topic diversity, with 7,297 students (18.5% of the total) contributing responses. Both NTKT variants showed stable or slightly improved gains on unseen items.

> "Baseline models exhibit a clear performance drop between seen and unseen questions (0.777 to 0.732,p <0.001), whereas NTKT maintains stable performance (0.843 on both,p >0.5)."

## Discussion


## Related Claims
- [In user cold-start scenarios, NTKT achieves higher F1 than baselines from the first interaction and personalises rapidly as history grows](ntkt-user-cold-start-fast-personalisation.md) — related
- [Modeling knowledge transfer within and across domains alleviates the cold-start problem on unseen concepts](knowledge-transfer-alleviates-cold-start-kt.md) — related
- [LLMs are more stable than supervised models across dataset shifts, though they do not surpass within-dataset fine-tuned performance](llms-more-stable-cross-dataset-than-supervised.md) — a broader claim this one bears on
- [All pretrained transformer models showed a significant performance drop of about 20% between IID and OOD data, and OOD performance correlated linearly with IID performance](pretrained-transformers-twenty-percent-ood-drop.md) — a broader claim this one bears on
- [Including full question text yields the best NTKT performance; removing text degrades AUC (ID-only 77.06% vs full text 90.32%)](question-text-improves-kt-accuracy.md) — related
