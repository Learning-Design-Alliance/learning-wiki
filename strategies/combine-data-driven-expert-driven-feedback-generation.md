---
type: strategy
id: combine-data-driven-expert-driven-feedback-generation
title: Combine data-driven and expert-driven approaches, and add a filter network, to mitigate non-factual output in automated feedback
description: The article recommends hybrid approaches to address the drawbacks of data-driven feedback generation, which the authors describe as data hungry and not always controllable.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: qinjin-jia-2022
    resource: "https://github.com/qinjinjia/JEDM22_Automated_Feedback_Generation"
    title: "Qinjin Jia, Mitchell Young, Yunkai Xiao, Jialin Cui, Chengyuan Liu, Parvez Rashid, Edward Gehringer. (2022). Automated Feedback Generation for Student Project Reports: A Data-Driven Approach. Journal of Educational Data Mining, Volume 14, No 3. https://github.com/qinjinjia/JEDM22_Automated_Feedback_Generation"
    author: Qinjin Jia, Mitchell Young, Yunkai Xiao, Jialin Cui, Chengyuan Liu, Parvez Rashid, Edward Gehringer
---

# Combine data-driven and expert-driven approaches, and add a filter network, to mitigate non-factual output in automated feedback

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends hybrid approaches to address the drawbacks of data-driven feedback generation, which the authors describe as data hungry and not always controllable. They suggest that "Future work could therefore attempt to alleviate the drawbacks by combining data-driven and expert-driven approaches", and specifically propose that "An alternative solution is to train an additional “filter” network to filter out non-factual statements before delivering them to students." This strategy targets the roughly 15.2% of generated statements that were non-factual or ambiguous.

## Design Implications

### Context
#### Requirements
- Sufficient training data of adequate quality for the data-driven component
- An additional filtering mechanism or expert-designed rules to check statements before delivery
#### Constraints
- Completely eliminating inaccurate sentences is almost impossible for a purely data-driven approach, per the article

### Target Learners
- students receiving automated feedback on project reports

### Target Learning Goals
- protecting learners from misleading or confusing automated feedback

## Related Strategies

- [Apply error mitigation such as self-consistency before deploying LLM-generated help, and frame unmitigated LLM feedback as an imperfect source](mitigate-llm-hint-errors-before-deployment.md)

## Examples
-

## Key Sources
- Qinjin Jia, Mitchell Young, Yunkai Xiao, Jialin Cui, Chengyuan Liu, Parvez Rashid, Edward Gehringer. (2022). Automated Feedback Generation for Student Project Reports: A Data-Driven Approach. Journal of Educational Data Mining, Volume 14, No 3. https://github.com/qinjinjia/JEDM22_Automated_Feedback_Generation
