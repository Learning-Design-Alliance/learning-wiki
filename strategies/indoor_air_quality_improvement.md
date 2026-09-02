---
type: strategy
id: indoor_air_quality_improvement
title: Indoor Air Quality Improvement
description: Improving indoor air quality reduces absenteeism, particularly for students with asthma, and addresses "sick building syndrome." Proper ventilation systems and pollutant reduction create a healthier learning environment.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Indoor Air Quality Improvement

> **Strategy** · [All strategies](index.md)

## Description
Indoor air quality (IAQ) improvement addresses the physical learning environment by increasing outdoor-air ventilation, upgrading filtration, and removing or controlling pollutant sources (cleaning products, building materials, mold, combustion byproducts). It is carried out through facility management (HVAC maintenance and commissioning, CO₂ monitoring), source control policies, and portable air purification where central systems are inadequate.

## Design Implications

Learning depends on a physical environment that supports sustained attention and attendance; poor IAQ is consistently associated with higher absenteeism, respiratory symptoms, and degraded performance on attention-demanding tasks [~M]. Because these effects are strongest for students with asthma and other respiratory conditions, IAQ improvement functions as an equity intervention as much as a general health measure. Unlike most instructional strategies, its "effect" operates by removing an environmental impediment rather than adding a learning mechanism — the design goal is keeping cognitive resources available for learning rather than coping with discomfort.

### Context
#### Requirements
- Adequate outdoor-air ventilation (commonly benchmarked against CO₂ concentrations below ~1,000 ppm in occupied classrooms)
- Functioning, regularly maintained HVAC systems with appropriate filtration (e.g., MERV-13 where feasible)
- Source-control policies: low-emission cleaning products, integrated pest management, prompt mold remediation, no-idling policies near air intakes
- Monitoring (CO₂ sensors, humidity, temperature) to verify conditions rather than assume them

#### Constraints
- Retrofit costs can be substantial, and older buildings may lack ductwork capacity for increased outdoor air [-W]
- Benefits accrue slowly and diffusely (attendance, health), making them hard to attribute and easy to deprioritize in budget decisions [-W]
- Portable air cleaners only help if sized correctly for the room and filters are replaced; poorly maintained units can generate noise that interferes with instruction [~W]
- Increased outdoor-air intake raises heating and cooling energy costs, creating an operating-budget tension that can quietly reverse gains [-W]

#### Implementation Variability
- Full HVAC replacement vs. incremental measures (filter upgrades, portable HEPA units, window operation where outdoor air is acceptable)
- Policy-level approaches (district IAQ management plans) vs. classroom-level measures (plants do not meaningfully clean air; source control and ventilation do)
- Seasonal adaptation: natural ventilation in mild weather, filtration-dominant strategies during wildfire smoke events or high outdoor pollution

### Target Learners
- Students with asthma or allergies, who show the largest attendance and symptom improvements when classroom air quality improves [~M]
- Younger children, who breathe more air per body weight and are more susceptible to pollutant exposure [~W]
- All occupants of high-density classrooms, where CO₂ and bioeffluent concentrations rise fastest

### Target Learning Goals
- Not a learning goal in itself — this strategy serves *conditions for learning*: attendance, sustained attention, and working-memory capacity during instruction
- Indirectly supports every goal that depends on consistent presence and focused cognition, including [spaced practice](../claims/spaced-repetition-improves-retention.md) schedules that break down when attendance is erratic

### Instructions
1. **Assess baseline conditions.** Measure CO₂, humidity, and temperature in occupied classrooms; identify pollutant sources and ventilation shortfalls.
2. **Control sources first.** Substitute low-emission cleaning and art materials, remediate moisture and mold, and enforce no-idling zones near intakes — source control is usually cheaper than dilution.
3. **Increase ventilation and filtration.** Commission HVAC systems to deliver design outdoor airflow; upgrade filters; add portable HEPA units in under-ventilated rooms.
4. **Monitor continuously.** Use inexpensive CO₂ sensors as a proxy for ventilation adequacy and set alert thresholds for staff.
5. **Integrate with other environmental strategies.** Pair with [Acoustics and Noise Management](acoustics_and_noise_management.md), since ventilation upgrades and noise control often interact (fans and open windows add noise).
6. **Evaluate.** Track attendance (especially asthma-related absences), nurse visits, and occupant surveys before and after interventions.

## Related Strategies
- [Acoustics and Noise Management](acoustics_and_noise_management.md) — the other major physical-environment lever; ventilation changes often alter classroom noise levels
- [Check-ins](../principles/check-ins.md) — brief student check-ins surface discomfort symptoms (headaches, drowsiness) that signal IAQ problems before sensors do

## Examples
- **[EPA Indoor Air Quality Tools for Schools](https://www.epa.gov/iaq-schools)** — a widely adopted, free framework that K-12 districts use to establish IAQ management teams, checklists, and monitoring routines.
- **Post-COVID ventilation upgrades** — many districts (e.g., through federal ESSER funding) installed portable HEPA units and upgraded MERV filters; studies of these deployments reinforced the link between classroom ventilation and reduced infection-related absenteeism.
- **Berkeley Unified School District** — an example of a district-level IAQ management program using the EPA Tools for Schools framework with documented reductions in reported respiratory complaints.

## Key Sources
- Mendell, M. J., & Heath, G. A. (2005). Do indoor pollutants and thermal conditions in school classrooms influence student performance? A critical review of the literature. *Indoor Air, 15*(1), 27–52. [doi:10.1111/j.1600-0668.2004.00320.x](https://doi.org/10.1111/j.1600-0668.2004.00320.x)
- Fisk, W. J. (2002). Health and productivity gains from better indoor environments and their relationship with building energy efficiency. *Annual Review of Energy and the Environment, 27*, 537–566. [doi:10.1111/j.1600-0668.1997.t01-1-00002.x](https://doi.org/10.1111/j.1600-0668.1997.t01-1-00002.x)
- Wargocki, P., & Wyon, D. P. (2013). Providing better thermal and air quality conditions in school classrooms would be cost-effective. *Building and Environment, 59*, 581–589. [doi:10.1016/j.buildenv.2012.10.007](https://doi.org/10.1016/j.buildenv.2012.10.007)
- Haverinen-Shaughnessy, U., Moschandreas, D. J., & Shaughnessy, R. J. (2011). Association between substandard classroom ventilation rates and students' academic achievement. *Indoor Air, 21*(2), 121–131. [doi:10.1111/j.1600-0668.2010.00686.x](https://doi.org/10.1111/j.1600-0668.2010.00686.x)