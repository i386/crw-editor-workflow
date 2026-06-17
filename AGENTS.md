# Consumer Rights Wiki Editor Workflow

This repository contains OpenCode skills, commands, scripts, and workflow playbooks for helping Consumer Rights Wiki editors improve article quality.

## Prime Directive

Do not publish directly to the wiki unless a human editor explicitly asks for that exact action. Prefer producing reviewable drafts, diffs, edit summaries, checklists, and issue reports.

## Authoritative Wiki References

Use these project pages as the editorial baseline:

- https://consumerrights.wiki/w/Consumer_Rights_Wiki:Editorial_guidelines
- https://consumerrights.wiki/w/Consumer_Rights_Wiki:Style_guide
- https://consumerrights.wiki/w/Consumer_Rights_Wiki:AI_usage_policy
- https://consumerrights.wiki/w/Article_suggestions
- https://consumerrights.wiki/w/Projects:Cargo-complete/report

When a workflow depends on current wiki content, fetch the current page or Cargo export before making claims.

## Editorial Standards

Follow Consumer Rights Wiki editorial guidance:

- Use neutral, factual, legally safe language.
- Do not attribute malice to a company or individual unless a court or regulator has established it, and even then phrase it indirectly.
- Support every factual claim with a reliable source.
- Prefer court decisions, regulatory findings, government documents, academic work, official company statements, primary documents, established news, and reputable specialist sources.
- Treat anonymous or vague sources cautiously and attribute them clearly.
- Avoid rant-like, promotional, inflammatory, or personality-driven language.
- Avoid unnecessary technical depth. Define jargon when technical details are needed.
- Preserve existing valid wikitext, citations, templates, and editorial intent unless the task requires changing them.

## Wiki Structure

Consumer Rights Wiki uses Cargo-backed templates for:

- Company
- ProductLine
- Product
- Incident

Incident-specific detail should usually live on Incident pages, not inside Company, Product, or ProductLine pages. Parent entity pages may contain a short neutral summary and links to related incidents.

## AI Use

For AI-assisted content, always produce:

- A human-reviewable diff or patch.
- A list of sources checked.
- A list of unsupported or weakly supported claims.
- Formatting and Cargo risks.
- A concise suggested edit summary.

Never fabricate sources, quotes, dates, page names, Cargo fields, Cargo relationships, archive URLs, or source contents.

## Workflow Expectations

Before drafting:

- Check whether related pages already exist.
- Identify the intended page type.
- Inspect current Cargo fields when available.
- Check whether the page is better handled as a Company, ProductLine, Product, Incident, or Theme article.

Before finalizing:

- Run the AI usage policy checklist.
- Check references.
- Check Cargo fields.
- Check tone and style.
- Produce a concise edit summary.

## Repository Layout

- `.opencode/skills/` contains reusable OpenCode skills.
- `.opencode/commands/` contains slash commands for common editorial workflows.
- `workflows/` contains human-readable workflow playbooks.
- `scripts/` contains local helper scripts for fetching, parsing, and reporting.
- `templates/` contains report and edit bundle templates.
- `data/snapshots/` is for fetched Cargo or wiki snapshots and is ignored by git except for `.gitkeep`.
- `reports/` is for generated reports and is ignored by git except for `.gitkeep`.

## Useful Commands

- `python3 scripts/fetch_cargo_export.py`
- `python3 scripts/cargo_quality_report.py data/snapshots/all_cargo_combined.json --markdown reports/cargo-quality.md`
- `python3 scripts/fetch_wiki_page.py "Page title"`
- `python3 scripts/article_suggestions_to_queue.py --limit 20`
- `python3 scripts/parse_wikitext_templates.py path/to/page.wiki`

## Relevant Skills

Use repo skills when relevant:

- `crw-cargo-triage`
- `crw-cargo-research-improver`
- `crw-cargo-infobox-fixer`
- `crw-incident-splitter`
- `crw-source-auditor`
- `crw-style-lint`
- `crw-ai-policy-finalizer`
- `crw-article-suggestion-intake`
- `crw-title-and-link-normalizer`
- `crw-relationship-mapper`
- `crw-edit-packager`
- `crw-video-transcript-to-page`
