---
type: claim
title: In a randomized experiment on fraction problems, participants who used an AI assistant solved fewer unassisted test problems and skipped more than control participants
description: In a randomized experiment on fraction problems, participants who used an AI assistant solved fewer unassisted test problems and skipped more than control participants
id: ai-assistance-impairs-unassisted-fraction-performance-exp1
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: grace-liu-2026
    resource: "https://arxiv.org/abs/2604.04721"
    title: "Grace Liu, Brian Christian, Tsvetomira Dumbalska, Michiel A. Bakker, Rachit Dubey. (2026). AI Assistance Reduces Persistence and Hurts Independent Performance. Published as a conference paper at COLM 2026. https://arxiv.org/abs/2604.04721"
    author: Grace Liu, Brian Christian, Tsvetomira Dumbalska, Michiel A. Bakker, Rachit Dubey
    q: 3
    i: 2
    kind: causal
    rigour: 2
  - id: grace-liu-2026-2
    resource: "https://arxiv.org/abs/2604.04721"
    title: "Grace Liu, Brian Christian, Tsvetomira Dumbalska, Michiel A. Bakker, Rachit Dubey. (2026). AI Assistance Reduces Persistence and Hurts Independent Performance. Published as a conference paper at COLM 2026. https://arxiv.org/abs/2604.04721"
    author: Grace Liu, Brian Christian, Tsvetomira Dumbalska, Michiel A. Bakker, Rachit Dubey
    q: 3
    i: 1
    kind: causal
    rigour: 2
---

# In a randomized experiment on fraction problems, participants who used an AI assistant solved fewer unassisted test problems and skipped more than control participants

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3` · `i1`–`i2`

## Subclaims
`q3 i2` After AI removal, the AI condition had a lower unassisted solve rate than controls (Cohen's d = -0.42). [→ Grace Liu 2026](#grace-liu-2026)
`q3 i1` The AI condition also skipped more test problems than controls (Cohen's d = 0.25), indicating reduced persistence. [→ Grace Liu 2026 (2)](#grace-liu-2026-2)

## Evidence

### Grace Liu 2026

Grace Liu, Brian Christian, Tsvetomira Dumbalska, Michiel A. Bakker, Rachit Dubey. (2026). AI Assistance Reduces Persistence and Hurts Independent Performance. Published as a conference paper at COLM 2026. https://arxiv.org/abs/2604.04721

`q3 · i2` · `causal · r2`

Randomized controlled experiment (N=354 recruited, 307 analyzed) on Prolific; AI condition solved 12 fraction problems with a GPT-5 sidebar assistant, then 3 unassisted test problems. The AI condition's test solve rate was lower, "Cohen's d=− 0.42".

> "Participants in the AI condition had a lower solve rate (mean 0.57, s.d. 0.41) than participants in the control condition (mean 0.73, s.d. 0.34; t(305) =− 3.64, P< 0.001; Cohen's d=− 0.42, 95% CI [−0.66,−0.19])."

### Grace Liu 2026 (2)

Grace Liu, Brian Christian, Tsvetomira Dumbalska, Michiel A. Bakker, Rachit Dubey. (2026). AI Assistance Reduces Persistence and Hurts Independent Performance. Published as a conference paper at COLM 2026. https://arxiv.org/abs/2604.04721

`q3 · i1` · `causal · r2`

Same RCT; skipping was a deliberate decision not to engage since there was no penalty for wrong answers. The AI condition's test skip rate was higher, "Cohen's d= 0.25".

> "Additionally, participants in the AI condition had a higher skip rate (mean 0.20, s.d. 0.36) than participants in the control condition (mean 0.11, s.d. 0.29; t(305) = 2.16, P= 0.031; Cohen's d= 0.25, 95% CI [0.02, 0.48])."

## Discussion


## Related Claims
- [Experiment 2 replicates the unassisted-performance impairment with a pretest-based exclusion, but the aggregate skip-rate difference does not reach significance](ai-assistance-impairs-performance-replication-exp2.md) — related
- [AI assistance impairs unassisted performance and persistence in reading comprehension, replicating the fraction-task effects in a second domain](ai-assistance-impairs-reading-comprehension-exp3.md) — a narrower finding that bears on this claim
- [Persistence and performance costs concentrate among participants who used the AI to obtain direct solutions, while hint-users resemble controls](persistence-costs-concentrated-among-direct-solution-users.md) — related
- [AI assistance reduces persistence: persistence costs concentrate among learners who used AI for direct solutions, not hints](ai-assistance-persistence-costs-direct-solutions.md) — a broader claim this one bears on
- [AI access raises immediate unaided test scores by 7.2 percentage points (0.28 SD) after a timed learning phase](genai-access-raises-immediate-test-scores.md) — reports the opposite
- [Unrestricted GPT-4 access in high-school mathematics raised assisted practice performance but left students worse off after withdrawal](gpt4-access-harms-learning-after-withdrawal.md) — related
- [Unguarded answer-giving AI harmed unaided exam performance while a guarded version of the same model erased the harm (Bastani et al., 2025, as reported)](guarded-ai-placement-prevents-unaided-exam-harm.md) — related
- [In math problem solving, a tutor-plus-peers LLM arrangement produced the strongest unassisted post-task test accuracy, with accuracy increasing monotonically from Control to Tutor + Peers](tutor-plus-peers-strongest-unassisted-math-accuracy.md) — related
