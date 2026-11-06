---
type: claim
title: The AI achieved perfect precision and specificity (1.0), higher true correct and true incorrect rates than surgeons, and no hallucinations were detected
description: The AI achieved perfect precision and specificity (1.0), higher true correct and true incorrect rates than surgeons, and no hallucinations were detected
id: ai-perfect-precision-specificity-no-hallucinations-vns
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: barrit-sami-2025
    resource: "https://doi.org/10.1007/s00701-025-06610-8"
    title: "Barrit Sami, Ranuzzi Giovanni, Fetzer Steffen, Al Barajraji Mejdeddine, Hadwe Salim El, Zanello Marc, Ortler Martin, O'Flaherty Julieta, Massager Nicolas, Madsen Joseph R., Dibué Maxine, Carron Romain. (2025). Specialized AI and neurosurgeons in niche expertise: a proof-of-concept in neuromodulation with vagus nerve stimulation. Acta Neurochirurgica. https://doi.org/10.1007/s00701-025-06610-8"
    author: "Barrit Sami, Ranuzzi Giovanni, Fetzer Steffen, Al Barajraji Mejdeddine, Hadwe Salim El, Zanello Marc, Ortler Martin, O'Flaherty Julieta, Massager Nicolas, Madsen Joseph R., Dibué Maxine, Carron Romain"
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# The AI achieved perfect precision and specificity (1.0), higher true correct and true incorrect rates than surgeons, and no hallucinations were detected

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Confusion-matrix analysis showed higher true correct and true incorrect rates for the AI than the surgeons, and the AI achieved perfect scores (1.0) in precision and specificity with no hallucinations detected. [→ Barrit Sami 2025](#barrit-sami-2025)

## Evidence

### Barrit Sami 2025

Barrit Sami, Ranuzzi Giovanni, Fetzer Steffen, Al Barajraji Mejdeddine, Hadwe Salim El, Zanello Marc, Ortler Martin, O'Flaherty Julieta, Massager Nicolas, Madsen Joseph R., Dibué Maxine, Carron Romain. (2025). Specialized AI and neurosurgeons in niche expertise: a proof-of-concept in neuromodulation with vagus nerve stimulation. Acta Neurochirurgica. https://doi.org/10.1007/s00701-025-06610-8

`q3 · i?` · `design · r2`

Performance-metric calculation from the same MCQ benchmark, with confusion matrices visualizing true correct, false correct, false incorrect and true incorrect responses for surgeons versus AI. The article reports "perfect scores (1.0) in precision and specificity" and no hallucinations.

> "The AI achieved perfect scores (1.0) in precision and specificity (Fig. 3). No hallucinations were detected."

## Discussion


## Related Claims
- [A specialized RAG-based LLM outscored all 36 neurosurgeons on a VNS knowledge MCQ, with a total score of 0.75 versus a highest individual surgeon score of 0.68](ai-outscores-neurosurgeons-vns-mcq.md) — related
- [General-purpose LLMs show accuracy and reliability limits, including hallucinations and task-specific accuracy below perfect, making them risky as expert advice sources](llm-accuracy-hallucination-coaching-risk.md) — a broader claim this one bears on
- [The three training methods differentially affected confusion-matrix components: lecture raised specificity, dataset raised sensitivity, AI improved all categories](training-methods-differential-confusion-matrix-effects.md) — related
- [Across all 52 dental students, errors fell and IoU, sensitivity, specificity, accuracy, precision, and F1 score rose significantly from pre-test to post-test after training, in one group with no comparison group](training-improves-bitewing-caries-detection-all-metrics.md) — related
- [Lower-performing groups gain relative advantage because the scorer detects incorrect responses better for them, producing more false positives](lower-performers-more-false-positives-advantage.md) — related
