# Cargo Quality Sweep

Use this workflow to find and batch Cargo-backed data problems.

## Skills

- `crw-cargo-triage`
- `crw-cargo-infobox-fixer`
- `crw-relationship-mapper`
- `crw-edit-packager`

## Steps

1. Fetch the latest Cargo export:

   ```sh
   python3 scripts/fetch_cargo_export.py
   ```

2. Generate reports:

   ```sh
   python3 scripts/cargo_quality_report.py data/snapshots/all_cargo_combined.json --markdown reports/cargo-quality.md --json reports/cargo-quality.json
   ```

3. Inspect the highest-count issue buckets.
4. Choose one low-risk batch.
5. For each page in the batch, fetch or inspect current wikitext before drafting a fix.
6. Package proposed edits for human review.

## Output

- `reports/cargo-quality.md`
- Batch recommendation list.
- Edit bundles for selected pages.

