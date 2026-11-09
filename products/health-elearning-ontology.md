---
type: product
id: health-elearning-ontology
title: Health eLearning ontology
description: An OWL ontology developed by Michalowski Martin et al.
product_kind: framework
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-08
---

# Health eLearning ontology

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
An OWL ontology developed by Michalowski Martin et al. to represent medical concepts, patient learner profiles, and education concepts for personalized patient-course authoring.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Health eLearning ontology expressing domain and learner models for personalized patient courses**: The framework's knowledge representation is an OWL eLearning ontology specified in Protégé, with three top-level classes: Medical_Concept, Patient, and Education_Concept. Medical_Concept subclasses (Condition, Observation, Treatment_Option) follow HL7 FHIR, while Education_Concept stores Condition_Profile, Condition_Fact, and BUK classes. The Patient class carries a comprehension_level property and preferred VARK_learning style(s). The authors state that "The use of an ontology facilities the capture and use of knowledge needed to create courses for the breadth of diseases and learning styles supported by our proposed framework." (Michalowski Martin et al. (2021))
- **Ontological knowledgebases as a machine-understandable representation for patient vaccine education**: The article proposes an explanatory framework in which domain knowledge is represented "in a machine-understandable format, which enables automatic and intelligent queries", making complex vaccination information scalable and query-able while remaining patient-friendly with limited medical jargon. The framework holds that an ontology can serve "as a foundation for an application that will empower patients to make vaccination decisions", powering patient-centered interactive agents such as mobile devices and kiosks that deliver personalized answers via patient-friendly natural language queries, like the VAMATA Siri-like application described for the military setting. (Wang D et al. (2016))

### Claims
- [Patients often rely on Internet sources for vaccine information, and printed VIS materials represent an inactive learning approach that may not produce adequate understanding](../claims/printed-vis-materials-insufficient-inactive-learning.md) [+W]

## Related Products and Programmes
-

## Key Sources
- Michalowski Martin, Wilk Szymon, Michalowski Wojtek, O'Sullivan Dympna, Bonaccio Silvia, Parimbelli Enea, Carrier Marc, Le Gal Grégoire, Kingwell Stephen, Peleg Mor. (2021). A Health eLearning Ontology and Procedural Reasoning Approach for Developing Personalized Courses to Teach Patients about Their Medical Condition and Treatment. International Journal of Environmental Research and Public Health. https://doi.org/10.3390/ijerph18147355
- Wang D, Cunningham R, Boom J, Amith M, Tao C. (2016). Towards a HPV Vaccine Knowledgebase for Patient Education Content. Studies in Health Technology and Informatics. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6677559/
