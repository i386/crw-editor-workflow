# Fix One Cargo Page

Use this workflow for a single Company, ProductLine, Product, or Incident page with known Cargo issues.

## Skills

- `crw-cargo-infobox-fixer`
- `crw-source-auditor`
- `crw-style-lint`
- `crw-ai-policy-finalizer`
- `crw-edit-packager`

## Steps

1. Fetch or paste current page wikitext.
2. Identify the page type.
3. Parse current templates:

   ```sh
   python3 scripts/parse_wikitext_templates.py path/to/page.wiki
   ```

4. Identify only the fields that need changes.
5. Verify any factual values with sources.
6. Produce a minimal template patch.
7. Run style, source, and AI policy checks.
8. Package the edit.

## Output

- Minimal patch.
- Field rationale.
- Sources checked.
- Suggested edit summary.

