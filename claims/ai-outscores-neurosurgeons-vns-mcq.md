---
type: claim
title: A specialized RAG-based LLM outscored all 36 neurosurgeons on a VNS knowledge MCQ, with a total score of 0.75 versus a highest individual surgeon score of 0.68
description: A specialized RAG-based LLM outscored all 36 neurosurgeons on a VNS knowledge MCQ, with a total score of 0.75 versus a highest individual surgeon score of 0.68
id: ai-outscores-neurosurgeons-vns-mcq
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
  - id: barrit-sami-2025-2
    resource: "https://doi.org/10.1007/s00701-025-06610-8"
    title: "Barrit Sami, Ranuzzi Giovanni, Fetzer Steffen, Al Barajraji Mejdeddine, Hadwe Salim El, Zanello Marc, Ortler Martin, O'Flaherty Julieta, Massager Nicolas, Madsen Joseph R., Dibué Maxine, Carron Romain. (2025). Specialized AI and neurosurgeons in niche expertise: a proof-of-concept in neuromodulation with vagus nerve stimulation. Acta Neurochirurgica. https://doi.org/10.1007/s00701-025-06610-8"
    author: "Barrit Sami, Ranuzzi Giovanni, Fetzer Steffen, Al Barajraji Mejdeddine, Hadwe Salim El, Zanello Marc, Ortler Martin, O'Flaherty Julieta, Massager Nicolas, Madsen Joseph R., Dibué Maxine, Carron Romain"
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# A specialized RAG-based LLM outscored all 36 neurosurgeons on a VNS knowledge MCQ, with a total score of 0.75 versus a highest individual surgeon score of 0.68

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q3 i?` The AI's total score of 0.75 exceeded the highest individual surgeon's score of 0.68 and the surgeons' median of 0.50, and was statistically significantly higher than the surgeons' score distribution. [→ Barrit Sami 2025](#barrit-sami-2025)
`q3 i?` A Wilcoxon signed-rank test with continuity correction comparing the AI's total score against the surgeons' score distribution yielded p < 0.001. [→ Barrit Sami 2025 (2)](#barrit-sami-2025-2)

## Evidence

### Barrit Sami 2025

Barrit Sami, Ranuzzi Giovanni, Fetzer Steffen, Al Barajraji Mejdeddine, Hadwe Salim El, Zanello Marc, Ortler Martin, O'Flaherty Julieta, Massager Nicolas, Madsen Joseph R., Dibué Maxine, Carron Romain. (2025). Specialized AI and neurosurgeons in niche expertise: a proof-of-concept in neuromodulation with vagus nerve stimulation. Acta Neurochirurgica. https://doi.org/10.1007/s00701-025-06610-8

`q3 · i?` · `design · r2`

Benchmark comparison in which a specialized LLM-driven system and 36 European neurosurgeons who completed a 2-day VNS masterclass answered the same MCQ under controlled conditions. The article reports "the AI's score of 0.75 was higher than the highest individual surgeon's score of 0.68".

> "Regarding the total scores, the AI's score of 0.75 was higher than the highest individual surgeon's score of 0.68, achieving higher scores than all 36 surgeons."

### Barrit Sami 2025 (2)

Barrit Sami, Ranuzzi Giovanni, Fetzer Steffen, Al Barajraji Mejdeddine, Hadwe Salim El, Zanello Marc, Ortler Martin, O'Flaherty Julieta, Massager Nicolas, Madsen Joseph R., Dibué Maxine, Carron Romain. (2025). Specialized AI and neurosurgeons in niche expertise: a proof-of-concept in neuromodulation with vagus nerve stimulation. Acta Neurochirurgica. https://doi.org/10.1007/s00701-025-06610-8

`q3 · i?` · `design · r2`

Wilcoxon signed-rank test with continuity correction comparing the AI's total score against the distribution of the 36 surgeons' scores; the article reports "a p-value of < 0.001". No effect size is printed, so impact is coded i? (no magnitude reported; not a null effect).

> "The test yielded a p-value of < 0.001, indicating a statistically significant difference between the AI's performance and that of the surgeons."

## Discussion


## Related Claims
- [AI and surgeons performed similarly on eight MCQ questions; the AI scored higher on anatomical/technical questions and surgeons scored higher on two practical-scenario questions](ai-versus-surgeon-question-level-pattern-vns.md) — related
- [The AI achieved perfect precision and specificity (1.0), higher true correct and true incorrect rates than surgeons, and no hallucinations were detected](ai-perfect-precision-specificity-no-hallucinations-vns.md) — related
