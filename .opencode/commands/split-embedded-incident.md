---
description: Split incident-specific content out of an entity page into a proper CRW Incident draft.
agent: build
---

Use `workflows/split-embedded-incident.md`.

Ask for or use the target parent page title/wikitext from the user message. Load and follow:

- `crw-incident-splitter`
- `crw-relationship-mapper`
- `crw-source-auditor`
- `crw-style-lint`
- `crw-ai-policy-finalizer`
- `crw-edit-packager`

Return a new Incident draft, parent-page patch, Cargo rationale, source notes, and edit summaries. Do not publish wiki edits.

