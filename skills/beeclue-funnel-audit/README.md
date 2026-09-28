# Beeclue Funnel Audit (`beeclue-funnel-audit`)

> An autonomous Conversion Rate Optimization (CRO), Funnel Architecture, and Lead Generation Audit System developed by **[Beeclue Tech](https://beeclue.com/?utm_source=skills_repo&utm_medium=readme&utm_campaign=funnel_audit)**. Built for Claude Code, Gemini CLI, Cursor, and Antigravity.

---

## Overview

`beeclue-funnel-audit` transforms any website or codebase into an optimized, high-converting lead generation machine. Operating directly inside your local repository, the skill inspects source code, runs the local development server, navigates all rendered routes across desktop and mobile, evaluates copy, forms, CTAs, trust signals, and tracking instrumentation, computes an objective **100-Point Funnel Health Index (FHI)**, and produces an actionable, prioritized roadmap with ready-to-publish copy rewrites.

### Why This Skill is Different
- **Direct Codebase Inspection**: Analyzes actual templates, routes, components, server actions, and tracking scripts instead of guessing from static screenshots.
- **Strict Code Freeze Guardrail**: Enforces a safety rule preventing the agent from modifying code during the audit phase. Changes are proposed in structured batches and executed only after your explicit approval.
- **Evidence-Based Conversion Science**: Grounded in the MECLABS Conversion Heuristic ($C = 4m + 3v + 2(i-f) - 2a$), BJ Fogg's Behavior Model ($B = MAP$), the LIFT Model, and Cialdini's Persuasion Principles.
- **Production-Ready Copy**: Delivers full, drop-in replacement copy (headline, subhead, body, CTA) for high-impact sections rather than vague advice like "make headline better".

---

## Quick Install

### Using the Skills CLI:
```bash
# Add from beeclue repository
npx skills add beeclue/beeclue-skills --skill beeclue-funnel-audit
```

### Manual Installation:
```bash
# For Gemini CLI / Antigravity:
cp -r skills/beeclue-funnel-audit ~/.gemini/config/skills/

# For Claude Code:
cp -r skills/beeclue-funnel-audit ~/.claude/skills/
```

---

## Trigger Phrases

Activate the skill by asking your AI coding assistant:
- *"Audit this website to increase qualified leads and conversions"*
- *"Run a complete CRO and funnel audit on this codebase"*
- *"Audit our marketing funnel and lead capture forms"*
- *"Analyze this site's conversion rate optimization and provide recommendations"*
- *"Review this website's copy, CTAs, and user journey"*

---

## The 29 Audit Dimensions

The skill executes an exhaustive evaluation across 29 core dimensions:

1. **Entire Codebase Reconnaissance**: Tech stack, framework, routing paradigms, component architecture, and CMS integrations.
2. **Local Runtime & DOM Verification**: Rendering tests across desktop and mobile viewports, interactive states, validation, and error states.
3. **Route Discovery & Inventory**: Tabulation of all routes, page types, primary CTAs, target audiences, and funnel stages.
4. **Business Model & ICP Mapping**: Observable offerings, inferred target profiles, core problems, value propositions, and differentiators.
5. **CRO Framework Evaluation**: Friction vs. motivation modeling, funnel leaks, and dead-end pathways.
6. **Homepage Fold-by-Fold Deep Dive**: 5-second clarity test above the fold; section-by-section breakdown below the fold.
7. **Copywriting Audit**: Verbatim current copy vs. problem diagnosis vs. recommended production copy and rationale.
8. **CTA Hierarchy Audit**: Full CTA inventory, removal of generic text ("Learn More"), and intent-matched replacements.
9. **Lead Capture & Form Ergonomics**: Field count minimization, input accessibility, validation UX, and thank-you sequences.
10. **Funnel Architecture Modeling**: Current leaky funnel vs. recommended high-velocity funnel flow.
11. **Intent-Based Segmentation**: Tailored journeys for High-Intent Buyers, Problem-Aware Visitors, Evaluators, Skeptics, and Returning Users.
12. **Trust & Credibility Architecture**: Social proof audit, client logos, case study depth, and unsubstantiated claim detection.
13. **Objection Disarmament Matrix**: Direct addressing of price, risk, time-to-value, and switching anxiety.
14. **UX & Usability Inspection**: Verified code/visual defects vs. potential analytics-dependent issues.
15. **Mobile Conversion Ergonomics**: Viewport constraints, tap target sizes, sticky mobile CTAs, and mobile navigation.
16. **Technical SEO & Structured Data**: Meta tags, OpenGraph, JSON-LD Schema, robots, and sitemap health.
17. **Content Gap Analysis**: Missing BOFU, MOFU, and TOFU assets that drive qualified pipeline.
18. **High-Value Lead Magnets**: 10–20 bespoke lead magnet concepts tied to qualified buyer problems.
19. **Competitive Positioning**: Differentiation analysis separating observed facts from strategic inferences.
20. **Analytics & Attribution Audit**: Tag manager, pixel, and event tracking status (form starts, completions, CTA clicks).
21. **Technical Performance & CWV**: Asset weights, lazy loading, LCP risks, and layout shifts without fake Lighthouse scores.
22. **Accessibility (WCAG 2.1 AA)**: Keyboard focus, semantic structure, color contrast, and form labeling.
23. **Code & Marketing Maintainability**: Hardcoded copy friction, component reusability, and A/B test readiness.
24. **A/B Testing Experiment Backlog**: Structured hypothesis, control, variant, primary metric, and priority.
25. **High-Impact Copy Rewrites**: Complete, drop-in replacement copy for the top 5–10 underperforming sections.
26. **Recommended Site Architecture**: High-converting Information Architecture (IA) tree.
27. **Prioritized Action Plan**: P0/P1/P2 classification with Impact vs. Effort ratings.
28. **30 / 60 / 90 Day Implementation Roadmap**: Staged rollout plan for immediate and long-term gains.
29. **TOP 10 Changes to Make First**: Exact file, change, rationale, and implementation guide for immediate execution.

---

## 100-Point Funnel Health Index (FHI)

Every audit scores your site against an objective 100-point rubric:

| Category | Max Score |
| :--- | :---: |
| 1. Hero & Above-the-Fold Clarity | 10 pts |
| 2. Value Proposition & Positioning | 10 pts |
| 3. CTA Hierarchy & Intent Matching | 10 pts |
| 4. Lead Capture & Form Ergonomics | 10 pts |
| 5. Social Proof & Trust Architecture | 10 pts |
| 6. Objection Handling & Risk Reversal | 10 pts |
| 7. Mobile Conversion Ergonomics | 10 pts |
| 8. Funnel Continuity & Path Routing | 10 pts |
| 9. Technical Speed & Conversion UX | 10 pts |
| 10. Analytics, Tracking & Measurement | 10 pts |
| **Total Benchmark** | **100 pts** |

---

## Human Approval & Phased Rollout Protocol

To ensure full control over codebase changes:
1. **Phase 1 (Audit)**: The agent runs the full evaluation, outputs the executive summary in chat, and writes the complete deliverable to `audits/conversion-funnel-audit-[date].md`.
2. **Phase 2 (Review)**: You review the findings and approve which items to implement.
3. **Phase 3 (Batch Rollout)**: The agent implements changes in 3 safe, incremental git batches:
   - **Batch 1**: Copy rewrites, meta tags, and low-risk text adjustments.
   - **Batch 2**: CTA hierarchy, form field reductions, trust badge placement, and objection accordions.
   - **Batch 3**: Structural layout refactors, new lead magnet landing pages, and event tracking hooks.

---

## Modular References

- [Conversion Psychology & Heuristics](references/frameworks/conversion-heuristics.md): Deep dive into MECLABS, Fogg, LIFT, and Cialdini frameworks.
- [Business Archetype Playbooks](references/playbooks/business-archetypes.md): Tailored funnel models for B2B Services, SaaS PLG, E-Commerce, and Local Services.
- [Audit Report Deliverable Template](references/templates/audit-report-template.md): Standardized markdown deliverable template.
- [Automated Codebase Reconnaissance](references/scripts/codebase-recon.md): Non-invasive terminal commands for route and form extraction.
