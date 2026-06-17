# Cargo Quality Research Sweep

Use this workflow to turn Cargo quality findings into researched article-improvement reports.

Cargo issues are discovery signals. A missing description, bad website, unresolved incident date, or suspicious relationship field often means the article itself needs better sourcing, clearer prose, or cleaner entity/incident separation. This workflow uses research to suggest edits that improve the page, not just the Cargo field.

## Skills

- `crw-cargo-triage`
- `crw-cargo-research-improver`
- `crw-cargo-infobox-fixer`
- `crw-relationship-mapper`
- `crw-source-auditor`
- `crw-style-lint`
- `crw-ai-policy-finalizer`
- `crw-edit-packager`

## Steps

1. Start from Cargo findings:

   ```sh
   reports/cargo-quality.json
   ```

   If no findings file exists, generate one:

   ```sh
   python3 scripts/fetch_cargo_export.py
   python3 scripts/cargo_quality_report.py data/snapshots/all_cargo_combined.json --markdown reports/cargo-quality.md --json reports/cargo-quality.json
   ```

2. Pick a small research batch, normally 3 to 10 pages. Prefer pages where research can improve the article, not just fill a field:
   - Missing descriptions.
   - Missing or malformed websites.
   - Resolved incidents missing EndDate.
   - Invalid dates.
   - Multi-status incidents.
   - Suspicious relationship fields.
   - Entity pages that may contain incident material.

3. For each selected page, inspect current wikitext:

   ```sh
   python3 scripts/fetch_wiki_page.py "Page title" --out "data/snapshots/Page_title.wiki"
   ```

4. Research the subject:
   - Official company/product pages.
   - Court, regulator, government, or standards documents.
   - Primary documents such as terms, support notices, policies, release notes, app store pages, archived pages, and announcements.
   - Established reporting or reputable specialist sources.
   - Existing CRW related pages.

5. Build a claim-source map:
   - What the current page says.
   - What Cargo says is missing or suspicious.
   - What reliable sources establish.
   - What remains unverified.

6. Decide article improvements:
   - Add or improve a concise lead or description.
   - Correct or add Cargo fields with sourced values.
   - Add citations for unsupported claims.
   - Replace risky language with neutral sourced wording.
   - Add or repair relationships to Company, ProductLine, Product, or Incident pages.
   - Recommend splitting incident content if it is embedded in an entity page.

7. Produce a researched edit report:
   - Include proposed wikitext patches.
   - Cite sources checked.
   - Separate ready edits from research notes.
   - Include suggested edit summaries.

8. Run style, source, and AI-policy checks before marking any edit ready for human publication.

## Output

- `reports/cargo-research-sweep.md`, or an equivalent report in the chat.
- One section per page.
- Research summary.
- Claim-source map.
- Proposed article/Cargo patch.
- Split recommendation when relevant.
- Sources checked.
- Unsupported claims.
- Risk level.
- Suggested edit summary.
- A separate backlog for pages that need deeper human research.

Do not publish wiki edits from this workflow.
