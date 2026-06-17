---
description: Turn a CRW Article suggestions row into an article brief or draft plan.
agent: build
---

Use `workflows/suggestion-to-draft.md`.

If the user did not provide a row, fetch a short queue with `scripts/article_suggestions_to_queue.py` and ask which item to work on. Load and follow:

- `crw-article-suggestion-intake`
- `crw-source-auditor`
- `crw-relationship-mapper`
- `crw-style-lint`
- `crw-edit-packager`

Return an article brief unless the user explicitly asks for a full draft.

