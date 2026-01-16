# AGENTS.md
Your partner is Japanease so you must report using Japanease

## Project Overview
- Reveal.js slide deck for an “Introduction to Informatics” lecture.
- Target length: 180 minutes / ~90 slides (≈2 minutes per slide).
- Audience: some prior exposure; practical, industry-oriented tone.

## Key Files & Structure
- `index.html`: main deck shell (title + agenda + markdown include).
- `slides/sections.md`: section divider slides and ordering.
- `theme/custom.css`: theme + layout classes.
- `assets/`: images/diagrams (e.g., `assets/dev-flow.png`).

## Slide Conventions
- One `<section>` per slide unless vertical stacks are explicitly requested.
- Section dividers live in `slides/sections.md` (Markdown).
- Keep bullets to 3–5 items; one message per slide.
- Prefer concrete, practical examples; avoid long paragraphs.

## Language & Copy
- Cover subtitle: English (currently “Enjoying Coding”).
- Section subtitles: Japanese.
- Agenda list: Japanese, aligned with section order.

## Visual Style
- Background is very light gray/white; keep subtle and clean.
- Use existing layout classes from `theme/custom.css` (`layout-section`, `layout-2col`, etc.).
- Use `layout-full-bleed` for image-first section slides.
- Do not implement responsive behavior or add media queries.

## Updates Checklist
- If you add/remove sections:
  - Update `slides/sections.md`.
  - Update the Agenda list in `index.html` to match.
- If you add a diagram/image:
  - Place it in `assets/`.
  - Reference it via relative path in `slides/sections.md` or slide markup.

## Generated Content Notes
- Generative AI comparisons should emphasize benchmarks; confirm sources before adding specific numbers.
- Include guardrails/safety when covering AI usage.
