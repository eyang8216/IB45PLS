# Lesson 32: Inflation — Measurement and Causes

## What You'll Learn
- How inflation is defined and measured using CPI
- How to calculate the inflation rate from CPI data
- The two main types of inflation: demand-pull and cost-push
- The critical distinction between deflation and disinflation
- Limitations of CPI as a measure

---

## 1. Definition and the CPI

### What Is Inflation?

**Inflation** is a **sustained increase in the general price level** of goods and services in an economy over a period of time. This does NOT mean all prices rise equally — individual prices may rise or fall, but the *average level* rises.

- One-off price increases (e.g., due to a tax change) = NOT inflation
- Inflation requires a continuous, self-perpetuating rise over multiple periods

### The Consumer Price Index (CPI)

The CPI is the most common measure of inflation. It tracks the cost of a **representative basket of goods and services** purchased by a typical household.

**Construction Steps**:

1. **Select a base year** — the reference point against which all comparisons are made
2. **Define the basket** — survey households to determine what they buy and in what proportions
3. **Assign weights** — each item's weight = its share of total household expenditure (e.g., housing 30%, food 15%, transport 12%)
4. **Collect prices** monthly from retail outlets across the country
5. **Compute the index**: 

$$\text{CPI}_t = \frac{\text{Cost of basket in year }t}{\text{Cost of basket in base year}} \times 100$$

### Worked Example: CPI Calculation

**Basket (base year 2020)**:

| Item | Weight | Price 2020 | Price 2021 | Price 2022 |
|------|--------|------------|------------|------------|
| Bread | 20% | $2.00 | $2.20 | $2.42 |
| Milk | 10% | $1.50 | $1.65 | $1.73 |
| Rice | 10% | $3.00 | $3.15 | $3.30 |
| Rent | 30% | $800 | $840 | $880 |
| Transport | 30% | $200 | $210 | $218 |

**Weighted basket cost** (for simplicity, assume 1 unit each):
- 2020: (0.2×2.00)+(0.1×1.50)+(0.1×3.00)+(0.3×800)+(0.3×200) = 0.40+0.15+0.30+240+60 = **$300.85**
- 2021: (0.2×2.20)+(0.1×1.65)+(0.1×3.15)+(0.3×840)+(0.3×210) = 0.44+0.165+0.315+252+63 = **$315.92**
- 2022: (0.2×2.42)+(0.1×1.73)+(0.1×3.30)+(0.3×880)+(0.3×218) = 0.484+0.173+0.330+264+65.4 = **$330.39**

**CPI values**:
- CPI₂₀₂₀ = (300.85/300.85) × 100 = **100.00**
- CPI₂₀₂₁ = (315.92/300.85) × 100 = **105.01**
- CPI₂₀₂₂ = (330.39/300.85) × 100 = **109.82**

---

## 2. Calculating the Inflation Rate

The **inflation rate** is the **percentage change** in the CPI from one period to the next:

$$\text{Inflation Rate}_t = \frac{\text{CPI}_t - \text{CPI}_{t-1}}{\text{CPI}_{t-1}} \times 100\%$$

**Using our example**:
- Inflation 2021 = (105.01 − 100.00) / 100.00 × 100% = **5.01%**
- Inflation 2022 = (109.82 − 105.01) / 105.01 × 100% = **4.58%**

**Quick check**: CPI rising but at a decreasing rate = **disinflation** (see Section 5).

---

## 3. Limitations of the CPI

The CPI, while widely used, is **not a perfect measure**. IB students must know these limitations:

### a) Substitution Bias
- CPI uses a **fixed basket** with fixed weights
- When the price of beef rises sharply, consumers **substitute** toward chicken
- The fixed basket overstates the inflation consumers actually experience
- **Result**: CPI overstates true cost-of-living increase

### b) Quality Changes
- A smartphone today costs more than a phone in 2005, but it's vastly superior (camera, GPS, apps)
- If the CPI records only the price increase, it misses the quality improvement
- **Result**: CPI overstates inflation when quality improves; understates when quality declines ("shrinkflation")

### c) New Goods Bias
- New products (e.g., streaming services) take time to enter the basket
- These often fall rapidly in price after introduction
- **Result**: CPI misses early price declines of innovative goods

### d) Different Household Patterns
- The CPI reflects an **average** household
- Elderly, students, rural, and urban households have very different spending patterns
- A retired person spends more on healthcare; a student more on education and rent
- **Result**: CPI may not reflect any particular group's actual inflation

### e) Geographic Variation
- Prices differ across regions within a country
- National CPI averages mask regional differences

---

## 4. Demand-Pull Inflation

### Definition
**Demand-pull inflation** occurs when **aggregate demand (AD) increases** while aggregate supply cannot keep up, pulling the price level upward. The classic description: **"Too much money chasing too few goods."**

### AD/AS Diagram

- Start at long-run equilibrium: AD₀, SRAS₀, LRAS at Yf, P₀
- AD shifts RIGHT to AD₁ (due to ↑C, ↑I, ↑G, or ↑(X−M))
- New short-run equilibrium: **higher price level (P₁) AND higher real GDP (Y₁ > Yf)**

**Key characteristic**: The economy operates **beyond full employment** — firms bid up wages to attract scarce labor, passing costs to consumers.

### Causes of AD Shifts Right
| AD Component | Causes |
|---|---|
| Consumption (C) | Tax cuts, consumer confidence ↑, wealth effect from asset prices |
| Investment (I) | Interest rate cuts, business confidence ↑, technological optimism |
| Government (G) | Fiscal stimulus, infrastructure spending, defense buildup |
| Net Exports (X−M) | Depreciation of currency, foreign income growth, trade liberalization |

### Policy Response
- **Contractionary monetary policy**: Raise interest rates → C↓, I↓ → AD shifts left
- **Contractionary fiscal policy**: Cut G, raise taxes → AD shifts left
- **Supply-side policies**: Increase LRAS to accommodate higher AD without inflation

---

## 5. Cost-Push Inflation

### Definition
**Cost-push inflation** occurs when the **costs of production rise**, reducing short-run aggregate supply (SRAS shifts LEFT). Prices rise **not** because demand is strong, but because supply has been constrained.

### AD/AS Diagram

- Start at long-run equilibrium: AD₀, SRAS₀, LRAS at Yf, P₀
- SRAS shifts LEFT to SRAS₁ (due to rising input costs)
- New equilibrium: **higher price level (P₁) AND LOWER real GDP (Y₁ < Yf)**

**This combination of rising prices AND falling output is called STAGFLATION.** It's the nightmare scenario for policymakers because the two problems require opposite remedies.

### Causes of SRAS Shifts Left
| Cause | Mechanism |
|---|---|
| Rising commodity prices | Oil, food, metals price shocks (e.g., OPEC 1973, 1979) |
| Rising wages | Strong unions, minimum wage increases exceeding productivity |
| Supply chain disruptions | Natural disasters, pandemics, wars |
| Currency depreciation | Imported inputs become more expensive |
| Tax increases | VAT, corporate taxes raise firms' costs |

### Policy Dilemma
- **Contractionary policy** reduces inflation but worsens the recession (Y already < Yf)
- **Expansionary policy** boosts Y but worsens inflation
- **Preferred response**: Supply-side policies to shift SRAS back right

---

## 6. Deflation vs Disinflation — Critical Distinction

IB examiners love testing this. Get it right:

| Term | Definition | CPI Behavior |
|---|---|---|
| **Deflation** | A sustained **decrease** in the general price level | CPI falling (negative inflation rate) |
| **Disinflation** | A **decrease in the rate of inflation** — prices still rising, but more slowly | CPI rising at a decreasing rate |

### Numerical Example

| Year | CPI | Change |
|---|---|---|
| 2020 | 100.0 | — |
| 2021 | 108.0 | +8.0% (inflation) |
| 2022 | 113.4 | +5.0% (**disinflation** — inflation falling from 8% to 5%) |
| 2023 | 109.0 | −3.9% (**deflation** — prices actually falling) |

**Why deflation is dangerous**:
- Consumers delay purchases (why buy today when cheaper tomorrow?) → C↓ → AD↓ → further deflation → **deflationary spiral**
- Real debt burden rises → bankruptcies, credit crunch
- Japan's "lost decades" is the classic case study

---

## IB Exam Tip

- **Diagrams are essential**: Draw AD/AS for both demand-pull (AD right: higher P, higher Y) and cost-push (SRAS left: higher P, lower Y). Label equilibrium points, axes, and shifts clearly.
- **"Sustained increase"** — definition must include the word "sustained" or "persistent."
- **CPI calculation**: Practice the formula — you may get a table of CPI values and be asked to calculate inflation rates.
- **Distinguish deflation/disinflation**: Write both on your diagram if relevant. Deflation = CPI line slopes down; disinflation = CPI line slopes up but less steeply.

---

## Practice Problems

### Problem 1 (Easy)
The CPI in Country A was 120 in 2022 and 126 in 2023. Calculate the inflation rate for 2023. Is this inflation, deflation, or disinflation if 2022's inflation rate was 9%?

### Problem 2 (Easy)
Explain TWO limitations of the CPI as a measure of the cost of living. Use specific examples.

### Problem 3 (Medium)
Using an AD/AS diagram, explain the difference between demand-pull and cost-push inflation in terms of their effects on real GDP.

### Problem 4 (Medium)
A country's CPI values are: 2020 = 100, 2021 = 105, 2022 = 108.15, 2023 = 109.23. Calculate the inflation rate for each year and identify any periods of disinflation or deflation.

### Problem 5 (Challenging)
Country X's CPI basket is weighted as: Food 30%, Housing 35%, Transport 15%, Healthcare 10%, Entertainment 10%. In 2023, food prices rose 8%, housing rose 3%, transport fell 2%, healthcare rose 12%, and entertainment rose 1%. Calculate the overall inflation rate. If the central bank targets 2–4%, should it intervene?

### Problem 6 (IB-Style 15-mark)
"Cost-push inflation is more difficult to control than demand-pull inflation." Discuss this statement.

---

## Answers

### Answer 1
- Inflation rate = (126 − 120) / 120 × 100% = 6/120 × 100 = **5.00%**
- 2022 inflation was 9%, so inflation fell from 9% to 5%. Prices are still rising, just more slowly.
- This is **disinflation** (not deflation — CPI is not falling, only the rate of increase is falling).

### Answer 2
**1. Substitution Bias**: CPI uses a fixed basket. If beef prices surge, consumers switch to chicken. The CPI, using fixed weights, continues to assume heavy beef consumption, overstating the true cost-of-living increase.

**2. Quality Changes**: A laptop today costs $1,200 vs. $1,000 five years ago. Raw price comparison suggests 20% inflation, but today's laptop has 4× RAM, SSD, and a Retina display. The CPI may not fully adjust for quality, overstating inflation.

Other acceptable answers: new goods bias, different household patterns, geographic variation.

### Answer 3
**Demand-pull inflation**:
- AD shifts RIGHT (C↑, I↑, G↑, or X−M↑)
- **Result**: P↑ AND Y↑ (economy overheats above Yf)
- Policy: Contractionary (raise rates, cut spending) — no dilemma

**Cost-push inflation**:
- SRAS shifts LEFT (rising input costs)
- **Result**: P↑ AND Y↓ (stagflation)
- Policy dilemma: contractionary fixes inflation but worsens recession; expansionary fixes recession but worsens inflation

**Diagram**: Show AD₀-AD₁ shift for demand-pull; SRAS₀-SRAS₁ shift for cost-push. Both show higher P, but demand-pull shows higher Y while cost-push shows lower Y — this is the crucial distinction.

### Answer 4

| Year | CPI | Inflation Rate |
|------|-----|----------------|
| 2020 | 100.00 | — |
| 2021 | 105.00 | (105−100)/100 = **5.00%** |
| 2022 | 108.15 | (108.15−105)/105 = **3.00%** |
| 2023 | 109.23 | (109.23−108.15)/108.15 = **1.00%** |

- 2021→2022: Inflation fell from 5% to 3% → **disinflation**
- 2022→2023: Inflation fell from 3% to 1% → **disinflation**
- No deflation: CPI never fell below previous year

### Answer 5
Weighted inflation = Σ(weight × price change for each category):

- Food: 0.30 × 8% = 2.40%
- Housing: 0.35 × 3% = 1.05%
- Transport: 0.15 × (−2%) = −0.30%
- Healthcare: 0.10 × 12% = 1.20%
- Entertainment: 0.10 × 1% = 0.10%

**Overall inflation = 2.40 + 1.05 − 0.30 + 1.20 + 0.10 = 4.45%**

**Analysis**: 4.45% exceeds the 2–4% target band. The central bank should consider intervention, BUT:
- Food (8%) and healthcare (12%) surges may be supply shocks (cost-push), which contractionary policy would worsen
- Transport is already falling (−2%), suggesting some demand weakness
- A rate hike might target the wrong problem

**Recommendation**: Investigate whether food/healthcare are supply-side shocks before acting. If demand-pull, raise rates. If cost-push, consider supply-side measures or tolerate a temporary overshoot.

### Answer 6 (Full IB-Style Response)

**Introduction**: Cost-push inflation arises from rising production costs shifting SRAS left, while demand-pull inflation arises from excessive AD. The statement claims cost-push is harder to control — a claim rooted in the policy dilemma of stagflation.

**The Policy Dilemma for Cost-Push**:
- To reduce inflation → contractionary policy (AD left) → Y falls further below Yf
- To restore output → expansionary policy (AD right) → inflation worsens
- **No policy can simultaneously fix both problems** using demand-side tools alone
- The appropriate remedy — shifting SRAS back right — is slow, uncertain, and often outside policymakers' direct control (e.g., global oil prices)

**Why Demand-Pull Is Easier**:
- Contractionary monetary policy (raise rates) shifts AD left
- No dilemma: both P and Y return toward equilibrium in the same direction
- Central banks can act quickly and independently

**BUT — Cost-Push May Self-Correct**:
- If caused by a temporary supply shock (oil spike), SRAS shifts back as shock fades
- No policy response may be the best response

**AND — Demand-Pull Has Its Own Complexities**:
- Identifying the output gap precisely is hard; overshooting creates a recession
- Time lags: rate hikes take 6–18 months to fully affect the economy
- Political pressure to avoid rate hikes (unpopular with borrowers)

**Supply-Side Solutions for Cost-Push**:
- Investment in alternative energy reduces oil dependence
- Productivity improvements reduce unit labor costs
- Trade liberalization reduces input costs through competition
- These shift LRAS right, addressing root causes permanently

**Conclusion**: Cost-push inflation is more difficult to control **in the short run** because of the stagflation policy dilemma. However, demand-pull can also be challenging due to identification and timing issues. The ideal approach is prevention — supply-side policies that make the economy resilient to cost shocks — combined with central bank credibility that anchors inflation expectations.

---

## Evaluate

**"Cost-push inflation is more difficult to control than demand-pull inflation."**

### CLASPP Analysis (166 words)

**Conclusion**: The statement is largely valid in the short run due to the stagflation policy dilemma. Cost-push inflation presents a trade-off between price stability and output that demand-pull does not, making it genuinely harder to manage with conventional tools.

**Long-term vs Short-term**: In the short run, cost-push creates the dilemma described above. In the long run, however, supply shocks often reverse naturally (oil prices fall), and supply-side policies can shift SRAS/LRAS right, resolving cost-push permanently. Demand-pull may be harder to control in the long run if driven by structural excess demand.

**Assumptions**: The statement assumes cost-push is a domestic problem controllable by domestic policy. In reality, cost-push often originates from global commodity prices outside domestic control. It also assumes policymakers value both price stability and output equally.

**Stakeholders**: Workers suffer most from cost-push (rising prices, potential layoffs). Central banks face credibility crises if they cannot control inflation. Governments lose popularity.

**Priorities**: If inflation expectations become unanchored (wage-price spiral), controlling inflation must be the priority regardless of output costs. If the shock is clearly temporary, preserving output takes priority.

**Pros/Cons of the statement**: Pro — accurately identifies the unique policy dilemma. Con — oversimplifies; demand-pull control has timing/identification challenges, and cost-push solutions exist albeit slower.

**Overall**: Cost-push is harder **short-run**, but both require thoughtful policy mixes.
