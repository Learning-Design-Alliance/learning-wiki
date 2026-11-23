---
type: research-method
id: standardized-zero-shot-multi-run-web-interface-evaluation-protocol-for-llms-on-high-stakes
title: Standardized zero-shot multi-run web-interface evaluation protocol for LLMs on high-stakes examinations
description: "The study employed a standardized zero-shot evaluation protocol in which all 10 LLMs completed five independent runs across all 300 examination statements through publicly available web interfaces rather than APIs, \"reflecting the predominant interaction patterns of clinical and educational end user"
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-04
---

# Standardized zero-shot multi-run web-interface evaluation protocol for LLMs on high-stakes examinations

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (2 design), `q1`–`q2` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
The study employed a standardized zero-shot evaluation protocol in which all 10 LLMs completed five independent runs across all 300 examination statements through publicly available web interfaces rather than APIs, "reflecting the predominant interaction patterns of clinical and educational end users". The prompt followed the CO-STAR structure (Context, Objective, Style, Tone, Audience, Response format) to specify task parameters and required concise true/false answers without explanations or hedging. Session independence was maintained by starting each run in a new browser session or incognito window, clearing all previous chat history and creating a fresh conversation for every evaluation, with model order randomized across runs and timestamps and exact model versions documented for each session.

## Accounts
<!-- How each source describes or uses the method -->
- **Standardized zero-shot CO-STAR-prompted multi-run web-interface evaluation protocol for assessing LLMs on high-stakes examinations.**: The study employed a standardized zero-shot evaluation protocol in which all 10 LLMs completed five independent runs across all 300 examination statements through publicly available web interfaces rather than APIs, "reflecting the predominant interaction patterns of clinical and educational end users". The prompt followed the CO-STAR structure (Context, Objective, Style, Tone, Audience, Response format) to specify task parameters and required concise true/false answers without explanations or hedging. Session independence was maintained by starting each run in a new browser session or incognito window, clearing all previous chat history and creating a fresh conversation for every evaluation, with model order randomized across runs and timestamps and exact model versions documented for each session. (Güler Ibrahim et al. (2026))
- **Physics GRE image-snippet evaluation protocol for LLMs**: An evaluation procedure in which a full-length, 100-question Physics GRE test from the Educational Testing Services website is split into individual question snippet images, each submitted to an LLM with no accompanying text or instructions, with question numbers removed to avoid bias. The article reports that "Bard gave detailed explanations of its answers even when there was no additional text provided in the prompt other than the image of the test question." Scoring uses the penalized rubric C − I/4, which gives a random guesser a score of 0. (Pranav Gupta (2023))

### Claims
- [Inter-run reliability of LLM performance on the EBHS examination was consistently high, with an overall mean Cohen's κ of 0.821 and no model falling below moderate agreement.](../claims/llm-ebhs-inter-run-reliability-high-kappa-0821.md) [+W]
- [Bard answered 26 of 98 Physics GRE questions correctly, earning a raw score of 8 out of 100 and placing in the bottom 2% of test-takers](../claims/bard-bottom-2-percent-physics-gre.md) [+M]
- [Bard's safety guardrails blocked image upload for 2 of the 100 Physics GRE questions](../claims/bard-image-upload-failures-two-of-100.md) [+W]

## Related Research Methods
-

## Key Sources
- Güler Ibrahim, Muir Lindsay, Grieb Gerrit, Moog Philipp, Kraus Armin, Stelling Henrik. (2026). Performance and reliability of large language models on the European Board of Hand Surgery examination: a multi-model evaluation study. The Journal of Hand Surgery, European Volume. https://doi.org/10.1177/17531934261436305
- Pranav Gupta. (2023). Testing an LLM's performance on the Physics GRE: some observations. https://arxiv.org/abs/2312.04613
