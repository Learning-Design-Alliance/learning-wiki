---
type: claim
title: Students using Google produce higher-quality justifications in their final recommendations than students using ChatGPT 3.5
description: Students using Google produce higher-quality justifications in their final recommendations than students using ChatGPT 3.5
id: web-search-higher-quality-justifications-than-llm
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-15
evidence_strength: moderate
newest_evidence: 2024
source_checked: 2026-10-29
sources:
  - id: matthias-stadler-2024
    resource: "https://doi.org/10.1016/j.chb.2024.108386"
    title: "Matthias Stadler, Maria Bannert, Michael Sailer. (2024). Cognitive ease at a cost: LLMs reduce mental effort but compromise depth in student scientific inquiry. Computers in Human Behavior. https://doi.org/10.1016/j.chb.2024.108386"
    author: Matthias Stadler, Maria Bannert, Michael Sailer
    q: 3
    i: 2
    kind: causal
    rigour: 2
---

# Students using Google produce higher-quality justifications in their final recommendations than students using ChatGPT 3.5

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3` · `i2` medium
> **Currency** · newest study 2024 · checked against its sources 2026-10-29 (automated, 1 of 1 entry) · not reviewed by a person

## Subclaims
`q3 i2` Students in the web search condition listed significantly more relevant arguments in their final recommendations than students in the LLM condition, adjusted for prior knowledge (η² = 0.11). [→ Matthias Stadler 2024](#matthias-stadler-2024)

## Evidence

### Matthias Stadler 2024

Matthias Stadler, Maria Bannert, Michael Sailer. (2024). Cognitive ease at a cost: LLMs reduce mental effort but compromise depth in student scientific inquiry. Computers in Human Behavior. https://doi.org/10.1016/j.chb.2024.108386

`q3 · i2` · `causal · r2`

ANCOVA on coded justification quality (number of relevant aspects mentioned; inter-rater agreement k = 0.92) in the randomized experiment (n=91). Web search mean 1.87 (SD 1.10) versus LLM 1.20 (SD 0.77), with "11.18 0.001 0.11", i.e., η² = 0.11, a medium effect.

> "H2 –Qualityofjustifications 1.87(1.10) 1.20(0.77) 11.18 0.001 0.11"

## Studies bearing on this claim

<!-- synthesis:start -->
*When learners research a question, does searching with a web search engine lead to deeper learning than asking a generative AI chatbot or reading an AI summary?* This table gathers the studies behind this claim and the 6 narrower claims that bear on it: **3 distinct studies** (3 causal), `q2`–`q3`, 1 of 3 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Matthias Stadler 2024](https://doi.org/10.1016/j.chb.2024.108386) | q2 / q3 · causal · r2 | i2; i?; i3 | this claim; [Germane cognitive load fully mediates the effect of information-search tool on justificati](germane-load-mediates-tool-effect-on-justification-quality.md) (supports); [Students using ChatGPT 3.5 experience lower germane cognitive load than students using Goo](llm-search-lower-germane-cognitive-load.md) (supports); [Students using ChatGPT 3.5 experience lower intrinsic cognitive load than students using G](llm-search-lower-intrinsic-cognitive-load.md) (qualifies) |
| [Shravika Mittal 2026](https://doi.org/10.48550/arxiv.2606.11669) | q2 · causal · r2 | i? | [ChatGPT users showed a non-significant trend toward worse overall informal learning outcom](chatgpt-worse-informal-learning-outcome-trend.md) (supports); [ChatGPT users began information seeking with narrow, specified queries far more often than](chatgpt-narrow-starting-queries.md) (qualifies) |
| [Yifan Liu 2026](https://doi.org/10.48550/arxiv.2606.08936) | q2 · causal · r? | i? | [AI overviews in an academic search engine showed mixed effects: summaries may reduce menta](ai-overviews-mixed-effects-academic-search.md) (qualifies) |
<!-- synthesis:end -->

## Discussion

## Related Claims

- [Direct GenAI-supported feedback improves immediate argument-quality gain over peer feedback, while reflective and hybrid designs outperform direct GenAI feedback](genai-feedback-design-argument-quality-gain.md) — the general claim this finding bears on, with the studies behind it
- [Recommendation homogeneity does not differ between students using ChatGPT 3.5 and students using Google](llm-recommendation-homogeneity-no-difference.md) — related
- [Students using ChatGPT 3.5 experience lower extraneous cognitive load than students using Google during a web research task](llm-search-lower-extraneous-cognitive-load.md) — related
- [Germane cognitive load fully mediates the effect of information-search tool on justification quality (exploratory analysis)](germane-load-mediates-tool-effect-on-justification-quality.md) — related
- [ChatGPT users differentiated information less (never by credibility) and rarely verified information compared to Google users](chatgpt-reduced-differentiation-verification.md) — related
- [Cognitive offloading to generative AI is associated with reduced learner engagement, lower critical thinking, and lower-quality reasoning](cognitive-offloading-reduces-engagement-critical-thinking.md) — a broader claim this one bears on
- [Google Trends data show ChatGPT search interest surged globally within weeks of its November 2022 public release, with plagiarism among the top related queries](google-trends-chatgpt-plagiarism-queries.md) — related
- [Undergraduate students’ genAI knowledge contains specific confident misconceptions, most prevalently that AI chatbots perform web searches](genai-misconceptions-web-search-item.md) — related
- [ChatGPT users showed a non-significant trend toward worse overall informal learning outcomes than Google Search users over 8 days](chatgpt-worse-informal-learning-outcome-trend.md) — related
- [The impact of the strategy training was higher for evaluation than for search skills, in terms of accuracy and quality of students' justifications.](training-impact-higher-evaluation-than-search.md) — related
- [ChatGPT biased information access toward solution-oriented artifacts over principle-oriented information](chatgpt-artifact-over-principle-bias.md) — related
- [LLM-supported socio-scientific inquiry lowered cognitive load but produced lower-quality reasoning and argumentation than conventional search](llm-inquiry-lower-load-lower-reasoning.md) — a broader claim this one bears on
