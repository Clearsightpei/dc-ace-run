<!--
Append-only history. Teacher adds one block per cycle. Do not edit
prior entries.
-->

## Cycle 1 — 2026-05-15

- **Phase:** 1
- **Batch:** [heng, shu, pie]
- **Why this batch:** Cold start. The Drawer is a fresh subagent that
  cannot see the GTs and has no memory file content. Picked the three
  most foundational atomic strokes — every Chinese character uses
  these. If the Drawer's general knowledge can produce even rough
  versions, the experiment has signal to work with. If it fails
  entirely, Curator's notes seed cycle 2.
- **Cycle summary from last cycle:** (none; this is the first cycle of
  a fresh run after the pilot's reset)

## Cycle 2 — 2026-05-15

- **Phase:** 1
- **Batch:** [heng, shu, pie]  ← same as cycle 1, deliberately
- **Why this batch:** All three carry over (every cycle-1 visual_score
  was < 0.7). The Curator wrote explicit diagnostic notes in
  drawer_memory.md (scale guidance: ~70 pixels; pie direction
  correction: sweep DOWN-LEFT not UP-RIGHT). Repeating the exact same
  batch is the cleanest experiment: did memory transfer? If scores
  jump significantly, the Curator's memory contribution is the cause.
  If they don't, the memory format isn't working.
- **Cycle summary from last cycle:** "0/3 passed visual (avg 0.25).
  Scale 4× too large; pie reversed. Memory now has scale guidance
  and direction correction. Recommend repeat batch as memory-transfer
  test."
  → Following the recommendation verbatim.

## Cycle 3 — 2026-05-16

- **Phase:** 1
- **Batch:** [pie, na, ti]
- **Why this batch:** heng (0.74) and shu (1.00) passed in cycle 2
  and leave the rotation per the carry-over rule. pie carries over
  (0.40 < 0.7) and the Curator codified a specific fix (more total
  rotation ~60°, ~60 steps). Introducing na and ti — the two
  remaining foundational single-direction strokes — tests whether
  the Drawer's general knowledge + canvas conventions in memory
  generalize to *new* strokes it has never attempted, while pie
  tests whether a targeted memory fix lands.
- **Cycle summary from last cycle:** "2/3 pass; avg visual 0.25→0.71
  from memory alone. heng/shu solved. pie curve too shallow; memory
  now specifies ~60° rotation. Recommend carry pie + add na, ti."
  → Followed verbatim.

## Cycle 4 — 2026-05-16

- **Phase:** 1
- **Batch:** [na, dian, heng_zhe]
- **Why this batch:** pie (1.00) and ti (0.95) passed cycle 3 and
  retire per the carry-over rule. na carries over (0.22 < 0.7) with
  a specific Curator fix (shallow ~20° bow, flattening tail — do NOT
  reuse pie's 60°). Introducing dian (the smallest atomic stroke, a
  scale-extreme test) and heng_zhe (the first *compound* stroke — a
  horizontal then a folded vertical), which probes whether the
  Drawer can compose two known primitives (heng + shu, both solved)
  into one connected stroke.
- **Cycle summary from last cycle:** "2/3 pass; pie solved 0.40→1.00
  via exact memory fix; ti passed first try; na failed by reusing
  pie's curvature. Recommend carry na, retire pie/ti, add dian +
  heng_zhe." → Followed verbatim.

## Cycle 5 — 2026-05-16

- **Phase:** 1
- **Batch:** [na, dian, heng_zhe]  ← full carry-over of cycle 4
- **Why this batch:** All three failed cycle 4 (<0.7). The Curator
  identified that each failure was a *specific number/method* error,
  not a conceptual one, and corrected memory: na heading 285°→325°,
  dian should use t.dot() not a line, heng_zhe segments shortened &
  recentered. Repeating the exact batch is the cleanest test of
  whether corrected numeric memory now lands (mirrors the c2 and c3
  memory-transfer tests). No new strokes — isolate the variable.
- **Cycle summary from last cycle:** "0/3; a wrong number in memory
  transfers as faithfully as a right one. Corrected na heading, dian
  method, heng_zhe scale. Carry all three." → Followed verbatim.
