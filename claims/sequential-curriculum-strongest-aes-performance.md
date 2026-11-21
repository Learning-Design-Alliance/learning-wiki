---
type: claim
title: Sequential curriculum fine-tuning yields the strongest overall AES performance, achieving the highest or tied-for-highest F1 on Claim, Evidence, and Conclusion
description: Sequential curriculum fine-tuning yields the strongest overall AES performance, achieving the highest or tied-for-highest F1 on Claim, Evidence, and Conclusion
id: sequential-curriculum-strongest-aes-performance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: ali-keramati-and-mark-warschauer-2026
    resource: "https://doi.org/10.48550/arXiv.2606.10327"
    title: "Ali Keramati and Mark Warschauer. (2026). The Order Matters: Sequential Fine-Tuning of LLaMA for Coherent Automated Essay Scoring. Published as a conference paper at ICLR 2026. [doi:10.48550/arXiv.2606.10327](https://doi.org/10.48550/arXiv.2606.10327)"
    author: Ali Keramati and Mark Warschauer
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Sequential curriculum fine-tuning yields the strongest overall AES performance, achieving the highest or tied-for-highest F1 on Claim, Evidence, and Conclusion

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A LLaMA-3.1-8B model fine-tuned sequentially on Lead, Position, Claim, Evidence, then Conclusion achieves the highest or tied-for-highest weighted F1-scores on Claim (40%), Evidence (65%), and Conclusion (87%) on the PERSUADE 2.0 test split. [→ Ali Keramati and Mark Warschauer 2026](#ali-keramati-and-mark-warschauer-2026)

## Evidence

### Ali Keramati and Mark Warschauer 2026

Ali Keramati and Mark Warschauer. (2026). The Order Matters: Sequential Fine-Tuning of LLaMA for Coherent Automated Essay Scoring. Published as a conference paper at ICLR 2026. [doi:10.48550/arXiv.2606.10327](https://doi.org/10.48550/arXiv.2606.10327)

`q2 · i?` · `causal · r1`

Model experiments on the PERSUADE 2.0 test split comparing three fine-tuning curricula for LLaMA-3.1-8B, reported in Table 1 and Section 5.2. The sequential curriculum reached "the highest or tied-for-highest F1-scores on three of the five components", with Conclusion at 87% F1 and Evidence at 65% F1.

> "TheSequentialmodel achieves the highest or tied-for-highest F1-scores on three of the five components:Claim(40%),Evidence(65%), andConclusion(87%)."

## Discussion


## Related Claims
- [A fine-tuned 8B model outperforms a zero-shot LLaMA-70B baseline on context-dependent components like Evidence and Conclusion, though the 70B excels on self-contained components like Position](fine-tuned-8b-outperforms-70b-on-context-dependent-components.md) — possibly the same claim (merge candidate)
- [Randomized multi-task fine-tuning shows inconsistent benefits, achieving the best Position F1 but performing poorly on Lead](randomized-multitask-inconsistent-aes-benefits.md) — related
- [Sequentially fine-tuned models dramatically outperform independently fine-tuned models on scoring conclusions, implying conclusions require contextual representations from other essay parts](sequential-beats-independent-on-conclusion.md) — possibly the same claim (merge candidate)
