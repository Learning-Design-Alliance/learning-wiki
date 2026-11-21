---
type: strategy
id: conversational-traces-early-warning-signals
title: Use conversational traces as signals for identifying students who may need additional support
description: "The article suggests that \"conversational traces can serve as useful signals for identifying students who may need additional support or different scaffolds.\" The persistence of associations after controlling for prio..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: chen-2026
    resource: "https://arxiv.org/abs/2602.18807"
    title: "Chen, E., Judicke, S., Beigh, K., Tang, X., Wang, Y., Yuan, M., Xiao, Z., Li, C., Li, S., Luttmer, R., Singh, S., Yampolsky, M., Parikh, N., Zhao, Y., Chen, M., Huang, C., Mohanty, A., Johnson, G., Mackey, J., Lin, J., & Koedinger, K. (2026). Chat-Based Support Alone May Not Be Enough: Comparing Conversational and Embedded LLM Feedback for Mathematical Proof Learning. arXiv. https://arxiv.org/abs/2602.18807"
    author: "Chen, E., Judicke, S., Beigh, K., Tang, X., Wang, Y., Yuan, M., Xiao, Z., Li, C., Li, S., Luttmer, R., Singh, S., Yampolsky, M., Parikh, N., Zhao, Y., Chen, M., Huang, C., Mohanty, A., Johnson, G., Mackey, J., Lin, J., & Koedinger, K"
---

# Use conversational traces as signals for identifying students who may need additional support

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 causal), `q3` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
The article suggests that "conversational traces can serve as useful signals for identifying students who may need additional support or different scaffolds." The persistence of associations after controlling for prior performance makes chatbot usage frequency a practical indicator of students at risk, enabling instructors or systems to intervene with additional support.

## Design Implications

### Context
#### Requirements
- System interaction logs must record chatbot usage frequency, aggregated by exam intervals to align reliance with subsequent assessments
#### Constraints
- The article cautions these are associative findings, not evidence that chatbot use causes lower scores

### Target Learners
- undergraduate students in discrete mathematics

### Target Learning Goals
- identifying students who may need additional support or different scaffolds

## Claims

- [Chatbot usage constituted a negative associative pathway to subsequent exam performance, while proof-review usage showed no detectable independent association](../claims/chatbot-usage-negative-pathway-exam.md) [~W]
- [Students with lower Midterm 2 scores used both GPTutor tools more frequently during the subsequent interval](../claims/lower-prior-performance-higher-tool-usage.md) [+W]

## Related Strategies

- [Use a cohort-wide instructor dashboard of topic-level question volume, with assistant-surfaced prerequisite review suggestions as an extension](instructor-dashboard-topic-question-volume.md)
- [Use early-session timing signals, interpreted relative to proficiency, to identify students needing adaptive support](early-session-timing-signals-target-adaptive-support.md)

## Examples
-

## Key Sources
- Chen, E., Judicke, S., Beigh, K., Tang, X., Wang, Y., Yuan, M., Xiao, Z., Li, C., Li, S., Luttmer, R., Singh, S., Yampolsky, M., Parikh, N., Zhao, Y., Chen, M., Huang, C., Mohanty, A., Johnson, G., Mackey, J., Lin, J., & Koedinger, K. (2026). Chat-Based Support Alone May Not Be Enough: Comparing Conversational and Embedded LLM Feedback for Mathematical Proof Learning. arXiv. https://arxiv.org/abs/2602.18807
