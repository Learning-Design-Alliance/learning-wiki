---
type: research-method
id: multimodal-analysis
aliases: [multimodal-classroom-video-analysis-for-teacherstudent-interaction-detection]
title: Multimodal analysis
description: "Multimodal analysis is one of three methodological advances the report highlights, defined as \"Integrating multiple streams of data, such as audio, video, eye gaze, sensors, and clickstream data.\" The introduction elaborates it as \"the study of learning with data streams that include physical moveme"
status: review
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: roschelle-2017
    resource: "https://digitalpromise.dspacedirect.org/items/dafbe585-c0f8-4693-bde8-a6d847a58aad"
    title: "Roschelle, J., Martin, W., Ahn, J. & Schank, P. (Eds.). (2017). Cyberlearning Community Report: The State of Cyberlearning and the Future of Learning With Technology. Menlo Park CA: SRI International. https://digitalpromise.dspacedirect.org/items/dafbe585-c0f8-4693-bde8-a6d847a58aad"
    author: "Roschelle, J., Martin, W., Ahn, J. & Schank, P. (Eds.)"
  - id: hur-2026
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/1030"
    title: "Hur, P., Palaguachi, C., Machaka, N., Krist, C., Dyer, E. B., D'Angelo, C., & Bosch, N. (2026). A Framework for Considering Exploration, Interpretation, and Confirmation During Data Analysis: Computationally Assisted Analysis of Teacher–Group Interactions. Journal of Educational Data Mining, 18(1). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/1030"
    author: "Hur, P., Palaguachi, C., Machaka, N., Krist, C., Dyer, E. B., D'Angelo, C., & Bosch, N"
---

# Multimodal analysis

> **Research Method** · [All research methods](index.md)
> **Evidence** · 8 claims (8 for) · 3 studies (2 associational, 1 design), `q2`–`q3` · 0 of 3 report an effect size · 8 claims rest on one study

## Description
Multimodal analysis is one of three methodological advances the report highlights, defined as "Integrating multiple streams of data, such as audio, video, eye gaze, sensors, and clickstream data." The introduction elaborates it as "the study of learning with data streams that include physical movement, sound, and logs from interactions with technology (as well as more traditional observations)." The report presents the Connected Worlds exhibit at the New York Hall of Science, which enables embodied learning in an immersive sensor-rich space, as a research site where scientists are pushing the frontiers of multimodal analytics.

## Accounts
<!-- How each source describes or uses the method -->
- **Multimodal analysis: studying learning with multiple integrated data streams**: Multimodal analysis is one of three methodological advances the report highlights, defined as "Integrating multiple streams of data, such as audio, video, eye gaze, sensors, and clickstream data." The introduction elaborates it as "the study of learning with data streams that include physical movement, sound, and logs from interactions with technology (as well as more traditional observations)." The report presents the Connected Worlds exhibit at the New York Hall of Science, which enables embodied learning in an immersive sensor-rich space, as a research site where scientists are pushing the frontiers of multimodal analytics. (Roschelle et al. (2017))
- **AI-based speech processing pipeline for multi-teacher classroom audio**: An automated pipeline for analysing team-teaching talk: multi-channel headset recordings are processed with a weighted fusion of spectral masking and ECAPA-TDNN speaker-embedding-based masking to reduce cross-channel interference, transcribed with WhisperX, and used to extract 88 acoustic features with openSMILE from fixed 1-second segments. Quality was verified via word error rate: "The WER decreased from158%before cross-talk mitigation to21%after processing, which is considered acceptable". Standardised features were reduced by Varimax-rotated PCA into five rotated components explaining 58% of cumulative variance. (Yuchen Liu et al. (2026))
- **EEG-fNIRS bimodal complementarity framework for attention quantification**: The article's attention modeling framework rests on the complementary strengths of EEG and fNIRS. EEG offers millisecond-level temporal resolution sensitive to rapid stimulus changes but is susceptible to motion artifacts, while fNIRS suffers hemodynamic latency yet provides region-level spatial specificity and greater tolerance to movement. As the authors state, "EEG primarily contributes high-temporal-resolution neural dynamics, whereas fNIRS provides complementary region-level spatial information over the targeted cortical regions." These complementary properties motivate the bimodal input, with fused features feeding a DDQN that outputs high, medium, or low attention levels. (Shixian Zhou et al. (2026))
- **Multimodal pipeline for detecting and analyzing teacher–student group interactions in classroom video**: A computational pipeline combining three modalities from high school mathematics classroom videos: OpenPose pose estimation with Euclidean-distance tracking postprocessing and group boundary boxes, openSMILE eGeMAPS acoustic/prosodic features (88 features), and WhisperX word-level transcripts aligned to detected windows. A pose-based heuristic flags teacher–group interactions using vertical dominance and proximity with 10-second smoothing and a 10-second minimum episode length. An on-premises Mistral large language model classified transcript snippets for question-asking, confusion, need for help, and math talk. (Hur et al. (2026))
- **Two-approach multi-modal learning analytics technique linking behavioral clusters to learning outcomes (Approach A backward, Approach B forward)**: This technique builds behavioral profiles of dyads by clustering teams on multi-modal behaviors (log, video, audio features) and then relating behavioral clusters to learning and performance outcomes. Approach A connects "the learning outcomes back to the behaviors observed during the learning process", while Approach B is "a forward approach as it helps to move from multi-modal behaviors to learning outcomes". Approach B was designed to detect multiple behavioral profiles for the same learning profile, which Approach A's one-cluster-one-profile assumption cannot do; it succeeded where Approach A found no significantly discriminating behavior between its cluster pairs. (Jauwairia Nasir et al. (2021))
- **Five emergent multimodality interaction themes characterize collaborative problem-solving across stages**: The multimodal analysis surfaced five emergent interaction themes showing participants' collaborative patterns in different problem-solving stages and their different strategies. These themes capture how learners orchestrate actions on virtual objects, gestures, body movements, and speech together — for example, action on objects first followed by reasoning through language. The themes are derived from the systematic coding and episode-building of the recorded VR sessions. (Wen Huang et al. (2023))
- **Four types of collaborative learning process data for analyzing individual participation**: The review synthesizes the process data used to analyze individual participation into four categories: oral conversational data (N = 28 studies, mostly co-located), textual input data (N = 18, almost all online), log data from CSCL platforms (N = 20, the most common in online settings), and nonverbal physical data (N = 14) including gestures, eye gazing, touch, and electrodermal activity. Fourteen studies employed multimodal data, most combining oral conversation data and nonverbal physical data, which the review says captured "a more comprehensive view of participation." The mapping of data types to participation forms is summarized in the study's Fig. 3. (Shihui Feng (2025))

### Claims
- [High-experience team teachers show higher voice-quality/spectral-structure and greater loudness-dynamics components than low-experience teachers across spatial pedagogy behavioural categories](../claims/experience-differences-team-teaching-acoustics.md) [+M]
- [Teacher talk differs acoustically by student cohort: undergraduate classes show higher loudness-dynamics components while postgraduate classes show higher spectral-slope and voice-quality components](../claims/cohort-differences-team-teaching-acoustics.md) [+M]
- [Collaborative tasks elicit higher loudness-dynamics components in team-teacher talk than individual tasks, which show higher spectral-slope and voice-quality components](../claims/task-design-differences-team-teaching-acoustics.md) [+M]
- [A DDQN-based attention quantification model trained on multimodal EEG-fNIRS features produces predicted attention levels at one-second temporal resolution](../claims/ddqn-multimodal-attention-quantification-accurate-stable.md) [+M]
- [Among 32 dyads in an open-ended collaborative tabletop task, three behavioral clusters split into two learning (gainer) profiles and one non-learning profile despite similar task performance](../claims/three-multimodal-collaborative-learning-profiles.md) [+M]
- [Speech activity and speech overlap distinguish gainer dyads from non-gainer Silent Wanderers across both gainer profiles](../claims/speech-overlap-distinguishes-gainers-from-non-gainers.md) [+M]
- [The two gainer profiles differ in problem-solving strategy: Expressive Explorers enact global exploration with reflection on past solutions, Calm Tinkerers enact local exploration with in-the-moment correction](../claims/global-versus-local-exploration-strategies-gainers.md) [+M]
- [Calm Tinkerers display significantly lower negative valence and arousal than Silent Wanderers, while Expressive Explorers show high arousal and negative valence similar to Silent Wanderers](../claims/affect-distinguishes-calm-tinkerers-from-silent-wanderers.md) [+M]

## Related Research Methods
-

## Key Sources
- Roschelle, J., Martin, W., Ahn, J. & Schank, P. (Eds.). (2017). Cyberlearning Community Report: The State of Cyberlearning and the Future of Learning With Technology. Menlo Park CA: SRI International. https://digitalpromise.dspacedirect.org/items/dafbe585-c0f8-4693-bde8-a6d847a58aad
- Hur, P., Palaguachi, C., Machaka, N., Krist, C., Dyer, E. B., D'Angelo, C., & Bosch, N. (2026). A Framework for Considering Exploration, Interpretation, and Confirmation During Data Analysis: Computationally Assisted Analysis of Teacher–Group Interactions. Journal of Educational Data Mining, 18(1). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/1030
<!-- merged 2026-10-10 from theories/multimodal-analysis-cyberlearning-method ("Multimodal analysis: studying learning with multiple integrated data streams"), misfiled as a theorie and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.
- Yuchen Liu, Roberto Martinez-Maldonado, Riordan Alfredo, Paola Mejia-Domenzain, Dwi Rahayu, and Sadia Nawaz. (2026). AI-Driven Analytics of Team-Teaching Talk: Acoustic Patterns across Experience, Cohorts and the Learning Design. https://arxiv.org/abs/2606.09831
- Shixian Zhou, Minghuan Shen, Xiaolin Wen, Zijun Qiu, Yongliang Jiang, Xiangyang Wu, Fei Wu, Yong Wang, and Zhiguang Zhou. (2026). SAVVY: Student Attention Visualization for Video-based Learning Analysis. arXiv. https://arxiv.org/abs/2607.29413
- Jauwairia Nasir, Aditi Kothiyal, Barbara Bruno, Pierre Dillenbourg. (2021). Many are the ways to learn identifying multi-modal behavioral profiles of collaborative learning in constructivist activities. Intern. J. Comput.-Support. Collab. Learn (2021) 16:485–523. https://doi.org/10.1007/s11412-021-09358-2
- Wen Huang, Candace Walkington, Mitchell J. Nathan. (2023). Coordinating modalities of mathematical collaboration in shared VR environments. Intern. J. Comput.-Support. Collab. Learn. https://doi.org/10.1007/s11412-023-09397-x
- Shihui Feng, Ziyi Wei. (2025). The CoMPAS Framework for Modeling Individual Participation in Collaborative Learning Processes: a Systematic Review. Intern. J. Comput.-Support. Collab. Learn. https://doi.org/10.1007/s11412-025-09450-x

# Multimodal analysis: studying learning with multiple integrated data streams

> **Theory** · [All theories](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 review), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Multimodal analysis is one of three methodological advances the report highlights, defined as "Integrating multiple streams of data, such as audio, video, eye gaze, sensors, and clickstream data." The introduction elaborates it as "the study of learning with data streams that include physical movement, sound, and logs from interactions with technology (as well as more traditional observations)." The report presents the Connected Worlds exhibit at the New York Hall of Science, which enables embodied learning in an immersive sensor-rich space, as a research site where scientists are pushing the frontiers of multimodal analytics.

## Design Implications

### Context
#### Requirements
- Data collection infrastructure capable of capturing multiple synchronized streams such as movement, sound, and interaction logs
#### Constraints
- The report notes wearable cameras used to capture learning on the move often produce unreliable audio records, odd perspectives, and vast amounts of video data to process

### Target Learners
- museum visitors, children, and multigenerational learner groups

### Target Learning Objectives
- embodied learning, scientific understanding of ecosystems and phenomena

### Claims


## Related Theories

- [Definitional framework of five modalities in MMCA research](../theories/mmca-definitional-framework-five-modalities.md)
- [Analytic agency framework: three stages of data analysis (exploration, interpretation, confirmation), each classified as primarily human-led or computer-led](../theories/analytic-agency-framework-three-stages.md)

## Examples

- [Multimodal pipeline for detecting and analyzing teacher–student group interactions in classroom video](multimodal-analysis.md)
- [Proposed MMLA design for maritime simulation combining body sensors, eye-tracking, and speech recognition](../elements/mmla-design-body-sensors-eye-tracking-speech-recognition-maritime.md)

## Key Sources
- Roschelle, J., Martin, W., Ahn, J. & Schank, P. (Eds.). (2017). Cyberlearning Community Report: The State of Cyberlearning and the Future of Learning With Technology. Menlo Park CA: SRI International. https://digitalpromise.dspacedirect.org/items/dafbe585-c0f8-4693-bde8-a6d847a58aad
-->

<!-- merged 2026-10-17 from research-methods/multimodal-classroom-video-analysis-for-teacherstudent-interaction-detection ("Multimodal classroom-video analysis for teacher–student interaction detection"), thin research-method page folded into the method it is a variant of (maintainer, 2026-10-17): its body as it stood. Its bullets this page lacked were added above.

# Multimodal classroom-video analysis for teacher–student interaction detection

> **Research Method** · [All research methods](index.md)
> **Evidence** · no claims cited

## Description
A computational pipeline combining three modalities from high school mathematics classroom videos: OpenPose pose estimation with Euclidean-distance tracking postprocessing and group boundary boxes, openSMILE eGeMAPS acoustic/prosodic features (88 features), and WhisperX word-level transcripts aligned to detected windows. A pose-based heuristic flags teacher–group interactions using vertical dominance and proximity with 10-second smoothing and a 10-second minimum episode length. An on-premises Mistral large language model classified transcript snippets for question-asking, confusion, need for help, and math talk.

## Accounts
<!- - How each source describes or uses the method - ->
- **Multimodal pipeline for detecting and analyzing teacher–student group interactions in classroom video**: A computational pipeline combining three modalities from high school mathematics classroom videos: OpenPose pose estimation with Euclidean-distance tracking postprocessing and group boundary boxes, openSMILE eGeMAPS acoustic/prosodic features (88 features), and WhisperX word-level transcripts aligned to detected windows. A pose-based heuristic flags teacher–group interactions using vertical dominance and proximity with 10-second smoothing and a 10-second minimum episode length. An on-premises Mistral large language model classified transcript snippets for question-asking, confusion, need for help, and math talk. (Hur et al. (2026))

### Claims

## Related Research Methods
-

## Key Sources
- Hur, P., Palaguachi, C., Machaka, N., Krist, C., Dyer, E. B., D'Angelo, C., & Bosch, N. (2026). A Framework for Considering Exploration, Interpretation, and Confirmation During Data Analysis: Computationally Assisted Analysis of Teacher–Group Interactions. Journal of Educational Data Mining, 18(1). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/1030

<!- - merged 2026-10-10 from elements/multimodal-teacher-group-interaction-pipeline ("Multimodal pipeline for detecting and analyzing teacher–student group interactions in classroom video"), misfiled as a element and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Multimodal pipeline for detecting and analyzing teacher–student group interactions in classroom video

> **Element** · [All elements](index.md)
> **Evidence** · 6 claims (5 for, 1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 6 claims rest on one study

## Description
A computational pipeline combining three modalities from high school mathematics classroom videos: OpenPose pose estimation with Euclidean-distance tracking postprocessing and group boundary boxes, openSMILE eGeMAPS acoustic/prosodic features (88 features), and WhisperX word-level transcripts aligned to detected windows. A pose-based heuristic flags teacher–group interactions using vertical dominance and proximity with 10-second smoothing and a 10-second minimum episode length. An on-premises Mistral large language model classified transcript snippets for question-asking, confusion, need for help, and math talk.

## Design Implications

### Context
#### Requirements
- Videos with sufficient visibility of target groups; group-level audio recorders placed at table centers; groups of at least three students mostly unobscured and discrete from other groups
#### Constraints
- The detector's heuristic assumes teachers stand while students sit; it systematically missed interactions where the teacher stood outside the group boundary box or was visually obscured or crouching

### Target Learners
- High school mathematics students in small groups (data context); education researchers as pipeline users

### Target Learning Goals
- Detecting and analyzing teacher–student group interactions to understand responsive pedagogy

### Affordances
- [Analytic Agency Framework Three Stages](../theories/analytic-agency-framework-three-stages.md)

## Claims


## Related Elements
- 

## Examples
-

## Key Sources
- Hur, P., Palaguachi, C., Machaka, N., Krist, C., Dyer, E. B., D'Angelo, C., & Bosch, N. (2026). A Framework for Considering Exploration, Interpretation, and Confirmation During Data Analysis: Computationally Assisted Analysis of Teacher–Group Interactions. Journal of Educational Data Mining, 18(1). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/1030
- ->
-->
