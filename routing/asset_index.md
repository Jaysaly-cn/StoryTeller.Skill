<!-- 作用：定义用户命令、任务意图与应加载文件之间的映射关系。 -->



\# Asset Index



\## Core Files



Always load:



\- `instruction.md`

\- `skill.md`



Usually load:



\- `routing/asset\_index.md`



\## Command-to-Asset Mapping



\### `/diagnose`



Purpose:



\- Diagnose journal fit and manuscript narrative problems.



Load:



\- `templates/journal\_profile\_template.md`

\- `templates/manuscript\_diagnosis\_template.md`

\- `checklists/claim\_calibration\_checklist.md`



Optional:



\- `checklists/reviewer\_risk\_checklist.md`



\---



\### `/analyze\_journal`



Purpose:



\- Analyze journal aims/scope and public orientation.



Load:



\- `templates/journal\_profile\_template.md`



\---



\### `/analyze\_references`



Purpose:



\- Analyze rhetorical patterns of reference papers.



Load:



\- `templates/reference\_analysis\_template.md`



\---



\### `/propose\_story`



Purpose:



\- Generate multiple narrative strategies.



Load:



\- `templates/narrative\_strategy\_template.md`

\- `checklists/claim\_calibration\_checklist.md`



\---



\### `/polish\_intro`



Purpose:



\- Polish or reconstruct Introduction.



Load:



\- `templates/intro\_rewrite\_template.md`

\- `checklists/intro\_quality\_checklist.md`

\- `checklists/claim\_calibration\_checklist.md`



Optional:



\- `templates/journal\_profile\_template.md`

\- `templates/reference\_analysis\_template.md`



\---



\### `/polish\_discussion`



Purpose:



\- Polish or reconstruct Discussion.



Load:



\- `templates/discussion\_rewrite\_template.md`

\- `checklists/discussion\_quality\_checklist.md`

\- `checklists/claim\_calibration\_checklist.md`



Optional:



\- `checklists/reviewer\_risk\_checklist.md`



\---



\### `/full\_restructure`



Purpose:



\- Reconstruct Title, Abstract, Introduction, Discussion, and overall narrative.



Phase 1 Load:



\- `templates/journal\_profile\_template.md`

\- `templates/reference\_analysis\_template.md`

\- `templates/manuscript\_diagnosis\_template.md`

\- `templates/narrative\_strategy\_template.md`

\- `checklists/claim\_calibration\_checklist.md`



Phase 2 Load after user confirmation:



\- `templates/intro\_rewrite\_template.md`

\- `templates/discussion\_rewrite\_template.md`

\- `checklists/intro\_quality\_checklist.md`

\- `checklists/discussion\_quality\_checklist.md`



Optional:



\- `templates/cover\_letter\_template.md`

\- `checklists/reviewer\_risk\_checklist.md`



\---



\### `/cover\_letter`



Purpose:



\- Generate a target-journal-aligned cover letter.



Load:



\- `templates/cover\_letter\_template.md`

\- `templates/journal\_profile\_template.md`



Optional:



\- `templates/narrative\_strategy\_template.md`



\---



\### `/reviewer\_risk`



Purpose:



\- Identify likely reviewer concerns.



Load:



\- `checklists/reviewer\_risk\_checklist.md`

\- `checklists/claim\_calibration\_checklist.md`



Optional:



\- `templates/manuscript\_diagnosis\_template.md`



\## Intent-based Loading Without Command



If the user does not use a command, infer intent:



\- Mentions “Introduction” or “引言” → `/polish\_intro`

\- Mentions “Discussion” or “讨论” → `/polish\_discussion`

\- Mentions “cover letter” or “投稿信” → `/cover\_letter`

\- Mentions “审稿人”, “reviewer”, “风险” → `/reviewer\_risk`

\- Mentions “故事线”, “叙事”, “narrative” → `/propose\_story`

\- Mentions “期刊匹配”, “journal fit” → `/diagnose`

\- Provides only journal information → `/analyze\_journal`

\- Provides reference papers → `/analyze\_references`



If uncertain, ask the user to choose a mode.

