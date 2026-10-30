---
type: research-method
id: epistemic-network-analysis-ena
moved_from: [element/epistemic-network-analysis-weighted-density]
title: Epistemic network analysis (ENA)
description: Epistemic network analysis (ENA) is a non-parametric analytic method developed for epistemic game data; the article focuses on its social-network based variant.
status: review
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: sweet-2012
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM"
    title: "Sweet, S. J., & Rupp, A. A. (2012). Using the ECD Framework to Support Evidentiary Reasoning in the Context of a Simulation Study for Detecting Learner Differences in Epistemic Games. Journal of Educational Data Mining, Special Issue, Article 5, Volume 4. https://jedm.educationaldatamining.org/index.php/JEDM"
    author: "Sweet, S. J., & Rupp, A. A"
---

# Epistemic network analysis (ENA)

> **Research Method** · [All research methods](index.md)
> **Evidence** · 8 claims (8 for) · 3 studies (1 causal, 1 design, 1 theoretical), `q2`–`q3` · 1 of 3 report an effect size · 8 claims rest on one study

## Description
Epistemic network analysis (ENA) is a non-parametric analytic method developed for epistemic game data; the article focuses on its social-network based variant. Chat utterances are automatically scored into binary indicators of SKIVE element use, aggregated into adjacency and cumulative adjacency matrices across evidentiary segments. The weighted density (WD) statistic summarizes, for each learner, "the total number of unique pair-wise associations / connections between SKIVE elements", and the article evaluates its utility via a simulation study in Land Science.

## Accounts
<!-- How each source describes or uses the method -->
- **Epistemic network analysis and its weighted density statistic for analyzing SKIVE element co-occurrence in epistemic games**: Epistemic network analysis (ENA) is a non-parametric analytic method developed for epistemic game data; the article focuses on its social-network based variant. Chat utterances are automatically scored into binary indicators of SKIVE element use, aggregated into adjacency and cumulative adjacency matrices across evidentiary segments. The weighted density (WD) statistic summarizes, for each learner, "the total number of unique pair-wise associations / connections between SKIVE elements", and the article evaluates its utility via a simulation study in Land Science. (Sweet et al. (2012))
- **ENA network model of problem posing with eleven category and quality codes**: This element is the article’s ENA modeling setup for analyzing students’ cognitive structures during problem posing. Because ENA focuses on associations among semantic units rather than frequency, "only 11 codes from question category (IQ, SC, SL, SR, OD, and CQ) and question quality (R, P , A, E, and C) were retained as network nodes". Lines between nodes represent co-occurrence relationships and line thickness indicates connection strength. Mean networks were constructed for phases and groups, with subtracted networks used to compare conditions, using the online tool epistemicnetwork.org. (Dai et al. (2026))
- **Epistemic Network Analysis reveals temporally ordered patterns in sequentially produced coded data**: The article describes ENA as an extension of bag-of-words text-mining that adds a sliding time "window" so co-occurrences are counted over meaningful parts of text, called "stanzas". Coded data form the nodes of a transition graph with co-occurrences as edges, allowing graph features and network visualization. The article states that "ENA allows the researcher to reveal temporally ordered patterns in sequentially produced data" and that it enabled nuanced condition differences and a better understanding of Simple questions' roles in talk. (Peter Reimann (2021))
- **Epistemic Network Analysis as a methodology for producing quantitative ethnographies of complex learning environments**: Epistemic Network Analysis (ENA) is described as "a methodology for producing quantitative ethnographies based on complex learning environments." The study uses ENA to analyze data collected during a semester of studies in a classroom learning community, applying it to socioemotional facets of learning, which the article notes ENA "has only begun to examine." ENA is positioned as complementary to deep, qualitative ethnography rather than a replacement for it. (Hod et al. (2020))

### Claims
- [In the simulation, task complexity and task difficulty explain the majority of variance in the individual-learner WD statistic, with some effect of task specificity](../claims/task-complexity-and-difficulty-dominate-wd-variance.md) [+W]
- [In simulated epistemic games, the weighted density statistic distinguishes simulated learner types with distinct mastery trajectories, with the expert trajectory showing the largest WD values](../claims/wd-detects-simulated-learner-trajectory-differences.md) [+W]
- [The WD statistic is more useful for differentiating between simulated learner types when games are played longer](../claims/longer-games-sharpen-wd-learner-differentiation.md) [+W]
- [In pairwise WD analyses, learner trajectory similarity dominates variation in percentage-overlap values (57.90% of variation) while remaining design factors are essentially zero](../claims/trajectory-similarity-dominates-wd-pair-overlap.md) [+W]
- [Easy, highly specific simulated tasks compress the range of the WD statistic across learner types, while well-designed tasks widen it](../claims/easy-highly-specific-tasks-shrink-wd-range.md) [+W]
- [Segmentation boundary choices differentially affect statistics computed on epistemic-game process data](../claims/segmentation-boundaries-differentially-affect-statistics.md) [+W]
- [A mirroring dashboard shifts teacher attention toward epistemic over social aspects of learning, while a guiding dashboard divides interventions more equally](../claims/mirroring-versus-guiding-dashboard-attention-balance.md) [+M]
- [Pre-written prompts increase Justifications and Alternative ideas in children's pair-programming talk and shift the role of Simple questions](../claims/prompts-increase-exploratory-talk-elements-pair-programming.md) [+M]

## Related Research Methods
-

## Key Sources
- Sweet, S. J., & Rupp, A. A. (2012). Using the ECD Framework to Support Evidentiary Reasoning in the Context of a Simulation Study for Detecting Learner Differences in Epistemic Games. Journal of Educational Data Mining, Special Issue, Article 5, Volume 4. https://jedm.educationaldatamining.org/index.php/JEDM. [doi:10.5281/zenodo.3554649](https://doi.org/10.5281/zenodo.3554649)
<!-- merged 2026-10-10 from elements/epistemic-network-analysis-weighted-density ("Epistemic network analysis and its weighted density statistic for analyzing SKIVE element co-occurrence in epistemic games"), misfiled as a element and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.
- Dai, Z., Huang, F., Xiong, J., Yang, Y., Zhang, Q., & Peng, X. (2026). Inquiry-based learning in STEM education: the impact of generative AI-based Chatbots on primary school students’ problem posing ability in science. International Journal of STEM Education. https://doi.org/10.1186/s40594-026-00631-0
- Peter Reimann. (2021). Socio-technical configurations for productive talk. Intern. J. Comput.-Support. Collab. Learn (2021) 16:301–306. https://doi.org/10.1007/s11412-021-09354-6
- Hod, Yotam; Eagan, Brendan; Katz, Shir. (2020). Refining qualitative ethnographies using Epistemic Network Analysis: A study of socioemotional learning dimensions in a humanistic knowledge building community. Journal article. https://doi.org/10.1016/j.compedu.2020.103943

# Epistemic network analysis and its weighted density statistic for analyzing SKIVE element co-occurrence in epistemic games

> **Element** · [All elements](index.md)
> **Evidence** · 6 claims (6 for) · 2 studies (1 design, 1 theoretical), `q2` · 1 of 2 report an effect size · 6 claims rest on one study

## Description
Epistemic network analysis (ENA) is a non-parametric analytic method developed for epistemic game data; the article focuses on its social-network based variant. Chat utterances are automatically scored into binary indicators of SKIVE element use, aggregated into adjacency and cumulative adjacency matrices across evidentiary segments. The weighted density (WD) statistic summarizes, for each learner, "the total number of unique pair-wise associations / connections between SKIVE elements", and the article evaluates its utility via a simulation study in Land Science.

## Design Implications

### Context
#### Requirements
- Utterances coded automatically at a fine grain size into binary indicators of SKIVE element use, organized into evidentiary segments
- Adjacency and cumulative adjacency matrices built from the binary codes, from which WD is computed
#### Constraints
- The article notes that for these data "there is currently no prototypical statistical analytic method – certainly no parametric one that we know of – that can be applied directly to these data"

### Target Learners
- individual learners playing epistemic games such as Land Science
- pairs of learners collaborating via group chat

### Target Learning Goals
- characterizing emerging expertise as connections among skills, knowledge, identity, values, and epistemological reasoning elements
- summarizing accumulated evidence of mastery across evidentiary segments

### Claims
<!- - Claims bearing on this element, each a link to a claim page followed by its evidence tag, e.g. [+M] - ->
- [In the simulation, task complexity and task difficulty explain the majority of variance in the individual-learner WD statistic, with some effect of task specificity](../claims/task-complexity-and-difficulty-dominate-wd-variance.md) [+W]
- [In simulated epistemic games, the weighted density statistic distinguishes simulated learner types with distinct mastery trajectories, with the expert trajectory showing the largest WD values](../claims/wd-detects-simulated-learner-trajectory-differences.md) [+W]
- [The WD statistic is more useful for differentiating between simulated learner types when games are played longer](../claims/longer-games-sharpen-wd-learner-differentiation.md) [+W]
- [In pairwise WD analyses, learner trajectory similarity dominates variation in percentage-overlap values (57.90% of variation) while remaining design factors are essentially zero](../claims/trajectory-similarity-dominates-wd-pair-overlap.md) [+W]
- [Easy, highly specific simulated tasks compress the range of the WD statistic across learner types, while well-designed tasks widen it](../claims/easy-highly-specific-tasks-shrink-wd-range.md) [+W]
- [Segmentation boundary choices differentially affect statistics computed on epistemic-game process data](../claims/segmentation-boundaries-differentially-affect-statistics.md) [+W]

## Related Elements

- [Combined tSSNA and ONA method for analyzing collaborative knowledge creation processes](combined-tssna-and-ona-method.md)

## Examples

- [Use the WD statistic during gameplay as a quick screening tool for pairing learners with likely different profiles](../strategies/wd-gameplay-screening-for-learner-pairing.md)

## Key Sources
- Sweet, S. J., & Rupp, A. A. (2012). Using the ECD Framework to Support Evidentiary Reasoning in the Context of a Simulation Study for Detecting Learner Differences in Epistemic Games. Journal of Educational Data Mining, Special Issue, Article 5, Volume 4. https://jedm.educationaldatamining.org/index.php/JEDM. [doi:10.5281/zenodo.3554649](https://doi.org/10.5281/zenodo.3554649)
-->
