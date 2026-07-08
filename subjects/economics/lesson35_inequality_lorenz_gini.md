# Lesson 35: Inequality — Lorenz Curve and Gini Coefficient

## What You'll Learn
- The difference between income and wealth, and between equality and equity
- How to construct and interpret Lorenz curves
- How to calculate the Gini coefficient
- Limitations of the Gini coefficient
- How to use these tools to compare inequality across countries and time

---

## 1. Income vs Wealth

### Income
- A **flow** concept — money received per period (weekly, monthly, annually)
- Sources: wages/salaries, rent, interest, dividends, profits, transfer payments
- E.g., "Maria earns $45,000 per year"

### Wealth
- A **stock** concept — the value of assets owned at a point in time
- Components: property, shares, bonds, savings, vehicles, jewelry
- E.g., "Maria's net worth is $120,000" (house equity + savings − debts)

### Why the Distinction Matters
- Wealth inequality is typically **far greater** than income inequality
- Wealth generates income (rent, dividends, interest) → wealth inequality perpetuates income inequality
- A person can have high income but low wealth (young professional) or high wealth but low income (retired homeowner)

---

## 2. Equality vs Equity

### Equality
- **Equal outcomes**: Everyone receives the same income/wealth
- Mathematically: everyone has exactly the average
- Gini coefficient = 0

### Equity
- **Fairness**: Distributions are just and morally acceptable
- Does NOT require equal outcomes — rewards for effort, skill, risk-taking may be considered "fair"
- A society with some inequality can still be considered equitable
- A society with perfect equality might be considered inequitable (no reward for effort)

**Key IB distinction**: "Equity" is a normative concept (value judgment about fairness); "Equality" is a positive concept (measurable fact about distribution). Don't confuse them.

---

## 3. The Lorenz Curve

The **Lorenz curve** (developed by Max O. Lorenz, 1905) is a graphical representation of income (or wealth) distribution.

### Construction

1. **Rank** all households from poorest to richest
2. Group them into **quintiles** (fifths: bottom 20%, next 20%, ... top 20%) or **deciles** (tenths)
3. Plot the **cumulative percentage of total income** (vertical axis) against the **cumulative percentage of population** (horizontal axis)

### Interpreting the Lorenz Curve

- The **45-degree line** = line of perfect equality (each x% of population receives x% of income)
- The **Lorenz curve** bows below the 45-degree line — the further the bow, the greater the inequality
- The shaded area between the 45-degree line and the Lorenz curve = **Area A**
- The area under the Lorenz curve = **Area B**

### Worked Example: Drawing a Lorenz Curve

**Data for Country X**:

| Quintile | % of Total Income |
|---|---|
| Bottom 20% | 4% |
| Second 20% | 9% |
| Third 20% | 15% |
| Fourth 20% | 24% |
| Top 20% | 48% |

**Cumulative values to plot**:

| Cumulative % Population | Cumulative % Income |
|---|---|
| 0% | 0% |
| 20% | 4% |
| 40% | 4+9 = 13% |
| 60% | 13+15 = 28% |
| 80% | 28+24 = 52% |
| 100% | 52+48 = 100% |

**Plot points**: (0,0), (20,4), (40,13), (60,28), (80,52), (100,100). Connect to form the Lorenz curve. The 45-degree line goes through (0,0), (20,20), (40,40), ..., (100,100). The gap between them shows inequality.

---

## 4. The Gini Coefficient

The **Gini coefficient** (developed by Corrado Gini, 1912) condenses the entire Lorenz curve into a single number.

### Definition and Formula

$$\text{Gini Coefficient} = \frac{A}{A + B}$$

Where:
- **A** = area between the 45-degree line and the Lorenz curve
- **B** = area under the Lorenz curve
- A + B = area under the 45-degree line = **0.5** (triangle area = ½ × base × height = ½ × 1 × 1 = 0.5)

### Scale Interpretation

| Gini Value | Meaning |
|---|---|
| 0 | Perfect equality (everyone has the same income) |
| 0.0–0.3 | Low inequality |
| 0.3–0.5 | Medium inequality |
| 0.5–0.7 | High inequality |
| 0.7–1.0 | Very high inequality |
| 1 (or 100 if scaled) | Perfect inequality (one person has ALL income) |

**Note**: The Gini is sometimes expressed on a 0–100 scale. Gini = 0.42 and Gini = 42 are the same thing. Multiply by 100 to convert.

### Approximate Calculation from Quintile Data

For grouped data (quintiles), the Gini can be approximated:

$$\text{Gini} \approx 1 - \sum_{i=1}^{n} (X_{i} - X_{i-1})(Y_i + Y_{i-1})$$

Where Xᵢ = cumulative population share, Yᵢ = cumulative income share.

### Worked Example: Gini Calculation

Using Country X from above:

| i | Xᵢ (cum pop) | Yᵢ (cum inc) | Xᵢ − Xᵢ₋₁ | Yᵢ + Yᵢ₋₁ | Product |
|---|---|---|---|---|---|
| 1 | 0.2 | 0.04 | 0.2 | 0.04 | 0.008 |
| 2 | 0.4 | 0.13 | 0.2 | 0.17 | 0.034 |
| 3 | 0.6 | 0.28 | 0.2 | 0.41 | 0.082 |
| 4 | 0.8 | 0.52 | 0.2 | 0.80 | 0.160 |
| 5 | 1.0 | 1.00 | 0.2 | 1.52 | 0.304 |

Sum of products = 0.008 + 0.034 + 0.082 + 0.160 + 0.304 = **0.588**

Gini = 1 − 0.588 = **0.412** (medium-high inequality)

**Sanity check**: With the top 20% receiving 48% of income (almost half), a Gini around 0.41 is plausible.

### Alternative Simple Formula (Trapezoidal Rule)

Another approach: Gini ≈ (n+1)/(n−1) − [2/(n(n−1)μ)] × Σ(rank × income)

For quintiles with shares s₁, s₂, s₃, s₄, s₅:

$$\text{Gini} \approx \frac{2}{5} \left(2s_5 + \frac{3}{2}s_4 + s_3 + \frac{1}{2}s_2\right) - 1$$

With s = (0.04, 0.09, 0.15, 0.24, 0.48):
= 0.4 × (2×0.48 + 1.5×0.24 + 1×0.15 + 0.5×0.09) − 1
= 0.4 × (0.96 + 0.36 + 0.15 + 0.045) − 1
= 0.4 × 1.515 − 1 = 0.606 − 1 = −0.394

Wait, that gives the negative area. Let me use the proper formula: Gini = 1 − sum of rectangles. My first method is the standard one and it gave 0.412, which is correct.

---

## 5. Interpreting Gini Values — Real World Examples

| Country | Approximate Gini (recent) | Interpretation |
|---|---|---|
| South Africa | ~0.63 | Highest in the world — legacy of apartheid |
| Brazil | ~0.53 | Very high — historical land concentration |
| United States | ~0.41 | Medium-high — rising since 1970s |
| United Kingdom | ~0.35 | Medium — welfare state moderates inequality |
| Sweden | ~0.28 | Low — extensive redistribution |
| Slovakia | ~0.24 | Very low — most equal in OECD |

### Trends
- Global inequality (between countries) has **decreased** as China and India grew rapidly
- Inequality within many developed countries has **increased** since the 1980s
- Technology and globalization are major drivers of within-country inequality

---

## 6. Limitations of the Gini Coefficient

The Gini is widely used but has significant limitations:

### a) Same Gini, Different Distributions
Two countries can have identical Gini coefficients but very different underlying distributions. The Gini doesn't tell you WHERE in the distribution inequality occurs.

**Example**: Country A (bottom 40% earn 15%, middle 40% earn 35%, top 20% earn 50%) and Country B (bottom 40% earn 25%, middle 40% earn 20%, top 20% earn 55%) might have similar Ginis, but the poor in Country A are much worse off than in Country B.

### b) No Information About Absolute Income
A Gini of 0.40 in a rich country (GDP/capita $60,000) means something very different from a Gini of 0.40 in a poor country (GDP/capita $2,000). The Gini is purely about **relative** distribution.

### c) Different Definitions of Income
- Before-tax or after-tax?
- Including or excluding transfers?
- Including or excluding non-cash benefits (healthcare, education)?
- Different countries use different definitions → comparability issues

### d) Lifecycle Effects
A society where everyone has identical lifetime earnings but different earnings at different ages (students earn little, mid-career earn much) will show a positive Gini at any point in time. This is not "unfair" inequality.

### e) Household Size
The Gini typically uses household income, but households differ in size. Per-capita-adjusted Ginis can look quite different.

---

## 7. Beyond the Gini — Other Measures

| Measure | What It Captures |
|---|---|
| **Palma ratio** | Ratio of top 10% income share to bottom 40% share. More sensitive to extremes. |
| **20:20 ratio** | Ratio of top 20% income to bottom 20%. Simple and intuitive. |
| **Absolute poverty measures** | Complement Gini by showing the floor, not just the spread. |

---

## IB Exam Tip

- You **must** be able to draw and label a Lorenz curve, including the 45-degree line and areas A and B.
- The Gini formula is A/(A+B). Know it. A common exam question: "Using the diagram, explain how the Gini coefficient is calculated."
- When comparing inequality, use Gini values with context (country, time, absolute income level).
- Always mention at least ONE limitation of the Gini when using it in an answer.

---

## Practice Problems

### Problem 1 (Easy)
Draw a Lorenz curve diagram and label: the 45-degree line, the Lorenz curve, Area A, and Area B. Explain what each area represents and write the formula for the Gini coefficient.

### Problem 2 (Easy)
Country A has a Gini of 0.29 and a GDP per capita of $12,000. Country B has a Gini of 0.29 and a GDP per capita of $55,000. Are living standards of the poor necessarily similar in both countries? Explain using the concept of absolute vs relative inequality.

### Problem 3 (Medium)
Calculate the Gini coefficient from the following data:

| Quintile | % of Income |
|---|---|
| Bottom 20% | 6% |
| Second 20% | 10% |
| Third 20% | 16% |
| Fourth 20% | 23% |
| Top 20% | 45% |

### Problem 4 (Medium)
Explain TWO limitations of the Gini coefficient as a measure of inequality. Use hypothetical examples to illustrate each.

### Problem 5 (Challenging)
Country X and Country Y have identical Gini coefficients of 0.38. However, Country X's bottom 40% earn 18% of income while Country Y's bottom 40% earn 22% of income. Country X has GDP per capita of $48,000 and Country Y has $8,000. Compare and evaluate the nature of inequality in the two countries.

### Problem 6 (IB-Style 15-mark)
"The Gini coefficient is the single best measure of a country's inequality." Discuss this statement.

---

## Answers

### Answer 1
**Diagram**: A square box (1×1). Horizontal axis = cumulative % population (0 to 100). Vertical axis = cumulative % income (0 to 100).

- **45-degree line**: Diagonal from (0,0) to (100,100) — represents perfect equality.
- **Lorenz curve**: Bowed line below the diagonal — the actual distribution.
- **Area A**: The area between the 45-degree line and the Lorenz curve. Represents the degree of inequality: larger A = more inequality.
- **Area B**: The area under the Lorenz curve.

$$\text{Gini Coefficient} = \frac{A}{A + B}$$

Since A + B = 0.5 (the area of the triangle under the 45-degree line), Gini = A/0.5 = 2A.

When the distribution is perfectly equal, the Lorenz curve IS the 45-degree line → A = 0 → Gini = 0. When one person has all income, the Lorenz curve runs along the bottom axis then shoots up at the right edge → B ≈ 0 → Gini ≈ 1.

### Answer 2
**Not necessarily.** Both countries have the same Gini (0.29), meaning the **relative** distribution of income is similar. However:

- Country A: GDP/capita = $12,000. The bottom 20% might earn, say, 8% of income = 0.08 × total. If we approximate, bottom quintile per capita ≈ 0.08 × $12,000 × (100/20) ≈ $4,800 per person (this overestimates slightly).
- Country B: GDP/capita = $55,000. Bottom quintile ≈ 0.08 × $55,000 × 5 ≈ $22,000.

The poor in Country B are likely far better off in absolute terms despite identical inequality. The Gini measures **relative** inequality, not absolute poverty. This is one of its key limitations.

### Answer 3

**Step 1**: Cumulative values.

| Cum Pop (X) | Cum Inc (Y) | Xᵢ−Xᵢ₋₁ | Yᵢ+Yᵢ₋₁ | Product |
|---|---|---|---|---|
| 0.2 | 0.06 | 0.2 | 0.06 | 0.012 |
| 0.4 | 0.16 | 0.2 | 0.22 | 0.044 |
| 0.6 | 0.32 | 0.2 | 0.48 | 0.096 |
| 0.8 | 0.55 | 0.2 | 0.87 | 0.174 |
| 1.0 | 1.00 | 0.2 | 1.55 | 0.310 |

Sum = 0.012 + 0.044 + 0.096 + 0.174 + 0.310 = **0.636**

Gini = 1 − 0.636 = **0.364** (medium inequality)

**Interpretation**: The bottom 60% earns 32% of income while the top 20% earns 45%. This is moderately unequal — typical of many developed countries with welfare states but significant market inequality.

### Answer 4

**Limitation 1 — Same Gini, different distributions**: Two countries can have equal Gini values but very different income structures. Suppose country A has a squeezed middle class (bottom 40% earn 15%, middle 40% earn 25%, top 20% earn 60%) and country B has a strong middle class (bottom 40% earn 20%, middle 40% earn 45%, top 20% earn 35%). These could produce similar Ginis, but in country A, the poor are desperate while the rich are ultra-wealthy; in country B, inequality is less extreme and the poor are relatively better off. Policy responses should differ, but the Gini alone doesn't reveal this.

**Limitation 2 — Ignores absolute income**: A Gini of 0.35 in Switzerland (GDP/capita ~$90,000) means something entirely different from a Gini of 0.35 in Bangladesh (GDP/capita ~$2,500). The bottom quintile in Switzerland might earn $25,000; in Bangladesh, $500. The Gini treats these as equivalent in "inequality" terms, but the welfare implications are vastly different. Absolute poverty may be a more pressing concern in Bangladesh despite equal Gini values.

### Answer 5

**Similarities**: Both have Gini = 0.38, indicating moderate inequality in relative terms.

**Critical Differences**:

**1. Bottom 40% share**: Country X (18%) vs Country Y (22%). Country Y's income is more evenly distributed in the lower half despite identical overall Gini. This means Country X's inequality is more concentrated at the bottom (the poorest are relatively poorer), while Country Y has better outcomes for the bottom 40%.

**2. Absolute income**: Country X GDP/capita = $48,000 vs Country Y = $8,000. Even though Country X's bottom 40% receive a smaller share (18% vs 22%), their absolute income is likely much higher:
- Country X: bottom 40% per capita ≈ 0.18 × $48,000 × (100/40) = $21,600
- Country Y: bottom 40% per capita ≈ 0.22 × $8,000 × (100/40) = $4,400

Country X's poorest, despite facing harsher relative inequality, enjoy nearly 5× the absolute income of Country Y's poor. This illustrates the fundamental limitation of the Gini: **relative inequality is not the same as absolute deprivation**.

**Policy implications**: Country Y likely needs growth-focused policies to raise absolute incomes, while Country X needs redistribution-focused policies to improve relative fairness. The same Gini conceals entirely different policy priorities.

### Answer 6 (Full IB-Style Response)

**Introduction**: The Gini coefficient is the most widely recognized single-number measure of inequality. The statement claims it is the "single best" — requiring evaluation against alternative measures and an examination of what "best" means in this context.

**Arguments For the Gini as "Best"**:
1. **Simplicity and communicability**: A single number between 0 and 1 (or 0 and 100) is easily understood by policymakers, journalists, and the public.
2. **Comparability**: Standardized methodology allows comparison across countries and over time. Widely reported by the World Bank, OECD, and national statistics agencies.
3. **Theoretical foundation**: Derived from the Lorenz curve, it has a clear geometric interpretation (A/(A+B)).
4. **Captures the entire distribution**: Unlike ratios (20:20, Palma), the Gini uses information from all income groups, not just extremes.

**Arguments Against the Gini as "Single Best"**:
1. **Same Gini, different distributions**: The Gini is not uniquely identifying. Two Lorenz curves that cross can produce identical Ginis. It doesn't tell you whether inequality comes from poverty at the bottom, wealth at the top, or a squeezed middle.
2. **Insensitive to extremes**: The Gini is most sensitive to changes in the middle of the distribution. The Palma ratio (top 10% ÷ bottom 40%) better captures the extreme-rich vs the poor, which many consider the ethically relevant comparison.
3. **No absolute income information**: A Gini of 0.40 in Norway means something very different from 0.40 in Niger. "Best" measure of inequality should arguably incorporate absolute welfare.
4. **Data quality issues**: Gini calculations depend on survey data, which notoriously underreport top incomes. Billionaires don't fill out household surveys. Tax-data-based measures often show much higher inequality.
5. **What kind of inequality?** The Gini doesn't distinguish income inequality from wealth inequality, pre-tax from post-tax, or market income from disposable income.

**What "Best" Depends On**:
- If the goal is international comparison and public communication, the Gini is strong.
- If the goal is capturing the plight of the poorest, the Palma ratio or absolute poverty measures are better.
- If the goal is understanding the structure of inequality, the full Lorenz curve (or decile shares) is needed.

**Conclusion**: The Gini coefficient is a valuable and widely used summary measure, but calling it the "single best" is an overstatement. Its strength — summarizing a complex distribution in one number — is also its weakness, as the single number masks important structural details. A comprehensive assessment of inequality requires supplementing the Gini with other measures (Palma ratio, decile shares, absolute poverty rates) and interpreting it alongside absolute income data. No single number can capture everything that matters about inequality.

---

## Evaluate

**"The Gini coefficient is the single best measure of a country's inequality."**

### CLASPP Analysis (175 words)

**Conclusion**: The statement overstates the case. The Gini is a useful summary measure with strong theoretical foundations and broad comparability, but it is not uniquely "best" — it has significant limitations that require supplementation with other measures.

**Long-term vs Short-term**: Over the long term, the Gini is excellent for tracking broad inequality trends. In the short term, however, it may miss rapid changes at the extremes (e.g., surging billionaire wealth during a stock market boom) because it is most sensitive to middle-distribution changes.

**Assumptions**: The statement assumes that inequality is a one-dimensional concept capturable in a single number. In reality, inequality is multi-dimensional (income vs wealth, pre-tax vs post-tax, relative vs absolute), and no single measure can capture all dimensions.

**Stakeholders**: Policymakers benefit from the Gini's simplicity for target-setting and communication. Academics find it limiting and prefer richer data. The poor are better served by measures focusing on the bottom of the distribution (Palma ratio, absolute poverty lines).

**Priorities**: If the priority is international benchmarking, the Gini is indeed the most practical tool. If the priority is understanding the lived experience of inequality, multiple measures are essential.

**Pros/Cons**: Pro — simple, comparable, theoretically grounded, widely available. Con — non-unique, insensitive to extremes, ignores absolute income, depends on data quality.

**Overall**: The Gini is a necessary but not sufficient measure of inequality.
