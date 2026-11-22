"""Validate portable package structure and reference scoring. Python 3 standard library."""
from pathlib import Path
import json
import math
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

def calculate(criteria):
    applicable = observed = earned = 0.0
    for item in criteria:
        w, status, rating = item["weight"], item["status"], item.get("rating")
        if isinstance(w, bool) or not isinstance(w, (int, float)) or not math.isfinite(w) or w <= 0:
            raise ValueError("Weight must be finite and positive")
        if status not in ("observed", "unverified", "na"):
            raise ValueError("Unknown evidence status")
        if status == "observed":
            if isinstance(rating, bool) or not isinstance(rating, (int, float)) or not math.isfinite(rating) or not 0 <= rating <= 5:
                raise ValueError("Observed rating must be 0..5")
        elif rating is not None:
            raise ValueError("Unavailable/inapplicable evidence cannot have a rating")
        if status == "na":
            continue
        applicable += w
        if status == "observed":
            observed += w
            earned += w * rating / 5
    return {
        "score": math.floor(100 * earned / observed + 0.5) if observed else None,
        "coverage": math.floor(100 * observed / applicable + 0.5) if applicable else None,
        "provisional": observed / applicable < 0.7 if applicable else False,
    }

def main():
    errors = []
    required = ["README.md", "GENERAL-REVIEW.md", "SKILL.md",
                "references/scoring.md", "references/evidence-and-tools.md",
                "references/research-sources.md", "templates/project-brief.json",
                "templates/review-report.md", "templates/builder-handoff.md",
                "validation/scenarios.md", "validation/results.md",
                "examples/poster-review.md", "examples/poster-score.json"]
    for name in required:
        if not (ROOT / name).is_file():
            errors.append("Missing: " + name)
    for path in ROOT.rglob("*.md"):
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            target = target.split("#", 1)[0]
            if target and not (path.parent / target).exists():
                errors.append(f"Broken local link in {path.relative_to(ROOT)}: {target}")
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not skill.startswith("---\n") or "\n---\n" not in skill[4:]:
        errors.append("Missing skill frontmatter")
    if "name: design-review-studio" not in skill or not re.search(r"^description: .+", skill, re.M):
        errors.append("Invalid skill metadata")
    general = (ROOT / "GENERAL-REVIEW.md").read_text(encoding="utf-8")
    contract = general.split("## Operating contract", 1)[1].split("## Select the review category", 1)[0].strip()
    categories = sorted((ROOT / "categories").glob("*.md"))
    if len(categories) != 7:
        errors.append("Expected seven standalone categories")
    for path in [ROOT / "GENERAL-REVIEW.md", *categories]:
        portable = path.read_text(encoding="utf-8")
        if "## Visual refinement — graphic-design-thinking" not in portable:
            errors.append("Missing visual-refinement guidance: " + path.name)
        if "Version 1.1.0" not in portable or "## Plain-language results" not in portable:
            errors.append("Missing version/plain-language guidance: " + path.name)
    sample = json.loads((ROOT / "examples/poster-score.json").read_text(encoding="utf-8"))
    if calculate(sample["criteria"]) != sample["expected"]:
        errors.append("Fictional example score calculation failed")
    example = (ROOT / "examples/poster-review.md").read_text(encoding="utf-8")
    if "74/100" not in example or "95%" not in example or "Illustration only" not in example:
        errors.append("Fictional example presentation differs from scoring fixture")
    for path in categories:
        text = path.read_text(encoding="utf-8")
        own = text.split("## Operating contract", 1)[1].split("## Category rubric", 1)[0].strip()
        if own != contract:
            errors.append("Standalone contract drift: " + path.name)
        weights = re.findall(r"^\| ([^|]+) \| (\d+) \| ([^|]+) \|$", text, re.M)
        if sum(int(w) for _, w, _ in weights) != 100:
            errors.append("Weights do not total 100: " + path.name)
        for label, weight, criteria in weights:
            line = f"- {label}: {weight}% — {criteria}."
            if line not in general:
                errors.append("General/category rubric drift: " + path.name + ": " + label)
    for path in (ROOT / "templates").glob("*.json"):
        json.loads(path.read_text(encoding="utf-8"))
    fixtures = json.loads((ROOT / "validation/fixtures.json").read_text(encoding="utf-8"))
    for case in fixtures:
        actual = calculate(case["criteria"])
        if actual != case["expected"]:
            errors.append(f"Scoring failure {case['name']}: {actual}")
    invalid = [
        [{"weight": 0, "status": "observed", "rating": 3}],
        [{"weight": 1, "status": "observed", "rating": 6}],
        [{"weight": 1, "status": "unverified", "rating": 3}],
        [{"weight": 1, "status": "unknown", "rating": None}],
    ]
    for case in invalid:
        try:
            calculate(case)
            errors.append("Invalid scoring input accepted")
        except ValueError:
            pass
    if errors:
        print("\n".join(errors))
        return 1
    print(f"PASS: links, metadata, {len(categories)} standalone contracts, matching weights, JSON, {len(fixtures)} scoring fixtures and {len(invalid)} invalid-input checks.")
    print("PASS: shared refinement guidance, plain-language guidance and fictional example arithmetic.")
    print("Structural/scoring verification only; no live-design or cross-model benchmark performed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())

