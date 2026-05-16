# Manga Production Plugin for Codex

This repository contains a Codex plugin for manga production. The plugin helps Codex turn user-provided story drafts, character references, and prepared images into planned manga pages, then generate complete page images with `$imagegen`.

## Contents

- `plugins/manga-production/`: Codex plugin manifest, skill, icon, and template generation script.
- `plugins/manga-production/skills/manga-generation/`: Skill instructions for story expansion, template selection, panel planning, and page-level image generation.
- `plugins/manga-production/skills/manga-generation/assets/Manga_Panel_Layout_Template/`: Bundled blank manuscript bases and manga page panel layout templates.

## Workflow

1. Provide Codex with a story draft, character references, and any prepared images.
2. Invoke `$manga-generation`.
3. Choose an expansion mode: `Original`, `Slight Expansion`, or `Expansion`.
4. Optionally specify the maximum number of manga pages. The default is 5.
5. Codex plans each page and generates each completed manga page as one image.

Final generated pages should be saved under `output/manga-pages/`, which is ignored by Git.

## Publishing Checklist

- Replace `OWNER/REPOSITORY` in `plugins/manga-production/.codex-plugin/plugin.json` with the final GitHub repository URL.
- Replace `maintainers@example.com` with the maintainer contact address.
- Keep `.codex-plugin/plugin.json`, `skills/`, `assets/`, and `scripts/` inside `plugins/manga-production/` so the plugin remains self-contained.

## Privacy

This plugin stores no credentials and defines no external service integration. Manga drafts, reference images, generated page plans, and output images stay in the active Codex workspace unless the user explicitly shares them elsewhere.

## Terms Of Use

Use of this plugin is governed by the MIT license in this repository.
