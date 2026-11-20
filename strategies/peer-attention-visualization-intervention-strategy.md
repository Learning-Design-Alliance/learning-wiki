---
type: strategy
id: peer-attention-visualization-intervention-strategy
title: Design adaptive online learning interventions that model and visualize peer attention to optimize student attentiveness
description: "The article recommends leveraging peer attention modelling in adaptive online learning: extract where peers gaze on course slides (via voted areas of interest) and display these regions as visual cues during video lea..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: songlin-xu-2023
    resource: "https://arxiv.org/abs/2312.02358"
    title: "Songlin Xu, Dongyin Hu, Ru Wang, and Xinyu Zhang. (2023). Peer attention enhances student learning. arXiv preprint. https://arxiv.org/abs/2312.02358"
    author: Songlin Xu, Dongyin Hu, Ru Wang, and Xinyu Zhang
---

# Design adaptive online learning interventions that model and visualize peer attention to optimize student attentiveness

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (5 for, 1 mixed) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 6 claims rest on one study

## Description
The article recommends leveraging peer attention modelling in adaptive online learning: extract where peers gaze on course slides (via voted areas of interest) and display these regions as visual cues during video learning. The authors state these insights "inform the design of adaptive educational interventions leveraging peer influence cues to optimize learning experiences and outcomes". The strategy targets attentional engagement rather than content delivery, and works because peer cues shape gaze while students retain personal adaptivity.

## Design Implications

### Context
#### Requirements
- Gaze data from a peer cohort (Control group) to extract shared attention regions
- Real-time capability to summarize gaze and generate visual feedback during video playback
#### Constraints
- Benefits manifest most strongly for difficult content necessitating engaged focus, not simple recognition items
- Pace-adherence alone does not guarantee comprehension; students may benefit from pausing to think deeply

### Target Learners
- online course students watching video lectures

### Target Learning Goals
- attentional focus and engagement
- comprehension of complex course content

## Claims

- [Logistic regression over question-specific video segments finds peer attention and valid focus positively predict accuracy while course following negatively predicts it](../claims/course-following-negatively-predicts-accuracy.md) [+W]
- [Over 60% of Feedback participants reported noticing the peer attention cues, though the authors argue influence may also be unconscious](../claims/peer-attention-cue-awareness-self-report.md) [+W]
- [Peer attention cues improve accuracy on hard comprehension questions and overall test scores, but not easy recognition questions](../claims/peer-attention-improves-hard-question-accuracy.md) [+W]
- [Displaying peer attention regions reduces inattention and confusion durations during online video learning](../claims/peer-attention-reduces-inattention-confusion.md) [+W]
- [Peer attention cues increase valid focus, course following, and crowd gaze consistency, yet students retain adaptability in following peer cues](../claims/peer-attention-shapes-gaze-with-retained-adaptability.md) [+W]
- [Group-level accuracy benefits of peer attention were not always significant when videos were analyzed individually](../claims/peer-attention-video-level-significance-limited.md) [~W]

## Related Strategies

- [Use gaze tracking as a feedback tool to alert students and instructors to key moments in simulation learning](gaze-tracking-feedback-simulation-debriefing.md)
- [Integrate AOI-dependent eye-tracking and motion metrics into training sessions for real-time formative feedback and personalized training](eye-tracking-real-time-formative-feedback-laparoscopic-training.md)

## Examples
-

## Key Sources
- Songlin Xu, Dongyin Hu, Ru Wang, and Xinyu Zhang. (2023). Peer attention enhances student learning. arXiv preprint. https://arxiv.org/abs/2312.02358
