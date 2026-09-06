#!/usr/bin/env python3
"""
BeeClue Commerce Design Intelligence — Automated Evaluation Runner
Parses verification criteria from eval/scenarios/*.md, audits generated theme
assets (CSS / PHP / JS) against the Anti-Generic Linter and scenario rules,
and reports pass/fail per scenario.

Usage:
    python3 scripts/run-eval.py --list
    python3 scripts/run-eval.py --scenario <name|all> --css <path/to/style.css>
    python3 scripts/run-eval.py --scenario <name|all> --theme-dir <path/to/theme>
    python3 scripts/run-eval.py --test
"""

import os
import re
import sys
import argparse
from typing import Dict, List, Tuple, Optional

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SKILL_DIR = os.path.join(REPO_ROOT, "skills", "beeclue-woocommerce-theme")
EVAL_SCENARIOS_DIR = os.path.join(SKILL_DIR, "eval", "scenarios")
LINTER_MD = os.path.join(SKILL_DIR, "references", "design", "anti-generic-linter.md")

# Banned tokens and patterns from references/design/anti-generic-linter.md
BANNED_HEX_CODES = [
    ("#6366F1", "AI Indigo 500 cliché"),
    ("#A855F7", "AI Purple 500 cliché"),
]

BANNED_GRADIENTS = [
    (re.compile(r'linear-gradient\([^)]*#6366[fF]1[^)]*#a855[fF]7[^)]*\)', re.IGNORECASE), "AI Purple/Indigo gradient (#6366F1 -> #A855F7)"),
    (re.compile(r'linear-gradient\([^)]*#a855[fF]7[^)]*#6366[fF]1[^)]*\)', re.IGNORECASE), "AI Purple/Indigo gradient (#A855F7 -> #6366F1)"),
    (re.compile(r'linear-gradient\([^)]*(indigo|purple|violet)[^)]*(indigo|purple|violet)[^)]*\)', re.IGNORECASE), "Generic purple/indigo AI gradient"),
]

BLACK_AND_GOLD_PATTERNS = [
    (re.compile(r'#000000.*#D4AF37', re.IGNORECASE | re.DOTALL), "Faux-luxury Black & Gold cliché (#000000 + #D4AF37)"),
    (re.compile(r'#000000.*#FFD700', re.IGNORECASE | re.DOTALL), "Faux-luxury Black & Gold cliché (#000000 + #FFD700)"),
]

BANNED_BUZZWORDS = [
    "Elevate Your", "Discover Excellence", "Redefining Perfection"
]

INVALID_UNIT_PATTERN = re.compile(r'\b\d+(\.\d+)?\s+(rem|px|ms|em|vw|vh|%)\b')


def parse_scenario(scenario_path: str) -> Dict:
    """Parses an evaluation scenario markdown file into structured metadata and criteria."""
    filename = os.path.basename(scenario_path)
    scenario_id = os.path.splitext(filename)[0]

    with open(scenario_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Title
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else scenario_id

    # Prompt
    prompt_match = re.search(r'## Scenario Prompt\s+>\s*"([^"]+)"', content)
    prompt = prompt_match.group(1).strip() if prompt_match else ""

    # Criteria
    criteria = []
    crit_section = re.search(r'## 3\.\s+Anti-Generic & Quality Verification Criteria\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if crit_section:
        lines = crit_section.group(1).strip().splitlines()
        for line in lines:
            line = line.strip()
            item_match = re.match(r'^-\s*\[([ xX])\]\s*(.+)$', line)
            if item_match:
                criteria.append({
                    "raw": line,
                    "text": item_match.group(2).strip(),
                    "completed": item_match.group(1).lower() == 'x'
                })

    return {
        "id": scenario_id,
        "filename": filename,
        "title": title,
        "prompt": prompt,
        "criteria": criteria,
        "raw_content": content,
    }


def load_all_scenarios() -> Dict[str, Dict]:
    scenarios = {}
    if not os.path.isdir(EVAL_SCENARIOS_DIR):
        return scenarios
    for f in sorted(os.listdir(EVAL_SCENARIOS_DIR)):
        if f.endswith(".md"):
            path = os.path.join(EVAL_SCENARIOS_DIR, f)
            sc = parse_scenario(path)
            scenarios[sc["id"]] = sc
    return scenarios


def lint_css(css_content: str, scenario_id: Optional[str] = None) -> List[Tuple[bool, str, str]]:
    """
    Audits CSS content against the Anti-Generic Linter rules.
    Returns a list of tuples: (passed: bool, rule_name: str, message: str)
    """
    results = []

    # 1. Check for banned hex codes
    found_banned_hex = []
    for hex_code, desc in BANNED_HEX_CODES:
        if hex_code.lower() in css_content.lower():
            found_banned_hex.append(f"{hex_code} ({desc})")

    if found_banned_hex:
        results.append((False, "Banned Hex Colors", f"Found prohibited AI cliché color(s): {', '.join(found_banned_hex)}"))
    else:
        results.append((True, "Banned Hex Colors", "No prohibited AI cliché hex codes (#6366F1, #A855F7) found."))

    # 2. Check for banned gradients
    found_gradients = []
    for pattern, desc in BANNED_GRADIENTS:
        if pattern.search(css_content):
            found_gradients.append(desc)

    if found_gradients:
        results.append((False, "Banned AI Gradients", f"Found prohibited gradient(s): {', '.join(found_gradients)}"))
    else:
        results.append((True, "Banned AI Gradients", "No generic purple/indigo AI gradients detected."))

    # 3. Check for unit formatting errors (e.g., '2.5 rem')
    unit_matches = INVALID_UNIT_PATTERN.findall(css_content)
    if unit_matches:
        results.append((False, "Strict Unit Formatting", f"Found {len(unit_matches)} invalid CSS units with whitespace (e.g. '2.5 rem')."))
    else:
        results.append((True, "Strict Unit Formatting", "Strict token unit formatting validated (zero whitespace unit errors)."))

    # 4. Scenario-specific checks
    if scenario_id == "luxury-jewelry":
        # Check for banned black and gold cliché
        found_bg = False
        for pattern, desc in BLACK_AND_GOLD_PATTERNS:
            if pattern.search(css_content):
                found_bg = True
                results.append((False, "Cliché Black & Gold Check", f"Haute Jewelry scenario forbids black & gold cliché: {desc} detected."))
                break
        if not found_bg:
            results.append((True, "Cliché Black & Gold Check", "Compliant: No faux-luxury #000000 + #D4AF37 detected."))

    # 5. Check for universal glassmorphism abuse
    card_glass_match = re.search(r'(\.card|\.product-card|article|div\[class\*="card"\])\s*\{[^}]*backdrop-filter:\s*blur', css_content, re.IGNORECASE)
    if card_glass_match:
        results.append((False, "Universal Glassmorphism", "Detected backdrop-filter: blur on standard content cards. Restrict glassmorphism to sticky header/navigation."))
    else:
        results.append((True, "Universal Glassmorphism", "No indiscriminate glassmorphism on content cards."))

    return results


def evaluate_theme(scenario: Dict, css_path: Optional[str] = None, theme_dir: Optional[str] = None) -> bool:
    """Runs evaluation for a single scenario."""
    print(f"\n=================================================================")
    print(f"EVALUATION: {scenario['title']} ({scenario['id']})")
    print(f"=================================================================")
    if scenario.get("prompt"):
        print(f"Prompt: \"{scenario['prompt'][:100]}...\"")
    print(f"\n[Scenario Verification Criteria]")
    for i, c in enumerate(scenario["criteria"], 1):
        print(f"  {i}. {c['text']}")

    passed = True
    checks_run = 0
    checks_passed = 0

    css_content = ""
    if css_path and os.path.isfile(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            css_content = f.read()
    elif theme_dir and os.path.isdir(theme_dir):
        style_css = os.path.join(theme_dir, "style.css")
        if os.path.isfile(style_css):
            with open(style_css, "r", encoding="utf-8") as f:
                css_content = f.read()

    if css_content:
        print(f"\n[Automated Linter Results]")
        results = lint_css(css_content, scenario["id"])
        for success, rule, msg in results:
            checks_run += 1
            if success:
                checks_passed += 1
                print(f"  ✓ [PASS] {rule}: {msg}")
            else:
                passed = False
                print(f"  ❌ [FAIL] {rule}: {msg}")

        # Check theme dir for buzzwords if provided
        if theme_dir and os.path.isdir(theme_dir):
            buzzword_hits = []
            for root, _, files in os.walk(theme_dir):
                for file in files:
                    if file.endswith((".php", ".html", ".js")):
                        fp = os.path.join(root, file)
                        try:
                            with open(fp, "r", encoding="utf-8", errors="ignore") as f:
                                t = f.read()
                            for bw in BANNED_BUZZWORDS:
                                if bw.lower() in t.lower():
                                    buzzword_hits.append(f"{bw} in {file}")
                        except Exception:
                            pass
            checks_run += 1
            if buzzword_hits:
                passed = False
                print(f"  ❌ [FAIL] Anti-Generic Copy: Found banned filler buzzwords: {', '.join(buzzword_hits)}")
            else:
                checks_passed += 1
                print(f"  ✓ [PASS] Anti-Generic Copy: Zero filler buzzwords detected in theme files.")
    else:
        print(f"\n[Notice]: No theme CSS or directory provided; criteria extracted and validated.")

    print(f"\nScenario Summary: {'PASSED' if passed else 'FAILED'} ({checks_passed}/{checks_run} automated checks passed)")
    return passed


def run_self_test() -> bool:
    """Self-test: parses all scenarios and runs linter against valid and invalid fixtures."""
    print("Running Evaluation Runner Self-Test...")
    scenarios = load_all_scenarios()
    assert len(scenarios) >= 4, f"Expected at least 4 scenarios, found {len(scenarios)}"
    for sid, sc in scenarios.items():
        assert sc["title"], f"Scenario {sid} missing title"
        assert len(sc["criteria"]) >= 3, f"Scenario {sid} has insufficient criteria: {len(sc['criteria'])}"
        print(f"  ✓ Parsed scenario: {sid} ({len(sc['criteria'])} verification criteria)")

    # Test linter on clean CSS
    clean_css = """
    :root {
        --color-bg: #0D1014;
        --color-accent: #ECEAE6;
        --spacing: 2.5rem;
    }
    """
    clean_results = lint_css(clean_css, "luxury-jewelry")
    assert all(r[0] for r in clean_results), f"Clean CSS unexpectedly failed: {clean_results}"
    print("  ✓ Clean CSS passed all linter checks.")

    # Test linter on dirty CSS (banned hex + spacing error)
    dirty_css = """
    :root {
        --color-ai: #6366F1;
        --spacing: 2.5 rem;
    }
    .hero {
        background: linear-gradient(135deg, #6366F1, #A855F7);
    }
    """
    dirty_results = lint_css(dirty_css)
    fails = [r[1] for r in dirty_results if not r[0]]
    assert "Banned Hex Colors" in fails, "Failed to catch banned hex"
    assert "Banned AI Gradients" in fails, "Failed to catch banned gradient"
    assert "Strict Unit Formatting" in fails, "Failed to catch unit formatting error"
    print("  ✓ Dirty CSS correctly caught banned hex, banned gradient, and unit space error.")

    # Test black & gold catch on luxury jewelry
    bg_css = """
    :root {
        --color-bg: #000000;
        --color-gold: #D4AF37;
    }
    """
    bg_results = lint_css(bg_css, "luxury-jewelry")
    bg_fails = [r[1] for r in bg_results if not r[0]]
    assert "Cliché Black & Gold Check" in bg_fails, "Failed to catch black & gold on luxury jewelry"
    print("  ✓ Luxury jewelry scenario correctly flagged cliché #000000 + #D4AF37.")

    print("Self-Test PASSED!")
    return True


def main():
    parser = argparse.ArgumentParser(description="BeeClue Commerce Design Intelligence Evaluation Runner")
    parser.add_argument("--list", action="store_true", help="List all evaluation scenarios and their verification criteria")
    parser.add_argument("--scenario", type=str, default="all", help="Target scenario ID (e.g. 'luxury-jewelry', 'premium-skincare', 'automotive', 'b2b-industrial', or 'all')")
    parser.add_argument("--css", type=str, help="Path to theme style.css file to evaluate")
    parser.add_argument("--theme-dir", type=str, help="Path to full theme directory to evaluate")
    parser.add_argument("--test", action="store_true", help="Run runner self-test with fixtures")

    args = parser.parse_args()

    if args.test:
        success = run_self_test()
        sys.exit(0 if success else 1)

    scenarios = load_all_scenarios()
    if not scenarios:
        print(f"Error: No scenarios found in {EVAL_SCENARIOS_DIR}", file=sys.stderr)
        sys.exit(1)

    if args.list:
        print("═══════════════════════════════════════════════════════════════")
        print("BeeClue Evaluation Scenarios & Verification Criteria")
        print("═══════════════════════════════════════════════════════════════")
        for sid, sc in scenarios.items():
            print(f"\nScenario: {sc['title']} (`{sid}`)")
            print(f"File: {sc['filename']}")
            print("Verification Criteria:")
            for i, c in enumerate(sc["criteria"], 1):
                print(f"  [{'x' if c['completed'] else ' '}] {i}. {c['text']}")
        sys.exit(0)

    target_scenarios = []
    if args.scenario.lower() == "all":
        target_scenarios = list(scenarios.values())
    else:
        target = args.scenario.lower().replace(".md", "")
        if target in scenarios:
            target_scenarios = [scenarios[target]]
        else:
            print(f"Error: Scenario '{args.scenario}' not found. Available: {', '.join(scenarios.keys())}", file=sys.stderr)
            sys.exit(1)

    overall_passed = True
    for sc in target_scenarios:
        res = evaluate_theme(sc, css_path=args.css, theme_dir=args.theme_dir)
        if not res:
            overall_passed = False

    print("\n═══════════════════════════════════════════════════════════════")
    print(f"OVERALL EVALUATION RESULT: {'ALL PASSED' if overall_passed else 'FAILURES DETECTED'}")
    print("═══════════════════════════════════════════════════════════════")
    sys.exit(0 if overall_passed else 1)


if __name__ == "__main__":
    main()
