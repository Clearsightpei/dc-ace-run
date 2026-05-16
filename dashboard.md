# DC-ACE Dashboard — last update: 2026-05-16

- **Cycle**: 3
- **Phase**: 1 (atomic strokes)
- **This cycle**: **2/3 pass** by visual ≥ 0.7 threshold (pie 1.00, ti 0.95, na 0.22); avg visual **0.72**
- **Last batch**: [pie, na, ti] (pie carry-over; na, ti new)
- **Trend**:
  - c1 → 0/3 (avg 0.25) — cold start, no memory
  - c2 → 2/3 (avg 0.71) — same batch, seeded memory
  - c3 → 2/3 (avg 0.72) — pie solved via memory fix; 2 new strokes introduced, 1 passed first try
- **Memory size**: ~155 lines / ~6 KB
- **Curator note**: pie 0.40→1.00 from the exact memory fix — strongest single-entry transfer signal. ti generalized first try from text. na failed by wrongly reusing pie's curvature; memory now separates "deep curve" (pie) from "shallow bow" (na).
- **Loop status**: running (delete dc_ace_run/.stop to allow cycles; create it to pause)

## The memory-transfer evidence (now two clean data points)

1. **Cycle 1→2**: identical task brief, only memory changed → avg 0.25→0.71.
2. **Cycle 2→3, pie**: pie carried over with a *specific* rotation
   fix written to memory (50°→60°). The fresh c3 Drawer applied it
   and scored **1.00** (was 0.40). Targeted memory edits land
   precisely, not just vaguely.

New observation: a *new* stroke (ti) passed 0.95 on first attempt
from text + canvas conventions alone — the Drawer's prior knowledge
plus generic memory generalizes. But na shows the failure mode:
over-generalizing one stroke's parameters (pie's 60°) onto another.

## Per-stroke status

| key  | char | best score | status                          |
|------|------|------------|---------------------------------|
| heng | 横   | 0.74       | passed (retired)                |
| shu  | 竖   | 1.00       | passed, perfect (retired)       |
| pie  | 撇   | 1.00       | **solved** (retired)            |
| ti   | 提   | 0.95       | passed first try (retire)       |
| na   | 捺   | 0.22       | carry over — shallow-bow fix in memory |

## OCR observations

- ti → '一' @ 0.41 (low — short diagonal flick, weak signal; expected)
- pie, na → no OCR signal (lone curved strokes)
- (prior) heng → '一' @ 0.75; shu → '一' @ 0.33
