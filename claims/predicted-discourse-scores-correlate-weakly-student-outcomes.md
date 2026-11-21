---
type: claim
title: Model-predicted discourse scores show weak but partially human-aligned correlations with student outcomes, including a positive link between Explanations and achievement
description: Model-predicted discourse scores show weak but partially human-aligned correlations with student outcomes, including a positive link between Explanations and achievement
id: predicted-discourse-scores-correlate-weakly-student-outcomes
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: ruikun-hou-2025
    resource: "https://doi.org/10.48550/arXiv.2505.07902"
    title: "Ruikun Hou, Babette Bühler, Tim Fütterer, Efe Bozkir, Peter Gerjets, Ulrich Trautwein, and Enkelejda Kasneci. (2025). Multimodal Assessment of Classroom Discourse Quality: A Text-Centered Attention-Based Multi-Task Learning Approach. arXiv preprint. [doi:10.48550/arXiv.2505.07902](https://doi.org/10.48550/arXiv.2505.07902)"
    author: Ruikun Hou, Babette Bühler, Tim Fütterer, Efe Bozkir, Peter Gerjets, Ulrich Trautwein, and Enkelejda Kasneci
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: ruikun-hou-2025-2
    resource: "https://doi.org/10.48550/arXiv.2505.07902"
    title: "Ruikun Hou, Babette Bühler, Tim Fütterer, Efe Bozkir, Peter Gerjets, Ulrich Trautwein, and Enkelejda Kasneci. (2025). Multimodal Assessment of Classroom Discourse Quality: A Text-Centered Attention-Based Multi-Task Learning Approach. arXiv preprint. [doi:10.48550/arXiv.2505.07902](https://doi.org/10.48550/arXiv.2505.07902)"
    author: Ruikun Hou, Babette Bühler, Tim Fütterer, Efe Bozkir, Peter Gerjets, Ulrich Trautwein, and Enkelejda Kasneci
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Model-predicted discourse scores show weak but partially human-aligned correlations with student outcomes, including a positive link between Explanations and achievement

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Human-rated Explanations correlated positively with student interest, while text-only and text-audio predictions correlated positively with test achievement and self-efficacy. [→ Ruikun Hou 2025](#ruikun-hou-2025)
`q3 i?` Overall associations between discourse quality scores and student outcomes were weak, though automated scores partially replicated patterns from human ratings. [→ Ruikun Hou 2025 (2)](#ruikun-hou-2025-2)

## Evidence

### Ruikun Hou 2025

Ruikun Hou, Babette Bühler, Tim Fütterer, Efe Bozkir, Peter Gerjets, Ulrich Trautwein, and Enkelejda Kasneci. (2025). Multimodal Assessment of Classroom Discourse Quality: A Text-Centered Attention-Based Multi-Task Learning Approach. arXiv preprint. [doi:10.48550/arXiv.2505.07902](https://doi.org/10.48550/arXiv.2505.07902)

`q2 · i?` · `design · r2`

Pearson correlation analysis (§5.3, Table 5) of classroom-level discourse scores against post-instruction test scores, interest, and self-efficacy (N = 958 printed in the table note). Table 5 prints specific coefficients (e.g., T+A Explanations–test scores .083*, p <0.05).

> "Regarding Explanations, human ratings showed a statistically significantly positive correlation with student interest, while two models' predictions (text-only and text-audio) were positively related to student test achievements and self-efficacy."

### Ruikun Hou 2025 (2)

Ruikun Hou, Babette Bühler, Tim Fütterer, Efe Bozkir, Peter Gerjets, Ulrich Trautwein, and Enkelejda Kasneci. (2025). Multimodal Assessment of Classroom Discourse Quality: A Text-Centered Attention-Based Multi-Task Learning Approach. arXiv preprint. [doi:10.48550/arXiv.2505.07902](https://doi.org/10.48550/arXiv.2505.07902)

`q2 · i?` · `design · r2`

Authors' summary of the correlation analysis in §5.3, based on teacher-level averaged scores collected after instruction in the GTI Germany data. The authors state they "generally found weak associations between discourse quality scores and student outcomes"; no standardized effect sizes are reported in the quoted prose.

> "Overall, although we generally found weak associations between discourse quality scores and student outcomes, the correlation analysis suggested the promise of our automated methods as a valuable proxy to replicate those findings based on human ratings in large-scale classroom observation studies."

## Discussion


## Learner Variables
- [Communication Skills](../learner-variables/communication-skills.md) — predictor: learners who differ on it differ in outcomes

## Related Claims
- [Positive motivational assessments of introductory activities correlate weakly with learning outcomes on near-in-time tests but not with distant exam results](motivational-assessments-correlate-weakly-near-tests.md) — related
- [SHAP and LLM explanation methods show consistently low alignment, with mean top-10 Jaccard similarity of 0.085](low-alignment-shap-llm-sentence-selection.md) — related
- [Text-audio fusion yields the best discourse-quality prediction (average QWK 0.384), exceeding human inter-rater reliability of 0.326 on the GTI Germany dataset](text-audio-fusion-qwk-0-384-exceeds-human-irr.md) — related
