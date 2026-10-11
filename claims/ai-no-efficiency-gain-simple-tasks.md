---
type: claim
title: AI assistance provides no significant overall time savings and can slow completion on easy task variants, with chat-interface friction (prompting time) dominating on trivial tasks
description: AI assistance provides no significant overall time savings and can slow completion on easy task variants, with chat-interface friction (prompting time) dominating on trivial tasks
id: ai-no-efficiency-gain-simple-tasks
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: sunny-yu-2026
    resource: "https://arxiv.org/abs/2605.22687"
    title: "Sunny Yu, Myra Cheng, Ahmad Jabbar, Ilia Sucholutsky, Katherine M. Collins, Dan Jurafsky, Robert D. Hawkins. (2026). The efficiency-gain illusion: People underestimate the rate of AI use and overestimate its benefits on simple tasks. arXiv. https://arxiv.org/abs/2605.22687"
    author: Sunny Yu, Myra Cheng, Ahmad Jabbar, Ilia Sucholutsky, Katherine M. Collins, Dan Jurafsky, Robert D. Hawkins
    q: 3
    i: "?"
    kind: causal
    rigour: 3
  - id: sunny-yu-2026-2
    resource: "https://arxiv.org/abs/2605.22687"
    title: "Sunny Yu, Myra Cheng, Ahmad Jabbar, Ilia Sucholutsky, Katherine M. Collins, Dan Jurafsky, Robert D. Hawkins. (2026). The efficiency-gain illusion: People underestimate the rate of AI use and overestimate its benefits on simple tasks. arXiv. https://arxiv.org/abs/2605.22687"
    author: Sunny Yu, Myra Cheng, Ahmad Jabbar, Ilia Sucholutsky, Katherine M. Collins, Dan Jurafsky, Robert D. Hawkins
    q: 3
    i: "?"
    kind: causal
    rigour: 3
---

# AI assistance provides no significant overall time savings and can slow completion on easy task variants, with chat-interface friction (prompting time) dominating on trivial tasks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r3` · `q3`

## Subclaims
`q3 i?` Across all tasks, AI assistance did not significantly reduce completion time, and on easy task variants AI-assisted completion was 10.0 seconds slower than independent completion. [→ Sunny Yu 2026](#sunny-yu-2026)
`q3 i?` In Study 1, AI users showed no time savings and reported higher mental effort than independent completers. [→ Sunny Yu 2026 (2)](#sunny-yu-2026-2)

## Evidence

### Sunny Yu 2026

Sunny Yu, Myra Cheng, Ahmad Jabbar, Ilia Sucholutsky, Katherine M. Collins, Dan Jurafsky, Robert D. Hawkins. (2026). The efficiency-gain illusion: People underestimate the rate of AI use and overestimate its benefits on simple tasks. arXiv. https://arxiv.org/abs/2605.22687

`q3 · i?` · `causal · r3`

Study 2 completion sample (N=1001) with hidden timers and GPT-4o chat interface. The article decomposes AI-assisted time into prompting, model response, and processing, finding "prompting (48.7 seconds) took significantly longer than response processing (37.6 seconds)".

> "Across all tasks, AI assistance did not significantly reduce completion time overall (β= 6.17,p= 0.07). A decomposition of the AI-assisted completion time reveals that this is because current chat-interface friction dominates on trivial tasks, leading to a slow-down effect where AI-assisted completion times is longer than the independent completion by 10.0 seconds on easy task variants (from 60.2 seconds for independent to 70.2 seconds for AI-assisted;p <0.05)."

### Sunny Yu 2026 (2)

Sunny Yu, Myra Cheng, Ahmad Jabbar, Ilia Sucholutsky, Katherine M. Collins, Dan Jurafsky, Robert D. Hawkins. (2026). The efficiency-gain illusion: People underestimate the rate of AI use and overestimate its benefits on simple tasks. arXiv. https://arxiv.org/abs/2605.22687

`q3 · i?` · `causal · r3`

Study 1 (N=498) recorded hidden-timer completion times and NASA-TLX effort per task. The article reports no significant time difference and higher effort for AI-assisted completion; Study 3 replicated that AI users spent 7.06 seconds more.

> "for time, there is no significant difference (β=−5.6,p= 0.10); for effort, people who completed tasks independently actually reported lower mental effort (1.99 for independent vs. 2.11 for AI-assisted on a 7-point scale) than those who used AI (β=−0.12,p<0.01)."

## Discussion


## Learner Variables
- [Time and Continuity](../learner-variables/time-and-continuity.md) — outcome: instruction changes it

## Related Claims
- [People significantly underestimate AI-assisted completion times even though actual AI-assisted and independent completion times do not differ (the speedup illusion)](speedup-illusion-ai-assisted-time-underestimation.md) — related
- [AI assistance sped up only difficult tasks and only a few individual tasks, not easy ones](ai-speedup-limited-to-difficult-tasks.md) — related
- [People overestimate how much time AI assistance saves (speedup illusion), driven by miscalibration about AI-assisted completion time while independent completion time is well calibrated](speedup-illusion-ai-time-savings.md) — related
- [Prior AI use carries over: brief AI exposure increases subsequent AI adoption and exacerbates the speedup illusion, while independent exposure does not reduce AI use](ai-exposure-carryover-effect.md) — related
- [AI assistance reduces subjective mental effort across all tasks even when it does not reduce completion time, dissociating time and effort](ai-effort-reduction-time-effort-dissociation.md) — related
- [Chat-log analysis indicates lower-education participants obtain substantial assistance from AI while higher-education participants use the tool somewhat more effectively across several margins, explaining why the gap narrows but does not disappear](chat-logs-explain-gap-narrows-but-persists.md) — related
