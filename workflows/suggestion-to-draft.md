# Suggestion To Draft

Use this workflow to turn an Article suggestions row into an article brief or draft.

## Skills

- `crw-article-suggestion-intake`
- `crw-source-auditor`
- `crw-relationship-mapper`
- `crw-style-lint`
- `crw-edit-packager`

## Steps

1. Fetch a suggestion queue:

   ```sh
   python3 scripts/article_suggestions_to_queue.py --limit 20
   ```

2. Inspect the original row on the wiki.
3. Check whether related pages already exist.
4. Classify the page type.
5. Review supplied refs.
6. Draft an article brief.
7. If requested, draft the article.
8. Package the result.

## Output

- Article brief.
- Source map.
- Cargo field proposal if applicable.
- Open questions.

