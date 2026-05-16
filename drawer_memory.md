# Drawer memory

Curator-owned. Notes for the next Drawer subagent based on what the
previous attempt actually produced vs what the ground truth shows.

---

## Cycle 1 results (cold start, 0/3 visual ≥ 0.5)

You drew shapes that were *qualitatively close but quantitatively far*.
The main issues:

### 1. Scale was ~4× too large

You drew heng with `forward(300)` and shu with `forward(300)`. The
ground-truth strokes are far smaller — roughly **70–100 pixels** for
an atomic stroke on the 800×600 canvas. The judge's phase correlation
penalizes scale mismatch heavily. **For Phase-1 atomic strokes, aim
for a total stroke length around 70 pixels.**

### 2. Pie direction was reversed

You drew pie as an arc sweeping *up and to the right* (start lower-left,
end upper-right, convex downward — like a smile ⌣ ). The actual 撇 is
the opposite: it **starts at the upper-right and sweeps DOWN-AND-LEFT**,
ending in the lower-left. The curve is convex toward the RIGHT (it
bows out to the right, like a closing parenthesis `)` rotated). When
implementing pie:

- Starting heading should point roughly **south** or slightly west of
  south (i.e., the initial direction of motion is *downward*, not
  upward-right).
- The turn during the stroke should rotate the heading toward
  *west-of-south*, sweeping the stroke further leftward as it descends.
- One way to write this: start the turtle high on the canvas, set
  heading pointing roughly down, then sweep with a per-step
  `forward(small) + t.right(small_angle)` loop. This makes the
  turtle's path bow rightward as it moves down-and-left.

### 3. heng's slight upward tilt — you got this right

`setheading(3)` to `setheading(5)` gives a faint upward tilt that
matches the GT. Heng is not perfectly horizontal — there's a small
positive angle. Keep this.

### 4. shu — straight down, no tilt — also correct

`setheading(270); t.forward(...)` is the right approach. The only
issue was length.

---

## Canvas conventions confirmed

- 800 × 600 white background.
- `pensize(3)`, black pen.
- `screen.tracer(0, 0)` then `screen.update()` for fast rendering;
  do NOT mix in module-level `turtle.tracer/update`.
- Between tasks: use a helper that does `t.reset(); t.hideturtle();
  t.speed(0); t.pencolor("black"); t.pensize(3); t.penup();
  t.goto(0,0); t.setheading(90)`. **Do NOT call `screen.bye()`
  between tasks** — it destroys the global turtle state and the next
  canvas raises `Terminator`.

---

## Coordinate sense reminder

- Turtle x grows to the right (east); y grows UP (north).
- `setheading(0)` = east; `setheading(90)` = north; `setheading(180)`
  = west; `setheading(270)` = south.
- `t.right(deg)` rotates clockwise (heading decreases mod 360).
- `t.left(deg)` rotates counterclockwise (heading increases).
- For `t.circle(r, extent)`: positive radius → arc curves to the
  turtle's LEFT (CCW); negative radius → curves to the turtle's
  RIGHT (CW).

---

## What to try next cycle

If you see heng / shu / pie again: keep your overall approach but
shrink stroke lengths to ~70 pixels, and for pie reverse the sweep
direction (start high heading roughly south, curve rightward during
the descent — the stroke should *finish* lower-left, not upper-right).
