# AGENTS.md

Project instructions for coding agents working in this repository.

## Skill Structure

- This repository is a single Codex skill package, not a plugin. Keep the published skill rooted at the repository root.
- Keep `SKILL.md`, `agents/`, `assets/`, `references/`, and `scripts/` at the repository root so the skill remains self-contained for GitHub distribution.
- Store manga page template assets under `assets/Manga_Panel_Layout_Template/`.
- When changing template assets or the template manifest, run `python3 scripts/generate_manga_templates.py` and verify `template_manifest.json` still references `assets/Manga_Panel_Layout_Template`.
- Keep generated manga output under `output/manga-pages/`; it is local runtime output and should not be committed.
- Do not add manifest wrappers, marketplace files, or `.codex-plugin/` metadata unless the project is intentionally converted away from a plain skill package.
