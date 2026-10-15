---
type: claim
title: Frontier agents exhibit three distinct behavioral phenotypes—read-first, execute-first, and minimalist—differing in efficiency and safety
description: Frontier agents exhibit three distinct behavioral phenotypes—read-first, execute-first, and minimalist—differing in efficiency and safety
id: three-agent-behavioral-phenotypes-academiclaw
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
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

# Frontier agents exhibit three distinct behavioral phenotypes—read-first, execute-first, and minimalist—differing in efficiency and safety

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r?` · `q2`

## Subclaims
`q2 i?` Models group into three phenotypes by tool-budget allocation: Claude Opus 4.6 read-first (41% of tool calls to file reading, exec-to-read ratio 0.92, highest score 71.9), Gemini 3.1 Pro execute-first (74.3% shell executions, lowest safety 74.9), and GPT-5.4 minimalist (fewest tool calls at 19, third-highest score 65.6). [→ Junjie Yu 2026](#junjie-yu-2026)

## Evidence

### Junjie Yu 2026

Junjie Yu, Pengrui Lu, Weiye Si, Hongliang Lu, Jiabao Wu, Kaiwen Tao, Kun Wang, Lingyu Yang, Qiran Zhang, Xiuting Guo, Xuanyu Wang, Yang Wang, Yanjie Wang, Yi Yang, Zijian Hu, Ziyi Yang, Zonghan Zhou, Binghao Qiang, Borui Zhang, Chenning Li, Enchang Zhang, Feifan Chen, Feng Jian, Fengyin Sun, Hao Qiu, Hao Zheng, Haoran Zhu, Hongyu Liu, Jianbin Deng, Jiaxin Song, Jiaying Chi, Jiayou Shi, Jie Fang, Jinghui Zhong, Jingyu Zhou, Jinze Li, Junfeng Yi, Junyan Yu, Junzhi Xue, Ni Song, Pengyi Chen, Qi Chen, Quansheng Li, Rui Tao, Shenghai Gong, Shenhang Lu, Tianqi Shen, Tianxiang Zhu, Tiehan Kang, Tingyu Li, Wendi Wu, Xiao Shen, Xiao Zhou, Xiaotao Zhang, Xinrong Li, Xuankun Yang, Xun Zhang, Yan Li, Ye Lu, Yi Wang, Yibo Zhou, Yichi Zhang, Yihao Sun, Yijun Huang, Yixin Zhu, Yixuan Wu, Yuchen Sun, Yue Wu, Yuheng Sun, Yukun Li, Yutian Tu, Yuxuan Qin, Yuzhuo Wu, Zeyu Li, Zhengyu Lou, Zhenning Ran, Zizhu He, Pengfei Liu. (2026). AcademiClaw: When Students Set Challenges for AI Agents. arXiv preprint. https://arxiv.org/abs/2605.02661 [doi:10.48550/arxiv.2605.02661](https://doi.org/10.48550/arxiv.2605.02661)

`q2 · i?` · `associational · r?`

Behavioral analysis of tool-usage profiles (Table 5) from the six-model evaluation, identifying phenotypes by how each model allocates tool calls across reading, writing, execution, and process management. The authors term Opus's pattern a comprehension premium: extra reading that converts to measurably better solutions.

> "Claude Opus 4.6 follows a read-first strategy: 41% of tool calls go to file reading—8.6× Gemini's 2.6%—and its exec-to-read ratio is 0.92, the only model where the two are roughly balanced."

## Discussion


## Related Claims
- [Even the best frontier model achieves only a 55% pass rate on AcademiClaw's 80 academic tasks](best-frontier-model-55-percent-pass-academiclaw.md) — related
- [Two of seven frontier LLMs show behavioral inconsistency between monitored and unmonitored conditions (Grok-4.1-fast 5.50; Gemini-3-Pro 5.00), while four show perfect consistency (1.0)](alignment-faking-inconsistency-educational-llms.md) — related
