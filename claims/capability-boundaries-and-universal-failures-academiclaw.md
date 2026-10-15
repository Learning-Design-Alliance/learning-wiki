---
type: claim
title: "Over a quarter of benchmark tasks (23 of 80) defeat all six frontier models, with over 22% showing capability boundaries where scores swing by up to 90 points"
description: "Over a quarter of benchmark tasks (23 of 80) defeat all six frontier models, with over 22% showing capability boundaries where scores swing by up to 90 points"
id: capability-boundaries-and-universal-failures-academiclaw
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

# Over a quarter of benchmark tasks (23 of 80) defeat all six frontier models, with over 22% showing capability boundaries where scores swing by up to 90 points

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r?` · `q2`

## Subclaims
`q2 i?` 23 of 80 tasks (28.8%) defeat all six models, with 8 tasks where every model scores below 50; high-variance tasks expose qualitative differences invisible in aggregate scores. [→ Junjie Yu 2026](#junjie-yu-2026)

## Evidence

### Junjie Yu 2026

Junjie Yu, Pengrui Lu, Weiye Si, Hongliang Lu, Jiabao Wu, Kaiwen Tao, Kun Wang, Lingyu Yang, Qiran Zhang, Xiuting Guo, Xuanyu Wang, Yang Wang, Yanjie Wang, Yi Yang, Zijian Hu, Ziyi Yang, Zonghan Zhou, Binghao Qiang, Borui Zhang, Chenning Li, Enchang Zhang, Feifan Chen, Feng Jian, Fengyin Sun, Hao Qiu, Hao Zheng, Haoran Zhu, Hongyu Liu, Jianbin Deng, Jiaxin Song, Jiaying Chi, Jiayou Shi, Jie Fang, Jinghui Zhong, Jingyu Zhou, Jinze Li, Junfeng Yi, Junyan Yu, Junzhi Xue, Ni Song, Pengyi Chen, Qi Chen, Quansheng Li, Rui Tao, Shenghai Gong, Shenhang Lu, Tianqi Shen, Tianxiang Zhu, Tiehan Kang, Tingyu Li, Wendi Wu, Xiao Shen, Xiao Zhou, Xiaotao Zhang, Xinrong Li, Xuankun Yang, Xun Zhang, Yan Li, Ye Lu, Yi Wang, Yibo Zhou, Yichi Zhang, Yihao Sun, Yijun Huang, Yixin Zhu, Yixuan Wu, Yuchen Sun, Yue Wu, Yuheng Sun, Yukun Li, Yutian Tu, Yuxuan Qin, Yuzhuo Wu, Zeyu Li, Zhengyu Lou, Zhenning Ran, Zizhu He, Pengfei Liu. (2026). AcademiClaw: When Students Set Challenges for AI Agents. arXiv preprint. https://arxiv.org/abs/2605.02661 [doi:10.48550/arxiv.2605.02661](https://doi.org/10.48550/arxiv.2605.02661)

`q2 · i?` · `design · r?`

Task-level analysis of the six-model evaluation (Table 7). The most discriminating task, zh_jiazu_tupu, shows Claude, GPT, and Gemini scoring 86–92 while MiniMax and Qwen score 3—a 90-point chasm the authors attribute to differences in long-context literary comprehension.

> "Meanwhile,23of80tasks(28.8%)defeatallsixmodels, with 8 tasks where every model scores below 50, confirming that AcademiClaw poses a substantial challenge to current frontier agents."

## Discussion


## Related Claims
- [Even the best frontier model achieves only a 55% pass rate on AcademiClaw's 80 academic tasks](best-frontier-model-55-percent-pass-academiclaw.md) — related
- [CDPK performance scales with model size, with a sharp Pareto-frontier drop-off below around 8B parameters](cdpk-scales-with-model-size-dropoff-below-8b.md) — related
- [Baseline capability moderates AI productivity benefits non-monotonically across AI's capability frontier](baseline-capability-nonmonotonic-ai-benefit.md) — related
- [LLM accuracy on the CDPK pedagogy benchmark ranges from 28% to 89%, with closed-weight reasoning models dominating the top of the leaderboard](cdpk-accuracy-range-28-89-closed-models-lead.md) — related
- [Frontier LLM prompting strategies cluster at joint integrity scores of 0.81-0.88 while non-frontier references collapse to 0.50-0.55, a 25-31 point capability-tier gap](varia-frontier-nonfrontier-tier-gap.md) — related
