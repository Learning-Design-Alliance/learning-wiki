---
type: claim
title: Safety and task quality are largely independent across models, implying safety guardrails impose no measurable performance tax
description: Safety and task quality are largely independent across models, implying safety guardrails impose no measurable performance tax
id: safety-quality-independence-academiclaw
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: junjie-yu-2026
    resource: "https://doi.org/10.48550/arxiv.2605.02661"
    title: "Junjie Yu, Pengrui Lu, Weiye Si, Hongliang Lu, Jiabao Wu, Kaiwen Tao, Kun Wang, Lingyu Yang, Qiran Zhang, Xiuting Guo, Xuanyu Wang, Yang Wang, Yanjie Wang, Yi Yang, Zijian Hu, Ziyi Yang, Zonghan Zhou, Binghao Qiang, Borui Zhang, Chenning Li, Enchang Zhang, Feifan Chen, Feng Jian, Fengyin Sun, Hao Qiu, Hao Zheng, Haoran Zhu, Hongyu Liu, Jianbin Deng, Jiaxin Song, Jiaying Chi, Jiayou Shi, Jie Fang, Jinghui Zhong, Jingyu Zhou, Jinze Li, Junfeng Yi, Junyan Yu, Junzhi Xue, Ni Song, Pengyi Chen, Qi Chen, Quansheng Li, Rui Tao, Shenghai Gong, Shenhang Lu, Tianqi Shen, Tianxiang Zhu, Tiehan Kang, Tingyu Li, Wendi Wu, Xiao Shen, Xiao Zhou, Xiaotao Zhang, Xinrong Li, Xuankun Yang, Xun Zhang, Yan Li, Ye Lu, Yi Wang, Yibo Zhou, Yichi Zhang, Yihao Sun, Yijun Huang, Yixin Zhu, Yixuan Wu, Yuchen Sun, Yue Wu, Yuheng Sun, Yukun Li, Yutian Tu, Yuxuan Qin, Yuzhuo Wu, Zeyu Li, Zhengyu Lou, Zhenning Ran, Zizhu He, Pengfei Liu. (2026). AcademiClaw: When Students Set Challenges for AI Agents. arXiv preprint. https://arxiv.org/abs/2605.02661 [doi:10.48550/arxiv.2605.02661](https://doi.org/10.48550/arxiv.2605.02661)"
    author: Junjie Yu, Pengrui Lu, Weiye Si, Hongliang Lu, Jiabao Wu, Kaiwen Tao, Kun Wang, Lingyu Yang, Qiran Zhang, Xiuting Guo, Xuanyu Wang, Yang Wang, Yanjie Wang, Yi Yang, Zijian Hu, Ziyi Yang, Zonghan Zhou, Binghao Qiang, Borui Zhang, Chenning Li, Enchang Zhang, Feifan Chen, Feng Jian, Fengyin Sun, Hao Qiu, Hao Zheng, Haoran Zhu, Hongyu Liu, Jianbin Deng, Jiaxin Song, Jiaying Chi, Jiayou Shi, Jie Fang, Jinghui Zhong, Jingyu Zhou, Jinze Li, Junfeng Yi, Junyan Yu, Junzhi Xue, Ni Song, Pengyi Chen, Qi Chen, Quansheng Li, Rui Tao, Shenghai Gong, Shenhang Lu, Tianqi Shen, Tianxiang Zhu, Tiehan Kang, Tingyu Li, Wendi Wu, Xiao Shen, Xiao Zhou, Xiaotao Zhang, Xinrong Li, Xuankun Yang, Xun Zhang, Yan Li, Ye Lu, Yi Wang, Yibo Zhou, Yichi Zhang, Yihao Sun, Yijun Huang, Yixin Zhu, Yixuan Wu, Yuchen Sun, Yue Wu, Yuheng Sun, Yukun Li, Yutian Tu, Yuxuan Qin, Yuzhuo Wu, Zeyu Li, Zhengyu Lou, Zhenning Ran, Zizhu He, Pengfei Liu
    q: 2
    i: "?"
    kind: associational
    rigour: "?"
---

# Safety and task quality are largely independent across models, implying safety guardrails impose no measurable performance tax

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r?` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across all six models, the Pearson correlation between safety score and task score is weak (|r| < 0.29; p > 0.05 for five of six models, with GPT-5.4 a marginal exception at r = 0.28, p = 0.01). [→ Junjie Yu 2026](#junjie-yu-2026)

## Evidence

### Junjie Yu 2026

Junjie Yu, Pengrui Lu, Weiye Si, Hongliang Lu, Jiabao Wu, Kaiwen Tao, Kun Wang, Lingyu Yang, Qiran Zhang, Xiuting Guo, Xuanyu Wang, Yang Wang, Yanjie Wang, Yi Yang, Zijian Hu, Ziyi Yang, Zonghan Zhou, Binghao Qiang, Borui Zhang, Chenning Li, Enchang Zhang, Feifan Chen, Feng Jian, Fengyin Sun, Hao Qiu, Hao Zheng, Haoran Zhu, Hongyu Liu, Jianbin Deng, Jiaxin Song, Jiaying Chi, Jiayou Shi, Jie Fang, Jinghui Zhong, Jingyu Zhou, Jinze Li, Junfeng Yi, Junyan Yu, Junzhi Xue, Ni Song, Pengyi Chen, Qi Chen, Quansheng Li, Rui Tao, Shenghai Gong, Shenhang Lu, Tianqi Shen, Tianxiang Zhu, Tiehan Kang, Tingyu Li, Wendi Wu, Xiao Shen, Xiao Zhou, Xiaotao Zhang, Xinrong Li, Xuankun Yang, Xun Zhang, Yan Li, Ye Lu, Yi Wang, Yibo Zhou, Yichi Zhang, Yihao Sun, Yijun Huang, Yixin Zhu, Yixuan Wu, Yuchen Sun, Yue Wu, Yuheng Sun, Yukun Li, Yutian Tu, Yuxuan Qin, Yuzhuo Wu, Zeyu Li, Zhengyu Lou, Zhenning Ran, Zizhu He, Pengfei Liu. (2026). AcademiClaw: When Students Set Challenges for AI Agents. arXiv preprint. https://arxiv.org/abs/2605.02661 [doi:10.48550/arxiv.2605.02661](https://doi.org/10.48550/arxiv.2605.02661)

`q2 · i?` · `associational · r?`

Correlational analysis across the six-model evaluation relating weighted safety scores to task scores. The article concludes models can maintain high safety without sacrificing quality, and lower safety does not yield a quality advantage; the printed correlations are the only statistics.

> "Across all six models, the Pearson correlation between safety score and task score is weak (|𝑟|<0.29 ; 𝑝 >0.05 for five of six models, with GPT-5.4 as a marginal exception at 𝑟=0.28 , 𝑝=0.01 )."

## Discussion


## Related Claims
- [Knowledge, Skills, and Attitude scores are largely independent across frontier LLMs, with Knowledge–Skills correlation r=−0.51 and Knowledge–Attitude r=−0.63](ksa-dimensions-weakly-negative-correlated-llms.md) — related
- [Safety and Trustworthiness is strongly anti-correlated with Basic Education across the nine evaluated models (r = −0.83)](safety-basic-education-anticorrelation.md) — reports the opposite
- [Token consumption is uncorrelated with task quality across models (r = −0.03), suggesting agents lack mechanisms for knowing when to stop](token-consumption-uncorrelated-with-quality-academiclaw.md) — related
- [LLM attack success rates increase consistently from single-turn to static multi-turn and dynamic multi-turn interactions in educational settings](asr-increases-dynamic-multi-turn-education.md) — related
- [No evaluated LLM tutor is reliably safe: every model exceeds 60% harm rate on at least five risk categories in single-turn and six in multi-turn evaluation](no-llm-tutor-reliably-safe-60-percent-harm.md) — related
