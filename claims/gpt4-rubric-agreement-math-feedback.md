---
type: claim
title: "GPT-4 achieves moderate-to-high agreement with human annotations when applying the five-aspect math feedback rubric, with 76% average label accuracy and a 0.56 average correlation of rubric scores."
description: "GPT-4 achieves moderate-to-high agreement with human annotations when applying the five-aspect math feedback rubric, with 76% average label accuracy and a 0.56 average correlation of rubric scores."
id: gpt4-rubric-agreement-math-feedback
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: alexander-scarlatos-2024
    resource: "https://doi.org/10.1007/978-3-031-64302-6_20"
    title: "Alexander Scarlatos, Digory Smith, Simon Woodhead, and Andrew Lan. (2024). Improving the Validity of Automatically Generated Feedback via Reinforcement Learning. Published in AIED 2024. [doi:10.1007/978-3-031-64302-6_20](https://doi.org/10.1007/978-3-031-64302-6_20)"
    author: Alexander Scarlatos, Digory Smith, Simon Woodhead, and Andrew Lan
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: alexander-scarlatos-2024-2
    resource: "https://doi.org/10.1007/978-3-031-64302-6_20"
    title: "Alexander Scarlatos, Digory Smith, Simon Woodhead, and Andrew Lan. (2024). Improving the Validity of Automatically Generated Feedback via Reinforcement Learning. Published in AIED 2024. [doi:10.1007/978-3-031-64302-6_20](https://doi.org/10.1007/978-3-031-64302-6_20)"
    author: Alexander Scarlatos, Digory Smith, Simon Woodhead, and Andrew Lan
    q: 2
    i: 3
    kind: design
    rigour: 2
---

# GPT-4 achieves moderate-to-high agreement with human annotations when applying the five-aspect math feedback rubric, with 76% average label accuracy and a 0.56 average correlation of rubric scores.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2` · `i3` large
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-4 generally agrees with human annotations, with an average accuracy of 76% across rubric labels. [→ Alexander Scarlatos 2024](#alexander-scarlatos-2024)
`q2 i3` The Pearson correlation of GPT-4's final rubric scores with human annotations is 0.56 on average, versus 0.40 for ROUGE-L and BERTScore. [→ Alexander Scarlatos 2024 (2)](#alexander-scarlatos-2024-2)

## Evidence

### Alexander Scarlatos 2024

Alexander Scarlatos, Digory Smith, Simon Woodhead, and Andrew Lan. (2024). Improving the Validity of Automatically Generated Feedback via Reinforcement Learning. Published in AIED 2024. [doi:10.1007/978-3-031-64302-6_20](https://doi.org/10.1007/978-3-031-64302-6_20)

`q2 · i?` · `design · r2`

Agreement study in §4.4 on 80 randomly sampled feedback messages from the augmented test set, annotated manually and by a graduate student with extensive teaching experience, blinded to GPT-4's annotations and feedback provenance. The article reports "an aver age accuracy of 76% across labels"; no effect size is printed.

> "We observe that GPT-4 generally agrees with human annotations, with an aver age accuracy of 76% across labels."

### Alexander Scarlatos 2024 (2)

Alexander Scarlatos, Digory Smith, Simon Woodhead, and Andrew Lan. (2024). Improving the Validity of Automatically Generated Feedback via Reinforcement Learning. Published in AIED 2024. [doi:10.1007/978-3-031-64302-6_20](https://doi.org/10.1007/978-3-031-64302-6_20)

`q2 · i3` · `design · r2`

Same §4.4 agreement study; the article reports r = 0.56 between GPT-4 and human rubric scores, while ROUGE-L and BERTScore both have average correlations of 0.40 with human-annotated rubric scores and are biased upward.

> "We also compute the Pearson correlation c oeﬃcient of the ﬁnal rubric scores between GPT-4 and human annotations, res ulting in 0.56 on average, indicating moderate overall correlation."

## Discussion


## Related Claims
- [GPT models achieved high polarity agreement with instructors only for positive feedback on the Topic aspect, and could not reliably assess the other rubric aspects](gpt-polarity-agreement-low-except-topic.md) — reports the opposite
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
- [GPT-4o's final-turn correctness labeling on CoMTA is only slightly less accurate than expert human annotators, which the authors read as close to human-level performance on a challenging task.](gpt-4o-final-turn-correctness-labeling-is-close-to-human-level.md) — related
- [Expert former math teachers rated GPT-4o's dialogue annotations very highly for student correctness and moderate-to-high for knowledge components, with volatile inter-rater reliability.](expert-teachers-rate-gpt-4o-dialogue-annotations-as-largely-accurate.md) — related
