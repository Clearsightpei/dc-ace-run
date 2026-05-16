# DC-ACE Dashboard — last update: 2026-05-15

- **Cycle**: 1 (fresh run after pilot reset)
- **Phase**: 1 (atomic strokes)
- **This cycle**: **0/3** visual ≥ 0.5 (avg visual 0.25, avg final 0.13)
- **Last batch**: [heng, shu, pie]
- **Trend (last 5 cycles)**: c1 → 0/3 (0.25 avg). First cycle of fresh run.
- **Memory size**: ~75 lines / ~3 KB (Curator-seeded for first time)
- **Curator note**: Cold-start failure as designed. Drawer subagent had no prior context — heng/shu were qualitatively correct but ~4× too large; pie's direction was reversed. Memory now contains scale guidance + pie direction correction.
- **Loop status**: running (delete `dc_ace_run/.stop` to allow cycles; create it to pause)

## What this run is testing

A redesigned harness where the **Drawer is a fresh subagent** each
cycle (no conversation-context leakage), and `make_char_gt.py`'s
y-flip bug from the pilot has been fixed. Cycle 1 is the cold-start
baseline; cycle 2 will be the first real test of whether memory
transfers across subagent instances.

## Pilot vs current run

- **Pilot** (cycles 1–5, deleted): Drawer was the same Claude session
  as Teacher/Curator → parameters leaked through conversation context
  → cycle 1 produced near-canonical attempts (visual 1.0000).
- **This run** (cycle 1): Drawer is a fresh subagent → no leakage →
  cold-start visual 0.25. **The big drop from 1.0 to 0.25 is the
  measure of how much was being leaked.**

## Phase-1 metric notes

- Trust `visual_score`; `is_correct` is False by phase-construction
  (lone strokes aren't recognizable characters).
- Caveat: low-confidence OCR hits *do* happen — cycle 1's pie got
  OCR='一' @ 0.13 (similarity signal). The Drawer's gentle arc
  looked more horizontal than a real pie.
