---
type: claim
title: Expert evaluation shows high recall and precision for SANN-identified logical errors across five problems
description: Expert evaluation shows high recall and precision for SANN-identified logical errors across five problems
id: sann-high-recall-precision-logical-errors
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: muntasir-hoq-2025
    resource: "https://doi.org/10.48550/arXiv.2505.10913"
    title: "Muntasir Hoq, Ananya Rao, Reisha Jaishankar, Krish Piryani, Nithya Janapati, Jessica Vandenberg, Bradford Mott, Narges Norouzi, James Lester, Bita Akram. (2025). Automated Identification of Logical Errors in Programs: Advancing Scalable Analysis of Student Misconceptions. arXiv preprint. [doi:10.48550/arXiv.2505.10913](https://doi.org/10.48550/arXiv.2505.10913)"
    author: Muntasir Hoq, Ananya Rao, Reisha Jaishankar, Krish Piryani, Nithya Janapati, Jessica Vandenberg, Bradford Mott, Narges Norouzi, James Lester, Bita Akram
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: muntasir-hoq-2025-2
    resource: "https://doi.org/10.48550/arXiv.2505.10913"
    title: "Muntasir Hoq, Ananya Rao, Reisha Jaishankar, Krish Piryani, Nithya Janapati, Jessica Vandenberg, Bradford Mott, Narges Norouzi, James Lester, Bita Akram. (2025). Automated Identification of Logical Errors in Programs: Advancing Scalable Analysis of Student Misconceptions. arXiv preprint. [doi:10.48550/arXiv.2505.10913](https://doi.org/10.48550/arXiv.2505.10913)"
    author: Muntasir Hoq, Ananya Rao, Reisha Jaishankar, Krish Piryani, Nithya Janapati, Jessica Vandenberg, Bradford Mott, Narges Norouzi, James Lester, Bita Akram
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Expert evaluation shows high recall and precision for SANN-identified logical errors across five problems

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For the caughtSpeeding problem, the framework identified 96% of expert-labeled logical errors with 90% precision, and identified all errors in a submission 86% of the time. [→ Muntasir Hoq 2025](#muntasir-hoq-2025)
`q2 i?` Across four additional problems, recall ranged from 83% to 97% and precision from 82% to 92%, with 100% recall for compilable syntactic errors in all problems. [→ Muntasir Hoq 2025 (2)](#muntasir-hoq-2025-2)

## Evidence

### Muntasir Hoq 2025

Muntasir Hoq, Ananya Rao, Reisha Jaishankar, Krish Piryani, Nithya Janapati, Jessica Vandenberg, Bradford Mott, Narges Norouzi, James Lester, Bita Akram. (2025). Automated Identification of Logical Errors in Programs: Advancing Scalable Analysis of Student Misconceptions. arXiv preprint. [doi:10.48550/arXiv.2505.10913](https://doi.org/10.48550/arXiv.2505.10913)

`q2 · i?` · `design · r2`

Expert evaluation of 957 incorrect caughtSpeeding submissions by two annotators (Cohen's kappa 0.94 in the second round). The framework's recall was 96%; precision was 90%; recall for identifying all errors in multi-error programs was 86% (average 2.6 errors per incorrect program).

> "Our framework identi- fied 96% of the logical errors from all the code (with an at- tention threshold of 20%)."

### Muntasir Hoq 2025 (2)

Muntasir Hoq, Ananya Rao, Reisha Jaishankar, Krish Piryani, Nithya Janapati, Jessica Vandenberg, Bradford Mott, Narges Norouzi, James Lester, Bita Akram. (2025). Automated Identification of Logical Errors in Programs: Advancing Scalable Analysis of Student Misconceptions. arXiv preprint. [doi:10.48550/arXiv.2505.10913](https://doi.org/10.48550/arXiv.2505.10913)

`q2 · i?` · `design · r2`

Robustness evaluation on 200 incorrect submissions each for redTicket, countCode, sum13, and canBalance covering loops, strings, and arrays. Recall per category included 100% syntactic, 85-98% strategic, and 76-96% conceptual; sum13 showed the lowest conceptual recall (76%).

> "As shown in Table 2, the framework achieved high recall across the problems, ranging from 83% to 97%. The precision of the model for the four new problems was calculated in the range of 82% to 92%."

## Discussion


## Related Claims
- [SANN code vectors outperform explainable baseline code2vec in logical error identification](sann-beats-code2vec-error-identification.md) — related
- [Modified SANN outperforms baseline models in predicting program correctness](sann-outperforms-baselines-correctness-prediction.md) — related
