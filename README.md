<!-- 作用：项目总说明，帮助用户和开发者快速理解本 skill 的目标、能力边界和使用方式。 -->

# Journal Narrative Polisher: StoryTeller.Skil

“你得讲一个故事 You should tell a good story”    ————我的导师 My PI

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

# USAGE：

## 1. 它能做什么？

这个 skill 可以帮助你：

- 分析目标期刊的 aims and scope
- 判断论文与目标期刊是否匹配
- 分析目标期刊相似文章的写作风格
- 梳理 Introduction 的 research gap
- 优化 Abstract、Title、Introduction、Discussion
- 设计更清晰的论文故事线
- 检查是否存在 overclaim
- 从审稿人角度识别潜在风险
- 辅助撰写 cover letter

---

## 2. 它和普通润色有什么不同？

普通润色更关注：

> 这句话英文是否正确？

这个 skill 更关注：

> 这篇论文的研究问题、gap、novelty 和 contribution 是否讲清楚？

因此，它特别适合以下情况：

- 数据和结果已有，但 Introduction 不够有吸引力
- Discussion 只是重复结果，缺少解释和升华
- 不知道如何突出 novelty
- 不确定文章是否适合目标期刊
- 改投新期刊，需要调整叙事逻辑

---

## 3. 使用前建议准备什么？

为了获得更好的效果，建议准备以下材料。

### 目标期刊信息

- 目标期刊名称
- Aims and Scope
- Author Guidelines，如有

### 参考文献

最好提供 2–5 篇目标期刊中与你主题相近的文章。

每篇可提供：

- Title
- Abstract
- Introduction
- Discussion
- DOI 或 URL

如果没有全文，至少提供 Title 和 Abstract。

### 自己的论文内容

建议提供：

- Title
- Abstract
- Introduction
- Main results
- Discussion
- Conclusion，如有

### 作者意图

请说明：

- 你认为本文最重要的发现是什么？
- 本文最大的 novelty 是什么？
- 你希望突出机制、方法、临床意义、应用价值，还是理论贡献？

---

## 4. 推荐使用流程

建议不要一开始就让它“重写全文”。

更推荐：

> 先诊断 → 再设计故事线 → 最后重写关键部分

### Step 1：诊断论文和期刊匹配度

使用命令：

`/diagnose`

示例：

```text
/diagnose

目标期刊：XXX Journal

Aims and Scope：
这里粘贴期刊介绍。

我的论文主题：
这里简单说明研究主题。

我的 Abstract：
这里粘贴摘要。

我的 Introduction：
这里粘贴引言。

我的 Discussion：
这里粘贴讨论。

本文最重要的发现是：
这里说明主要发现。

请帮我判断这篇论文是否适合该期刊，并指出 Introduction 和 Discussion 的主要问题。
```

---

### Step 2：分析目标期刊相似文章风格

使用命令：

`/analyze_references`

示例：

```text
/analyze_references

以下是 3 篇目标期刊相近文章的 Title、Abstract、Introduction 和 Discussion：

Paper 1:
Title:
Abstract:
Introduction:
Discussion:

Paper 2:
...

Paper 3:
...

请总结这些文章常见的叙事风格和写作逻辑。
```

---

### Step 3：生成论文故事线方案

使用命令：

`/propose_story`

示例：

```text
/propose_story

请基于目标期刊、参考文献和我的论文内容，给出 2–3 种可能的叙事路线，并说明每种路线的优点和风险。
```

常见叙事路线包括：

- Gap-driven narrative：从研究空白出发
- Problem-solution narrative：从问题和解决方案出发
- Mechanism-driven narrative：从机制解释出发
- Translational-impact narrative：从临床或应用意义出发

---

### Step 4：确认路线后重写关键部分

例如：

```text
我选择 mechanism-driven narrative，但希望语气保守一些。
请帮我重构 Introduction。
```

或：

```text
请采用 problem-solution narrative，重写 Abstract 和 Discussion。
```

---

## 5. 常用命令

### `/diagnose`

诊断论文与目标期刊的匹配度，以及当前稿件的主要问题。

### `/analyze_journal`

分析目标期刊的 aims/scope 和公开可观察定位。

### `/analyze_references`

分析目标期刊相似文章的叙事风格。

### `/propose_story`

生成多种论文故事线方案。

### `/polish_intro`

润色或重构 Introduction。

### `/polish_discussion`

润色或重构 Discussion。

### `/full_restructure`

重构 Title、Abstract、Introduction 和 Discussion 的整体叙事逻辑。

### `/cover_letter`

生成投稿 Cover Letter。

### `/reviewer_risk`

从审稿人角度识别潜在风险。

---

## 6. 输出通常包括什么？

根据任务不同，它可能输出：

- 目标期刊画像
- 期刊 aims/scope 摘要
- 参考文献写作风格分析
- 当前论文的优势和问题
- 多种可选叙事路线
- 推荐润色逻辑
- 重构后的 Introduction 或 Discussion
- 修改理由
- 需要作者确认的科学事实或 claim
- 潜在审稿风险

---

## 7. 注意事项

这个 skill 不会：

- 编造数据
- 编造引用
- 编造期刊政策
- 声称知道编辑私人偏好
- 保证论文接收
- 把相关性写成因果性
- 帮助隐藏研究局限

它的目标是：

> 在不改变科学事实的前提下，让论文的研究问题、gap、novelty 和 contribution 表达得更清楚。

---

## 8. 隐私提醒

如果论文尚未投稿或包含敏感信息，建议使用前先删除或脱敏：

- 作者姓名
- 单位信息
- 未公开数据
- 基金编号
- 伦理审批编号
- 可识别患者或样本信息

---

## 9. 一句话总结

**Journal Narrative Polisher** 是一个面向目标期刊的论文叙事润色助手。

它适合帮助你回答：

> 我的论文该如何讲故事，才能更清楚、更准确、更符合目标期刊的期待？

This repository was built using GPT-5.5 assistance.
