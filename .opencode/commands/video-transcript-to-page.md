---
description: Turn a video transcript into a CRW article brief, source map, suggestion row, draft, or page patch.
agent: build
---

Use `workflows/video-transcript-to-page.md`.

Ask for or use the video URL, transcript/captions, and intended output from the user message. Load and follow:

- `crw-video-transcript-to-page`
- `crw-source-auditor`
- `crw-article-suggestion-intake`
- `crw-relationship-mapper`
- `crw-style-lint`
- `crw-ai-policy-finalizer`
- `crw-edit-packager`

Treat the transcript as an orientation source unless the video itself is the fact being cited. Return a claim-source map and mark anything needing independent verification. Do not publish wiki edits.

