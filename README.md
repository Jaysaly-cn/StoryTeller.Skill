<!-- 作用：项目总说明，帮助用户和开发者快速理解本 skill 的目标、能力边界和使用方式。 -->

# Journal Narrative Polisher: StoryTeller.Skil

A journal-oriented academic manuscript polishing skill.

本项目用于构建一个“目标期刊导向”的论文叙事润色 skill。它不是普通英文润色工具，而是帮助作者根据目标期刊定位、参考文献风格和自身研究内容，优化论文的 scientific story。实际部署时，建议使用mvp_loader.py最小化加载：instruction.md  skill.md  routing/asset_index.md，以节约token, 其余文件按命令或用户意图动态加载.

## Core Purpose

帮助作者改善：

- Journal fit
- Research gap framing
- Novelty expression
- Introduction logic
- Discussion depth
- Abstract and title positioning
- Claim calibration
- Reviewer-risk reduction
- Cover letter alignment

## Key Idea

普通润色关注：

> Is the English correct?

本 skill 关注：

> Is the manuscript telling the right scientific story for the target journal?

## Main Workflow

1. 收集目标期刊、aims/scope、参考文献和待润色论文。
2. 分析目标期刊公开可观察的定位。
3. 分析参考文献的叙事结构和写作风格。
4. 诊断当前 manuscript 的故事线、gap、novelty 和 claim。
5. 提出多种 narrative strategy。
6. 用户确认路线。
7. 重构或润色 Introduction、Discussion、Abstract、Title 等关键部分。
8. 输出修改理由和需要作者确认的问题。

## Loading Strategy

为节省 token，默认只加载：

- `instruction.md`
- `skill.md`
- `routing/asset_index.md`

其他模板、清单和示例按任务需要动态加载。

## Safety Boundaries

本 skill 不会：

- 编造数据
- 编造引用
- 编造期刊政策
- 声称知道编辑私人偏好
- 保证接收
- 把相关性写成因果性
- 隐藏研究局限

## Recommended Use

适用于：

- 投稿前润色
- 改投目标期刊
- 重写 Introduction
- 重写 Discussion
- 修改 Abstract 和 Title
- 准备 Cover Letter
- 识别审稿风险

### This repository was built using GPT-5.5 assistance.
