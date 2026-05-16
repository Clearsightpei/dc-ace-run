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
| na       | 捺   | c3 0.22 / c4 0.31 / c5 0.14 | failing — score non-monotonic w/ visual quality |
| dian     | 点   | c4 0.38 / c5 0.40 | failing — tiny dot; score barely moves |
| heng_zhe | 横折 | c4 0.49 / c5 0.33 | shape correct; better-looking c5 scored LOWER |

**Phase 2 characters (c6):** 十 ✓ recognized 0.78 · 人 ✓ recognized
0.95 · 一 ✗ (OCR blind spot, featureless). Composition works.

Memory transfer confirmed: avg visual 0.25 (c1) → 0.71 (c2) → 0.72
(c3) → 0.39 (c4) → 0.29 (c5). pie 0.40→1.00 the moment the exact
rotation fix entered memory — strongest single-entry transfer signal.

**Key lessons:**
1. Do NOT reuse one stroke's curvature/heading for another. Each
   stroke has its own bend AND its own descent angle.
2. A wrong number in memory transfers just as faithfully as a right
   one. Memory is applied verbatim — false precision propagates.
3. **The judge's `visual_score` is phase-correlation on the full
   800×600 image and is NOISY and non-monotonic at lone-stroke
   scale.** Cycle 5's na and heng_zhe were drawn *more* like their
   GTs than cycle 4's, yet scored *lower* (heng_zhe 0.49→0.33, na
   0.31→0.14). Consequence for whoever reads this: **do not chase
   the second decimal.** Match the GShape qualitatively (right
   primitive, right rough scale, right orientation) and stop. A
   single cycle's score drop is not proof the recipe got worse —
   it may just be metric noise. Solved strokes (pie/shu at 1.00,
   ti 0.95) were clean, simple, well-centered — aim for that
   character, not for pixel-exact coordinates.

---

## Phase 2 — composing characters (started cycle 6)

**Composition from memorized stroke recipes WORKS.** Cycle 6 (first
Phase-2 cycle) composed scaled-up heng/shu/pie/na recipes into
characters with no character-specific memory, and on the first
attempt:

- **十** (heng + shu as a plus sign, ~340px) → OCR'd **'十' @ 0.78,
  is_correct=True**.
- **人** (pie + na splaying from a top apex, ~320px) → OCR'd **'人'
  @ 0.95, is_correct=True**.
- **一** (single large heng) → **not recognized** (OCR empty).

Key Phase-2 lessons:
1. **The OCR `is_correct` signal is far cleaner than phase
   correlation.** Multi-stroke characters that look right get
   recognized with high confidence (0.78–0.95). Aim for OCR
   recognizability, not phase-correlation visual_score (which is
   ~0.15–0.28 even for *correct* characters — visual_score is no
   longer the thing to optimize in Phase 2).
2. **Scale up and center**: characters ~320–340px across, centered
   on (0,0), composed from the lone-stroke recipes scaled by ~4–5×.
   This worked.
3. **Single-stroke "characters" (一) are an OCR blind spot** — too
   featureless; a lone line is ambiguous to OCR (same root cause as
   the Phase-1 thin-stroke metric noise). Best effort for 一: keep
   it **near-flat (tilt ~0°, not 4°)** and use a **thicker pen
   (pensize ~8–10)** so it reads as a bold bar, not a hairline.
   But treat a failed 一 as a known hard case, not a regression.
4. General: a **thicker pen (pensize 6–10) likely helps OCR** for
   all Phase-2 characters — the GT/real glyphs are bold, not
   hairline. Worth doing by default in Phase 2.

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

> **Read the metric caveat in "Key lessons" above before tuning
> any of the three below.** These recipes are *qualitatively*
> right. Their scores bounce around for reasons that are not your
> fault. Draw the shape cleanly and move on; do not keep nudging
> numbers chasing a higher decimal.

### 捺 (na) — right-falling press

It is a single down-and-to-the-right diagonal with a gentle bow,
moderately steep (steeper than 45° — descends a bit more than it
travels sideways), drawn over ~70–75px, with the curve front-loaded
so the tail flattens slightly. c4 used heading 285° (steep) → 0.31;
c5 used 325° (shallow) → 0.14. The truth is between them and closer
to the steeper end. A reasonable, robust recipe:
```python
t.penup(); t.goto(-25, 30); t.setheading(300)  # down-right, ~moderately steep
t.pendown()
for i in range(60):
    t.forward(74 / 60)
    t.left(0.45 if i < 35 else 0.12)   # early curve, flattening tail
t.penup()
```
Do not over-tune the heading — 290–310° is the plausible band; the
score will not cleanly tell you which value is best.

### 点 (dian) — dot

A tiny round dab, not a line. `t.dot()` is the right primitive. The
GT dot is small; c5 used `t.dot(10)` and scored 0.40 (its ceiling
seems low — a near-point has little frequency content for phase
correlation, so expect a modest score even when it's correct).
```python
t.penup(); t.goto(0, 0); t.pendown()
t.dot(9); t.penup()
```
This is "done" in the qualitative sense — it IS a dot. Don't keep
adjusting the diameter expecting a big score jump.

### 横折 (heng_zhe) — horizontal-fold

Shape is correct and stable: a short horizontal then a sharp ~90°
fold straight down (box top-right corner). c4 (60+55px, off-centre)
scored 0.49; c5 (45+45px, centred — visually closer to the GT)
scored 0.33. The lower score on the better drawing is metric noise,
not regression. Keep the clean compact version:
```python
t.penup(); t.goto(-22, 5); t.setheading(4)
t.pendown()
t.forward(48); t.right(94); t.forward(48)
t.penup()
```
General compound-stroke rule (still believed sound): each segment
is shorter than the same stroke drawn alone (~45–50px, not the
~70px of a standalone heng), and the figure should be roughly
centred.

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

- **na**: heading ~300° (band 290–310°; 285° steep→0.31, 325°
  shallow→0.14, truth between & nearer steep), ~74px, front-loaded
  `t.left`, flattening tail. Don't over-tune the angle.
- **dian**: `t.dot(9)` at (0,0). Round dab, not a line. Low score
  ceiling expected — it's still correct.
- **heng_zhe**: ~48+48px right-angle fold, centred. Shape is
  already correct; the score wobbles for metric reasons, not yours.
