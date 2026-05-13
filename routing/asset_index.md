<!-- 作用：定义用户命令、任务意图与应加载文件之间的映射关系。 -->

# Asset Index

## Core Files

Always load:

- `instruction.md`
- `skill.md`

Usually load:

- `routing/asset_index.md`

## Command-to-Asset Mapping

### `/diagnose`

Purpose:

- Diagnose journal fit and manuscript narrative problems.

Load:

- `templates/journal_profile_template.md`
- `templates/manuscript_diagnosis_template.md`
- `checklists/claim_calibration_checklist.md`

Optional:

- `checklists/reviewer_risk_checklist.md`

---

### `/analyze_journal`

Purpose:

- Analyze journal aims/scope and public orientation.

Load:

- `templates/journal_profile_template.md`

---

### `/analyze_references`

Purpose:

- Analyze rhetorical patterns of reference papers.

Load:

- `templates/reference_analysis_template.md`

---

### `/propose_story`

Purpose:

- Generate multiple narrative strategies.

Load:

- `templates/narrative_strategy_template.md`
- `checklists/claim_calibration_checklist.md`

---

### `/polish_intro`

Purpose:

- Polish or reconstruct Introduction.

Load:

- `templates/intro_rewrite_template.md`
- `checklists/intro_quality_checklist.md`
- `checklists/claim_calibration_checklist.md`

Optional:

- `templates/journal_profile_template.md`
- `templates/reference_analysis_template.md`

---

### `/polish_discussion`

Purpose:

- Polish or reconstruct Discussion.

Load:

- `templates/discussion_rewrite_template.md`
- `checklists/discussion_quality_checklist.md`
- `checklists/claim_calibration_checklist.md`

Optional:

- `checklists/reviewer_risk_checklist.md`

---

### `/full_restructure`

Purpose:

- Reconstruct Title, Abstract, Introduction, Discussion, and overall narrative.

Phase 1 Load:

- `templates/journal_profile_template.md`
- `templates/reference_analysis_template.md`
- `templates/manuscript_diagnosis_template.md`
- `templates/narrative_strategy_template.md`
- `checklists/claim_calibration_checklist.md`

Phase 2 Load after user confirmation:

- `templates/intro_rewrite_template.md`
- `templates/discussion_rewrite_template.md`
- `checklists/intro_quality_checklist.md`
- `checklists/discussion_quality_checklist.md`

Optional:

- `templates/cover_letter_template.md`
- `checklists/reviewer_risk_checklist.md`

---

### `/cover_letter`

Purpose:

- Generate a target-journal-aligned cover letter.

Load:

- `templates/cover_letter_template.md`
- `templates/journal_profile_template.md`

Optional:

- `templates/narrative_strategy_template.md`

---

### `/reviewer_risk`

Purpose:

- Identify likely reviewer concerns.

Load:

- `checklists/reviewer_risk_checklist.md`
- `checklists/claim_calibration_checklist.md`

Optional:

- `templates/manuscript_diagnosis_template.md`

## Intent-based Loading Without Command

If the user does not use a command, infer intent:

- Mentions “Introduction” or “引言” → `/polish_intro`
- Mentions “Discussion” or “讨论” → `/polish_discussion`
- Mentions “cover letter” or “投稿信” → `/cover_letter`
- Mentions “审稿人”, “reviewer”, “风险” → `/reviewer_risk`
- Mentions “故事线”, “叙事”, “narrative” → `/propose_story`
- Mentions “期刊匹配”, “journal fit” → `/diagnose`
- Provides only journal information → `/analyze_journal`
- Provides reference papers → `/analyze_references`

If uncertain, ask the user to choose a mode.
