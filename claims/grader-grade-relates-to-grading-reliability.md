---
type: claim
title: Higher-scoring students tend to be more reliable graders (except the very best), and students are least biased when grading peers with similar scores
description: Higher-scoring students tend to be more reliable graders (except the very best), and students are least biased when grading peers with similar scores
id: grader-grade-relates-to-grading-reliability
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-16
evidence_strength: moderate
sources:
  - id: chris-piech-2013
    resource: "https://arxiv.org/abs/1307.2579"
    title: "Chris Piech, Jonathan Huang, Zhenghao Chen, Chuong Do, Andrew Ng, Daphne Koller. (2013). Tuned Models of Peer Assessment in MOOCs. arXiv. https://arxiv.org/abs/1307.2579"
    author: Chris Piech, Jonathan Huang, Zhenghao Chen, Chuong Do, Andrew Ng, Daphne Koller
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: chris-piech-2013-2
    resource: "https://arxiv.org/abs/1307.2579"
    title: "Chris Piech, Jonathan Huang, Zhenghao Chen, Chuong Do, Andrew Ng, Daphne Koller. (2013). Tuned Models of Peer Assessment in MOOCs. arXiv. https://arxiv.org/abs/1307.2579"
    author: Chris Piech, Jonathan Huang, Zhenghao Chen, Chuong Do, Andrew Ng, Daphne Koller
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Higher-scoring students tend to be more reliable graders (except the very best), and students are least biased when grading peers with similar scores

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`

## Subclaims
`q2 i?` Graders that score higher on assignments have close to monotonically decreasing biases, but students with the best grades (+1.75 z-score) are not as accurate as students who do very well (+0.75 z-score, p = 0.04). [→ Chris Piech 2013](#chris-piech-2013)
`q2 i?` Students are least biased when grading peers with similar scores; the best students significantly downgrade the worst submissions and the worst students notably inflate the best submissions. [→ Chris Piech 2013 (2)](#chris-piech-2013-2)

## Evidence

### Chris Piech 2013

Chris Piech, Jonathan Huang, Zhenghao Chen, Chuong Do, Andrew Ng, Daphne Koller. (2013). Tuned Models of Peer Assessment in MOOCs. arXiv. https://arxiv.org/abs/1307.2579

`q2 · i?` · `associational · r2`

Observational analysis of grader latent variables in the HCI datasets (Figure 2a), relating grader grade to grading residual statistics. The article reports higher-scoring students are more reliable graders, with the exception that +1.75 z-score students are less accurate than +0.75 z-score students (p = 0.04).

> "Graders that score higher on assignments have close to monotonically decreasing biases (Figure 2(a)). Getting a better grade on the homework in general makes students more reliable graders; with the notable exception that the students that get the best grades (+1.75 z-score) are not as accurate as the students who do very well (+.75 z-score,p = 0.04)."

### Chris Piech 2013 (2)

Chris Piech, Jonathan Huang, Zhenghao Chen, Chuong Do, Andrew Ng, Daphne Koller. (2013). Tuned Models of Peer Assessment in MOOCs. arXiv. https://arxiv.org/abs/1307.2579

`q2 · i?` · `associational · r2`

Observational analysis of grading residuals against gradee grade (Figure 2c) in the HCI datasets. The article reports least bias when grader and gradee have similar scores, with best students downgrading worst submissions and worst students inflating best submissions.

> "Finally, our results show that students are least biased when grading peers with similar score (Figure 2(c)). The best students signiﬁcantly downgrade the worst submissions and the worst students notably inﬂate the best submissions."

## Discussion


## Related Claims
- [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](llm-grading-mixed-against-human-raters.md) — related
- [Grading time shows a sweet spot: students grading around 20 minutes (time z-score near -0.25) have significantly lower residual standard deviations than slow graders, while snap graders are unreliable and inflate grades](grading-time-sweet-spot-twenty-minutes.md) — related
