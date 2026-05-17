# DC-ACE Dashboard — last update: 2026-05-16

- **Cycle**: 10
- **Phase**: 2 (simple characters)
- **This cycle**: **2/3 correct** — 中 ✓1.00, 日 ✓0.99, 天 ✗→元 0.80
- **Last batch**: [天(carry), 中, 日]
- **Trend (pass count)**: c4 0/3 · c5 0/3 · c6 2/3 · c7 2/3 · c8 3/3 · c9 2/3 · c10 **2/3**
- **Memory size**: ~280 lines / ~12 KB
- **Curator note**: c9 reflection for 天 was applied faithfully yet 天 still →元 (0.80). The reflection itself was wrong: 天 = short heng + 大 (piercing), not 二+人. Corrected in memory; 天 carries again to c11. 中/日 (box reuse) ✓ first try.
- **Loop status**: running (delete dc_ace_run/.stop to allow cycles; create it to pause)

## Headline finding (cycle 10)

**A reflection can be faithfully applied and still be wrong** — and
the mandatory carry-over rule is precisely what exposes that. c10's
天 implemented the c9 fix correctly (verified in the generated
code: pie+na share an apex, no crossing) yet the outcome failed
identically (→元, higher confidence). A "successful application,
failed outcome" is a clean falsification signal: it isolates the
*theory* as the error, not the execution. The corrected theory
(天 = short heng + the confirmed 大, with pie/na piercing the bar)
is now in memory and itself becomes a c11 carry-over test. This is
the experiment's error-correction loop operating at full strength.

## Per-task status (Phase 2)

| char | pinyin | OCR (conf) | is_correct |
|------|--------|------------|------------|
| 天   | tian   | 元 (0.80)  | ✗ — c9 theory falsified; corrected, carries to c11 |
| 中   | zhong  | 中 (1.00)  | ✓ — box + vertical, first try |
| 日   | ri     | 日 (0.99)  | ✓ — box + middle bar, first try |

## Recommendation to Teacher

Mandatory carry-over: 天 → c11 with the corrected "short heng + 大
(piercing)" structure. 中/日 retire. Keep reusing confirmed
primitives (口/大/木/人) in new compositions; the productive
frontier remains structural assembly.
