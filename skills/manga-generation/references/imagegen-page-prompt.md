# Imagegen Page Prompt Scaffold

Use this scaffold with `$imagegen` for each page. Replace bracketed text before generation.

```text
Use case: illustration-story
Asset type: completed full-color manga page
Primary request: Draw Page [N] as one complete colorful manga page, not separate panels and not a pasted collage.
Page sequence: This is Page [N] of [TOTAL], generated and saved in story order. Preserve continuity from previous pages and do not depict later story beats early.
Input images: [Image 1: selected panel layout template; Image 2: character reference; Image 3: style/reference image; Image 4: scene/object reference]
Reference handling: Use the layout image as a panel geometry guide. Redraw character and object references into the manga artwork with consistent identity; do not paste or crop reference images into panels.
Panel layout: Follow the selected template's panel borders and numeric panel order. Preserve the same number of panels and clear gutters. Do not add extra panels.
Story context: [one-sentence page context]
Continuity: [outfits, props, setting, character design invariants]
Style/medium: polished full-color manga, crisp ink linework, expressive faces, cinematic color, clean cel shading with subtle painterly detail, readable speech balloons.
Color script: [hair/clothing colors, environment palette, lighting, mood, recurring motif colors]
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

Constraints: Generate the whole page in one image; keep panel borders clean; keep gutters white; remove template panel numbers from final art unless the user explicitly wants numbered templates; no unrelated text; no watermark; preserve character reference features and color continuity.
Avoid: pasted-photo collage, obvious Python/layout compositing, extra characters, extra panels, cropped dialogue, unreadable lettering, inconsistent costumes, logo marks.
```

## Prompting Notes

- Use active generation/editing verbs: `draw`, `redraw`, or `edit the layout reference by turning it into a finished manga page`.
- Treat every input image as a role-labeled reference. The prompt should say exactly what to preserve from each reference and what may change.
- For user reference images, preserve durable identity cues such as face shape, hairstyle, outfit silhouette, accessories, and color palette. Let pose, lighting, expression, and camera angle change per panel.
- Keep dialogue short. For text-heavy pages, ask imagegen for clean speech balloons and reserved lettering areas, then add exact lettering in a later pass.
