# Video Transcript To Page

Use this workflow to turn a video transcript, caption file, or timestamped video notes into a CRW article brief, source map, article suggestion, or draft page.

## Skills

- `crw-video-transcript-to-page`
- `crw-source-auditor`
- `crw-article-suggestion-intake`
- `crw-relationship-mapper`
- `crw-style-lint`
- `crw-ai-policy-finalizer`
- `crw-edit-packager`

## Steps

1. Collect inputs:
   - Video URL.
   - Video title/channel/date if known.
   - Transcript or caption text.
   - Video description links or sources.
   - Desired output: brief, draft, source map, suggestion row, or page patch.

2. Identify the topic:
   - Company.
   - ProductLine.
   - Product.
   - Incident.
   - Theme.

3. Extract a claim list from the transcript:
   - Timeline.
   - Named entities.
   - Alleged practice or consumer harm.
   - Evidence shown or cited.
   - Creator commentary that should not be copied into wiki voice.

4. Build a claim-source map:
   - Transcript-only claims.
   - Claims supported by linked sources.
   - Claims supported by primary sources.
   - Claims needing independent verification.

5. Check existing wiki coverage:
   - Existing page for the incident.
   - Existing Company/Product/ProductLine pages.
   - Related incidents that should be linked.

6. Decide output:
   - If sourcing is weak, produce an Article suggestions row or research brief.
   - If sourcing is adequate, produce a page draft or patch.
   - If incident details are mixed into an entity page, switch to `split-embedded-incident`.

7. Run style, source, and AI-policy checks.
8. Package the result for human review.

## Output

Include:

- Video metadata.
- Transcript reliability notes.
- Suggested page type.
- Claim-source table.
- Draft or brief.
- Cargo field proposal if applicable.
- Claims needing human verification.
- Suggested edit summary.

