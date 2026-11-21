---
type: design
id: regex-recipe-jupyter-collab-activity
title: Regex recipe-organization collaborative learning activity in JupyterLab with embedded auto-grader and LLM agent support
description: The article describes a Python programming activity on regular expressions, a topic the authors note is particularly challenging for novice programmers.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: wu-2025
    resource: "http://bit.ly/4leDl0U"
    title: "Wu, Z., Shi, J., Murray, R. C., Rosé, C., & San Andres, M. (2025). LLM Bazaar: A Service Design for Supporting Collaborative Learning with an LLM-Powered Multi-Party Collaboration Infrastructure. CSCL 2025 Proceedings. http://bit.ly/4leDl0U"
    author: "Wu, Z., Shi, J., Murray, R. C., Rosé, C., & San Andres, M"
---

# Regex recipe-organization collaborative learning activity in JupyterLab with embedded auto-grader and LLM agent support

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article describes a Python programming activity on regular expressions, a topic the authors note is particularly challenging for novice programmers. "The activity is set in the JupyterLab infrastructure, which has already been integrated with Bazaar", with a built-in auto-grader offering immediate feedback. Eight progressively building tasks alternate between creating regex patterns and applying them to extract, modify, and organize recipe text, framed as helping a home cook prepare for a family cooking session. An LLM agent joins the chat window to prompt idea sharing and provide hints after a preset timer if the group is stuck.

## Design Implications

### Context
#### Requirements
- Requires the JupyterLab environment integrated with Bazaar, a chat window within the notebook, and a preset hint timer for the support agent
#### Constraints
- The collaborative version includes improvements based on a pilot and will be deployed in the next iteration of the course; it has not yet been fully deployed

### Target Learners
- novice programmers
- community college Python students

### Learning Goals
- constructing and refining regex patterns
- applying regex to extract, modify, and format structured text data

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Wu, Z., Shi, J., Murray, R. C., Rosé, C., & San Andres, M. (2025). LLM Bazaar: A Service Design for Supporting Collaborative Learning with an LLM-Powered Multi-Party Collaboration Infrastructure. CSCL 2025 Proceedings. http://bit.ly/4leDl0U. [doi:10.48550/arxiv.2510.18877](https://doi.org/10.48550/arxiv.2510.18877)
