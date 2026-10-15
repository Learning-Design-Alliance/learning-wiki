---
type: claim
title: "Even the best frontier model achieves only a 55% pass rate on AcademiClaw's 80 academic tasks"
description: "Even the best frontier model achieves only a 55% pass rate on AcademiClaw's 80 academic tasks"
id: best-frontier-model-55-percent-pass-academiclaw
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
    kind: design
    rigour: "?"
---

# Even the best frontier model achieves only a 55% pass rate on AcademiClaw's 80 academic tasks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r?` · `q2`

## Subclaims
`q2 i?` In a single-attempt evaluation of six frontier models, Claude Opus 4.6 achieves the highest average score (71.9) and shares the top pass rate of 55.0% with Claude Sonnet 4.6, confirming academic-level tasks pose a substantial challenge. [→ Junjie Yu 2026](#junjie-yu-2026)

## Evidence

### Junjie Yu 2026

Junjie Yu, Pengrui Lu, Weiye Si, Hongliang Lu, Jiabao Wu, Kaiwen Tao, Kun Wang, Lingyu Yang, Qiran Zhang, Xiuting Guo, Xuanyu Wang, Yang Wang, Yanjie Wang, Yi Yang, Zijian Hu, Ziyi Yang, Zonghan Zhou, Binghao Qiang, Borui Zhang, Chenning Li, Enchang Zhang, Feifan Chen, Feng Jian, Fengyin Sun, Hao Qiu, Hao Zheng, Haoran Zhu, Hongyu Liu, Jianbin Deng, Jiaxin Song, Jiaying Chi, Jiayou Shi, Jie Fang, Jinghui Zhong, Jingyu Zhou, Jinze Li, Junfeng Yi, Junyan Yu, Junzhi Xue, Ni Song, Pengyi Chen, Qi Chen, Quansheng Li, Rui Tao, Shenghai Gong, Shenhang Lu, Tianqi Shen, Tianxiang Zhu, Tiehan Kang, Tingyu Li, Wendi Wu, Xiao Shen, Xiao Zhou, Xiaotao Zhang, Xinrong Li, Xuankun Yang, Xun Zhang, Yan Li, Ye Lu, Yi Wang, Yibo Zhou, Yichi Zhang, Yihao Sun, Yijun Huang, Yixin Zhu, Yixuan Wu, Yuchen Sun, Yue Wu, Yuheng Sun, Yukun Li, Yutian Tu, Yuxuan Qin, Yuzhuo Wu, Zeyu Li, Zhengyu Lou, Zhenning Ran, Zizhu He, Pengfei Liu. (2026). AcademiClaw: When Students Set Challenges for AI Agents. arXiv preprint. https://arxiv.org/abs/2605.02661 [doi:10.48550/arxiv.2605.02661](https://doi.org/10.48550/arxiv.2605.02661)

`q2 · i?` · `design · r?`

Systematic single-attempt evaluation of six frontier models on all 80 AcademiClaw tasks (Table 3), each run in an identical Docker sandbox with pass defined as score ≥ 75. The description reports the printed pass rates and average scores; no standardized effect size is printed.

> "Claude Opus 4.6 achieves the highest average score (71.9) and shares the top pass rate of 55.0% with Claude Sonnet 4.6. GPT-5.4 and Gemini 3.1 Pro form a second tier at 42.5–43.8% pass rate, while Qwen3.5-397B and MiniMax M2.7 trail at 37.5–40.0%."

## Discussion


## Related Claims
- [Frontier agents exhibit three distinct behavioral phenotypes—read-first, execute-first, and minimalist—differing in efficiency and safety](three-agent-behavioral-phenotypes-academiclaw.md) — related
- [Over a quarter of benchmark tasks (23 of 80) defeat all six frontier models, with over 22% showing capability boundaries where scores swing by up to 90 points](capability-boundaries-and-universal-failures-academiclaw.md) — related
