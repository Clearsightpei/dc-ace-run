# Drawer memory

Curator-owned. Notes for the next Drawer subagent based on what
previous attempts actually produced vs the ground truths.

---

## Stroke status

| key      | char | best visual | status |
|----------|------|-------------|--------|
| heng     | 横   | 0.74        | **passed** (retired) |
| shu      | 竖   | 1.00        | **solved** (retired) |
| pie      | 撇   | 1.00        | **solved** (retired) — 60° curve recipe below |
| ti       | 提   | 0.95        | **passed** (retired) — straight flick recipe below |
| na       | 捺   | 0.22→0.31   | failing — heading was too steep (see fix) |
| dian     | 点   | 0.38        | failing — drawn as a line, must be a tiny dot |
| heng_zhe | 横折 | 0.49        | failing — shape right, oversized & off-center |

Memory transfer confirmed: avg visual 0.25 (c1) → 0.71 (c2) → 0.72
(c3) → 0.39 (c4, two brand-new strokes dragged it down). pie 0.40→1.00
the moment the exact rotation fix entered memory — strongest
single-entry transfer signal.

**Key lessons:**
1. Do NOT reuse one stroke's curvature/heading for another. Each
   stroke has its own bend AND its own descent angle.
2. A wrong number in memory transfers just as faithfully as a right
   one. The c4 Drawer applied "na heading ~285°" exactly — and 285°
   was wrong (too steep). Curator must get the number right, not
   just the shape description.

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

### 撇 (pie) — left-falling sweep — cycle 3 score 1.00 **SOLVED**
```python
t.penup(); t.goto(24, 35); t.setheading(260)
t.pendown()
for _ in range(60):
    t.forward(70 / 60)
    t.right(1)            # 60 steps × 1° = 60° total rotation
t.penup()
```
Lesson: pie = ~70px length, **60° total clockwise rotation** over 60
steps, start (24,35) heading 260°. The cycle-2 version (50°) was too
shallow; 60° is exactly right. Don't change this — it scored 1.00.

### 提 (ti) — rising flick — cycle 3 score 0.95
```python
t.penup(); t.goto(-30, -20); t.setheading(30)  # up and to the right
t.pendown(); t.forward(55); t.penup()
```
Lesson: ti is a **short, straight** rising stroke — no curve. Start
lower-left, heading ~30° (up-and-right), ~55px. Scored 0.95 on the
first attempt. Solved enough; minor placement gap only.

---

## Recipes that need refinement

### 捺 (na) — right-falling press — c3 0.22, c4 0.31

Two failures. c3 over-curled (reused pie's 60°). c4 fixed the
curvature but used **heading 285°, which is far too steep** — 285°
is only 15° off straight-down, so the stroke came out nearly
vertical. The GT na is a **shallow ~45° diagonal**: it descends
from upper-left to lower-right at roughly equal x- and y-travel
(like a gentle backslash that sags), then flattens toward more
horizontal at the tail (concave-up — bows downward like the bottom
of a bowl).

Corrected fix for next attempt:
```python
t.penup(); t.goto(-30, 25); t.setheading(325)  # ~45° below horizontal, down-RIGHT
t.pendown()
for i in range(60):
    t.forward(75 / 60)
    if i < 35:
        t.left(0.55)   # early curve
    else:
        t.left(0.12)   # tail flattens toward horizontal
t.penup()
```
Why 325°: heading 0=east, 270=south. Down-and-right at ~45° is
**~315–325°**. 285° (what c4 used) is almost due south — wrong.
`t.left()` from 325° increases heading toward 360°=east, which
flattens the tail toward horizontal — correct direction. General
rule: **na = shallow ~45° descent, gentle bow, flattening tail.
pie = deep 60° curve, much steeper. Not mirror images.**

### 点 (dian) — dot — cycle 4 score 0.38

The Drawer drew an **18px diagonal line** (a mini-pie). Wrong: the
GT dian is a **tiny round dab, ~8–10px across, almost a filled
point** — it reads as a dot, not a stroke. Fix: make it very short
and blunt. Best approach — draw a small filled dot rather than a
line:
```python
t.penup(); t.goto(0, 0); t.pendown()
t.dot(10)            # a 10px filled round dot, centered
t.penup()
```
If using a stroke instead, keep it under ~8px with a fat pen. The
defining property: dian is the **smallest** stroke and is round,
not linear.

### 横折 (heng_zhe) — horizontal-fold — cycle 4 score 0.49

**Shape was correct** (horizontal segment, then a sharp ~90° fold
straight down — like a box's top-right corner). Closest of the
three c4 strokes. Two errors: (1) **too big** — used 60px + 55px;
compound strokes are more compact, use **~45px horizontal + ~45px
vertical**; (2) **off-center** — it sat up-and-left of canvas
center; the GT corner sits near center. The fold itself is right:
go east (slight up-tilt ~4°), then `t.right(94)` to head south,
then forward. Refined recipe:
```python
t.penup(); t.goto(-22, 5); t.setheading(4)
t.pendown()
t.forward(45)        # horizontal, shorter than a lone heng
t.right(94)          # fold to straight-down
t.forward(45)        # vertical drop
t.penup()
```
Lesson for compound strokes generally: **each segment is shorter
than the same stroke drawn alone** (a heng inside heng_zhe ≈ 45px,
not the 70px of a standalone heng), and the whole figure must be
recentered so its bounding box centers on the canvas.

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

## Quick reference for carry-over strokes

- **na**: heading **325°** (NOT 285° — that was too steep), shallow
  ~45° descent, front-loaded `t.left` ~25° total, flattening tail.
  See full recipe above.
- **dian**: use `t.dot(10)` at (0,0). It is a round dab, not a line.
- **heng_zhe**: ~45px + ~45px segments (shorter than a lone heng),
  recentered on canvas. Shape (right-angle fold) is already correct.
