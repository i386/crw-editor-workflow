---
name: crw-relationship-mapper
description: Validate and propose CRW Company/ProductLine/Product/Incident relationships for Cargo templates and page links.
---

# CRW Relationship Mapper

Use this skill when a page needs relationship cleanup or when splitting incident content.

## Relationship Model

- Company pages describe organizations.
- ProductLine pages describe product families or services.
- Product pages describe specific products or services.
- Incident pages describe discrete anti-consumer events, practices, policy changes, or disputes.

## Checks

- Incident pages point to the relevant Company.
- Incident pages point to ProductLine/Product when specific enough.
- Product pages point to their Company and ProductLine where appropriate.
- ProductLine pages point to their Company.
- Parent entity pages link to related Incident pages through concise summaries or related sections.
- Incident details are not duplicated heavily across parent entity pages.

## Output

Return:

- Current relationship map.
- Missing or suspicious relations.
- Proposed Cargo field changes.
- Pages that may need backlinks or summary edits.
- Pages that may be mistyped as the wrong Cargo type.

Do not create non-existent related page names unless the workflow is explicitly drafting those pages.

