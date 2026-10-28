---
type: claim
title: AI-generated assessment items frequently need faculty correction, supporting AI as a draft generator within quality assurance
description: AI-generated assessment items frequently need faculty correction, supporting AI as a draft generator within quality assurance
id: genai-assessment-items-draft-generator-quality-assurance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-10-27
recheck_by: 2029
sources:
  - id: zhao-j-2026
    resource: "https://doi.org/10.3389/feduc.2026.1907589"
    title: "Zhao J, Yang K, Gao H and Jiang G (2026). Generative artificial intelligence and the transformation of medical education: a scoping review. Front. Educ. 11:1907589. https://doi.org/10.3389/feduc.2026.1907589"
    author: Zhao J, Yang K, Gao H and Jiang G
    q: 2
    i: "?"
    kind: review
    rigour: 3
  - id: zhao-j-2026-2
    resource: "https://doi.org/10.3389/feduc.2026.1907589"
    title: "Zhao J, Yang K, Gao H and Jiang G (2026). Generative artificial intelligence and the transformation of medical education: a scoping review. Front. Educ. 11:1907589. https://doi.org/10.3389/feduc.2026.1907589"
    author: Zhao J, Yang K, Gao H and Jiang G
    q: 2
    i: "?"
    kind: review
    rigour: 2
---

# AI-generated assessment items frequently need faculty correction, supporting AI as a draft generator within quality assurance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · review `r2`–`r3` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-27 (automated, 2 of 2 entries) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Only 9 of 40 ChatGPT physiology items met all ideal criteria compared with 19 of 40 faculty items. [→ Zhao J 2026](#zhao-j-2026)
`q2 i?` AI item generation reduced authoring time and sometimes produced difficulty and discrimination comparable with human items, but incorrect keys, nonfunctional distractors, and poor discrimination required faculty correction. [→ Zhao J 2026 (2)](#zhao-j-2026-2)

## Evidence

### Zhao J 2026

Zhao J, Yang K, Gao H and Jiang G (2026). Generative artificial intelligence and the transformation of medical education: a scoping review. Front. Educ. 11:1907589. https://doi.org/10.3389/feduc.2026.1907589

`q2 · i?` · `review · r3`

The review reports this psychometric comparison from Chauhan et al. within the 22-report assessment category as evidence of inconsistent AI item performance.

> "For example, only 9 of 40 ChatGPT physiology items met all ideal criteria compared with 19 of 40 faculty items (Chauhan et al., 2025)."

### Zhao J 2026 (2)

Zhao J, Yang K, Gao H and Jiang G (2026). Generative artificial intelligence and the transformation of medical education: a scoping review. Front. Educ. 11:1907589. https://doi.org/10.3389/feduc.2026.1907589

`q2 · i?` · `review · r2`

The review reports these positive signals alongside settings where incorrect keys, multiple defensible answers, nonfunctional distractors, and mismatched cognitive levels required faculty correction.

> "AI item generation reduced authoring time and sometimes produced difficulty and discrimination comparable with human items (Al-Najafi et al., 2026; Wu et al., 2026)."

## Studies bearing on this claim

<!-- synthesis:start -->
*Can a language model write usable multiple-choice items and distractors, or do its drafts need human review?* This table gathers the studies behind this claim and the 17 narrower claims that bear on it: **8 distinct studies** (3 design, 2 associational, 1 review, 1 qualitative, 1 causal), `q2`–`q3`, 0 of 8 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Zhao J 2026](https://doi.org/10.3389/feduc.2026.1907589) | q2 · review · r3 | i? | this claim |
| [Xiaojing Duan 2026](https://doi.org/10.48550/arxiv.2604.03926) | q2 · design · r2 | i? | [Distractor quality is the weakest automated dimension, with the lowest success rate (79.9%](code-gen-distractor-quality-weakest-dimension.md) (supports) |
| [math-output](https://doi.org/10.51388/20.500.12265/232) | q2 · qualitative · r? | i? | [AI pilots found models not yet capable of high-quality math output generation, including m](ai-not-capable-math-output-generation.md) (supports) |
| [Eamon Worden 2026](https://doi.org/10.48550/arxiv.2602.00070) | q2 · design · r2 | i? | [LLMs predict common distractors above chance but fall 15 percentage points below chance at](llm-distractor-prediction-asymmetry.md) (supports) |
| [Yuan An 2026](https://doi.org/10.48550/arxiv.2609.27063) | q2 · associational · r2 | i? | [LLM-assigned difficulty labels fail to predict empirical item difficulty in classroom retr](llm-difficulty-labels-fail-to-predict-empirical-item-difficulty.md) (supports); [LLM-generated retrieval practice was practical to deploy and well received, but high corre](llm-generated-retrieval-practice-deployable-but-high-accuracy-limits-variance.md) (qualifies) |
| [Vogt P 2026](https://doi.org/10.1186/s12909-026-10410-8) | q3 · associational · r1 | i? | [Students identified MCQ item source at a rate significantly above the 50% chance level in ](students-identify-mcq-source-above-chance.md) (supports); [Exploratory analysis found item difficulty differed across sources, driven by the Google G](item-difficulty-differs-across-sources-gemini-nle.md) (qualifies); [Distractor distribution did not differ across ChatGPT, Google Gemini and NLE MCQs](distractor-distribution-does-not-differ-across-sources.md) (counts against); [Student-perceived curricular alignment did not differ between AI and NLE MCQs or among Cha](perceived-alignment-does-not-differ-ai-vs-nle.md) (counts against); [Students' recognition did not differ between AI-generated and NLE MCQs](recognition-does-not-differ-ai-vs-nle.md) (counts against) |
| [human-answers-1](https://doi.org/10.1145/3785022.3785100) | q2 / q3 · design · r2 | i? | [MCQs generated by the generate-then-validate SLM pipeline are generally answerable and una](slm-generated-mcqs-answerable-unambiguous-human-judges.md) (counts against); [Phi-2's answers to its own generated MCQs align with human experts at least as strongly as](phi2-answers-align-with-human-experts.md) (qualifies); [Raising the answer-confidence threshold reduces the number of retained MCQs but substantia](answer-confidence-threshold-trades-quantity-for-quality.md) (qualifies); [Judging learning-objective alignment of generated MCQs is more subjective than answering t](lo-alignment-judgment-more-subjective-than-answering.md) (qualifies) |
| [Yanick Zengaffinen 2026](https://doi.org/10.48550/arxiv.2603.15547) | q2 · causal · r2 | i? | [Chain-of-thought and reasoning prompting significantly improve LLM proportional match with](reasoning-prompting-improves-llm-distractor-match.md) (qualifies); [Providing the correct solution in the prompt improves LLM alignment with human-authored di](correct-solution-in-prompt-bottleneck.md) (qualifies); [Candidate selection is a second bottleneck: an oracle ranker over proposed candidates subs](candidate-selection-loss-oracle-ranker.md) (qualifies) |
<!-- synthesis:end -->

## Discussion


## Related Claims
- [Students' main AI challenges are content reliability and depth, and most expect AI to serve as tutor, creative partner, and critical thinking partner rather than mere content generator](student-critical-ai-role-expectations.md) — related
- [Educators use AI tools mainly for personalized learning and language support and frequently use generative AI for lesson planning](educators-ai-use-personalization-lesson-planning.md) — related
- [75% of student-authored physics questions met combined high-quality criteria (clear, correct, plausible distractors, above recall, adequate explanation)](peerwise-student-questions-75-percent-high-quality.md) — related
- Benchmark items showed high mean difficulty and low item discrimination, with many trivial items and only one broken item — related
- [AI pilots found models not yet capable of high-quality math output generation, including multiple choice problems, coherent word problems, and math visuals](ai-not-capable-math-output-generation.md) — related
- [PeerWise student ratings of multiple-choice questions correlate well with instructor ratings (0.5 and 0.58)](peerwise-student-ratings-correlate-instructor-ratings.md) — related
- [Judging learning-objective alignment of generated MCQs is more subjective than answering them, with only moderate human agreement](lo-alignment-judgment-more-subjective-than-answering.md) — related
- [Faculty-generated SBMCQs met all three ideal item-analysis criteria more often than ChatGPT-generated SBMCQs (19 vs. 9 of 40)](faculty-sbmcqs-outperform-chatgpt-ideal-criteria.md) — possibly the same claim (merge candidate)
- [Faculty-generated SBMCQs showed superior discrimination indices and distractor effectiveness compared with ChatGPT-generated SBMCQs](faculty-sbmcqs-superior-discrimination.md) — related
- [Math and science are well-structured domains whose formal tasks make them favorable application areas for AIED technology](well-structured-domains-favor-aied.md) — related
