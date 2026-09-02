---
type: strategy
id: temperature_control
title: Temperature Control
description: Maintaining classroom temperatures within a moderate comfort range (roughly 68–74°F / 20–23°C) to protect attention, working memory, and engagement.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Temperature Control

> **Strategy** · [All strategies](index.md)

## Description
Temperature control is the deliberate regulation of ambient thermal conditions in learning environments to keep them within a moderate comfort range — roughly 68–74°F (20–23°C) for typical sedentary classroom activity. It is carried out through HVAC management, monitoring, and responsive adjustment, treating thermal comfort as an instructional precondition rather than a facilities afterthought.

## Design Implications

Thermal conditions measurably affect cognitive performance: performance on learning and office tasks declines as temperatures move above the low-to-mid 70s°F, with losses of roughly 2% per °C above ~25°C [Seppänen & Fisk's quantitative review links elevated temperatures to reduced work performance.](https://doi.org/10.1080/10789669.2006.10391208) [+M]. Field studies in schools show that improving thermal and air quality conditions produces reliable gains in learning-relevant task performance [Wargocki & Wyon's school intervention studies.](https://doi.org/10.1016/j.buildenv.2013.01.017) [+S], and even moderate heat exposure during heat waves degrades cognitive function in occupants of non-air-conditioned buildings [Cedeño Laurent et al. heat-wave study.](https://doi.org/10.1371/journal.pmed.1002605) [+S]. Temperature control is best treated as one component of a broader environmental-quality strategy alongside ventilation and lighting.

### Context
#### Requirements
- A means of measuring actual classroom temperature (thermostat readings often diverge from conditions at student desks)
- Heating/cooling capacity that can hold the target range across seasons and occupancy levels
- Attention to interacting factors — ventilation and CO₂ levels compound thermal effects on cognition [Allen et al. cognitive function study.](https://doi.org/10.1289/ehp.1510037) [+S]
- A mechanism for gathering learner comfort feedback, since individual comfort varies

#### Constraints
- Overcooling is as harmful as overheating: performance drops when temperatures fall below the comfort range, and cold-induced distraction competes for attentional resources [~M]
- Individual thermal comfort varies by clothing, metabolism, and acclimatization; a single setpoint will leave some learners uncomfortable regardless of where it is set [~W]
- Older buildings without adequate HVAC may be unable to hold the target range during heat waves, making schedule adjustments (moving high-cognitive-load tasks to cooler parts of the day) the only viable mitigation [~M]
- Thermal effects are smaller than instructional-quality effects; temperature control cannot compensate for poor teaching [-W]

#### Implementation Variability
- Passive strategies: shading, ventilation timing, dress-code flexibility, and scheduling demanding work during cooler hours
- Active strategies: programmable HVAC setpoints, portable units, and zoned controls
- Learner agency: allowing students to adjust layers or relocate within the room rather than fixing one room-wide temperature

### Target Learners
- Children and adolescents, who are more sensitive to elevated classroom temperatures than adults in task performance studies [Wargocki & Wyon's school intervention studies.](https://doi.org/10.1016/j.buildenv.2013.01.017) [+S]
- Learners in buildings without air conditioning during warm periods, who show measurable cognitive decrements [Cedeño Laurent et al. heat-wave study.](https://doi.org/10.1371/journal.pmed.1002605) [+S]
- Learners with attention difficulties, who are disproportionately affected by environmental distraction and discomfort [~W]

### Target Learning Goals
- Any goal requiring sustained attention or working memory — the cognitive functions most degraded by thermal discomfort
- High-stakes assessment performance, where environmental conditions should not add noise to measurement
- Complex problem-solving tasks, which are more temperature-sensitive than simple or routine tasks [~M]

### Instructions
1. Establish a baseline: measure temperature at student level during typical instructional hours, not just at the thermostat.
2. Set and maintain the target range (68–74°F / 20–23°C), adjusting seasonally for clothing norms.
3. Pair temperature control with ventilation management, since CO₂ buildup independently degrades cognition [Allen et al. cognitive function study.](https://doi.org/10.1289/ehp.1510037) [+S].
4. Schedule cognitively demanding activities ([Assessment](../elements/assessment.md), [Practice](../elements/practice.md)) during the coolest parts of the day when full control is not possible.
5. Use brief [Check-Ins](../elements/check-in.md) to surface thermal discomfort and adjust within available means (open windows, fan direction, seating changes).

## Related Strategies
- Acoustics and noise management — the other major physical-environment factor competing for attentional resources
- Accommodating processing speed challenges — thermal discomfort slows response times, compounding processing-speed difficulties

## Examples
- **School HVAC intervention studies (Denmark)** — Wargocki and Wyon's field experiments improved classroom ventilation and temperature and documented significant gains in children's performance on speed and accuracy tasks ([Building and Environment](https://doi.org/10.1016/j.buildenv.2013.01.017)).
- **Heat-wave natural experiment (Boston area)** — College students living in non-air-conditioned dormitories during a 2016 heat wave performed ~13% slower on cognitive tests than peers in air-conditioned buildings ([PLoS Medicine](https://doi.org/10.1371/journal.pmed.1002605)).
- **COGfx study (Syracuse University / Harvard)** — Controlled exposure studies showing cognitive function scores decline sharply as CO₂ rises, motivating combined temperature-and-ventilation management ([Environmental Health Perspectives](https://doi.org/10.1289/ehp.1510037)).

## Key Sources
- Wargocki, P., & Wyon, D. P. (2013). Providing better thermal and air quality conditions in school classrooms would be cost-effective. *Building and Environment, 59*, 581–589. [doi:10.1016/j.buildenv.2012.10.007](https://doi.org/10.1016/j.buildenv.2012.10.007)
- Cedeño Laurent, J. G., et al. (2018). Reduced cognitive function during a heat wave among residents of non-air-conditioned buildings. *PLoS Medicine, 15*(7), e1002605. [doi:10.1371/journal.pmed.1002605](https://doi.org/10.1371/journal.pmed.1002605)
- Allen, J. G., et al. (2016). Associations of cognitive function scores with carbon dioxide, ventilation, and volatile organic compound exposures in office workers. *Environmental Health Perspectives, 124*(6), 805–812. [doi:10.1289/ehp.1510037](https://doi.org/10.1289/ehp.1510037)
- Seppänen, O., & Fisk, W. J. (2006). Some quantitative relations between indoor environmental quality and work performance or health. *HVAC&R Research, 12*(3), 623–636. [doi:10.1080/10789669.2006.10391208](https://doi.org/10.1080/10789669.2006.10391208)