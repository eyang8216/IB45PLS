# Lesson 25: Kc Calculations — ICE Tables and Exam Technique

## What You'll Learn
- Set up and systematically solve ICE (Initial, Change, Equilibrium) tables for equilibrium problems
- Calculate equilibrium concentrations when given initial amounts and Kc
- Calculate Kc from equilibrium composition data
- Handle stoichiometric coefficients correctly in the change row of an ICE table
- Recognise and avoid the most common mistakes students make in equilibrium calculations

---

## 1. The ICE Table Method

### What This Concept Is and Why It Matters

When you know the amount of each substance you start with, and you know the value of the equilibrium constant Kc, you can calculate exactly what the concentrations will be at equilibrium. But equilibrium calculations are not as straightforward as just plugging numbers into the Kc formula, because the equilibrium concentrations are what you are trying to find — they are not given to you directly.

The ICE table is a structured, systematic method for organising this kind of problem. The letters stand for **I**nitial concentration, **C**hange in concentration, and **E**quilibrium concentration. By setting up rows for each species and columns for I, C, and E, you turn a confusing algebra problem into a clear, step-by-step procedure.

### The Step-by-Step Procedure

Follow these steps in order, every time. Do not skip any step.

**Step 1: Write the balanced chemical equation.** Everything depends on the stoichiometric coefficients being correct. Double-check that the equation is balanced.

**Step 2: Set up the ICE table.** Draw a table with rows for Initial, Change, and Equilibrium. Make columns for each gaseous and aqueous species in the reaction. (Do not include solids or pure liquids — they do not appear in Kc.)

**Step 3: Fill in the Initial row.** Enter the initial concentrations of all species. If you are given amounts in moles and a volume in dm³, convert to concentration by dividing moles by volume: concentration = n/V. If a species is not present initially, its initial concentration is zero.

**Step 4: Express the Change row using the variable x.** Reactants are consumed, so their Change entries are negative (e.g., −x, −2x, −3x). Products are formed, so their Change entries are positive (e.g., +x, +2x, +3x). The coefficient in front of x must match the stoichiometric coefficient from the balanced equation. For example, if the balanced equation has 2A → B, then the change for A is −2x and the change for B is +x.

**Step 5: Write the Equilibrium row.** For each species, add the Initial and Change entries: Equilibrium = Initial + Change.

**Step 6: Substitute the Equilibrium expressions into the Kc expression.** Write the Kc expression and replace each concentration with the algebraic expression from the Equilibrium row.

**Step 7: Solve for x.** This usually involves algebra — sometimes a simple square root, sometimes a quadratic equation. If Kc is very small (less than about 10⁻³), you may be able to make an approximation (assume x is negligible compared to the initial concentration), but always check that the approximation is valid (x should be less than 5% of the initial concentration).

**Step 8: Calculate all equilibrium concentrations.** Plug the value of x back into the expressions in the Equilibrium row.

**Step 9: Check your work.** Substitute your calculated equilibrium concentrations back into the Kc expression and verify that you get the given value of Kc. If you do not, you made an error.

---

## 2. Example 1: H₂ + I₂ ⇌ 2HI (Equal Moles on Each Side)

### Worked Example 1

**Problem:** The reaction H₂(g) + I₂(g) ⇌ 2HI(g) has an equilibrium constant Kc = 49 at a certain temperature. A chemist places 1.0 mole of H₂ gas and 1.0 mole of I₂ gas into a sealed container with a volume of 1.0 dm³. No HI is present initially. Calculate the equilibrium concentrations of all three species.

**Strategy:** We will set up an ICE table. Since the volume is 1.0 dm³, the initial concentrations in mol dm⁻³ are numerically equal to the moles. We let x represent the amount of H₂ that reacts (in mol dm⁻³). The stoichiometry then determines all other changes.

**Solution:**

**Step 1:** The equation is H₂(g) + I₂(g) ⇌ 2HI(g). It is already balanced.

**Step 2-5:** Build the ICE table.

| Species | H₂ | I₂ | HI |
|---------|----|----|-----|
| **I**nitial / mol dm⁻³ | 1.0 | 1.0 | 0 |
| **C**hange / mol dm⁻³ | −x | −x | +2x |
| **E**quilibrium / mol dm⁻³ | 1.0 − x | 1.0 − x | 2x |

Why is the change for HI +2x? Because the coefficient of HI in the balanced equation is 2. For every 1 molecule of H₂ that reacts (our −x), 2 molecules of HI are formed. So the change in [HI] is twice as large.

**Step 6:** Write the Kc expression and substitute:

\[
K_c = \frac{[\text{HI}]^2}{[\text{H}_2][\text{I}_2]} = \frac{(2x)^2}{(1.0 - x)(1.0 - x)} = 49
\]

\[
\frac{4x^2}{(1.0 - x)^2} = 49
\]

**Step 7:** Because both sides are perfect squares, we can take the square root of both sides. This is only possible because the numerator is a square (4x² = (2x)²) and the denominator is a square ((1.0 − x)²). Taking the square root:

\[
\frac{2x}{1.0 - x} = 7
\]

(We take the positive root, 7, because concentrations must be positive. The negative root, −7, is mathematically valid but chemically meaningless — it would give a negative value for x, which would mean a negative concentration.)

Now solve for x:

\[
2x = 7(1.0 - x)
\]

\[
2x = 7.0 - 7x
\]

\[
2x + 7x = 7.0
\]

\[
9x = 7.0
\]

\[
x = \frac{7.0}{9} = 0.778 \text{ mol dm}^{-3}
\]

**Step 8:** Calculate the equilibrium concentrations:

[H₂] = 1.0 − 0.778 = 0.222 mol dm⁻³ (approximately 0.22 mol dm⁻³)

[I₂] = 1.0 − 0.778 = 0.222 mol dm⁻³ (same as H₂, as expected from symmetry)

[HI] = 2 × 0.778 = 1.556 mol dm⁻³ (approximately 1.6 mol dm⁻³)

**Step 9:** Check:

\[
K_c = \frac{(1.556)^2}{(0.222)(0.222)} = \frac{2.421}{0.0493} = 49.1 \approx 49
\]

The small difference is due to rounding. The answer is verified.

**Why this makes sense:** We started with equal amounts of the two reactants, and the stoichiometry uses them in a 1:1 ratio. So they should have equal concentrations at equilibrium. Also, Kc = 49 is fairly large, so most but not all of the reactants should be converted to products. Our result shows about 78% conversion, which is consistent with Kc = 49.

---

## 3. Example 2: N₂O₄ ⇌ 2NO₂ (One Reactant Dissociating)

### Worked Example 2

**Problem:** Dinitrogen tetroxide gas, N₂O₄, partially dissociates into nitrogen dioxide gas, NO₂, according to the equilibrium N₂O₄(g) ⇌ 2NO₂(g). At 373 K, the equilibrium constant Kc for this reaction is 0.36. A chemist places 2.0 moles of pure N₂O₄ gas into a container with a volume of 5.0 dm³. No NO₂ is present initially. Calculate the equilibrium concentrations of N₂O₄ and NO₂.

**Strategy:** This is similar to the previous example, but there are two important differences. First, the stoichiometric coefficients are different (1 and 2 instead of 1 and 1 and 2). Second, taking a square root will not simplify the algebra because the denominator is (0.40 − x), not (0.40 − x)². We will need to solve a quadratic equation.

**Solution:**

**Step 3:** Calculate initial concentrations. [N₂O₄]₀ = moles/volume = 2.0 mol / 5.0 dm³ = 0.40 mol dm⁻³. [NO₂]₀ = 0.

**Steps 2-5:** Build the ICE table.

| Species | N₂O₄ | NO₂ |
|---------|------|-----|
| **I**nitial / mol dm⁻³ | 0.40 | 0 |
| **C**hange / mol dm⁻³ | −x | +2x |
| **E**quilibrium / mol dm⁻³ | 0.40 − x | 2x |

**Step 6:** Write the Kc expression and substitute:

\[
K_c = \frac{[\text{NO}_2]^2}{[\text{N}_2\text{O}_4]} = \frac{(2x)^2}{0.40 - x} = 0.36
\]

\[
\frac{4x^2}{0.40 - x} = 0.36
\]

**Step 7:** Multiply both sides by (0.40 − x):

\[
4x^2 = 0.36(0.40 - x)
\]

\[
4x^2 = 0.144 - 0.36x
\]

Bring all terms to one side to form a quadratic equation:

\[
4x^2 + 0.36x - 0.144 = 0
\]

To make the numbers easier to work with, multiply the entire equation by 100:

\[
400x^2 + 36x - 14.4 = 0
\]

Use the quadratic formula: for ax² + bx + c = 0,

\[
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\]

where a = 400, b = 36, c = −14.4.

\[
x = \frac{-36 \pm \sqrt{36^2 - 4(400)(-14.4)}}{2(400)}
\]

\[
x = \frac{-36 \pm \sqrt{1296 + 23040}}{800}
\]

\[
x = \frac{-36 \pm \sqrt{24336}}{800}
\]

\[
x = \frac{-36 \pm 156}{800}
\]

This gives two possible values for x:

x = (−36 + 156) / 800 = 120 / 800 = 0.15

x = (−36 − 156) / 800 = −192 / 800 = −0.24

The negative value would give a negative concentration of NO₂ (since [NO₂] = 2x), which is chemically impossible. We take the positive root: **x = 0.15 mol dm⁻³**.

**Step 8:** Calculate equilibrium concentrations:

[N₂O₄] = 0.40 − 0.15 = 0.25 mol dm⁻³

[NO₂] = 2 × 0.15 = 0.30 mol dm⁻³

**Step 9:** Check:

\[
K_c = \frac{(0.30)^2}{0.25} = \frac{0.090}{0.25} = 0.36
\]

This matches the given Kc exactly.

**Why this makes sense:** Kc = 0.36 is less than 1, so the equilibrium should favour the reactant N₂O₄ somewhat. Our results show [N₂O₄] = 0.25 and [NO₂] = 0.30, which means there is slightly more NO₂ than N₂O₄ in terms of concentration, but the squared term in the numerator means the equilibrium still favours the reactant side overall.

---

## 4. Example 3: Esterification (Equal Moles on Both Sides)

### Worked Example 3

**Problem:** The esterification reaction between ethanoic acid and ethanol produces ethyl ethanoate and water:

\[
\text{CH}_3\text{COOH}(\text{l}) + \text{C}_2\text{H}_5\text{OH}(\text{l}) \rightleftharpoons \text{CH}_3\text{COOC}_2\text{H}_5(\text{l}) + \text{H}_2\text{O}(\text{l})
\]

At a certain temperature, the equilibrium constant Kc for this reaction is 4.0. All four species are liquids, but none is the solvent in vast excess, so all appear in the Kc expression. Initially, 1.0 mole of ethanoic acid and 1.0 mole of ethanol are mixed in a container of volume V dm³. No ester and no water are present initially. Calculate the equilibrium amount of ester in moles.

**Strategy:** Since the total volume V is the same for all species and cancels out in the Kc expression, we can work directly with amounts in moles. We let x be the number of moles of acid that react.

**Solution:**

**Step 2-5:** Build the ICE table using moles (the volume will cancel later).

| Species | CH₃COOH | C₂H₅OH | CH₃COOC₂H₅ | H₂O |
|----------|---------|--------|-------------|-----|
| **I**nitial / mol | 1.0 | 1.0 | 0 | 0 |
| **C**hange / mol | −x | −x | +x | +x |
| **E**quilibrium / mol | 1.0 − x | 1.0 − x | x | x |

**Step 6:** Write the Kc expression. The concentration of each species is its amount in moles divided by the volume V:

\[
K_c = \frac{[\text{ester}][\text{H}_2\text{O}]}{[\text{acid}][\text{alcohol}]} = \frac{(x/V)(x/V)}{((1.0-x)/V)((1.0-x)/V)}
\]

All the V terms cancel out, so we can work entirely with moles:

\[
K_c = \frac{x \cdot x}{(1.0 - x)(1.0 - x)} = \frac{x^2}{(1.0 - x)^2} = 4.0
\]

**Step 7:** Take the square root of both sides:

\[
\frac{x}{1.0 - x} = 2.0
\]

\[
x = 2.0(1.0 - x)
\]

\[
x = 2.0 - 2.0x
\]

\[
3.0x = 2.0
\]

\[
x = \frac{2.0}{3.0} = 0.67 \text{ mol}
\]

**Step 8:** The equilibrium amount of ester is x = **0.67 mol**.

**Why this makes sense:** Kc = 4.0 means products are favoured, and with equal starting amounts of both reactants, we expect more than half but not all to be converted. Our result shows that 67% of the acid (and alcohol) has been converted to ester.

---

## 5. Common Pitfalls and How to Avoid Them

### Pitfall 1: Forgetting to Convert Moles to Concentration

If you are given moles of a substance and the volume of the container, you must divide moles by volume to get concentration (in mol dm⁻³) before entering values into the ICE table. The Kc expression uses concentrations, not amounts. The only exception is when the volume cancels out — which happens only when there are equal numbers of moles on both sides of the equation after the stoichiometric coefficients are counted. When in doubt, always convert to concentration.

### Pitfall 2: Getting the Signs Wrong in the Change Row

Reactants are consumed, so their Change row entries are always negative (e.g., −x, −2x). Products are produced, so their Change row entries are always positive (e.g., +x, +2x). If you put +x for a reactant, your algebra will give nonsensical results. Always check: is this species being used up or being made?

### Pitfall 3: Missing Stoichiometric Coefficients in the Change Row

The number in front of x in the Change row must match the stoichiometric coefficient from the balanced equation. For the reaction 2A → B, the change for A is −2x (coefficient 2) and the change for B is +x (coefficient 1). A common mistake is to write −x for A because "one x represents one unit of reaction." In fact, one unit of reaction consumes two A particles.

### Pitfall 4: Solving a Quadratic Equation Incorrectly

When you get two roots from the quadratic formula, one will usually give a negative concentration (and should be discarded). Always check both roots against the physical constraints: all concentrations must be positive, and x cannot be larger than the initial concentration of any reactant.

### Pitfall 5: Not Checking Your Answer

After you have calculated all equilibrium concentrations, substitute them back into the Kc expression. If the value you get is not reasonably close to the given Kc, you made a mistake somewhere. This simple check takes 30 seconds and catches most errors.

### Pitfall 6: Including Solids or Pure Liquids

Remember that solids (s) and pure liquids (l) do not appear in the Kc expression. Do not include columns for them in the ICE table when you are substituting into Kc. You may include them in the table for your own tracking, but do not use their concentrations in the Kc expression.

---

## Practice Problems

1. For the equilibrium CO(g) + H₂O(g) ⇌ CO₂(g) + H₂(g), the equilibrium constant Kc has the value 1.0 at 1100 K. Initially, the concentrations of CO and H₂O are both 2.0 mol dm⁻³, and no CO₂ or H₂ is present. Construct a complete ICE table for this reaction and calculate the equilibrium concentrations of all four species.

2. Phosphorus pentachloride decomposes according to the equilibrium PCl₅(g) ⇌ PCl₃(g) + Cl₂(g). At 500 K, the equilibrium constant Kc for this decomposition is 0.042. A chemist places 0.50 moles of pure PCl₅ gas into a container with a volume of 2.0 dm³. Construct an ICE table and calculate the equilibrium concentrations of all three species. Solve the resulting quadratic equation, showing each step of your algebra.

3. The oxidation of sulfur dioxide to sulfur trioxide reaches equilibrium according to the equation 2SO₂(g) + O₂(g) ⇌ 2SO₃(g). In a container with volume 2.0 dm³ at a certain temperature, the equilibrium mixture is found to contain 0.060 moles of SO₂, 0.040 moles of O₂, and 0.080 moles of SO₃. Calculate the value of the equilibrium constant Kc.

4. For the reaction N₂(g) + 3H₂(g) ⇌ 2NH₃(g), the equilibrium constant Kc has the value 0.50 at a certain temperature. Initially, the concentrations are [N₂] = 1.0 mol dm⁻³ and [H₂] = 3.0 mol dm⁻³, with no NH₃ present. Construct the ICE table and write the equilibrium concentrations in terms of x. Write the full Kc equation in terms of x. Do not solve the equation — the algebra is complex — but simplify it as much as possible.

5. **(IB-Exam Style)** Hydrogen iodide decomposes according to the equilibrium:

   \[
   2\text{HI}(\text{g}) \rightleftharpoons \text{H}_2(\text{g}) + \text{I}_2(\text{g})
   \]

   A chemist places 0.40 moles of pure HI gas into a sealed container with a volume of 2.0 dm³ at a temperature of 700 K. The system is allowed to reach equilibrium. At equilibrium, analysis shows that 0.10 moles of HI remain in the container.

   (a) Calculate the initial concentration of HI in mol dm⁻³.

   (b) Calculate the amount (in moles) of HI that has reacted.

   (c) Using the stoichiometry of the balanced equation, determine the amounts (in moles) of H₂ and I₂ that have been formed at equilibrium.

   (d) Convert all equilibrium amounts to concentrations in mol dm⁻³ and calculate the value of Kc at 700 K.

   (e) In a second experiment at the same temperature, the chemist starts with 0.20 moles of H₂ and 0.20 moles of I₂ in the same 2.0 dm³ container, with no HI present initially. Use the value of Kc from part (d) to calculate the equilibrium concentration of HI in this second experiment. Set up an ICE table and solve for the unknown.

---

## Answers

### Answer 1

The balanced equation is CO + H₂O ⇌ CO₂ + H₂. Since all coefficients are 1, the ICE table is straightforward.

| Species | CO | H₂O | CO₂ | H₂ |
|----------|-----|------|------|-----|
| **I**nitial / mol dm⁻³ | 2.0 | 2.0 | 0 | 0 |
| **C**hange / mol dm⁻³ | −x | −x | +x | +x |
| **E**quilibrium / mol dm⁻³ | 2.0 − x | 2.0 − x | x | x |

Kc = [CO₂][H₂] / ([CO][H₂O]) = x² / (2.0 − x)² = 1.0.

Taking the square root: x / (2.0 − x) = 1.0.

x = 2.0 − x → 2x = 2.0 → x = 1.0.

All equilibrium concentrations are: [CO] = [H₂O] = [CO₂] = [H₂] = **1.0 mol dm⁻³**.

This makes sense: Kc = 1.0 means neither side is favoured, and with equal starting amounts and 1:1 stoichiometry, exactly half of each reactant is converted at equilibrium.

### Answer 2

**Step 1:** Initial concentration of PCl₅: [PCl₅]₀ = 0.50 mol / 2.0 dm³ = 0.25 mol dm⁻³.

| Species | PCl₅ | PCl₃ | Cl₂ |
|---------|------|------|-----|
| **I**nitial / mol dm⁻³ | 0.25 | 0 | 0 |
| **C**hange / mol dm⁻³ | −x | +x | +x |
| **E**quilibrium / mol dm⁻³ | 0.25 − x | x | x |

Kc = [PCl₃][Cl₂] / [PCl₅] = x² / (0.25 − x) = 0.042.

x² = 0.042(0.25 − x) = 0.0105 − 0.042x.

x² + 0.042x − 0.0105 = 0.

Using the quadratic formula with a = 1, b = 0.042, c = −0.0105:

x = [−0.042 ± √(0.042² − 4(1)(−0.0105))] / 2 = [−0.042 ± √(0.001764 + 0.042)] / 2 = [−0.042 ± √0.043764] / 2 = [−0.042 ± 0.2092] / 2.

Positive root: x = (−0.042 + 0.2092) / 2 = 0.1672 / 2 = 0.0836.

Negative root is chemically impossible.

Equilibrium concentrations: [PCl₅] = 0.25 − 0.0836 = 0.1664 ≈ **0.17 mol dm⁻³**, [PCl₃] = [Cl₂] = **0.084 mol dm⁻³** (approximately, to two significant figures).

### Answer 3

First, convert all amounts to concentrations by dividing by the volume (2.0 dm³):

[SO₂] = 0.060 / 2.0 = 0.030 mol dm⁻³

[O₂] = 0.040 / 2.0 = 0.020 mol dm⁻³

[SO₃] = 0.080 / 2.0 = 0.040 mol dm⁻³

Kc = [SO₃]² / ([SO₂]²[O₂]) = (0.040)² / ((0.030)² (0.020)) = 0.0016 / (0.0009 × 0.020) = 0.0016 / 0.000018 = 88.89 ≈ **89**.

### Answer 4

| Species | N₂ | H₂ | NH₃ |
|---------|-----|------|------|
| **I**nitial / mol dm⁻³ | 1.0 | 3.0 | 0 |
| **C**hange / mol dm⁻³ | −x | −3x | +2x |
| **E**quilibrium / mol dm⁻³ | 1.0 − x | 3.0 − 3x | 2x |

Note carefully the change for H₂ is −3x (coefficient 3) and for NH₃ is +2x (coefficient 2).

Kc = [NH₃]² / ([N₂][H₂]³) = (2x)² / [(1.0 − x)(3.0 − 3x)³] = 0.50.

Simplify: (3.0 − 3x) = 3(1.0 − x), so (3.0 − 3x)³ = 27(1.0 − x)³.

The Kc expression becomes: 4x² / [(1.0 − x) × 27(1.0 − x)³] = 4x² / [27(1.0 − x)⁴] = 0.50.

This is the simplified form. Solving it would involve expanding (1.0 − x)⁴, which leads to a quartic equation — beyond what is expected in IB, but the setup is the critical skill.

### Answer 5

**(a)** Initial [HI] = moles / volume = 0.40 mol / 2.0 dm³ = **0.20 mol dm⁻³**.

**(b)** Amount of HI that reacted = initial amount − equilibrium amount = 0.40 − 0.10 = **0.30 moles**.

**(c)** From the balanced equation 2HI ⇌ H₂ + I₂, for every 2 moles of HI that decompose, 1 mole of H₂ and 1 mole of I₂ are formed. Since 0.30 moles of HI decomposed, the amount of H₂ formed = 0.30 / 2 = 0.15 moles, and the amount of I₂ formed is also **0.15 moles**.

**(d)** Equilibrium concentrations in mol dm⁻³:

[HI] = 0.10 mol / 2.0 dm³ = 0.050 mol dm⁻³

[H₂] = 0.15 mol / 2.0 dm³ = 0.075 mol dm⁻³

[I₂] = 0.15 mol / 2.0 dm³ = 0.075 mol dm⁻³

Kc = [H₂][I₂] / [HI]² = (0.075)(0.075) / (0.050)² = 0.005625 / 0.0025 = **2.25**.

**(e)** In the second experiment, initial concentrations: [H₂] = [I₂] = 0.20 / 2.0 = 0.10 mol dm⁻³, [HI] = 0. The reaction must proceed in reverse: H₂ + I₂ → 2HI.

| Species | H₂ | I₂ | HI |
|---------|-----|------|------|
| **I**nitial / mol dm⁻³ | 0.10 | 0.10 | 0 |
| **C**hange / mol dm⁻³ | −x | −x | +2x |
| **E**quilibrium / mol dm⁻³ | 0.10 − x | 0.10 − x | 2x |

Kc = [H₂][I₂] / [HI]² = 2.25 (using the same Kc as the forward reaction 2HI ⇌ H₂ + I₂).

2.25 = (0.10 − x)(0.10 − x) / (2x)² = (0.10 − x)² / 4x².

Take the square root: √2.25 = 1.5 = (0.10 − x) / (2x).

1.5 = (0.10 − x) / (2x).

3.0x = 0.10 − x.

4.0x = 0.10.

x = 0.025.

Equilibrium [HI] = 2x = 2 × 0.025 = **0.050 mol dm⁻³**.

This is exactly the same [HI] as in part (d) — starting from the opposite side at the same temperature leads to the same equilibrium concentrations, confirming that Kc is a true constant.
