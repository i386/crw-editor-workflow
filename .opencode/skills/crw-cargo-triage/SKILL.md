---
name: crw-cargo-triage
description: Triage Consumer Rights Wiki Cargo export quality issues and group them into useful editor work queues.
---

# CRW Cargo Triage

Use this skill when working from the Cargo export or the Cargo completeness report.

## Local Helpers

Use:

```sh
python3 scripts/fetch_cargo_export.py
python3 scripts/cargo_quality_report.py data/snapshots/all_cargo_combined.json --markdown reports/cargo-quality.md --json reports/cargo-quality.json
```

The script is intentionally conservative. If the export schema changes, inspect a few records before trusting counts.

## Triage Buckets

Group findings into:

- Missing descriptions for Company/Product/ProductLine pages.
- Missing or malformed websites.
- Incident missing StartDate.
- Incident invalid StartDate or EndDate.
- Resolved Incident missing EndDate.
- Incident with multiple statuses.
- Entity pages with names or relation tokens too short for reliable matching.
- Pages whose Cargo type appears inconsistent with their title/content.

## Prioritization

Prefer batches that:

- Affect browser extension popovers.
- Are easy to verify from official sources.
- Fix many pages with low editorial risk.
- Unblock relationship mapping between incidents and parent entities.

## Output

Return:

- Summary counts.
- 3 to 5 recommended work batches.
- For each batch: example pages, risk level, suggested workflow, and whether human source lookup is required.

Do not invent Cargo values. If a field cannot be verified, leave it blank and mark it for human review.

