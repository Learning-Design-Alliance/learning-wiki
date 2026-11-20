---
type: claim
title: "Human teachers' preferences for LM-generated worksheets correlate significantly with evaluator LM judgments (r = 0.661), but teachers sometimes cannot distinguish worksheets the LM perceives as different"
description: "Human teachers' preferences for LM-generated worksheets correlate significantly with evaluator LM judgments (r = 0.661), but teachers sometimes cannot distinguish worksheets the LM perceives as different"
id: lm-judgments-align-with-teacher-preferences
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: joy-he-yueya-2024
    resource: "https://doi.org/10.48550/arXiv.2403.02795"
    title: "Joy He-Yueya, Noah D. Goodman, Emma Brunskill. (2024). Evaluating and Optimizing Educational Content with Large Language Model Judgments. arXiv preprint. [doi:10.48550/arXiv.2403.02795](https://doi.org/10.48550/arXiv.2403.02795)"
    author: Joy He-Yueya, Noah D. Goodman, Emma Brunskill
    q: 3
    i: 3
    kind: design
    rigour: 2
  - id: joy-he-yueya-2024-2
    resource: "https://doi.org/10.48550/arXiv.2403.02795"
    title: "Joy He-Yueya, Noah D. Goodman, Emma Brunskill. (2024). Evaluating and Optimizing Educational Content with Large Language Model Judgments. arXiv preprint. [doi:10.48550/arXiv.2403.02795](https://doi.org/10.48550/arXiv.2403.02795)"
    author: Joy He-Yueya, Noah D. Goodman, Emma Brunskill
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# Human teachers' preferences for LM-generated worksheets correlate significantly with evaluator LM judgments (r = 0.661), but teachers sometimes cannot distinguish worksheets the LM perceives as different

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q3` · `i3` large
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q3 i3` Pearson correlation between LM-predicted post-test scores and human teacher preference scores across 10 worksheets is significant (r = 0.661, p < 0.05). [→ Joy He-Yueya 2024](#joy-he-yueya-2024)
`q3 i?` Human teachers sometimes cannot distinguish worksheets that LMs identify as distinct, particularly those with predicted post-test scores ranging from 60 to 90. [→ Joy He-Yueya 2024 (2)](#joy-he-yueya-2024-2)

## Evidence

### Joy He-Yueya 2024

Joy He-Yueya, Noah D. Goodman, Emma Brunskill. (2024). Evaluating and Optimizing Educational Content with Large Language Model Judgments. arXiv preprint. [doi:10.48550/arXiv.2403.02795](https://doi.org/10.48550/arXiv.2403.02795)

`q3 · i3` · `design · r2`

Human teacher evaluation on Prolific: 465 ratings from 95 participants, reduced to 270 ratings from 56 participants after catch-trial filtering; pairwise slider comparisons of 10 worksheets (45 unique pairs). Figure 11 shows the correlation with bootstrapped 95% confidence intervals.

> "We calculate the Pearson correlation between post-test scores predicted by the LM and the human preference scores for all worksheets and find a significant correlation ( r = 0.661, p < 0.05) between the LM judgments and human teacher preferences"

### Joy He-Yueya 2024 (2)

Joy He-Yueya, Noah D. Goodman, Emma Brunskill. (2024). Evaluating and Optimizing Educational Content with Large Language Model Judgments. arXiv preprint. [doi:10.48550/arXiv.2403.02795](https://doi.org/10.48550/arXiv.2403.02795)

`q3 · i?` · `design · r2`

Reported in the same human evaluation section as a divergence between LM and human judgments, raising concerns the authors note about the models' decision-making processes and potential training-data biases.

> "However, human teachers sometimes cannot distinguish worksheets that LMs identify as distinct, particularly those with predicted post-test scores ranging from 60 to 90."

## Discussion


## Related Claims
- [An optimizer LM can iteratively improve math word problem worksheets using an evaluator LM's judgments as the reward function](instruction-optimization-improves-worksheets.md) — related
- [LLM-as-a-Judge scores correlate with blinded human expert judgments, more strongly for Medical Narrative Generation than Story Direction](llm-judge-correlates-human-experts-medgame.md) — related
- [Human raters' preferences align with the LLM judge on TutorBench (Pearson r = 0.82 across metric-level win rates)](human-llm-judge-preference-alignment-deeptutor.md) — related
- [Automated metrics and LLM judges can misalign with expert human preferences in non-verifiable educational evaluation](non-verifiability-crisis-llm-judges-misalign.md) — related
