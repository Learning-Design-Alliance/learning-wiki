---
type: claim
title: "Most student project reports exceed the BART model's 1024-token input limit, motivating a select-then-generate design because truncation can lose critical information"
description: "Most student project reports exceed the BART model's 1024-token input limit, motivating a select-then-generate design because truncation can lose critical information"
id: project-reports-exceed-bart-token-limit
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: qinjin-jia-2022
    resource: "https://github.com/qinjinjia/JEDM22_Automated_Feedback_Generation"
    title: "Qinjin Jia, Mitchell Young, Yunkai Xiao, Jialin Cui, Chengyuan Liu, Parvez Rashid, Edward Gehringer. (2022). Automated Feedback Generation for Student Project Reports: A Data-Driven Approach. Journal of Educational Data Mining, Volume 14, No 3. https://github.com/qinjinjia/JEDM22_Automated_Feedback_Generation"
    author: Qinjin Jia, Mitchell Young, Yunkai Xiao, Jialin Cui, Chengyuan Liu, Parvez Rashid, Edward Gehringer
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: qinjin-jia-2022-2
    resource: "https://github.com/qinjinjia/JEDM22_Automated_Feedback_Generation"
    title: "Qinjin Jia, Mitchell Young, Yunkai Xiao, Jialin Cui, Chengyuan Liu, Parvez Rashid, Edward Gehringer. (2022). Automated Feedback Generation for Student Project Reports: A Data-Driven Approach. Journal of Educational Data Mining, Volume 14, No 3. https://github.com/qinjinjia/JEDM22_Automated_Feedback_Generation"
    author: Qinjin Jia, Mitchell Young, Yunkai Xiao, Jialin Cui, Chengyuan Liu, Parvez Rashid, Edward Gehringer
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Most student project reports exceed the BART model's 1024-token input limit, motivating a select-then-generate design because truncation can lose critical information

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q1`–`q2`

## Subclaims
`q2 i?` 75.8% of reports in the dataset contain more than 1024 tokens, and the longest report is approximately eight times longer than that limit. [→ Qinjin Jia 2022](#qinjin-jia-2022)
`q1 i?` Truncating reports by discarding tokens beyond the limit can cause loss of critical information from the inputs. [→ Qinjin Jia 2022 (2)](#qinjin-jia-2022-2)

## Evidence

### Qinjin Jia 2022

Qinjin Jia, Mitchell Young, Yunkai Xiao, Jialin Cui, Chengyuan Liu, Parvez Rashid, Edward Gehringer. (2022). Automated Feedback Generation for Student Project Reports: A Data-Driven Approach. Journal of Educational Data Mining, Volume 14, No 3. https://github.com/qinjinjia/JEDM22_Automated_Feedback_Generation

`q2 · i?` · `design · r2`

Dataset statistics from twelve semesters of a graduate object-oriented course: the average original report has 1193 words (1643 subword tokens), and "75.8 % of the reports contain more than 1024 tokens". Descriptive statistics; no effect size.

> "75.8 % of the reports contain more than 1024 tokens, and the longest report is approximately eight times longer than that limit"

### Qinjin Jia 2022 (2)

Qinjin Jia, Mitchell Young, Yunkai Xiao, Jialin Cui, Chengyuan Liu, Parvez Rashid, Edward Gehringer. (2022). Automated Feedback Generation for Student Project Reports: A Data-Driven Approach. Journal of Educational Data Mining, Volume 14, No 3. https://github.com/qinjinjia/JEDM22_Automated_Feedback_Generation

`q1 · i?` · `design · r2`

Methodological rationale in Section 4.2: the authors reject simple truncation because "this can cause loss of critical information from the inputs", a hypothesis they state is verified in Section 10.1 (not included in the supplied text).

> "One simple fix is to truncate the report by discarding all tokens beyond the length limit, but this can cause loss of critical information from the inputs"

## Discussion


## Related Claims
-
