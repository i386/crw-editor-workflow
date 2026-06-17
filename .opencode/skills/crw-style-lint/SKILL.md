---
name: crw-style-lint
description: Check Consumer Rights Wiki drafts or page wikitext for style, tone, structure, and readability issues.
---

# CRW Style Lint

Use this skill when reviewing a CRW draft, proposed edit, or existing page for editorial style.

## Inputs

- Page title, page type, and wikitext or draft prose.
- Relevant sources when available.

## Checks

1. Lead and structure
   - Page begins with a concise lead before headings.
   - Headings are sentence case.
   - Heading levels do not skip levels.
   - Headings are unique, not questions, and do not contain citations.

2. Tone
   - Neutral, factual, and legally safe.
   - No direct insults, direct accusations, or unsourced conclusions.
   - No attribution of malice unless established by a court or regulator, and then only indirectly.
   - No rant-like phrasing or personality-driven commentary.

3. Accessibility
   - Avoid unnecessary technical depth.
   - Define jargon where it is needed.
   - Prefer simpler wording when it preserves precision.

4. Links and citations
   - Page links are for navigation or context, not support for claims.
   - Citations support factual claims.
   - Citations appear at the end of the relevant sentence or clause.

## Output

Return:

- `Pass`, `Needs edits`, or `High risk`.
- Specific findings with quoted snippets or line references when available.
- Suggested replacements for risky wording.
- Remaining questions for the editor.

Do not rewrite the whole page unless asked. Prefer targeted edits.

