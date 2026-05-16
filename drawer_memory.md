# Drawer memory

Curator-owned. Notes for the next Drawer subagent based on what
previous attempts actually produced vs the ground truths.

---

## Status of the basic 3 strokes

| key  | char | cycle 1 visual | cycle 2 visual | status                                |
|------|------|----------------|----------------|---------------------------------------|
| heng | 横   | 0.28           | **0.74**       | **passed** (≥0.7 threshold); also OCR'd as '一' @ 0.75 — a clean heng IS visually the character 一 |
| shu  | 竖   | 0.33           | **1.00**       | **passed** with perfect score; stable |
| pie  | 撇   | 0.15           | 0.40 → **1.00** (c3) | **solved** — the cycle-3 ~60° rotation fix landed perfectly |
| ti   | 提   | —              | **0.95** (c3, first attempt) | **passed** — straight rising flick from text alone |
| na   | 捺   | —              | 0.22 (c3, first attempt) | failing — over-curled (reused pie's curvature) |

Memory transfer is working: avg visual 0.25 (c1) → 0.71 (c2) → 0.72
(c3). pie went 0.40 → 1.00 the moment the Curator's exact rotation
fix was in memory — strongest single-entry transfer signal so far.
**Key lesson from c3: do NOT reuse one stroke's curvature for
another. Each stroke has its own bend.**

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

### 捺 (na) — right-falling press — cycle 3 score 0.22

The Drawer treated na as a mirror of pie and reused **pie's 60°
rotation over 70px** (with `t.left(1)`). Result: a tight little
curl, far too short and far too curved — it looked like a comma/hook,
not a press stroke. Compared to the GT:

- **na is much straighter than pie.** Its body is nearly a straight
  diagonal that only gently bows; the curvature *decreases* toward
  the end (the tail flattens out — that flattening is the defining
  feature of a 捺).
- The GT na descends from upper-left to lower-right over roughly the
  same ~70px length but with only a **gentle bend (~20–25° total,
  not 60°)**, and the bend should taper (more curve early, flatter
  tail).
- Direction/position were roughly OK (start upper-left ~(-24,+35),
  heading ~280° = down-and-slightly-east). The error was almost
  entirely **over-rotation**.

Fix to try next cycle: keep start (-24, 35), heading ~285–290°, 60
steps of `forward(70/60)`, but rotate only **~20° total** with
`t.left()`, and bias the rotation to the first half of the steps so
the tail flattens (e.g. `t.left(0.5)` for the first 30 steps, then
`t.left(0.15)` for the last 30). General rule: **na ≈ shallow bow,
flattening tail. pie ≈ deep 60° curve. They are NOT mirror images
in curvature — only in direction.**

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

## What to try next cycle if na repeats

na = **shallow bow with a flattening tail**, NOT a mirrored pie.
Keep start (-24, 35), heading ~285°, 60 steps of `forward(70/60)`,
but only **~20° total** left-rotation, front-loaded:
`t.left(0.5)` for steps 1–30, `t.left(0.15)` for steps 31–60.
Do not reuse pie's 60° — that over-curls it (cycle 3 scored 0.22).
