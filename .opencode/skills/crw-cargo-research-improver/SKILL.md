---
name: crw-cargo-research-improver
description: Use CRW Cargo quality findings as leads for researched article improvements, including sourcing, prose, Cargo fields, and relationship cleanup.
---

# CRW Cargo Research Improver

Use this skill when a Cargo quality issue should lead to researched article improvement, not just a field-level fix.

## Inputs

- Cargo finding or report row.
- Current page wikitext.
- Existing related CRW pages when relevant.
- Web research or supplied sources.

## Principle

Cargo findings are symptoms. Research the subject enough to understand whether the article needs:

- Better source support.
- A clearer lead or description.
- Correct Cargo fields.
- Relationship cleanup.
- Incident/entity separation.
- Safer wording.
- A note that the finding is a false positive.

## Research Targets

Prefer sources in this order:

1. Court, regulator, government, or standards documents.
2. Official company/product/service pages.
3. Primary documents such as terms, policies, support notices, app store pages, changelogs, archived pages, and announcements.
4. Established news and reputable specialist reporting.
5. Technical or consumer advocacy analysis, clearly attributed.

Use video transcripts, forums, social posts, and anonymous claims as leads unless they directly establish the narrow fact being cited.

## Per-Page Workflow

1. Confirm the Cargo finding still applies.
2. Identify the page type and current template.
3. Read enough of the page to understand the article's current claim structure.
4. Research the subject and collect reliable sources.
5. Build a claim-source map:
   - Current claim.
   - Source support.
   - Proposed action.
6. Decide improvements:
   - Cargo-only patch.
   - Cargo plus prose/citation patch.
   - New or revised lead/description.
   - Relationship cleanup.
   - Incident split recommendation.
   - No edit because the finding is stale or wrong.
7. Produce the smallest useful patch.
8. Run `crw-source-auditor`, `crw-style-lint`, and `crw-ai-policy-finalizer` before marking an edit ready.

## Report Format

Use this structure:

~~~md
# Cargo Research Sweep

## Summary

- Batch:
- Pages researched:
- Ready edits:
- Needs human review:
- Split candidates:
- False positives:

## Ready Edits

### Page title

- Cargo finding:
- Article issue:
- Research summary:
- Sources checked:
- Risk:

| Claim or field | Source | Supports? | Proposed action |
| --- | --- | --- | --- |

```diff
proposed patch
```

Suggested edit summary:

## Needs Human Review

### Page title

- Cargo finding:
- What research found:
- Missing evidence or decision:

## Split Candidates

### Page title

- Embedded incident:
- Suggested Incident page:
- Reason:

## False Positives

- Page title: reason
~~~

## Output

Return a researched report with proposed edits. Do not publish wiki edits.
