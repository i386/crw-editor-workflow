---
name: crw-incident-splitter
description: Split incident-specific content out of Company, Product, or ProductLine pages into proper Incident pages.
---

# CRW Incident Splitter

Use this skill when a Company, Product, or ProductLine page contains detailed incident content that should be its own Incident article.

## Detection Cues

Incident content often includes:

- A discrete event, policy change, outage, lawsuit, recall, enforcement action, lockout, fee change, data breach, or product degradation.
- A timeline with a start date.
- A specific affected product, service, or company action.
- A status such as active, pending resolution, or resolved.
- Multiple citations supporting a controversy or consumer harm.

## Workflow

1. Identify the embedded incident section or paragraphs.
2. Decide whether the incident is notable enough to stand alone.
3. Draft a new Incident page with:
   - Neutral lead.
   - Background only as needed.
   - Timeline or events section.
   - Company response or outcome when sourced.
   - References.
   - Incident Cargo template.
4. Replace parent-page detail with:
   - A short neutral summary.
   - Link to the new Incident page.
   - No duplicate deep incident analysis.
5. Add or verify Cargo relationships:
   - Company
   - ProductLine
   - Product
   - StartDate
   - EndDate
   - Status
   - Type
   - Description

## Output

Return an edit bundle containing:

- Proposed new Incident page title.
- New Incident page wikitext.
- Patch for the parent page.
- Cargo field rationale.
- Sources checked.
- Suggested edit summaries for both pages.
- Any redirects or backlinks to consider.

Do not delete parent content without preserving supported facts in either the incident page or a concise parent summary.

