---
name: crw-ai-policy-finalizer
description: Run the Consumer Rights Wiki AI-assisted edit checklist before a draft or patch is ready for human publication.
---

# CRW AI Policy Finalizer

Use this skill before finalizing any AI-assisted wiki edit.

## Required Checklist

1. Diff review
   - Identify exactly what changed.
   - Confirm unrelated text, citations, templates, and formatting were not altered.

2. Preview review
   - Check for broken wikitext, malformed refs, heading mistakes, list/table issues, and AI-copy artifacts.

3. Source review
   - Examine every AI-found or AI-used link.
   - Confirm each source supports the sentence it is attached to.
   - Flag fabricated, broken, paywalled-without-context, or weak sources.

4. Accuracy review
   - Check dates, company names, product names, legal/regulatory outcomes, and quotes.
   - Mark claims that still need human verification.

5. Editorial review
   - Run the style and tone rules from `crw-style-lint`.
   - Confirm the edit is factual, non-accusatory, and accessible.

## Output

Produce an edit finalization block:

- Ready status: `Ready for editor review`, `Needs fixes`, or `Do not publish`.
- Diff summary.
- Sources checked.
- Claims needing human verification.
- Formatting risks.
- Suggested edit summary.

Never claim that an edit is safe to publish if sources were not checked.

