---
type: claim
title: "Expert audit attributes 95.20% of audited benchmark rejections to benchmark or grader errors rather than model errors"
description: "Expert audit attributes 95.20% of audited benchmark rejections to benchmark or grader errors rather than model errors"
id: expert-audit-most-physics-benchmark-rejections-are-benchmark-or-grader-errors
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: ali-ansari-2026
    resource: "https://arxiv.org/abs/2609.13009"
    title: "Ali Ansari, Haoran Sun, Andy Zeyi Liu, Mark Jabbour, Yongshan Ding, Steven Girvin, Yu He, Sohrab Ismail-Beigi, Aleksander Kubica, Owen D. Miller, Corey O'Hern, Vidvuds Ozolins, David Poland, A. Douglas Stone, Frank C. van den Bosch, Logan Wright, Navid Akbari, Santanu Antu, Kangle Cai, Andrew Calabrese-Day, Mateo Cárdenes Wuttig, Meng Cheng, Barry T. Chiang, Ali Ghorashi, Shouzhen Gu, Haoyang Huang, Zhibo Kang, Lukas Kienesberger, Hantian Liu, Charles Lomba, Zhongling Lu, Wenchao Ma, Rohin E. McIntosh, Evan McKinney, Ivan Rojkov, Xulei Sun, Yarone Meir Tokayer, Naveen Balaji Umasankar, Mira Varma, Leda Wang, Qimin Wang, Tyler Wang, Haoyu Wei, Jinming Yang, Jinchen Zhao, Sherlock Tingrui Zhao, Qinyuan Zheng, Jay S. Zou, Lucas Baker, Arman Cohan, John Sous. (2026). How Good Are Frontier Models at Physics? Expert Re-Grading Reveals Broken Evaluations and Near-Saturation of Leading Benchmarks. https://arxiv.org/abs/2609.13009"
    author: "Ali Ansari, Haoran Sun, Andy Zeyi Liu, Mark Jabbour, Yongshan Ding, Steven Girvin, Yu He, Sohrab Ismail-Beigi, Aleksander Kubica, Owen D. Miller, Corey O'Hern, Vidvuds Ozolins, David Poland, A. Douglas Stone, Frank C. van den Bosch, Logan Wright, Navid Akbari, Santanu Antu, Kangle Cai, Andrew Calabrese-Day, Mateo Cárdenes Wuttig, Meng Cheng, Barry T. Chiang, Ali Ghorashi, Shouzhen Gu, Haoyang Huang, Zhibo Kang, Lukas Kienesberger, Hantian Liu, Charles Lomba, Zhongling Lu, Wenchao Ma, Rohin E. McIntosh, Evan McKinney, Ivan Rojkov, Xulei Sun, Yarone Meir Tokayer, Naveen Balaji Umasankar, Mira Varma, Leda Wang, Qimin Wang, Tyler Wang, Haoyu Wei, Jinming Yang, Jinchen Zhao, Sherlock Tingrui Zhao, Qinyuan Zheng, Jay S. Zou, Lucas Baker, Arman Cohan, John Sous"
    q: 2
    i: "?"
    kind: qualitative
    rigour: "?"
---

# Expert audit attributes 95.20% of audited benchmark rejections to benchmark or grader errors rather than model errors

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · qualitative `r?` · `q2`

## Subclaims
`q2 i?` Across four pooled audit sets, 238 of 250 audited rejections (95.20%) were benchmark or grader errors and only 12 (4.80%) were model errors. [→ Ali Ansari 2026](#ali-ansari-2026)

## Evidence

### Ali Ansari 2026

Ali Ansari, Haoran Sun, Andy Zeyi Liu, Mark Jabbour, Yongshan Ding, Steven Girvin, Yu He, Sohrab Ismail-Beigi, Aleksander Kubica, Owen D. Miller, Corey O'Hern, Vidvuds Ozolins, David Poland, A. Douglas Stone, Frank C. van den Bosch, Logan Wright, Navid Akbari, Santanu Antu, Kangle Cai, Andrew Calabrese-Day, Mateo Cárdenes Wuttig, Meng Cheng, Barry T. Chiang, Ali Ghorashi, Shouzhen Gu, Haoyang Huang, Zhibo Kang, Lukas Kienesberger, Hantian Liu, Charles Lomba, Zhongling Lu, Wenchao Ma, Rohin E. McIntosh, Evan McKinney, Ivan Rojkov, Xulei Sun, Yarone Meir Tokayer, Naveen Balaji Umasankar, Mira Varma, Leda Wang, Qimin Wang, Tyler Wang, Haoyu Wei, Jinming Yang, Jinchen Zhao, Sherlock Tingrui Zhao, Qinyuan Zheng, Jay S. Zou, Lucas Baker, Arman Cohan, John Sous. (2026). How Good Are Frontier Models at Physics? Expert Re-Grading Reveals Broken Evaluations and Near-Saturation of Leading Benchmarks. https://arxiv.org/abs/2609.13009

`q2 · i?` · `qualitative · r?`

Expert audit of 250 rejected answers across HLE-Physics, PHYBench, PRISM-Physics, and UGPhysics audit runs, with conflict resolution among auditors. The audit "143 (57.20%) are benchmark errors, 95 (38.00%) grader errors, and 12 (4.80%) model errors"; no effect size is printed.

> "The four audit runs of Appendix B.3 cover 502 questions: 252 accepted and 250 rejected and sent for review. After conflict resolution, 143 (57.20%) are benchmark errors, 95 (38.00%) grader errors, and 12 (4.80%) model errors."

## Discussion


## Related Claims
- [After expert correction of benchmark materials, GPT-5.6-Sol's measured accuracy rises substantially on HLE-Physics, CMT-Benchmark, and CritPt](corrected-benchmark-scores-rise-substantially-after-expert-audit.md) — a narrower finding that bears on this claim
- [Grader errors dominate audited rejections on benchmarks using rule-based evaluators (PHYBench and PRISM-Physics)](grader-errors-dominate-rule-based-evaluator-benchmarks.md) — related
- [The HLE-adapted evaluator shows the lowest grader error rate (4.08%) among the evaluators audited](hle-adapted-evaluator-lowest-grader-error-rate.md) — related
- [On public-source benchmark subsets, corrected scores for all three frontier models rise dramatically after excluding flawed questions](public-source-benchmark-corrected-scores-rise-dramatically.md) — related
