---
type: claim
title: CSG-KT significantly outperforms classical, graph-based and SOTA knowledge tracing baselines across four real-world datasets
description: CSG-KT significantly outperforms classical, graph-based and SOTA knowledge tracing baselines across four real-world datasets
id: csg-kt-outperforms-kt-baselines
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: hengnian-gu-2025
    resource: "https://doi.org/10.48550/arXiv.2508.12647"
    title: "Hengnian Gu, Zhifu Chen, Yuxin Chen, Jin Peng Zhou, and Dongdai Zhou. (2025). Cognitive Structure Generation: From Educational Priors to Policy Optimization. arXiv preprint. [doi:10.48550/arXiv.2508.12647](https://doi.org/10.48550/arXiv.2508.12647)"
    author: Hengnian Gu, Zhifu Chen, Yuxin Chen, Jin Peng Zhou, and Dongdai Zhou
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# CSG-KT significantly outperforms classical, graph-based and SOTA knowledge tracing baselines across four real-world datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` CSG-KT significantly outperforms classical KT models, graph-based baselines modeling only concept construction, and recent SOTA methods on Math1, Math2, FrcSub and NIPS34. [→ Hengnian Gu 2025](#hengnian-gu-2025)

## Evidence

### Hengnian Gu 2025

Hengnian Gu, Zhifu Chen, Yuxin Chen, Jin Peng Zhou, and Dongdai Zhou. (2025). Cognitive Structure Generation: From Educational Priors to Policy Optimization. arXiv preprint. [doi:10.48550/arXiv.2508.12647](https://doi.org/10.48550/arXiv.2508.12647)

`q2 · i?` · `design · r2`

Five-fold cross-validated comparison on four public datasets (Math1, Math2, FrcSub, NIPS34) reported in Table 1; CSG-KT reaches AUC 0.8192 on Math1 versus 0.8103 for ENAS-KT, with Wilcoxon rank-sum significance markers. The authors state CSG-KT "even surpasses recent SOTA methods".

> "CSG-KT not only significantly outperforms classical knowledge tracing models (e.g., DKT, SAKT) but also yields clear improvements over graph-based baselines that model only concept construction without capturing inter-concept relations (e.g., GKT, SKT, GRKT), and even surpasses recent SOTA methods (e.g., GRKT, MIKT, ENAS-KT)."

## Discussion


## Related Claims
- [CSG-CD significantly outperforms classical, neural and graph-based cognitive diagnosis baselines across four datasets](csg-cd-outperforms-cd-baselines.md) — related
- [GRATE outperforms state-of-the-art knowledge tracing baselines in student performance prediction on three real-world datasets](grate-outperforms-kt-baselines-performance-prediction.md) — related
- [TSDR improves the AUC of six state-of-the-art KT backbones across nine real-world benchmark datasets](tsdr-improves-kt-backbone-auc-benchmarks.md) — related
- [LT-MKT achieves the best performance across all four datasets and all three evaluation metrics against eleven KT baselines](lt-mkt-outperforms-kt-baselines-four-datasets.md) — related
- [Under controlled synthetic MNAR bias, TSDR-equipped models improve across the entire bias spectrum, with the RMSE advantage diminishing beyond gamma > 0.8](tsdr-robust-across-mnar-spectrum.md) — related
- [Existing KT methods fail to beat a majority-class baseline on the small CoMTA dialogue dataset but perform significantly better on the larger MathDial dataset.](existing-kt-methods-fail-on-small-comta-but-improve-with-more-data-on-mathdial.md) — related
- [CogEvolution performs comparably to the KT-based PEERS model on mastery prediction (AUC 0.80 vs 0.82) while achieving higher mistake precision (76.8%) on CogMath-948](cogevolution-mistake-precision-beats-kt-baseline.md) — related
- [AKT outperforms existing knowledge tracing methods on benchmark datasets in predicting future learner responses](akt-outperforms-kt-baselines-auc-benchmarks.md) — related
- [Rule-based simulated cognitive structures alone nearly match or slightly surpass classical KT and CD baselines](rule-based-simulation-matches-classical-baselines.md) — related
- [Cross-skill effects exist in knowledge tracing: mastery of a target skill depends on previous interactions with other, related skills, not only the same skill](cross-skill-effects-in-knowledge-tracing.md) — related
