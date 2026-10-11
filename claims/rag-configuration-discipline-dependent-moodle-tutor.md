---
type: claim
title: "Optimal RAG configuration differs by discipline: STEM subjects perform best with 512-character chunks and temperature 0.3 (faithfulness 0.97), while humanities require 1000-character chunks and temperature 0.1 (context recall 1.00, faithfulness 0.98)"
description: "Optimal RAG configuration differs by discipline: STEM subjects perform best with 512-character chunks and temperature 0.3 (faithfulness 0.97), while humanities require 1000-character chunks and temperature 0.1 (contex..."
id: rag-configuration-discipline-dependent-moodle-tutor
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: anna-ostrowska-2026
    resource: "https://tinyurl.com/mrytc2dr"
    title: "Anna Ostrowska, Michał Kukla, Gabriela Majstrak, Jan Opala, Sebastian Pergała, Jan Skwarek, Anna Wróblewska. (2026). From Surface Learning to Deep Understanding: A Grounded AI Tutoring System for Moodle. https://tinyurl.com/mrytc2dr"
    author: Anna Ostrowska, Michał Kukla, Gabriela Majstrak, Jan Opala, Sebastian Pergała, Jan Skwarek, Anna Wróblewska
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: anna-ostrowska-2026-2
    resource: "https://tinyurl.com/mrytc2dr"
    title: "Anna Ostrowska, Michał Kukla, Gabriela Majstrak, Jan Opala, Sebastian Pergała, Jan Skwarek, Anna Wróblewska. (2026). From Surface Learning to Deep Understanding: A Grounded AI Tutoring System for Moodle. https://tinyurl.com/mrytc2dr"
    author: Anna Ostrowska, Michał Kukla, Gabriela Majstrak, Jan Opala, Sebastian Pergała, Jan Skwarek, Anna Wróblewska
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Optimal RAG configuration differs by discipline: STEM subjects perform best with 512-character chunks and temperature 0.3 (faithfulness 0.97), while humanities require 1000-character chunks and temperature 0.1 (context recall 1.00, faithfulness 0.98)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` For STEM subjects the optimal chunk size was 512 characters with model temperature 0.3, achieving RAGAS faithfulness of 0.97. [→ Anna Ostrowska 2026](#anna-ostrowska-2026)
`q2 i?` For humanities, larger chunks (1000 chars) and lower temperature (0.1) achieved context recall of 1.00 and average faithfulness of 0.98. [→ Anna Ostrowska 2026 (2)](#anna-ostrowska-2026-2)

## Evidence

### Anna Ostrowska 2026

Anna Ostrowska, Michał Kukla, Gabriela Majstrak, Jan Opala, Sebastian Pergała, Jan Skwarek, Anna Wróblewska. (2026). From Surface Learning to Deep Understanding: A Grounded AI Tutoring System for Moodle. https://tinyurl.com/mrytc2dr

`q2 · i?` · `design · r2`

RAGAS (LLM-as-a-Judge) evaluation of the system's retrieval and generation pipelines across disciplines. The technical optimization experiments found the printed STEM configuration, with "achieving a RAGAS faithfulness of 0.97" for technical formulas.

> "for STEM subjects: The optimal chunk size was 512 characters, and the best performance was reached with a model temperature of 0.3 were optimal for technical formulas, achieving a RAGAS faithfulness of 0.97"

### Anna Ostrowska 2026 (2)

Anna Ostrowska, Michał Kukla, Gabriela Majstrak, Jan Opala, Sebastian Pergała, Jan Skwarek, Anna Wróblewska. (2026). From Surface Learning to Deep Understanding: A Grounded AI Tutoring System for Moodle. https://tinyurl.com/mrytc2dr

`q2 · i?` · `design · r2`

The same RAGAS evaluation of the retrieval and generation pipelines reported the humanities configuration, "achieving a context recall of 1.00, and an average faithfulness of 0.98" with the larger chunks and lower temperature.

> "for humanities: larger chunks (1000 chars) and a lower temperature (0.1) were required to capture interpreted meanings, achieving a context recall of 1.00, and an average faithfulness of 0.98"

## Discussion


## Related Claims
- [Temperature-construct interactions: constructs with moderate theoretical coherence benefited from higher temperatures, while well-defined constructs required deterministic settings](temperature-construct-type-interaction-coding.md) — related
- [Gemini Flash 2.0 was selected for production over GPT-4o-mini and Llama 3.1 for its superior faithfulness and speed-to-cost ratio](gemini-flash-2-selected-for-faithfulness-and-cost.md) — related
