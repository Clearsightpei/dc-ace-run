#!/usr/bin/env python3
"""Render a single Chinese character as a ground-truth PNG using stroke medians.

Reads MakeMeAHanzi-format graphics.txt (one JSON object per line, with a
'medians' field giving stroke skeleton coordinates in 0–1024 space, with
y-axis flipped relative to standard screen coords).

Usage:
    python tools/make_char_gt.py <character> <output_path> [--scale N]

Default graphics.txt path: ../draw_character/graphics.txt
Override with $GRAPHICS_TXT environment variable.
"""

import argparse
import io
import json
import os
import sys
import turtle

from PIL import Image

WIDTH = 800
HEIGHT = 600

DEFAULT_GRAPHICS = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "..", "draw_character", "graphics.txt",
)


def load_character(graphics_path, char):
    with open(graphics_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                continue
            if item.get("character") == char:
                return item
    return None


def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    b = io.BytesIO(ps.encode("utf-8"))
    img = Image.open(b)
    img.load(scale=1)
    img.convert("RGBA").save(path, "PNG")


def render(char, out_path, scale=0.4, graphics_path=None):
    graphics_path = graphics_path or os.environ.get("GRAPHICS_TXT", DEFAULT_GRAPHICS)
    if not os.path.exists(graphics_path):
        print(f"graphics.txt not found at {graphics_path}", file=sys.stderr)
        print("Set $GRAPHICS_TXT or pass --graphics", file=sys.stderr)
        sys.exit(2)

    item = load_character(graphics_path, char)
    if item is None:
        print(f"Character '{char}' not found in {graphics_path}", file=sys.stderr)
        sys.exit(1)

    medians = item["medians"]

    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    turtle.tracer(0, 0)
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pencolor("black")
    t.pensize(4)

    for stroke in medians:
        if not stroke:
            continue
        # Source coords are 0–1024, origin top-left, y grows downward.
        # Center at (0,0) and flip y for turtle's bottom-left origin.
        def to_xy(p):
            x, y = p
            tx = (x - 512) * scale
            ty = (512 - y) * scale
            return tx, ty

        x0, y0 = to_xy(stroke[0])
        t.penup(); t.goto(x0, y0); t.pendown()
        for p in stroke[1:]:
            t.goto(*to_xy(p))
        t.penup()

    turtle.update()
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    save_canvas_to_png(screen, out_path)
    try:
        screen.bye()
    except Exception:
        pass

    print(f"Wrote {out_path}  (character={char}, {len(medians)} strokes, scale={scale})")


def main():
    parser = argparse.ArgumentParser(description="Render a Chinese character to PNG using median strokes.")
    parser.add_argument("character", help="The Chinese character to render (e.g. '人')")
    parser.add_argument("output_path", help="Output PNG path")
    parser.add_argument("--scale", type=float, default=0.4, help="Coordinate scale (default 0.4 → ~400px)")
    parser.add_argument("--graphics", default=None, help="Path to graphics.txt (overrides $GRAPHICS_TXT)")
    args = parser.parse_args()
    render(args.character, args.output_path, scale=args.scale, graphics_path=args.graphics)


if __name__ == "__main__":
    main()
