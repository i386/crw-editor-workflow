---
name: crw-source-auditor
description: Audit Consumer Rights Wiki sources for reliability, claim support, citation placement, and missing archive/access metadata.
---

# CRW Source Auditor

Use this skill when verifying sources for a CRW article, draft, or proposed edit.

## Source Reliability Order

Prefer:

1. Court decisions, regulatory findings, official government documents.
2. Peer-reviewed research and academic publications.
3. Official company documents and statements, especially for what a company said or published.
4. Primary documents such as contracts, terms, policies, release notes, support pages, and notices.
5. Major established news organizations and reputable specialist publications.
6. Consumer advocacy organizations and technical experts.

Use caution with:

- Social media posts.
- Forums and community discussions.
- Anonymous sourcing.
- Personal blogs without established credibility.
- Legal statements from parties to a dispute.

Do not use other wikis as sources for factual claims.

## Checks

- Every factual claim has a source.
- The source supports the exact claim, not merely the general topic.
- Anonymous claims are attributed as claims.
- Conflicting sources are acknowledged.
- Access dates are present for online sources.
- Archive links are present where practical.
- Links used for page navigation are not mistaken for citations.

## Output

Return a table:

| Claim | Source | Supports? | Reliability | Action |
| --- | --- | --- | --- | --- |

Then list:

- Unsupported claims.
- Sources to replace.
- Sources that need archive/access metadata.
- Suggested wording changes for weakly supported claims.

