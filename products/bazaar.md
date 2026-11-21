---
type: product
id: bazaar
title: Bazaar
description: "Bazaar is Adamson et al.'s modular architecture for composing and integrating domain-independent collaboration-support agents into learning environments."
product_kind: framework
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-27
---

# Bazaar

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Bazaar is Adamson et al.'s modular architecture for composing and integrating domain-independent collaboration-support agents into learning environments.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Bazaar Collaborative Reflection: agent-supported synchronous chat in a MOOC**: Bazaar Collaborative Reflection makes synchronous collaboration opportunities available to students in a MOOC context, importing agent-supported collaborative learning technology in which "conversational computer agents can serve as effective automated facilitators of synchronous collaborative learning". A Lobby program matches waiting students with a random conversational partner; matched pairs receive a link to a chat room where they interact with each other and with a conversational agent appearing as a regular user. (Carolyn Penstein Rosé et al. (2016))
- **Bazaar's distributed listener-actor-output-coordinator architecture for dynamic collaboration support**: Bazaar manages the complexity of supporting collaborative groups by distributing support across multiple specialized agents. As the article puts it, the architecture works "by distributing the task of listening for particular events in the collaboration and injecting support of various kinds across multiple specialized agents operating collaboratively in the background". Listeners detect events (rule-based or machine-learned) and place them on a queue; actors propose templated responses with priority and timeout values; an output coordinator selects which response, if any, to emit based on the micro and macro state of the activity and chat. LLM Bazaar extends this by adding LLM agents as listeners and actors. (Wu et al. (2025))
- **LLM Bazaar: an open-source extension integrating customizable LLM agents into the Bazaar collaboration support architecture**: LLM Bazaar is an extension to the open-source Bazaar platform that adds LLM agents as listeners and actors within multi-party collaborative learning sessions. The article states its key advancement is "integration of any number of customizable LLM agents with context-aware interaction support". Plain text configuration files specify LLM parameters (model, URL, API key, temperature, context length) and personalization parameters such as persona, interest areas, and conversational style. Code, an illustrative activity, and support instructions are released on GitHub. (Wu et al. (2025))

### Claims
- [Participation in Bazaar synchronous chat sessions is associated with roughly a 50 percent lower risk of dropout in an edX MOOC](../claims/chat-participation-halves-dropout-risk.md) [+M]

## Related Products and Programmes

- [MentorChat](mentorchat.md)
- [MALA (Modular Artificial Learning Assistance)](mala-modular-artificial-learning-assistance.md)

## Key Sources
- Rohit Kumar & Jihie Kim. (2013). Special Issue on Intelligent Support for Learning in Groups. International Journal of Artificial Intelligence in Education, 24. https://doi.org/10.1007/s40593-013-0013-5
- Carolyn Penstein Rosé & Oliver Ferschke. (2016). Technology Support for Discussion Based Learning: From Computer Supported Collaborative Learning to the Future of Massive Open Online Courses. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-016-0107-y
- Adamson, D., Dyke, G., Jang, H., & Rosé, C. P. (2014). Towards an Agile Approach to Adapting Dynamic Collaboration Support to Student Needs. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-013-0012-6
- Wu, Z., Shi, J., Murray, R. C., Rosé, C., & San Andres, M. (2025). LLM Bazaar: A Service Design for Supporting Collaborative Learning with an LLM-Powered Multi-Party Collaboration Infrastructure. CSCL 2025 Proceedings. http://bit.ly/4leDl0U. [doi:10.48550/arxiv.2510.18877](https://doi.org/10.48550/arxiv.2510.18877)
