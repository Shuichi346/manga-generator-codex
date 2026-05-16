# Notes

## 2026-05-16

- The manga template assets were kept inside `plugins/manga-production/skills/manga-generation/assets/Manga_Panel_Layout_Template/` so the plugin does not depend on repository-root assets when published.
- The plugin manifest repository, homepage, website, privacy, and terms URLs were set to `https://github.com/Shuichi346/manga-generator-codex`.
- The maintainer contact email remained `maintainers@example.com` because no final contact address was provided.
- The manga-generation workflow was revised so template PNGs and user images are role-labeled imagegen references. Final manga pages must be full-color imagegen renders, not Python/Pillow compositing output.
