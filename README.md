<table>
  <thead>
    <tr>
      <th style="text-align:center"><a href="README_ja.md">日本語</a></th>
      <th style="text-align:center"><a href="README.md">English</a></th>
    </tr>
  </thead>
</table>

# Manga Generation Skill for Codex

Manga Generation is a Codex skill for planning and generating colorful manga pages from story drafts, character references, and style notes. It expands a draft into page beats, selects bundled manga page templates, writes panel-by-panel briefs, and uses `$imagegen` to render each completed manga page as one full page instead of separate panel images or code-composited layouts.

## Features

- Plans manga pages from a draft, script, or story premise.
- Supports three expansion modes: `Original`, `Slight Expansion`, and `Expansion`.
- Selects from bundled blank manuscript bases and numbered manga panel layouts.
- Produces page plans with template choice, page purpose, continuity notes, drawing briefs, dialogue, sound effects, and balloon placement.
- Guides `$imagegen` to create complete full-color manga pages with preserved panel borders and gutters.
- Uses templates and user-provided images as role-labeled references for image generation, not as pasted or Python-composited assets.
- Keeps generated manga pages under `output/manga-pages/`, which is ignored by Git.

## Template Preview

The skill bundles reusable manga page templates under `assets/Manga_Panel_Layout_Template/`.

<img src="assets/Manga_Panel_Layout_Template/generated-layout-5-panel-balanced.png" alt="Five-panel manga page template" width="480">

## Requirements

- Codex with skill support.
- `$imagegen` availability when generating final manga page images.
- Python 3 with Pillow available only when regenerating template PNGs with `generate_manga_templates.py`.

No API keys, credentials, or environment variables are defined by this repository.

## Installation

Clone or copy this repository as a skill folder named `manga-generation` under your Codex skills directory:

```text
~/.codex/skills/manga-generation
```

The required skill entry point is:

```text
SKILL.md
```

## Usage

Invoke the skill from Codex with a story draft and any relevant reference images:

```text
Use $manga-generation to make a 5-page colorful manga from my draft and references.
```

You can also specify an expansion mode:

```text
Use $manga-generation in Slight Expansion mode for this story draft.
```

By default, the skill uses:

- Expansion mode: `Original`
- Maximum pages/images: `5`
- Template folder: `assets/Manga_Panel_Layout_Template/` relative to the skill directory
- Output folder: `output/manga-pages/` relative to the repository root

The skill plans each page before generation. Each `$imagegen` request should generate one complete colorful manga page containing all panels, borders, speech balloons, dialogue, sound effects, and page composition.

Template PNGs are only references for page geometry. Final pages should be drawn by imagegen from the template, story plan, and user reference images rather than assembled with Python or pasted source images.

## Development

Regenerate deterministic blank manuscript bases, generated panel templates, and `template_manifest.json` with:

```bash
python3 scripts/generate_manga_templates.py
```

The script writes to:

```text
assets/Manga_Panel_Layout_Template/
```

Keep the skill self-contained at the repository root so it remains publishable from GitHub.

## Project Structure

```text
.
├── SKILL.md
├── agents/openai.yaml
├── assets/Manga_Panel_Layout_Template/
├── references/
├── scripts/generate_manga_templates.py
├── AGENTS.md
├── LICENSE
└── README.md
```

## Privacy

This skill stores no credentials and defines no external service integration. Manga drafts, reference images, generated page plans, and output images stay in the active Codex workspace unless the user explicitly shares them elsewhere.

## License

This repository is licensed under the MIT License. See [LICENSE](LICENSE).
