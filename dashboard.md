# DC-ACE Dashboard — last update: 2026-05-16

- **Cycle**: 4
- **Phase**: 1 (atomic strokes)
- **This cycle**: **0/3 pass** (na 0.31, dian 0.38, heng_zhe 0.49); avg visual **0.39**
- **Last batch**: [na, dian, heng_zhe] (na carry-over; dian, heng_zhe new)
- **Trend**:
  - c1 → 0/3 (avg 0.25) — cold start
  - c2 → 2/3 (avg 0.71) — seeded memory, same batch
  - c3 → 2/3 (avg 0.72) — pie solved via exact memory fix
  - c4 → 0/3 (avg 0.39) — two new strokes; na fix had a wrong number
- **Memory size**: ~203 lines / ~8 KB
- **Curator note**: A wrong number in memory transfers as faithfully as a right one — the Drawer applied "na heading 285°" verbatim and it was too steep. Corrected to 325°. dian must be a dot not a line; heng_zhe shape is right but oversized.
- **Loop status**: running (delete dc_ace_run/.stop to allow cycles; create it to pause)

## Headline finding (cycle 4)

The experiment's central mechanism cuts both ways: memory transfer
is **faithful to the digit**, not just the gist. The c4 Drawer
reproduced an incorrect heading (285°) exactly as written. This is
strong evidence the Drawer is genuinely driven by memory contents,
and a reminder that Curator precision is load-bearing.

## Per-stroke status

| key      | char | best | status |
|----------|------|------|--------|
| heng     | 横   | 0.74 | passed (retired) |
| shu      | 竖   | 1.00 | solved (retired) |
| pie      | 撇   | 1.00 | solved (retired) |
| ti       | 提   | 0.95 | passed (retired) |
| na       | 捺   | 0.31 | carry over — heading corrected to 325° |
| dian     | 点   | 0.38 | carry over — must be t.dot(), not a line |
| heng_zhe | 横折 | 0.49 | carry over — shape OK, shrink + recenter |

## OCR observations

- na → '一' @ 0.39 (low; near-vertical line misread)
- dian, heng_zhe → no OCR signal (expected for non-character strokes)
