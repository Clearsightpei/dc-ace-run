# DC-ACE Dashboard — last update: 2026-05-16

- **Cycle**: 6
- **Phase**: 2 (simple characters) — entered this cycle
- **This cycle**: **2/3 correct** (十 ✓ 0.78, 人 ✓ 0.95, 一 ✗); avg visual 0.19 (ignore — wrong metric for Phase 2)
- **Last batch**: [一, 十, 人] — first Phase-2 batch, pure compositions of solved strokes
- **Trend (pass count)**:
  - c1 0/3 · c2 2/3 · c3 2/3 · c4 0/3 · c5 0/3 · c6 **2/3**
  - c1–c5 = Phase-1 visual≥0.7; c6 = Phase-2 OCR is_correct
- **Memory size**: ~235 lines / ~9 KB
- **Curator note**: Phase-2 composition works first-try — 十/人 recognized 0.78/0.95 from scaled stroke recipes, no char-specific memory. 一 is an OCR blind spot (featureless lone line). OCR is_correct is the Phase-2 signal; phase-correlation is now irrelevant.
- **Loop status**: running (delete dc_ace_run/.stop to allow cycles; create it to pause)

## Headline finding (cycle 6)

**The emergent stroke memory composes.** A fresh Drawer subagent
with no character-specific memory built recognizable 十 and 人 on
the first attempt purely by scaling and combining the heng/shu/pie/
na recipes the Curator had accumulated over cycles 1–5. This is the
payoff of the whole experiment: atomic memory generalizes upward to
unseen compositions. The single failure (一) is the featureless-
image edge case showing up on the OCR axis instead of the phase-
correlation axis.

## Per-task status (Phase 2)

| char | pinyin | OCR (conf)  | is_correct |
|------|--------|-------------|------------|
| 一   | yi     | (none)      | ✗ — featureless, OCR blind spot |
| 十   | shi    | 十 (0.78)   | ✓ |
| 人   | ren    | 人 (0.95)   | ✓ |

## Recommendation to Teacher

Continue Phase 2 with more multi-stroke simple characters. Either
drop 一, or retry it once with a bold near-flat pen to test the
"thicker pen aids OCR" hypothesis. Good candidates: 二/三 (probe the
1-stroke hypothesis), 大/木/口 (new compositions of solved strokes).
