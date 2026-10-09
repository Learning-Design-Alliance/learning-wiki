---
type: claim
title: On a real dataset with problem content, the skill discovery model matches BKT with expert-provided skills despite using fewer KCs
description: On a real dataset with problem content, the skill discovery model matches BKT with expert-provided skills despite using fewer KCs
id: skill-discovery-matches-expert-skills-fewer-kcs
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-27
evidence_strength: moderate
sources:
  - id: khajah-2024
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/16-1"
    title: "Khajah, M. M. (2024). Supercharging BKT with Multidimensional Generalizable IRT and Skill Discovery. Journal of Educational Data Mining, Volume 16, No 1, 2024. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/16-1"
    author: Khajah, M. M.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# On a real dataset with problem content, the skill discovery model matches BKT with expert-provided skills despite using fewer KCs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On the equations (handwriting) dataset with problem text features, the skill discovery model's prediction performance matches that of BKT using expert-provided KC assignments, using fewer knowledge components. [→ Khajah 2024](#khajah-2024)

## Evidence

### Khajah 2024

Khajah, M. M. (2024). Supercharging BKT with Multidimensional Generalizable IRT and Skill Discovery. Journal of Educational Data Mining, Volume 16, No 1, 2024. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/16-1

`q2 · i?` · `design · r2`

Evaluation on the equations dataset (2007 handwriting study, control condition only), where step names are cleaned equations embedded with all-mpnet-base-v2 into 768-dimensional feature vectors. The article reports the model "matches BKT with expert-provided skills, despite using fewer KCs".

> "On a real dataset where problem content is available, the skill discovery model matches BKT with expert-provided skills, despite using fewer KCs."

## Discussion


## Related Claims
- [The skill discovery model partially recovers the true problem-KC assignment matrix in synthetic datasets when provided with problem representations](skill-discovery-partially-recovers-true-kc-assignments.md) — related
- [The expert-designed KC model adds little predictive power on most datasets, with significant contributions only on the two KDD Cup 2010 datasets](expert-kc-model-adds-little-predictive-power.md) — related
- [Automatic skill discovery identifies more knowledge components than domain experts on both tutoring datasets](skill-discovery-finds-more-kcs-than-experts.md) — related
