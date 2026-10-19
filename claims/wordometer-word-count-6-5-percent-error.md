---
type: claim
title: The Wordometer eye-tracking app estimates the number of words a person reads with an average error rate of 6.5 percent
description: The Wordometer eye-tracking app estimates the number of words a person reads with an average error rate of 6.5 percent
id: wordometer-word-count-6-5-percent-error
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-16
evidence_strength: moderate
sources:
  - id: kai-kunze-2013
    resource: "http://kaikunze.de/papers/2013Kunze-1.pdf"
    title: "Kai Kunze, Masakazu Iwamura, Koichi Kise, Seiichi Uchida, and Shinichiro Omachi. (2013). Activity Recognition for the Mind: Toward a Cognitive “Quantified Self.” Computer, IEEE Computer Society, October 2013. http://kaikunze.de/papers/2013Kunze-1.pdf"
    author: Kai Kunze, Masakazu Iwamura, Koichi Kise, Seiichi Uchida, and Shinichiro Omachi
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The Wordometer eye-tracking app estimates the number of words a person reads with an average error rate of 6.5 percent

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` A support vector regression algorithm using detected line breaks and eye-gaze features estimates words read with 6.5 percent average error for 8 users over 10 documents. [→ Kai Kunze 2013](#kai-kunze-2013)

## Evidence

### Kai Kunze 2013

Kai Kunze, Masakazu Iwamura, Koichi Kise, Seiichi Uchida, and Shinichiro Omachi. (2013). Activity Recognition for the Mind: Toward a Cognitive “Quantified Self.” Computer, IEEE Computer Society, October 2013. http://kaikunze.de/papers/2013Kunze-1.pdf

`q2 · i?` · `design · r2`

Prototype evaluation of the Wordometer app on the SMI iView X eye tracker: eye movements of users reading English documents were recorded, a line-break detector looked for long saccades against the reading direction, and support vector regression estimated word counts. The article reports an "average error rate of only 6.5 percent for 8 users over 10 documents"; no effect size is printed.

> "Our word-count estimation method achieves an average error rate of only 6.5 percent for 8 users over 10 documents."

## Discussion


## Related Claims

- [Mobile eye tracking distinguishes five document types with 99 percent user-dependent and 74 percent user-independent recognition from about one minute of gaze data](document-type-recognition-mobile-eye-tracking.md)
- [Eye tracking can identify which words a second-language reader had trouble understanding](eye-tracking-identifies-difficult-words-l2-reading.md)
