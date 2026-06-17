---
name: crw-cargo-infobox-fixer
description: Propose minimal fixes to CRW Cargo-backed templates for Company, ProductLine, Product, and Incident pages.
---

# CRW Cargo Infobox Fixer

Use this skill when fixing one page's Cargo-backed template.

## Inputs

- Current page wikitext.
- Page title.
- Known page type.
- Sources for any proposed values.

## Template Fields

Company:

- Founded
- Industry
- Logo
- ParentCompany
- Type
- Website
- Description

ProductLine:

- Company
- ReleaseYear
- InProduction
- ArticleType
- Category
- Logo
- Website
- Description

Product:

- Company
- ProductLine
- ReleaseYear
- InProduction
- ArticleType
- Category
- Logo
- Website
- Description

Incident:

- Company
- StartDate
- EndDate
- Status
- ProductLine
- Product
- ArticleType
- Type
- Description

## Rules

- Make the smallest patch needed.
- Keep descriptions at or below 150 characters.
- Use existing related page names when possible.
- Do not create relation values that have not been verified.
- Use `Active`, `Pending Resolution`, or `Resolved` as a single Incident status.
- Leave EndDate blank for ongoing incidents.
- If Status is `Resolved`, look for a supported EndDate.

## Output

Return:

- Proposed template patch or replacement template.
- Source/rationale for each changed field.
- Fields left blank because they need human verification.
- Suggested edit summary.

