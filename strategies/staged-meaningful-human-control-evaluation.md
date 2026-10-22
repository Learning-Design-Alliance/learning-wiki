---
type: strategy
id: staged-meaningful-human-control-evaluation
title: Evaluate LLM data extraction through a staged meaningful-human-control sequence before integrating it into evidence synthesis
description: "The article proposes a three-stage evaluation sequence grounded in the construct of meaningful human control, in which \"human agents can meaningfully influence system behavior and be appropriately accountable for its..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-22
sources:
  - id: jansen-2026
    resource: "https://doi.org/10.1007/s10648-026-10136-5"
    title: "Jansen, T., Liebenow, L. W., Schaller, N.-J., Hattie, J., & Möller, J. (2026). Automated Data Extraction by Large Language Models: Assessing Accuracy in Comparison to Human Experts Using the Example of Visible Learning. Educational Psychology Review. https://doi.org/10.1007/s10648-026-10136-5"
    author: "Jansen, T., Liebenow, L. W., Schaller, N.-J., Hattie, J., & Möller, J"
---

# Evaluate LLM data extraction through a staged meaningful-human-control sequence before integrating it into evidence synthesis

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (6 for) · 1 study (1 design), `q3` · 0 of 1 report an effect size · 6 claims rest on one study

## Description
The article proposes a three-stage evaluation sequence grounded in the construct of meaningful human control, in which "human agents can meaningfully influence system behavior and be appropriately accountable for its outcomes". First, establish a baseline accuracy to assess predictability and basic viability; second, compare against expert human coders as the status quo; third, evaluate responsible integration patterns such as LLM as an independent second coder, LLM as a judge, or LLM as an assistant to a human coder, to balance speed and quality. The present study carries out the first two stages for educational SOMA data extraction.

## Design Implications

### Context
#### Requirements
- Evaluation studies must determine whether an AI performs adequately in the given context, as the RAISE working group requires
- LLM use must remain under meaningful human control, so researchers can identify errors and influence the output
#### Constraints
- The article states the current state of research satisfies only the first stage in some contexts, and comparisons against the status quo were missing before this study

### Target Learners
- Educational researchers conducting second-order meta-analyses and systematic reviews

### Target Learning Goals
- Accurate, efficient extraction of effect sizes, study counts, and participant counts from meta-analyses for evidence synthesis

## Claims

- [Across 468 data points, human coders, LLMs, and both standards agreed on the same value in 280 cases (59.8%)](../claims/coder-agreement-patterns-upset-468.md) [+W]
- [Most extraction discrepancies stemmed from ambiguity within the source meta-analyses rather than coder fabrication](../claims/discrepancies-source-ambiguity.md) [+W]
- [State-of-the-art LLMs extract effect sizes, study counts, and participant counts from educational meta-analyses with excellent agreement with adjudicated gold and silver standards](../claims/llm-data-extraction-icc-gold-standard.md) [+W]
- [LLM-based extraction of three variables from 156 meta-analyses cost about $50 in computing fees, far less than estimated human-assistant labor costs](../claims/llm-extraction-cost-time-savings.md) [+W]
- [Hallucinations were rare for both human and LLM coders, whereas omission errors were more frequent and varied by coder](../claims/llm-hallucinations-rare-omissions-frequent.md) [+W]
- [Neither LLM nor human coders showed systematic over- or under-estimation in extracting data from educational meta-analyses](../claims/no-systematic-bias-llm-extraction.md) [+W]

## Related Strategies

- [Allocate human and AI effort by dimension type: automate explicit-criteria dimensions, retain human review for pedagogical judgment](human-ai-division-of-labor-mcq-generation.md)

## Examples
-

## Key Sources
- Jansen, T., Liebenow, L. W., Schaller, N.-J., Hattie, J., & Möller, J. (2026). Automated Data Extraction by Large Language Models: Assessing Accuracy in Comparison to Human Experts Using the Example of Visible Learning. Educational Psychology Review. https://doi.org/10.1007/s10648-026-10136-5
