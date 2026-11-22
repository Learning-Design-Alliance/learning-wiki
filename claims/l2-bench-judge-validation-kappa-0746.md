---
type: claim
title: "The LLM-as-a-judge production scorer achieves substantial agreement with human rater majority vote (Cohen's kappa = 0.746, accuracy 92.3%)"
description: "The LLM-as-a-judge production scorer achieves substantial agreement with human rater majority vote (Cohen's kappa = 0.746, accuracy 92.3%)"
id: l2-bench-judge-validation-kappa-0746
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: james-edgell-2026
    resource: "https://doi.org/10.1609/aies.v9i2.43189"
    title: "James Edgell, Wm. Matthew Kennedy, Ben Knight, Danielle Carvalho, Martin Ku, Isaac Pattis. (2026). L2-Bench: An Evaluation Benchmark for Measuring LLM Capabilities in Second Language Education. [doi:10.1609/aies.v9i2.43189](https://doi.org/10.1609/aies.v9i2.43189)"
    author: James Edgell, Wm. Matthew Kennedy, Ben Knight, Danielle Carvalho, Martin Ku, Isaac Pattis
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# The LLM-as-a-judge production scorer achieves substantial agreement with human rater majority vote (Cohen's kappa = 0.746, accuracy 92.3%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The production judge (Claude Sonnet 4.6 with reference-guided classifier prompt) achieved Cohen's kappa = 0.746 against human rater majority vote, with accuracy of 92.3%, F1 = 0.932, and recall of 0.948. [→ James Edgell 2026](#james-edgell-2026)
`q2 i?` Practitioners achieved Krippendorff's alpha = 0.362 with 89.8% raw agreement on criterion-level binary judgments, and the LLM judge matched or exceeded human inter-rater consistency on 7 of 9 tested configurations. [→ James Edgell 2026](#james-edgell-2026)

## Evidence

### James Edgell 2026

James Edgell, Wm. Matthew Kennedy, Ben Knight, Danielle Carvalho, Martin Ku, Isaac Pattis. (2026). L2-Bench: An Evaluation Benchmark for Measuring LLM Capabilities in Second Language Education. [doi:10.1609/aies.v9i2.43189](https://doi.org/10.1609/aies.v9i2.43189)

`q2 · i?` · `design · r3`

Judge validation against a rater baseline of 145 practitioners contributing 1,023 criterion-level ratings across 443 items, on 326 criteria with matched practitioner validation data. The article notes the kappa is computed against a denoised human majority-vote target and is not directly comparable to raw pairwise alpha = 0.362.

> "The production judge achieved Cohen'sκ= 0.746against human rater majority vote (67%)—categorized as “substantial agreement” (Landis and Koch 1977)—with accuracy of 92.3%, F1 = 0.932, and recall of 0.948 across 326 criteria with matched practitioner validation data."

## Discussion


## Related Claims
- [Unadjusted foundation models achieve only moderate agreement (Cohen's κ = 0.38–0.58) with expert annotations when classifying instructional moves in authentic classroom transcripts](llm-baseline-moderate-kappa-talk-moves.md) — related
- [A non-fine-tuned pre-trained sentiment analysis model achieves moderate agreement with human coders of student open-ended answers](pretrained-sa-moderate-agreement.md) — related
- [Inter-model agreement is moderate, indicating models do not consistently identify the same questions correctly](moderate-inter-model-agreement-endodontic-questions.md) — related
- [The emergent LLM coding pipeline reaches substantial agreement with expert human coding (Cohen's κ = 0.78, raw agreement 84%) on a stratified 10% sample](llm-discourse-coding-kappa-078-expert-agreement.md) — related
- [A fine-tuned BERT model achieves almost perfect agreement with human coders when classifying student self-affirmation essays, matching human-human reliability](fine-tuned-bert-matches-human-coders-self-affirmation-essays.md) — related
- [Inter-rater reliability between human experts and AI coding is very low](low-irr-experts-vs-ai-coding.md) — reports the opposite
