---
type: strategy
id: maintain_optimal_classroom_temperature
title: Maintain Optimal Classroom Temperature
description: Keeping classroom temperature within a moderate comfort range (roughly 68–74°F / 20–23°C) protects attention, working memory, and task engagement.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Maintain Optimal Classroom Temperature

> **Strategy** · [All strategies](index.md)

## Description
Thermal comfort is a physical precondition for learning: rooms that are too hot or too cold divert physiological and attentional resources away from the task at hand. Field studies in schools show that learning performance on tasks requiring concentration (reading speed, comprehension, arithmetic) declines measurably as classroom temperature rises above roughly 23–24°C, with each degree of excess heat imposing a small but consistent cost [Wargocki & Wyon's school field experiments link reduced classroom temperature to improved learning task performance.](https://doi.org/10.1080/09613210308668851) [+S]. The strategy is carried out by giving teachers or building operators the ability to monitor and adjust temperature at the classroom level, and by treating thermal comfort as part of routine instructional setup rather than facilities management alone.

## Design Implications

Thermal discomfort functions as extraneous cognitive load: the body's effort to regulate temperature competes with working memory resources needed for learning [Cognitive load theory distinguishes intrinsic, extraneous, and germane load; environmental distraction is a classic extraneous source.](../principles/cognitive-load-management.md) [+M]. Because the effect is dose-dependent and continuous, the design goal is not a single "perfect" number but keeping rooms inside a comfort band and preventing the upper tail (hot, stuffy rooms) where performance losses are steepest.

### Context
#### Requirements
- Classroom-level temperature monitoring (thermometers or sensors teachers can actually see)
- A mechanism for adjustment — operable windows, thermostats, or responsive building management — at the classroom or small-block level
- Ventilation to accompany cooling; temperature and air quality interact, and CO₂ buildup independently degrades decision performance [Classroom ventilation and air quality affect learning outcomes.](https://doi.org/10.1111/j.1600-0668.2006.00427.x) [+M]
- Awareness among staff that comfort complaints are instructional data, not noise

#### Constraints
- Individual thermal preferences vary by body size, clothing, metabolism, and acclimatization; no single setpoint satisfies everyone, so a rigid district-wide standard can create discomfort for some students even at the "correct" temperature [-M]
- Retrofitting HVAC for classroom-level control is costly, and many legacy buildings give teachers no local control at all [-M]
- Overcooling is a real failure mode: cold rooms increase discomfort and reduce fine-motor performance and self-reported comfort, with some evidence of performance costs below ~20°C [~M]
- Effects on complex, high-interest tasks are smaller than on routine speed-and-accuracy tasks; a warm room will not sink a highly engaging activity, but it will tax sustained attention during drill and assessment [~M]

#### Implementation Variability
- Low-cost: portable thermometers, scheduled ventilation, fan use, dress-code flexibility, relocating activities to cooler rooms during heat events
- Mid-cost: zoned thermostats for classroom blocks with teacher override authority
- Systems-level: building management systems with per-room sensors and automated setpoints tied to occupancy schedules

### Target Learners
- All learners benefit from the comfort band, but the largest measured effects are on school-age children in reading and mathematics tasks during warm-season instruction [+S]
- Younger children are more vulnerable: they thermoregulate less efficiently and are less likely to report discomfort or act on it
- Students with certain disabilities or medications that impair thermoregulation need particular attention

### Target Learning Goals
- Any goal requiring sustained attention and working memory: reading fluency, computation, extended writing, assessment performance
- Not specific to a content domain — this is an enabling condition rather than a pedagogical technique

### Instructions
1. Measure: place a visible thermometer or sensor in the instructional space; record readings at the start of key activities.
2. Set a target band (approximately 68–74°F / 20–23°C) and identify who can adjust what, and how quickly.
3. Pair temperature management with [Acoustics and Noise Management](acoustics_and_noise_management.md) — both are environmental load reducers best handled as a single "learning environment" routine.
4. Treat complaints as data: survey students on comfort and cross-check against sensor readings, since perceived comfort predicts performance effects better than the thermostat number alone.
5. During heat events, shift high-load activities (tests, dense reading) to cooler times of day or cooler rooms rather than pushing through.

## Related Strategies
- [Acoustics and Noise Management](acoustics_and_noise_management.md) — the parallel environmental-load strategy; noise and heat both consume attention nonproductively
- [Chunking](../principles/chunking.md) — reduces intrinsic processing demands; environmental management reduces extraneous demands, and the two compound

## Examples
- **Wargocki & Wyon's school field studies (Denmark/Sweden)** — classroom intervention studies in which lowering temperature from ~25°C to ~20°C and improving ventilation produced significant gains in speed and accuracy on reading and numerical tasks.
- **Heat and learning at scale (Goodman et al., 2018)** — analysis of U.S. exam data showing that each 1°F hotter school year reduces learning, with air conditioning substantially offsetting the effect, implying large equity gaps between hot and cool school buildings.
- **Practical low-cost case** — a teacher without thermostat access uses a $10 thermometer, cross-ventilation before class, fans, and a seating plan that moves heat-sensitive students away from sunlit windows.

## Key Sources
- Wargocki, P., & Wyon, D. P. (2007). The effects of moderately raised classroom temperatures and classroom ventilation rate on the performance of schoolwork by children. *HVAC&R Research, 13*(2), 193-220. [doi:10.1080/10789669.2007.10390951](https://doi.org/10.1080/10789669.2007.10390951)
- Wargocki, P., & Wyon, D. P. (2013). Providing better thermal and air quality conditions in school classrooms would be cost-effective. *Building and Environment, 64*, 139–153. [doi:10.1016/j.buildenv.2012.10.007](https://doi.org/10.1016/j.buildenv.2012.10.007)
- Goodman, J., Hurwitz, M., Park, J., & Smith, J. (2020). Heat and learning. *American Economic Journal: Economic Policy, 12*(2), 306–339. [doi:10.1257/pol.20180612](https://doi.org/10.1257/pol.20180612)
- Cedeño Laurent, J. G., et al. (2018). Reduced cognitive function during a heat wave among residents of non-air-conditioned buildings. *PLOS Medicine, 15*(7), e1002605. [doi:10.1371/journal.pmed.1002605](https://doi.org/10.1371/journal.pmed.1002605)
- Seppänen, O., Fisk, W. J., & Lei, Q. H. (2006). Ventilation and performance in office work. *Indoor Air, 16*(6), 465–480. [doi:10.1111/j.1600-0668.2006.00447.x](https://doi.org/10.1111/j.1600-0668.2006.00447.x)