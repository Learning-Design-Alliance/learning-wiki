---
type: element
id: constructed-response-assessment-items
title: Constructed-Response Assessment Items
description: Completion, short-answer, and extended-response (essay) items ask students to recall and produce an answer rather than recognize one, reducing guessing but introducing a genuine scoring-reliability problem that model answers, sample-reading, and rubrics are all meant to address.
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-08-29
---

# Constructed-Response Assessment Items

> **Element** · [All elements](index.md)
> **Evidence** · 87 claims (27 for, 58 mixed, 2 against) · 65 studies (22 design, 15 associational, 12 causal, 11 review, 2 quant-synthesis, 2 theoretical, 1 qualitative), `q1`–`q4` · 10 of 65 report an effect size · 87 claims rest on one study

## Description
Constructed-response items ask students to recall information and produce their own answer rather than recognize a provided one, which reduces guessing compared with [selected-response items](selected-response-assessment-items.md). Two major kinds are used: **completion/short-answer** items (answerable in a word, phrase, number, or symbol — the same underlying format whether phrased as a statement to complete or a question to answer) and **extended-response** items (answers ranging from a paragraph to several pages, often called essay questions when they run long).

Completion and short-answer items are easy to construct and are sometimes called "objective" on the assumption that only one answer is correct — but unless a question is phrased very precisely, multiple genuinely correct answers often exist ("Where was President Lincoln born?" can correctly be answered "in a log cabin," "on Sinking Spring Farm," "in Hardin County," or "in Kentucky"), which undercuts that objectivity in practice. Common errors: more than one defensibly correct answer; too many blanks in one item, making it confusing rather than difficult in the intended way; and blank-length or spacing that inadvertently cues the expected answer.

Extended-response items are the most adaptable format for measuring complex learning outcomes — particularly integration and application — and, because they require writing, double as a way to assess writing skill directly. They have a reputation for being easy to write, but a genuinely well-constructed item (one clearly worded, tied to the actual learning outcome, and capable of assessing complex thinking) is hard to devise. Common errors: an ambiguous question that gives students no real guidance on what's being asked (leaving them free to answer "yes" or "no," or to address only one of several plausible dimensions of the topic); scoring without a rubric, so the same teacher scores the same response differently depending on unrelated factors (unexpected responses, irrelevant information, grammatical errors); a "halo" effect from grading one student's whole test at once rather than one question across all students at once, so accumulated impressions of a given student bleed into how later answers on the same paper are scored; and offering students a choice of prompts, which undermines score comparability since students are no longer really taking the same test.

The central disadvantage of extended-response items is unreliable scoring: different teachers can score an identical response differently, and the same teacher can score the same response differently on different occasions (Linn & Miller, 2005). Several concrete steps improve scoring reliability and validity: (1) write an outline of a model answer before scoring begins, to make explicit what students are actually expected to include; (2) read a sample of student answers first, to calibrate expectations and notice common misconceptions before scoring in earnest; (3) decide in advance how irrelevant information and mechanical errors (grammar, spelling) will be handled, rather than deciding ad hoc per paper; and (4) score using either point-scoring or a scoring rubric, rather than an unstructured overall impression. In **point-scoring**, specific components of an answer are each assigned a point value — useful for consistency, but prone to pulling attention toward easily-counted facts (e.g., naming risk factors) at the expense of the higher-level thinking the item may actually have been designed to assess. A **scoring rubric** that describes the quality of an answer at each performance level is generally the stronger alternative when higher-order thinking is the real target — see [Rubrics](../strategies/rubrics.md).

## Design Implications

### Context
#### Requirements
- A genuinely clear prompt: well-constructed extended-response items make the actual task explicit through wording and, often, planning notes or hints, not through length or elaborateness alone
- A model answer and a scoring plan (rubric or point-scoring) prepared before scoring begins, not improvised paper by paper
#### Constraints
- Completion and short-answer items outside mathematics are poorly suited to complex learning outcomes and are frequently harder to score reliably than they first appear, since genuinely unambiguous phrasing is difficult to achieve
- Extended-response scoring reliability degrades specifically when there is no rubric, when papers are graded question-by-question-per-student rather than one question across all students, and when choice among prompts is offered
- Point-scoring's ease of use comes at a real cost to validity when the actual goal is higher-order thinking rather than fact enumeration

### Target Learners
- All students in a K-12 or classroom-assessment context; extended-response items are the natural choice when the learning goal itself requires integration, application, or written expression that selected-response items structurally cannot assess

### Target Learning Goals
- Recall and production of specific factual content (completion/short-answer); integration, application, and writing skill (extended-response)

### Affordances
- [Rubrics](../strategies/rubrics.md) — the recommended scoring structure for extended-response items when higher-order thinking, not just factual coverage, is the target
- [Validity, Reliability, and Bias in Classroom Assessment](../principles/validity-reliability-and-bias-in-classroom-assessment.md) — the scoring-reliability problem this page describes is a direct instance of that principle's reliability concerns

### Claims
<!-- Claims bearing on this element, each a link to a claim page followed by its evidence tag, e.g. [+M] -->
- [Adding writing prompts and essays to state English language arts assessments shifted classroom instruction toward writing](../claims/ela-writing-prompts-shift-instruction.md) [~W]
- [Despite generally accurate feedback, the LLM's scoring explanations could be unpredictable and prone to logical inconsistency, failing to award points even when citing the correct rubric directive](../claims/llm-logical-inconsistency-scoring-feedback.md) [-W]
- [LLMs overrate short underdeveloped essays and over-penalize minor language errors in well-developed essays](../claims/llm-overrate-short-essays-overpenalize-errors.md) [~W]
- [Adding a model answer to the GPT-4 prompt was counterproductive, lowering scoring reliability](../claims/model-answer-in-prompt-lowered-reliability.md) [~W]
- [Different LLMs rely on different subsets of rubric traits when assigning essay scores](../claims/llms-weight-rubric-traits-differently.md) [~W]
- [For short-answer questions, real student responses received higher LLM-likelihood estimates than LLM-generated responses, a reversal of the pattern in other tasks](../claims/short-answer-detection-reversal.md) [~W]
- [Students perceive AI scoring as accurate for grammar, mechanics, and organization but skeptical of its ability to evaluate diverse styles, complex writing, tone, and emotion](../claims/ai-scoring-perceptions-lower-vs-higher-order.md) [~W]
- [Admissions staff rate essays they perceive as AI-generated lower than essays they believe are human-written, even after adjusting for measured essay quality and actual AI authorship](../claims/perceived-ai-use-lowers-staff-quality-ratings.md) [-W]
- [The revised Round II grading workflow reduced AI over-awarding and total-score MAD, most clearly for OE1 (7.1% to 4.8%) and QM (9.4% to 3.8%)](../claims/revised-workflow-reduces-overawarding-mad.md) [~W]
- [Claude3 and PaLM2 show substantial agreement but fall short on identifying failing grades](../claims/claude3-palm2-substantial-agreement-failing-grades.md) [~W]
- [Newer LLM generations such as GPT-4 generally outperform GPT-3.5 in short-answer grading accuracy, but this advantage is not consistent across all tasks and domains](../claims/gpt4-advantage-uneven-across-tasks.md) [+W]
- [Prompt quality and detailed scoring rubrics significantly influence the accuracy and consistency of LLM-generated grades](../claims/prompt-rubric-quality-drives-llm-grading.md) [~W]
- [AI-assigned total scores on a handwritten chemistry exam align strongly with TA-assigned totals (R2 = 0.91), while per-problem agreement is lower (R2 = 0.61–0.85)](../claims/ai-total-scores-align-with-ta-grades-chemistry-exam.md) [+W]
- [The GED essay is scored holistically on a six-point scale by two independent readers](../claims/ged-essay-holistic-six-point-two-readers.md) [+W]
- [Human inter-rater reliability with a single rubric exceeded the ±5-point equivalence margin used for rubric-source comparisons](../claims/human-inter-rater-disagreement-exceeds-margin.md) [+W]
- [A page-by-page, rubric-guided multimodal LLM workflow graded an authentic handwritten exam in about three hours at roughly $100 in token costs, versus about $3,500 in TA time](../claims/ai-grading-workflow-feasibility-cost.md) [~W]
- [Adapting the scoring mechanism substantially reduced ceiling effects found in the pilot study](../claims/skt-srl-scoring-reduced-ceiling-effects.md) [~W]
- [Multiple-choice single-select items are less difficult than open-ended response questions, and delayed perceived task difficulty ratings relate more strongly to relative item difficulty for open-ended items](../claims/answer-format-availability-affects-difficulty-and-ratings.md) [+W]
- [Automated essay scoring can achieve high agreement with human raters but faces calibration constraints](../claims/aes-high-agreement-calibration-constraint.md) [~W]
- [Transformer-based NLP models achieve automated essay scoring with correlations to human grading exceeding 0.85](../claims/bert-essay-scoring-correlation-085.md) [+W]
- [AEEGS and human raters produced nearly equivalent, low mean scores (5.94 vs 5.97 of 20), with AEEGS slightly higher](../claims/aeegs-human-mean-scores-equivalent-low.md) [~W]
- [Six closed-model configurations grade at or below the human inter-grader floor of 2.61/35 on the CV exam, with the best reaching MAE 1.64](../claims/closed-llm-graders-below-human-floor.md) [+W]
- [A construction-focused correctness rubric underperformed behavior-focused and undefined prompts for LLM scoring of code explanations](../claims/construction-rubric-underperformed-llm-scoring.md) [+W]
- [Sentence embedding models reach only moderate agreement and need human supervision for open-ended grading](../claims/embedding-models-moderate-agreement-need-supervision.md) [+W]
- [Equivalence failures under human evaluators were confined to five assignment-by-question-type cells, four of them on code questions](../claims/five-cells-exceeded-equivalence-margin.md) [~W]
- [Grading time shows a sweet spot: students grading around 20 minutes (time z-score near -0.25) have significantly lower residual standard deviations than slow graders, while snap graders are unreliable and inflate grades](../claims/grading-time-sweet-spot-twenty-minutes.md) [~W]
- [Human scoring and feedback for HDR takes about 11 minutes 30 seconds per learner, while GPT-based scoring and feedback is nearly instant](../claims/hdr-human-scoring-time-burden.md) [+W]
- [Hint-based prompts raise ChatGPT scoring agreement with human experts to 98–100%, while no-hint prompts are unstable (Q2 precision 0.42)](../claims/hint-prompts-raise-llm-scoring-agreement.md) [+W]
- [Human evaluators' prioritization of essential features was significantly better for low-quality essays than for average- and high-scoring essays](../claims/human-prioritization-varies-by-essay-quality.md) [~W]
- [In one study of five LLMs scoring 60 undergraduate essays on IELTS rubric dimensions, systematic underestimation of human scores was the dominant bias trend, with some models also compressing scores into a narrow range](../claims/llm-essay-scoring-systematic-underestimation.md) [~W]
- [LLM agreement with human examiners is limited in fast mode and improves in reasoning or thinking modes](../claims/llm-fast-mode-limited-thinking-mode-better-agreement.md) [~W]
- [A short strict-grader preamble knocks 14 of 17 open-weights LLM graders out of the graded band on a computer-vision exam, with three stopping grading outright](../claims/llm-grader-strict-persona-collapse.md) [~M]
- [Machine–machine agreement exceeds human–machine agreement but remains below human–human agreement](../claims/machine-machine-above-human-machine-below-human-human.md) [~W]
- [A multi-armed bandit controller achieves scoring accuracy comparable to exhaustive grid search while reducing LLM calls by 78.4% and token consumption by 72.8%](../claims/mab-prompt-selection-reduces-aes-costs.md) [~W]
- [NLP-based feedback generation for textual student answers in large courses reduced grading effort by up to 85% with high precision (reported from Bernius et al.)](../claims/nlp-feedback-reduced-grading-effort-85-percent.md) [~W]
- [Native speaking fourth graders answered more open-ended text comprehension questions correctly than non-native speakers (Study 2)](../claims/native-speakers-outperform-text-comprehension.md) [~W]
- [Benchmarking shows NLP-based automated essay scoring achieves grading times up to 80% faster than human graders while maintaining comparable accuracy](../claims/nlp-grading-80-percent-faster-benchmark.md) [~W]
- [Ensembles of operational raters outperform the LLMs: two raters suffice on average across aspects, but larger ensembles are needed for individual aspects](../claims/rater-ensembles-outperform-llms-feedback.md) [~W]
- [Rubric-enhanced prompting (Variant 2) raises LLM assigned scores relative to the no-rubric baseline, with model-specific gaps at particular taxonomy levels](../claims/rubric-prompting-raises-llm-assigned-scores.md) [~W]
- [On assessment item Q10, describing a TinkerPlots plot, 32% of students achieved the maximum score of 4 and 70% achieved half marks or better](../claims/q10-plot-description-scores.md) [~W]
- [Removing detailed rubric explanations from prompts improved grading accuracy across all approaches in an ablation study](../claims/simplified-prompts-outperform-detailed-rubrics.md) [~W]
- [Word count correlates with suggested final grade, with the ordering Gemini Pro > humans > ChatGPT > Gemini among statistically significant correlations (human Spearman's rho = 0.603)](../claims/wordcount-grade-correlation-llm-human.md) [~W]
- [Open response format is associated with higher Alpha than multiple choice in knowledge tests](../claims/knowledge-test-alpha-response-format.md) [+W]
- [Cognitive artifact scoring in the digital workbook achieved high intercoder reliability, with average Spearman's rho of 0.97 overall](../claims/high-intercoder-reliability-workbook-scoring.md) [+W]
- [Grading variability: 40.7% of grade variance lies between teachers and essay quality is the largest random effect](../claims/variance-decomposition-teacher-grading.md) [+W]
- [Experiential attitudes toward feedback predict agreement with expert criteria on weak-essay grades](../claims/feedback-attitudes-predict-expert-consensus.md) [~W]
- [After studying the composition scale, normal-school students double-rated 32 seventh-grade compositions, each composition being rated by two students with the second rater rating a different set](../claims/witham-double-rating-32-compositions.md) [+W]
- [Sentence units of a completion test differ greatly in completion time, ranging from 12.8% of total test time for unit 1 down to 3.4% for unit 11.](../claims/completion-test-sentence-unit-time-differences.md) [~W]
- [Composition scores based on only two compositions are too unreliable for measurement, requiring roughly 17 compositions to match the Terman test's reliability](../claims/composition-reliability-requires-many-samples.md) [+W]
- [Individual freshmen shifted greatly in relative rank between the two completion tests: 47 scored higher on M, 42 higher on K, and 11 the same](../claims/completion-test-individual-rank-shifts.md) [~W]
- [Text reading relates more strongly to multiple-choice, cloze, and oral open-ended comprehension tasks than to written open-ended and retell tasks](../claims/comprehension-task-type-moderates-text-reading-relation.md) [~W]
- [Using the Hillegas Scale reduces the standard deviations of judgments on all but two of the twenty-five compositions](../claims/hillegas-scale-reduces-judgment-sd.md) [+W]
- [Using the Hillegas Scale reduces the range of judgments on each composition, with an average reduction of 11.5 points](../claims/hillegas-scale-reduces-judgment-range.md) [~W]
- [The scale reduces spread on individual compositions without reducing the spread of median scores across compositions (range of medians 32 points in both conditions)](../claims/hillegas-scale-preserves-median-spread.md) [~W]
- [A broad linguistic feature set yields 73.2% classification accuracy for three-level proficiency scoring of TOEFL11 essays](../claims/broad-linguistic-features-73-percent-toefl11-classification.md) [~W]
- [Random Forest performed slightly better overall than SVM and Complement Naive Bayes for classifying short exam answers, with an average F-score of 0.82](../claims/random-forest-slightly-better-for-answer-classification.md) [~W]
- [Rubric-aligned NLP features for evidence and organization outperform proxy-feature and coherence baselines and generalize across datasets](../claims/rubric-aligned-nlp-features-outperform-proxies.md) [+W]
- [LLM grading performance is markedly worse for open-ended history and philosophy questions than for content-based astronomy and astrobiology questions](../claims/llm-grading-worse-on-open-ended-questions.md) [~W]
- [Automated concept-based scoring for c-rater model building achieved kappa comparable to manually built models in 11 of 12 scenarios](../claims/c-rater-automated-concept-scoring-comparable-kappa.md) [+W]
- [SVM with RoBERTa sentence embeddings was the most accurate automatic scoring method (κ = .82) among the four tested combinations](../claims/roberta-svm-most-accurate-scoring-pisa.md) [~W]
- [Wise-crowd content models for summary assessment correlate well with an educational rubric, manually and via two automated NLP methods](../claims/wise-crowd-content-model-summary-assessment.md) [+W]
- [Klein '11 LSA approach achieved its desired effectiveness only after manually marking the majority of student answers, totaling 83 percent across scenarios](../claims/klein-lsa-manual-marking-83-percent.md) [~W]
- [GPT-4o frequently makes characteristic errors in homework assessment, including failing to recognize unit and numeric equivalences, marking complete solutions incomplete, and mishandling alternative methods and notations](../claims/gpt4o-characteristic-assessment-error-types.md) [~W]
- [Autograding is most accurate for numeric answers, and error rates vary less than 8% across languages](../claims/numeric-answers-most-accurate-language-variation-under-8.md) [~W]
- [MSE loss performed at least as well as cross-entropy loss for pseudo-regression scoring of constructed response items](../claims/mse-loss-at-least-as-effective-as-cross-entropy.md) [+W]
- [Finetuned DeBERTa-v3-large models achieved human-like agreement on nine of ten NAEP math constructed response items in the held-out test set](../claims/deberta-human-like-agreement-nine-of-ten-naep-math-items.md) [~W]
- [Inter-rater reliability between human experts and AI coding is very low](../claims/low-irr-experts-vs-ai-coding.md) [~W]
- [LLMs cannot effectively perform in-context learning for short answer scoring, but cross-prompt pre-finetuning substantially boosts their zero-shot performance](../claims/llm-icl-insufficient-prefinetuning-boosts-zero-shot.md) [~W]
- [Cross-prompt finetuning of a pre-finetuned 8B LLM on 50 instances per prompt achieves average QWK of 0.85, comparable to professional human graders (0.87)](../claims/cross-prompt-finetuning-8b-human-level.md) [~W]
- [Fine-tuning several pre-trained LLMs with class balancing, data augmentation, and tailored input modification reaches near human-level automated scoring accuracy on most extended-response mathematics assessment items](../claims/fine-tuned-llms-near-human-math-scoring.md) [~W]
- [Feature-based short-answer scoring systems may be less susceptible to certain student gaming attempts than end-to-end neural models](../claims/feature-based-asas-less-gaming-susceptible.md) [~W]
- [The two human raters of ASAP D7 showed an average inter-rater agreement of 0.60 QWK across rubrics, with rubric-level agreements ranging from 0.46 (Ideas–Conventions) to 0.79 (Ideas–Organization)](../claims/d7-human-rater-agreement-qwk-060.md) [+W]
- [The introduction reports that deep learning and NLP techniques predicted fine-grained rubric scores of student essays with success well beyond the agreement level between two human raters](../claims/deep-learning-essay-scoring-beyond-human-rater-agreement.md) [~W]
- [Holistic scoring of German university students' essays posed significant challenges to both a neural model and an SVM with n-gram features](../claims/german-essay-scoring-challenges-both-models.md) [~W]
- [The proposed AES system predicts holistic essay scores through predicted rubric scores, achieving a QWK of 0.78, competitive with cutting-edge AES tools reporting 0.77–0.81](../claims/aes-holistic-qwk-078-competitive.md) [+W]
- [LLMs can grade short-answer reading comprehension questions with accuracy comparable to human experts, supporting formative assessment grading](../claims/llm-grading-reading-comprehension-expert-comparable.md) [+W]
- [Among six tested MLP architectures, classifiers achieved higher exact-match accuracy on rubric scores, while regression and ensemble variants achieved higher QWK on some rubrics](../claims/aes-architecture-comparison-d7.md) [~W]
- [No correlation between evenness of response score distribution and ML model performance](../claims/no-correlation-evenness-ml-performance.md) [~W]
- [An automated scoring engine matched experienced human markers yet was rejected over the confidentiality-explainability conflict](../claims/crase-scoring-equivalent-to-human-markers-rejected.md) [~W]
- [Expert graders show high agreement among themselves when scoring a written exam on first degree equations](../claims/expert-inter-rater-agreement-high-written-exam.md) [+W]
- [LLM-generated essay scores correlated moderately to strongly with expert human assessor scores](../claims/llm-essay-scoring-correlates-with-experts.md) [~W]
- [Global rating scales by expert practitioners are as reliable as item-specific checklists and less labour intensive to devise](../claims/global-rating-scales-as-reliable-as-checklists.md) [~W]
- [Longer APSS responses received higher scores, particularly for the scenario-application question (r = 0.70)](../claims/response-length-score-correlation-apss.md) [~W]
- [Inter-rater scoring of the writing tests showed good correlation-coefficient reliability](../claims/inter-rater-reliability-writing-scores.md) [+W]

## The evidence by question
- *Which practice format: short answer, multiple choice, or matching the final test?* [Evidence on whether initial short-answer questions produce more learning than initial multiple-choice questions is mixed, with recent studies finding little or no difference](../claims/short-answer-versus-multiple-choice-retrieval-practice-evidence-is-mixed.md) [~M]
- *Do markers scoring the same responses agree, and do written criteria bring their judgements closer?* [Raters differed significantly in severity/leniency in the MFRM analysis](../claims/raters-differed-severity-mfrm.md) [+M]
- *Can a language model score learners' written constructed responses as a trained human marker would, and on which tasks?* [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](../claims/llm-grading-mixed-against-human-raters.md) [~M]

## Related Elements

- [Selected-Response Assessment Items](selected-response-assessment-items.md) — the complementary item family for recognition-level goals
- [Computer-delivered figural response test items for architecture](figural-response-items-architecture.md)

## Examples

- A third-grade mathematics extended-response item asking students to divide books among classrooms and explain their reasoning in words (Illinois Standards Achievement Test, 2006)
- A fifth-grade science item asking students to plan a full investigation (prediction, materials, controlled/manipulated variables, procedure) rather than just answer a single question (Washington State Assessment of Student Learning, 2004)
- [Give learners control over how learning is measured via assessment choices and science-fair-type projects](../strategies/learner-controlled-assessment-science-fair-projects.md)

## Key Sources
- Linn, R. L., & Miller, M. D. (2005). *Measurement and assessment in teaching* (9th ed.). Pearson.
- Arduini-Van Hoose, N. (2020). Teacher-made assessments. In *Educational psychology*. Retrieved from https://edpsych.pressbooks.sunycreate.cloud. CC BY-NC-SA 4.0.
