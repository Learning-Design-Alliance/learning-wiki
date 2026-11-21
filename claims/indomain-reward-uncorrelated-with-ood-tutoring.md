---
type: claim
title: In-domain reward maximization is essentially uncorrelated with out-of-distribution tutoring performance across methods
description: In-domain reward maximization is essentially uncorrelated with out-of-distribution tutoring performance across methods
id: indomain-reward-uncorrelated-with-ood-tutoring
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: unggi-lee-2026
    resource: "https://doi.org/10.48550/arXiv.2605.27088"
    title: "Unggi Lee, Minchul Shin, Yeil Jeong, Sookbun Lee, Jeongsu Moon, Kyungtae Joo, Eunjoo Lee, Hoilym Kwon. (2026). LLMs Are Already Good Tutors: Training-Free Prompt Optimization for Pedagogical Math Tutoring. arXiv preprint. [doi:10.48550/arXiv.2605.27088](https://doi.org/10.48550/arXiv.2605.27088)"
    author: Unggi Lee, Minchul Shin, Yeil Jeong, Sookbun Lee, Jeongsu Moon, Kyungtae Joo, Eunjoo Lee, Hoilym Kwon
    q: 2
    i: 0
    kind: causal
    rigour: 2
---

# In-domain reward maximization is essentially uncorrelated with out-of-distribution tutoring performance across methods

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2` · `i0` negligible
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i0` In-domain Rtotal shows essentially no correlation with OOD MathTutorBench-Avg (ρ = 0.01, p = 0.96) and only a weak correlation with OpenLearnLM-Avg (ρ = 0.25, p = 0.41). [→ Unggi Lee 2026](#unggi-lee-2026)

## Evidence

### Unggi Lee 2026

Unggi Lee, Minchul Shin, Yeil Jeong, Sookbun Lee, Jeongsu Moon, Kyungtae Joo, Eunjoo Lee, Hoilym Kwon. (2026). LLMs Are Already Good Tutors: Training-Free Prompt Optimization for Pedagogical Math Tutoring. arXiv preprint. [doi:10.48550/arXiv.2605.27088](https://doi.org/10.48550/arXiv.2605.27088)

`q2 · i0` · `causal · r2`

Generalization analysis (§4.1, Figure 4 left): correlation of in-domain Rtotal with OOD benchmark averages across the 12 methods. The printed ρ = 0.01 is a negligible effect size. Striking dissociations include ACE ranking 12th in-domain but 2nd on MTB.

> "Figure 4 reveals essentially no correlation between in-domain Rtotal and OOD MathTutorBench-Avg across the 12 listed methods (ρ= 0.01 , p= 0.96 )"

## Discussion


## Related Claims
- [All pretrained transformer models showed a significant performance drop of about 20% between IID and OOD data, and OOD performance correlated linearly with IID performance](pretrained-transformers-twenty-percent-ood-drop.md) — reports the opposite
- [Dialogue-based RL training on mathematics tutoring dialogues generalizes to unseen educational benchmarks while largely preserving factual knowledge](dialogue-rl-out-of-distribution-generalization.md) — related
- [Reasoning-mode effects are task-dependent: thinking improves MathTutorBench but degrades OpenLearnLM and sharply degrades in-domain leak control, across both training-free and RL paradigms](task-dependent-reasoning-mode-effect-tutoring.md) — related
