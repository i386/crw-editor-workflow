# CRW Editor Workflow

OpenCode skills, commands, scripts, and playbooks for helping Consumer Rights Wiki editors improve article quality.

The repo is designed around reviewable editorial assistance. Agents should help editors inspect pages, draft fixes, validate Cargo data, split misplaced incident content, and package edits for human review. They should not publish directly unless a human explicitly asks.

## Quick Start

From this directory:

```sh
python3 scripts/fetch_cargo_export.py
python3 scripts/cargo_quality_report.py data/snapshots/all_cargo_combined.json --markdown reports/cargo-quality.md
```

Then open the repo with OpenCode. It will discover:

- `AGENTS.md` as project instructions.
- `.opencode/skills/*/SKILL.md` as task-specific skills.
- `.opencode/commands/*.md` as slash commands.

## OpenCode Commands

- `/cargo-quality-sweep`
- `/fix-one-cargo-page`
- `/split-embedded-incident`
- `/suggestion-to-draft`
- `/source-hardening-pass`
- `/tone-and-risk-pass`
- `/video-transcript-to-page`

## Core Workflows

- Cargo quality sweeps from the latest Cargo export.
- Minimal Cargo template fixes for individual pages.
- Splitting incident content out of company/product/product-line pages.
- Turning article suggestions into sourced article briefs.
- Turning video transcripts into article briefs, source maps, suggestion rows, drafts, or patches.
- Source hardening passes.
- Tone and legal-risk cleanup passes.

## Safety Model

The default output should be an edit bundle:

- Proposed wikitext or diff.
- Sources checked.
- Unsupported claims.
- Cargo changes.
- Formatting risks.
- Suggested edit summary.

Publishing remains a human editor decision.
