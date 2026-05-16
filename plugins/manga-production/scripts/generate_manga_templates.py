#!/usr/bin/env python3
"""Generate reusable manga manuscript bases and panel layout templates."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


PAGE_SIZE = (1024, 1536)
BLACK = (12, 12, 12)
WHITE = (255, 255, 255)
GUIDE = (180, 180, 180)
SAFE = (215, 215, 215)
PLUGIN_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_DIR = (
    PLUGIN_ROOT
    / "skills"
    / "manga-generation"
    / "assets"
    / "Manga_Panel_Layout_Template"
)


LEGACY_TEMPLATES = [
    {
        "id": "legacy-skewed-6-panel",
        "file": "Manga Panel Layout Template1.png",
        "kind": "panel-layout",
        "panel_count": 6,
        "best_for": ["action", "turning point", "large central beat"],
        "description": "Two top panels, one wide central panel, and three small bottom panels with dynamic skew.",
    },
    {
        "id": "legacy-balanced-5-panel",
        "file": "Manga Panel Layout Template2.png",
        "kind": "panel-layout",
        "panel_count": 5,
        "best_for": ["balanced scene", "conversation", "setup and reveal"],
        "description": "One wide opening panel followed by two rows of paired panels.",
    },
    {
        "id": "legacy-dense-7-panel",
        "file": "Manga Panel Layout Template3.png",
        "kind": "panel-layout",
        "panel_count": 7,
        "best_for": ["dense dialogue", "multi-beat sequence", "investigation"],
        "description": "A wide top panel followed by three rows of two smaller panels.",
    },
    {
        "id": "legacy-staggered-6-panel",
        "file": "Manga Panel Layout Template4.png",
        "kind": "panel-layout",
        "panel_count": 6,
        "best_for": ["reaction chain", "uneven tension", "dramatic reveal"],
        "description": "A wide top panel with staggered lower panels and one tall right-side panel.",
    },
    {
        "id": "legacy-dynamic-6-panel",
        "file": "Manga Panel Layout Template5.png",
        "kind": "panel-layout",
        "panel_count": 6,
        "best_for": ["fast action", "chase", "impact page"],
        "description": "Slanted gutters and asymmetric panels for high-energy page movement.",
    },
    {
        "id": "legacy-yonkoma-4-panel",
        "file": "4-panel manga template1.png",
        "kind": "panel-layout",
        "panel_count": 4,
        "best_for": ["yonkoma", "gag", "simple four-beat scene"],
        "description": "Four stacked horizontal panels for classic four-panel timing.",
    },
    {
        "id": "legacy-grid-8-panel",
        "file": "4-panel manga template2.png",
        "kind": "panel-layout",
        "panel_count": 8,
        "best_for": ["dense sequence", "short dialogue beats", "parallel reactions"],
        "description": "Two-column grid with eight panels in manga-style numbered order.",
    },
]


def load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def draw_centered_text(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str) -> None:
    font = load_font(96)
    text_box = draw.textbbox((0, 0), text, font=font)
    width = text_box[2] - text_box[0]
    height = text_box[3] - text_box[1]
    x = box[0] + (box[2] - box[0] - width) / 2
    y = box[1] + (box[3] - box[1] - height) / 2
    draw.text((x, y), text, fill=BLACK, font=font)


def draw_rect_panel(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    number: int | None = None,
    width: int = 7,
) -> None:
    draw.rectangle(box, outline=BLACK, width=width)
    if number is not None:
        draw_centered_text(draw, box, str(number))


def create_canvas(size: tuple[int, int] = PAGE_SIZE) -> Image.Image:
    return Image.new("RGB", size, WHITE)


def save_base_simple(path: Path) -> None:
    image = create_canvas()
    draw = ImageDraw.Draw(image)
    draw.rectangle((52, 52, 972, 1484), outline=BLACK, width=6)
    draw.rectangle((96, 96, 928, 1440), outline=SAFE, width=3)
    image.save(path)


def save_base_bleed(path: Path) -> None:
    image = create_canvas()
    draw = ImageDraw.Draw(image)
    draw.rectangle((24, 24, 1000, 1512), outline=GUIDE, width=3)
    draw.rectangle((64, 64, 960, 1472), outline=BLACK, width=5)
    draw.rectangle((112, 112, 912, 1424), outline=SAFE, width=3)
    draw.line((64, 768, 960, 768), fill=(235, 235, 235), width=2)
    draw.line((512, 64, 512, 1472), fill=(235, 235, 235), width=2)
    image.save(path)


def save_base_yonkoma(path: Path) -> None:
    image = create_canvas((887, 1774))
    draw = ImageDraw.Draw(image)
    draw.rectangle((36, 36, 851, 1738), outline=BLACK, width=6)
    draw.rectangle((72, 72, 815, 1702), outline=SAFE, width=3)
    image.save(path)


def save_layout_3(path: Path) -> None:
    image = create_canvas()
    draw = ImageDraw.Draw(image)
    draw_rect_panel(draw, (48, 48, 976, 570), 1)
    draw_rect_panel(draw, (48, 615, 500, 1488), 3)
    draw_rect_panel(draw, (524, 615, 976, 1488), 2)
    image.save(path)


def save_layout_4(path: Path) -> None:
    image = create_canvas((887, 1774))
    draw = ImageDraw.Draw(image)
    panels = [
        (36, 36, 851, 420),
        (36, 464, 851, 848),
        (36, 892, 851, 1276),
        (36, 1320, 851, 1738),
    ]
    for idx, box in enumerate(panels, start=1):
        draw_rect_panel(draw, box, idx, width=8)
    image.save(path)


def save_layout_5(path: Path) -> None:
    image = create_canvas()
    draw = ImageDraw.Draw(image)
    draw_rect_panel(draw, (48, 48, 976, 460), 1)
    draw_rect_panel(draw, (48, 505, 500, 950), 3)
    draw_rect_panel(draw, (524, 505, 976, 950), 2)
    draw_rect_panel(draw, (48, 995, 500, 1488), 5)
    draw_rect_panel(draw, (524, 995, 976, 1488), 4)
    image.save(path)


def save_layout_6(path: Path) -> None:
    image = create_canvas()
    draw = ImageDraw.Draw(image)
    draw_rect_panel(draw, (48, 48, 500, 430), 2)
    draw_rect_panel(draw, (524, 48, 976, 430), 1)
    draw_rect_panel(draw, (48, 475, 976, 930), 3)
    draw_rect_panel(draw, (48, 975, 330, 1488), 6)
    draw_rect_panel(draw, (354, 975, 670, 1488), 5)
    draw_rect_panel(draw, (694, 975, 976, 1488), 4)
    image.save(path)


GENERATED_TEMPLATES = [
    {
        "id": "blank-manuscript-simple-portrait",
        "file": "blank-manuscript-simple-portrait.png",
        "kind": "blank-base",
        "panel_count": 0,
        "best_for": ["custom layout", "cover", "chapter opener"],
        "description": "Portrait manuscript base with outer trim and inner safe area.",
        "writer": save_base_simple,
    },
    {
        "id": "blank-manuscript-bleed-safe-portrait",
        "file": "blank-manuscript-bleed-safe-portrait.png",
        "kind": "blank-base",
        "panel_count": 0,
        "best_for": ["custom page", "print-aware composition", "full-page illustration"],
        "description": "Portrait manuscript base with bleed, trim, safe area, and center guides.",
        "writer": save_base_bleed,
    },
    {
        "id": "blank-manuscript-yonkoma-tall",
        "file": "blank-manuscript-yonkoma-tall.png",
        "kind": "blank-base",
        "panel_count": 0,
        "best_for": ["yonkoma custom layout", "vertical gag strip"],
        "description": "Tall manuscript base for four-panel vertical manga pages.",
        "writer": save_base_yonkoma,
    },
    {
        "id": "generated-layout-3-panel-establishing",
        "file": "generated-layout-3-panel-establishing.png",
        "kind": "panel-layout",
        "panel_count": 3,
        "best_for": ["establishing beat", "slow reveal", "quiet scene"],
        "description": "One wide top panel with two lower vertical panels for setup and reaction.",
        "writer": save_layout_3,
    },
    {
        "id": "generated-layout-4-panel-yonkoma",
        "file": "generated-layout-4-panel-yonkoma.png",
        "kind": "panel-layout",
        "panel_count": 4,
        "best_for": ["yonkoma", "gag timing", "four-beat exchange"],
        "description": "Four stacked panels for compact gag or slice-of-life pacing.",
        "writer": save_layout_4,
    },
    {
        "id": "generated-layout-5-panel-balanced",
        "file": "generated-layout-5-panel-balanced.png",
        "kind": "panel-layout",
        "panel_count": 5,
        "best_for": ["balanced scene", "setup escalation hook"],
        "description": "Wide opening panel followed by two rows of paired panels.",
        "writer": save_layout_5,
    },
    {
        "id": "generated-layout-6-panel-rhythm",
        "file": "generated-layout-6-panel-rhythm.png",
        "kind": "panel-layout",
        "panel_count": 6,
        "best_for": ["action rhythm", "central dramatic beat", "reaction sequence"],
        "description": "Two top panels, one wide middle panel, and three compact lower panels.",
        "writer": save_layout_6,
    },
]


def write_manifest(output_dir: Path) -> None:
    entries = []
    for entry in LEGACY_TEMPLATES:
        path = output_dir / entry["file"]
        item = {key: value for key, value in entry.items() if key != "writer"}
        if path.exists():
            with Image.open(path) as image:
                item["size"] = list(image.size)
        else:
            item["size"] = None
        entries.append(item)

    for entry in GENERATED_TEMPLATES:
        path = output_dir / entry["file"]
        item = {key: value for key, value in entry.items() if key != "writer"}
        with Image.open(path) as image:
            item["size"] = list(image.size)
        entries.append(item)

    manifest = {
        "schema_version": 1,
        "template_folder": "assets/Manga_Panel_Layout_Template",
        "reading_order": "Use visible panel numbers as the panel IDs and reading order.",
        "default_max_pages": 5,
        "templates": entries,
    }
    (output_dir / "template_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def generate(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for entry in GENERATED_TEMPLATES:
        entry["writer"](output_dir / entry["file"])
    write_manifest(output_dir)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Directory where manuscript template PNGs and template_manifest.json are written.",
    )
    args = parser.parse_args()
    output_dir = Path(args.output_dir) if args.output_dir else DEFAULT_OUTPUT_DIR
    generate(output_dir)


if __name__ == "__main__":
    main()
