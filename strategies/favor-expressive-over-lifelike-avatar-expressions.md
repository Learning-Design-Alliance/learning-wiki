---
type: strategy
id: favor-expressive-over-lifelike-avatar-expressions
title: Prioritize exaggerated, easy-to-read avatar emotional expressions over lifelike realism in communication-training avatars
description: The article recommends that future avatar-based training systems favor emotional clarity over photorealism.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: kurtis-haut-2025
    resource: "https://arxiv.org/abs/2505.02694"
    title: "Kurtis Haut, Masam Hasan, Thomas Carroll, Ronald Epstein, Taylan Sen, Ehsan Hoque. (2025). AI Standardized Patient Improves Human Conversations in Advanced Cancer Care. https://arxiv.org/abs/2505.02694"
    author: Kurtis Haut, Masam Hasan, Thomas Carroll, Ronald Epstein, Taylan Sen, Ehsan Hoque
---

# Prioritize exaggerated, easy-to-read avatar emotional expressions over lifelike realism in communication-training avatars

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (2 for, 1 against) · 4 studies (3 causal, 1 review), `q2`–`q3` · 0 of 4 report an effect size · 2 claims rest on one study

## Description
The article recommends that future avatar-based training systems favor emotional clarity over photorealism. In its discussion it states that "Future systems may benefit from intentionally favoring exaggerated, easy-to-read expressions over striving for subtle, lifelike realism," because avatars that look too human can feel uncanny while stylized expressions may make emotional cues clearer. SOPHIE itself implements this by having facial and vocal cues "prioritize expressiveness over naturalness," escalating emotional intensity when a user fails to recognize the patient's state.

## Design Implications

### Context
#### Requirements
- An emotion-tagging dialogue manager that can drive facial expressions and vocal tone, with escalation when learners miss emotional cues
#### Constraints
- Participants still rated realism moderately (3.4/5) and described some interactions as uncanny; the recommendation rests on user feedback rather than a tested comparison of expression styles

### Target Learners
- healthcare students and clinicians practicing emotionally demanding conversations

### Target Learning Goals
- recognizing and responding to patient emotional cues

## Claims

- [Users rated SOPHIE's actionable feedback highest (4.7/5) and usability 4.2/5, while virtual human realism was rated more moderately (3.4/5)](../claims/sophie-actionable-feedback-highest-rated-feature.md) [+M]
- [Students rated the VSP system positively for usability and learning assistance, with comparatively low ratings for patient realism and authenticity](../claims/positive-ueq-ratings-vsp-system.md) [+W]
- [A 2024 vendor white paper cites research that avatars provide social presence and that realistic avatars in intelligent tutoring systems can increase student-tutor engagement](../claims/avatar-social-presence-increases-tutor-engagement.md) [-W]

## Related Strategies

- [Improve VR simulation realism by adding dynamic elements, animated avatars, and improved rendering](vr-realism-dynamic-avatars-rendering-strategy.md)

## Examples
-

## Key Sources
- Kurtis Haut, Masam Hasan, Thomas Carroll, Ronald Epstein, Taylan Sen, Ehsan Hoque. (2025). AI Standardized Patient Improves Human Conversations in Advanced Cancer Care. https://arxiv.org/abs/2505.02694
