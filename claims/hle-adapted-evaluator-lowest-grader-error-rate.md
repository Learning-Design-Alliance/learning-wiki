---
type: claim
title: "The HLE-adapted evaluator shows the lowest grader error rate (4.08%) among the evaluators audited"
description: "The HLE-adapted evaluator shows the lowest grader error rate (4.08%) among the evaluators audited"
id: hle-adapted-evaluator-lowest-grader-error-rate
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: ali-ansari-2026
    resource: "https://arxiv.org/abs/2609.13009"
    title: "Ali Ansari, Haoran Sun, Andy Zeyi Liu, Mark Jabbour, Yongshan Ding, Steven Girvin, Yu He, Sohrab Ismail-Beigi, Aleksander Kubica, Owen D. Miller, Corey O'Hern, Vidvuds Ozolins, David Poland, A. Douglas Stone, Frank C. van den Bosch, Logan Wright, Navid Akbari, Santanu Antu, Kangle Cai, Andrew Calabrese-Day, Mateo Cárdenes Wuttig, Meng Cheng, Barry T. Chiang, Ali Ghorashi, Shouzhen Gu, Haoyang Huang, Zhibo Kang, Lukas Kienesberger, Hantian Liu, Charles Lomba, Zhongling Lu, Wenchao Ma, Rohin E. McIntosh, Evan McKinney, Ivan Rojkov, Xulei Sun, Yarone Meir Tokayer, Naveen Balaji Umasankar, Mira Varma, Leda Wang, Qimin Wang, Tyler Wang, Haoyu Wei, Jinming Yang, Jinchen Zhao, Sherlock Tingrui Zhao, Qinyuan Zheng, Jay S. Zou, Lucas Baker, Arman Cohan, John Sous. (2026). How Good Are Frontier Models at Physics? Expert Re-Grading Reveals Broken Evaluations and Near-Saturation of Leading Benchmarks. https://arxiv.org/abs/2609.13009"
    author: "Ali Ansari, Haoran Sun, Andy Zeyi Liu, Mark Jabbour, Yongshan Ding, Steven Girvin, Yu He, Sohrab Ismail-Beigi, Aleksander Kubica, Owen D. Miller, Corey O'Hern, Vidvuds Ozolins, David Poland, A. Douglas Stone, Frank C. van den Bosch, Logan Wright, Navid Akbari, Santanu Antu, Kangle Cai, Andrew Calabrese-Day, Mateo Cárdenes Wuttig, Meng Cheng, Barry T. Chiang, Ali Ghorashi, Shouzhen Gu, Haoyang Huang, Zhibo Kang, Lukas Kienesberger, Hantian Liu, Charles Lomba, Zhongling Lu, Wenchao Ma, Rohin E. McIntosh, Evan McKinney, Ivan Rojkov, Xulei Sun, Yarone Meir Tokayer, Naveen Balaji Umasankar, Mira Varma, Leda Wang, Qimin Wang, Tyler Wang, Haoyu Wei, Jinming Yang, Jinchen Zhao, Sherlock Tingrui Zhao, Qinyuan Zheng, Jay S. Zou, Lucas Baker, Arman Cohan, John Sous"
    q: 2
    i: "?"
    kind: associational
    rigour: "?"
---

# The HLE-adapted evaluator shows the lowest grader error rate (4.08%) among the evaluators audited

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r?` · `q2`

## Subclaims
`q2 i?` Among the evaluators the authors audited, the HLE-adapted evaluator had the lowest grader error rate, at 4.08%. [→ Ali Ansari 2026](#ali-ansari-2026)

## Evidence

### Ali Ansari 2026

Ali Ansari, Haoran Sun, Andy Zeyi Liu, Mark Jabbour, Yongshan Ding, Steven Girvin, Yu He, Sohrab Ismail-Beigi, Aleksander Kubica, Owen D. Miller, Corey O'Hern, Vidvuds Ozolins, David Poland, A. Douglas Stone, Frank C. van den Bosch, Logan Wright, Navid Akbari, Santanu Antu, Kangle Cai, Andrew Calabrese-Day, Mateo Cárdenes Wuttig, Meng Cheng, Barry T. Chiang, Ali Ghorashi, Shouzhen Gu, Haoyang Huang, Zhibo Kang, Lukas Kienesberger, Hantian Liu, Charles Lomba, Zhongling Lu, Wenchao Ma, Rohin E. McIntosh, Evan McKinney, Ivan Rojkov, Xulei Sun, Yarone Meir Tokayer, Naveen Balaji Umasankar, Mira Varma, Leda Wang, Qimin Wang, Tyler Wang, Haoyu Wei, Jinming Yang, Jinchen Zhao, Sherlock Tingrui Zhao, Qinyuan Zheng, Jay S. Zou, Lucas Baker, Arman Cohan, John Sous. (2026). How Good Are Frontier Models at Physics? Expert Re-Grading Reveals Broken Evaluations and Near-Saturation of Leading Benchmarks. https://arxiv.org/abs/2609.13009

`q2 · i?` · `associational · r?`

Comparison of grader error rates across evaluators encountered during the expert audit, motivating adoption of the HLE-adapted pipeline for all corrected evaluations. The article prints the rate as "(4.08%)"; no effect size is reported.

> "All corrected evaluations use a common pipeline adapted from HLE, with its system prompt for response generation and its judge prompt for grading (Center for AI Safety et al., 2026). In our audit, this evaluator has the lowest grader error rate of all the evaluators we audited (4.08%)."

## Discussion


## Related Claims
- [Expert audit attributes 95.20% of audited benchmark rejections to benchmark or grader errors rather than model errors](expert-audit-most-physics-benchmark-rejections-are-benchmark-or-grader-errors.md) — related
- [Grader errors dominate audited rejections on benchmarks using rule-based evaluators (PHYBench and PRISM-Physics)](grader-errors-dominate-rule-based-evaluator-benchmarks.md) — related
- [After expert correction of benchmark materials, GPT-5.6-Sol's measured accuracy rises substantially on HLE-Physics, CMT-Benchmark, and CritPt](corrected-benchmark-scores-rise-substantially-after-expert-audit.md) — related
