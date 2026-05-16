<table>
  <thead>
    <tr>
      <th style="text-align:center"><a href="README_ja.md">日本語</a></th>
      <th style="text-align:center"><a href="README.md">English</a></th>
    </tr>
  </thead>
</table>

# Manga Production Plugin for Codex

Manga Production is a Codex plugin for planning and generating manga pages from story drafts, character references, and style notes. It provides a `manga-generation` skill that expands a draft into page beats, selects bundled manga page templates, writes panel-by-panel briefs, and uses `$imagegen` to generate each completed manga page as one full page instead of separate panel images.

## Features

- Plans manga pages from a draft, script, or story premise.
- Supports three expansion modes: `Original`, `Slight Expansion`, and `Expansion`.
- Selects from bundled blank manuscript bases and numbered manga panel layouts.
- Produces page plans with template choice, page purpose, continuity notes, drawing briefs, dialogue, sound effects, and balloon placement.
- Guides `$imagegen` to create complete black-and-white manga pages with preserved panel borders and gutters.
- Keeps generated manga pages under `output/manga-pages/`, which is ignored by Git.

## Template Preview

The plugin bundles reusable manga page templates under `plugins/manga-production/skills/manga-generation/assets/Manga_Panel_Layout_Template/`.

<img src="plugins/manga-production/skills/manga-generation/assets/Manga_Panel_Layout_Template/generated-layout-5-panel-balanced.png" alt="Five-panel manga page template" width="480">

## Requirements

- Codex with plugin support.
- `$imagegen` availability when generating final manga page images.
- Python 3 with Pillow available only when regenerating template PNGs with `generate_manga_templates.py`.

No API keys, credentials, or environment variables are defined by this repository.

## Installation

Use the plugin root directory when adding this plugin to Codex:

```text
plugins/manga-production
```

The manifest is located at:

```text
plugins/manga-production/.codex-plugin/plugin.json
```

## Usage

Invoke the skill from Codex with a story draft and any relevant reference images:

```text
Use $manga-generation to make a 5-page manga from my draft and references.
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

The skill plans each page before generation. Each `$imagegen` request should generate one complete manga page containing all panels, borders, speech balloons, dialogue, sound effects, and page composition.

## Development

Regenerate deterministic blank manuscript bases, generated panel templates, and `template_manifest.json` with:

```bash
python3 plugins/manga-production/scripts/generate_manga_templates.py
```

The script writes to:

```text
plugins/manga-production/skills/manga-generation/assets/Manga_Panel_Layout_Template/
```

Keep the plugin self-contained under `plugins/manga-production/` so it remains publishable from GitHub.

## Project Structure

```text
.
├── plugins/manga-production/
│   ├── .codex-plugin/plugin.json
│   ├── assets/manga-production-icon.svg
│   ├── scripts/generate_manga_templates.py
│   └── skills/manga-generation/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── assets/Manga_Panel_Layout_Template/
│       └── references/
├── AGENTS.md
├── CHANGELOG.md
├── LICENSE
├── NOTES.md
└── README.md
```

## Publishing Checklist

- Replace `maintainers@example.com` in `plugins/manga-production/.codex-plugin/plugin.json` with the final maintainer contact address.
- Keep `.codex-plugin/plugin.json`, `skills/`, `assets/`, and `scripts/` inside `plugins/manga-production/`.
- Keep `plugin.json` repository, homepage, website, privacy, and terms URLs aligned with `https://github.com/Shuichi346/manga-generator-codex`.

## Privacy

This plugin stores no credentials and defines no external service integration. Manga drafts, reference images, generated page plans, and output images stay in the active Codex workspace unless the user explicitly shares them elsewhere.

## License

This repository is licensed under the MIT License. See [LICENSE](LICENSE).
