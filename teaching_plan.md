# Teaching plan

## Current phase

**Phase 1 — atomic strokes.** The Drawer is a fresh subagent that has
never seen this codebase. It has no memory. We are starting from
zero, by design.

## Pacing principle (provisional)

- **3 tasks per cycle**, always (subject to revision based on what
  emerges).
- Cycle 1: introduce the three most foundational atomic strokes —
  横, 竖, 撇. These are present in nearly every Chinese character.
  If the Drawer can produce *recognizable* versions of these from
  textual description alone, the experiment has a viable starting
  point.
- After cycle 1, decisions about pacing depend on what the Curator
  observes.

## Carry-over rule (Phase 1)

- A stroke whose `visual_score < 0.7` carries over to next cycle.
  (Threshold loose at first because the Drawer is blind to the GT.)
- If a stroke passes once, it leaves the rotation.

## How I will use Curator feedback

`cycle_summary.md` is the primary input. The Curator tells me what
*kind* of mistake the Drawer made; my job is to design next cycle's
batch to either drill that mistake or introduce something new.

## Open questions

- How much does the Drawer's "general knowledge of Chinese strokes"
  carry it through cycle 1 without memory? That's the first
  observable.
- Is the visual_score threshold sane in the GT-blind regime? It may
  need to be lower than the previous run's 0.9.
