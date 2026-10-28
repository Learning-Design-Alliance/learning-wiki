---
type: product
id: fieldtriporganizer
title: FieldTripOrganizer
description: FieldTripOrganizer is a web-based, mobile-accessible application developed to help teachers filter educational points of interest and activities and construct time-constrained field-trip itineraries.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-28
---

# FieldTripOrganizer

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
FieldTripOrganizer is a web-based, mobile-accessible application developed to help teachers filter educational points of interest and activities and construct time-constrained field-trip itineraries.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **FieldTripOrganizer web application for teacher-led field trip planning**: FieldTripOrganizer is a web-based, mobile-accessible application that helps teachers design custom field trips by filtering Points of Interest and activities by geographical area, domain of interest, school level, and type, and by incrementally building an itinerary. The article proposes "a field trip planner based on the mixed-initiative approach aimed at increasing teachers' autonomy and motivation in designing educational tours". While the user designs the trip, the application keeps the spare time visible, invokes the VROOM solver to re-estimate the optimal schedule after each addition or removal, and graphically annotates items with a green or red semaphore indicating whether they fit the time constraints. It was instantiated on science field trips in the Ivrea area of Piedmont, Italy, and evaluated with 18 science teachers. (Noemi Mauro et al. (2024))
- **Generic ontology-based domain data model for places, activities, and objects**: FieldTripOrganizer's domain knowledge is expressed as an OWL ontology (Fig. 1) stored in the Omeka-S content management system, which domain experts populate at setup time. The model defines "Items" representing places (PoIs), activities, or objects, related through is-a, use_in, and is_in relations, so that a PoI can aggregate one or more activities — unlike the atomic elements of typical tourist applications. Activities carry attributes for school levels (difficulty), type (laboratory or outdoors), and setup time (10 minutes by default). The generic data model abstracts from entity details and specifies only "Domains of interest", making the application suitable for tours on different topics such as science and arts. (Noemi Mauro et al. (2024))

### Claims
- [In a user study with 18 science teachers, FieldTripOrganizer was rated more usable than the Klarna.Trips baseline tour planner](../claims/fieldtriporganizer-higher-usability-than-baseline.md) [+M]
- [Teachers rated FieldTripOrganizer higher than Klarna.Trips on support, autonomy, anxiety reduction, and motivation during field trip planning](../claims/fieldtriporganizer-support-autonomy-anxiety-motivation.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Noemi Mauro, Liliana Ardissono, Federica Cena, Livio Scarpinati, Gianluca Torta. (2024). An Intelligent Support System to Help Teachers Plan Field Trips. Int J Artif Intell Educ 34, 793–824. https://doi.org/10.1007/s40593-023-00366-x
