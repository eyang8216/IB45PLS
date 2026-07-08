# Lesson 5: Unit Conversion & Dimensional Analysis

## What You'll Learn
- The factor-label method (multiplying by clever forms of 1) for unit conversion
- Converting compound units: speed (mi/hr), density (kg/m³), rates
- Square and cubic unit conversions — the most dangerous SAT trap
- Converting between metric prefixes (kilo-, centi-, milli-)
- Handling unfamiliar units the SAT provides conversion factors for
- Setting up conversion chains without memorizing formulas

## SAT Context

Unit conversion questions appear 1-3 times per SAT. They range from straightforward (feet to inches) to deceptive (square feet to square yards). The SAT almost always provides the conversion factor (e.g., "1 mile = 5,280 feet"), so you don't need to memorize anything. What you DO need is the systematic technique for chaining conversions without getting lost. The SAT's favorite trick: square and cubic unit conversions, where the naive answer (e.g., "1 m² = 100 cm²") is always wrong and always among the answer choices. For an AAHL student, the skill is methodical setup, not mathematical difficulty.

## The Factor-Label Method (Dimensional Analysis)

### The Core Idea
Multiply by fractions that equal 1:
$$\frac{12 \text{ inches}}{1 \text{ foot}} = 1 \quad \text{and} \quad \frac{1 \text{ foot}}{12 \text{ inches}} = 1$$

Choose the version that cancels the units you want to get rid of.

### The Algorithm
1. Start with what you're given.
2. Multiply by a conversion factor (a fraction = 1) with the unit you want to CANCEL in the denominator.
3. Repeat until you reach the desired unit.
4. Multiply all numerators, divide by all denominators.

### Example: Convert 65 miles per hour to feet per second

Given: 1 mile = 5,280 ft, 1 hour = 3,600 seconds.

$$65\frac{\text{mi}}{\text{hr}} \times \frac{5280\text{ ft}}{1\text{ mi}} \times \frac{1\text{ hr}}{3600\text{ s}}$$

Cancel: mi cancels, hr cancels, leaving ft/s.

$$65 \times \frac{5280}{3600} = 65 \times 1.466... \approx 95.3 \text{ ft/s}$$

### Visual Setup for Complex Conversions

Draw a chain:

$$65\ \frac{\text{mi}}{\text{hr}} \ \times\ \frac{5280\ \text{ft}}{1\ \text{mi}} \ \times\ \frac{1\ \text{hr}}{60\ \text{min}} \ \times\ \frac{1\ \text{min}}{60\ \text{s}}$$

Each fraction is a conversion factor. Units cascade and cancel.

## Compound Units: Speed, Density, Rates

### Speed
"65 miles per hour" means $\frac{65\ \text{miles}}{1\ \text{hour}}$. The "per" creates a fraction.

### Density
"2.7 grams per cubic centimeter" means $\frac{2.7\ \text{g}}{1\ \text{cm}^3}$.

### Conversion Strategy for Compound Units
Convert numerator and denominator separately. Then combine.

**Example:** Convert 60 mi/hr to inches per second.

Step 1: Convert numerator: 60 mi → inches.
$60\ \text{mi} \times \frac{5280\ \text{ft}}{1\ \text{mi}} \times \frac{12\ \text{in}}{1\ \text{ft}} = 3,801,600\ \text{in}$

Step 2: Convert denominator: 1 hr → seconds.
$1\ \text{hr} \times \frac{60\ \text{min}}{1\ \text{hr}} \times \frac{60\ \text{s}}{1\ \text{min}} = 3,600\ \text{s}$

Step 3: Divide: $\frac{3,801,600\ \text{in}}{3,600\ \text{s}} = 1,056\ \text{in/s}$

> **🚨 SAT TRAP ALERT: Square and Cubic Unit Conversions.** This is the #1 unit conversion trap on the SAT. **1 square meter does NOT equal 100 square centimeters.** Here's why:
>
> $1\ \text{m} = 100\ \text{cm}$
>
> $(1\ \text{m})^2 = (100\ \text{cm})^2$ → $1\ \text{m}^2 = 10,000\ \text{cm}^2$
>
> $(1\ \text{m})^3 = (100\ \text{cm})^3$ → $1\ \text{m}^3 = 1,000,000\ \text{cm}^3$
>
> **The SAT WILL put $100$ and $1,000$ as answer choices for these conversions.** Don't fall for it.
>
> **Rule:** Square the conversion factor for area, cube it for volume.
> - If $1\ \text{yd} = 3\ \text{ft}$, then $1\ \text{yd}^2 = 9\ \text{ft}^2$ and $1\ \text{yd}^3 = 27\ \text{ft}^3$.
> - If $1\ \text{m} = 100\ \text{cm}$, then $1\ \text{m}^2 = 10,000\ \text{cm}^2$ and $1\ \text{m}^3 = 1,000,000\ \text{cm}^3$.

> **🔍 PATTERN RECOGNITION: When to check if units match.** If a problem mentions area (square feet, acres) or volume (cubic meters, gallons), and the answer asks for a linear measurement, or vice versa, be extra careful. Check that your conversion factor is squared or cubed appropriately. Another tell: if all the wrong answers are off by a factor of 100, 1000, or 9, it's a square/cubic unit trap.

### Worked Example 1: Simple Linear Conversion

**Problem:** A road is 3.5 miles long. What is its length in feet? (1 mile = 5,280 feet)

A) 1,760 ft
B) 15,840 ft
C) 18,480 ft
D) 22,176 ft

**Solution:**
$3.5\ \text{mi} \times \frac{5,280\ \text{ft}}{1\ \text{mi}} = 3.5 \times 5,280 = 18,480\ \text{ft}$

**Answer: C.**

**Wrong answer analysis:**
- A (1,760 ft): $5,280 / 3 \approx 1,760$, dividing instead of multiplying.
- B (15,840 ft): $3 \times 5,280 = 15,840$, forgetting the 0.5 mile.
- D (22,176 ft): $3.5 \times 5,280 \times$ something extra? Or $5,280 \times 4.2$? Unclear derivation.

### Worked Example 2: Speed Conversion with Multiple Steps

**Problem:** A cheetah runs at 70 miles per hour. Which expression gives its speed in feet per second? (1 mi = 5,280 ft)

A) $70 \times \frac{1}{5280} \times \frac{1}{3600}$
B) $70 \times \frac{5280}{1} \times \frac{3600}{1}$
C) $70 \times \frac{5280}{1} \times \frac{1}{3600}$
D) $70 \times \frac{1}{5280} \times \frac{3600}{1}$

**Solution:**
We need to convert mi to ft (multiply by 5,280) and hr to sec (divide by 3,600).

$70\ \frac{\text{mi}}{\text{hr}} \times \frac{5,280\ \text{ft}}{1\ \text{mi}} \times \frac{1\ \text{hr}}{3,600\ \text{s}} = 70 \times \frac{5,280}{1} \times \frac{1}{3,600}$

**Answer: C.**

**Wrong answer analysis:**
- A: $\frac{1}{5280}$ would divide by 5,280 instead of multiplying—gives ft⁻¹.
- B: $\frac{3600}{1}$ would multiply by 3,600 instead of dividing—gives ft·hr/s, nonsense.
- D: Both conversions inverted.

### Worked Example 3: Square Unit Trap

**Problem:** A rectangular floor measures 12 feet by 15 feet. What is the area of the floor in square yards? (1 yard = 3 feet)

A) 20 yd²
B) 60 yd²
C) 180 yd²
D) 540 yd²

**Solution:**
**Method 1** (Convert dimensions first):
- 12 ft = 12/3 = 4 yd
- 15 ft = 15/3 = 5 yd
- Area = $4 \times 5 = 20$ yd²

**Method 2** (Convert area with squared factor):
- Area in ft²: $12 \times 15 = 180$ ft²
- Since 1 yd = 3 ft, 1 yd² = 9 ft²
- $180\ \text{ft}^2 \times \frac{1\ \text{yd}^2}{9\ \text{ft}^2} = 20\ \text{yd}^2$

**Answer: A, 20 yd².**

**Wrong answer analysis:**
- B (60 yd²): $180 / 3 = 60$, using the linear conversion factor instead of squaring it. **The classic trap.**
- C (180 yd²): Forgetting to convert at all—just the area in ft².
- D (540 yd²): $180 \times 3 = 540$, multiplying by 3 instead of dividing by 9.

### Metric Prefixes Reference

The SAT expects you to know these metric prefixes. Memorize them:

| Prefix | Symbol | Factor      |
|--------|--------|-------------|
| kilo-  | k      | $10^3 = 1,000$ |
| hecto- | h      | $10^2 = 100$ |
| deka-  | da     | $10^1 = 10$ |
| *(base)* |      | $10^0 = 1$ |
| deci-  | d      | $10^{-1} = 0.1$ |
| centi- | c      | $10^{-2} = 0.01$ |
| milli- | m      | $10^{-3} = 0.001$ |

**Common SAT conversions:**
- 1 km = 1,000 m
- 1 m = 100 cm
- 1 cm = 10 mm
- 1 kg = 1,000 g
- 1 L = 1,000 mL

---

## Practice Problems

1. A car travels at 45 miles per hour. Which of the following is closest to its speed in feet per second? (1 mi = 5,280 ft)
   A) 50 ft/s
   B) 66 ft/s
   C) 85 ft/s
   D) 100 ft/s

2. A swimming pool holds 15,000 gallons of water. If 1 gallon $\approx 0.134$ cubic feet, what is the volume of the pool in cubic feet?
   A) 1,120 ft³
   B) 2,010 ft³
   C) 11,194 ft³
   D) 112,000 ft³

3. A rectangular garden is 24 feet long and 18 feet wide. What is the area of the garden in square yards? (1 yd = 3 ft)
   A) 24 yd²
   B) 48 yd²
   C) 72 yd²
   D) 432 yd²

4. A box has a volume of 2 cubic meters. What is its volume in cubic centimeters?
   A) 200 cm³
   B) 20,000 cm³
   C) 200,000 cm³
   D) 2,000,000 cm³

5. A metal block has a density of 8.0 grams per cubic centimeter. What is its density in kilograms per cubic meter? (1 kg = 1,000 g, 1 m = 100 cm)
   A) 80 kg/m³
   B) 800 kg/m³
   C) 8,000 kg/m³
   D) 80,000 kg/m³

6. **(Challenge)** Water flows through a pipe at a rate of 3 cubic feet per second. If 1 ft³ ≈ 7.48 gallons, which is closest to the flow rate in gallons per minute?
   A) 22 gal/min
   B) 134 gal/min
   C) 1,346 gal/min
   D) 8,078 gal/min

---

## Answers

1. **Answer: B.** $45 \times \frac{5280}{3600} = 45 \times \frac{22}{15} = 45 \times 1.466... = 66$ ft/s. (Simplify: $\frac{5280}{3600} = \frac{528}{360} = \frac{22}{15}$). **Wrong answers:** A (50 ft/s): rough guess, too low. C (85 ft/s): $45 \times 1.9$ or similar miscalculation. D (100 ft/s): $45 \times 2.2$, perhaps using 1 mi ≈ 8,000 ft or 1 hr ≈ 2,000 s.

2. **Answer: B.** $15,000 \times 0.134 = 2,010$ ft³. **Wrong answers:** A (1,120): $15,000 / 0.134 \approx 112,000$ — wait, dividing gives a larger number. $15,000 \times 0.134$ is correct. A might be $15,000 \times 0.0748$ (wrong factor). C (11,194): $15,000 \times 0.134 \times$ something else, or decimal point error. D (112,000): $15,000 / 0.134 \approx 111,940$, using division instead of multiplication (common trap when the factor is less than 1).

3. **Answer: B.** Method 1: 24 ft = 8 yd, 18 ft = 6 yd, area = $8 \times 6 = 48$ yd². Method 2: Area = $24 \times 18 = 432$ ft², $432 / 9 = 48$ yd². **Wrong answers:** A (24 yd²): adding dimensions? $8 + 6 + 10$? Unclear. C (72 yd²): $432 / 6 = 72$, dividing by 6 (perimeter-like) instead of 9. D (432 yd²): forgetting to convert—just reporting ft² as yd².

4. **Answer: D.** $1\ \text{m} = 100\ \text{cm}$, so $1\ \text{m}^3 = (100)^3\ \text{cm}^3 = 1,000,000\ \text{cm}^3$. $2\ \text{m}^3 = 2,000,000\ \text{cm}^3$. **Wrong answers:** A (200): $2 \times 100$, using linear factor. B (20,000): $2 \times 100^2 = 20,000$, squaring but not cubing. C (200,000): $2 \times 100,000$, off by factor of 10.

5. **Answer: C.** Convert $8.0\ \frac{\text{g}}{\text{cm}^3}$ to $\frac{\text{kg}}{\text{m}^3}$:
   $$8.0\ \frac{\text{g}}{\text{cm}^3} \times \frac{1\ \text{kg}}{1000\ \text{g}} \times \left(\frac{100\ \text{cm}}{1\ \text{m}}\right)^3 = 8.0 \times \frac{1}{1000} \times 1,000,000 = 8,000\ \frac{\text{kg}}{\text{m}^3}$$
   **Wrong answers:** A (80): misses both conversions. B (800): $8.0 \times 100 = 800$, only converting cm³→m³ once (linear). D (80,000): $8.0 \times 10,000$, off by factor of 10.

6. **Answer: C.** $3\ \frac{\text{ft}^3}{\text{s}} \times \frac{7.48\ \text{gal}}{1\ \text{ft}^3} \times \frac{60\ \text{s}}{1\ \text{min}} = 3 \times 7.48 \times 60 = 1,346.4 \approx 1,346\ \text{gal/min}$. **Wrong answers:** A (22): $3 \times 7.48 = 22.44$, forgetting the seconds→minutes conversion. B (134): $3 \times 7.48 \times 6$, using 6 instead of 60. D (8,078): $3 \times 7.48 \times 3600 / 10$, or $3 \times 7.48 \times 360$, multiplying by 360 instead of 60.
