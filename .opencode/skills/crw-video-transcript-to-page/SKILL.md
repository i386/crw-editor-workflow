---
name: crw-video-transcript-to-page
description: Turn a video transcript into a Consumer Rights Wiki article brief, draft, or source map without over-relying on the video as a sole source.
---

# CRW Video Transcript To Page

Use this skill when an editor provides a video URL, transcript, caption file, or notes from a video and wants to create or improve a CRW page.

## Inputs

- Video URL and title when available.
- Transcript, captions, or timestamped notes.
- Any linked sources from the video description.
- Intended output: article brief, new page draft, incident split, or source map.

## Core Rule

Treat the transcript as a lead-finding and orientation source, not automatically as the factual basis for the page. Strong claims should be verified against primary documents, official statements, court/regulatory materials, established reporting, or the original artifacts discussed in the video.

## Workflow

1. Identify the video metadata:
   - Title.
   - Creator/channel.
   - Publication date.
   - URL.
   - Transcript source and whether it appears auto-generated.

2. Extract candidate claims:
   - Company, product, product line, and incident names.
   - Dates and timeline events.
   - Consumer harm or anti-consumer practice alleged.
   - Direct quotes or on-screen evidence.
   - Sources mentioned verbally or linked in the description.

3. Classify the target:
   - New Incident page.
   - New Product/ProductLine/Company page.
   - Theme page.
   - Update to an existing page.
   - Article suggestion entry.

4. Build a source map:
   - Mark each claim as `transcript-only`, `video evidence`, `linked source`, `primary source`, `secondary source`, or `needs source`.
   - Prefer independent or primary confirmation for significant allegations.
   - Do not cite the transcript for claims that the transcript does not directly establish.

5. Draft cautiously:
   - Use neutral attribution such as "In a video published on DATE, CREATOR stated..." only where the video itself is the relevant fact.
   - For incident facts, cite stronger underlying sources where possible.
   - Avoid adopting the creator's rhetoric or conclusions.
   - Keep technical explanations accessible.

6. Prepare Cargo fields if applicable:
   - Company.
   - ProductLine.
   - Product.
   - StartDate.
   - EndDate.
   - Status.
   - Type.
   - Description.

## Red Flags

- Transcript appears auto-generated and contains name/date errors.
- Video makes allegations without showing or linking supporting evidence.
- Claims rely on forum posts, screenshots, or anonymous comments.
- The creator uses inflammatory language that should not enter wiki voice.
- The video describes several incidents that should become separate pages.

## Output

Return one of:

- Article brief.
- Draft page wikitext.
- Source map.
- Article suggestion row.
- Existing-page patch.

Always include:

- Transcript reliability notes.
- Claim-source table.
- Claims that need independent verification.
- Suggested page type.
- Suggested edit summary if producing a patch.

