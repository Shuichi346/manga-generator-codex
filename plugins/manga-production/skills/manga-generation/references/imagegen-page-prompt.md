# Imagegen Page Prompt Scaffold

Use this scaffold with `$imagegen` for each page. Replace bracketed text before generation.

```text
Use case: illustration-story
Asset type: completed manga page
Primary request: Generate Page [N] as one complete black-and-white manga page, not separate panels.
Input images: [Image 1: selected panel layout template; Image 2: character reference; Image 3: style/reference image]
Panel layout: Use the selected template's panel borders and numeric panel order. Preserve the same number of panels and clear gutters. Do not add extra panels.
Story context: [one-sentence page context]
Continuity: [outfits, props, setting, character design invariants]
Style/medium: polished black-and-white manga, clean ink linework, screentone shading, expressive faces, readable speech balloons.
Composition/framing: Follow the template geometry; each panel should match its brief.

Panel 1:
Draw: [subject/action/camera/background]
Dialogue: "[exact text or none]"
SFX: "[exact text or none]"
Balloon/caption placement: [placement]

Panel 2:
Draw: [subject/action/camera/background]
Dialogue: "[exact text or none]"
SFX: "[exact text or none]"
Balloon/caption placement: [placement]

Constraints: Generate the whole page in one image; keep panel borders clean; keep gutters white; do not include panel-number placeholders in final art unless the user explicitly wants numbered templates; no unrelated text; no watermark; preserve character reference features.
Avoid: extra characters, extra panels, cropped dialogue, unreadable lettering, inconsistent costumes, logo marks.
```
