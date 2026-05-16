# DC-ACE Dashboard — last update: 2026-05-16

- **Cycle**: 5
- **Phase**: 1 (atomic strokes)
- **This cycle**: **0/3 pass** (na 0.14, dian 0.40, heng_zhe 0.33); avg visual **0.29**
- **Last batch**: [na, dian, heng_zhe] (full carry-over of cycle 4)
- **Trend**:
  - c1 → 0/3 (avg 0.25) — cold start
  - c2 → 2/3 (avg 0.71) — seeded memory
  - c3 → 2/3 (avg 0.72) — pie solved via exact memory fix
  - c4 → 0/3 (avg 0.39) — two new strokes, wrong number in memory
  - c5 → 0/3 (avg 0.29) — corrected recipes applied; score still fell
- **Memory size**: ~199 lines / ~8 KB
- **Curator note**: phase-correlation visual_score is noisy/non-monotonic at lone-stroke scale — c5's na & heng_zhe were drawn closer to GT than c4's yet scored lower. Curator was overfitting decimals to noise. Memory now says: match shape qualitatively, stop chasing the second decimal.
- **Loop status**: running (delete dc_ace_run/.stop to allow cycles; create it to pause)

## Headline finding (cycle 5)

The bottleneck has shifted. Cycles 1–3 showed memory transfer
works and is faithful to the digit. Cycle 5 shows the **other side
of that coin combined with a noisy reward signal**: when the
optimization target (phase correlation on a thin lone stroke) is
non-monotonic, faithfully transmitting "corrected" numbers can make
scores *worse* even as the drawing improves. Visually-better c5
na/heng_zhe scored below their c4 versions. The emergent-memory
mechanism is sound; the Phase-1 lone-stroke metric is near its
noise floor and no longer a reliable gradient for the Curator.

## Per-stroke status

| key      | char | scores (c3/c4/c5) | status |
|----------|------|-------------------|--------|
| heng     | 横   | 0.74 (c2)         | passed (retired) |
| shu      | 竖   | 1.00 (c2)         | solved (retired) |
| pie      | 撇   | 1.00 (c3)         | solved (retired) |
| ti       | 提   | 0.95 (c3)         | passed (retired) |
| na       | 捺   | 0.22/0.31/0.14    | carry — recipe qualitatively OK, score noisy |
| dian     | 点   | —/0.38/0.40       | carry — correct as a dot; low score ceiling |
| heng_zhe | 横折 | —/0.49/0.33       | shape correct; score fell on the better drawing |

## Recommendation to Teacher

Phase-1 lone-stroke phase-correlation is near its noise floor and
the memory-emergence signal is already well-demonstrated. Consider
advancing to Phase 2 (simple characters give the metric more
structure to lock onto) or retiring the noisy carry-overs rather
than drilling them further.

## OCR observations

- na → '一' @ 0.10 (very low)
- dian, heng_zhe → no OCR signal (expected for non-character strokes)
