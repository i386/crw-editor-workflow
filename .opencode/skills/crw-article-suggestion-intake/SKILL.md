---
name: crw-article-suggestion-intake
description: Turn a Consumer Rights Wiki Article suggestions row into a reviewable article brief or draft plan.
---

# CRW Article Suggestion Intake

Use this skill when an editor wants to work from the Article suggestions page.

## Local Helper

Use this to get a rough queue:

```sh
python3 scripts/article_suggestions_to_queue.py --limit 20
```

Because wiki tables can contain complex wikitext, inspect the original row before relying on extracted text.

## Workflow

1. Identify the suggested subject and incident summary.
2. Check whether a related page already exists.
3. Check inclusion fit.
4. Classify target page type:
   - Incident
   - Theme
   - Company
   - ProductLine
   - Product
5. Review supplied sources.
6. Identify missing source types.
7. Draft a brief:
   - Proposed title.
   - Page type.
   - One-paragraph neutral summary.
   - Suggested outline.
   - Cargo fields if applicable.
   - Source map.
   - Open questions.

## Output

Return an article brief, not a finished article, unless the editor asks for a draft.

If the suggestion is already partially covered, recommend updating the existing page instead of creating a duplicate.

