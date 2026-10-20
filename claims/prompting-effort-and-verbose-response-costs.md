---
type: claim
title: "Prompting is a major source of AI-assisted cognitive effort: copying prompts reduces effort but not time, and verbose model responses can make AI-assisted completion slower than predicted"
description: "Prompting is a major source of AI-assisted cognitive effort: copying prompts reduces effort but not time, and verbose model responses can make AI-assisted completion slower than predicted"
id: prompting-effort-and-verbose-response-costs
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: sunny-yu-2026
    resource: "https://doi.org/10.48550/arxiv.2605.23177"
    title: "Sunny Yu, Myra Cheng, Ahmad Jabbar, Ilia Sucholutsky, Katherine M. Collins, Dan Jurafsky, Robert D. Hawkins. (2026). Cognitive offloading and the speedup illusion in human-AI interaction. arXiv. https://arxiv.org/abs/2605.23177 [doi:10.48550/arxiv.2605.23177](https://doi.org/10.48550/arxiv.2605.23177)"
    author: Sunny Yu, Myra Cheng, Ahmad Jabbar, Ilia Sucholutsky, Katherine M. Collins, Dan Jurafsky, Robert D. Hawkins
    q: 3
    i: "?"
    kind: causal
    rigour: 3
---

# Prompting is a major source of AI-assisted cognitive effort: copying prompts reduces effort but not time, and verbose model responses can make AI-assisted completion slower than predicted

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r3` · `q3`

## Subclaims
`q3 i?` Over 70% of interactions were single-turn; copying prompts reduced NASA-TLX by 0.14 points without reducing time; for one logic problem, AI-assisted completion took significantly longer than predicted. [→ Sunny Yu 2026](#sunny-yu-2026)

## Evidence

### Sunny Yu 2026

Sunny Yu, Myra Cheng, Ahmad Jabbar, Ilia Sucholutsky, Katherine M. Collins, Dan Jurafsky, Robert D. Hawkins. (2026). Cognitive offloading and the speedup illusion in human-AI interaction. arXiv. https://arxiv.org/abs/2605.23177 [doi:10.48550/arxiv.2605.23177](https://doi.org/10.48550/arxiv.2605.23177)

`q3 · i?` · `causal · r3`

Analysis of user-LLM interaction logs found more than 70% single-turn interactions, 18.5% of prompts directly copied, and "much of the cognitive effort comes from writing the prompt". Time decomposition showed model generation was minimal (2.89 seconds); for one logic problem, verbose GPT-4o answers made AI-assisted completion significantly longer (β=−110.66, p<0.01) despite predictions of a speedup over 2 minutes.

> "Copying and pasting did not significantly reduce completion time, but it reduced NASA-TLX (average) by 0.14 points (SE=0.058,z=2.38,p<0.05). The finding reveals that when completing a task with AI assistance, much of the cognitive effort comes from writing the prompt."

## Discussion


## Related Claims
- [AI assistance reduces subjective mental effort across all tasks even when it does not reduce completion time, dissociating time and effort](ai-effort-reduction-time-effort-dissociation.md) — related
- [In interviews with 25 engineering students at one Swedish university, students described GenAI as acceptable when it stimulates reflection and directly copying its outputs as cheating, and one used its fallibility as a prompt to double-check](genai-ethics-reflection-versus-copying-boundaries.md) — related
- [Limiting verbose Math Agent guidance sharply reduced answer giveaway but decreased cognitive engagement](math-agent-guidance-limit-tradeoff.md) — related
- [People significantly underestimate AI-assisted completion times on simple cognitive tasks, even though AI assistance saves little or no actual time (the speedup illusion)](speedup-illusion-ai-assisted-time-underestimation.md) — related
- [Participants more averse to thinking are more susceptible to the speedup illusion; AI familiarity measures do not predict calibration error](thinking-aversion-predicts-speedup-illusion.md) — related
- [People overestimate how much mental effort AI assistance alleviates (offloading illusion), driven by overestimating the effort of independent completion while AI-assisted effort is accurately estimated](offloading-illusion-ai-effort-savings.md) — related
- [Within prompt–response AI interfaces, students without guidance rarely move beyond prompt tuning, yielding interactions of limited educational value and increased reliance on outputs](prompt-response-interface-limits-learning-value.md) — related
- [AI-section students framed the AI as a collaborative partner even when logs showed one-shot imperatives and rapid acceptance (Illusion of Dialogue)](illusion-of-dialogue-partnership-framing.md) — related
- [No differences were found on mental effort during instruction or on transfer across illusion-of-control and instruction-method conditions](no-mental-effort-differences.md) — related
- [AI assistance provides no significant overall time savings and can slow completion on easy task variants, with chat-interface friction (prompting time) dominating on trivial tasks](ai-no-efficiency-gain-simple-tasks.md) — related
- [Behavioural engagement indicators such as platform interaction and task completion do not by themselves establish cognitive engagement with mathematical ideas](behavioural-engagement-not-cognitive-engagement.md) — related
- [Reducing Math Agent output and disabling it for non-math courses reduced latency and increased behavioral engagement](math-agent-reduction-livelatency-engagement-gains.md) — related
