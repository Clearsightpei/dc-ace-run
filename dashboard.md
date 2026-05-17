# DC-ACE Dashboard — last update: 2026-05-16

- **Cycle**: 9
- **Phase**: 2 (simple characters)
- **This cycle**: **2/3 correct** — 本 ✓0.97, 口 ✓0.94, 天 ✗→元 0.61
- **Last batch**: [天, 本, 口]
- **Trend (pass count)**: c1 0/3 · c2 2/3 · c3 2/3 · c4 0/3 · c5 0/3 · c6 2/3 · c7 2/3 · c8 3/3 · c9 **2/3**
- **Memory size**: ~265 lines / ~11 KB
- **Curator note**: 口 (new enclosure structure) recognized first try @0.94 — composition generalizes beyond lines/splays to boxes. 天→元: bottom pie+na crossed (乂/儿) instead of sharing an apex like 人. Reflection written; 天 carries to c10 to verify.
- **Loop status**: running (delete dc_ace_run/.stop to allow cycles; create it to pause)

## Headline finding (cycle 9)

Composition generalizes to a structurally new primitive (the
enclosed box 口) on the first attempt — the emergent memory is not
just a lookup of seen characters but a reusable stroke-composition
capability. The failure mode has descended another level: from
stroke shape (c1–5) → stroke stacking order (c7 大) → **how
sub-components join** (c9 天: pie+na must share an apex, not cross).
Each level's fix has so far been confirmable via the carry-over
rule.

## Per-task status (Phase 2)

| char | pinyin | OCR (conf) | is_correct |
|------|--------|------------|------------|
| 天   | tian   | 元 (0.61)  | ✗ — pie+na crossed (→儿); carries to c10 |
| 本   | ben    | 本 (0.97)  | ✓ — 木 + bottom heng, first try |
| 口   | kou    | 口 (0.94)  | ✓ — NEW enclosure structure, first try |

## Recommendation to Teacher

Mandatory carry-over: 天 → cycle 10 (verify the "人 bottom shares
an apex, never crosses" reflection). 本/口 retire. Add two new
characters that reuse the box (口) primitive now that it works —
e.g. 中 (口 + vertical), 日 (口 + middle bar), 田 (口 + cross).
