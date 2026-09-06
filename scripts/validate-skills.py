#!/usr/bin/env python3
"""
BeeClue Skills V2 — Automated Verification & Linting Suite
Validates:
1. Master SKILL.md YAML frontmatter and required sections.
2. All reference markdown files exist and contain non-empty content.
3. Strict CSS Custom Property unit formatting (flags '2.5 rem', '4 px', '150 ms').
4. Internal markdown links resolve to valid relative paths.
5. Cross-industry evaluation scenarios and MCP specifications are intact.
"""

import os
import re
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SKILL_DIR = os.path.join(REPO_ROOT, "skills", "beeclue-woocommerce-theme")
SKILL_MD = os.path.join(SKILL_DIR, "SKILL.md")
REFERENCES_DIR = os.path.join(SKILL_DIR, "references")
EVAL_DIR = os.path.join(SKILL_DIR, "eval")
DOCS_DIR = os.path.join(SKILL_DIR, "docs")

def test_skill_frontmatter():
    print("[TEST 1/5] Validating SKILL.md frontmatter...")
    assert os.path.exists(SKILL_MD), f"SKILL.md missing at {SKILL_MD}"
    with open(SKILL_MD, "r", encoding="utf-8") as f:
        content = f.read()

    assert content.startswith("---"), "SKILL.md must start with YAML frontmatter delimiter '---'"
    parts = content.split("---", 2)
    assert len(parts) >= 3, "Invalid frontmatter structure"
    frontmatter = parts[1]

    assert "name: beeclue-woocommerce-theme" in frontmatter, "Missing name: beeclue-woocommerce-theme"
    assert "description:" in frontmatter, "Missing description in frontmatter"
    assert "create woocommerce theme" in frontmatter, "Missing core trigger phrase"
    print("  ✓ SKILL.md frontmatter is valid.")

def test_reference_files():
    print("[TEST 2/5] Validating modular references hierarchy...")
    expected_subdirs = [
        "brand", "intelligence", "intelligence/industries", "design",
        "commerce", "wordpress", "quality", "content", "examples"
    ]
    for subdir in expected_subdirs:
        path = os.path.join(REFERENCES_DIR, subdir)
        assert os.path.isdir(path), f"Missing required reference directory: {path}"

    expected_files = [
        "brand/brand-strategy.md", "brand/positioning.md", "brand/voice.md",
        "intelligence/customer-behavior.md", "intelligence/competitive-intelligence.md",
        "intelligence/industries/luxury-jewelry.md", "intelligence/industries/skincare-beauty.md",
        "intelligence/industries/furniture-home.md", "intelligence/industries/consumer-electronics.md",
        "intelligence/industries/automotive-mobility.md", "intelligence/industries/industrial-b2b.md",
        "intelligence/industries/fashion-apparel.md", "intelligence/industries/food-gourmet.md",
        "intelligence/industries/hospitality-hotel.md", "intelligence/industries/saas-tech.md",
        "design/archetypes-library.md", "design/luxury-definition.md", "design/superclass-tokens.md",
        "design/typography.md", "design/color-systems.md", "design/layout-grids.md",
        "design/image-direction.md", "design/motion-personality.md", "design/anti-generic-linter.md",
        "commerce/strategy.md", "commerce/product-discovery.md", "commerce/cart-checkout.md",
        "wordpress/wp-architecture.md", "wordpress/theme-engineering.md", "wordpress/woocommerce-api.md",
        "quality/visual-qa.md", "quality/a11y-wcag.md", "quality/performance-cwv.md",
        "quality/seo-schema.md", "quality/design-critic.md",
        "content/brand-copy.md", "content/content-strategy.md",
        "examples/lumiere-reasoning.md"
    ]

    for rel_path in expected_files:
        full_path = os.path.join(REFERENCES_DIR, rel_path)
        assert os.path.isfile(full_path), f"Missing expected reference file: {rel_path}"
        size = os.path.getsize(full_path)
        assert size > 200, f"File {rel_path} appears empty or truncated ({size} bytes)"

    print(f"  ✓ All {len(expected_files)} modular reference files exist and are populated.")

def test_css_token_formatting():
    print("[TEST 3/5] Validating CSS token syntax (detecting invalid spaces like '2.5 rem')...")
    tokens_file = os.path.join(REFERENCES_DIR, "design", "superclass-tokens.md")
    with open(tokens_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Extract CSS code blocks
    css_blocks = re.findall(r'```css(.*?)```', text, re.DOTALL)
    assert css_blocks, f"No CSS blocks found in {tokens_file}"

    invalid_pattern = re.compile(r'\b\d+(\.\d+)?\s+(rem|px|ms|em|vw|vh|%)\b')
    for block in css_blocks:
        matches = invalid_pattern.findall(block)
        assert not matches, f"Found invalid CSS token syntax with spaces in CSS block: {matches}"
    print("  ✓ Strict CSS unit formatting validated in all CSS blocks (zero whitespace errors).")

def test_evaluations_and_mcp_docs():
    print("[TEST 4/5] Validating Evaluation Scenarios and MCP Specifications...")
    eval_files = [
        "scenarios/luxury-jewelry.md", "scenarios/premium-skincare.md",
        "scenarios/automotive.md", "scenarios/b2b-industrial.md",
        "cross-industry-diversity-test.md"
    ]
    for ef in eval_files:
        p = os.path.join(EVAL_DIR, ef)
        assert os.path.isfile(p), f"Missing evaluation file: {ef}"

    mcp_files = [
        "beeclue-design-mcp.md", "beeclue-commerce-mcp.md", "beeclue-visual-mcp.md"
    ]
    for mf in mcp_files:
        p = os.path.join(DOCS_DIR, "mcp-specifications", mf)
        assert os.path.isfile(p), f"Missing MCP specification: {mf}"

    print(f"  ✓ All {len(eval_files)} evaluation scenarios and {len(mcp_files)} MCP specs validated.")

def test_relative_markdown_links():
    print("[TEST 5/5] Auditing relative markdown links in SKILL.md...")
    with open(SKILL_MD, "r", encoding="utf-8") as f:
        skill_text = f.read()

    links = re.findall(r'references/([a-zA-Z0-9_\-/\.]+)', skill_text)
    checked = 0
    for link in links:
        # Normalize punctuation
        clean_link = link.rstrip(").,")
        target = os.path.join(REFERENCES_DIR, clean_link)
        assert os.path.exists(target), f"Broken reference link in SKILL.md: references/{clean_link}"
        checked += 1

    print(f"  ✓ Verified {checked} internal reference links in SKILL.md.")

def main():
    print("═══════════════════════════════════════════════════════════════")
    print("BeeClue Skills V2 — Automated Verification Suite")
    print("═══════════════════════════════════════════════════════════════")
    try:
        test_skill_frontmatter()
        test_reference_files()
        test_css_token_formatting()
        test_evaluations_and_mcp_docs()
        test_relative_markdown_links()
        print("═══════════════════════════════════════════════════════════════")
        print("ALL TESTS PASSED: Commerce Design Intelligence V2 is Validated!")
        print("═══════════════════════════════════════════════════════════════")
    except AssertionError as e:
        print(f"\n❌ VALIDATION FAILED: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
