<!-- 作用：skill 主体说明文件，定义 skill 名称、适用场景、输入输出、命令、加载策略和工作流。 -->

# Skill: Journal Narrative Polisher

## Name

`journal_narrative_polisher`

## Version

`0.1.0`

## Description

A journal-oriented manuscript polishing skill for improving scientific storytelling and target-journal alignment.

It helps authors analyze the target journal, learn rhetorical patterns from reference papers, diagnose manuscript weaknesses, and rewrite key sections such as Introduction, Discussion, Abstract, Title, and Cover Letter.

## Use This Skill When

The user wants to:

- Submit to a specific journal
- Improve journal fit
- Analyze similar papers from the target journal
- Rewrite Introduction or Discussion
- Clarify research gap, novelty, or contribution
- Reduce reviewer concerns
- Prepare a cover letter

## Do Not Use For

- Fabricating results
- Creating fake citations
- Hiding limitations
- Guaranteeing acceptance
- Plagiarism disguise
- Unsupported overclaiming

## Preferred Input

```json
{
  "target_journal": "",
  "journal_aims_scope": "",
  "author_guidelines": "",
  "reference_papers": [
    {
      "title": "",
      "abstract": "",
      "introduction": "",
      "discussion": "",
      "doi_or_url": ""
    }
  ],
  "manuscript": {
    "title": "",
    "abstract": "",
    "introduction": "",
    "methods_summary": "",
    "results_summary": "",
    "discussion": "",
    "conclusion": ""
  },
  "author_intent": {
    "main_claim": "",
    "novelty": "",
    "preferred_tone": "conservative / balanced / assertive",
    "editing_depth": "light / medium / deep / full_restructure"
  },
  "constraints": {
    "word_limit": "",
    "avoid_overclaiming": true,
    "output_language": "Chinese analysis + English revision"
  }
}
```

## Minimal Input

For preliminary diagnosis:

- Target journal name
- Manuscript title and abstract
- Main findings

For deep rewriting:

- Target journal
- Aims/scope
- 2–5 reference papers
- Manuscript Introduction and Discussion
- Main claim and novelty

## Commands

### `/diagnose`

Analyze journal fit and manuscript problems.

### `/analyze_journal`

Analyze aims/scope and public journal orientation.

### `/analyze_references`

Analyze rhetorical patterns of reference papers.

### `/propose_story`

Propose multiple narrative strategies.

### `/polish_intro`

Polish or reconstruct Introduction.

### `/polish_discussion`

Polish or reconstruct Discussion.

### `/full_restructure`

Reconstruct Title, Abstract, Introduction, and Discussion.

### `/cover_letter`

Generate a target-journal-aligned cover letter.

### `/reviewer_risk`

Identify likely reviewer concerns.

## Default Workflow

1. Intake
2. Journal analysis
3. Reference paper analysis
4. Manuscript diagnosis
5. Narrative strategy proposal
6. User confirmation
7. Rewriting
8. Explanation and verification questions

## Loading Behavior

To reduce token usage, this skill uses lazy loading.

Default loaded files:

- `instruction.md`
- `skill.md`
- `routing/asset_index.md`

Task-specific files should be loaded only when needed.

Examples:

- `/polish_intro` loads Introduction-related template and checklist.
- `/polish_discussion` loads Discussion-related template and checklist.
- `/reviewer_risk` loads reviewer-risk checklist.
- `/cover_letter` loads cover-letter template.

Do not load examples by default.

## Default Output

Use task-relevant templates from `/templates`.

Always include:

- Strategy options before full rewrite
- Claim calibration
- Author confirmation points

## Safety Reminder

Do not fabricate journal information, references, data, mechanisms, or editorial preferences. Do not guarantee acceptance.