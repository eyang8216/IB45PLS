# Lesson 50: Measuring Development (Ch 18.2)

## What You'll Learn
- The use and limitations of single indicators of development
- How composite indicators provide a more complete picture
- How to interpret and compare HDI, IHDI, MPI, and GDI values
- Strengths and weaknesses of each measurement approach

---

## 1. Single Indicators of Development

### 1.1 GDP per Capita at Purchasing Power Parity (PPP)

**GDP per capita** = total GDP ÷ population. At **PPP**, it adjusts for differences in the cost of living across countries, making comparisons more meaningful.

**Advantages**:
- Easy to calculate and compare across countries
- Correlated with many aspects of well-being (nutrition, healthcare spending)
- Data is widely available and regularly updated

**Limitations**:
- **Ignores income distribution**: a high average masks inequality (e.g., South Africa has middle-income GDP per capita but extreme inequality)
- **Excludes non-market activities**: subsistence farming, household work, and volunteer work are not counted
- **Ignores health and education**: a country may be wealthy but have poor health outcomes
- **Does not account for environmental depletion**: GDP rises when forests are cut down, but natural capital is lost
- **Exchange rate distortions**: even with PPP adjustments, measurement is imperfect

### 1.2 Health Indicators

| Indicator | What It Measures | Typical Range |
|---|---|---|
| Life expectancy at birth | Average years a newborn is expected to live | 53 (low) to 84 (high) |
| Infant mortality rate | Deaths per 1,000 live births under age 1 | <5 (developed) to >50 (least developed) |
| Maternal mortality ratio | Maternal deaths per 100,000 live births | <10 to >500 |

**Advantages**: Directly measure well-being; sensitive to quality of healthcare, nutrition, and sanitation.

**Limitations**: Only capture one dimension of development; data quality is poor in many developing countries.

### 1.3 Education Indicators

- **Adult literacy rate**: percentage of adults (15+) who can read and write
- **Mean years of schooling**: average years of education completed by adults
- **Expected years of schooling**: years a child entering school can expect to receive
- **Net enrolment rates**: percentage of school-age children enrolled

**Limitations**: Literacy rates may be self-reported and unreliable; years of schooling does not measure quality of education.

---

## 2. Composite Indicators

### 2.1 The Human Development Index (HDI)

The HDI, developed by the UNDP, combines three dimensions into a single index (0 to 1):

**Three components**:
1. **Health**: Life expectancy at birth
2. **Education**: Mean years of schooling (adults) + Expected years of schooling (children)
3. **Income**: GNI per capita at PPP (log-transformed to reflect diminishing marginal utility)

**Calculation method** (simplified):
Each component is normalized to a 0–1 scale:
$$ \text{Dimension index} = \frac{\text{Actual value} - \text{Minimum value}}{\text{Maximum value} - \text{Minimum value}} $$

The HDI is the geometric mean of the three dimension indices:
$$ \text{HDI} = (\text{Health Index} \times \text{Education Index} \times \text{Income Index})^{1/3} $$

**Worked Example — Simplified HDI calculation**:

Suppose a country has:
- Life expectancy = 70 years (min = 20, max = 85)
- Mean years of schooling = 8 years (min = 0, max = 15)
- Expected years of schooling = 12 years (min = 0, max = 18)
- GNI per capita (PPP) = $15,000 (min = $100, max = $75,000)

*Health Index* = (70 − 20) / (85 − 20) = 50/65 = 0.769

*Mean Schooling Index* = (8 − 0) / (15 − 0) = 8/15 = 0.533
*Expected Schooling Index* = (12 − 0) / (18 − 0) = 12/18 = 0.667
*Education Index* = (0.533 + 0.667) / 2 = 0.600

*Income Index* = [ln(15,000) − ln(100)] / [ln(75,000) − ln(100)]
= [9.616 − 4.605] / [11.225 − 4.605] = 5.011/6.620 = 0.757

*HDI* = (0.769 × 0.600 × 0.757)^(1/3) = (0.349)^(1/3) ≈ 0.704

**HDI Classification** (UNDP, approximate):
- Very high: ≥ 0.800
- High: 0.700–0.799
- Medium: 0.550–0.699
- Low: < 0.550

**Advantages of HDI**:
- Broader than GDP alone — captures health and education
- Enables cross-country comparisons
- Highlights that income is not the only dimension of development

**Limitations of HDI**:
- Still excludes inequality within each dimension (addressed by IHDI)
- Excludes political freedom, environmental quality, gender equality
- Data quality varies across countries
- Arbitrary weighting of the three dimensions (equal weights may not reflect true importance)

### 2.2 Inequality-Adjusted HDI (IHDI)

The IHDI adjusts the HDI downward to account for inequality in each dimension. Under perfect equality, IHDI = HDI. The larger the gap between HDI and IHDI, the greater the inequality.

**Interpretation**: If a country has HDI = 0.750 but IHDI = 0.580, it means 22.7% of potential human development is "lost" to inequality.

### 2.3 Multidimensional Poverty Index (MPI)

The MPI measures poverty at the household level across three dimensions, each with multiple indicators:

| Dimension | Indicators |
|---|---|
| Health | Child mortality, Nutrition |
| Education | Years of schooling, School attendance |
| Living Standards | Cooking fuel, Sanitation, Drinking water, Electricity, Housing, Assets |

A household is "multidimensionally poor" if it is deprived in at least **one-third** of the weighted indicators. The MPI reports both the **headcount** (percentage who are poor) and the **intensity** (average share of deprivations among the poor).

**Advantages**: Captures poverty directly at the household level, not just averages; shows *how* people are poor.

**Limitations**: Data collection is intensive; indicators may not capture all relevant deprivations (e.g., safety, freedom).

### 2.4 Gender Development Index (GDI)

The GDI is the ratio of female HDI to male HDI. A value of 1 indicates parity; below 1 indicates females are disadvantaged.

$$ \text{GDI} = \frac{\text{Female HDI}}{\text{Male HDI}} $$

Groups: GDI ≥ 0.975 (high equality); 0.950–0.974 (medium-high); 0.900–0.949 (medium); 0.850–0.899 (medium-low); <0.850 (low).

---

## 3. Comparing the Measures

| Measure | Dimensions | Accounts for Inequality? | Ease of Use |
|---|---|---|---|
| GDP per capita (PPP) | Income only | No | Very easy |
| HDI | Health, education, income | No | Moderate |
| IHDI | Health, education, income | Yes | More complex |
| MPI | Health, education, living standards | At household level | Data-intensive |
| GDI | Gender gap in HDI | Partially | Moderate |

**Key insight**: No single measure is perfect. Each captures different aspects of development. The best approach is to examine multiple indicators together.

---

## IB Exam Tip

When asked to "evaluate" a development measure, always discuss both what it captures AND what it misses. For HDI, note that it covers health, education, and income but excludes inequality, environment, and political freedom. For GDP per capita, note its narrow focus. Use concrete country examples.

---

## Practice Problems

### Problem 1
Explain two limitations of using GDP per capita (PPP) as a measure of economic development. (4 marks)

### Problem 2
A country has the following data: life expectancy = 72 years (min=20, max=85), mean years of schooling = 6 (min=0, max=15), expected years of schooling = 10 (min=0, max=18), GNI per capita PPP = $8,000 (min=$100, max=$75,000). Calculate the HDI to three decimal places. (6 marks)

### Problem 3
Country A (HDI = 0.82, IHDI = 0.64) and Country B (HDI = 0.78, IHDI = 0.75). Compare and interpret the development levels of these two countries. (4 marks)

### Problem 4
Explain how the Multidimensional Poverty Index (MPI) provides a more nuanced picture of poverty than income-based poverty lines. (5 marks)

### Problem 5
A country ranks highly on GDP per capita but moderately on HDI. Suggest two reasons for this discrepancy and explain each. (4 marks)

### Problem 6 (IB-Style)
Evaluate the view that the Human Development Index (HDI) is a sufficient measure of a country's development level. (10 marks)

---

## Answers

### Answer 1
1. **Ignores income distribution**: GDP per capita is an average that conceals inequality. A country like South Africa has relatively high GDP per capita (by developing-country standards) but extreme income inequality means that the average masks widespread poverty among the majority. Development is about well-being for all, not just the average.

2. **Excludes non-market activities**: GDP only counts market transactions. In many developing countries, subsistence agriculture, household work, and informal sector activities provide significant value that goes unmeasured. A farmer growing food for his family contributes to well-being but not to measured GDP, understating true living standards.

### Answer 2
*Health Index* = (72 − 20) / (85 − 20) = 52/65 = 0.800

*Mean Schooling Index* = (6 − 0) / (15 − 0) = 6/15 = 0.400
*Expected Schooling Index* = (10 − 0) / (18 − 0) = 10/18 = 0.556
*Education Index* = (0.400 + 0.556) / 2 = 0.478

*Income Index* = [ln(8,000) − ln(100)] / [ln(75,000) − ln(100)]
= [8.987 − 4.605] / [11.225 − 4.605]
= 4.382/6.620 = 0.662

*HDI* = (0.800 × 0.478 × 0.662)^(1/3) = (0.253)^(1/3) ≈ 0.633

The country has a **medium** level of human development.

### Answer 3
Country A has a higher HDI (0.82 vs 0.78), suggesting higher overall human development. However, Country A's IHDI is only 0.64 — a "loss" of 22% of potential development due to inequality. Country B's IHDI (0.75) is only slightly below its HDI (0.78), a loss of 3.8%. This means Country B distributes its health, education, and income achievements much more equally than Country A. While Country A has higher *average* achievement, the typical person in Country B may experience better development outcomes because inequality is lower. This demonstrates why HDI alone can be misleading — it ignores how achievements are shared.

### Answer 4
The MPI provides a more nuanced picture than income-based poverty measures for several reasons:

1. **Multidimensional**: Income poverty lines only capture whether a household has enough money. The MPI captures whether households actually experience deprivations in health (nutrition, child mortality), education (years of schooling, attendance), and living standards (water, sanitation, electricity, etc.).

2. **Direct measurement of outcomes**: A household may have income above the poverty line but still lack access to clean water, adequate nutrition, or education — the MPI captures this directly.

3. **Intensity measure**: The MPI reports not just *how many* are poor (headcount) but *how poor* they are (intensity — the average share of deprivations). This allows policymakers to distinguish between mildly and severely poor populations and target interventions accordingly.

### Answer 5
**Reason 1 — Resource extraction economy**: The country may derive high GDP from capital-intensive oil or mineral extraction (e.g., Equatorial Guinea, Saudi Arabia in earlier decades). This generates high income but employs few people and may not translate into broad-based improvements in health and education, resulting in a lower HDI relative to GDP rank.

**Reason 2 — Unequal distribution of income**: High GDP per capita may mask extreme inequality. If a wealthy elite captures most of the income while the majority lacks access to quality healthcare and education, the HDI (which uses average life expectancy and schooling) will be pulled down, creating a gap between the GDP and HDI rankings.

### Answer 6
**Introduction**: The HDI is a significant improvement over GDP-only measures by incorporating health and education alongside income. However, whether it is "sufficient" depends on what aspects of development are being evaluated.

**Arguments for sufficiency**:
- Captures three core dimensions — health, education, and income — that are fundamental to human well-being.
- Enables transparent, comparable rankings across countries.
- Simplicity aids policy communication and goal-setting.

**Arguments against sufficiency**:
- **Omits inequality** within each dimension — a country can have a high HDI while large segments of the population are deprived (addressed by IHDI).
- **Excludes political freedom** and human rights — a country could have high HDI but be authoritarian.
- **Ignores environmental sustainability** — development that is unsustainable is not genuine development. Norway ranks differently from Qatar when sustainability is considered.
- **No gender dimension** — the GDI complements HDI but is not part of it.
- **Arbitrary weights**: the three dimensions are equally weighted, which may not reflect their true relative importance.

**Conclusion**: The HDI is a useful summary measure but is not sufficient on its own. A thorough assessment of development requires complementary indicators: IHDI for inequality, MPI for poverty depth, GDI for gender, and environmental indicators for sustainability. The HDI is best used as a starting point, not a definitive judgment.

---

## Evaluate

**Question**: "The HDI is a sufficient measure of a country's development level."

**CLASPP Model Answer (195 words)**:

**Conclusion**: The HDI is a valuable but insufficient measure of development. It improves on GDP per capita by including health and education, but it misses several critical dimensions that a complete assessment of development requires.

**Logic and assumptions**: The claim assumes that income, health, and education — equally weighted — capture all that matters for development. This overlooks inequality, sustainability, and political freedoms as dimensions of human well-being.

**Advantages**: The HDI's three dimensions are undeniably central to development. It is transparent, widely available, and allows meaningful cross-country comparisons. For policymakers, it communicates that GDP is not the only goal.

**Disadvantages / Limitations**: The HDI ignores inequality (addressed separately by IHDI), environmental degradation, political freedom, and gender disparities. A country like Qatar has a very high HDI but relies on unsustainable resource extraction and has limited political freedoms. The equal weighting of the three components is also arbitrary.

**Stakeholders**: Ordinary citizens whose deprivations are masked by averages are poorly served by HDI alone. Governments may focus on raising HDI while neglecting excluded dimensions. International organisations need richer data for effective aid allocation.

**Preconditions for sufficiency**: The HDI would only be sufficient if inequality and environmental impacts were negligible — which is rarely true.

**Priorities**: Development assessment should use HDI alongside IHDI (for inequality), MPI (for poverty depth), and environmental indicators, forming a dashboard rather than relying on any single number.

---

## Key Terms

| Term | Definition |
|---|---|
| GDP per capita (PPP) | Total GDP divided by population, adjusted for cost-of-living differences |
| Life expectancy at birth | Average number of years a newborn is expected to live |
| Infant mortality rate | Deaths per 1,000 live births under age 1 |
| HDI | Composite index combining income, health, and education (0 to 1) |
| IHDI | HDI adjusted downward to account for inequality in each dimension |
| MPI | Measures poverty across health, education, and living standards at household level |
| GDI | Ratio of female HDI to male HDI; measures gender disparity |
| Geometric mean | The nth root of the product of n numbers; used to compute HDI |

---

## Summary

No single indicator perfectly captures development. GDP per capita is easy to compute and compare but ignores health, education, and inequality. Health and education indicators capture vital dimensions but are narrow. Composite indicators like the HDI represent a significant improvement by combining income, health, and education into a single measure. However, the HDI still omits inequality (addressed by IHDI), poverty depth (MPI), gender (GDI), and environmental sustainability. A comprehensive assessment of development requires examining multiple indicators together — a dashboard approach rather than reliance on any single number. For IB exam purposes, the HDI is the most important composite measure to understand in detail, including its calculation logic and limitations.
