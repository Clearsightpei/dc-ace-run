# Drawer memory

Curator-owned. Notes for the next Drawer subagent based on what
previous attempts actually produced vs the ground truths.

---

## Status of the basic 3 strokes

| key  | char | cycle 1 visual | cycle 2 visual | status                                |
|------|------|----------------|----------------|---------------------------------------|
| heng | 横   | 0.28           | **0.74**       | **passed** (≥0.7 threshold); also OCR'd as '一' @ 0.75 — a clean heng IS visually the character 一 |
| shu  | 竖   | 0.33           | **1.00**       | **passed** with perfect score; stable |
| pie  | 撇   | 0.15           | 0.40           | still failing — direction now correct, but curve too shallow |

Cycle 2 was a *carry-over* of the cycle-1 batch with no parameter
changes from the Teacher. The score jump (avg 0.25 → 0.71) came
entirely from this memory file. Memory transfer is working.

---

## Recipes that work

### 横 (heng) — horizontal — cycle 2 score 0.74
```python
t.penup(); t.goto(-35, 0); t.setheading(4)  # slight upward tilt
t.pendown(); t.forward(70); t.penup()
```
Lesson: **length ~70 pixels**, tilt 3°–5° (faint upward). The Drawer
in cycle 2 used 70px and `setheading(4)` and scored 0.74. The
remaining gap to 1.0 is mostly placement noise — getting closer than
0.74 is hard without exact pixel placement.

### 竖 (shu) — vertical — cycle 2 score 1.00
```python
t.penup(); t.goto(0, 35); t.setheading(270)  # due south
t.pendown(); t.forward(70); t.penup()
```
Lesson: starting at (0, 35) heading south for 70 pixels lands exactly
on the GT centerline. No tilt, no curve. **This is solved.**

---

## Recipes that need refinement

### 撇 (pie) — left-falling sweep — cycle 2 score 0.40

The cycle-2 attempt got the direction right (start upper-right, sweep
down-left, convex right) but the curve was **too shallow**. The
Drawer used:

```python
t.penup(); t.goto(24.5, 35); t.setheading(260)
t.pendown()
for _ in range(35):
    t.forward(2)         # = 70 / 35
    t.right(50 / 35)     # ≈ 1.43° per step, total 50° rotation
t.penup()
```

Compared to the GT, the resulting arc is too straight — not enough
bend. The fix is **more total rotation and more steps**:

- Target rotation: roughly **60°** total (not 50°).
- Step count: around **60 steps** of `forward(70/60)` with
  `t.right(1)` each (1° per step is a natural pattern).
- Starting heading is still ~260° (south, slightly west of south).
- Start position around (+24, +35) is roughly right; the GT pie has
  its top end at roughly upper-right of canvas center.

In other words: keep the same general shape but make the curve more
pronounced by rotating further over more steps.

---

## Canvas conventions (confirmed working)

- 800 × 600 white background, pensize 3, black pen.
- `screen.tracer(0, 0)` then `screen.update()` for fast rendering;
  do NOT mix in module-level `turtle.tracer/update`.
- Helper between tasks: `t.reset(); t.hideturtle(); t.speed(0);
  t.pencolor("black"); t.pensize(3); t.penup(); t.goto(0,0);
  t.setheading(90)`.
- **Do NOT call `screen.bye()` between tasks** — it destroys the
  global turtle state.
- Save via `canvas.postscript()` → PIL → `.png`.

---

## Coordinate sense reminder

- Turtle x grows right (east); y grows UP (north).
- `setheading(0)` = east; 90 = north; 180 = west; 270 = south.
- `t.right(deg)` rotates clockwise (heading decreases mod 360).
- `t.left(deg)` rotates counterclockwise (heading increases).
- For `t.circle(r, extent)`: positive r → arc curves to turtle's LEFT
  (CCW); negative r → curves to turtle's RIGHT (CW).

---

## Observed OCR quirks (not actionable yet, but record)

- Cycle 2 heng was OCR'd as **'一' @ 0.75** (high confidence). A
  clean horizontal stroke visually IS the character 一 — this is
  expected and not a problem.
- Cycle 2 shu was OCR'd as **'一' @ 0.33** (low confidence). The
  judge's preprocessing pads to square, which flattens aspect ratio
  of a vertical line. OCR misreads it as 一. This is a preprocessing
  artifact; the drawing is correct.
- Cycle 1 pie was OCR'd as **'一' @ 0.13** (very low). That cycle's
  pie was so shallow it looked horizontal.

The point: in Phase 1, `is_correct` is structurally False (lone
strokes aren't characters), but OCR's *guesses* tell you whether
your stroke looks like a recognizable character. If a heng is OCR'd
as '一' with high confidence, you've drawn it well.

---

## What to try next cycle if pie repeats

Increase rotation total to 60° (was 50°). Try ~60 steps of
`forward(70/60)` + `t.right(1)` per step. Keep start at (24, 35)
and heading 260°.
