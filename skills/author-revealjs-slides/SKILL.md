---
name: author-revealjs-slides
description: Create, edit, and structure Reveal.js lecture slides in this repo using `index.html` and `theme/custom.css`. Use when asked to draft slides, adjust layouts, reorganize sections, or enforce slide design standards for the Introduction-to-Informatics course (practical tone, 180 minutes / ~90 slides by default).
---

# Author Reveal.js Slides

## Overview
Create consistent Reveal.js slides for this repository using the existing theme and layout classes. Keep slides concise, practical, and visually structured.

## Workflow
1. Confirm scope (section/topic, target slide count, language, any must-include examples).
2. Choose layout classes that match the content (see `references/layouts.md`).
3. Draft or update slides in `index.html` (one `<section>` per slide unless vertical stacks are requested).
4. Keep text minimal, emphasize key terms with `<strong>`, and use callouts for metrics or guidance.
5. Summarize edits and suggest next steps (preview, asset placement, or theme tweaks).

## Content Rules
- Keep one message per slide; 3-5 bullets max per list.
- Keep code blocks under ~12 lines; prefer pseudo-code for concepts.
- Use concrete, practical examples over abstract definitions.
- Default language to the user's request (Japanese if the request is in Japanese).
- Use horizontal slides by default; use vertical stacks only when explicitly requested.
- Aim for ~2 minutes per slide when targeting 180 minutes / 90 slides.

## Writing & Pacing
- Prefer verb-led headlines (e.g., "Map the data flow", "Define the handoff").
- Avoid long paragraphs; break into bullets or a callout.
- Add one "decision" slide per section (trade-offs or constraints).
- Use numbers or metrics when possible to keep it practical.

## Repo Conventions
- Slides live in `index.html`.
- Theme and layout classes live in `theme/custom.css`.
- Images/diagrams go in `assets/` and are referenced relatively (e.g., `assets/diagram.png`).
- Maintain the light, subtle gray background and high-contrast text.

## Common Tasks
- Add a new section: insert a `layout-section` slide as a divider, then related slides after it.
- Add examples: prefer `layout-2col` or `layout-image-left/right` with a `callout`.
- Compare options: use `layout-table` or `layout-3col`.
- Quote/definition: use `layout-quote` with a short attribution line.

## Automation
- Generate a section divider + placeholder slides with `scripts/new_section.py`.
- Example: `python3 skills/author-revealjs-slides/scripts/new_section.py "Data Flow" --subtitle "Ingest to serve" --count 3`

## References
- Layout class list and HTML snippets: `references/layouts.md`
- Writing guidance: `references/writing.md`
