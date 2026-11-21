---
type: claim
title: A SANN model pretrained on FalconCode and fine-tuned on LLM-generated synthetic code outperformed synthetic-only, pretrained-only, and GPT-4o baselines at predicting correctness on an unseen problem
description: A SANN model pretrained on FalconCode and fine-tuned on LLM-generated synthetic code outperformed synthetic-only, pretrained-only, and GPT-4o baselines at predicting correctness on an unseen problem
id: fine-tuned-sann-outperforms-baselines-unseen-problem
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: muntasir-hoq-2026
    resource: "https://doi.org/10.1007/978-3-032-29744-0_13"
    title: "Muntasir Hoq, Griffin Pitts, Bradford Mott, Seung Lee, Jessica Vandenberg, Shuyin Jiao, Narges Norouzi, James Lester, and Bita Akram. (2026). An Explainable AI Assistant for Introductory Programming Education: Improving Feedback Reliability with Instructor-AI Collaboration. arXiv. [doi:10.1007/978-3-032-29744-0_13](https://doi.org/10.1007/978-3-032-29744-0_13)"
    author: Muntasir Hoq, Griffin Pitts, Bradford Mott, Seung Lee, Jessica Vandenberg, Shuyin Jiao, Narges Norouzi, James Lester, and Bita Akram
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A SANN model pretrained on FalconCode and fine-tuned on LLM-generated synthetic code outperformed synthetic-only, pretrained-only, and GPT-4o baselines at predicting correctness on an unseen problem

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On an unseen conditionals problem, the fine-tuned SANN significantly outperformed synthetic-only SANN, pretrained SANN, and GPT-4o on accuracy, precision, recall, and F1-score (Wilcoxon signed rank test p-value < 0.05). [→ Muntasir Hoq 2026](#muntasir-hoq-2026)

## Evidence

### Muntasir Hoq 2026

Muntasir Hoq, Griffin Pitts, Bradford Mott, Seung Lee, Jessica Vandenberg, Shuyin Jiao, Narges Norouzi, James Lester, and Bita Akram. (2026). An Explainable AI Assistant for Introductory Programming Education: Improving Feedback Reliability with Instructor-AI Collaboration. arXiv. [doi:10.1007/978-3-032-29744-0_13](https://doi.org/10.1007/978-3-032-29744-0_13)

`q2 · i?` · `design · r2`

Offline evaluation on 548 real student submissions (168 correct, 380 incorrect) for an unseen conditionals problem, comparing fine-tuned SANN against three baselines. Table 1 reports fine-tuned SANN accuracy 0.89 and F1-score 0.86 versus GPT-4o accuracy 0.86, F1 0.83; the paper reports the comparison as "outperformed all the baselines significantly".

> "the fine-tuned SANN outperformed all the baselines significantly (p-value<0.05 using Wilcoxon signed rank test) across accuracy, precision, recall, and F1-score"

## Discussion


## Related Claims
- [SANN code vectors outperform explainable baseline code2vec in logical error identification](sann-beats-code2vec-error-identification.md) — related
- [Modified SANN outperforms baseline models in predicting program correctness](sann-outperforms-baselines-correctness-prediction.md) — related
