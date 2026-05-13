<!-- 作用：定义本 skill 的文件加载策略，用于减少默认上下文 token 消耗。 -->

# Loading Policy

## Default Loading

默认只加载：

1. `instruction.md`
2. `skill.md`
3. `routing/asset_index.md`

不要默认加载：

- `/templates` 下的全部模板
- `/checklists` 下的全部清单
- `/examples` 下的示例文件

## Lazy Loading Rule

仅当用户请求或意图明确涉及某一任务时，才加载对应模板或清单。

Examples:

- 用户请求润色 Introduction → 加载 `intro_rewrite_template.md` 和 `intro_quality_checklist.md`
- 用户请求润色 Discussion → 加载 `discussion_rewrite_template.md` 和 `discussion_quality_checklist.md`
- 用户请求审稿风险分析 → 加载 `reviewer_risk_checklist.md`
- 用户请求 cover letter → 加载 `cover_letter_template.md`

## Examples Loading

`examples/` 目录默认不加载。

仅在以下情况加载：

1. 用户要求示例。
2. 测试 skill 表现。
3. few-shot demonstration 场景。
4. 用户领域与某个 example 高度匹配且需要参考格式。

## Progressive Loading

优先采用渐进式加载：

1. 先判断用户任务。
2. 只加载完成该任务所必需的文件。
3. 如果后续用户进入更深任务，再加载更多文件。

## Full Restructure Rule

对于 `/full_restructure`：

第一阶段加载：

- journal profile
- reference analysis
- manuscript diagnosis
- narrative strategy
- claim calibration

用户确认叙事路线后，再加载：

- intro rewrite
- discussion rewrite
- section-specific checklists
