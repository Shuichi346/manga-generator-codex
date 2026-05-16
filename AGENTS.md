# AGENTS.md

Project instructions for coding agents working in this repository.

## Plugin Structure

- Keep the published plugin rooted at `plugins/manga-production/`.
- Keep `.codex-plugin/plugin.json`, `skills/`, `assets/`, and `scripts/` inside `plugins/manga-production/` so the plugin remains self-contained for GitHub distribution.
- Store manga page template assets under `plugins/manga-production/skills/manga-generation/assets/Manga_Panel_Layout_Template/`; do not move them back to a repository-root template folder.
- When changing template assets or the template manifest, run `python3 plugins/manga-production/scripts/generate_manga_templates.py` and verify `template_manifest.json` still references `assets/Manga_Panel_Layout_Template`.
- Keep generated manga output under `output/manga-pages/`; it is local runtime output and should not be committed.
- Before publishing, replace `maintainers@example.com` in `plugins/manga-production/.codex-plugin/plugin.json` with the final maintainer contact address.
