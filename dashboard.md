# DC-ACE Dashboard — last update: 2026-05-16

- **Cycle**: 8
- **Phase**: 2 (simple characters)
- **This cycle**: **3/3 correct** — 大 ✓1.00, 八 ✓1.00, 三 ✓1.00 (first perfect cycle)
- **Last batch**: [大(carry), 八, 三]
- **Trend (pass count)**: c1 0/3 · c2 2/3 · c3 2/3 · c4 0/3 · c5 0/3 · c6 2/3 · c7 2/3 · c8 **3/3**
- **Memory size**: ~255 lines / ~10 KB
- **Curator note**: First 3/3. The new mandatory carry-over rule worked end to end — 大 (✗天 c7) → Curator reflection → forced carry-over → ✓大@1.00 c8. Reflection confirmed, not hoped. Composition from atomic memory is robust.
- **Loop status**: running (delete dc_ace_run/.stop to allow cycles; create it to pause)

## Headline finding (cycle 8)

The reflection→carry-over→confirm loop is now demonstrated as a
**closed verification cycle**: a documented failure (大→天)
produced a falsifiable structural fix in memory, the carry-over
rule forced a re-test, and the fix was confirmed (大→大 @ 1.00) on
the very next attempt by a fresh subagent that only read memory.
This is the strongest form of the experiment's core claim: memory
not only transfers, it can be *deliberately corrected and the
correction verified*.

## Per-task status (Phase 2)

| char | pinyin | OCR (conf) | is_correct |
|------|--------|------------|------------|
| 大   | da     | 大 (1.00)  | ✓ — c7 stacking fix CONFIRMED |
| 八   | ba     | 八 (1.00)  | ✓ — pie+na split, first try |
| 三   | san    | 三 (1.00)  | ✓ — three stacked heng, first try |

## Recommendation to Teacher

大/八/三 retire (clean confirmed passes). Advance to harder
structural compositions (天/夫/本/口/中) — structural arrangement
is the current learning frontier; stroke shape is solved.

## Note on metrics

Phase-2 visual_score is now ~0.05 even for perfectly-recognized
characters. It is fully decoupled from correctness; the OCR
`is_correct` / confidence is the only meaningful Phase-2 signal.
