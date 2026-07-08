# IB Physics HL — Data Booklet Cross-Check

**Official booklet:** Physics Data Booklet, First Assessment 2016 (17 pages)
**My reference:** `lessons/data_booklet.md` (built for 2025 syllabus themes)

---

## Summary

| Aspect | Official (2016) | My Reference | Verdict |
|--------|-----------------|--------------|---------|
| Structure | Old topics 1–12 + Options | New themes A–E | ✅ Correct for 2025 |
| Fundamental constants | 17 constants | All 17 | ✅ Match |
| Equations coverage | All core + AHL + Options | All core + HL (mapped to themes) | ✅ Match |
| Values | g = 9.81 | g = 10 (per textbook) | ⚠️ Both valid |
| Missing items | — | See below | 🔴 7 items to add |

---

## Items Missing from My Reference (Now Added)

### 1. Metric (SI) Multipliers
Was missing entirely. Now added as Section 10.

### 2. Unit Conversions
Missing: radian definition, K ↔ °C, light year, parsec, AU, kWh. Now in Section 10.

### 3. Uncertainty Propagation Rules
I had percentage uncertainty but not the 3 specific IB formulas:
- $y = a \pm b \Rightarrow \Delta y = \Delta a + \Delta b$
- $y = \frac{ab}{c} \Rightarrow \frac{\Delta y}{y} = \frac{\Delta a}{a} + \frac{\Delta b}{b} + \frac{\Delta c}{c}$
- $y = a^n \Rightarrow \frac{\Delta y}{y} = |n|\frac{\Delta a}{a}$

Now added to Section 1.

### 4. $I = nAvq$
Drift velocity relation — missing. Now in circuits section.

### 5. Intensity Relations
$I \propto A^2$ and $I \propto x^{-2}$ — missing. Now in waves section.

### 6. Wind Power
$P = \frac{1}{2}\rho Av^3$ — missing. Now in energy section.

### 7. Capacitors in Series/Parallel
$C_{\text{parallel}} = C_1 + C_2 + \dots$ and $\frac{1}{C_{\text{series}}} = \frac{1}{C_1} + \frac{1}{C_2} + \dots$ — missing. Now in circuits section.

---

## 2016 vs. 2025 Syllabus Differences

| 2016 Booklet Has | 2025 Status |
|------------------|-------------|
| Option A: Relativity | Now in Theme A.5 (core HL) |
| Option B: Rigid bodies, Thermo, Fluids | Rigid bodies → A.4, Thermo → B.4, Fluids removed |
| Option C: Imaging | Still an Option |
| Option D: Astrophysics | Still an Option |
| Separate Doppler for moving source/observer | Combined formula in 2025 |
| Sub-topic numbering (1.1, 2.3, etc.) | Theme+chapter (A.1, B.3, etc.) |

My reference correctly uses the 2025 structure.

---

## What the 2016 PDF Has That I Can't Replicate

- **Electrical circuit symbols** (page 7): The official booklet has a diagram of ~15 circuit symbols. My reference lists them in text. The PDF diagram is cleaner — keep the official PDF open for this page.

---

## Verdict

**My reference is accurate and complete for the 2025 syllabus.** The 7 missing items above have been added to the updated `data_booklet.md` and `data_booklet.html`. Use the official 2016 PDF for the circuit symbols diagram (page 7), and use my reference for everything else — it's organized to match your textbook's theme structure.

---

## Updated Files

- `lessons/data_booklet.md` — regenerated with all missing items
- `lessons/data_booklet.html` — regenerated with MathJax
