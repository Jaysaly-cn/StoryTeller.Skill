from pathlib import Path

BASE_DIR = Path("journal_narrative_polisher")

DEFAULT_ASSETS = [
    "instruction.md",
    "skill.md",
    "routing/asset_index.md"
]

ASSET_MAP = {
    "/diagnose": [
        "templates/journal_profile_template.md",
        "templates/manuscript_diagnosis_template.md",
        "checklists/claim_calibration_checklist.md"
    ],
    "/analyze_journal": [
        "templates/journal_profile_template.md"
    ],
    "/analyze_references": [
        "templates/reference_analysis_template.md"
    ],
    "/propose_story": [
        "templates/narrative_strategy_template.md",
        "checklists/claim_calibration_checklist.md"
    ],
    "/polish_intro": [
        "templates/intro_rewrite_template.md",
        "checklists/intro_quality_checklist.md",
        "checklists/claim_calibration_checklist.md"
    ],
    "/polish_discussion": [
        "templates/discussion_rewrite_template.md",
        "checklists/discussion_quality_checklist.md",
        "checklists/claim_calibration_checklist.md"
    ],
    "/full_restructure_phase1": [
        "templates/journal_profile_template.md",
        "templates/reference_analysis_template.md",
        "templates/manuscript_diagnosis_template.md",
        "templates/narrative_strategy_template.md",
        "checklists/claim_calibration_checklist.md"
    ],
    "/full_restructure_phase2": [
        "templates/intro_rewrite_template.md",
        "templates/discussion_rewrite_template.md",
        "checklists/intro_quality_checklist.md",
        "checklists/discussion_quality_checklist.md"
    ],
    "/cover_letter": [
        "templates/cover_letter_template.md",
        "templates/journal_profile_template.md"
    ],
    "/reviewer_risk": [
        "checklists/reviewer_risk_checklist.md",
        "checklists/claim_calibration_checklist.md"
    ]
}


def detect_command(user_text: str) -> str:
    commands = [
        "/diagnose",
        "/analyze_journal",
        "/analyze_references",
        "/propose_story",
        "/polish_intro",
        "/polish_discussion",
        "/full_restructure",
        "/cover_letter",
        "/reviewer_risk"
    ]

    for command in commands:
        if command in user_text:
            if command == "/full_restructure":
                return "/full_restructure_phase1"
            return command

    lower = user_text.lower()

    if "introduction" in lower or "引言" in user_text:
        return "/polish_intro"
    if "discussion" in lower or "讨论" in user_text:
        return "/polish_discussion"
    if "cover letter" in lower or "投稿信" in user_text:
        return "/cover_letter"
    if "reviewer" in lower or "审稿" in user_text or "风险" in user_text:
        return "/reviewer_risk"
    if "故事线" in user_text or "叙事" in user_text or "narrative" in lower:
        return "/propose_story"
    if "期刊匹配" in user_text or "journal fit" in lower:
        return "/diagnose"

    return "/diagnose"


def load_file(relative_path: str) -> str:
    path = BASE_DIR / relative_path
    return path.read_text(encoding="utf-8")


def build_context(user_text: str) -> str:
    command = detect_command(user_text)
    assets = DEFAULT_ASSETS + ASSET_MAP.get(command, [])

    seen = set()
    unique_assets = []

    for asset in assets:
        if asset not in seen:
            seen.add(asset)
            unique_assets.append(asset)

    context_parts = []

    for asset in unique_assets:
        context_parts.append(f"\n\n<!-- Loaded: {asset} -->\n")
        context_parts.append(load_file(asset))

    return "\n".join(context_parts)