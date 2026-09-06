# Internal Link Architecture & Silo Topic Clustering

Search engines reward websites with logical, hierarchical internal link structures. Internal linking distributes PageRank efficiently and helps AI models index topical authority clusters.

---

## 1. The Hub-and-Spoke Silo Architecture

Organize site pages into distinct thematic silos:

```
                  [Homepage (Tier 1 Authority)]
                               │
       ┌───────────────────────┼───────────────────────┐
       ▼                       ▼                       ▼
 [Services Hub]         [Case Studies Hub]       [Insights Hub]
       │                       │                       │
 ┌─────┴─────┐           ┌─────┴─────┐           ┌─────┴─────┐
 ▼           ▼           ▼           ▼           ▼           ▼
Service A   Service B   Project A   Project B   Article A   Article B
```

### 1.1 Hierarchical Upward Linking
Every child page must link back to its parent hub via accessible semantic breadcrumbs (`Home > Services > Minimalist Residential`).

### 1.2 Cross-Silo Contextual Linking
Relevant services link directly to matching case studies, and case studies link directly to the services deployed.
- Example: Inside `case-studies/napa-valley-estate`, embed a contextual callout:
  *"Discover how our [Sustainable Passive Architecture](/services/passive-architecture) framework was implemented on this site."*

---

## 2. Descriptive Anchor Text Rules

Never use vague anchor text:
- ❌ *"Click here"*, *"Read more"*, *"Learn more"*, *"Check this out"*
- ✅ *"Explore our sustainable architecture methodology"*
- ✅ *"View the Napa Valley residence case study"*
- ✅ *"Review enterprise security specifications"*

---

## 3. Footer Topic Clusters

The footer is not an afterthought; it is the secondary site index. Organize footer links into 4 distinct semantic pillars:
1. **Capabilities / Solutions**: Deep links to individual service pages.
2. **Featured Projects / Case Studies**: Direct links to marquee client outcomes.
3. **Company & Studio**: About, leadership, press, careers, contact.
4. **Legal & Compliance**: Privacy policy, terms, accessibility statement, security posture.
